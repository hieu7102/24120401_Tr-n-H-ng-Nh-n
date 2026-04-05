from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient

app = FastAPI()

client = InferenceClient()

class RequestData(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Text Generation API (Online Model)"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(data: RequestData):

    if not data.prompt or not data.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    if len(data.prompt) > 200:
        raise HTTPException(status_code=400, detail="Prompt too long")

    try:
        result = client.text_generation(
            data.prompt,
            model="gpt2",
            max_new_tokens=50
        )

        return {
            "success": True,
            "data": {
                "input": data.prompt,
                "output": result
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))