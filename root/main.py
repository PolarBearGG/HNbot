from bot import Bot
from parser import Parser

p = Parser()
p.createDB()
p.saveNewStories()
df = p.getStory()

id = df["id"][0]
title = df["title"][0]
url = df["url"][0]


text = f'<b>{title}</b>\n\n{url}'


b = Bot("5183911411:AAGl7yMmUE5Soj1G-ztDBd4YCyTXjkrET2o",
        "Python_HN_bot", '@PythomHN')
b.send_message(text, "HTML")

p.rememberStoryId()
p.deleteStoryFromDB()
