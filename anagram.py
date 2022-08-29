def anagram(a,b):\

## these variables will sort according to alphabets
    sort_a = sorted(a)
    sort_b = sorted(b)
    
## this variable will return the bolean value Either False or True
    is_anagram = False
    
## this if statement match the sorted variables 
    if sort_a == sort_b:
       is_anagram = True
    else:
       is_anagram = False
       
    return is_anagram
