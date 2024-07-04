import openai

openai.api_key = "Need to enter API key here"


def generate_response(prompt):
  response = openai.Completion.create(
      model="gpt-3.5-turbo",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  return response.choices[0].text.strip()


while True:
  user_input = input("You: ")
  if user_input.lower() == "exit":
    break

  prompt = f"You: {user_input}\nAI:"
  response = generate_response(prompt)

  print(response)
