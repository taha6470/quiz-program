#add a dictionary that stores questions and awnsers
#then we make a variable that tracks the scroe of the player
#then we loop through the dictionary 
#then display the questions to the user and tell them to awnser
#then we show the final result of the user
quiz = {
    "question1":
    {
        "question":"What is the capital of france? : "
        ,"awnser":"Paris"
    },
    "question2":
    {
        "question":"What is the capital of germany? : "
        ,"awnser":"Berlin"
    },
    "question3":
    {
        "question":"What is the capital of Italy? : "
        ,"awnser":"Rome"
    }
    #you can add as many questions and awnsers as you want
}
score=0
for key,value in quiz.items():
    print(value["question"])
    awnser=input("input awnser :")
    if awnser.lower()==value["awnser"].lower():
        print("correct")
        score=score+1
    else:
        print("wrong")

print("your final score is {} out of 3!".format(score))