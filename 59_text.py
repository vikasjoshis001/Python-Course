import textwrap
value=input("Enter text: ")
width=int(input("Enter width: "))
wrapper = textwrap.TextWrapper(width=width) 
  
word_list = wrapper.wrap(text=value) 
  
# Print each line. 
# for element in word_list: 
print(word_list) 