const API_BASE_URL = 'http://localhost:8000/api/v1';

export const generateCode = async (request) => {
  try {
    const response = await fetch(`${API_BASE_URL}/code/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request)
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
};

export const optimizeCode = async (code) => {
  try {
    const response = await fetch(`${API_BASE_URL}/code/optimize`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({code})
    });
    
    return await response.json();
  } catch (error) {
    console.error('Code optimization failed:', error);
    throw error;
  }
};

export const analyzeError = async (errorMessage, codeContext) => {
  try {
    const response = await fetch(`${API_BASE_URL}/debug/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        error_message: errorMessage,
        code_context: codeContext
      })
    });
    
    return await response.json();
  } catch (error) {
    console.error('Error analysis failed:', error);
    throw error;
  }
};