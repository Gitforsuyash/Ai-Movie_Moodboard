# 🎬 AI Movie Moodboard

An **interactive Streamlit web app** that analyzes the **emotional tone of a movie plot or vibe** using a transformer model and generates a **visual moodboard** that matches the detected emotion.  

  


---

[![LinkedIn – Connect with Me](https://img.shields.io/badge/LinkedIn-Suyash_Kulkarni-blue?style=for-the-badge&logo=linkedin)](www.linkedin.com/in/suyash-kulkarni-yes777)  


---

## ✨ Features

- 🎭 **Emotion Detection:** Detects emotion from text using `j-hartmann/emotion-english-distilroberta-base`.
- 🖼️ **Moodboard Generator:** Maps emotions to mood images from local folders.
- ⚡ **Instant Results:** See the raw emotion output and visual moodboard instantly.
- 🎨 **Streamlit UI:** Minimal, elegant, and interactive front-end.

---

## 🛠️ How It Works

1. You describe your movie vibe or plot.
2. A fine-tuned DistilRoBERTa model detects the dominant emotion.
3. The app loads emotion-specific images from `emotions/{emotion}/` folder.
4. A visual **moodboard** appears for that emotion.

---

## 🚀 Tech Stack

| Component | Use |
|----------|-----|
| 🐍 Python | Backend Logic |
| 🔥 Streamlit | Web App UI |
| 🤗 Hugging Face Transformers | Emotion Detection Model |
| 🖼️ Local Image Folders | Moodboards |
| 🧠 Model Used | `j-hartmann/emotion-english-distilroberta-base` |

---

## 📦 Installation

1. **Clone this repository**  
```bash
git clone https://github.com/your-username/ai-movie-moodboard.git
cd ai-movie-moodboard
```
2. **Set up**
   # Windows
   ```bash
    python -m venv venv
    venv\Scripts\activate

# macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
3. **Install Dependancies**
   ```bash
    pip install -r requirements.txt
4. **Folder Structure**
   
        ├── emotions/
        │   ├── anger/
        │   ├── fear/
        │   ├── joy/
        │   ├── neutral/
        │   ├── sadness/
        │   └── surprise/
        ├── app.py
        └── requirements.txt

5. **How to Run**
   ```bash
      streamlit run app.py
## 💡 Future Ideas
  🔍 Real-time image fetching from Unsplash/Pexels APIs
  
  🌍 Multilingual text input and model
  
  🎞️ Moodboard with GIFs or video clips
  
  ☁️ Deploy on Hugging Face Spaces or Streamlit Cloud




