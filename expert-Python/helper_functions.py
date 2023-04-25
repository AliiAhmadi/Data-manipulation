from urllib.parse import parse_qs
import random
import itertools


query_string = "name=ali&family=ahmadi&age=20&midName="

parsed_query = parse_qs(query_string, keep_blank_values=True)

# print(parsed_query.get("names", [''])[0] or 0)

this = "ali"

# print(f"my name is {this!r}")

snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}

# print(snack_calories.items())

items = tuple(snack_calories.items())

# print(items)


random_bits = 0
for i in range(32):
    if random.randint(0, 1):
        random_bits |= 1 << i
        
        
print(bin(random_bits))