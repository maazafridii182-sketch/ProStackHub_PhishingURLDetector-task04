import streamlit as st
import joblib
import pandas as pd
from extractor import extract_features

# Load trained ML model
model = joblib.load('phishing_model.pkl')

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

st.title("🛡️ Cyber Security Phishing URL Detector")
st.write("Analyze any website link in real-time to detect potential security threats.")

# User Input Box
url_input = st.text_input("Paste URL here to analyze:", "http://paypal.com.login-verify.account-update.com/login")

if st.button("Analyze Link"):
    if not url_input.strip():
        st.warning("Please enter a valid URL.")
    else:
        # Extract features from input URL
        feats = extract_features(url_input)
        df_feats = pd.DataFrame([feats])
        
        # Make prediction using trained model
        prediction = model.predict(df_feats)[0]
        
        st.divider()
        st.subheader("Analysis Result")
        
        if prediction == 1:
            st.error("🚨 WARNING: High Risk Phishing URL Detected!")
        else:
            st.success("✅ SAFE: This URL appears to be Legitimate.")
        
        st.divider()
        st.subheader("🔍 Threat Breakdown & Factors")
        
        # Explainable AI Analysis
        reasons = []
        if feats['has_https'] == 0:
            reasons.append("❌ Missing HTTPS protocol (Unencrypted connection)")
        else:
            reasons.append("✅ Secure HTTPS protocol active")
            
        if feats['having_ip'] == 1:
            reasons.append("❌ Direct IP Address used instead of domain name")
            
        if feats['having_at_symbol'] == 1:
            reasons.append("❌ Contains '@' symbol used for URL redirection")
            
        if feats['url_length'] > 50:
            reasons.append(f"❌ Suspicious URL length ({feats['url_length']} characters)")
            
        if feats['subdomain_count'] > 1:
            reasons.append(f"❌ Multiple subdomains detected ({feats['subdomain_count']} subdomains)")
            
        if feats['prefix_suffix'] == 1:
            reasons.append("❌ Domain contains hyphen '-' (Common in deceptive brand domains)")

        for item in reasons:
            st.write(item)