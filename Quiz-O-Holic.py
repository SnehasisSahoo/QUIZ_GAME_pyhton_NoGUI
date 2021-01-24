import requests
import json
import pprint
import random
import html
import time

print("||QUIZ-O-HOLIC||\n")
score_correct = 0
score_incorrect = 0
qs_no = 1

url = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple"
endGame = ""

while endGame != "x":
    try:
        r = requests.get(url)
    except:
        input('Can not connect to the Internet, make sure you have active Internet Connection.\nPress ENTER to try again.\n')
        continue
    
    if (r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieving the question.\nPress ENTER to try again or type 'x' to quit  the game.\n")
    else:
        valid_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        category = data['results'][0]['category']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(f"{str(qs_no)}. {html.unescape(question)} (categorey: {html.unescape(category)})\n")
        qs_no += 1

        print("Options:")
        for answer in answers:
            print(str(answer_number) + ". " + html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\nType the option number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid Answer, enter numbers between 1 to 4")
                else:
                    valid_answer = True
            except:
                print("Invalid Answer, enter only numbers between 1 to 4")
            
        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulations! You are absolutely CORRECT! The answer is: " + html.unescape(correct_answer))
            score_correct += 1
        else:
            print("\nSorry, " + html.unescape(user_answer) + " is INCORRECT. The correct answer is: " + html.unescape(correct_answer))
            score_incorrect += 1

        endGame = input("\nPress ENTER to play again or type 'x' to quit the game.\n").lower()

print("\n###########################################")
print("SCORE: You answered " + str(score_correct) + ' CORRECTLY out of ' + str(score_correct+score_incorrect) + '.')
print("###########################################")

print("\nTHANKS FOR PLAYING!GOOD BYE!\n")
print('closing in...')
print('5..')
time.sleep(1)
print('4..')
time.sleep(1)
print('3..')
time.sleep(1)
print('2..')
time.sleep(1)
print('1..')
time.sleep(1)


        
