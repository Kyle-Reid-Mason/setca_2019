"""
Tests for geom_analysis.py
"""
import pytest
import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2.0

def test_bond_check_false():
    """A test for the bond check function."""
    bond_length = 3
    observed = ga.bond_check(bond_length)
    assert observed == False

def test_bond_check_true():
    bond_length = 1.4
    observed = ga.bond_check(bond_length)
    assert observed == True

def test_bond_check_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)
