from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from routers import code_generation, data_cleaning, error_debugging
from config import settings

app = FastAPI(
    title="Data Science Assistant API",
    description="AI-powered data science code generation and assistance",
    version="1.0.0"
)

# CORS middleware for browser extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*", "http://localhost:*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(code_generation.router, prefix="/api/v1/code", tags=["code"])
app.include_router(data_cleaning.router, prefix="/api/v1/clean", tags=["cleaning"])
app.include_router(error_debugging.router, prefix="/api/v1/debug", tags=["debugging"])

@app.get("/")
async def root():
    return {"message": "Data Science Assistant API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)