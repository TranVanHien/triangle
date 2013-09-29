'''
Created on Sep 23, 2013

@author: Tran Van Hien
'''
import decimal
def detect_triangle(a,b,c):
    end =  2**32 - 1
    if (type(a) in [float, int, long] and type(b) in [float, int, long] and type(c) in [float, int, long] and (a > 0 and a <= end ) and (b > 0 and b <= end ) and (c > 0 and c <= end ) ):
        
            if decimal.Decimal(a)+ decimal.Decimal(b) > decimal.Decimal(c) and decimal.Decimal(b)+decimal.Decimal(c)>decimal.Decimal(a) and decimal.Decimal(c)+decimal.Decimal(a)>decimal.Decimal(b) :
                if (abs(a*a + b*b - c*c) < 10**-9) or (abs(c*c + b*b - a*a) < 10**-9) or (abs(a*a + c*c - b*b) < 10**-9):
                        if a==b or b==c or c==a:
                            return "Tam giac vuong can"
                        else:
                            return "Tam giac vuong"
                else:
                    if a==b and b == c:
                        return "Tam giac deu"
                    elif a==b or b==c or c==a:
                        return "Tam giac can"
                    else:
                        return "Tam giac thuong"
            else:
                return "Tam giac khong hop le"
    
    else:
        return "Input invalid"

#end
       




                 
                     
