import sys
import time

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {} ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)


def text_to_words(txt):
    """ Return a list of words with all punctuation removed,
        and all in lowercase.
    """

    substitute = txt.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    clean_text = txt.translate(substitute)
    return clean_text.split()

    
def load_wds_file(filename):
    """ Read words from filename, return list of words. """
    with open(filename, "r") as f:
        file_content = f.read()
    wds = text_to_words(file_content)
    return wds


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab. """
    result = []
    for w in wds:
        if search_linear(vocab, w) < 0:
            result.append(w)
    return result


def find_unknown_words_index(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab using
        lists' index method as search function. """
    result = []
    for w in wds:
        try:
            if vocab.index(w) > 0:
                continue
        except ValueError:
            result.append(w)

    return result


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs. """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

def search_binary(xs, target):
    """ Find and return the index of target in sequence xs. """
    lb = 0
    ub = len(xs)
if __name__ == "__main__":
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    test(search_linear(friends, "Zoe") == 1)
    test(search_linear(friends, "Joe") == 0)
    test(search_linear(friends, "Paris") == 6)
    test(search_linear(friends, "Bill") == -1)

    vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass",
             "the", "tree"]
    book_words = "the apple fell from the tree to the grass".split()
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

    bigger_vocab = load_wds_file("vocab.txt")
    book_words = load_wds_file("alice_in_wonderland.txt")
    print("{} words in bigger_vocab, and {} in book_words".format(len(bigger_vocab), len(book_words)))

    t0 = time.clock()
    missing_words = find_unknown_words_index(bigger_vocab, book_words)
    t1 = time.clock()
    print("There are {0} unknown words.".format(len(missing_words)))
    print("That took {0:.4f} seconds using .index() method.".format(t1 - t0))

    t0 = time.clock()
    missing_words = find_unknown_words(bigger_vocab, book_words)
    t1 = time.clock()
    print("There are {0} unknown words.".format(len(missing_words)))
    print("That took {0:.4f} seconds using linear search algorithm.".format(t1 - t0))
