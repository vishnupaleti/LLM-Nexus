from concurrent.futures import ThreadPoolExecutor #concurrent.futures is a package used for parallel execution of tasks, ThreadPoolExecutor is a class used to manage a pool of threads which can execute calls asynchronously
from models.chatgpt_model import chatgpt_response
from models.gemini_model import gemini_response
from models.llama_model import llama_response

def run_parallel(prompt: str) -> dict:  #dict is a return type and str is used for readability
    results = {}

    with ThreadPoolExecutor(max_workers=3) as executor:  #with keyword is used to closing threads after use. max_workers is used to define number of threads
        futures = {
            "ChatGPT": executor.submit(chatgpt_response, prompt), #executor.submit(). is used to schedule the callable to be executed and returns a Future object representing the execution of the callable
            "Gemini": executor.submit(gemini_response, prompt),
            "LLaMA": executor.submit(llama_response, prompt)
        }
        for model, future in futures.items(): #items() is used to get keys+values pairs from dictionary
            try:
                results[model] = future.result() #.result() is used to get the return value from the thread
            except Exception as e:
                results[model] = f"Error: {str(e)}" #str() is used to convert exception to string
    return results