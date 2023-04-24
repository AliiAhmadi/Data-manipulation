my_list = [1, 2, 3, 4, 5]


result = map(lambda x: x ** 2, my_list)

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']

strings.sort(key=lambda string: len(set(list(string))))

print(strings)