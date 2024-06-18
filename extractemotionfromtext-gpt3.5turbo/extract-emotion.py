import openai
openai.api_key = "[ENTER YOURS HERE]"

userIn = input("Enter a paragraph: \n")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": ("Extract an emotion from this text: \n"+userIn)},
    ]
  )

print(response['choices'][0]['message']['content'])
