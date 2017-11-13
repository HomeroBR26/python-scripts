"""Unit test."""
import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {} ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file). """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("S") == "W")
    test(turn_clockwise(42) is None)
    test(turn_clockwise("rubbish") is None)


def absolute_value(x):
    """ Return absolute value of x. """
    if x < 0:
        return -x
    return x


def turn_clockwise(dir):
    """ Return next compass point clockwise. """
    compass = ["N", "E", "S", "W"]
    if dir in compass:
        if dir == "W":
            return "N"
        return compass[compass.index(dir) + 1]

if __name__ == "__main__":
    test_suite()
