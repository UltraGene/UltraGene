import unittest
import sys

sys.path.append('..')

from ultragene.snp_processor import validate_and_load__data  


class TestSNPProcessor(unittest.TestCase):
    
    def test_smoke_valid_input(self):
        pass

    def test_one_shot_invalid_allele(self):
       pass

    def test_one_shot_empty_file(self):
       pass

    def test_edge_all_invalid_data(self):
        pass

if __name__ == '__main__':
    unittest.main()
