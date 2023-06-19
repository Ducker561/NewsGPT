# 导入请求包
import requests

proxies = {"http":"127.0.0.1:7890", "https":"127.0.0.1:7890"}
APIKEY = '***'  # Your news API key

def get_top_news(q):

    url = "https://api.newscatcherapi.com/v2/search"

    querystring = {"q": q, "sort_by": "relevancy", "page": "1"}

    headers = {
        "x-api-key": APIKEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    page=response.json()

    article = page["articles"]

    results = []
    for ar in article:
        results.append(ar["title"])
        results.append(ar["summary"])
    return results

