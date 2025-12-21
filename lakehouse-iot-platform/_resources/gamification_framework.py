"""
Gamification Framework for GenAI Learning Path
==============================================
This module provides badge tracking, level progression, and validation utilities
for the interactive learning experience.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class Badge:
    """Represents a learning achievement badge"""
    
    BADGES = {
        "first_agent": {
            "name": "🤖 First Agent",
            "description": "Successfully deployed your first AI Agent",
            "points": 100,
            "criteria": "Deploy an agent to Model Serving"
        },
        "prompt_master": {
            "name": "📝 Prompt Master",
            "description": "Created an optimized system prompt",
            "points": 150,
            "criteria": "Agent response quality > 85%"
        },
        "tool_builder": {
            "name": "🔧 Tool Builder",
            "description": "Developed a custom AI Tool",
            "points": 200,
            "criteria": "Create and register a UC function"
        },
        "performance_optimizer": {
            "name": "⚡ Performance Optimizer",
            "description": "Optimized agent latency under 2s",
            "points": 250,
            "criteria": "Agent avg response time < 2000ms"
        },
        "rag_expert": {
            "name": "🔍 RAG Expert",
            "description": "Mastered Retrieval Augmented Generation",
            "points": 300,
            "criteria": "Implement custom RAG with >90% relevance"
        },
        "multi_agent_architect": {
            "name": "🏗️ Multi-Agent Architect",
            "description": "Built a multi-agent orchestration system",
            "points": 400,
            "criteria": "Deploy coordinated multi-agent system"
        },
        "debugging_hero": {
            "name": "🐛 Debugging Hero",
            "description": "Fixed all challenge bugs successfully",
            "points": 150,
            "criteria": "Complete all debugging challenges"
        },
        "cost_optimizer": {
            "name": "💰 Cost Optimizer",
            "description": "Reduced agent costs by 50%",
            "points": 200,
            "criteria": "Optimize token usage and model selection"
        },
        "security_champion": {
            "name": "🛡️ Security Champion",
            "description": "Implemented secure agent patterns",
            "points": 250,
            "criteria": "Pass all security validation checks"
        },
        "genai_master": {
            "name": "🎓 GenAI Master",
            "description": "Completed all GenAI modules",
            "points": 1000,
            "criteria": "Earn all other badges"
        }
    }
    
    @classmethod
    def get_badge_info(cls, badge_id: str) -> Dict:
        return cls.BADGES.get(badge_id, {})
    
    @classmethod
    def list_all_badges(cls) -> List[Dict]:
        return [{"id": k, **v} for k, v in cls.BADGES.items()]


class LearningLevel:
    """Manages learning progression levels"""
    
    LEVELS = {
        1: {"name": "Beginner", "points_required": 0, "color": "🟢"},
        2: {"name": "Intermediate", "points_required": 500, "color": "🔵"},
        3: {"name": "Advanced", "points_required": 1500, "color": "🟣"},
        4: {"name": "Expert", "points_required": 3000, "color": "🟠"},
        5: {"name": "Master", "points_required": 5000, "color": "🔴"}
    }
    
    @classmethod
    def get_level(cls, total_points: int) -> Dict:
        """Calculate current level based on points"""
        current_level = 1
        for level, info in cls.LEVELS.items():
            if total_points >= info["points_required"]:
                current_level = level
        return {"level": current_level, **cls.LEVELS[current_level]}
    
    @classmethod
    def points_to_next_level(cls, total_points: int) -> int:
        """Calculate points needed for next level"""
        current_level_num = cls.get_level(total_points)["level"]
        if current_level_num >= max(cls.LEVELS.keys()):
            return 0  # Max level reached
        next_level = cls.LEVELS[current_level_num + 1]
        return next_level["points_required"] - total_points


class LearnerProgress:
    """Tracks individual learner progress"""
    
    def __init__(self, learner_id: str):
        self.learner_id = learner_id
        self.progress_file = Path(f"/tmp/learner_progress_{learner_id}.json")
        self.data = self._load_progress()
    
    def _load_progress(self) -> Dict:
        """Load progress from file or create new"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            "learner_id": self.learner_id,
            "earned_badges": [],
            "completed_challenges": [],
            "total_points": 0,
            "started_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat()
        }
    
    def _save_progress(self):
        """Save progress to file"""
        self.data["last_activity"] = datetime.now().isoformat()
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def award_badge(self, badge_id: str):
        """Award a badge to the learner"""
        if badge_id not in self.data["earned_badges"]:
            badge_info = Badge.get_badge_info(badge_id)
            self.data["earned_badges"].append(badge_id)
            self.data["total_points"] += badge_info.get("points", 0)
            self._save_progress()
            return True
        return False
    
    def complete_challenge(self, challenge_id: str, points: int = 50):
        """Mark a challenge as completed"""
        if challenge_id not in self.data["completed_challenges"]:
            self.data["completed_challenges"].append(challenge_id)
            self.data["total_points"] += points
            self._save_progress()
            return True
        return False
    
    def get_summary(self) -> Dict:
        """Get learner progress summary"""
        level_info = LearningLevel.get_level(self.data["total_points"])
        return {
            "learner_id": self.learner_id,
            "level": level_info,
            "total_points": self.data["total_points"],
            "points_to_next_level": LearningLevel.points_to_next_level(self.data["total_points"]),
            "badges_earned": len(self.data["earned_badges"]),
            "total_badges": len(Badge.BADGES),
            "challenges_completed": len(self.data["completed_challenges"]),
            "badge_details": [Badge.get_badge_info(b) for b in self.data["earned_badges"]]
        }
    
    def display_progress(self):
        """Display formatted progress"""
        summary = self.get_summary()
        level = summary["level"]
        
        print("=" * 60)
        print(f"🎓 GenAI Learning Progress - {self.learner_id}")
        print("=" * 60)
        print(f"\n{level['color']} Level {level['level']}: {level['name']}")
        print(f"📊 Total Points: {summary['total_points']}")
        print(f"⬆️  Points to Next Level: {summary['points_to_next_level']}")
        print(f"\n🏅 Badges Earned: {summary['badges_earned']}/{summary['total_badges']}")
        
        if summary["badge_details"]:
            print("\nYour Badges:")
            for badge in summary["badge_details"]:
                print(f"  {badge['name']} - {badge['description']} (+{badge['points']} pts)")
        
        print(f"\n✅ Challenges Completed: {summary['challenges_completed']}")
        print("=" * 60)


