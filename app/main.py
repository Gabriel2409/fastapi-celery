from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Hello world"""
    return {"message": "Hello World"}
