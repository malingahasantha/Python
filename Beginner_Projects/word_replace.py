"""
Write program to replace words of a sentence
"""

def replace_word():
    sentence = "Hi guys, i am malinga, and hi hi hi"

    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')

    print(sentence.replace(word_to_replace,word_replacement))

replace_word()

# The replace() method replaces a specified phrase with another specified phrase.
"""
string.replace(oldvalue, newvalue, count)

oldvalue - Required. The string to search for
newvalue - Required. The string to replace the old value with
count	- Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
"""