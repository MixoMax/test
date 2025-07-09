from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import sys
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number, using default port 8000.")
            port = 8000
    
    uvicorn.run(app, host="0.0.0.0", port=port)