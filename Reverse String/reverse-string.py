#define the function to reverse the string 
def reverse_string(text):
    #converting the input to string
    text=str(text)

    #reverse the string
    return text[::-1]

print(reverse_string("Hello, World!"))