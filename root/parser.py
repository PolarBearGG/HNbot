import pandas as pd
import sqlite3


class Parser:

    def __init__(self) -> None:
        self.stories_id_url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
        self.conn = sqlite3.connect(
            '/home/korolyktv/HNbot/root/pythonStories.sqlite')

    def createDB(self):
        c = self.conn.cursor()

        c.execute('''
          CREATE TABLE IF NOT EXISTS stories
          (id INTEGER, 
           by TEXT,
           descendants INTEGER,
           kids BLOB,
           time INTEGER,
           title TEXT,
           score INTEGER,
           type TEXT,
           url TEXT)
          ''')

        c.execute('''
          CREATE TABLE IF NOT EXISTS history
          (id INTEGER)
          ''')

        self.conn.commit()

    def saveNewStories(self):
        df_new_top500_from_HN = pd.read_json(self.stories_id_url)
        history = pd.read_sql("select * from history", self.conn)
        for i, id in enumerate(df_new_top500_from_HN[0]):
            df_story_details_from_HN = pd.read_json(
                f'https://hacker-news.firebaseio.com/v0/item/{id}.json', orient='index').T

            if ('python' in df_story_details_from_HN['title'][0] or 'Python' in df_story_details_from_HN['title'][0]) and (len(history) == 0 or history['id'].astype(str).str.contains(str(df_story_details_from_HN['id'][0])).any() == False):
                df_story_details_from_HN.to_sql(
                    'stories', self.conn, if_exists='append', index=False)

    def getStory(self):
        df = pd.read_sql('select * from stories limit 1', self.conn)
        return df

    def rememberStoryId(self):
        df = self.getStory()
        c = self.conn.cursor()
        c.execute("INSERT INTO history VALUES (?)", (int(df['id'][0]),))
        self.conn.commit()

    def deleteStoryFromDB(self):
        df = self.getStory()
        c = self.conn.cursor()
        c.execute("DELETE FROM stories WHERE id = (?)", (int(df['id'][0]),))
        self.conn.commit()
