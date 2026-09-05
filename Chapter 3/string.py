# Single or Double quotes for single-line text
str1 = 'Hello'
str2 = "World"

# Triple quotes for multi-line text
str3 = '''This is a 
multi-line string'''

name = "Harry"
nameshort = name[0:3]  # Slicing the string to get first three characters   it will exclude 3
print(nameshort)

text = "PYTHON"

# Index positions:
#  P   Y   T   H   O   N
#  0    1   2   3   4   5
# -6  -5  -4  -3  -2  -1
print(text[::-1])  # Output: 'NOHTYP' (Step -1 reverses the entire string)


# D A T A B A S E
# 0 1 2 3 4 5 6 7

#  D  A  T  A  B  A  S  E
# -8 -7 -6 -5 -4 -3 -2 -1

# word[4:] ka output kya hoga?   Output : BASE

# word[:-3] ka output kya hoga?  Output : DATAB

# word[-5:] ka output kya hoga?  Output : ABASE

word = "PROGRAM"
# Index guide:
#  P   R   O   G   R   A   M
#  0   1   2   3   4   5   6
# -7  -6  -5  -4  -3  -2  -1

#word[-5:] ka output kya hoga?   Ouutput: OGRAM

#word[:-4] ka output kya hoga?  Output: PRO



word = "AUTOMATION"

# Index Guide:
# Positive:  0   1   2   3   4   5   6   7   8   9     What is the output of word[1:9:2]?   it is U O A I
# Letters:   A   U   T   O   M   A   T   I   O   N     
# Negative: -10 -9  -8  -7  -6  -5  -4  -3  -2  -1    What is the output of word[8:1:-2]   it is O T M A

print ("\"Harry is a good boy\n and not a bad boy\"")