# fstrings

# normal string vs f-string
statement = "I love {'this'} Python"
print(statement)
statement = f"I love {'this'} Python"
print(statement)

# f string
# curly braces cannot be empty
# statement = f"I love Python {}"  # curly braces cannot be empty! will fail

# f string
# another_string = "so much"
# statement = f"I love Python {another_string}"
# print(statement)


# print(f"The sum of 5 and 5 is {5+5}")
# print(f"The sum of 5 and 5 is {statement.replace('love', 'hate')}")
