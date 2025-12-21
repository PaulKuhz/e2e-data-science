# 🎓 Databricks GenAI Interactive Learning Path
## Wind Turbine Intelligence Platform - From Zero to GenAI Hero

### 🌟 Welcome to Your GenAI Journey!

This is **not just a demo** - it's your **interactive learning adventure** into Generative AI with Databricks! 

Built for students, educators, and GenAI enthusiasts who want to master the Databricks Intelligence Platform through **hands-on challenges**, **real-world scenarios**, and **gamified learning**.

### 🎮 What Makes This Different?

- **🏅 Gamified Learning**: Earn badges, level up, and track your progress
- **💪 Challenge-Based**: Learn by doing, not just reading
- **🎯 Progressive Difficulty**: From Beginner to Expert levels
- **🏆 Real Skills**: Build production-ready GenAI solutions
- **🤝 Peer Learning**: Compare solutions, review code, compete on leaderboards

---

## 🎯 Your Learning Path

### 📊 Progress Tracking System

We've built a complete gamification framework to track your journey:

```python
# Check your progress anytime:
from _resources.gamification_framework import check_progress
check_progress()
```

### 🏅 Badges You Can Earn

| Badge | Description | Points | How to Earn |
|-------|-------------|--------|-------------|
| 🤖 **First Agent** | Deploy your first AI Agent | 100 | Complete Module 05.2 |
| 📝 **Prompt Master** | Optimize system prompts | 150 | Agent quality > 85% |
| 🔧 **Tool Builder** | Create custom AI Tools | 200 | Build UC function tool |
| ⚡ **Performance Optimizer** | Speed demon | 250 | Agent latency < 2s |
| 🔍 **RAG Expert** | Master RAG patterns | 300 | Complete RAG deep dive |
| 🏗️ **Multi-Agent Architect** | Orchestrate agents | 400 | Build multi-agent system |
| 🐛 **Debugging Hero** | Fix all bugs | 150 | Complete debug challenges |
| 💰 **Cost Optimizer** | Reduce costs 50% | 200 | Optimize token usage |
| 🛡️ **Security Champion** | Secure patterns | 250 | Pass security checks |
| 🎓 **GenAI Master** | The ultimate achievement | 1000 | Earn all badges |

### 📈 Level System

Progress through 5 levels as you learn:

- 🟢 **Level 1: Beginner** (0-499 pts) - Guided tutorials with full code
- 🔵 **Level 2: Intermediate** (500-1499 pts) - Fill-in-the-blank challenges  
- 🟣 **Level 3: Advanced** (1500-2999 pts) - Design your own solutions
- 🟠 **Level 4: Expert** (3000-4999 pts) - Optimize and debug complex systems
- 🔴 **Level 5: Master** (5000+ pts) - Create novel GenAI applications

---

## 🚀 **Getting Started - Your First Steps**

### **Step 1: Clone Repository to Databricks** 📦
1. Open Databricks Free Edition
2. Go to **Workspace** → **Repos** → **Add Repo**
3. Enter: `https://github.com/PaulKuhz/e2e-data-science` (or Berkeley-Data if using original)
4. Click **Create Repo**

### **Step 2: Configure Your Environment** ⚙️
1. Open `lakehouse-iot-platform/config.ipynb`
2. Set your catalog name (e.g., `main` for Free Edition)
3. Run all cells

### **Step 3: ⚠️ CRITICAL - Run Data Ingestion Pipeline** 🏗️
**You MUST do this before any GenAI modules!**

1. Open `lakehouse-iot-platform/01-Data-ingestion/01.1-SDP-Wind-Turbine-SQL.ipynb`
2. Run all cells (creates turbine tables with sensor data)
3. Verify: `SELECT * FROM turbine_status LIMIT 10` returns data ✅

**Why?** All GenAI tools query these tables. Without data → tools fail!

### **Step 4: Start Your GenAI Journey** 🎓
1. Open `lakehouse-iot-platform/05-Generative-AI/README.md`
2. Choose your learning path
3. Begin with `05.1.1-prompt-engineering-basics.ipynb`

---

### Overview
This comprehensive learning experience uses the Databricks Free Edition to teach you end-to-end GenAI development. You'll build production-ready solutions while mastering both traditional ML and cutting-edge agentic AI patterns.

### Key Learning Objectives
- Experience Databricks’ modern open platform from data ingestion through productionization
- Understand open standards, open source, and cloud-native best practices in a reproducible, academic context
- Explore both declarative data engineering and agentic orchestration patterns

