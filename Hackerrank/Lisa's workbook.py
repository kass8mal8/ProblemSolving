left_chars = []
look_up = {'{':'}','[':']','(':')'}
statement = "[]()"
for char in statement:
    if '{' in look_up:
        left_chars.append(char)
    elif not left_chars or look_up[left_chars.pop()] != char:
        #return False
        pass
    
#print([x for x in left_chars.iter()])
#return not left_chars
print(left_chars)