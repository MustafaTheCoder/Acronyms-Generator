user_inp = str(input("Enter a Phrase: "))
text = user_inp.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)