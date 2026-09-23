# write a program to read the text from a file "poem.txt" and find out that whether it contains the word 'twinkle'

with open("poem.txt") as f:
    text = f.read()
    if "twinkle" in text:
        print("Yes, the word 'twinkle' is present in the file.")
    else:
        print("No, the word 'twinkle' is not present in the file.")
        