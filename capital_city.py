# this game program displayes the country name the user guess  the capital city name.
from game import Game # importing the file that contain the Game class.
#creating question array.
question_games = [
                   "What is the capital city of Greece?:\n ",
                   "What is the capital city of Spain?:\n",
                   "What is the capital city of Russia?:\n"
                 ] 
#creating answer array
ans_questions = [
                  Game(question_games[0], "Athens"),
                  Game(question_games[1], "Madrid"),
                  Game(question_games[2], "Moscow"),
                ]

def run_game(ans_questions): # define the ans the answer array.
    score = 0  # score variable created to contain scores
    for question in ans_questions: # for loop to loop through answers array
        answer = input(question.quest) # answer declair to take user input.
        if answer.lower() == question.ans.lower():# if the true is met, it adds score take andy case
            score += 1 # add score
    print("You answerd " + str(score))

run_game(ans_questions)


 





