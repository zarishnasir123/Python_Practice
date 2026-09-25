# 5. Repeat program 4 for a list of such words to be censored.


words = ["Donkey", "ganda", "bad"]

with open("prob4.txt", "r") as f:
    content = f.read()
    
for word in words:
    contentNew = content.replace(word, "######")

with open("prob4.txt", "w") as f:
    f.write(contentNew)