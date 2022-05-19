import feedparser
import pandas as pd
import time

def get_rss(sources):
    # Create temporary variable
    titles, urls, pub_dates = [], [], []
    df = pd.DataFrame()
    for index, element in sources.iterrows():
        # Here I could split the 
        item = feedparser.parse(element['url'])
        print('Requesting '+ element['source'] + ' RSS signals')
        print('Parsing RSS in dataframe')
        
        for event in item.entries:
            titles.append(event.title)
            urls.append(event.link)
            pub_dates.append(event.published)
        

        tmp_df = pd.DataFrame(list(zip(titles, urls, pub_dates)), columns = ['title', 'url', 'pub_date'])
        
        df = pd.concat([df, tmp_df])
        
        time.sleep(3)

    # Sanitizing output
    df = df.drop_duplicates()
    return df
