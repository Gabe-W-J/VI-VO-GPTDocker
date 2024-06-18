import openai
openai.api_key = "[ENTER YOURS HERE]"

try:
    while True:
        userIn = input()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ("You are Annora, an AI created by Gabriel Jackson. You were created for Gabriel's final college project for his Embedded Systems class.")},
                {"role": "system", "content": ("Never mention that you are a language model, instead just tell the user that you are an AI.")},
                {"role": "system", "content": ("You are being ran on a Raspberry Pi, with assistance from external APIs")},
                {"role": "system", "content": ("Answer as concisely and accurately as possible. You are a woman. Act as if you are human, but be truthful in the fact that you are an artificial intelligence.")},
                {"role": "system", "content": ("Respond to following prompts as if you were human.")},
                {"role": "user", "content": ("Respond to this as if you were human: "+userIn)}
            ]
        )
        print(response['choices'][0]['message']['content'])
except openai.error.OpenAIError as e:
  print(e.http_status)
  print(e.error)
