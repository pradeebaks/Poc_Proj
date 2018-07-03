import re
var = "this is a replace of abthe abthejelkwe sdjkkab"
x = re.compile('ab', re.IGNORECASE)
var=x.sub("food",var)
print(var)
num ="123_ 445_ 123_ 45667 jhkhf8 732472734 1234"

r = re.findall("\d{3}_?",num)
#r = re.findall("\w[a-z]",num)
print(r)