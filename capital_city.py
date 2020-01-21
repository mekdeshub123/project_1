# this game program displayes the country name the user guess  the capital city name.

question = 0 #creating global variable
score = 0

#Q1
question1 = input("What is the capital city of Greece? \nYour Answer: ") #user answer input
if question1 == "Athens": #if condition is meet to true count the score.
    score += 1 # for correct question add 1 score
    print("Correct ! ")
    print("Scored: ", score) # print the acumilated score.
    print("\n") #for readablity, add space on the buttom line.

else:
    print("The answer is Athens.")
    print("You scored: ", score)
    print("\n")
#Q2
question2 = input("What is the capital city of Spain? \nYour Answer: ")
if question2 == "Madrid": 
    score += 1 
    print("Correct ! ")
    print("Scored: ", score) 
    print("\n") 

else:
    print("The correct answer is Madrid.")
    print("You scored: ", score)
    print("\n")
#Q3
question3 = input("What is the capital city of Russia? \nYour Answer: ")
if question3 == "Moscow": 
    score += 1 
    print("Correct ! ")
    print("Scored: ", score) 
    print("\n") 

else:
    print("The correct answer is Moscow.")
    print("You scored: ", score)
    print("\n")
#Q4
question4 = input("What is the capital city of Egypt? \nYour Answer: ")
if question4 == "Cairo":
    score += 1 
    print("Correct ! ")
    print("Scored: ", score) 
    print("\n") 

else:
    print("The answer is Cairo.")
    print("You scored: ", score)
    print("\n")

#Qestion5
question5 = input("what is the capital of Italy \nYour Answer: ")
if question5 == "Rome":
    score += 1
    print("Correct! ")
    print("You scored: ", score)
    print("\n")
else:
    print("The correct answer is Rome. ")
    print("You scored: ", score)
    print("\n")
if score >= 0:
    print("Your total score is:", score)# it displayed the total score of the game if the total score is grater than 0.
    print("\n")
# else:
#     print("Ttry again")
