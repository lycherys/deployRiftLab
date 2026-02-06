# test_deployrift.py
"""
Tests for deployRift module.
"""

import unittest
from deployrift import deployRift

class TestdeployRift(unittest.TestCase):
    """Test cases for deployRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = deployRift()
        self.assertIsInstance(instance, deployRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = deployRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
