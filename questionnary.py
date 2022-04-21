# Excercice questionnary
# ask a question , 4 answers , only one correct, 
# ask user the answer must be either a b c d
# depending the question you should print Well done right answer or Bad luck wrong answer
# 4 questions


def input_answer ():
    the_Answer =  input ("Your answer : ")
    while the_Answer not in ["a","b","c","d"]:
        print (f"the answer {the_Answer} is not a b c or d")
        the_Answer =  input ("Your answer : ")
    return the_Answer



def ask_Questions ( question :str ,
    answer_a :str , 
    answer_b :str , 
    answer_c :str , 
    answer_d : str , 
    good_answer :str):
    global score
    print (f"Question : {question} ?")
    print (f"   (a) {answer_a} ")
    print (f"   (b) {answer_b} ")
    print (f"   (c) {answer_c} ")
    print (f"   (d) {answer_d} ")
    print()
    answer = input_answer()
    if answer == good_answer:
        print ("Well done right answer.")
        score += 1
    else:
        print("Bad luck wrong answer")
    print ()

    
score = 0

ask_Questions ("quelle est la capitale de l'Italie", "Rome" , "Bruxelles", "Lyon", "Paris" , "a")
ask_Questions ("quelle est la capitale de la France", "Rome" , "Bruxelles", "Lyon", "Paris" , "d")
ask_Questions ("quelle est la capitale de la Belgique", "Rome" , "Bruxelles", "Lyon", "Paris" , "b")
ask_Questions ("quelle est la capitale de la Suisse", "Genêve" , "Berne", "Zurich", "Bâle" , "b")

print (f"Your score is  {score} points")