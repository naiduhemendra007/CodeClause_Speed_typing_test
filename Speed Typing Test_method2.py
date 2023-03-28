###### Program for making a Speed Typing Test in Python in python wihout GUI (Method 2) ###
### PROGRAM MADE BY HEMENDRA NAIDU ###
from time import * # importing all the functions from time
import random as r #this will import random as alias r
def mistake(par_test,user_test): #defining mistake function for comparing the original text with entered text
    error=0
    for i in range(len(par_test)):
        try:
            if par_test[i]!=user_test[i]:
                error=error+1
        except:
            error=error+1
    return error   
def speed_time(intial_time,end_time,user_input):
    time_delay=end_time-intial_time
    time_roundoff=round(time_delay,2)
    speed=len(user_input)/time_roundoff #this line will show the speed of typing in w/sec
    return round(speed)
    

test=["The quick brown fox jumps over the lazy dog","This speed typing test has been created by Hemendra Naidu",
      "Now this speed will determine how fast you can type and how much mistake you are making"]
test1=r.choice(test)
print("     ***** typing speed *****")
print(test1)
print()
print()
time_1=time()
testinput=input(" Enter: ")
time_2=time()

print('Speed: ',speed_time(time_1,time_2,testinput)," w/sec") #will print speed of typing 
print("Error: ",mistake(test1,testinput)) #this line will print number of errors done by user 
