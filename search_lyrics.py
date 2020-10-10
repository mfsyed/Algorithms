PRIME = 2 ** 31 - 1


def search_lyrics(L, Q):
    """
    Input: L | an ASCII string
    Input: Q | an ASCII string where |Q| < |L|

    Return `True` if Q appears inside the lyrics L and `False` otherwise.
    """

    ##################
    # YOUR CODE HERE #
    if len(L) < len(Q):
        return False

    power = 1 #exponent
    total = 0 #query_hash_value
    sub = 0 #lyric_substring_hash_value

    for i, c  in enumerate(Q[::-1]):
        total += ord(c)*power
        sub  += ord(L[len(Q)-i-1])*power
        power *= 128

    i += 1
    power = power%PRIME
    total = total%PRIME
    sub = sub%PRIME

    if total == sub:
        return True

    for l in range(i,len(L)):
        sub = (sub*128-ord(L[l-len(Q)])*power + ord(L[l]))%PRIME
        if sub == total:
            return True

    return False
    ##################
