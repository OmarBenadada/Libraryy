import re
result = re.search(r"\d+", " abab ")
print(result.group())  # Output: 100
