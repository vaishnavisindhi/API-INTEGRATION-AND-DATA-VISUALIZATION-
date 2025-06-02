import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

API_KEY = "17752da8ebf74d71a1d8f15608ebd294"

# 🔎 Fetching top headlines (sports + entertainment)
params = {
    'category': 'sports',  # or 'entertainment', or remove to get general headlines
    'pageSize': 20,
    'apiKey': API_KEY
}

response = requests.get("https://newsapi.org/v2/top-headlines", params=params)
data = response.json()

articles = data.get("articles", [])
headlines = " ".join(article['title'] for article in articles if article['title'])

# ❗Checking if headlines are available
if not headlines:
    print("No headlines found. Try adjusting the category or API key.")
else:
    # ☁️ Generating the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(headlines)

    # 🎨 Displaying the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Most Common Words in News Headlines", fontsize=16)
    plt.show()
