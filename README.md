---

# **US Visa Prediction System**

## **Overview**

The **US Visa Prediction System** is a machine learning-powered solution designed to predict the approval status of US visa applications based on historical data and applicant details. The project leverages state-of-the-art machine learning algorithms, cloud deployment, and containerized infrastructure to ensure scalability, reliability, and ease of integration.

This project is built with **FastAPI**, a modern Python web framework, and integrates with **AWS ECR**, **AWS S3**, and **MongoDB** for data management and deployment.

---

## **Features**

- Predict visa application approval with high accuracy.
- Clean and responsive UI for user inputs using **FastAPI** and **HTML**.
- Fully containerized using **Docker** for portability.
- Deployed to **AWS EC2** using **GitHub Actions** CI/CD pipelines.
- Scalable data ingestion and storage using **MongoDB Atlas**.
- Cloud storage for model artifacts using **AWS S3**.
- Automated model training, evaluation, and deployment pipelines.

---

## **Architecture Workflow**

1. **Data Ingestion**:
   - Data is retrieved from **MongoDB Atlas**.
   - The raw data is preprocessed and split into training and testing datasets.

2. **Data Validation**:
   - Schema validation ensures data quality and consistency.
   - Drift detection identifies changes in data distributions.

3. **Data Transformation**:
   - Feature engineering and encoding are performed to prepare the data for training.

4. **Model Training**:
   - Uses algorithms like Random Forest, XGBoost, and KNN for training.
   - Hyperparameter tuning with GridSearchCV.
   - The best model is selected based on performance metrics.

5. **Model Evaluation**:
   - Compares trained models with production models using F1 score.
   - The model is accepted if it outperforms the current production model.

6. **Model Deployment**:
   - Model artifacts are pushed to **AWS S3**.
   - The web application is containerized and deployed via **AWS ECR** and **EC2**.

7. **Prediction Pipeline**:
   - User inputs are processed through a REST API.
   - The model predicts visa approval status in real time.

---

## **Technologies Used**

### **Backend**
- **FastAPI**: For creating REST APIs.
- **Python**: Programming language for data processing and machine learning.

### **Machine Learning**
- **Scikit-Learn**
- **XGBoost**
- **CatBoost**
- **Imbalanced-Learn**

### **Data Storage**
- **MongoDB Atlas**: Cloud database for storing raw and processed data.
- **AWS S3**: For storing model artifacts.

### **Infrastructure**
- **Docker**: For containerizing the application.
- **AWS ECR**: Hosting the Docker images.
- **AWS EC2**: Deploying the application.

### **CI/CD**
- **GitHub Actions**: Automating testing, building, and deployment pipelines.

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/US-Visa-Prediction-System.git
cd US-Visa-Prediction-System
```

### **2. Install Dependencies**
Ensure you have Python 3.12+ and Docker installed.
```bash
pip install -r requirements.txt
```

### **3. Environment Variables**
Set up the following environment variables:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `MONGODB_URL`
- `ECR_REPO`

### **4. Run Locally**
To start the application locally:
```bash
python app.py
```

### **5. Dockerize and Deploy**
#### Build Docker Image
```bash
docker build -t us-visa-prediction .
```

#### Run Docker Container
```bash
docker run -p 8080:8080 --env-file .env us-visa-prediction
```

---

## **Deployment Workflow**

### **GitHub Actions CI/CD**
The deployment is automated using a multi-step workflow:
1. **Continuous Integration**:
   - Builds and tests the application.
   - Pushes the Docker image to **AWS ECR**.
2. **Continuous Deployment**:
   - Pulls the Docker image from **AWS ECR**.
   - Runs the containerized application on **AWS EC2**.

---

## **Usage**

### **Prediction via Web Application**
1. Access the application at `http://<your-ec2-instance>:8080`.
2. Enter the applicant's details (e.g., education, region, wage).
3. Click **Predict Visa Status**.
4. View the predicted result (Visa Approved or Not Approved).

---

## **Project Structure**

```plaintext
US-Visa-Prediction-System/
├── app.py                  # Main application entry point
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
├── static/                 # CSS and static assets
├── us_visa/                # Application modules
│   ├── components/         # Data processing and ML pipeline components
│   ├── entity/             # Entity definitions
│   ├── pipeline/           # Training and prediction pipelines
│   ├── utils/              # Helper functions and utilities
│   └── cloud_storage/      # AWS S3 integration
└── .github/workflows/      # CI/CD pipeline configuration
```


## **Contributing**

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Contact**

**Author**: Abdul Ghaffar Ansari  
**Email**: abdulghaffaransari9@gmail.com 
**LinkedIn**: [LinkedIn Profile](<[linkedin-url](https://www.linkedin.com/in/abdulghaffaransari/)>)  


---
