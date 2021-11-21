import random
score = 0
for x in range(10):
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    print(f"What is {number1} + {number2}?")
    userAnswer = int(input("What is your answer?: "))
    answer = number1 + number2
    if userAnswer == answer:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
print(f"Your score is: {score}/10")