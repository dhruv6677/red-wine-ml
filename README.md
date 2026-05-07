# 🍷 Red Wine Quality Prediction - End-to-End ML Project

This project predicts the quality of red wine using Machine Learning techniques.  
It follows a complete **MLOps pipeline structure** including configuration management, reusable components, training pipelines, and Flask deployment.

---

# 📸 Project Overview

The model predicts wine quality based on chemical properties such as:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Sulphates
- Alcohol
- pH
- Density

The project is designed using a modular architecture so it is easy to scale, maintain, and deploy. :contentReference[oaicite:0]{index=0}

---

# 🚀 Workflows

The project follows these steps:

```bash
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration manager
6. Update components
7. Update pipeline
8. Update main.py
9. Update app.py
```

---

# 📁 Project Structure

```bash
red-wine-ml/
│
├── config/
│   └── config.yaml
│
├── schema.yaml
├── params.yaml
├── main.py
├── app.py
├── requirements.txt
├── README.md
│
├── artifacts/
│
├── research/
│
├── templates/
│   └── index.html
│
└── src/
    └── redWine/
        │
        ├── components/
        │   ├── data_ingestion.py
        │   ├── data_validation.py
        │   ├── data_transformation.py
        │   ├── model_trainer.py
        │   └── model_evaluation.py
        │
        ├── pipeline/
        │   ├── stage_01_data_ingestion.py
        │   ├── stage_02_data_validation.py
        │   ├── stage_03_data_transformation.py
        │   ├── stage_04_model_trainer.py
        │   └── stage_05_model_evaluation.py
        │
        ├── config/
        │   └── configuration.py
        │
        ├── entity/
        │   └── config_entity.py
        │
        ├── utils/
        │   └── common.py
        │
        └── constants/
            └── __init__.py
```

---

# ⚙️ Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Flask
- YAML
- MLflow
- DVC

---

# 📂 Dataset

Dataset used:

**Wine Quality Dataset**

The dataset contains physicochemical properties of red wine and corresponding quality scores. :contentReference[oaicite:1]{index=1}

---

# 🛠️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository_url>
cd red-wine-ml
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration Files

## 📌 config.yaml

Stores:
- dataset paths
- model paths
- artifacts paths
- training directories

---

## 📌 schema.yaml

Defines:
- column names
- datatypes
- validation schema

---

## 📌 params.yaml

Contains:
- hyperparameters
- learning rate
- train-test split
- random state

---

# 🧩 Entity

The `entity` folder contains dataclass-based configuration entities.

Example:

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
```

---

# ⚙️ Configuration Manager

Located inside:

```bash
src/redWine/config/configuration.py
```

Responsibilities:
- read YAML files
- create directories
- manage configurations
- return config objects

---

# 🧠 Components

Located inside:

```bash
src/redWine/components/
```

Components include:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Trainer
- Model Evaluation

Each component handles one stage of the ML pipeline. :contentReference[oaicite:2]{index=2}

---

# 🔄 Pipeline

Located inside:

```bash
src/redWine/pipeline/
```

Pipeline stages:

```bash
stage_01_data_ingestion.py
stage_02_data_validation.py
stage_03_data_transformation.py
stage_04_model_trainer.py
stage_05_model_evaluation.py
```

The pipeline connects all ML stages sequentially.

---

# ▶️ Run Training Pipeline

Run the full pipeline:

```bash
python main.py
```

This will:

- ingest data
- validate schema
- transform dataset
- train model
- evaluate model
- save artifacts

---

# 🌐 Run Flask App

Start the Flask application:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000/
```

---

# 📊 Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1 Score

MLflow can also be used for experiment tracking.

---

# 📦 Artifacts Generated

```bash
artifacts/
│
├── data_ingestion/
├── data_validation/
├── data_transformation/
├── model_trainer/
└── model_evaluation/
```

---

# 📈 Example Features

| Feature | Description |
|---|---|
| fixed acidity | Non-volatile acids |
| volatile acidity | Acetic acid level |
| citric acid | Wine freshness |
| alcohol | Alcohol percentage |
| sulphates | Antimicrobial additive |

---

# 📝 Notes

- Modular project structure
- YAML-based configuration system
- Reusable ML components
- Easy deployment
- Production-ready architecture

---

# 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- MLflow
- DVC

---



# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
