# Text Analyzer // With a String given, ask the user for three letters to search them in the String.
# How many times the letters appear in the Sting?
# How many words does the String have?
# First and last letter.
# Show the words in reverse order.
# The string does have "Python" in it?

# Ask for a String to analyze
# Use .lower to make the string easy to analyze

text = input("Insert a text to analyze it: ").lower()

# Ask for 3 letters to search for
# Use .lower to match the given letters to the string

letter1 = input("Insert your first letter: ").lower()
letter2 = input("Insert your second letter: ").lower()
letter3 = input("Insert your third letter: ").lower()

# Count how many times each letter appear

counter1 = text.count(letter1)
counter2 = text.count(letter2)
counter3 = text.count(letter3)

# Return of the count using F-String

print(f"\nThe letter '{letter1}' appears {counter1} times!\nThe letter '{letter2}' appear {counter2} times!\nThe letter '{letter3}' appears {counter3} times!")

# How many words does the text have?
# Using split to separete the words and group them in a list to count them with len function.

split_words = text.split()
wordscounter = len(split_words)

print(f"\nYour text have {wordscounter} words!")

# First and last letter. Use index to find each letter.

first_letter = text[0]
last_letter = text[-1]

print(f"\nThe first letter is '{first_letter}' and the last letter is '{last_letter}'\n")

# Show the words in reverse order.
# Create a new list with the text splited (.split)
# Use reversed in the list and store it with list()
# Use join to put the spaces again

words_list = list(text.split())
reversed_list = list(reversed(words_list))
print(" ".join(reversed_list).strip())

# The string does have "Python" in it?

result = "Python" in text

print(f"\n¡Is {result} that the word 'Python' is in your text!")







