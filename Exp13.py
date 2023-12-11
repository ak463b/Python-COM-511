#Specify the file path:-
file path =  r "C:\Users\alokk\OneDrive\Documents\pythonprogram\Input.txt"
#Read and print the context of file:-
with open(file path,"r") as file:
    file_content = file.read()
    print("Contents of the file:")
    print(file_content)
    
#Extract unique words and sort them alphabetically:-
words = file_content.split()
unique_words = sorted(set(words))

#Print unique words:-
print("\n Unique words in alphabetical order:")
for words in unique_words:
    print(words)