# TASK 3 Kaun Banega corepati

q1 = ("What is the capital of japan","delhi","tokyo","washinton dc","beijing")
q2 = ("What is the capital of india","delhi","tokyo","washinton dc","beijing")
q3 = ("What is the capital of usa","delhi","tokyo","washinton dc","beijing")
q4 = ("What is the capital of china","delhi","tokyo","washinton dc","beijing")

# Question 1
print("Question",q1[0])
print("Option 1 :",q1[1])
print("Option 2 :",q1[2])
print("Option 3 :",q1[3])
print("Option 4 :",q1[4])

# Take input from user

print("Answer\n")
ans1 = int(input())

# Check the answer

if(ans1 == q1.index("tokyo")):
    print("Correct Answer")
    print("Type 'yes' to go to the  question 2 ")
    yes1 = input()
    if (yes1 == "yes"):

        # Question 2 

        print("Question",q2[0])
        print("Option 1 :",q2[1])
        print("Option 2 :",q2[2])
        print("Option 3 :",q2[3])
        print("Option 4 :",q2[4])

        # take input of the answer

        print("Answer\n")
        ans2 = int(input())

        # Checking the ans 
        if(ans2 == q2.index("delhi")):
         print("Correct Answer")

        #  if ans is correct proceed with next question

         print("Type 'yes' to go to the  question 3 ")
         yes3 = input()
         if (yes3 == "yes"):
             print("Question",q3[0])
             print("Option 1 :",q3[1])
             print("Option 2 :",q3[2])
             print("Option 3 :",q3[3])
             print("Option 4 :",q3[4])

             # take input

             print("Answer\n")
             ans3 = int (input())

             if(ans3 == q3.index("washinton dc")):
                 print("Correct Answer")
                 print("Type 'yes' to go to the question 4 ")
                 yes4 = input()
                 if (yes4 == "yes"):

                 #Question 4    
            
                  print("Question",q4[0])
                  print("Option 1 :",q4[1])
                  print("Option 2 :",q4[2])
                  print("Option 3 :",q4[3])
                  print("Option 4 :",q4[4])

                 # getting ans
                 print("Answer\n")
                 ans4 = int(input())

                 if(ans4 == q4.index("beijing")):
                     print("Congrats on winning the game\nYou win 1 rupees")

                 else:
                    print("Match Over")
             else:
                print("Match Over")    
        else:
            print("Match Over")    
    else:
        print("Match Over")       

    
        

else:
    print("Match Over")

