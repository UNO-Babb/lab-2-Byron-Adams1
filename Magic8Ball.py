#Magic8Ball.py
#Name: Byron Adams
#Date: 1/29/2025
#Assignment: Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("-Magic 8 Ball-")
answers = [
  "As I see it, yes",
  "Ask again later",
  "Better not tell you now",
  "Cannot predict now",
  "Concentrate and ask again.",
  "Don’t count on it",
  "It is certain",
  "It is decidedly so",
  "Most likely",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Outlook good",
  "Reply hazy, try again",
  "Signs point to yes",
  "Very doubtful",
  "Without a doubt",
  "Yes",
  "Definitely",
  "You may rely on it."
  ]

  #Prompt the user for their question.

question = input("Please ask me a general or very specific yes or no question.")
  #Answer question randomly with one of the options from your earlier list.

response = random.choice(answers)
print (response)

if __name__ == '__main__':
  main()
