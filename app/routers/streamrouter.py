from fastapi import Query, APIRouter
from utils.generate import generate_llama_response
from utils.supress import suppress_stdout_stderr
import time
from routers.content import prompt
router = APIRouter()

init_pharase = {}
def response(input_text, postfix = "A: "):
    with suppress_stdout_stderr():
        response = generate_llama_response(input_text + postfix)
        response_string = response["choices"][0]["text"]
        
        answer = response_string.split("A:")[1].strip()
        input_text += answer

        return (answer, input_text)

def stream_chars(text):
  """Yields each character in the given text string."""
  for char in text:
    yield char

def display_sentence(text):
  """Prints the entire sentence after streaming each character."""
  for char in stream_chars(text):
    print(char, end="")
    time.sleep(0.5)
  print() 

@router.get("/streamop")
async def get_tasks(message: str = Query(...)):
    global prompt
    for i in range(3):
        ans , ip = response(prompt)
        init_pharase[i] = ans
        print(ans)
    
    return init_pharase

    


