from rivescript import RiveScript

mika = RiveScript()
mika.load_directory("./brain")
mika.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = mika.reply("localuser", msg)
    print('Mika>', reply)
