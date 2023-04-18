## BONUS ##

(
    netflix
    .assign(time_to_netflix = lambda df: df['year_added'] - df['release_year'])
    .groupby('type')
    ['time_to_netflix']
    .mean().round(1)
)

# on average it takes 5.7 years for a movie and 2.3 years for a TV show to make it to Netflix