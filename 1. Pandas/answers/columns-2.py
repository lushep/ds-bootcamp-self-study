(
    netflix
    .groupby(['release_year', 'type'])
    .size()
    .unstack()
    .assign(Difference = lambda df: df['Movie'] - df['TV Show'])
).tail(10)

# there were 38 more TV Shows released in 2021