from models.chatgpt_model import chatgpt_response
from models.gemini_model import gemini_response
from models.llama_model import llama_response

MODEL_MAP = {
    "ChatGPT": chatgpt_response,
    "Gemini": gemini_response,  
    "llaMA": llama_response
}

FALLBACK_ORDER = {
    "ChatGPT": ["Gemini", "llaMA"],
    "Gemini": ["llaMA"],
    "llaMA": []

}
def execute_with_fallback(model_name: str, prompt: str):
    """
    Try primary model, if it fails, automatically fallback to the next model in the order.
  
    """
    try:
        return MODEL_MAP[model_name](prompt)
    except Exception as primary_error:
        for fallback_model in FALLBACK_ORDER[model_name]:
            try:
                return MODEL_MAP[fallback_model](prompt)
            except Exception:
                continue
        return f"All models failed for {model_name}"
         
