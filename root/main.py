from bot import send_message
import pandas as pd


df = pd.read_csv('stories.csv')

id = df["id"].head(1)[0]
title = df["title"].head(1)[0]
url = df["url"].head(1)[0]


text = f'<b>{title}</b>\n\n{url}'
send_message(text, '@PythomHN', 'HTML')

df = df.drop([0])
df.to_csv('stories.csv', index=False)

with open('history.txt', mode='a') as f:
    f.write(f'{id}\n')
