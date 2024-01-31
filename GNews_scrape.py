import requests
from bs4 import BeautifulSoup

import uvicorn
from fastapi import FastAPI

def scrape(query):
    l=[]
    store={}

    URL = "https://news.google.com/search?q="+str(query)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find_all(class_="JtKRv")
    image=soup.find_all(class_="K0q4G")
    time=soup.find_all(class_="hvbAAd")
    link=soup.find_all(class_="WwrzSb")

    #print("Name:",name)
    #print(image)
    
    #print("Time:",time)
    #print(link)

    for i in range(0,len(name)):
        try:
            title=str(name[i]).split('target="_blank">')[1].split("</a>")[0]
            #print(title)
            imagelink=str(image[i]).split('src="')[1].split('" src')[0]
            upload=time[i].text
            articleLink=str(link[i]).split('href="')[1].split('" jslog')[0]
            store[i]={"title":title,"image":imagelink,"uploadTime":upload,"articlelink":articleLink}
        except:
            print("That's Enough!")
            break
    #print(store)
    return store

app = FastAPI()

@app.get("/news/{inpu}")
async def root(inpu:str):
    return scrape(inpu)

@app.get("/news/")
async def root():
    return {"Message":"Pleaase specify a search query."}
@app.get("/")
async def root():
    return {"Message":"Hello From SSR!"},{"Correct Way":r"https://gnewssapi.vercel.app/news/{query}"}

if __name__ == "__main__":
    uvicorn.run("GNews_scrape:app", host="0.0.0.0", port=4000, reload=True)
