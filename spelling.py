'''
Check spelling prior to SQL look-up
'''

from difflib import get_close_matches as find_match


with open('data/spell.words.txt', 'r') as words:
    words = [word.strip() for word in words]
with open('data/country.txt') as myfile:
    country = myfile.read()


def checker(word):

    if word.lower() in words:
        return word
    elif word.title() in country:
        return word
    elif word.upper() in country:
        return word
    # return the 1st of the top 15% matching possibilities
    elif len(find_match(word, words, cutoff= .85)) > 0:
        return find_match(word, words)[0]
    else:
        return "oops! we can't find that word"


