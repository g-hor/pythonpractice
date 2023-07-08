sequence = ('hi', 'bye', 'wat')

def print_sequence(self):
  for ele in sequence:
    print(ele)


dictionary = {1: sequence, 'b': 42, 69: 'howdy', 'a': print_sequence}

for key in dictionary:
  print(key)
  print(dictionary[key])


list = [sequence, dictionary, print_sequence]


# print(sequence * dictionary) # ERRORS OUT
# print(dictionary * 5) # ERRORS OUT
# print(sequence * 5)
# print(list)
# print(list + sequence) # ERRORS OUT
# print(list + list)
# print(sequence + sequence)

# list.append(420)
# print(list)

# list.reverse()
# list.remove(print_sequence)
# print(list)


tuple = 1, 2, 3
print(tuple)
print(tuple[0])
tuple.append(69)
print(tuple)