(
    netflix
    .assign(dominant_topic = lambda df: df['listed_in'].str.split(',').str[0])
    .loc[lambda df: df['dominant_topic'].isin(['TV Sci-Fi & Fantasy']), 'description']
    .iloc[0]
)

# After waking up aboard a derelict spaceship with no memories, the crew 
# of the Raza investigates the mystery of their identities and destination.