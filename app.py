from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GIC Python Assessment API is running!"}
