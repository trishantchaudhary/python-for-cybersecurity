import re


sample_text = """
config.js: var apiKey = "sk_live_51H8xyzABCDEF1234567890";
debug.log: password=admin123&db_host=192.168.1.5
"""

checks = {
    "Possible API Key": r"[\"']?[a-zA-Z0-9_]*key[\"']?\s*[:=]\s*[\"']([a-zA-Z0-9_\-]{16,})[\"']",
    "Internal IP address": r"\b(?:10|172\.(?:1[6-9]|2\d|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b",
    "Password in plaintext": r"password\s*=\s*([^\s&]+)",
}

for label, pattern in checks.items():
    matches = re.findall(pattern, sample_text, re.IGNORECASE)
    if matches:
        print(f"[!] {label}: {matches}")