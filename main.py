from fastapi import FastAPI
from crawl4ai import WebCrawler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Web Scraper SaaS is Live!"}

@app.get("/scrape")
async def scrape(url: str):
    async with WebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return {"markdown": result.markdown}
