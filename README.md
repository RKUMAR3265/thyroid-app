# AI Powered System for Early Diagnosis of Thyroid Cancer

## Overview
This project is an AI-based multimodal thyroid cancer diagnosis system that combines ultrasound image analysis and clinical data prediction to provide early and accurate thyroid cancer risk assessment.

The system uses:
- CNN (Convolutional Neural Network) for ultrasound image classification
- Random Forest Machine Learning model for clinical data analysis
- Weighted fusion technique for final prediction

The final output classifies patients into:
- Low Risk
- Medium Risk
- High Risk

---

## Features

- Thyroid ultrasound image analysis
- Clinical biomarker prediction
- AI-generated risk classification
- Secure login system
- Patient registration module
- Medical report generation
- Probability graph visualization
- Web-based interface using Flask

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning & Deep Learning
- TensorFlow
- Keras
- Scikit-learn

### Data Processing
- NumPy
- Pandas

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Project Structure

```text
thyroid_app/
│
├── app.py
│
├── model/
│   ├── clinical_model.pkl
│   └── image_model.h5
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── logo.jpg
│   └── uploads/
│
├── templates/
│   ├── login.html
│   ├── registration_form.html
│   ├── patient_form.html
│   ├── result.html
│   ├── verify.html
│   ├── reset.html
│   └── forgot.html
│
├── dataset/
│
├── requirements.txt
│
└── README.md
```

---

## Workflow

### Step 1: Image Analysis
Ultrasound images are processed using a CNN model to extract texture and shape-based features.

### Step 2: Clinical Data Analysis
Clinical parameters such as:
- TSH
- T3
- T4
- Age
- Gender

are analyzed using a Random Forest model.

### Step 3: Multimodal Fusion
Both model outputs are combined using a weighted fusion formula:

```math
Pfinal = 0.4 × Pimg + 0.6 × Pclin
```

### Step 4: Risk Classification
- Pfinal < 0.3 → Low Risk
- 0.3 – 0.6 → Medium Risk
- > 0.6 → High Risk

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Powered-Thyroid-Cancer-Diagnosis.git
```

### Navigate to Project Folder

```bash
cd AI-Powered-Thyroid-Cancer-Diagnosis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Results

- Accuracy: 94.3%
- Improved diagnostic reliability using multimodal AI
- Reduced dependency on manual interpretation
- Better clinical decision support

---

## Future Enhancements

- ResNet / EfficientNet integration
- Explainable AI (XAI)
- Mobile application deployment
- Multi-disease prediction
- EHR integration



## License

This project is developed for educational and research purposes.
