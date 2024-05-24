from datetime import datetime

conversation_database = [
    {"timestamp": datetime(2024, 5, 15, 10, 30), "message": "Hi", "sender": "Alice"},
    {"timestamp": datetime(2024, 5, 15, 10, 32), "message": "Hello!", "sender": "Bob"},
    {"timestamp": datetime(2024, 5, 16, 11, 20), "message": "How are you?", "sender": "Alice"},
    {"timestamp": datetime(2024, 5, 16, 11, 22), "message": "I'm fine, thank you!", "sender": "Bob"},
    {"timestamp": datetime(2024, 5, 17, 12, 15), "message": "Need assistance?", "sender": "Alice"},
    {"timestamp": datetime(2024, 5, 17, 12, 17), "message": "Sure, what do you need help with?", "sender": "Bob"}
]

context = "\n".join([f"{msg['sender']}: {msg['message']}" for msg in conversation_database])

prompt = f"""Given the following conversation in <{context}>:

Generate the next initialization phrase text that the user can say next in the ongoing chat. 

Instructions:
1. Provide only the next initialization phrase that the user might say, focusing on generating a single probable text.
3. The context provided within context is dynamic and will vary, so ensure the generated prompt is relevant to the given context everytime.
4. Only provide one phrase per request. The process will be repeated in a loop to generate a total of three phrases.
5. Provide the phrases that might help strike the conversation between users.
6. Add a flare of fun, comedy, work, life etc. in the generated phrase.
7. Please give me one initialization phrase per request only. Remember just one at a time.


Example output:
"next initialization phrase here"


Ensure the output adheres strictly to this format. Do not include any additional information or text outside of the JSON object.

Remember:
- Do not include the name of the user.
- Focus solely on the next phrase to generate.
- Maintain relevance to the provided conversation context.  """
