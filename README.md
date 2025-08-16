# 🫀 Heart Disease Prediction System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive machine learning system for predicting heart disease risk using clinical parameters. This project implements and compares three state-of-the-art algorithms: **Logistic Regression**, **Support Vector Machine (SVM)**, and **Random Forest** to provide accurate cardiovascular risk assessment.

## 🎯 Project Motivation

Cardiovascular diseases (CVDs) are the leading cause of death worldwide, claiming approximately **17 million lives annually** according to the World Health Organization. Early detection and risk assessment are crucial for preventing heart disease complications. This project addresses the critical need for:

- **Early Detection**: Identifying at-risk patients before symptoms appear
- **Data-Driven Insights**: Leveraging machine learning to uncover complex patterns in clinical data
- **Clinical Decision Support**: Providing healthcare professionals with reliable predictive tools
- **Accessible Healthcare**: Creating user-friendly interfaces for risk assessment

## 🚀 Key Features

### 🔬 Advanced Machine Learning Pipeline
- **Comprehensive Data Preprocessing**: Handles missing values, outliers, and data normalization
- **Feature Engineering**: Optimizes clinical parameters for maximum predictive power
- **Hyperparameter Optimization**: Fine-tuned models using GridSearchCV for optimal performance
- **Cross-Validation**: Robust model validation to ensure generalizability

### 📊 Three Powerful Algorithms
1. **Logistic Regression (LR)**: Interpretable baseline model with probability outputs
2. **Support Vector Machine (SVM)**: Advanced non-linear classification with kernel functions
3. **Random Forest (RF)**: Ensemble learning with feature importance analysis

### 🎨 Interactive Web Application
- **User-Friendly Interface**: Flask-based web application for easy patient data input
- **Real-Time Predictions**: Instant risk assessment using trained models
- **Multi-Language Support**: Integrated translation API for global accessibility
- **Visual Results**: Clear, interpretable prediction outputs

### 📈 Comprehensive Analysis
- **Exploratory Data Analysis (EDA)**: Deep insights into data patterns and relationships
- **Performance Metrics**: Accuracy, Precision, Recall, F1-Score, and AUC analysis
- **ROC Curve Comparisons**: Visual model performance evaluation
- **Feature Importance**: Identification of key risk factors

## 🏆 Performance Results

| Model | Accuracy | Precision | Recall | F1-Score | AUC |
|-------|----------|-----------|--------|----------|-----|
| **Logistic Regression** | **85.96%** | **86.96%** | **80.00%** | **83.33%** | **0.915** |
| **Support Vector Machine** | **84.21%** | **85.71%** | **76.00%** | **80.54%** | **0.919** |
| **Random Forest** | **78.95%** | **81.25%** | **76.00%** | **78.55%** | **0.886** |

### 🎯 Key Findings
- **Logistic Regression** achieved the highest accuracy (85.96%) and lowest false negative rate (20%)
- **SVM** showed significant improvement after hyperparameter tuning (AUC: 0.728 → 0.919)
- **All models** demonstrated excellent clinical viability with AUC scores > 0.88

## 📁 Project Structure

```
heart-disease-prediction/
├── 📊 DataTraining/
│   ├── HeartDiseaseDataset.csv          # Cleveland Heart Disease dataset
│   ├── HeartDiseasePredictionAssignment.ipynb  # Main analysis notebook
│   └── 🤖 Models/
│       ├── lr_model.pkl                 # Trained Logistic Regression
│       ├── rf_model.pkl                 # Trained Random Forest
│       └── svm_model.pkl                # Trained SVM
├── 🌐 heart_disease_app/
│   ├── app.py                           # Flask web application
│   ├── 🤖 models/                       # Deployed model files
│   ├── 🎨 static/                       # CSS, JavaScript assets
│   └── 📄 templates/                    # HTML templates
└── 📖 README.md                         # Project documentation
```

## 🏥 Dataset Information

**Source**: Cleveland Heart Disease Dataset (UCI Machine Learning Repository)
- **Records**: 303 patient cases
- **Features**: 14 clinical parameters
- **Target**: Binary classification (Heart Disease: Yes/No)

