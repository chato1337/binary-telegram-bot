from setup import bot_settings

import botogram

bot = botogram.create(bot_settings['telegram_token'])
bot.about = "Find the frame when the rocket takes of! by Didier Cuetia"
bot.owner = "@chatuz_dev"

"""
    at the moment the bot memory is managed by a 32b string in initial_data variable
    in the next order => [start, end, attemps]
    https://botogram.dev/docs/0.6.1/buttons/#buttons
"""
initial_data = "1,61696,1"

@bot.process_message
def process_text_message(chat):
    greeting(chat)

@bot.command("start")
def start_comand(chat):
    greeting(chat)

@bot.callback("play")
def play_callback(query, data, chat, message):
    parse_data = data.split(",")
    # uncomment to debug ;)
    # print(parse_data)
    start = int(parse_data[0])
    end = int(parse_data[1])
    attemps = int(parse_data[2])
    if attemps >= 16:
        game_over(chat, start, end)
    else:
        show_image(chat, start, end, attemps)


def show_image(chat, start, end, attemps):
    global initial_data
    middle = get_middle(start=start, end=end)
    link = get_image_link(middle)
    btns = botogram.Buttons()
    data_yes = [str(start), str(middle + 1), str(attemps + 1)]
    data_no = [str(middle + 1), str(end), str(attemps + 1)]
    btns[0].callback("yes", "play", ",".join(data_yes))
    btns[0].callback("no", "play", ",".join(data_no))
    btns[1].callback("start over", "play", initial_data)
    chat.send_photo(url=link)
    chat.send("⏲️ attemp #: " + str(attemps))
    chat.send("Has the rocket taken off? 🚀", attach=btns)

def greeting(chat):
    global initial_data
    btns = botogram.Buttons()
    btns = botogram.Buttons()
    chat.send("Hello, find the frame when the rocket takes off 🚀")
    btns[0].callback("start game 🎮", "play", initial_data)
    btns[1].url("check my repo 🤖", "https://github.com/chato1337/binary-telegram-bot",)
    chat.send("Select an option: ", attach=btns)

def get_image_link(frame) -> str:
    return bot_settings["api_frames"] + str(frame) + "/"

def get_middle(start: int, end: int) -> int:
    return (start + end) // 2

def game_over(chat, start, end):
    global initial_data
    middle = get_middle(start, end)
    link = get_image_link(middle)
    chat.send("number attemps reached!")
    chat.send_photo(url=link)
    btns = botogram.Buttons()
    btns[0].callback("play again", "play", initial_data)

if __name__ == "__main__":
    bot.run()
