def get_consonant_value(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    
    values = []
    s_value = 0
    
    
    for i in range(len(string)):
        character = string[i]
        if str.__contains__(vowels, character):
            if i != 0 and s_value != 0:
                values.append(s_value)
                s_value = 0
        else:
            s_value+=alphabet.find(character) + 1
            
        if i == (len(string) - 1) and s_value != 0:
            values.append(s_value)
        
    values.sort(reverse=True)
    
    return values[0] if len(values) > 0 else 0

print(get_consonant_value('zodiacs'))
# print(get_consonant_value('strength'))


