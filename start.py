import telepot

token = 'your token here'
bot = telepot.Bot(token)

def receivingMsg(msg):
    # user says: 
    print(f'@{msg["chat"]["username"]} disse: {msg["text"]}')

bot.message_loop(receivingMsg)

while True:
    pass
