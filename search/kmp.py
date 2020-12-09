"""
This module contains kmp implementation.

Terms:
    FSM: Finite State Machine
    lps: Longest Proper Suffix(prefix)

You can run a test using this command:
    python3 -m doctest kmp.py -v
or just
    python3 kmp.py [--verbose]
"""


def create_fsm(pattern, optimize=True, verbose=False):
    """ Create an optimized Finite State Machine.

    Args:
        pattern (string): A string to analyze.

    Returns:
        list: Optimized state machine, in list form.

    Examples:
        >>> create_fsm("10100111", optimize=True)
        [-1, 0, -1, 0, 2, -1, 1, 1]
        >>> create_fsm("10100111", optimize=False)
        [-1, 0, 0, 1, 2, 0, 1, 1]
    """

    # Create FSM(The next array).
    next = [None] * len(pattern)
    lps = -1  # Longest proper prefix
    for current_char_index in range(0, len(pattern)):
        next[current_char_index] = lps
        while (lps >= 0) and (pattern[current_char_index] != pattern[lps]):
            lps = next[lps]
        lps += 1

    # Optimize FSM.
    if optimize:
        for current_char_index in range(0, len(pattern)):
            lps = current_char_index
            while (lps >= 0) and (pattern[current_char_index] == pattern[lps]):
                lps = next[lps]
                next[current_char_index] = lps

    return next


def kmp(text, pattern, verbose=False):
    """
    >>> kmp("ABBBCBABDBEBABBABABA", "ABAB")
    15
    >>> kmp("ABBBCBABDBEBABBABABA", "ABCD")
    -1
    """
    if verbose:
        print("KMP search for a given pattern \"" +
              pattern + "\" in \"" + text + "\".")

    next = create_fsm(pattern=pattern, optimize=True, verbose=verbose)

    if verbose:
        print("FSM for the pattern(next): " + str(next))

    current_char_index = 0
    comparisons = 0
    lps = 0

    while current_char_index < len(text) and lps < len(pattern):
        if verbose:
            print("")
            print("Text:        ", end='')
            print(text[0:current_char_index] + "[" +
                  text[current_char_index] + "]" + text[current_char_index+1:])
            print("Pattern:     ", end='')
            print((" "*(current_char_index-lps)) +
                  pattern[0:lps] + "[" + pattern[lps] + "]" + pattern[lps+1:])

        # The inner loop below might be reduced to a single if-statement
        # when the FSM is optimized (No need to keep jumping).

        # Reaching the loop means the condition of the loop above is evaluated for
        # at least one time.
        comparisons += 1

        while (lps >= 0) and (text[current_char_index] != pattern[lps]):
            comparisons += 1
            lps = next[lps]
            if verbose:
                print("Miss! lps is now " + str(lps) + ".")
                print("Pattern:     ", end='')
                print((" "*(current_char_index-max(lps, 0))) + pattern[0:max(
                    lps, 0)] + "[" + pattern[max(lps, 0)] + "]" + pattern[max(lps, 0)+1:])

        current_char_index += 1
        lps += 1

    print("")

    if lps == len(pattern):
        found_index = current_char_index - len(pattern)
        if verbose:
            print("Pattern found at index " + str(found_index) + ": ", end='')
            print(text[0:found_index] + "[" + pattern + "]" +
                  text[found_index+len(pattern):])
            print(str(comparisons) + " comparisons.")
        return found_index
    else:
        if verbose:
            print("Pattern not found.")
            print(str(comparisons) + " comparisons.")
        return -1


if __name__ == "__main__":
    from common.invoker import from_input

    inputs = []
    def insert(key, verbose): return inputs.append(key)

    def search(key, verbose): return True if kmp(
        ''.join(inputs), key, verbose) != -1 else False
    from_input(insert, search, True)
