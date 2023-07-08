scores = [90, 86, 69, 69, 69, 32, 100]

def gradeA(num):
    return num >= 90

a_scores = filter(gradeA, scores)
print(list(a_scores))

def letter_grade(num):
  if num >= 90:
    return "A"
  elif num >= 80:
    return "B"
  elif num >= 70:
    return "C"
  elif num >= 60:
    return "D"
  else: 
    return "F"
    
grades = list(map(letter_grade, scores))
print(grades)

combined = list(zip(scores, grades))
print(combined)