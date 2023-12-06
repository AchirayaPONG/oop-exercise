
"""
This script tests your slimebox assignment for code quality.

01219114 Computer Programming
Week 9, Long Program Assignment: Slime Box (testing module)
(C) 2022 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

# DO NOT MODIFY

import sys
import os
import filecmp
from contextlib import contextmanager
import pytest
from pylint.lint import Run as run_pylint
from slimebox import Slime, Color, clamp, mix_colors
import sim

# reference: http://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

score = 0

def test_pep8():

    with suppress_stdout():
        pylint_results = run_pylint(['slimebox.py', '--good-names=i,j,k,x,y,z,ex,Run,_,r,g,b'], exit = False)
        pylint_score = min(pylint_results.linter.stats.global_note, 9)

    assert pylint_score == 9

def test_clamp():

    assert clamp(10, 0, 100) == 10
    assert clamp(1891728931892, 0, 100) == 100
    assert clamp(-12378184912, 0, 100) == 0
    with pytest.raises(ValueError):
        clamp(0, 9999, 0)

def test_color():

    c = Color(10000, -9999, 10000)
    assert c.r == 255
    assert c.g == 0
    assert c.b == 255

def test_color_equality():
    c = Color(10000, -9999, 10000)
    c2 = Color(255, 0, 255)
    assert c == c2

def test_color_setter():
    c2 = Color(255, 0, 255)
    c2.g = 999
    assert c2 == Color(255, 255, 255)

def test_mix_colors():

    c1 = Color(0, 0, 0)
    c2 = Color(100, 100, 100)

    assert mix_colors(c1, c2, 1, 1) == Color(50, 50, 50)
    assert mix_colors(c1, c2, 9, 1) == Color(10, 10, 10)
    assert mix_colors(c1, c2, 0.9, 0.1) == Color(10, 10, 10)

def test_slime_init():
    s = Slime(100, 1000, Color(0, 10, 20))
    assert isinstance(s, Slime)

def test_slime_getters():
    s = Slime(100, 1000, Color(0, 10, 20))
    assert s.mass == 100
    assert s.volume == 1000
    assert s.color == Color(0, 10, 20)

def test_slime_eat():
    s = Slime(1000, 1000)
    s.eat(1000, "L")
    assert s.mass == 1900
    assert s.volume == 1900
    s.eat(100, "S")
    assert s.mass == 1940
    assert s.volume == 1900

def test_slime_equality():
    assert Slime(100, 100, Color(255, 255, 255)) == Slime(100, 100)

def test_slime_split():
    s = Slime(256, 128)
    new_slimes = s.split(2)
    assert len(new_slimes) == 2
    assert new_slimes[0] == Slime(128, 64)
    assert new_slimes[1] == Slime(128, 64)

    s = Slime(100, 100)
    new_slimes = s.split(1)
    assert len(new_slimes) == 1
    assert new_slimes[0] == Slime(100, 100)

    with pytest.raises(ValueError):
        s = Slime(100, 100)
        new_slimes = s.split(0)

def test_slime_combine():
    slime1 = Slime(50, 20, Color(0, 20, 0))
    slime2 = Slime(50, 10, Color(10, 0, 10))
    assert slime1 + slime2 == Slime(100, 30, Color(5, 10, 5))
    slime3 = Slime(1, 1, Color(0, 0, 0))
    slime4 = Slime(9, 1, Color(100, 100, 100))
    assert slime3 + slime4 == Slime(10, 2, Color(90, 90, 90))

def test_privacy():
    c = Color()
    s = Slime()
    assert all([key.startswith('_') for key in (vars(c) | vars(s)).keys()])

def test_case1(capsys):
    sim.main('case1.input')
    captured = capsys.readouterr()
    with open('case1.output') as f:
        expected_output = f.read().strip()

    assert captured.out.strip() == expected_output

