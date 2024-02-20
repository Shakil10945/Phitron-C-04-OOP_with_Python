import re

def clean_string(text):
    # Remove multiple consecutive commas with a single comma
    text = re.sub(r',+', ',', text)
    
    # Remove any other unwanted characters (in this case, it removes non-alphanumeric characters except commas)
    text = re.sub(r'[^a-zA-Z0-9,]+', '', text)
    
    return text

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output)

