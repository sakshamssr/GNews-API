import requests
import time
import feedparser
from fastapi.responses import JSONResponse

def scrape(inp):
    try:
        store=[]

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/153.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }

        url = "https://news.google.com/rss/search?q="+inp

        response = requests.get(url, timeout=20, headers=headers)

        print(response.status_code)

        feed = feedparser.parse(response.text)
        if(feed == {}):
            return JSONResponse(
                status_code=500,
                content={"success":"false","message":"Internal Server Error"}
            )
        # return feed["entries"]

        for i in feed["entries"]:
            temp = {}
            try:
                temp[i["id"]] = {
                "title": i["title"],
                "updated_on" : {
                    "time" : time.strftime("%H:%M:%S", i["published_parsed"]),
                    "date" : time.strftime("%Y:%m:%d", i["published_parsed"])
                },
                "link" : i["link"],
                "source":{
                    "href":i["source"]["href"],
                    "title":i["source"]["title"]
                }
                }
                store.append(
                    temp
                )
            except:
                pass 
        
        return JSONResponse(
            status_code=200,
            content=store
        )
    except:
        return JSONResponse(
            status_code=500,
            content={"success":"false","message":"Internal Server Error"}
        )

