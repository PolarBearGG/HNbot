from bot import Bot
from parser import getStory, rememberStoryId


def main():

    story = getStory()
    title = story['title'][0]
    url = story['url'][0]

    text = f'<b>{title}</b>\n\n{url}'

    b = Bot('token',
            'Python_HN_bot', '@PythomHN')
    b.send_message(text, 'HTML')
    rememberStoryId()


if __name__ == '__main__':

    main()
