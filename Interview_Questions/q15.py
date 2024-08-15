"""
Q15. Find the number of words in a sentence.

Example: "How are you" --> 3

Use:
1. User Input
2. Function
3. f.string

Additional tasks : count only words
"""

special_chars = [';', ':', '!', "*", '?', "@", "#", "$", "%", "&"]
#initializing alphanumeric characters

def count_words(sentence):
    for i in special_chars:
        sentence = sentence.replace(i,'')
        # replace alphanumeric characters with ''

    word_list = sentence.split()
    print(word_list)
    return len(word_list)

user_input = input('Please enter a sentence: ')
num_words = count_words(user_input)

print(f'Word count is: {num_words}')