import urllib.request
import json

# Prompt for URL
url = "https://py4e-data.dr-chuck.net/comments_1828349.json"

response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")

info = json.loads(data)
comments = info["comments"]

#total = sum(comment["count"] for comment in comments)
for comment in comments:
    print(comment)

#print("Sum of comment counts:", total)
