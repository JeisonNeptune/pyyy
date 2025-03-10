import requests
import json

def get_news(api_key, country='us'):
    url = f'https://newsapi.org/v2/top-headlines?category=sports&country={country}&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])

        if not articles:
            print("No sports news found.")
            return []
        
        news_list = []

        for article in articles[:10]:
            news_list.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "description": article.get("description"),
                "url": article.get("url")
            })
        return news_list
    else:
        print("Error fetching news:", response.status_code)
        return []
API_KEY = "e2ae976f4ed64f709937493e060e7cab"
sports_news = get_news(API_KEY)

if sports_news:
    print("\nTop Sports News:\n")
    for idx, news in enumerate(sports_news, 1):
        print(f"{idx}. {news['title']} ({news['source']})")
        print(f"    {news['description']}")
        print(f"     Read more: {news['url']}\n")

