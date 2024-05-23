import requests
from send_email import send_email

api_key="YOUR_API_KEY_HERE"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-04-23&" \
"sortBy=publishedAt&apiKey=${api_key}"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"
    
    
send_email(subject="News Mailer" , body=body)