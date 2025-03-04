from openai import OpenAI
import ollama
client = OpenAI(api_key="sk-fade8f7c781e42aab15ec3c019e87a50", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)

blog_title=ollama.chat(model='llama3',messages=[
        {
            'role':'user',
            'content':"I will write an article with the keyword 'peach market' and, while strictly following the blog logic, please write an article of 1500 to 1800 characters including your experience on the meaning, importance, pros and cons, real-life cases (on the topic of difficulty), and implications of the term. In addition, an essential part is that there should be no excessive repetition of words in the article. You should write an article that is original and has accurate information! Just like a person writing! Never copy other people's articles or duplicate articles. Please include your thoughts! I will also ask you to optimize for SEO (search engine optimization). However, please use different terms so that words are not repeated too often. The core of the blog logic is that the same words should not be repeated! Please write naturally as if written by a human! It should never be read as if it were written by a machine!",

        },
    
    ])
blog_title['message']['content']