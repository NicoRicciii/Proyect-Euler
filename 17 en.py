from num2words import num2words

# using the "num2words" library, we can
# count the total number of letters in the variable "q"
 
q = 0
for i in range(1, 1001):

    s = num2words(i)
    for m in range(0, len(s)):

        if not(s[m] == " " or s[m] == "-"):
            q += 1

print(q)