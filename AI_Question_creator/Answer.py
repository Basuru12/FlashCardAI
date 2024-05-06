import openai
import pyinputplus as pyip
import shelve
import random
ShelfFile = shelve.open("mydata")
QA = ShelfFile["QA"]
Questions = list(QA.keys())
random.shuffle(Questions)
openai.api_key = ""
for key in Questions:
    answer = pyip.inputStr(prompt = key)
    

    messages = []
    system_msg = f"you are a robot made to check the validity of an answer given by a user to a question asked by a pogramme. the correct answer is { QA[key]} . the answer given by the user is {answer}. if the answer given by the user is the correct answer or simmillar in meaning to the correct answer you have to say the answer is correct. if it is wrong you have to provide the correct answer to the user"
    messages.append({"role": "system", "content": system_msg})

    
    messages.append({"role": "user", "content": answer})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

    
