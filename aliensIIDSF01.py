#Add "While Loop" To Question Two

#Identify variables
landed = int()
weeks = int()
wks = str("week")
are =str("are")
# The Condition 
aliens = False
time = False
#We don't know what happened so aliens = False

#Intro
print ("Look up in the sky its a bird, its a plane, no wait its ... aliens?")
print()
print ("Space aliens have just landed on earth! Suprisingly, you discovered that space aliens")
print("reproduce asexually. A baby alien grows up in a week and has it's own baby.")
print("Since you discovered the aliens, tell us...")
print()

#Q1
while aliens == False:
    try:
       landed = int(input("How many aliens landed on Earth? "))
       
       if landed > 0:
           print("Oh, and tell us...")
           aliens = True
           #aliens is TRUE becayse the user used a positive integer
           #This allows the user to break out the loop and go to Q2
       else:
           print("Please input a positive integer")
           #aliens is NOT true because the user did not input a good number
           #User will stay in loop, until a good number is entered
            
    except ValueError:
           print("Seriously? Input a positive WHOLE Number")
           #the user did not put a number and/or a whole number, so aliens is NOT true
           #User will stay in loop, until a good number is entered

#Q2
while time == False:
    try:
        weeks = int(input ("How many weeks did they stay? "))

        if weeks > 0:
            print("Let me calculate real quick")
            time = True
            #time is TRUE becayse the user used a positive integer
            #This allows the user to break out the loop and allows them to see the calculations
            
        else:
            print("Please input a positive integer")
            #time is NOT true because the user did not input a good number
            #User will stay in loop, until a good number is entered

    except ValueError:
         print("Seriously? Input a positive WHOLE Number")
         #the user did not put a number and/or a whole number, so time is NOT true
         #User will stay in loop, until a good number is entered

    
        
#Calculations
for i in range(weeks):
    print("There are ", str(landed * 2 ** (i+1)), "aliens at the end of", str(i+1),
          wks, ".")
    if i == 0:
        wks = "weeks"
