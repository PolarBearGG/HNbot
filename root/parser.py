import pandas as pd
import sqlite3


def getStory():
    conn = sqlite3.connect(
        '/home/korolyktv/HNbot/root/pythonStories.sqlite')
    c = conn.cursor()

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

    conn.commit()

    df_new_top500_from_HN = pd.read_json(
        'https://hacker-news.firebaseio.com/v0/newstories.json')
    history = pd.read_sql('select * from history', conn)
    for i, id in enumerate(df_new_top500_from_HN[0]):
        df_story_details_from_HN = pd.read_json(
            f'https://hacker-news.firebaseio.com/v0/item/{id}.json', orient='index').T

        if ('python' in df_story_details_from_HN['title'][0] or 'Python' in df_story_details_from_HN['title'][0]) and (len(history) == 0 or history['id'].astype(str).str.contains(str(df_story_details_from_HN['id'][0])).any() == False):
            df_story_details_from_HN.to_sql(
                'stories', conn, if_exists='append', index=False)

    df = pd.read_sql('select * from stories limit 1', conn)
    return df


def rememberStoryId():
    conn = sqlite3.connect(
        '/home/korolyktv/HNbot/root/pythonStories.sqlite')
    df = pd.read_sql('select * from stories limit 1', conn)
    c = conn.cursor()
    c.execute('INSERT INTO history VALUES (?)', (int(df['id'][0]),))
    c.execute('DELETE FROM stories WHERE id = (?)', (int(df['id'][0]),))
    conn.commit()
