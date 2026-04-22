from ollama import chat
from ollama import ChatResponse



def call_llama(model, prompt, stream=False):
    if stream:
        stream = chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
        )
        full_text = "" 
        for chunk in stream:
            content = chunk.message.content or ""
            print(content, end='', flush=True)
            full_text += content
        return full_text
    
    else:
        response: ChatResponse = chat(model=model, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
            ])
        return response.message.content
