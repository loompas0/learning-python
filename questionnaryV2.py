# Excercice questionnary
# ask a question , 4 answers , only one correct, 
# ask user the answer must be either a b c d
# depending the question you should print Well done right answer or Bad luck wrong answer
# 4 questions


def input_answer (answer):
    the_Answer =  input ("Your answer is ")
    while the_Answer not in answer:
        print (f"the answer {the_Answer} is not {answer}")
        the_Answer =  input ("Your answer is : ")
    return the_Answer



def ask_Questions (pays):
    global score
    print (f"Question : Quelle la capitale de la {pays[0][0]} ?")
    print ("==================================")
    liste_answer = []
    for i in range(len(pays)-1 ):
        print (f"   {pays[i+1][1]}    {pays[i+1][0]}")
        liste_answer += pays[i+1][1]

    answer = input_answer(liste_answer)

    if answer == pays[0][1]:
        print ("Well done right answer.")
        score += 1
    else:
        print("Bad luck wrong answer")
    print ()

# Main 
# 
# Variable   
score = 0
france = (
    ("France", "d"),
    ("Rome", "a"),
    ("Bruxelles", "b"),
    ("Lyon", "c"),
    ("Paris", "d")
)
italie = (
    ("Italie", "1"),
    ("Rome", "1"),
    ("Bruxelles", "2"),
    ("Lyon", "3"),
    ("Paris", "4")
)
belgique = (
    ("Belgique", "B"),
    ("Rome", "A"),
    ("Bruxelles", "B"),
    ("Lyon", "C"),
    ("Paris", "D")
)
suisse = (
    ("Suisse", "b"),
    ("Genêve", "a"),
    ("Berne", "b"),
    ("Zurich", "c"),
    ("Bâle", "d")
)
# call functions
ask_Questions (france)
ask_Questions (italie)
ask_Questions (belgique)
ask_Questions (suisse)
print (f"Your score is  {score} points")