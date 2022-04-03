import requests
import urllib


TOKEN = "5183911411:AAGl7yMmUE5Soj1G-ztDBd4YCyTXjkrET2o"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
USERNAME_BOT = "Python_HN_bot"


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def send_message(text, chat_id, parse_mode):
    tot = urllib.parse.quote_plus(text)
    url = URL + \
        "sendMessage?text={}&chat_id={}&parse_mode={}".format(
            tot, chat_id, parse_mode)
    get_url(url)
