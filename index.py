from fastapi import FastAPI
from fastapi.responses import JSONResponse
from.GNews_scrape import scrape

app = FastAPI()

@app.get("/news/{inpu}")
async def root(inpu:str):
    return scrape(inpu)

@app.get("/news/")
async def root():
    return JSONResponse(
        status_code=400,
        content={"message":"Pleaase specify a search query."}
        )
@app.get("/")
async def root():
    return JSONResponse(
        status_code=200, 
        content={
            "status":"ok",
            "message":"Hello From SSR!",
            "correct_way":r"https://gnewssapi.vercel.app/news/{query}"
            }
        )