### 📋 Clinical Features
| Feature | Description | Type |
|---------|-------------|------|
| `age` | Patient age | Numerical |
| `sex` | Gender (1 = male, 0 = female) | Categorical |
| `cp` | Chest pain type (0-3) | Categorical |
| `trestbps` | Resting blood pressure | Numerical |
| `chol` | Serum cholesterol level | Numerical |
| `fbs` | Fasting blood sugar > 120 mg/dl | Binary |
| `restecg` | Resting ECG results | Categorical |
| `thalach` | Maximum heart rate achieved | Numerical |
| `exang` | Exercise induced angina | Binary |
| `oldpeak` | ST depression induced by exercise | Numerical |
| `slope` | Slope of peak exercise ST segment | Categorical |
| `ca` | Number of major vessels (0-3) | Numerical |
| `thal` | Thalassemia type | Categorical |
| `target` | Heart disease diagnosis | Binary |

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.7+**: Primary programming language
- **Jupyter Notebook**: Interactive development environment
- **Flask**: Web application framework

### Machine Learning & Data Science
- **Scikit-learn**: Machine learning algorithms and evaluation
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Joblib**: Model serialization

### Visualization & Analytics
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualizations
- **Plotly**: Interactive charts

### Web Development
- **HTML5/CSS3**: Frontend structure and styling
- **JavaScript**: Client-side interactivity
- **Google Translate API**: Multi-language support

## 🚀 Quick Start Guide

### Prerequisites
```bash
# Python 3.7 or higher
python --version

# Recommended: Anaconda distribution
conda --version
```

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/jimsenglee/heart-disease-prediction.git
cd heart-disease-prediction
```

2. **Install Dependencies**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly flask joblib
pip install googletrans==4.0.0-rc1
```

3. **Run the Jupyter Notebook**
```bash
jupyter notebook DataTraining/HeartDiseasePredictionAssignment.ipynb
```

4. **Launch the Web Application**
```bash
cd heart_disease_app
python app.py
```

5. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 🔬 Scientific Methodology

### Hypothesis Testing
- **H₁**: Machine learning models (SVM, RF, LR) achieve statistically significant predictive accuracy for heart disease (AUC > 0.75)
- **H₀**: Models fail to achieve significant predictive accuracy (AUC ≤ 0.75)

### Validation Approach
- **Train-Test Split**: 80-20 ratio with stratified sampling
- **Cross-Validation**: 5-fold CV for robust performance estimation
- **Hyperparameter Tuning**: GridSearchCV with 3-fold inner CV
- **Statistical Testing**: Significance testing for performance differences

## 📊 Model Interpretability

### Feature Importance Analysis
The Random Forest model identified key predictive factors:
1. **Chest Pain Type (cp)**: Primary indicator of heart disease risk
2. **ST Depression (oldpeak)**: Exercise-induced cardiac stress marker
3. **Thalassemia (thal)**: Blood disorder indicator
4. **Number of Major Vessels (ca)**: Coronary artery involvement

### Clinical Implications
- **Logistic Regression**: Provides interpretable coefficients for clinical decision-making
- **SVM**: Excellent for complex, non-linear relationships in patient data
- **Random Forest**: Robust against overfitting with built-in feature selection

## 🌟 Future Enhancements

### Technical Improvements
- [ ] **Deep Learning Integration**: CNN/RNN models for advanced pattern recognition
- [ ] **Real-Time Monitoring**: Integration with wearable device data
- [ ] **Ensemble Methods**: Advanced model combination techniques
- [ ] **Explainable AI**: SHAP/LIME integration for model interpretability

### Clinical Applications
- [ ] **Multi-Class Classification**: Severity level prediction
- [ ] **Longitudinal Analysis**: Time-series prediction capabilities
- [ ] **Risk Stratification**: Personalized treatment recommendations
- [ ] **Clinical Validation**: Real-world hospital deployment studies

### Platform Enhancements
- [ ] **Mobile Application**: iOS/Android app development
- [ ] **API Development**: RESTful API for third-party integration
- [ ] **Database Integration**: Patient record management system
- [ ] **Security Features**: HIPAA-compliant data handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **UCI Machine Learning Repository** for providing the Cleveland Heart Disease dataset
- **Cleveland Clinic Foundation** for the original data collection
- **World Health Organization** for cardiovascular disease statistics and guidelines
- **Open Source Community** for the excellent tools and libraries used in this project

## 📞 Contact

**GitHub**: [@jimsenglee](https://github.com/jimsenglee)  
**Email**: gimsheng.lee@gmail.com

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐
