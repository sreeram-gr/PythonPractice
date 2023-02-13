import requests

response = requests.get("https://api.github.com/users/SreeramGovindanRajendran/repos")
repos = response.json()

for repo in repos:
    print(f"Name : {repo['name']}\nURL : {repo['url']}")