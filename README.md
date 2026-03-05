# AI Customer Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Transformers](https://img.shields.io/badge/NLP-HuggingFace-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive AI-powered dashboard that analyzes customer feedback and predicts sentiment using Natural Language Processing.  
The application provides sentiment prediction, AI explanations, voice output, and visual analytics.

---

## Live Demo

Demo App:  
https://ai-customer-sentiment-analyzer.onrender.com/

---

## Features

• Real-time sentiment prediction  
• AI explanation for sentiment results  
• Interactive analytics dashboard  
• 3D visualization of feedback insights  
• Word cloud visualization of customer feedback  
• Voice response using text-to-speech  
• Modern dark-themed dashboard UI

---

## Tech Stack

Python  
Streamlit  
HuggingFace Transformers  
PyTorch  
Pandas  
NumPy  
Plotly  
gTTS (Text-to-Speech)

---

## Dashboard Components

Sentiment Result Card  
Displays predicted sentiment with confidence score.

Analytics Dashboard  
Includes:

• Sentiment Distribution Pie Chart  
• Confidence Score Gauge Chart  
• 3D Customer Feedback Scatter Plot

Word Cloud Visualization  
Shows frequently used words in customer feedback.

AI Explanation Panel  
Provides a short AI-generated explanation of the sentiment prediction.

---

## Project Structure

```
ai-customer-sentiment-analyzer
│
├── app.py
├── sentiment_model.py
├── analytics.py
├── utils.py
├── requirements.txt
├── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-customer-sentiment-analyzer.git
```

Go to the project directory

```
cd ai-customer-sentiment-analyzer
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

## Example Use Cases

Customer feedback analysis  
Product review sentiment detection  
Social media sentiment monitoring  
Business customer satisfaction insights

---

## Future Improvements

• Emotion detection (anger, joy, sadness)  
• Multi-language sentiment analysis  
• Real-time data streaming  
• Voice input for sentiment analysis  
• Dashboard performance optimization

---

## Author

Hari Krishna

---

## License

This project is open-source and available for educational and research purposes.
