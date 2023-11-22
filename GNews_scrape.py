import requests
from bs4 import BeautifulSoup

import uvicorn
from fastapi import FastAPI

def scrape(inp):
    l=[]
    n=[]
    nl={}

    URL = "https://news.google.com/search?q="+inp
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find_all(class_="DY5T1d RZIKme")
    time=soup.find_all(class_="WW6dff uQIVzc Sksgp slhocf")

    for abc in range(0,11):
        c=str(name[abc]).split('" target="_blank">')
        r1=c[1].replace("</a>","")
        datetime=str(time[abc]).split('<time class="WW6dff uQIVzc Sksgp slhocf" datetime="')
        datetime2=datetime[1].split('">')
        r2=c[0].replace('<a class="DY5T1d RZIKme" href="',"")
        n.append(r1)
        l.append(r2)
        id_=r2.split('./articles/')
        link = ("https://news.google.com/"+r2)
        id2=id_[1].replace("?hl=en-IN&amp;gl=IN&amp;ceid=IN%3Aen","")
        nl[id2]={"title":r1,"updated_on":{"time":datetime2[0].split("T")[1].replace('Z',''),"date":datetime2[0].split("T")[0]},"link":link}
        
    return nl

app = FastAPI()

@app.get("/news/{inpu}")
async def root(inpu:str):
    return scrape(inpu)

@app.get("/news/")
async def root():
    return {"Message":"Pleaase specify a search query."}
@app.get("/")
async def root():
    return {"Message":"Hello From SSR!"},{"Correct Way":r"http://127.0.0.1:8000/news/{query}"}

if __name__ == "__main__":
    uvicorn.run("GNews_scrape:app", host="0.0.0.0", port=8000, reload=True)