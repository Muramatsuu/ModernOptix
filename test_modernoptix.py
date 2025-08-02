# test_modernoptix.py
"""
Tests for ModernOptix module.
"""

import unittest
from modernoptix import ModernOptix

class TestModernOptix(unittest.TestCase):
    """Test cases for ModernOptix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModernOptix()
        self.assertIsInstance(instance, ModernOptix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModernOptix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
