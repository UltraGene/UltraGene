import unittest
import sys 

sys.path.append('..')


from ultragene.snp_gene_mapper import is_valid_snp_id, make_api_request, fetch_gene_name


class TestSNPGeneMapper(unittest.TestCase):
    def test_is_valid_snp_id(self):
        self.assertTrue(is_valid_snp_id("rs123456"))
        self.assertFalse(is_valid_snp_id("123456"))
        self.assertFalse(is_valid_snp_id("rs123abc"))

    def test_make_api_request(self):
        # mock the requests.get call here to avoid making actual API calls
        pass

    def test_fetch_gene_name(self):
        # mock the is_valid_snp_id and make_api_request calls here
        pass

if __name__ == '__main__':
    unittest.main()