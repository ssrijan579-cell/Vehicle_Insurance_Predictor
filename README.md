# 🚗 Vehicle Insurance Predictor — End-to-End MLOps Platform

> **An end-to-end production-oriented Machine Learning application that predicts whether a customer is likely to purchase vehicle insurance, with automated data ingestion, validation, transformation, model training, evaluation, model versioning, CI/CD, AWS deployment, and a FastAPI web interface.**

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production_API-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb)](https://www.mongodb.com/atlas)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws)](https://aws.amazon.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=github-actions)](https://github.com/features/actions)

---

## 📌 Project Overview

**Vehicle Insurance Predictor** is an end-to-end Machine Learning and MLOps system designed to predict whether a customer is likely to purchase vehicle insurance.

Instead of building only a standalone ML model, this project focuses on the **complete ML lifecycle**:

```text
Raw Data
   ↓
MongoDB Atlas
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
SMOTEENN
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Model Registry / AWS S3
   ↓
CI/CD
   ↓
Docker / EC2
   ↓
FastAPI Application
   ↓
Real-Time Prediction
```

The project demonstrates how a machine learning model can be transformed from an experimental notebook into a **repeatable, deployable and maintainable ML system**.

---

# 🎯 Business Problem

Vehicle insurance companies need to identify customers who are more likely to purchase insurance.

The dataset contains customer and vehicle-related attributes such as:

* Age
* Gender
* Driving License
* Region Code
* Previously Insured
* Vehicle Age
* Vehicle Damage
* Annual Premium
* Policy Sales Channel
* Vintage
* Response

The target variable is:

```text
Response
```

where:

* `1` → Customer is likely to purchase insurance
* `0` → Customer is unlikely to purchase insurance

### Business Objective

Build a reliable classification system that can help insurance companies:

* Identify potential customers
* Prioritize sales efforts
* Improve customer targeting
* Reduce unnecessary marketing costs
* Support data-driven insurance campaigns

---

# ⭐ Why This Project Stands Out

This project goes beyond a traditional ML notebook.

### Machine Learning

* Classification modeling
* Feature engineering
* Data preprocessing
* Handling categorical and numerical variables
* Class imbalance handling using **SMOTEENN**
* Model evaluation using precision, recall and F1-score

### MLOps

* Modular project architecture
* Custom logging
* Custom exception handling
* Data ingestion pipeline
* Data validation
* Data transformation
* Model training
* Model evaluation
* Model registry
* Model pushing
* Prediction pipeline

### Cloud & DevOps

* MongoDB Atlas
* AWS S3
* AWS IAM
* AWS EC2
* Docker
* Amazon ECR
* GitHub Actions
* Self-hosted GitHub Actions runner

### Application

* FastAPI REST/web application
* HTML templates
* Static CSS
* Real-time predictions
* Dedicated training endpoint

---

# 🏗️ System Architecture

```text
                        ┌─────────────────────┐
                        │   MongoDB Atlas      │
                        │   Vehicle Dataset    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Data Ingestion    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Data Validation   │
                        │ Schema + Quality     │
                        │ Checks               │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Data Transformation │
                        │ Encoding + Scaling  │
                        │ Feature Engineering │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    SMOTEENN         │
                        │ Class Balancing     │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Model Training    │
                        │   Random Forest     │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Model Evaluation    │
                        │ Compare with        │
                        │ Production Model    │
                        └──────────┬──────────┘
                                   │
                         New model accepted?
                           /              \
                         YES               NO
                          │                 │
                          ▼                 ▼
                  ┌───────────────┐      Reject
                  │   AWS S3      │
                  │ Model Storage │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   CI/CD       │
                  │ GitHub        │
                  │ Actions       │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ AWS EC2       │
                  │ Ubuntu        │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   FastAPI     │
                  │ Application   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ User          │
                  │ Prediction    │
                  └───────────────┘
```

---

# 🧰 Technology Stack

## Programming & Machine Learning

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| Python 3.10      | Core programming language        |
| Pandas           | Data manipulation                |
| NumPy            | Numerical computing              |
| Scikit-learn     | Machine learning & preprocessing |
| imbalanced-learn | SMOTEENN class balancing         |
| Matplotlib       | Data visualization               |
| Seaborn          | Exploratory data analysis        |
| PyYAML           | Configuration management         |
| Pickle           | Model serialization              |

## Backend & Application

| Technology       | Purpose         |
| ---------------- | --------------- |
| FastAPI          | Prediction API  |
| Uvicorn          | ASGI server     |
| Jinja2           | HTML templating |
| HTML/CSS         | Frontend        |
| python-multipart | Form handling   |

## Data Layer

| Technology    | Purpose             |
| ------------- | ------------------- |
| MongoDB Atlas | Cloud data storage  |
| PyMongo       | MongoDB integration |

## MLOps

| Technology                | Purpose                       |
| ------------------------- | ----------------------------- |
| Custom Logging            | Pipeline observability        |
| Custom Exception Handling | Structured error reporting    |
| Modular Components        | Maintainability               |
| Artifact Management       | Intermediate pipeline outputs |
| Model Evaluation          | Production model comparison   |
| Model Registry            | Versioned model storage       |

## Cloud & DevOps

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| AWS S3             | Model storage             |
| AWS IAM            | Secure AWS authentication |
| AWS EC2            | Application hosting       |
| Amazon ECR         | Docker image registry     |
| Docker             | Containerization          |
| GitHub Actions     | CI/CD                     |
| Self-hosted Runner | Automated EC2 deployment  |

---

# 📁 Project Structure

```text
Vehicle_Insurance_Predictor/
│
├── .github/
│   └── workflows/
│       └── aws.yaml
│
├── config/
│   └── schema.yaml
│
├── notebook/
│   ├── EDA.ipynb
│   └── mongoDB_demo.ipynb
│
├── static/
│   └── css/
│       └── style.css
│
├── template/
│   └── ...
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/
│   │   ├── mongo_db_connection.py
│   │   └── aws_connection.py
│   │
│   ├── data_access/
│   │   └── proj1_data.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   │
│   ├── pipline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── utils/
│   │   ├── main_utils.py
│   │   └── logger.py
│   │
│   ├── exception.py
│   ├── constants/
│   │   └── __init__.py
│   └── ...
│
├── artifact/
│   └── ...
│
├── app.py
├── demo.py
├── template.py
├── setup.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 🔄 ML Pipeline

## 1. Data Ingestion

The pipeline retrieves vehicle insurance data from **MongoDB Atlas**.

The ingestion component:

1. Connects to MongoDB
2. Selects the required database and collection
3. Fetches documents
4. Converts MongoDB records into a Pandas DataFrame
5. Splits data into training and testing datasets
6. Stores the resulting artifacts

Example dataset size used in the project:

```text
381,109 records
```

---

# 2. Data Validation

The validation stage verifies that incoming data follows the expected schema.

The schema is maintained in:

```text
config/schema.yaml
```

Validation covers:

* Expected columns
* Numerical columns
* Categorical columns
* Target variable
* Data structure
* Required fields
* Identifier handling

This prevents unexpected data from silently entering the ML pipeline.

---

# 3. Data Transformation

The transformation component prepares raw data for machine learning.

### Operations include:

* Dropping identifier columns
* Handling categorical features
* Encoding categorical variables
* Feature engineering
* Numerical preprocessing
* Scaling selected features
* Train/test transformation

The transformation process is implemented as a reusable pipeline rather than being manually repeated inside notebooks.

---

# 4. Handling Class Imbalance

The insurance dataset contains an imbalanced target distribution.

To address this, the project uses:

### SMOTEENN

SMOTEENN combines:

* **SMOTE** → Synthetic Minority Over-sampling Technique
* **ENN** → Edited Nearest Neighbours

This helps create a more balanced training dataset while cleaning potentially noisy observations.

---

# 5. Model Training

The project uses a:

### Random Forest Classifier

Random Forest was selected because it:

* Handles nonlinear relationships
* Works well with mixed feature types
* Is relatively robust to noise
* Provides strong baseline performance
* Supports feature importance analysis
* Performs well for tabular classification problems

The trained model is serialized and stored as:

```text
model.pkl
```

---

# 6. Model Evaluation

One of the key MLOps features of the project is **production-vs-new-model evaluation**.

Instead of automatically replacing the existing production model, the pipeline compares:

```text
New Model Performance
        vs
Current Production Model
```

The model is promoted only when it meets the configured performance criteria.

The project uses:

* Accuracy
* Precision
* Recall
* F1 Score

### Latest Training Performance

The latest trained model achieved approximately:

```text
F1 Score : 0.9316
Precision: 0.8803
Recall   : 0.9892
```

The production model was evaluated at approximately:

```text
F1 Score: 0.4311
```

The new model therefore demonstrated a substantial improvement and was accepted for deployment.

---

# ☁️ AWS Model Management

The project integrates AWS S3 as the model storage layer.

Current production configuration:

```text
AWS Region:
us-east-1

S3 Bucket:
vehicle-insurance-predict

Model:
model.pkl
```

The model evaluation component checks whether a newly trained model is better than the currently stored production model.

If accepted:

```text
New Model
    ↓
Model Pusher
    ↓
AWS S3
    ↓
Production Model
```

---

# 🔐 AWS Security

For local development, AWS credentials can be supplied through environment variables or a `.env` file.

For EC2 deployment, the application uses an **IAM Instance Role**.

This allows:

```text
EC2
 ↓
IAM Role
 ↓
Temporary AWS Credentials
 ↓
S3
```

No AWS access keys need to be hardcoded into the EC2 application.

The EC2 instance is associated with:

```text
VehicleInsuranceEC2Role
```

and uses boto3's standard credential resolution mechanism.

> **Security Note:** Never commit `.env`, AWS access keys, secret keys, MongoDB credentials, or other secrets to GitHub.

---

# 🌐 Prediction Pipeline

The project contains a dedicated prediction pipeline that:

1. Receives user input
2. Converts input into the expected data structure
3. Loads the preprocessing object
4. Loads the production model from S3
5. Applies the same preprocessing used during training
6. Generates the prediction
7. Returns the prediction to the FastAPI application

This ensures that training-time and prediction-time transformations remain consistent.

---

# 🚀 FastAPI Application

The ML pipeline is exposed through a FastAPI application.

Application responsibilities include:

* Serving the web interface
* Accepting customer information
* Running predictions
* Loading the production model
* Returning prediction results
* Providing a training route

The application is started using:

```bash
python app.py
```

The deployed application runs on:

```text
Port: 5000
```

---

# 🖥️ Web Application

The frontend is built using:

* HTML
* CSS
* Jinja2 templates

Project structure:

```text
template/
static/
    css/
        style.css
```

The frontend communicates with the FastAPI backend and provides a simple interface for submitting vehicle insurance information.

---

# 🔁 Training Endpoint

The application also provides a training route.

This allows the ML pipeline to be triggered from the deployed application.

Conceptually:

```text
/training
     ↓
Training Pipeline
     ↓
MongoDB
     ↓
Validation
     ↓
Transformation
     ↓
Training
     ↓
Evaluation
     ↓
S3 Model Registry
```

---

# 🐳 Dockerization

The application is containerized using Docker.

Docker provides:

* Reproducible environments
* Dependency isolation
* Easier deployment
* Consistent development/production environments
* Portable application packaging

Key files:

```text
Dockerfile
.dockerignore
```

Build the image:

```bash
docker build -t vehicle-insurance-predictor .
```

Run the container:

```bash
docker run -p 5000:5000 vehicle-insurance-predictor
```

---

# 🔄 CI/CD Pipeline

The project uses **GitHub Actions** to automate deployment.

The workflow is located at:

```text
.github/workflows/aws.yaml
```

High-level workflow:

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Build
    ├── Test / Validate
    ├── Build Docker Image
    ├── Push Image
    │
    ▼
Amazon ECR
    │
    ▼
EC2
    │
    ▼
Deploy Application
```

---

# 🖥️ Self-Hosted GitHub Actions Runner

The project uses an EC2-hosted **self-hosted GitHub Actions runner**.

The runner allows GitHub Actions workflows to execute deployment tasks directly on the EC2 environment.

Architecture:

```text
GitHub
   │
   │ GitHub Actions
   ▼
Self-Hosted Runner
   │
   ▼
AWS EC2
   │
   ▼
Vehicle Insurance API
```

This demonstrates practical knowledge of CI/CD infrastructure rather than relying only on local deployment.

---

# ☁️ AWS Infrastructure

The deployed architecture uses multiple AWS services.

### Amazon S3

Used for:

* Production model storage
* Model retrieval
* Model promotion

### IAM

Used for:

* EC2 authentication
* S3 permissions
* Secure AWS resource access

### EC2

Used for:

* Hosting the FastAPI application
* Running the self-hosted GitHub Actions runner
* Running the production environment

### Amazon ECR

Used for:

* Docker image storage
* Container deployment workflow

---

# 🗄️ MongoDB Atlas

MongoDB Atlas acts as the cloud data source for the ML pipeline.

Data flow:

```text
Dataset
   ↓
MongoDB Atlas
   ↓
PyMongo
   ↓
Data Ingestion
   ↓
Pandas DataFrame
```

The dataset is stored in:

```text
Database:
Vehicle_Insurance_Predictor

Collection:
Vehicle-Data
```

---

# 🧪 Exploratory Data Analysis

EDA was initially performed using Jupyter Notebook.

The notebook workflow includes:

* Dataset inspection
* Data type analysis
* Missing value analysis
* Distribution analysis
* Target distribution
* Numerical feature analysis
* Categorical feature analysis
* Feature relationships
* Feature engineering exploration

Notebook location:

```text
notebook/
```

---

# 📝 Logging & Exception Handling

The project implements custom logging and exception handling to improve debugging and observability.

Instead of receiving generic Python errors, exceptions can provide information such as:

```text
File
Line Number
Error Message
```

This is particularly useful for debugging multi-stage ML pipelines.

The pipeline logs important events such as:

```text
Data ingestion started
Data validation completed
Data transformation completed
Model training completed
Model evaluation completed
Model pushed to S3
```

---

# ⚙️ Installation & Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ssrijan579-cell/Vehicle_Insurance_Predictor.git

cd Vehicle_Insurance_Predictor
```

---

## 2. Create the Conda Environment

```bash
conda create -n vehicle python=3.10 -y
```

Activate it:

```bash
conda activate vehicle
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installed packages:

```bash
pip list
```

---

# 📦 Local Package Installation

The project follows a modular package structure.

`setup.py` and `pyproject.toml` are configured so that local source packages can be imported properly.

This enables imports such as:

```python
from src.components.data_ingestion import DataIngestion
```

instead of relying on manually modifying Python paths.

---

# 🔐 Environment Variables

Create a `.env` file for local development.

Example:

```env
MONGODB_URL=<your-mongodb-connection-string>

AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_DEFAULT_REGION=us-east-1
```

> Do not commit `.env` to GitHub.

Make sure it is included in:

```text
.gitignore
```

Also keep generated artifacts out of version control:

```text
artifact/
```

---

# 🗃️ MongoDB Setup

Create a MongoDB Atlas project and cluster.

For local development:

1. Create a MongoDB Atlas account.
2. Create a project.
3. Create an M0 cluster.
4. Create a database user.
5. Configure network access.
6. Obtain the Python connection string.
7. Add the connection string to `MONGODB_URL`.
8. Run the MongoDB notebook to upload the dataset.

The data can then be verified from:

```text
MongoDB Atlas
    ↓
Database
    ↓
Browse Collections
```

---

# ▶️ Run the Training Pipeline

Once MongoDB and environment variables are configured:

```bash
python demo.py
```

The complete pipeline runs through:

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Pushing
```

Successful model promotion results in the model being uploaded to S3.

---

# 🌐 Run the FastAPI Application Locally

```bash
python app.py
```

The API will run on:

```text
http://127.0.0.1:5000
```

Open the URL in your browser to access the application.

---

# 🚀 AWS Deployment

The production environment is hosted on:

```text
AWS EC2
```

Current deployment architecture:

```text
GitHub
   ↓
GitHub Actions
   ↓
Self-Hosted Runner
   ↓
AWS EC2
   ↓
FastAPI
   ↓
S3
   ↓
Production Model
```

The deployed application is exposed through EC2 port:

```text
5000
```

---

# 🔄 Complete End-to-End Workflow

A complete production workflow looks like this:

### Step 1 — Data

```text
Vehicle Insurance Dataset
        ↓
MongoDB Atlas
```

### Step 2 — Ingestion

```text
MongoDB
   ↓
Data Ingestion Component
   ↓
DataFrame
```

### Step 3 — Validation

```text
Raw Data
   ↓
Schema Validation
   ↓
Validated Data
```

### Step 4 — Transformation

```text
Validated Data
   ↓
Encoding
   ↓
Scaling
   ↓
Feature Engineering
```

### Step 5 — Balancing

```text
Training Data
   ↓
SMOTEENN
   ↓
Balanced Data
```

### Step 6 — Training

```text
Balanced Data
   ↓
Random Forest
   ↓
Trained Model
```

### Step 7 — Evaluation

```text
New Model
     │
     ├───────────────┐
     ▼               ▼
New Performance   Production
                  Performance
     │               │
     └───────┬───────┘
             ▼
      Model Comparison
             │
       Better Model?
        /          \
      YES           NO
       │             │
       ▼             ▼
      S3           Reject
```

### Step 8 — Deployment

```text
Git Push
   ↓
GitHub Actions
   ↓
Docker / ECR
   ↓
EC2
   ↓
FastAPI
```

### Step 9 — Prediction

```text
User Input
   ↓
FastAPI
   ↓
Prediction Pipeline
   ↓
Preprocessing
   ↓
Production Model
   ↓
Prediction
```

---

# 📊 Current Model Performance

Latest trained model:

| Metric    |      Score |
| --------- | ---------: |
| F1 Score  | **0.9316** |
| Precision | **0.8803** |
| Recall    | **0.9892** |

Production model before promotion:

| Metric   |      Score |
| -------- | ---------: |
| F1 Score | **0.4311** |

### Model Promotion

The new model significantly outperformed the previous production model and was therefore promoted.

This demonstrates an important MLOps principle:

> **A new model should not automatically replace a production model without evaluation.**

---

# 🧠 Key Engineering Concepts Demonstrated

This project demonstrates practical understanding of:

### Machine Learning

* Supervised learning
* Binary classification
* Random Forest
* Feature engineering
* Feature preprocessing
* Class imbalance
* SMOTEENN
* Model evaluation

### Software Engineering

* Modular Python architecture
* Object-oriented programming
* Configuration management
* Package management
* Logging
* Exception handling
* Separation of concerns

### MLOps

* Automated ML pipelines
* Data validation
* Reproducible transformations
* Model artifacts
* Model evaluation
* Model promotion
* Model registry
* Prediction pipelines

### Cloud

* AWS S3
* AWS EC2
* AWS IAM
* Amazon ECR
* Cloud-hosted application deployment

### DevOps

* Docker
* Git
* GitHub
* GitHub Actions
* CI/CD
* Self-hosted runners
* Automated deployment

---

# 🔒 Security Considerations

The project follows several security practices:

* AWS credentials are not hardcoded into source code.
* `.env` is excluded from Git.
* EC2 uses an IAM role for AWS access.
* Sensitive configuration is stored through environment variables.
* Production model access is controlled through AWS IAM permissions.

For a production enterprise deployment, additional improvements would include:

* Least-privilege IAM policies
* Restricted MongoDB network access
* HTTPS/TLS
* AWS Secrets Manager
* Private subnets
* Application Load Balancer
* Monitoring and alerting
* Automated testing
* Model/data drift monitoring

---

# 📈 Future Improvements

The current system provides a complete MLOps foundation, but it can be extended further.

### MLOps Improvements

* MLflow experiment tracking
* DVC-based dataset versioning
* Automated model versioning
* Model drift detection
* Data drift monitoring
* Automated retraining
* Model performance dashboards

### Cloud Improvements

* AWS ECS/EKS deployment
* Application Load Balancer
* Auto Scaling
* CloudWatch monitoring
* AWS Secrets Manager
* Infrastructure as Code using Terraform

### ML Improvements

* Hyperparameter optimization
* XGBoost / LightGBM comparison
* Cross-validation
* Explainable AI with SHAP
* Feature importance dashboard
* Probability calibration

### CI/CD Improvements

* Automated unit tests
* Integration tests
* Docker image scanning
* Automated rollback
* Blue-green deployment
* Deployment health checks

---

# 🎓 What This Project Demonstrates

This project was built to demonstrate that machine learning development is not limited to training a model in a Jupyter notebook.

It covers the complete journey:

```text
Data
 ↓
Engineering
 ↓
Validation
 ↓
Feature Engineering
 ↓
Machine Learning
 ↓
Evaluation
 ↓
Model Registry
 ↓
Cloud
 ↓
Docker
 ↓
CI/CD
 ↓
Deployment
 ↓
Real-Time Prediction
```

The primary focus is on building an ML system that is:

**Modular → Reproducible → Evaluated → Deployable → Maintainable**

---

# 👨‍💻 Author

### Srijan Srivastava

**Aspiring AI/ML Engineer | Data Scientist**

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* MLOps
* NLP
* Cloud & Deployment
* Production ML Systems

### GitHub

https://github.com/ssrijan579-cell

---

# ⭐ Project Highlights

If you found this project useful, consider giving the repository a ⭐.

The project demonstrates an end-to-end approach to taking a Machine Learning model from **raw data to a cloud-deployed prediction service using modern MLOps practices.**
