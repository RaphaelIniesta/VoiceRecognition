
import voice_recognition as vr
import time
import os

instructions = """
First things first. These are the rules of the game:
1) Don't look up on the internet for the answers, because you won't have enough time
2) For your answer be accepted, you'll need to say "Alternative (number)" (I'm working on that)
3) If you want, you can play with someone
4) The room need to be as quiet as possible or your answer will not be accepeted
5) Have fun :)
"""


q1 = """
1. What is the biggest ocean in the world?
1) Pacific
2) Atlantic
3) Indigo
4) Artic
5) Mediterranean
"""
aQ1 = "1) Pacific"

q2 = """
What is the biggest country in the world?
1) China
2) India
3) USA
4) Brazil
5) Russia
"""
aQ2 = "5) Russia"

q3 = """
What is the second best selling book in the world after the Bible?
1) Dom Quixote
2) Lord of the Rings
3) The Little Prince
4) Harry Potter
5) Quran
"""
aQ3 = "1) Dom Quixote"

"""
This is for developers:

Apparently, there are some issues with monosyllabic words, such as 'one'.
In portuguese, my mother language, the program don't recognize the 'um' (1) sound. I think it recognize it as background noise.
They may have more similar problems in other languages, so bo on lookout for any errors
"""

def questions():
    print(instructions)
    time.sleep(15)
    os.system('cls')

    print(q1)
    answer1 = vr.Recognition()

    if ('one' not in answer1):
        print(answer1)
        print("Incorrect. The answer is:", aQ1)
        time.sleep(3)
        os.system('cls')
    else:
        print("Correct! Prepare for the next question.")
        time.sleep(3)
        os.system('cls')

    print(q2)
    answer2 = vr.Recognition()

    if ('5' not in answer2):
        print("Incorrect. The answer is:", aQ2)
        time.sleep(3)
        os.system('cls')
    else:
        print("Correct! Prepare for the next question.")
        time.sleep(3)
        os.system('cls')

    print(q3)
    answer3 = vr.Recognition()

    if ('one' not in answer3):
        print("Incorrect. The answer is:", aQ3)
        time.sleep(3)
        os.system('cls')
    else:
        print("Correct! Prepare for the next question.")
        time.sleep(3)
        os.system('cls')

questions()