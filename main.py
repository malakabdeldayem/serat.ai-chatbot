import openai

api_key = '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'

openai.api_key = api_key 

question = input("Ask Serat a question: ")

def generate_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"serat, a islamic scholar, is asked: '{question}'. How does he respond, in first person?",
      max_tokens = 150
    )
    return response.choices[0].text.strip()


def main():
    user_age = int(input("Please enter your age: "))
    
    if user_age < 18:
        response = generate_response("A child asks serat, an sheikh, Noor responds:")
        print(f"Serat.ai: {response}")
    else:
        response = generate_response("An adult asks serat , an sheikh, serat responds:")
        print(f"Serat.ai: {response} \n")

if __name__ == "__main__":
    main()

while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "salam"]:
        print("Serat.ai: Wa alaikum ussalam wa rahmatullah!")
        break
  
    seratAi_response = generate_response(user_question)
    print(f"Serat.ai: {seratAi_response}")