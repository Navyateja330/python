def leftover(a, b):
    left = ""
    remove = set(b)

    for ch in a:
        if ch not in remove:
            left += ch

    if left == "":
        print("empty")
    else:
        print(left)


a = "abcde"
b = "bde"
leftover(a, b)
