text = input("Enter a string: ")

for ch in dict.fromkeys(text):
    if ch != " ":
        print(ch, ":", text.count(ch))
