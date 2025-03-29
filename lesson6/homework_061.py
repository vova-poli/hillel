text = input("Enter your text: ")
text = text.lower()
unique_symbols = ""

for i in text:
    if i not in unique_symbols:
        unique_symbols += i
    else:
        continue

if len(unique_symbols) > 10:
    print(f"{True}. Amount of unique symbols: {len(unique_symbols)}")
else:
    print(f"{False}. Amount of unique symbols: {len(unique_symbols)}")



