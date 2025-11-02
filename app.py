from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GIC Python Assessment API is running!"}

@app.get("/health")
def health():
    """Health check endpoint to verify the API is up."""
    return {"status": "ok"}
