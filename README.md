# 🚀 El País Opinion Scraper with BrowserStack Parallel Execution

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![BrowserStack](https://img.shields.io/badge/BrowserStack-Automate-orange)
![Status](https://img.shields.io/badge/Project-Complete-success)

---

## 📌 Project Overview

This project demonstrates:

- Web scraping using Selenium
- Translation API integration
- Text processing and word frequency analysis
- Cross-browser parallel execution using BrowserStack

The script scrapes the first 5 articles from the **Opinion** section of El País (Spanish news website), translates the article titles into English, analyzes repeated words, and executes the complete solution across multiple browsers and devices in parallel using BrowserStack.

---

## 🛠 Features

### 🔹 1. Web Scraping (Selenium)

- Navigate to: https://elpais.com/opinion/
- Ensure Spanish content
- Extract first 5 article links
- Scrape:
  - Spanish article title
  - Article content
  - Cover image (if available)
- Download and store images locally

---

### 🔹 2. Translation API Integration

- Uses RapidAPI Google Translate endpoint
- Translates Spanish titles to English
- Secure credential handling via `.env`
- Graceful error handling for failed API calls

---

### 🔹 3. Word Frequency Analysis

- Combine translated titles
- Normalize text (lowercase + punctuation removal)
- Count word frequency
- Display words repeated more than twice

---

### 🔹 4. BrowserStack Parallel Execution

The full solution runs across **5 environments in parallel**:

- Windows 11 – Chrome
- Windows 11 – Edge
- macOS Ventura – Safari
- Samsung Galaxy S22 – Chrome
- iPhone 14 – Safari

Each environment runs the entire scraping + translation workflow independently.

Parallel execution is implemented using `ThreadPoolExecutor`.

---

## 🏗 Architecture Overview

```
Local Machine
     │
     ├── main.py  → Local Execution
     │
     └── browserstack_runner.py
              │
              ▼
      BrowserStack Cloud
      ├── Windows + Chrome
      ├── Windows + Edge
      ├── macOS + Safari
      ├── Samsung Galaxy S22
      └── iPhone 14
              │
              ▼
        El País Website
              │
              ▼
     Scraper → Translator → Analyzer
```

---

## 📂 Project Structure

```
browserstack_elpais/
│
├── main.py                  # Local execution
├── browserstack_runner.py   # Parallel BrowserStack execution
├── scraper.py               # Scraping logic
├── translator.py            # Translation API integration
├── analyzer.py              # Word frequency analysis
├── images/                  # Downloaded cover images
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
conda create -n elpais_bs python=3.10
conda activate elpais_bs
pip install -r requirements.txt
```

---

### 2️⃣ Create `.env` File

Create a `.env` file in the root directory:

```
RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=google-api31.p.rapidapi.com

BROWSERSTACK_USERNAME=your_browserstack_username
BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
```

⚠️ Do NOT commit `.env` to GitHub.

---

## ▶️ Run Locally

```bash
python main.py
```

This will:

- Scrape first 5 opinion articles
- Download cover images
- Translate titles
- Perform word frequency analysis

---

## 🌐 Run on BrowserStack (Parallel Execution)

```bash
python browserstack_runner.py
```

This will:

- Execute the complete solution remotely
- Run across 5 browsers/devices in parallel
- Appear in BrowserStack Automate dashboard

---

## 📸 Execution Screenshots (Optional)

If you add screenshots inside `assets/` folder:

![Local Execution](assets/paralleltests.png)
![BrowserStack Parallel](assets/tests1.png)
![Session Recording](assets/tests2.png)




## ✅ Verification

Execution is verified through:

- Console output
- Downloaded images in `/images`
- BrowserStack session recordings
- BrowserStack command logs
- Parallel build dashboard view

---

## 🧰 Technologies Used

- Python 3.10
- Selenium 4
- Requests
- RapidAPI (Google Translate)
- BrowserStack Automate
- ThreadPoolExecutor (concurrent execution)
- dotenv (secure credential handling)

---

## 🔒 Security Considerations

- API keys stored securely in `.env`
- No credentials committed to repository
- Each BrowserStack session uses independent WebDriver instance

---

## 🎯 Assignment Completion Summary

✔ Web scraping implemented  
✔ Cover images downloaded  
✔ Titles translated via API  
✔ Word frequency analysis completed  
✔ Local validation done  
✔ BrowserStack parallel execution across 5 environments  
✔ Verified via cloud session recordings  

Project successfully meets all assignment requirements.
