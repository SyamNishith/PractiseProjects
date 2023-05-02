s=input("enter the string:")
def palindrome(s):
  rev=s[::-1]
  if rev==s:
    return True
if(palindrome(s)==True):
  print(s,"is a palindorme")
else:
  print(s,"not a palindrome")
