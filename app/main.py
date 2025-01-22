from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World 1"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
