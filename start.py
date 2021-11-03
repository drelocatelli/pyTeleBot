import telepot

token = 'your token here'
bot = telepot.Bot(token)

def receivingMsg(msg):
    print(f'@{msg["chat"]["username"]} disse: {msg["text"]}')

    # send msg
    if(msg["text"] == '/vagas'):
        bot.sendMessage(msg["chat"]["id"], msg["text"])

bot.message_loop(receivingMsg)

while True:
    pass