# test_coindot.py
"""
Tests for CoinDot module.
"""

import unittest
from coindot import CoinDot

class TestCoinDot(unittest.TestCase):
    """Test cases for CoinDot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinDot()
        self.assertIsInstance(instance, CoinDot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinDot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
