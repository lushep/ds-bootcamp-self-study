# Part E, DIRECTOR: use some advanced work with string, split and indexing to access the lead actor
netflix['cast'].str.split(',').str[0]