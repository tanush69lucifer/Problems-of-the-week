import re

def reverse_words_with_delimiters(s):
    # Split into words and delimiters
    tokens = re.findall(r'[a-z]+|[^a-z]', s)
    # Extract words and reverse them
    words = [t for t in tokens if t.isalpha()][::-1]
    result = []
    word_idx = 0
    for t in tokens:
        if t.isalpha():
            result.append(words[word_idx])
            word_idx += 1
        else:
            result.append(t)
    return ''.join(result)

# Examples
print(reverse_words_with_delimiters("hello/world:here"))      # "here/world:hello"
print(reverse_words_with_delimiters("hello/world:here/"))     # "here/world:hello/"
print(reverse_words_with_delimiters("hello//world:here"))     # "here//world:hello"
