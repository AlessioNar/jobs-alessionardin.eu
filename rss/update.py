#! /usr/bin/env python

import pandas as pd 
from parser import get_rss



db = pd.read_csv('/home/alessio/blog.alessionardin.eu/static/data/raw_events.csv')
sources = pd.read_csv('/home/alessio/blog.alessionardin.eu/static/data/events.csv')

sources = sources[0:10]

df = get_rss(sources)

db = pd.concat([db, df])

# Sanitize dataframe
db.drop_duplicates()

db.to_csv('/home/alessio/blog.alessionardin.eu/static/data/raw_events.csv')










