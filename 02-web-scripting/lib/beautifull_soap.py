import requests
from bs4 import BeautifulSoup 


url = "http://testaspnet.vulnweb.com/login.aspx"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")



# find all forms
forms = soup.find_all("form")

print(f"total forms : {len(forms)}")


for form in forms:
    print("\n form action:", form.get("action"))
    print("form method:", form.get("method","GET"))


    inputs = form.find_all("input")
    for inp in inputs:
        name = inp.get("name")
        type = inp.get("type", "text")
        value = inp.get("value", "")
        print(f" input name : {name}  | type : {type} | value : {value}")
