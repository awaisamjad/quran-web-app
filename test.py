import re
from db import get_verses_by_id

s = "hello [1] world [2] my [3] name"

# Split using regex, matching anything inside square brackets
result = re.split(r"\s*\[\d+\]\s*", s)
verses = get_verses_by_id(1)
verses_list = re.split(r"\s*\[\d+\]\s*", verses[0][0])
print(verses_list)
# Print the result
# print(result)