import streamlit as st
import joblib
import pandas as pd
from extractor import extract_features

# Page Config
st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return joblib.load('phishing_model.pkl')

model = load_model()

st.title("🛡️ Cyber Security Phishing URL Detector")
st.markdown("""
    <h4 style='text-align: center; color: #1E90FF; font-weight: bold; margin-top: -15px;'>
        Built by Maaz Afridi
    </h4>
""", unsafe_allow_html=True)
st.write("Analyze any website link in real-time to detect potential security threats.")

# User Input
url_input = st.text_input("Paste URL here to analyze:", placeholder="https://example.com")

# Analyze Button
if st.button("Analyze Link", type="primary"):
    url = url_input.strip()

    # Check 1: Empty input
    if not url:
        st.warning("⚠️ Please enter a URL.")

    # Check 2: Invalid / random text
    elif " " in url or "." not in url:
        st.error("❌ Invalid URL. Please enter a proper website link (example: https://google.com)")

    # Check 3: Valid looking URL → run model
    else:
        feats = extract_features(url)
        df_feats = pd.DataFrame([feats])

        prediction = model.predict(df_feats)[0]
        proba = model.predict_proba(df_feats)[0]
        confidence = proba[1] * 100 if prediction == 1 else proba[0] * 100

        st.divider()
        st.subheader("Analysis Result")

        if prediction == 1:
            st.error(f"🚨 WARNING: High Risk Phishing URL Detected! (Confidence: {confidence:.1f}%)")
        else:
            st.success(f"✅ SAFE: This URL appears to be Legitimate. (Confidence: {confidence:.1f}%)")

        st.divider()
        st.subheader("🔍 Threat Breakdown & Factors")

        reasons = []

        if feats['has_https'] == 0:
            reasons.append("❌ Missing HTTPS protocol (Unencrypted connection)")
        else:
            reasons.append("✅ Secure HTTPS protocol active")

        if feats['having_ip'] == 1:
            reasons.append("❌ Direct IP Address used instead of domain name")
        else:
            reasons.append("✅ Domain name used (No IP address)")

        if feats['having_at_symbol'] == 1:
            reasons.append("❌ Contains '@' symbol (used for URL redirection tricks)")
        else:
            reasons.append("✅ No '@' symbol found")

        if feats['url_length'] > 50:
            reasons.append(f"❌ Suspicious URL length ({feats['url_length']} characters)")
        else:
            reasons.append(f"✅ Normal URL length ({feats['url_length']} characters)")

        if feats['subdomain_count'] > 1:
            reasons.append(f"❌ Multiple subdomains detected ({feats['subdomain_count']} subdomains)")
        else:
            reasons.append(f"✅ Normal subdomain structure ({feats['subdomain_count']} subdomains)")

        if feats['prefix_suffix'] == 1:
            reasons.append("❌ Domain contains hyphen '-' (Common in deceptive brand domains)")
        else:
            reasons.append("✅ No hyphen in domain name")

        for item in reasons:
            st.write(item)
