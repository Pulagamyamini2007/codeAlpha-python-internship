def bot_reply(user):
    if user in['hello','hi','hey']:
        return 'Hi!'
    elif user=="good morning":
        return "good morning"
    elif user=="how are you":
        return "I am Good"
    elif user=="what's your name":
        return "I am a basic chat bot"
    elif user=="bye":
        return "Good bye!"
    else:
        return "Sorry! i didn't know that."
print("Welcome to the Basic chatBot")
Continue=True
while Continue:
    user=input("You: ").lower()
    reply=bot_reply(user)
    print("Bot: ",reply)
    if reply=="Good bye!":
        Continue=False
        