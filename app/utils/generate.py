from llama_cpp import Llama

llm = Llama(model_path="./utils/model/mistral.gguf")

def generate_llama_response(input_text, max_tokens=50, stop=["Q:", "\n"], echo=True):
    """
    Generate a response from the Llama model based on the input text.

    Parameters:
        llm (Llama): The Llama model.
        input_text (str): The input text.
        max_tokens (int): Maximum number of tokens for the response.
        stop (list): List of strings at which to stop generation.
        echo (bool): Whether to echo the input text in the response.

    Returns:
        str: The generated response.
    """
    output = llm(
        input_text,
        max_tokens=max_tokens,
        stop=stop,
        echo=echo,
    )
    
    # print(output)
    return output




