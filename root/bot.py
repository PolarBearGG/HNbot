import requests
import urllib


class Bot:

    def __init__(self, token, username_bot, chat_id) -> None:
        self.token = token
        self.username_bot = username_bot
        self.chat_id = chat_id
        self.url = f'https://api.telegram.org/bot{token}/'

    def get_url(self, url):
        self.response = requests.get(url)
        self.content = self.response.content.decode("utf8")
        return self.content

    def send_message(self, text, parse_mode):
        tot = urllib.parse.quote_plus(text)
        url = f'{self.url}sendMessage?text={tot}&chat_id={self.chat_id}&parse_mode={parse_mode}'
        self.get_url(url)
