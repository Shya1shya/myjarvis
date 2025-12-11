from chatterbot.trainers import ListTrainer
from chatterbot import Chatbot

bot = Chatbot('Test')
conv = open("chats.txt","r").readliens()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request = input('you: ')
    response = bot.get_response(request)
    print('Bot: ', response)