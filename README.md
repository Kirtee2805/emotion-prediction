# 😊 Emotion Predictor using NLP

An NLP-based Emotion Prediction System that analyzes user text and predicts emotions such as **Sadness, Anger, Love, Surprise, Fear, and Joy** using **TF-IDF Vectorization** and **Logistic Regression**. The project includes an interactive web application built with Streamlit.

## 🚀 Features

* Text preprocessing and cleaning
* URL, HTML tag, and emoji removal
* TF-IDF Vectorization
* Logistic Regression Classifier
* Real-time emotion prediction
* Interactive Streamlit interface
* Fast and lightweight model deployment

## 🎯 Supported Emotions

* 😢 Sadness
* 😡 Anger
* ❤️ Love
* 😲 Surprise
* 😨 Fear
* 😄 Joy

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Streamlit
* Joblib

## 📂 Project Structure

```text
Emotion-Predictor/
│
├── app.py
├── emotion_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

## ⚙️ Model Pipeline

```text
User Text
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression
    ↓
Emotion Prediction
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/emotion-predictor.git
cd emotion-predictor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🧪 Example Inputs

### Joy 😄

I just got my dream internship and I am extremely excited.

### Sadness 😢

I feel completely alone and nothing seems to be going right today.

### Anger 😡

I am really frustrated because nobody listened to my concerns.

### Fear 😨

Walking through the dark street at night made me feel nervous and scared.

### Surprise 😲

I couldn't believe my eyes when I saw the results.

### Love ❤️

Spending time with my family makes me feel warm and happy.

## 📈 Future Improvements

* Deep Learning Models (LSTM, GRU)
* Transformer Models (BERT)
* Confidence Score Visualization
* Multi-language Emotion Detection
* Emotion Analytics Dashboard
* Cloud Deployment

## 👨‍💻 Author

Kirtee

Built using Natural Language Processing, Machine Learning, and Streamlit.
