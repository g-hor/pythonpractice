a = 100
b = "5"
try:
  print(a/b)
except ZeroDivisionError:
  pass
except (TypeError, NameError) as error:
  print("what are u doin mate")
  print(f'this is what u did: {error}')