### End-to-End Workflow Components
1. Free Account Setup
Step-by-step walk-through of signing up for Databricks Free Edition
Direct GitHub code repository connection and synchronization within the Databricks workspace
2. Data Ingestion & ETL Pipeline Construction
Selection and exploration of a publicly available dataset
Visual ETL transformation with Lakeflow Designer, demonstrating pipeline construction
Compatibility with Spark Declarative Pipelines and open-source workflow standards
3. Open Data Governance with Unity Catalog
Data wrangling and cleansing workflows
Creating and managing a Unity Catalog (open source) for structured, secured, and discoverable data assets
4. Exploratory Data Analysis (EDA)
Interactive EDA using Python (pandas, matplotlib, seaborn) within Databricks notebooks
Additional EDA techniques using Genie integration for rapid data insight generation
5. Machine Learning & Agentic Workflows
Feature engineering and baseline ML model development using open source libraries
Orchestration and management with MLflow 3.0, including experiment tracking and model evaluation (open source)
Introduction to agentic workflows—demonstrating orchestration with agents alongside traditional ML pipelines
6. Model Deployment & Open Standards Access
Promotion of the trained ML model to an endpoint for consumption
Registration and access to the model via MCP (Model Connectivity Protocol) adhering to open standards
7. Interactive Application Integration
Development of an interactive Databricks App using JavaScript (Streamlit or React)
Real-time demonstration of agentic solution interaction, powered by the deployed ML endpoint

### Academic Relevance
This demo encapsulates the state-of-the-art in reproducible, open science workflows, from raw data through actionable endpoints. Graduate students gain practical experience with both engineering and applied data science lifecycles, all accessible at no cost on the Databricks Free Edition. The approach fosters both technical competence and confidence to build and share robust, production-grade analytics and agentic solutions.

### Summary Table
| Stage | Tools/Tech Used | Open Source/Standard? | Key Academic Takeaway |
|-------|-----------------|-----------------------|-----------------------|
| Setup | Databricks Free, GitHub | Yes | Platform access & reproducibility |
| ETL/Data | Lakeflow Designer, Spark | Yes | Visual, scalable pipeline design |
| Governance | Unity Catalog | Yes | Data discoverability/security |
| EDA | Python, Genie | Yes | Modern open EDA methods |
| ML/Agent | MLflow 3, Agents | Yes | Model and orchestration lifecycle |
| Deployment | Model Serving, MCP, Playground | Yes | Open model serving with function calling |
| App Integration | Streamlit/React | Yes | App-building with live ML agents |

The session is designed to inspire, inform, and empower early-career researchers with direct exposure to end-to-end, open-source-powered analytics and AI workflows.

![](lakehouse-iot-platform/_resources/images/e2eai-0.jpg)

### To Get Started:
**0. Initialization**

*TLDR: Review the config. Read and run the notebook.*

Review the `config` file in the lakehouse-iot-platform directory.  Change the catalog or schema if you desire.

Read and run the `00-IOT-wind-turbine-introduction-DI-platform` notebook in the lakehouse-iot-platform directory. This notebook explains the project and it contains a single line of code that:
1. Creates the catalog and schema where all metadata will be stored.
2. Loads the required data into the designated AWS S3 bucket.

Once the notebook finishes running, you can verify the data load by navigating to Catalog → My Organization in the left panel and selecting `main.e2eai_iot_turbine.Volumes` (or whichever catalog and schema you set in your config file). Seeing the data here confirms it has been loaded into S3 and is ready for ingestion by Databricks.

**1. Data Ingestion**

*TLDR: Create a pipeline to run this notebook. Do not run the notebook outside a pipeline.* 

The ETL step for your project involves ingesting, cleaning, and transforming data, ultimately producing eight tables. All related code is located in the `01-Data-ingestion/01.1-DLT-Wind-Turbine-SQL` notebook. However, you cannot run this notebook directly, as it contains STREAMING TABLES defined in the Lakeflow Declarative Pipeline format.
    
To start the ETL process:
- Go to the Jobs & Pipelines section in Databricks.
- Click `Create` button, and select `ETL Pipeline`. 
- Ensure `Lakeflow Pipelines Editor` is set to ON.
- Give your pipeline a name and change the cataloge and schema to the values in your `config` file.
- Click the Advanced Option for `Add existing assets` and point the pipeline to the 01 root folder and notebook 1.1.
- Click `Run` to start your pipeline from the UI. Alternatively, you can do a dry run first to test your pipeline.

Key details:
- The ETL process extracts data from source systems, cleans and transforms it, and loads it into production tables.
- Using Delta Live Tables (DLT) and the declarative pipeline approach allows you to manage both batch and streaming data, ensuring reliability and scalability in data processing.
- The workflow is managed outside the notebook to ensure proper orchestration, dependency handling, and monitoring, as is best practice with declarative pipelines and production ETL in the Databricks Lakehouse environment.

**2. Security and Governance**

*TLDR: Create groups, then run this notebook.*

The `02-Data-goverenence` notebook sets up grants for groups and offers best practices for access control, data lineage, and compliance, helping to ensure responsible data management.

Before running this notebook, create two groups for users:
- dataengineers
- analysts

Illustrated steps for group creation are given in the notebook and included here for reference:
1. Go to Settings under the circle for your profile in the top right corner
2. Under Workspace Admin, select `Identity and access`
3. Click the `Manage` button for Groups 
4. Click `Add Group`, then add each of the two groups mentioned above<br>

Once the groups are created, run the notebook. 

**3. AI/BI Genie and Data Warehousing**

*TLDR: Read and explore this notebook.  There is no code to run, but check out the dashboards.*

