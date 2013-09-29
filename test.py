'''
Created on Sep 23, 2013

@author: Tran Van Hien
'''
import unittest
import math
from triangle import detect_triangle

class Test(unittest.TestCase):


    def testTRiangle1(self):
        self.assertEqual(detect_triangle(3, 4, 5), "Tam giac vuong")
    def testTRiangle2(self):
        self.assertEqual(detect_triangle(3, 5, 4), "Tam giac vuong")
    def testTRiangle3(self):
        self.assertEqual(detect_triangle(5, 4, 3), "Tam giac vuong")
        
    def testTRiangle4(self):
        self.assertEqual(detect_triangle(1, 1, math.sqrt(2)), "Tam giac vuong can")
    def testTRiangle5(self):
        self.assertEqual(detect_triangle(1,math.sqrt(2),1), "Tam giac vuong can")
    def testTRiangle6(self):
        self.assertEqual(detect_triangle( math.sqrt(2), 1, 1), "Tam giac vuong can") 
     
    def testTRiangle7(self):
        self.assertEqual(detect_triangle(3,4,4), "Tam giac can") 
    def testTRiangle8(self):
        self.assertEqual(detect_triangle(4, 4, 3), "Tam giac can")
    def testTRiangle9(self):
        self.assertEqual(detect_triangle(4, 3, 4), "Tam giac can")
   
    def testTRiangle10(self):
        self.assertEqual(detect_triangle(4, 4, 4), "Tam giac deu")
    
    def testTRiangle11(self):
        self.assertEqual(detect_triangle(3,5 ,7 ), "Tam giac thuong")
    def testTRiangle12(self):
        self.assertEqual(detect_triangle(3,7 ,5 ), "Tam giac thuong")
    def testTRiangle13(self):
        self.assertEqual(detect_triangle(7,5 ,3 ), "Tam giac thuong")
        
    def testTRiangle14(self):
        self.assertEqual(detect_triangle(1, 2, 3), "Tam giac khong hop le")
    def testTRiangle15(self):
        self.assertEqual(detect_triangle(3, 2, 1), "Tam giac khong hop le")
    def testTRiangle16(self):
        self.assertEqual(detect_triangle(1, 3, 2), "Tam giac khong hop le") 
    
    def testTRiangle18(self):
        self.assertEqual(detect_triangle(-3, 4, 5), "Input invalid")
    def testTRiangle19(self):
        self.assertEqual(detect_triangle(3, -4, 5), "Input invalid")
    def testTRiangle20(self):
        self.assertEqual(detect_triangle(3, 4, -5), "Input invalid")
    def testTRiangle21(self):
        self.assertEqual(detect_triangle(-3, -4, 5), "Input invalid")
    def testTRiangle22(self):
        self.assertEqual(detect_triangle(-3, 4, -5), "Input invalid")
    def testTRiangle23(self):
        self.assertEqual(detect_triangle(3, -4, -5), "Input invalid")
    def testTRiangle24(self):
        self.assertEqual(detect_triangle(-1, -4, -5), "Input invalid")
   
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTRiangle']
    unittest.main()
