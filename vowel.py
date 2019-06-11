v=input()
vow=['a','e','i','o','u','A','E','I','O','U']
if v in vow:
  print("Vowel")
elif v.isalpha():
  print("Consonant")
else:
  print("invalid")
