# 📊 YouTube Comment Sentiment Analyzer 🎥

This is a Streamlit-based web app that performs **sentiment analysis** on **YouTube video comments** using the **VADER SentimentIntensityAnalyzer** from NLTK. The app fetches comments using the **YouTube Data API v3** and classifies them into **Positive**, **Neutral**, or **Negative**, providing an overall sentiment label for the video.

---

## 🚀 Demo

> 💡 Coming soon: Add your demo video or Streamlit deployment link here (e.g., Streamlit Cloud or YouTube).

---

## 🔍 Features

- 🔗 Input any public YouTube video URL
- 📥 Automatically fetches up to 100 top-level comments and replies
- 🧠 Uses **VADER** sentiment analysis
- 📈 Displays results with bar chart using `matplotlib`
- 🟢 Returns the overall sentiment: **Positive**, **Negative**, or **Neutral**
- 🌐 Fully browser-based using **Streamlit**

---

## 📸 Sample Output

| Sentiment Chart | Output Label |
|------------------|--------------|
| ![Sample Chart](<img width="1008" height="867" alt="image" src="https://github.com/user-attachments/assets/34eab13e-dd14-4f39-a780-7d5b9519f707" />) | `Positive Video` |

---

## 🛠️ Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| Python | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| NLTK | Sentiment analysis with VADER |
| Streamlit | Web-based app interface |
| Google API Client | YouTube Data API access |
| Matplotlib | Plotting sentiment results |

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.7+
- Google API Key for YouTube Data API v3  
  (Generate from: [https://console.developers.google.com/](https://console.developers.google.com/))

### 📥 Install Requirements

```bash
pip install pandas numpy matplotlib nltk streamlit google-api-python-client
```

Also download VADER lexicon:

```bash
python -m nltk.downloader vader_lexicon
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

Then open in your browser:  
[http://localhost:8501](http://localhost:8501)

---

## 🔑 API Key Setup

Replace the `api_key` variable in your code with your own YouTube API key:

```python
api_key = 'YOUR_OWN_API_KEY'
```

---

## 📌 Example Usage

1. Paste any YouTube video link (e.g., `https://youtu.be/dQw4w9WgXcQ`)
2. Click **Predict**
3. Wait while comments are fetched and analyzed
4. See bar chart and overall video sentiment

---

## 📚 Use Cases

- Detect public opinion about a video
- Evaluate content engagement sentiment
- Educational projects in NLP
- Dashboard integration for content creators

---

## 🧠 Future Improvements

- Add support for large comment sets using pagination
- Display sample comments with their sentiment
- Allow keyword-based filtering
- Add deployment using Streamlit Cloud

---

## 📜 License

MIT License – Feel free to use and modify.

---

## 🤝 Credits

- [NLTK](https://www.nltk.org/)
- [Streamlit](https://streamlit.io/)
- [Google API Client](https://github.com/googleapis/google-api-python-client)

---

## 🙋‍♂️ Author

Made by Vinoth Kumar S – If you like it, ⭐ the repo!
