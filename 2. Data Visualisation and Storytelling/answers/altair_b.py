alt.Chart(wine).mark_point().encode(
    x='alcohol',
    y='color_intensity',
    color='class:N',
    tooltip = ['alcohol', 'color_intensity']
).properties(
    width=200,
    height=400
).interactive()
