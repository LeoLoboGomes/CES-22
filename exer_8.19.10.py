import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_palindrome (word):
    tamanho = len(word)
    if tamanho == 0:
        return False
    invertida = ""
    for i in range (tamanho):
        invertida += word[tamanho-1-i]
    if word == invertida:
        return True
    else: return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))    # Is an empty string a palindrome? No