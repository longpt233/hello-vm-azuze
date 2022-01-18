from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/test")
async def root():
    return {"message": "Hello World"}

uvicorn.run(app)