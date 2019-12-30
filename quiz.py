print("Welcome to the quiz game")
ans=input("Are you ready to play \n")
score =0
total_q=4
if ans == "no":
    print("ok bye")
if ans == "yes":
    ans= input ("1)what is the name of our country? \n")
    if ans.lower() == "pakistan":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans= input ("2)what is the atomic number of carbon? \n")
    if ans == "6":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans= input ("3)5+8+6? \n")
    if ans == "19":
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans= input ("4)which is the best programming language? \n")
    if ans.lower() == "python":
        score += 1
        print("correct")
    else:
        print("incorrect")
    print("Thankyou for playing", "your", score , "answers are correct")
    percentage= int((score/total_q)*100)
    print("congrates you got ", percentage ,"percent marks in quiz")
