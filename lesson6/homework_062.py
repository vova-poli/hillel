while True:
    text = input("Enter your text with letter 'h': ")
    text = text.lower()

    if "h" in text:
        break
    else:
        print("Try again")