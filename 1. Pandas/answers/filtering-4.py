netflix.loc[lambda df: (df['listed_in']=='Comedies, Independent Movies')
                       & (df['release_year']>2010)
                       & (df['rating'] == 'R')
                       & (df['title'].str.count(' ') == 0) # optional (can answer through visual inspection)
                       & (df['director']==df['cast'].str.split(',').str[0]) # optional (can answer through visual inspection)
           ]

# The movie is Chef