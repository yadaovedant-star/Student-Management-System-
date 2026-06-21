import random
print("Made By vedant")

# Question bank stored as tuples (immutable)
# Format: (question, optA, optB, optC, optD, correct_option) #correct option at last 
def load_questions():
    return [
        ("Which data type is IMMUTABLE in Python?", "List", "Dictionary", "Tuple", "Set", "C"),  #correct answer is 'c'
        ("Which keyword is used to define a function?", "func", "def", "function", "lambda", "B"), #b
        ("Which operator is used for floor division?", "/", "//", "%", "**", "B"), #b
        ("Which method is used to add an item to a list?", "append()", "add()", "insert()", "push()", "A"), #a
        ("Which module is used for random numbers?", "math", "random", "numbers", "os", "B"), #b
        ("Which loop executes at least once?", "for", "while", "do-while", "None", "C"), #c
        ("Which symbol is used for comments?", "//", "#", "/* */", "--", "B"), #b
        ("Which function returns length of a list?", "count()", "len()", "size()", "length()", "B"), #b
        ("Which keyword is used for exception handling?", "try", "catch", "except", "finally", "A"), #a
        ("Which function converts string to integer?", "int()", "str()", "float()", "chr()", "A") #a
    ]

# Display question
def display_question(q, num):                # q=question num=number
    print(f"\nQ{num}: {q[0]}") #question on index 0
    print(f"A. {q[1]}    B. {q[2]}") #option selection for the answer if its A,B,C,D
    print(f"C. {q[3]}    D. {q[4]}") 

# Get and validate answer
def get_answer():
    ans = input("Your Answer (A/B/C/D): ").strip().upper() #takes your answer as input  
    while ans not in ["A", "B", "C", "D"]: #while loop to check that the input is invalid
        print("Invalid option! Please enter A, B, C, or D.") #executes when error 
        ans = input("Your Answer (A/B/C/D): ").strip().upper() #again asks input
    return ans  #returns the value and stores it into ans variable

# Calculate grade
def calculate_grade(percent):       #stores and prints according to condition 
    if percent >= 90:
        return "A+"                 #if grade is greater than 90 or equals to then print grade as A+
    elif percent >= 75:             
        return "A"                  #if grade is greater than 75 or equals to then print grade as A
    elif percent >= 60:
        return "B+"                 #if grade is greater than 60 or equals to then print grade as B+
    elif percent >= 50:
        return "B"                  #if grade is greater than 50 or equals to then print grade as B
    else:
        return "Fail"               #if grade is less than 50 print Fail

# Show wrong answers
def show_wrong_answers(wrong_answers):          #this block will show the wrong answers 
    if not wrong_answers:
        print("All answers correct!")           #If there are no wrong answers then it prints this 
    else:
        print("\nWrong Answers Review:")        #else this will print as this
        for q, your_ans in wrong_answers:
            print(f"Q: {q[0]} | Your Answer: {your_ans} | Correct: {q[5]}")      #it will print (question:youranswer | correct answer)

# Show final report
def show_report(name, roll, score, total, wrong_answers):             #this function shows you all the overall data 
    percent = (score / total) * 100            #percentage you got 
    grade = calculate_grade(percent)          #grades calculation
    result = "PASS" if percent >= 50 else "FAIL"        #if you got greater than or equals to 50 you will be pass or
    print("\n====== RESULT REPORT ======")              #otherwise fail if lower tham 50%
    print(f"Name    : {name}")                    #prints full report _____------______ Your Name
    print(f"Roll    : {roll}")                    # Roll Number
    print(f"Score   : {score} / {total}")         # Score
    print(f"Percent : {percent:.2f}%")            # Percentage achieved
    print(f"Grade   : {grade}")                   #grade you got weather its an A+
    print(f"Result  : {result}")                  # And final result
    show_wrong_answers(wrong_answers)             # Shows your Wrong answers

# Main quiz function
def evaluate_quiz():
    print("====== PYTHON QUIZ SYSTEM =====")             #main function starts
    name = input("Enter Student Name: ")                #Your name as student
    roll = input("Enter Roll Number: ")                 #roll number

    questions = load_questions()               #this loads quesions 
    random.shuffle(questions)  # Bonus feature: shuffle questions         #this shuffles them accordingly

    score = 0                  #score
    wrong_answers = []         #wrong answers empty list
  
    for i, q in enumerate(questions, start=1):         #questions start
        display_question(q, i)               #displays prints questions
        ans = get_answer()         #if answer correct
        if ans == q[5]:          
            print("Correct!")      #prints corret
            score += 1       #score gets added per question one
        else:
            print("Incorrect!")        #else prints incorrect 
            wrong_answers.append((q, ans))         #and gets added to wrong answers list

    show_report(name, roll, score, len(questions), wrong_answers)              #full report about your name rollno etc 

# Start Program
if __name__ == "__main__":            
    evaluate_quiz()
