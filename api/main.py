from routes import companies
from fastapi import FastAPI

app = FastAPI()
app.include_router(companies.companies)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SKRI Company Analyzer Dashboard, inspired by the one and only Martin Shkrelli"}

