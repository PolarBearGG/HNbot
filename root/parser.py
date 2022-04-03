import pandas as pd

stories_id_url = 'https://hacker-news.firebaseio.com/v0/newstories.json'


def parseStories(stories_id_url):

    df_new_top500_from_HN = pd.read_json(stories_id_url)

    with open('history.txt', mode='r') as f:
        file = f.read()

    for i, id in enumerate(df_new_top500_from_HN[0]):

        df_story_details_from_HN = pd.read_json(
            f'https://hacker-news.firebaseio.com/v0/item/{id}.json', orient='index').T

        if ('python' in df_story_details_from_HN['title'][0] or 'Python' in df_story_details_from_HN['title'][0]) and str(df_story_details_from_HN['id'][0]) not in file:
            df_story_details_from_HN.to_csv(
                'stories.csv', mode='a', index=False, header=False)

    df = pd.read_csv("stories.csv", on_bad_lines='skip')
    df.drop_duplicates(inplace=True, keep=False, )
    df.to_csv("stories.csv", index=False)


parseStories(stories_id_url)
