from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


#develop branch
# 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