"""
1. D(p) = p7 + 5p6 +7p3 + p + 1;
2. D(p) = p8 + 3p6 +8 p3 + 2p + 1;
3. D(p) = p10 + 7p8 + 11p7 +5p + 1;
4. D(p) = p77 + p55 + p4 + p + 3; 
5. D(p) = p99 + p88 + p77 + p5 + p + 4; 
6. D(p) = p101 + p99 + p88 + p77 + p4 + p + 5; 
7. D(p) = 3p6 + p4 + 2p3 + 2; 
8. D(p) = p5 + 4p3 + p2 + 2p + 3; 
9. D(p) = 2p5 + 5p4 + 2p3 + p2 + 12p + 1; 
10. D(p) = 17p5 + 4p3 + 5p2 + 21p + 13; 
11. D(p) = 7p5 + 5p3 + 7p2 + 2p + 3; 
12. D(p) = 11p7 + p3 + 15p2 + 6p + 4; 
13. D(p) = 17p5 + 4p3 + 5p2 + 21p + 13; 
14. D(p) = 3p6 + 3p5 + 4p3 + 3p + 3;

"""

def d1(p):
    return p7 + 5*p**6 +7*p**3 + p + 1 

def d2(p):
    return p**8 + 3*p**6 +8*p**3 + 2*p + 1

def d3(p):
    return p**10 + 7*p**8 + 11*p**7 +5**p + 1

def d4(p):
    return p**77 + p**55 + p**4 + p + 3

def d5(p):
    return p**99 + p**88 + p**77 + p*5 + p + 4

def d6(p):
    return p**101 + p**99 + p**88 + p**77 + p**4 + p + 5

def d7(p):
    return 3*p**6 + p**4 + 2*p**3 + 2

def d8(p):
    return p**5 + 4*p**3 + p**2 + 2*p + 3

def d9(p):
    return 2*p**5 + 5*p**4 + 2*p**3 + p**2 + 12*p + 1

def d10(p):
    return 7*p**5 + 5*p**3 + 7*p**2 + 2*p + 3

def d11(p):
    return 7*p**5 + 5*p**3 + 7*p**2 + 2*p + 3

def d12(p):
    return 11*p**7 + p**3 + 15*p**2 + 6*p + 4

def d13(p):
    return 17*p**5 + 4*p**3 + 5*p**2 + 21*p + 13

def d14(p):
    return 3*p**6 + 3*p**5 + 4*p**3 + 3*p + 3
