# 🔄 How to Update Your Repository in Databricks

## Method 1: Git Pull via UI (Recommended) ✅

### Step-by-Step:

1. **Navigate to your Repository**
   - Click **Workspace** in left sidebar
   - Go to **Repos**
   - Click on your `e2e-data-science` repository

2. **Open Git Menu**
   - Look for the **Git branch dropdown** (top of the page, shows "main")
   - Or click the **Git icon** (branching symbol)

3. **Pull Latest Changes**
   - Click the dropdown menu next to branch name
   - Select **"Pull"** or **"Update from remote"**
   - Databricks will fetch and pull latest changes from GitHub

4. **Verify Update**
   - Check the commit hash or timestamp
   - You should see the latest notebooks and files

**⏱️ Time:** 5-10 seconds  
**✅ Keeps your local changes** if any

---

## Method 2: Git Commands in Notebook 🖥️

You can also use Git commands directly in a notebook:

```python
# In a Databricks notebook
%sh
cd /Workspace/Repos/[your-email]/e2e-data-science
git pull origin main
```

**Note:** Replace `[your-email]` with your Databricks user email

---

## Method 3: Full Repo Sync (Nuclear Option) 🔄

If you have conflicts or want a fresh start:

1. **Delete existing repo**
   - Right-click on repo folder
   - Select **"Delete"**

2. **Re-clone repository**
   - Workspace → Repos → **Add Repo**
   - URL: `https://github.com/PaulKuhz/e2e-data-science`
   - Click **Create Repo**

**⏱️ Time:** 30-60 seconds  
**⚠️ Warning:** Deletes any local changes you made

---

## 🎯 Recommended Workflow:

### When to Pull:
- ✅ After I push updates to GitHub
- ✅ Before starting a new learning session
- ✅ If notebooks seem outdated

### Auto-Sync (Future):
Some Databricks plans support auto-sync, but **Free Edition requires manual pull**.

---

## 🐛 Troubleshooting:

### "Cannot pull - you have local changes"
**Solution:**
```python
%sh
cd /Workspace/Repos/[your-email]/e2e-data-science
git stash  # Save local changes
git pull origin main
git stash pop  # Restore local changes (optional)
```

### "Permission denied"
**Solution:** Make sure you're pulling from your fork:
- URL should be: `https://github.com/PaulKuhz/e2e-data-science`
- Not: `https://github.com/Berkeley-Data/e2e-data-science`

### "Branch is up to date"
**Solution:** You already have the latest version! ✅

---

## 📋 Quick Reference:

| Method | When to Use | Pros | Cons |
|--------|-------------|------|------|
| **Git Pull UI** | Regular updates | Fast, simple | Manual process |
| **Git Commands** | Advanced users | Flexible | Requires command knowledge |
| **Re-clone** | Major conflicts | Clean slate | Loses local changes |

---

## 💡 Pro Tip:

Before pulling updates, **save your progress** if you've completed any challenges:

```python
# Save your learning progress
learner.save_progress()
```

The gamification framework stores progress in your workspace, so it won't be lost during pulls!

---

**Need help?** Open an issue on GitHub or check the troubleshooting section in `SETUP_GUIDE.md`
