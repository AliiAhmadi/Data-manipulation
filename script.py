from collections import defaultdict


test = defaultdict(list)


words = ["ali", "ahmad", "reza", "salman"]

for word in words:
    test[word[0]].append(word)
    

print(test)

# test_dict = {}
# for word in words:
#     test_dict[word[0]].append(word)