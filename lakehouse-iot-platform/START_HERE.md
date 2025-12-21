# 🚀 START HERE - Setup Guide

## Welcome to Databricks GenAI Learning! 🎓

**⏱️ Time:** 15-20 minutes to setup  
**✅ Result:** Ready to earn your first badge!

---

## Step 1: Configure Catalog ⚙️

Run this in a new Python cell:

```python
# Manual Configuration (works in Free Edition)
catalog = "main"
db = "e2eai_iot_turbine"
volume_name = "e2eai_iot_volume"

spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"CREATE DATABASE IF NOT EXISTS `{db}`")
spark.sql(f"USE DATABASE `{db}`")

print(f"✅ Using catalog: {catalog}")
print(f"✅ Using database: {db}")
print(f"✅ Configuration complete!")
```

**✅ Expected:** You see success messages

---

## Step 2: Run Data Pipeline 🏗️ ⚠️ CRITICAL!

**Open:** `01-Data-ingestion/01.1-SDP-Wind-Turbine-SQL.ipynb`

**Action:**
1. Open notebook in new tab
2. Attach to Serverless cluster
3. **Run ALL cells** (~3-5 minutes)
4. Wait for completion

**This creates all turbine data tables!**

---

## Step 3: Verify Data ✅

Run this SQL query:

```sql
SELECT 
  turbine_id,
  status,
  avg_energy,
  location
FROM main.e2eai_iot_turbine.turbine_status 
LIMIT 10
```

**✅ Success:** You see turbine data (WT-001, WT-002, etc.)  
**❌ Error:** Go back to Step 2

---

## Step 4: Create AI Tools 🔧

**Open:** `05-Generative-AI/05.1-ai-tools.ipynb`

**Action:**
1. Open notebook
2. Run ALL cells (~2 minutes)
3. Creates 3 UC Functions for agents

**Verify:**
```sql
SHOW FUNCTIONS IN main.e2eai_iot_turbine
```

**✅ You should see:**
- turbine_specifications_retriever
- turbine_maintenance_predictor
- turbine_maintenance_guide_retriever

---

## Step 5: Initialize Learning System 🎓

Run in a new notebook:

```python
# Initialize
%run ./_resources/00-setup $reset_all_data=false

# Import framework
import sys
sys.path.append('./_resources')
from gamification_framework import init_learner

learner = init_learner()
learner.display_progress()
```

**✅ You should see your learning dashboard!**

---

## 🎉 Setup Complete!

### Next Step: Start Learning

**Open:** `05-Generative-AI/05.1.1-prompt-engineering-basics.ipynb`

**You'll:**
- ✅ Learn RACE Framework
- ✅ Complete 5 challenges
- ✅ Earn badge: 📝 Prompt Master (150 pts)
- ✅ Takes 30 minutes!

---

## 🗺️ Learning Paths

Choose your path:

**🚀 Quick Start** (2-3h)
```
05.1.1 → 05.2 → 05.X
```

**🔧 Tool Developer** (4-5h)
```
05.1.1 → 05.2 → 05.6 → 05.8
```

**🏗️ Architect** (8-10h)
```
All modules in 05-Generative-AI/
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Table not found | Re-run Step 2 (data ingestion) |
| Function not found | Re-run Step 4 (05.1-ai-tools.ipynb) |
| Catalog error | Check Step 1, use `main` catalog |
| Import error | Re-run Step 5 setup |

---

## 📚 Resources

- **Module Overview:** `05-Generative-AI/README.md`
- **Learning Paths:** `05-Generative-AI/LEARNING_ROADMAP.md`
- **Update Repo:** `HOW_TO_UPDATE.md`

---

**Ready?** Open `05.1.1-prompt-engineering-basics.ipynb` and start! 🚀
