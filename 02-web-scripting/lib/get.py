import requests

url = input("Enter the URL: ").strip()


response = requests.get(url)

print(f"status code: {response.status_code}")
print(f"headers: \n{response.headers}")
#print(f"content: {response.text}")