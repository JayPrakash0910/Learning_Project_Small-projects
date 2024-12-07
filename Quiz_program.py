# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary suing the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or copyright()
# show the final result when quiz id completed

quiz = {
    "question1": {
        "question": "what is capital of bihar?",
        "answer": "patna"
    },
    "question2": {
        "question": "what is capital of madhya pradesh?",
        "answer": "bhopal"
    },
    "question3": {
        "question": "what is capital of utter pradesh?",
        "answer": "lucknow"
    },
    "question4": {
        "question": "what is capital of karnataka?",
        "answer": "bengaluru"
    },
    "question5": {
        "question": "what is capital of Maharashtra?",
        "answer": "mumbai"
    },

    "question6": {
        "question": "what is capital of tamil nadu?",
        "answer": "chennai"
    },

    "question7": {
        "question": "what is capital of west bangal?",
        "answer": "kolkata"
    }

}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("answer? ")

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score+1
        print("your score is: " + str(score))
        print("")
        print("")
    else:
        print("WRONG !")
        print("the answer is : " + value['answer'])
        print("your score is: " + str(score))
        print("")
        print("")

        print("you got " + str(score) + "out of 7 question correctly")
        print("your percentage is = " + str(int(score/7*100)) + "%")
