"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
grade_to_test = int(input("What was your grade?"))
if grade_to_test == 100:
    print(f"Your grade was {grade_to_test} You get A+!")
elif grade_to_test >= 90:
    print(f"Your grade was {grade_to_test} You get A")
elif grade_to_test >= 80:
    print(f"Your grade was {grade_to_test} You get B")
elif grade_to_test >= 70:
    print(f"Your grade was {grade_to_test} You get C")
elif grade_to_test >= 60:
    print(f"Your grade was {grade_to_test} You get D")
else:
    print(f"Your grade was {grade_to_test} You get F")
