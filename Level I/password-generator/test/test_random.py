import string 
import random

# Generating a random string of length 8 using ascii_letters
random_string = ''.join(random.choices(string.hexdigits, k=20))
print(random_string)

low_case = "abcdefghijklmnopqrstuvxyz"
up_case = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "0123456789"
special_character = '"£$&()*+[]@#^-_!'

# Source - https://stackoverflow.com/a
# Posted by Salvador Dali
# Retrieved 2025-11-16, License - CC BY-SA 3.0

# def LCG(seed, n, a=1664525, c=1013904223, m=2**32):
#     numbers = []
#     for i in range(n):
#         seed = (a * seed + c) % m
#         numbers.append(seed)

#     return numbers

# print(LCG(3, 5))


# Source - https://stackoverflow.com/q
# Posted by J. Taylor, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-16, License - CC BY-SA 4.0

from nltk.corpus import words
from random import sample

n = 100

rand_words = ' '.join(sample(words.words(), n))

