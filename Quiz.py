##Python quiz game

questions = ("What is the full form of the AWS?",
             "What is AWS cloudformation?",
             "What is abbreviation of AWS S3 ",
             "What is VPC?",
             "What is AWS CloudFront?")
options = (("A. Amazon Web Services ","B. Amazon Web Service ","C. American Web Service","D. American Web services"),
           ("A. Cloudformation is configuration tool", "B. Cloudformation is migration tool","C. Related to DevOps", "D. Related to Vmware"),
           ("A. S3 => Simple storage services","B. S3 => Storage simple services","C. S3 => Storage simple Service","D. S3 => Simple storage management"),
           ("A. Virtual Private Cloud","B. Virtual Public cloud", "C. Virtual Private Configuration", "D. Virtual Public configuration"),
           ("A. CloudFront is frontier service","B. CloudFront is edge computing service","C. CloudFront is to enable internet","D. Amazon CloudFront is a content delivery network (CDN) that's part of Amazon Web Services (AWS)"))
answers = ("A","A","A","A","D")
guesses = []
score = 0
question_num=0

for question in questions:
    print("-------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("-------------------------------------")
print("             RESULTS         ")
print("-------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"{score}%")

if score == 100:
    print("you are exceptional")
elif 60 <= score <= 80 :
    print("You are passed!")
else:
    print("Please try again!!")
