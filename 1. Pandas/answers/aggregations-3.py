(
    netflix
    .groupby(['release_year', 'type'])
    .size()
    .unstack()
).tail(10)

# There were 658 movies and 244 TV shows released in 2016