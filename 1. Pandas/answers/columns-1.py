(
    netflix
    .assign(time_to_netflix = lambda df: df['year_added'] - df['release_year'])
    ['time_to_netflix'].mean()
)

# on average it takes 4.7 years for a show to make it to Netflix