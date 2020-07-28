import json
import requests
import pprint
import random
import html
import time
import matplotlib.pyplot as pyplot

data_valid=True
t=[]
result=[]
score_correct=0
score_incorrect=0

time_start=time.time()

while data_valid==True:
    valid = False
    r = requests.get("https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple")
    r.text
    question=json.loads(r.text)
    q=question['results'][0]['question']
    ans=question['results'][0]['correct_answer']
    w_ans=question['results'][0]['incorrect_answers']
    # w_ans.append(ans)
    # print (ans)
    w_ans.append(ans)
    random.shuffle(w_ans)
    value=w_ans.index(ans)
    # print (value)
    answer = value + 1
    print("Que.",html.unescape(q))
    print("Your option are: ")
    i=1
    for x in w_ans:
        print(i,".",html.unescape(x))
        i+=1
    user_ans=input("Enter your Answer: ")
    while valid==False:
        try:
            user_ans=int(user_ans)
            if (user_ans<0 and user_ans>4):
                print("Invalid Answer!!Please choose Number Between 1 to 4")
            else:
                valid=True
        except:
            ("Invalid Answer!!Please use Numbers")
    if (user_ans == answer):
        print("Correct Answer")
        score_correct+=1
    else:
        print("Incorrect Answer\nCorrect Answer is ",html.unescape(ans))
        score_incorrect+=1

    again=input("Do You Want to Play Again: \n1.YES (press Enter)\n2.NO (press q)\n")
    if again=='q':
        print("######################################")
        print("Your total score is: ")
        print("Correct Answers: ",score_correct)
        print("Incorrect Answers: ",score_incorrect)
        print("######################################")

        data_valid=False
    else:
        pass
time_end=time.time()
total_time=time_end - time_start
t.append(total_time)
result.append(score_correct)
print("Total Time taken by you to complete quiz is ",round(total_time,2),"sec")
print("Wait a second.....")
time.sleep(3)
x=result
y=t
pyplot.scatter(x,y)
pyplot.xlabel("score")
pyplot.ylabel("time")
pyplot.title("Total Time vs Score in Quiz")
pyplot.show()