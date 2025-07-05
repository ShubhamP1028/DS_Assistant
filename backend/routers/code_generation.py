from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.llm import AnthropicLLM
from services.cleaner import DataCleaner
from models.schemas import CodeGenerationRequest, CodeGenerationResponse

router = APIRouter()
llm = AnthropicLLM()
cleaner = DataCleaner()

class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None
    data_info: Optional[dict] = None

@router.post("/generate", response_model=CodeGenerationResponse)
async def generate_code(request: QueryRequest):
    """Generate Python code from natural language query"""
    try:
        # Enhance query with context
        enhanced_query = llm.enhance_query(request.query, request.context)
        
        # Generate code using Anthropic API
        code_response = await llm.generate_code(enhanced_query)
        
        # Post-process and validate code
        validated_code = llm.validate_code(code_response.code)
        
        return CodeGenerationResponse(
            code=validated_code,
            explanation=code_response.explanation,
            libraries=code_response.libraries,
            confidence=code_response.confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/optimize")
async def optimize_code(code: str):
    """Optimize existing code for better performance"""
    try:
        optimized = await llm.optimize_code(code)
        return {
            "original_code": code,
            "optimized_code": optimized.code,
            "improvements": optimized.improvements,
            "performance_gain": optimized.estimated_speedup
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
