'''TASK 1: Hangman Game 
Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time. Simplified Scope: 
● Use a small list of 5 predefined words (no need to use a file or API). 
● Limit incorrect guesses to 6. 
● Basic console input/output — no graphics or audio. 
Key Concepts Used: random, while loop, if-else, strings, lists.
'''
LOGO='''
 _   _   ___   _   _ _____ ___  ___  ___   _   _   _____   ___  ___  ___ _____ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | | |  __ \ / _ \ |  \/  ||  ___|
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| | | |  \// /_\ \| .  . || |__  
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` | | | __ |  _  || |\/| ||  __| 
| | | || | | || |\  | |_\ \| |  | || | | || |\  | | |_\ \| | | || |  | || |___ 
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/  \____/\_| |_/\_|  |_/\____/ 
                                                                               
                                                                               

'''
import random
import hangman_images
print(LOGO)

words=["apple", 'bat','ball','cat','cow','artificial','intelligence','data','computing','blockchain','linux','webdevelopment','python']
selected_word=random.choice(words)
display=[]
lives=6
for i in range(len(selected_word)):
    display+='_'
print(display)
#while(True):
game_over=True
while game_over:    #if guess in selected_word:
    guess=input("Guess a letter: ").lower()      #print("yes")
    for i in range(len(selected_word)):
        if guess==selected_word[i]:
            display[i]=guess
            print(display)
        if '_' not in display:
           print("Hurray! you won.")
           game_over=False
           break
#for i in range(len(selected_word)):
    if guess not in selected_word:
        lives-=1
        print(hangman_images.stage[lives])
        print(f"you have {lives} chances left ")
        if lives==0:
            print("You are out of lives..")
            game_over=False

                 #else:
           # lives-=1
            #print(lives,"are left ")
