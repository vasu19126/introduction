text = input("Enter something : ")

#dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
dict = {}
for i in text :
    if i in dict :
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print(dict)