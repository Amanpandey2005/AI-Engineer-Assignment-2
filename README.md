🚀 AI Review Analyzer: End-to-End Sentiment Pipeline
📌 Overview

The AI Review Analyzer is an automated pipeline that extracts, processes, and analyzes product reviews from e-commerce websites. It transforms raw, unstructured customer feedback into meaningful insights using web scraping and Large Language Models (LLMs).

This project demonstrates how to integrate data extraction + NLP + AI models into a complete real-world system.

🎯 Objective
Automate review extraction from websites
Clean and preprocess textual data
Generate sentiment insights using LLM
Store structured outputs for analysis
✨ Features
🔍 Web Scraping
Extracts review text, usernames, and ratings
Works on standard HTML-based e-commerce pages
🧹 Data Preprocessing
Removes noise and special characters
Handles encoding issues
Token-based text chunking using tiktoken
🤖 AI Sentiment Analysis
Uses Mistral-7B-Instruct via Hugging Face API
Generates concise sentiment summaries
📊 Data Storage
Saves results into a CSV file
Includes:
Cleaned reviews
Ratings
AI-generated sentiment
🔐 Security
Uses .env file for API key management
🛠️ Tech Stack
Language: Python
Web Scraping: BeautifulSoup4, Requests
Data Processing: Pandas
LLM Integration: OpenAI Python Client (Hugging Face)
Tokenization: Tiktoken
📂 Project Structure
AI-Review-Analyzer/
│── scraper.py        # Extracts reviews from website
│── processor.py      # Cleans and preprocesses data
│── llm_service.py    # Handles LLM API calls
│── main.py           # Entry point
│── requirements.txt
│── .env              # API keys (not uploaded to GitHub)
│── data/
│    └── processed_reviews.csv
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/AI-Review-Analyzer.git
cd AI-Review-Analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create a .env file:

HF_TOKEN=your_hugging_face_token_here
▶️ Usage

Run the application:

python main.py
🔗 Test URL

Use this sample URL:

https://www.snapdeal.com/product/leavess-6-socket-extension-board/645549433371/reviews
📤 Output

Processed data will be saved in:

data/processed_reviews.csv
🏗️ Architecture
        Website
           ↓
      scraper.py
           ↓
     processor.py
           ↓
     llm_service.py
           ↓
   processed_reviews.csv
⚠️ Limitations
❌ Some websites block scraping (403 errors)
❌ JavaScript-heavy pages not supported
❌ Hugging Face API rate limits (free tier)
🔮 Future Improvements
Add Streamlit Dashboard for visualization
Use Selenium/Playwright for dynamic scraping
Implement aspect-based sentiment analysis
Deploy as a web application
🎥 Demo

👉 Add your demo video link here


Link used for testing of SnapDeal :
https://m.snapdeal.com/product/leavess-6-socket-extension-board/645549433371?vendorCode=Sf7f5a&pa=true&fv=true&supc=SDL448569501&utm_campaign=category_fallback&utm_medium=ProductAds&isSellerPage=true#reviews

👨‍💻 Author
Aman Pandey

⭐ Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.
