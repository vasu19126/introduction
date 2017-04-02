def count():
    text = input("Enter something : ")

    dict = {}
    for i in text:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    print(dict)

for i in range(10):
    count()