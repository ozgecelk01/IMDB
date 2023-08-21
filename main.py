import pandas as pd

path = 'imdb_top_1000.csv'
df = pd.read_csv(path)

df.drop(['Poster_Link','Certificate','Overview','Meta_score','No_of_Votes','Gross','Runtime'],axis = 1,inplace= True)

name=input("Actress or Actor or Director name: ")

found_entries = df[df[['Director', 'Star1', 'Star2', 'Star3', 'Star4']].apply(lambda row: row.str.contains(name, case=False)).any(axis=1)]['Series_Title']

if not found_entries.empty:
    found_entries.index = found_entries.index + 1
    print(found_entries)
else:
    print("Not found.")
