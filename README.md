# 🩺 DermAI – Skin Cancer Classification using Deep Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-CNN-green)
![Dataset](https://img.shields.io/badge/Dataset-HAM10000-orange)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

---

## 👥 Team Members

<div align="center">

### 🚀 Project Team

**Ibad Rehman** & **Zaid Rizwan**

*Deep Learning | Computer Vision | Medical AI*

</div>

---

## 📌 About The Project

Skin cancer is one of the most common forms of cancer worldwide. Early detection can significantly improve treatment outcomes.

This project aims to develop an AI-powered skin lesion classification system using the **HAM10000 dataset** and compare the performance of modern Convolutional Neural Networks.

The final system will allow users to upload an image of a skin lesion and receive a prediction of the lesion category.

---

## 🎯 Objectives

- 📷 Classify dermatoscopic skin lesion images
- 🧠 Train and compare multiple CNN architectures
- 📊 Evaluate model performance using standard metrics
- 🚀 Deploy a user-friendly prediction application
- 🔬 Explore the application of Deep Learning in Healthcare

---

## 🗂 Dataset

### HAM10000 Dataset

**Human Against Machine with 10,000 Training Images**

The dataset contains dermatoscopic images belonging to seven different skin lesion categories.

### Classes

| Code | Lesion Type |
|--------|--------|
| akiec | Actinic Keratoses |
| bcc | Basal Cell Carcinoma |
| bkl | Benign Keratosis |
| df | Dermatofibroma |
| mel | Melanoma |
| nv | Melanocytic Nevus |
| vasc | Vascular Lesions |

---

## 🏗 Project Workflow

```text
HAM10000 Dataset
        │
        ▼
Data Exploration
        │
        ▼
Data Preprocessing
        │
        ▼
Image Augmentation
        │
        ▼
Model Training
        │
        ▼
Performance Evaluation
        │
        ▼
Model Comparison
        │
        ▼
Web Application Deployment
```

---

## 🧠 Models

### 🔥 ResNet50

- Residual Learning Architecture
- Skip Connections
- Strong Baseline Performance

### ⚡ EfficientNet-B0

- Compound Scaling
- Lightweight Architecture
- High Accuracy with Fewer Parameters

---

## 📊 Evaluation Metrics

The models will be evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 📈 Results Dashboard

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|---------|---------|---------|---------|
| ResNet50 | ⏳ Pending | ⏳ Pending | ⏳ Pending | ⏳ Pending |
| EfficientNet-B0 | ⏳ Pending | ⏳ Pending | ⏳ Pending | ⏳ Pending |

---

## 📂 Project Structure

```text
DermAI-Skin-Cancer-Classification/
│
├── data/
├── notebooks/
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
├── app/
│   └── streamlit_app.py
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technology Stack

### Programming

- Python

### Deep Learning

- PyTorch
- Torchvision

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Version Control

- Git
- GitHub

---

## 🚀 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/DermAI-Skin-Cancer-Classification.git

cd DermAI-Skin-Cancer-Classification
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running The Project

Train Model

```bash
python src/train.py
```

Evaluate Model

```bash
python src/evaluate.py
```

Run Web Application

```bash
streamlit run app/streamlit_app.py
```

---

## 📸 Project Gallery

### Dataset Samples
🚧 Coming Soon

### Training Curves
🚧 Coming Soon

### Confusion Matrix
🚧 Coming Soon

### Streamlit Application
🚧 Coming Soon

---

## 🔮 Future Improvements

- Vision Transformers (ViT)
- MobileNet Comparison
- Explainable AI (Grad-CAM)
- Cloud Deployment
- Real-Time Mobile Integration

---

## 📚 References

- HAM10000 Dataset
- PyTorch Documentation
- ResNet Research Paper
- EfficientNet Research Paper

---

## 🤝 Contributors

This project is being developed collaboratively by:

### 👨‍💻 Ibad Rehman
### 👨‍💻 Zaid Rizwan

Together we are responsible for:

✅ Data Collection  
✅ Data Preprocessing  
✅ Model Development  
✅ Model Training  
✅ Evaluation  
✅ Documentation  
✅ Deployment

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.

---

## 📜 License

This project is developed for academic and research purposes.

© 2026 Ibad Rehman & Zaid Rizwan
