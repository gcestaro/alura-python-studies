class A:
    def print(self):
        print("A")


class B(A):
    def print(self):
        print("B")


class C(A):
    def print(self):
        print("C")


class D(B, C):
    pass


class E(C, B):
    pass


class F(C, B):
    def print(self):
        print("F")


if __name__ == '__main__':
    '''
        MRO: Method Resolution Order
        Example: D > B > (#excluded A) > C > A
        Explanation: 
        There is no print in D class, so it passes to the first defined super class (i.e. B). 
        If B didn't have print also, it would go to A (B's super class), but since B and C shares 
        the same class, this is not a 'good head', so passes to C. 
        Finally, if C didn't have a print method overridden, it would use A's print. 
    '''
    a = A()
    a.print()  # A

    b = B()
    b.print()  # B

    c = C()
    c.print()  # C

    d = D()
    d.print()  # B

    e = E()
    e.print()  # C

    f = F()
    f.print()  # F
