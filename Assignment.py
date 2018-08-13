#Ask for Age and Name

name = (input("What is your name?\n"))
print("Hello", name)
Age = int(input("What is your Age?\n"))
# subtract Age from 2018 t0 get birth year
Birthyear = (2018 - Age)
Centurytime = (2018 - Age) + 100
print(name,"Your birthyear is", Birthyear)
print(name,"You will be 100 years old in", Centurytime)

