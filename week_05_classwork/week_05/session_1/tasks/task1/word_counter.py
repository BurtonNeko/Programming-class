# Your aim is to read in a text file, and calculate how many words are in it.
# You should:
#    - ask the user to enter the file name
#    - read the file in
#    - count how many words are in the file - there are multiple ways of doing this.

# You can use any of the .txt files to test this - or even make your own.

# get the file name
def count_words_in_file():
  
    filename = input('The text to be read: ')
# open and read the file
    try:        
          with open(filename, 'r', encoding='utf-8') as file:
              total_words = 0
              for line in file:
                  words = [word for word in line.strip().split() if word]
                  total_words += len(words)
          print(f"Text '{filename}' has total words of {total_worlds}")   
# hint: remember to handle the case where the file might not exist
    except FileNotFoundError:
          print(f'Text Not Found')
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 215