class ChallengeValidator:
    """Validates challenge solutions"""
    
    @staticmethod
    def validate_agent_deployment(endpoint_name: str, catalog: str, schema: str) -> bool:
        """Validate that an agent endpoint exists"""
        try:
            from databricks.sdk import WorkspaceClient
            w = WorkspaceClient()
            
            # Check if endpoint exists
            endpoints = w.serving_endpoints.list()
            endpoint_exists = any(e.name == endpoint_name for e in endpoints)
            
            if endpoint_exists:
                print("✅ Agent endpoint found!")
                return True
            else:
                print(f"❌ Endpoint '{endpoint_name}' not found")
                return False
        except Exception as e:
            print(f"❌ Validation error: {str(e)}")
            return False
    
    @staticmethod
    def validate_agent_performance(endpoint_name: str, max_latency_ms: int = 2000) -> bool:
        """Validate agent response time"""
        try:
            from databricks.sdk import WorkspaceClient
            import time
            
            w = WorkspaceClient()
            
            # Test query
            test_query = "What is the status of turbine ID 004a641f?"
            
            start_time = time.time()
            response = w.serving_endpoints.query(
                name=endpoint_name,
                inputs=[{"query": test_query}]
            )
            latency_ms = (time.time() - start_time) * 1000
            
            if latency_ms < max_latency_ms:
                print(f"✅ Agent response time: {latency_ms:.0f}ms (< {max_latency_ms}ms)")
                return True
            else:
                print(f"❌ Agent too slow: {latency_ms:.0f}ms (target: < {max_latency_ms}ms)")
                return False
        except Exception as e:
            print(f"❌ Performance test error: {str(e)}")
            return False
    
    @staticmethod
    def validate_uc_function(catalog: str, schema: str, function_name: str) -> bool:
        """Validate UC function exists and is callable"""
        try:
            from databricks.sdk import WorkspaceClient
            w = WorkspaceClient()
            
            full_name = f"{catalog}.{schema}.{function_name}"
            
            # Check if function exists
            try:
                func = w.functions.get(name=full_name)
                print(f"✅ UC Function found: {full_name}")
                return True
            except:
                print(f"❌ UC Function not found: {full_name}")
                return False
        except Exception as e:
            print(f"❌ Validation error: {str(e)}")
            return False
    
    @staticmethod
    def validate_vector_search_index(catalog: str, schema: str, index_name: str) -> bool:
        """
        ⚠️ NOT AVAILABLE IN FREE EDITION ⚠️
        Vector Search is not available in Databricks Free Edition.
        This validator is kept for reference but will always skip validation.
        """
        print(f"⚠️ Vector Search validation skipped - not available in Free Edition")
        print(f"   (Would check: {catalog}.{schema}.{index_name})")
        return True  # Skip validation in Free Edition


def display_challenge_intro(challenge_name: str, difficulty: str, points: int, description: str):
    """Display formatted challenge introduction"""
    difficulty_colors = {
        "Beginner": "🟢",
        "Intermediate": "🔵",
        "Advanced": "🟣",
        "Expert": "🔴"
    }
    
    color = difficulty_colors.get(difficulty, "⚪")
    
    print("\n" + "=" * 70)
    print(f"🎯 CHALLENGE: {challenge_name}")
    print("=" * 70)
    print(f"{color} Difficulty: {difficulty}")
    print(f"💎 Points: {points}")
    print(f"\n📋 Description:\n{description}")
    print("\n" + "=" * 70 + "\n")


def display_challenge_success(challenge_name: str, points_earned: int):
    """Display challenge completion message"""
    print("\n" + "🎉" * 35)
    print(f"✅ CHALLENGE COMPLETED: {challenge_name}")
    print(f"💎 You earned {points_earned} points!")
    print("🎉" * 35 + "\n")


def display_badge_awarded(badge_id: str):
    """Display badge award animation"""
    badge_info = Badge.get_badge_info(badge_id)
    print("\n" + "⭐" * 35)
    print(f"🏅 NEW BADGE UNLOCKED!")
    print(f"\n{badge_info['name']}")
    print(f"{badge_info['description']}")
    print(f"💎 +{badge_info['points']} points")
    print("⭐" * 35 + "\n")


# Quick access functions for notebooks
def init_learner(learner_id: Optional[str] = None):
    """Initialize learner progress tracking"""
    if learner_id is None:
        import getpass
        learner_id = getpass.getuser()
    return LearnerProgress(learner_id)


def check_progress():
    """Quick progress check"""
    learner = init_learner()
    learner.display_progress()
    return learner


if __name__ == "__main__":
    # Example usage
    learner = init_learner("demo_user")
    learner.display_progress()
