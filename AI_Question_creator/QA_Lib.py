import pyinputplus as pyip
import shelve

shelfFile = shelve.open('mydata')
QA = shelfFile["QA"]
count = 1
repeat = True
while repeat == True :
    question = pyip.inputStr(prompt = "Enter the Question : ")
    answer = pyip.inputStr(prompt = "Enter the Answer :")
    QA[question] = answer
    repeat = pyip.inputBool(prompt = " Do you want to repeat (True/False)?")
    
    
shelfFile["QA"] = QA
shelfFile.close()
