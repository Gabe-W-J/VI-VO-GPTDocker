import openai
openai.api_key = "[ENTER YOURS HERE]"

print("Emotions Available:\nHappiness, Confidence, Playfulness, Embarassment, Anger, Fear,\nSadness, Anxiousness, Stress, Annoyment, Boredom, Guilt or Curiousness\n")
userIn = input("Enter an Emotion: ")
emoticonPrompt = ("closeup portrait photograph of a futuristic, robotic woman expressing the emotion of "+userIn+", halo 3 cortana, sci-fi, futurama, 1999 low-polygon design, nintendo 64")

try:
  response = openai.Image.create(
    prompt=emoticonPrompt,
    n=1,
    size="256x256"
  )
  print(response['data'][0]['url'])
except openai.error.OpenAIError as e:
  print(e.http_status)
  print(e.error)
