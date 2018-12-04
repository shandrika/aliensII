# Add Condition for The While Loop

#Identify variables
landed = int()
weeks = int()
wks = str("week")
are =str("are")
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
landed = int(input("How many aliens landed on Earth? "))
print()

if landed > 0:

    #Q2
    print("Oh, and tell us...")
    print()
    weeks = int(input ("How many weeks did they stay? "))
    print()
    if weeks > 0:
        print()
    else:
        # bad input 2
        print("please restart the program and input")
        print("whole number. Thank You")
# bad input 1
else:
    print("please restart the program and input")
    print("whole number. Thank You")


#Calculations
for i in range(weeks):
    print("There are ", str(landed * 2 ** (i+1)), "aliens at the end of", str(i+1),
          wks, ".")
    if i == 0:
        wks = "weeks"

        
        
    

