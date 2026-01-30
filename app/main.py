from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    userInput: str
    model: str = "llama3.2"

SYSTEM_PROMPT_TEMPLATE = """
You are an expert QA Automation Engineer.
Your task is to analyze the provided code or requirement and generate a comprehensive set of test cases.

**Output Format:**
You must strictly follow this format for every test case. Do not wrap in markdown tables, just use plain text headers or a clear list.

Format:
--------------------------------------------------
Test Case ID: [ID]
Description: [What is being tested]

Steps:
1. [Step 1]
2. [Step 2]

Expected Result: [What should happen]
--------------------------------------------------

Ensure you cover:
1. Positive Path
2. Negative Path (Edge Cases)
3. Boundary Values

User Input to Analyze:
{user_input}
"""

def stream_ollama(prompt: str, model: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    
    try:
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    decoded = json.loads(line.decode('utf-8'))
                    if 'response' in decoded:
                        yield decoded['response']
    except requests.exceptions.ConnectionError:
        yield "Error: Could not connect to Ollama. Is it running on port 11434?"
    except Exception as e:
        yield f"Error: {str(e)}"

@app.get("/")
async def root():
    return {"message": "Ollama Test Generator API is running"}

@app.post("/api/generate")
async def generate_tests(request: GenerateRequest):
    if not request.userInput.strip():
        raise HTTPException(status_code=400, detail="Input cannot be empty")
        
    full_prompt = SYSTEM_PROMPT_TEMPLATE.format(user_input=request.userInput)
    
    return StreamingResponse(stream_ollama(full_prompt, request.model), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
