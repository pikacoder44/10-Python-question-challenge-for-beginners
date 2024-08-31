# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.


def count_vowels(n=""):
    count =0
    for i in n:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            count+=1
    return count    

n = str(input("Enter a String: "))
print(count_vowels(n))