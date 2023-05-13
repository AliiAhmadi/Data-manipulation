def compare(string1, string2):
    while string1 and string2:
        if string1[0] < string2[0]:
            string1 = string1[1:]
            
        elif string1[0] > string2[0]:
            string2 = string2[1:]
            
        else:
            string1 = string1[1:]
            string2 = string2[1:]
            
        string1 = string1[::-1]
        string2 = string2[::-1]
    
    if (not string1) and (not string2):
        return "Both strings are empty!"
    
    if not string1:
        return string2[::-1]
    
    return string1[::-1]


print(compare('ali', 'salib'))