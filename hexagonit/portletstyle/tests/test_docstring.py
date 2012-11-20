# -*- coding: utf-8 -*-
"""Boilerplate for unit tests in method docstrings."""

import unittest
import doctest


def test_suite():
    import hexagonit.portletstyle

    return unittest.TestSuite([doctest.DocTestSuite(hexagonit.portletstyle)])
