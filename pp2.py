def starts_B(s):
    return s[0]=="B"
fruit=["Apple","Banana","Cherry"]
filter_ob=filter(lambda s:s[0]=="B",fruit)

print(list(filter_ob))
