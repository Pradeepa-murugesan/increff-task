# Increff Assignment: Sentiment Analysis of Customer Reviews

This is an **AI-Powered Sentiment Analysis System** that automatically classifies customer reviews into `positive`, `neutral`, or `negative` categories. The goal is to help businesses quickly assess customer sentiment and improve feedback-driven decisions. The system is built using `gemini-1.5-flash` for classification and features a complete UI/API stack using Streamlit and FastAPI.

---

## 📦 Tech Stack

- **🧠 Language Model:** Gemini 1.5 Flash API
- **🗃️ Database:** MongoDB (via PyMongo)
- **🧠 Text Embedding:** Sentence Transformers (all-MiniLM-L6-v2)
- **⚙️ Backend Framework:** FastAPI (Python)
- **🌐 Frontend Framework:** Streamlit
- **🧪 Development Environment:** Localhost (for development & testing)

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 🖥️ Backend Setup (FastAPI)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pradeepa-Murugesan/increff-task.git
   cd increff-task/backend
    ```
2. **Create a virtual environment**
   ```
   python -m venv sentiment-env
   ```
   
3. **Activate the environment**
   # for windows
   ```
   sentiment-env\Scripts\activate
   ```

   # for linux\macOS
   ```
   source sentiment-env/bin/activate
   ```

5. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

6. **Run the FastAPI server on port 8000**
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

7. **Frontend Setup (Streamlit)**
   ```
   cd ../frontend
   ```

8. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

9. **Run the Streamlit app**
   ```
   streamlit run app.py
   ```

## ⚙️ Preprocessing Steps
- Removed punctuation, emojis, and special symbols
- Lowercased the input text
- Tokenized using Hugging Face tokenizer
- Removed stop words
- Normalized the reviews
- Handled blank or invalid entries

## 🤖 Model Workflow
- The /analyse FastAPI endpoint takes a review as input
- Embeddings are generated via sentence-transformers
- Gemini-1.5-Flash is used for final sentiment classification
- For long reviews, sentiment is averaged across chunks

## 📊 Evaluation Metrics
### Metric	Value
- Accuracy	84.32%
- Precision	81.0%
- Recall	80.09%
- F1-Score	83.5%

## ⚠️ Challenges Faced
- Mixed reviews with both positive and negative tones
- Sarcasm and humor were hard to classify
- Differentiating neutral vs mildly positive/negative feedback
- Class imbalance toward positive sentiment

## 🔭 Future Improvements
### Model Fine-Tuning
- Use real-world product reviews to improve contextual accuracy.

### Multilingual Support
- Add language detection and auto-translation for non-English reviews.

### UI Enhancements
- Add file upload feature and sentiment distribution visualizations in Streamlit.

### Fake Review Detection
- Implement duplicate and bot-generated review detection using heuristics.

## 🖼️ Sample Output Screenshots

### 1. User Interface using Streamlit

![Streamlit UI](https://github.com/Pradeepa-murugesan/increff-task/blob/main/images/img-1.jpg)

### 2. Sample Output-1

![Output 1](https://github.com/Pradeepa-murugesan/increff-task/blob/main/images/img-2.jpg)

### 3. Sample Output-2

![Sample Output-2.1](https://github.com/Pradeepa-murugesan/increff-task/blob/main/images/img-3.jpg)

### 4. Sample Output-2

![Sample Output-2](https://github.com/Pradeepa-murugesan/increff-task/blob/main/images/img-4.jpg)


## ✅ Conclusion
#### This project showcases how large language models can be integrated into real-world applications for scalable, real-time sentiment analysis. It provided hands-on experience with FastAPI, Streamlit, and NLP pipelines using LLMs.
