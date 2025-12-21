# 🚀 Setup Guide - From Zero to Ready

## Prerequisites
- Databricks Free Edition Account (https://www.databricks.com/try-databricks)
- GitHub Account (for repository access)

---

## Step 1: Import Repository to Databricks 📦

### Option A: Via Databricks Repos (Recommended)

1. **Open Databricks Workspace**
   - Go to https://accounts.cloud.databricks.com/
   - Login to your workspace

2. **Add Repository**
   - Click **Workspace** in left sidebar
   - Click **Repos**
   - Click **Add Repo** button
   
3. **Configure Repository**
   ```
   Git repository URL: https://github.com/PaulKuhz/e2e-data-science
   Git provider: GitHub
   Repository name: e2e-data-science
   ```
   
4. **Click "Create Repo"**
   - Repository will sync automatically
   - All notebooks will appear in your workspace

### Option B: Manual Upload (Alternative)

1. Download this repository as ZIP
2. In Databricks: **Workspace** → **Import**
3. Upload ZIP file
4. Extract to desired location

---

## Step 2: Configure Catalog & Schema ⚙️

1. **Open:** `lakehouse-iot-platform/config.ipynb`

2. **Check/Update catalog name:**
   ```python
   catalog = "main"  # For Free Edition, use "main"
   db = "e2eai_iot_turbine"
   ```

3. **Run all cells** in config.ipynb

**Expected Output:**
```
✅ Using catalog: main
✅ Using schema: e2eai_iot_turbine
✅ Configuration complete
```

---

## Step 3: ⚠️ CRITICAL - Run Data Ingestion Pipeline 🏗️

**This creates all the turbine data tables. Without this, GenAI tools will fail!**

### Run the Pipeline:

1. **Open:** `lakehouse-iot-platform/01-Data-ingestion/01.1-SDP-Wind-Turbine-SQL.ipynb`

2. **Attach to Cluster:**
   - Use Serverless compute (Free Edition)
   - Or create a small cluster (1 worker)

3. **Run all cells** (takes ~3-5 minutes)

### What This Creates:

Tables created in `main.e2eai_iot_turbine`:
- ✅ `turbine_status` - Current turbine status
- ✅ `sensor_readings` - Real-time sensor data
- ✅ `turbine_maintenance` - Maintenance history
- ✅ `turbine_power` - Power output data
- ✅ `historical_turbine_status` - Historical data

---

## Step 4: Verify Data is Loaded ✅

### Test Query:

Create a new SQL cell and run:

```sql
SELECT * FROM main.e2eai_iot_turbine.turbine_status LIMIT 10
```

**Expected Result:**
```
turbine_id | status | vibration | temperature | ...
WT-001     | normal | 5.2       | 68.5       | ...
WT-002     | normal | 4.8       | 70.1       | ...
...
```

If you see data → **Setup Complete!** ✅

If error "Table not found" → Go back to Step 3

---

## Step 5: Initialize Gamification Framework 🎮

1. **Open:** `lakehouse-iot-platform/05-Generative-AI/05.1.1-prompt-engineering-basics.ipynb`

2. **Run the first 2 cells:**
   ```python
   # Cell 1: Install dependencies
   %pip install databricks-sdk==0.40.0 mlflow==2.18.0 --quiet
   dbutils.library.restartPython()
   
   # Cell 2: Initialize progress tracking
   %run ../_resources/00-setup $reset_all_data=false
   
   import sys
   sys.path.append('../_resources')
   from gamification_framework import init_learner
   
   learner = init_learner()
   ```

**Expected Output:**
```
╔══════════════════════════════════════════════════════╗
║  🎯 CHALLENGE: Prompt Engineering Basics             ║
║  Difficulty: 🟢 Beginner                             ║
║  Points: 100 📊                                      ║
║                                                      ║
║  Your Level: 1 🟢 Beginner                          ║
║  Total Points: 0                                    ║
╚══════════════════════════════════════════════════════╝
```

---

## Step 6: Create Unity Catalog Functions (Tools) 🔧

Before building agents, create the UC Functions they'll use:

1. **Open:** `lakehouse-iot-platform/05-Generative-AI/05.1-ai-tools.ipynb`

2. **Run all cells** to create 3 functions:
   - ✅ `turbine_specifications_retriever` - SQL query tool
   - ✅ `turbine_maintenance_predictor` - AI prediction tool
   - ✅ `turbine_maintenance_guide_retriever` - Vector search tool

### Verify Functions Created:

```sql
SHOW FUNCTIONS IN main.e2eai_iot_turbine;
```

Should show:
```
main.e2eai_iot_turbine.turbine_specifications_retriever
main.e2eai_iot_turbine.turbine_maintenance_predictor
main.e2eai_iot_turbine.turbine_maintenance_guide_retriever
```

---

## 🎉 Setup Complete! What's Next?

### Recommended Learning Path:

1. **Start Learning:** Open `05-Generative-AI/README.md`
2. **Choose Path:** Pick from 4 learning paths (Quick Start, Tool Developer, Architect, Complete Mastery)
3. **First Challenge:** `05.1.1-prompt-engineering-basics.ipynb`
4. **Earn Badges:** Complete challenges to level up!

### Check Your Progress Anytime:

```python
from _resources.gamification_framework import check_progress
learner = check_progress()
learner.display_progress()
```

---

## 🐛 Troubleshooting

### "Table not found" error
→ Re-run Step 3 (Data Ingestion Pipeline)

### "Catalog does not exist"
→ Check Step 2 - verify catalog name in `config.ipynb`

### "Function not found" error
→ Run Step 6 - create UC Functions in `05.1-ai-tools.ipynb`

### Cluster issues
→ Use Serverless compute (recommended for Free Edition)

### Permission errors
→ Ensure you're owner of catalog `main` or use a catalog you own

---

## 📚 Additional Resources

- **Documentation:** `05-Generative-AI/LEARNING_ROADMAP.md`
- **Module Overview:** `05-Generative-AI/README.md`
- **Project Summary:** `TRANSFORMATION_SUMMARY.md`

---

**Ready to start?** Open `05.1.1-prompt-engineering-basics.ipynb` and earn your first badge! 🏅
