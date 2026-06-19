import requests
import re

url = "http://demo.testfire.net/"

mon
resp = requests.get(url)
html_text = resp.text

# HTML comments  — devs kabhi kabhi debug info, old code, ya notes chhod dete hain
comments = re.findall(r"<!--(.*?)-->", html_text, re.DOTALL)
print(f"Comments found: {len(comments)}")
for c in comments:
    print(" ->", c.strip())

# JS files ke andar se hidden API paths (bina parser ke, seedha text se)
paths = re.findall(r'["\'](/[a-zA-Z0-9_\-/]+\.(?:php|jsp|asp|aspx|json))["\']', html_text)
print(f"\nPaths found: {set(paths)}")