counter_data = 'counter-data.txt'
frequent_words_data = 'frequent-words-data.txt'

# Returns how many times pattern appears in text
def counter(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern)):
        match = text[i: i + len(pattern)]
        if match == pattern:
            count += 1
    return count
# Returns the most frequent k-mers in text
def frequentWords(text, k):
    k = int(k)
    frequent_patterns = {}
    for i in range(0, len(text) - k + 1):
        match = text[i: i + k]
        if match in frequent_patterns:
            frequent_patterns[match] += 1
        else:
            frequent_patterns[match] = 1
    
    highest_key = max(frequent_patterns, key=frequent_patterns.get)
    highest_val = frequent_patterns[highest_key]

    results = set()
    for key in frequent_patterns:
        if frequent_patterns[key] == highest_val:
            results.add(key)

    return results

def main():
    # Solving problem 1:
    # How many times patterns appears in text
    with open(counter_data) as cd:
        content = cd.readlines()
        content = [x.strip() for x in content]
        count = counter(content[0], content[1])
        print("%s instances %s appeared in file" % (count, content[1]))

    # Solving problem 2:
    # Getting the most frequent k-mers in text
    with open(frequent_words_data) as fwd:
        content = fwd.readlines()
        content = [x.strip() for x in content]
        text = content[0]
        k = content[1]
        print(*frequentWords(text, k))

if __name__ == "__main__":
    main()

