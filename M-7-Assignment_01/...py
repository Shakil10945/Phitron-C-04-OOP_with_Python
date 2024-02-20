original_string = "hello"
original_string = bytearray(original_string, 'utf-8')
print(type(original_string))
original_string[0] = ord('H')  # Modify the first character
original_string = original_string.decode('utf-8')
print(type(original_string))
print(original_string)