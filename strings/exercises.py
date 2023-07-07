# returns sentence with first and last name
def format_name(first_name, last_name):
  return f'Hi, my name is {first_name} {last_name}.'

# returns a string starting from index 3, up to the second to last character
def index_string(string):
  return string[3:-2]

# returns index of char in a string, not case-sensitive
def index_of(string, char):
  return string.lower().index(char)

# returns boolean indicating whether last char is 'n'
def is_last_character_n(string):
  return string.endswith("n")

def long_burp(n):
  return "Bu" + "r" * n + "p"

def is_palindrome(string):
  return string == string[::-1]

# reverse a string recursively
def recursive_string(string):
  if len(string):
    return recursive_string(string[1:]) + string[0]
  else: return string