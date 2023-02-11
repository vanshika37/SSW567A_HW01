import unittest

def classify_triangles(a,b,c):
	if a==b and b==c :
		return 'Equilateral'
	elif a==b or b==c or a==c:
		return 'Isoceles'
	elif (a*a + b*b == c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
		return 'Right'
	else:
		return 'Scalene'

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangles(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangles(2,2,2),'Equilateral','2,2,2 should be equilateral')
        self.assertEqual(classify_triangles(10,10,11),'Isoceles','10,10,11 should be equilateral')
        self.assertEqual(classify_triangles(1,5,3),'Scalene','1,5,3 should be Scalene')
        self.assertEqual(classify_triangles(2,4,35),'Scalene','2,4,35 should be Scalene')
        self.assertEqual(classify_triangles(10,1,10),'Isoceles','10,1,10 should be Isoceles')
        self.assertEqual(classify_triangles(5,7,10),'Scalene','5,7,10 is a Right triangle')
        
   # def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classify_triangles(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangles(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classify_triangles(10,15,30),'Scalene','10,15,10 should be Scalene')
        self.assertNotEqual(classify_triangles(11,11,11),'Isoceles','Should be Equilateral')
        self.assertNotEqual(classify_triangles(111,11,11),'Equilateral','Should be Isoceles')


if __name__=="__main__":
    aa = "enter length a"
    a=int(input(aa))
    bb = "enter length b"
    b=int(input(bb))
    cc = "enter length c"
    c=int(input(cc))

    ans = classify_triangles(a,b,c)
    if(ans == 'Equilateral'):
    	print("Equilateral")
    elif (ans== 'Isoceles'):
    	print("isoseles")
    elif(ans =='Scalene'):
    	print("scalene")
    elif (ans=='Right'):
    	print("right triangle")

unittest.main(exit=True) 



