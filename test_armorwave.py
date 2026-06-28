# test_armorwave.py
"""
Tests for ArmorWave module.
"""

import unittest
from armorwave import ArmorWave

class TestArmorWave(unittest.TestCase):
    """Test cases for ArmorWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArmorWave()
        self.assertIsInstance(instance, ArmorWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArmorWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
