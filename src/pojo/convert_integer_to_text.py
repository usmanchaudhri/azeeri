"""
Write a function to convert integer to text. Like 44556 should be Forty four thousand five hundred fifty six
"""

"""
which category the number calls under:
1's
10
100
1000
10000
100000
1000000
"""

"""
4 4 5 5 6
"""
def what_decimal_number(number):
    i = 1
    while (i < 1000000):
        if (number % i) == number:
            return i//10
        i = i*10
    return 0

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
twenties = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ["", "thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ",
             "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ",
             "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ",
             "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]

def num999(n):
    """
    NOTE: this method only constructs text strings for numbers upto 999.

    the idea is to break down a three digit number into one's, ten's, and hundred.
    and then for each individual component (hundred's, ten's, one's) we construct the
    final string
    """

    c = n % 10                               # singles digit
    b = ((n % 100) - c) // 10                # tens digit
    a = ((n % 1000) - (b * 10) - c) // 100   # hundreds digit

    # check if the number is not a number ending with zero
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + " hundred "
    elif a != 0:
        t = ones[a] + " hundred and"

    # for case 506 where '0' is in the middle, we don't need to write anything for that zero.
    # 0 will act silent and only 6 will be pronounced. 506 % 100 = 06 and only 6 will be printed
    # So, we can just lookup 6 in the one's array to check for the answer.
    if b <= 1:
        h = ones[n % 100]
    elif b > 1:
        # 556 where there are non-zero value for hundred and one's
        h = twenties[b] + ' ' + ones[c]

    st = t + ' ' + h
    return st

def number_to_text(number):
    # decimal_number = what_decimal_number(number)
    if number == 0:
        return 'zero'

    i = 3
    n = str(number)
    word = ""
    k = 0
    while i == 3:
        # breakdown the number into thousand starting from right to left.
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word

        if n == '':
            i = i +1
        k +=1

    print(word)

number_to_text(44556)
# number_to_text(44506)
print((556 % 100))


