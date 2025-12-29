from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello FastAPI!"}

@app.get("/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}!"}
uvicorn.run(app)

