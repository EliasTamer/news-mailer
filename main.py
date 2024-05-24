import requests
from send_email import send_email


topic = input("Select a topic that you would like to receive daily news for:")

api_key="KEY HERE"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-04-24&" \
    f"sortBy=publishedAt&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + article["description"]  + "\n" \
        + article["url"] + 2 * "\n"
    
    
send_email(subject="Today's News" , body=body)