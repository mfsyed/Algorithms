

def counting_sort(wordlist, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    fd = dict()
    answer = []
    for word in wordlist:
        letter = word[index]
        try:
            fd[letter].append(word)
        except:
            fd[letter] = [word]

    for letter in alphabet:
        try:
            answer.extend(fd[letter])
        except:
            answer.extend([])

    return answer


def martian_sort(wordlist, order):
    """
    Input: wordlist | a list of Martian words, consisting of lowercase letters and all the same length k
    Input: order | a permutation of [0, ..., k-1]

    Return the list of words in wordlist sorted based on order, as described in the problem set

    Runs in O(kn) time.
    """
    index = order.pop()
    answer = counting_sort(wordlist,index)

    while len(order) > 0:
        index = order.pop()
        answer = counting_sort(answer,index)


    return answer
