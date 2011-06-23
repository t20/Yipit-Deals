from yipit import YipitDeals
import unittest

class YipitDealsTestCase(unittest.TestCase):
    """YipitDealsTestCase"""
    
    def testNoParams(self):
        y1 = YipitDeals()
        deals = y1.main({})
        self.assertEqual(20, len(deals))
    
    def testLimit(self):
        """Passing limit to API call"""
        y2 = YipitDeals()
        deals = y2.main(["limit=5"])
        self.assertEqual(5, len(deals))
    
    def testInvalidDivision(self):
        """Passing invalid division"""
        y3 = YipitDeals()
        deals = y3.main(["division=newyork2", "tag=restaurants"])
        params = y3.params
        division_found = "division" in params
        self.assertEqual(False, division_found)
    
    def testInvalidLimit(self):
        """docstring for testInvalidLimit"""
        y4 = YipitDeals()
        deals = y4.main(["limit=20A", "division=minneapolis"])
        params = y4.params
        limit_found = "limit" in params
        self.assertEqual(False, limit_found)
    
    def testInvalidTag(self):
        """docstring for testInvalidTag"""
        y5 = YipitDeals()
        deals = y5.main(["limit=5", "division=minneapolis", "tag=10"])
        params = y5.params
        tag_found = "tag" in params
        self.assertEqual(False, tag_found)
    
    def testMultipleDivisions(self):
        """docstring for testMultipleDivisions"""
        y6 = YipitDeals()
        deals = y6.main(["limit=5", "division=minneapolis,new-york", "tag=10"])
        params = y6.params
        division_found = "division" in params
        self.assertEqual(True, division_found)
    
    def testPaid1(self):
        """paid tag takes bool or bit representation"""
        y7 = YipitDeals()
        deals = y7.main(["limit=5", "paid=1"])
        params = y7.params
        paid_found = "paid" in params
        self.assertEqual(True, paid_found)
    
    def testPaidTrue(self):
        """pass true for paid param"""
        y8 = YipitDeals()
        deals = y8.main(["limit=5", "paid=True"])
        params = y8.params
        paid_found = "paid" in params
        self.assertEqual(True, paid_found)

if __name__ == '__main__':
    unittest.main()   