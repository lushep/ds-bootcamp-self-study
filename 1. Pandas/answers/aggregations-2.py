(
    netflix.groupby(['year_added', 'month_added'], as_index=False)
    .size()
    .sort_values(['year_added','month_added'])
)

# in 2003 content was added only in December (month 12)