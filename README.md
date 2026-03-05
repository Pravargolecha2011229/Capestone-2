# 🌍 GlobeTrek AI — Cultural Travel Planner

> AI-powered cultural travel planning platform built with Streamlit + Google Gemini

## ✨ Features

| Feature | Description |
|---|---|
| ✈️ **AI Trip Planner** | Full day-by-day itineraries powered by Gemini Pro |
| 🤖 **AI Chatbot** | GlobeBot travel assistant for real-time Q&A |
| 📊 **Analytics Dashboard** | Interactive charts, maps & community stats |
| ⭐ **Community Reviews** | Live-updating reviews for destinations |
| 💬 **Feedback System** | Platform feedback with live community feed |
| ❤️ **Favourites** | Save destinations with AI insights |
| 📝 **Travel Notes** | Personal travel journal / note-taking |
| 🌍 **Destination Explorer** | Browse 30+ curated cultural destinations |
| 🌤️ **Weather Preview** | Climate preview for your travel dates |
| 👤 **User Profiles** | Full auth system with saved itineraries |
| 🌐 **Multilingual** | Itineraries in 9 languages |
| 📥 **Data Export** | Download your personal data as JSON |

## 🚀 Deploy on Streamlit Cloud

### 1. Fork / Clone this repo
```bash
git clone https://github.com/yourusername/globetrek-ai.git
cd globetrek-ai
```

### 2. Get a Gemini API Key
Visit [Google AI Studio](https://makersuite.google.com/app/apikey) — it's free.

### 3. Create secrets file
```toml
# .streamlit/secrets.toml
GEMINI_API_KEY = "AIza..."
```

### 4. Deploy on Streamlit Cloud
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → `app.py`
4. Add `GEMINI_API_KEY` in **App Settings → Secrets**
5. Click **Deploy**

### 5. Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 File Structure
```
globetrek-ai/
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── secrets.toml        # API keys (DO NOT commit)
└── dataset/
    └── Tourist_Destinations.csv   # Optional: real dataset
```

## 📊 Dataset
The app works with a built-in sample of 30 destinations.
To use the full dataset, place `Tourist_Destinations.csv` in a `dataset/` folder.

Required columns: `site_name`, `country`, `site_type`, `rating`, `budget_per_day`, `best_season`

## 🎨 Tech Stack
- **Frontend:** Streamlit + custom CSS (Midnight Teal dark theme)
- **AI:** Google Gemini Pro API
- **Charts:** Plotly Express & Graph Objects
- **Database:** SQLite (persistent across sessions)
- **Auth:** SHA-256 password hashing

## 📄 License
MIT License — feel free to use and modify.
