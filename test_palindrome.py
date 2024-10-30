import pytest
import time
from typing import Iterable


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Start + {func.__name__}')
        result = func(*args, **kwargs)
        stop = time.time()
        print(f'END + {func.__name__}')
        result_time = stop - start
        print(f'Function execution time: {result_time:.6f} seconds')
        return result
    return wrapper


@count_time
def is_palindrome(word: str) -> bool:
    return word == ''.join(reversed(word))


@pytest.mark.parametrize('word, expected', [
    ('peep', True),
    ('pekep', True),
    ('white', False),
    ('fire', False),
    ('beep', False),
    ('beeb', True),
    ('mono', False),
    ('house', False),
    ('mouse', False),
    ('bwb', True),
])
def test_palindrome1(word, expected):
    assert is_palindrome(word) == expected


def test_palindrome2():
    assert is_palindrome('peep') == True
    assert is_palindrome('pekep') == True
    assert is_palindrome('white') == False
    assert is_palindrome('fire') == False
    assert is_palindrome('beep') == False
    assert is_palindrome('beeb') == True
    assert is_palindrome('mono') == False
    assert is_palindrome('house') == False
    assert is_palindrome('mouse') == False
    assert is_palindrome('bwb') == True


def test_palindrome3():
    assert is_palindrome('peep') == True
    assert is_palindrome('pekep') == True
    assert is_palindrome('white') != True
    assert is_palindrome('fire') != True
    assert is_palindrome('beep') != True
    assert is_palindrome('beeb') == True
    assert is_palindrome('mono') != True
    assert is_palindrome('house') != True
    assert is_palindrome('mouse') != True
    assert is_palindrome('bwb') == True


big_word = "peeppeep"


def is_palindrome_iter(word: Iterable) -> bool:
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


@count_time
def test_is_palindrome_iter():
    assert is_palindrome_iter(big_word) == True



pytest -v test_palindrome.py

answer:

reque/test_palindrome.py::test_palindrome1[peep-True] PASSED                                                                                                                                  [  7%]
reque/test_palindrome.py::test_palindrome1[pekep-True] PASSED                                                                                                                                 [ 15%]
reque/test_palindrome.py::test_palindrome1[white-False] PASSED                                                                                                                                [ 23%]
reque/test_palindrome.py::test_palindrome1[fire-False] PASSED                                                                                                                                 [ 30%]
reque/test_palindrome.py::test_palindrome1[beep-False] PASSED                                                                                                                                 [ 38%]
reque/test_palindrome.py::test_palindrome1[beeb-True] PASSED                                                                                                                                  [ 46%]
reque/test_palindrome.py::test_palindrome1[mono-False] PASSED                                                                                                                                 [ 53%]
reque/test_palindrome.py::test_palindrome1[house-False] PASSED                                                                                                                                [ 61%]
reque/test_palindrome.py::test_palindrome1[mouse-False] PASSED                                                                                                                                [ 69%]
reque/test_palindrome.py::test_palindrome1[bwb-True] PASSED                                                                                                                                   [ 76%]
reque/test_palindrome.py::test_palindrome2 PASSED                                                                                                                                             [ 84%]
reque/test_palindrome.py::test_palindrome3 PASSED                                                                                                                                             [ 92%]
reque/test_palindrome.py::test_is_palindrome_iter PASSED                                                                                                                                      [100%]
