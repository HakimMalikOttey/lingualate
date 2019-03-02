from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Lingua")
#enables Chatboot to do time and mathematic calculation when asked
bot = ChatBot('Norman', storage_adapter = 'chatterbot.storage.SQLStorageAdapter',logic_adapters=['chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'],database_uri = 'sqlite:///database.db')
# Speeds up training process by exposing chatbot to existing conversations
trainer = ListTrainer(chatbot)
trainer.train([
    "Good morning",
    "Good afternoon",
    "Good night",
    "Howdy!",
    "Are you okay?",
    "How are you feeling?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "That is great!",
    "Congrats!"
])
print("Lingualate is a chatbot that runs on the chatterbot engine.")
print("This chatbot will hold the ability to learn how to speak different languages, which could be used to bridge gaps between cultures")
print("This chatbot could be used to help different peoples from different backgrounds communicate with each other automatically..")
print ("or could be used as a mutlicultural vendor that could communicate with anyone and everyone")
print ("However, in this build, it can respond to a multitude of languages, but can not speak them yet.")
print ('\n')
print('Type in a response to communicate with the chatbot')
#Loop will execute every time user inputs something
while True:
    try:
        user = input()
        response = chatbot.get_response(user)
        print (response)
        #Press ctrl c or ctrl d to exit loop
    except(KeyboardInterrupt, EOFError, SystemExit):
       break
