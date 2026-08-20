import re
import urllib.parse
import tldextract

def extract_features(url):
    features = {}
    
    # 1. URL ki length count karna
    features['url_length'] = len(url)
    
    # 2. Check karna ke kya '@' symbol hai
    features['having_at_symbol'] = 1 if '@' in url else 0
    
    # 3. Check karna ke kya IP address directly use hua hai
    ip_pattern = r"(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])"
    features['having_ip'] = 1 if re.search(ip_pattern, url) else 0
    
    # 4. HTTPS Protocol check karna
    features['has_https'] = 1 if url.startswith('https://') else 0
    
    # 5. Subdomains count karna
    extracted = tldextract.extract(url)
    subdomain = extracted.subdomain
    features['subdomain_count'] = len(subdomain.split('.')) if subdomain else 0
    
    # 6. Check karna ke kya domain mein hyphen '-' hai
    features['prefix_suffix'] = 1 if '-' in extracted.domain else 0
    
    return features

# Quick Test
if __name__ == "__main__":
    sample_url = "http://paypal.com.login-verify.account-update.com/login"
    result = extract_features(sample_url)
    print("Extracted Features:")
    for k, v in result.items():
        print(f"  {k}: {v}")