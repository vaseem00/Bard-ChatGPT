from bardapi import Bard
import openai
openai.api_key = "Your API Key"
token = 'Your API Key'
bard = Bard(token=token)
query = input("Your query: ")
bard_result = bard.get_answer(query)['content']
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                   {"role": "system", "content": "Act as an AI chatbot with access to the internet."},
                   {"role": "user", "content": "Provide a well structured and easily readable text by analyzing this: The first content below is the user's query and the second content below is the result obtained by accessing the internet with the help of google's search alogoritm. Provide the well structured and good mannered answer by processing the user's query and the result from Google search algorithm. /n"+query+' /n '+ bard_result}
       
                 ]
)
final_response = completion["choices"][0]["message"]["content"]
print(final_response)