In `03-BI-Data-warehousing`, you'll find guidance on using Databricks SQL for analytics, dashboard creation, and business intelligence tasks. Two example dashboards have been included in this repo (lakehouse-iot-platform/_dashboards/). You may need to adjust the catalog and schema on the data tab of the dashboards for all the querie to work.
    
Also check out the AI/BI Genie.  It's available in Free Edition and can be easily enabled when you publish a dashboard.

**4. Data Science and ML**

4.1. EDA
   
*TLDR: Run this notebook end to end.*

Once the data is prepared and ready for analysis, the next phase is exploratory data analysis (EDA). The code for this stage can be found in the `04-Data-Science-ML/04.1-EDA` notebook. Here, data scientists will explore trends, visualize data distributions, and generate insights that inform the modeling process.

4.2. Model Creation
   
*TLDR: Run this notebook end to end. It can take 30+ minutes to run.*
    
In this step, multiple models are developed and each step of experimentation is logged in MLflow. Unity Catalog offers seamless integration with MLflow, simplifying experiment tracking and model management. Within the `04-Data-Science-ML/04.2-predictive_model_creation` notebook, you will:
- Create and run different model experiments.
- Record experiment results in MLflow.
- Register the final, chosen model as a production model in the MLflow model registry for easier deployment and governance.

4.3. Model Deployment

*TLDR: Run this notebook end to end.*

In this step, the registered model is deployed as an endpoint to enable inference. You will use the `04-Data-Science-ML/04.3-model_deployment` notebook for this step. The deployment workflow typically includes:
- Deploying the Model: The notebook guides you through deploying the chosen model from the MLflow model registry to a serving endpoint, making it accessible for real-time or batch predictions.
- Batch Inference: After deployment, the same notebook demonstrates how to perform batch inference on a table—specifically, using one of the tables available in your catalog. This allows you to generate predictions at scale and store results back into your Lakehouse environment.

**5. Generative AI and Databricks Apps** 🔥 **PRIMARY LEARNING FOCUS**

This is the **heart of your GenAI learning journey**! We've completely transformed this section into an **interactive workshop** with:

- 🎯 **Progressive Challenges**: From basics to advanced patterns
- 🏅 **Badge Opportunities**: Earn 5+ badges in this section alone
- 💡 **Real-World Scenarios**: Fix production issues, optimize costs, handle emergencies
- 🔬 **Experimentation Labs**: Try ideas in safe sandbox environments
- 📊 **Performance Tracking**: See how your agents stack up

**Learning Modules:**

This section serves as your comprehensive guide for mastering GenAI with Databricks. Each module builds on the previous, with increasing challenge levels and real-world complexity.

5.1. AI Tools

*TLDR: Add a TOKEN and workspace ROOT, then run the notebook.*

`05.1-ai-tools-iot-turbine-prescriptive-maintenance` utilizes Databricks' generative AI capabilities for advanced analytics and automation tasks. The key actions include:

- Tool 1 - Turbine Spec Retriever Tool: Create a tool that queries a table and returns the sensor readings for a given turbine ID.  This is an example of a simple SQL function tool.
- Tool 2 - Turbine Predictor Tool: Create a tool that leverages the previously built ML model to predict turbine failures, supporting prescriptive maintenance strategies.
- Parsing and Saving Unstructured Data: Extract and store relevant text from unstructured sources such as PDF documents, making it available for downstream AI-powered search and analytics.
- Vector Search Endpoint Creation: Set up a vector search endpoint and assign a dedicated vector search index. This enables high-performance, semantic search across your dataset.
- Tool 3 - Turbine Maintenance Vector Search Tool: Develop a tool that interfaces with the vector search index, enabling agents to retrieve contextually relevant information based on semantic similarity rather than traditional keyword search.  This is an example of RAG as an agent tool.

5.2 Agent Creation Guide

*TLDR: Read this notebook*

Read this notebook and explore the UI to chat with your data and create an agent.

5.3 Agent via code

*TLDR: Optional to run this notebook.*

Run this notebook if you want to use code to build an agent instead of the UI.  This is optional if you already built your agent in step 5.2.

5.4 Agent Eval and Serve

*TLDR: Run this notebook.*

This notebook walks you through how to evaluate your agent and serve it.  Free Edition is limited to 1 serving endpoint, so while the code is provided for serving your agent, the available endpoint is already consumed by our ML model that we served.

5.5 Agent App
    
*TLDR: Follow the steps in this notebook*

This notebook walks you through the steps to create an app on Databricks.  The repo includes all the files you will need to create a simple chat agent using the tools we built in section 4.  While you are navigating around, check out the sample questions that have been provided for you in `e2e-data-science/lakehouse-iot-platform/_app/` to help with a quick test of your chat agent.

5.6 MCP

*TLDR: Read and explore*

**6. Workflow Orchestration**

*TLDR: Read and explore this notebook*

The `06-workflow-orchestration` directory provides information on how to schedule, automate, and monitor your data and ML pipelines effectively. Altogether, these materials serve as guides to help improve data security, analytics, and operational efficiency within your platform.



