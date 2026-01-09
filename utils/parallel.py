# from concurrent.futures import ThreadPoolExecutor #concurrent.futures is a package used for parallel execution of tasks, ThreadPoolExecutor is a class used to manage a pool of threads which can execute calls asynchronously
# from models.chatgpt_model import chatgpt_response
# from models.gemini_model import gemini_response
# from models.llama_model import llama_response

# def run_parallel(prompt: str) -> dict:  #dict is a return type and str is used for readability
#     results = {}

#     with ThreadPoolExecutor(max_workers=3) as executor:  #with keyword is used to closing threads after use. max_workers is used to define number of threads
#         futures = {
#             "ChatGPT": executor.submit(chatgpt_response, prompt), #executor.submit(). is used to schedule the callable to be executed and returns a Future object representing the execution of the callable
#             "Gemini": executor.submit(gemini_response, prompt),
#             "LLaMA": executor.submit(llama_response, prompt)
#         }
#         for model, future in futures.items(): #items() is used to get keys+values pairs from dictionary
#             try:
#                 results[model] = future.result() #.result() is used to get the return value from the thread
#             except Exception as e:
#                 results[model] = f"Error: {str(e)}" #str() is used to convert exception to string
#     return results
from concurrent.futures import ThreadPoolExecutor
from models.chatgpt_model import chatgpt_response
from models.gemini_model import gemini_response
from models.llama_model import llama_response
from utils.metrics import log_metrics
import time

MODEL_FUNCTIONS = {
    "chatgpt": chatgpt_response,
    "gemini": gemini_response,
    "llama": llama_response
}
def run_parallel(prompt, models):
    results = {}

    def call_model(model_name):
        key = model_name.lower()  
        start_time = time.time()
        if key in MODEL_FUNCTIONS:
            try:
                response = MODEL_FUNCTIONS[key](prompt)
            except Exception as e:
                response = f"Error: {e}"
        else:
            response = f"Model {model_name} not supported."

        elapsed = time.time() - start_time
        log_metrics(model_name, elapsed, len(response))
        return response

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(models)) as executor:
        futures = {model: executor.submit(call_model, model) for model in models}

        for model, future in futures.items():
            try:
                results[model] = future.result()
            except Exception as e:
                results[model] = f"Unexpected error: {e}"

    return results