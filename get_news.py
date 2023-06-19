# 导入请求包
import requests

<<<<<<< HEAD
proxies = {"http":"127.0.0.1:7890", "https":"127.0.0.1:7890"}
APIKEY = 'YRVOtybkUNns06LzmYTb150OVr2WXuAn7ZtbcFr9Lb4'
=======
proxies={"http":"127.0.0.1:7890", "https":"127.0.0.1:7890"}
APIKEY="***"
>>>>>>> e25590165641979172de7cf245643198770fe36f

def get_top_news(q):

    url = "https://api.newscatcherapi.com/v2/search"

    querystring = {"q": q, "sort_by": "relevancy", "page": "1"}

    headers = {
<<<<<<< HEAD
        "x-api-key": APIKEY
=======
        "x-api-key": "***"
>>>>>>> e25590165641979172de7cf245643198770fe36f
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    page=response.json()

    article = page["articles"]

    results = []
    for ar in article:
        results.append(ar["title"])
        results.append(ar["summary"])
    return results

