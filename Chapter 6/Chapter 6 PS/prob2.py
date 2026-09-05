# write a program to find out that wether a student has passed or failed if it requires 
# a total of 40% to pass and atleast 30% in each subject to pass. Assume that the student 
#  has taken 3 subjects and the maximum marks in each subject is 100.

subj1 = int((input("Enter marks obtained in subject 1: ")))

subj2 = int((input("Enter marks obtained in subject 2: ")))

subj3 = int((input("Enter marks obtained in subject 3: ")))

total_marks = (subj1 + subj2 + subj3) / 3
print("Total marks obtained: ", total_marks)

if(total_marks>=40 and subj1>=30 and subj2>=30 and subj3>=30):
    print("Congratulations! You have passed the exam.")

else:
    print("Sorry! You have failed the exam.")




