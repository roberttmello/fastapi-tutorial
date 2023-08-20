from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello() -> str:
  return "Hi, i'm Robert!"

@app.get("/secret")
def secret() -> str:
  return "This is my sec***"
