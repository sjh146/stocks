import ollama 
def llama():
    response=ollama.chat(model='llama3',messages=[
        {
            'role':'user',
            'content':'You are a helpful assistant',

        },
    
    ])
    print(response['message']['content'])