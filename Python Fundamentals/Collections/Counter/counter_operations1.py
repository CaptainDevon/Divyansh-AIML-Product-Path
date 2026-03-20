from collections import Counter

day1_checkouts=Counter({"fiction":7,"non_fiction":4,'mystery':5,"sci-fi":2})
day2_checkouts=Counter({"fiction":5,"non_fiction":6,'mystery':8,"sci-fi":3})

total_checkouts=day1_checkouts+day2_checkouts
print(total_checkouts)

difference_between_days=day2_checkouts-day1_checkouts
print(difference_between_days)
# You wil not see fiction in the list because after substraction it comes to negative and hence it will not show 