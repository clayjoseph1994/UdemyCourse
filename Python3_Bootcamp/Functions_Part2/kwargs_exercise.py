#INSTRUCTIONS
#Write a function called combine_words that accepts a single string called word and any number of additional
#keyword arguments. If a prefix is provided, return the prefix followed by the word.
#If a suffix is provided, return the word followed by the suffix.
#If neither a prefix or suffix is provided, just return the word

# Define combine_words below:

def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        if 'suffix' in kwargs:
            return kwargs['prefix'] + word + kwargs['suffix']
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    else:
        return word

#testing
print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("chimp", suffix="ape", prefix="monkey"))


#trying something else
def yeet(word2, **kwargs):
    if 'prefix' and 'suffix' in kwargs:
        return kwargs['prefix'] + word2 + kwargs['suffix']
    # elif 'prefix' in kwargs and 'suffix' not in kwargs:
    #     return kwargs['prefix'] + word2
    # elif 'suffix' in kwargs and 'prefix' not in kwargs:
    #     return word2 + kwargs['suffix']
    else:
        return word2


print(yeet("bing", prefix="mega", suffix="mini"))
print(yeet("bing"))