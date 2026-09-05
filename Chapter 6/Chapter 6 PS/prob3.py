#a spam comment is defined as a text contatining the following keywords

# "Make a lot of money", "buy now", "click this", "subscribe", "free", "limited time offer"

text = ["Make a lot of money", "buy now", "click this", "subscribe", "free", "limited time offer"]

input = str(input("Enter a comment: "))


if ("Make a lot of money" in text or "buy now" in text or
    "click this" in text or
    "subscribe" in text or
    "free" in text or
    "limited time offer" in text):
    print("This is a spam comment")


elif ("Make a lot of money" not in text and "buy now" not in text and
    "click this" not in text and
    "subscribe" not in text and
    "free" not in text and
    "limited time offer" not in text):
    print("This is not a spam comment")

print("Thank you for using the program.")