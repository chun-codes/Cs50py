import re

email= input("What your email? ")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")