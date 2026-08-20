# 🛡️ Phishing URL Detector using Machine Learning

An AI-powered cybersecurity web application designed to detect malicious phishing URLs in real-time using structural URL features, lexical metrics, and Machine Learning classification algorithms.

![Dashboard Preview](dashboard.png)

## 🚀 Key Features
- **Real-Time Analysis:** Instantly scans URLs to detect security threats.
- **Explainable AI (XAI) Engine:** Breaks down specific security risk factors (e.g., missing HTTPS, domain spoofing hyphens, suspicious subdomains).
- **Machine Learning Powered:** Utilizes a Random Forest classifier trained on key lexical and structural features.
- **User-Friendly Dashboard:** Clean and responsive Streamlit interface for quick domain inspection.

## 🛠️ Tech Stack & Tools
- **Core Language:** Python 3
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Feature Parsing:** `tldextract`, `regex`
- **Web Interface:** Streamlit

## 📁 Repository Structure
