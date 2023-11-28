#The functions that you will test here are:
#num_of_a_kind()
#yahtzee()
#Create a new file called test_yahtzee2.py in the same folder as yahtzee2.py.
#Start by importing the functions you want to test from yahtzee2.py in the file test_yahtzee2.py.
#Write six unit tests, covering the following cases:
#a) “3 of a kind” found
#b) “3 of a kind” not found
#c) “4 of a kind” found
#d) “4 of a kind” not found
#e) “Yahtzee” found
#f) “Yahtzee” not found
#Each test must have a hardcoded roll and a single assertion.
#Use the following template. All unit tests defined in the template must be present and implemented in your code (you may not omit anything).

from yahtzee1 import sum_of_given_number, fill_upper_section
from yahtzee2 import num_of_a_kind, yahtzee

def test_sum_of_given_number_all_different():
    """
    Tests sum_of_given_number() with one roll
    where all dice have different face values.
    """
    roll = [1,2,3,4,5]
    assert sum_of_given_number(roll, 1) == 1
    assert sum_of_given_number(roll, 2) == 2
    assert sum_of_given_number(roll, 3) == 3
    assert sum_of_given_number(roll, 4) == 4
    assert sum_of_given_number(roll, 5) == 5
    assert sum_of_given_number(roll, 6) == 0

def test_sum_of_given_number_all_same():
    """
    Test sum_of_given_number() with one roll
    where all dice have the same face value.
    """
    roll = [3,3,3,3,3]
    assert sum_of_given_number(roll, 1) == 0
    assert sum_of_given_number(roll, 2) == 0
    assert sum_of_given_number(roll, 3) == 15
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 0
def test_sum_of_given_number_some_different():
    """
    Test sum_of_given_number() with one roll
    where some dice have the same face value.
    """
    roll = [1,1,1,2,6]
    assert sum_of_given_number(roll, 1) == 3
    assert sum_of_given_number(roll, 2) == 2
    assert sum_of_given_number(roll, 3) == 0
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 6

def test_fill_upper_section():
    """
    Test fill_upper_section() with any one roll of your choice.
    """
    roll = [1,2,3,3,3]
    assert fill_upper_section(roll) == (1,2,9,0,0,0)

def test_three_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "3 of a kind".
    """
    roll = [2,2,2,1,4]
    assert num_of_a_kind(roll, 3) == 6


def test_three_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "3 of a kind".
    """
    roll = [2,2,3,1,4]
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "4 of a kind".
    """
    roll = [2,2,2,2,1]
    assert num_of_a_kind(roll, 4) == 8

def test_four_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "4 of a kind".
    """
    roll = [1,2,3,4,5]
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    """
    Tests yahtzee() with a roll that has a yahtzee.
    """
    roll = [5,5,5,5,5]
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    """
    Tests yahtzee() with a roll that has no yahtzee.
    """
    roll = [1,1,2,2,3]
    assert yahtzee(roll) == 0