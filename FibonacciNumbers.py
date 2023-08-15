import sys
sys.set_int_max_str_digits(0)
class FibMatrix():
    Q = [[1,1],[1,0]]
    def __init__(self):
        self.__memory = {}

    def __matrix_multiply(self,M1,M2):
        a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
        a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
        a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
        a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
        return [[a11,a12],[a21,a22]]

    def __matrix_pow(self,M,n):

        if n == 1:
            return M
        if n in self.__memory: return self.__memory[n]
        if n%2 == 1:
            A = self.__matrix_multiply(self.__matrix_pow(M,n-1), M)
            return A
        A = self.__matrix_pow(M,n/2)
        R = self.__matrix_multiply(A,A)
        self.__memory[n] = R
        return R
        
    def get_fib_number(self,n):
        if n == 0 : return 0
        if n == 1 : return 1
        return self.__matrix_pow(FibMatrix().Q, n)[0][1]




a = FibMatrix()
print(a.get_fib_number(1000000))