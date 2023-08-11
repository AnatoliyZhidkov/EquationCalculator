import math
import re


class Convertor:

    def convert_To_Comlpex(self,number):

        if number =='+i' or number == 'i':
            number = complex(0,1)
        elif number =='-i':
            number = complex(0,-1)
        else:
            regularComplex = r'(((?<!\^)(?:\+|-)?\d+(?:\.\d+)?(?=\+|-))?((?:\+|-)\d+(?:\.\d+)?(?=i)))'
            number = re.findall(regularComplex,number)
            if number[0][1]=='':
                number = complex(0,int(number[0][2]))
            else:
                number = complex(int(number[0][1]),int(number[0][2]))
        return number
    
    def convert_Str_To_Num(self,number):
        if number == '' or number == '+':
            number = 1
        elif number == '-':
            number = -1
        else:
            try:
                number = int(number)
            except ValueError:
                number = self.convert_To_Comlpex(number)
        return number


class Coefficients(Convertor):

    def calc_coeff_A(self,equation) : return self.convert_Str_To_Num(equation[:equation.find('x')])
    def calc_coeff_B(self,equation) : return self.convert_Str_To_Num(equation[equation.find('x')+3:equation.rfind('x')])
    def calc_coeff_C(self,equation) : return self.convert_Str_To_Num(equation[equation.rfind('x')+1:equation.find('=')])

class Equation(Coefficients):

    def __init__(self,equation):                                                                            #   Изучить       '-> None:'
        super().__init__()
        self.equation = equation
        self.__coeff_A = Coefficients().calc_coeff_A(equation)
        self.__coeff_B = Coefficients().calc_coeff_B(equation)
        self.__coeff_C = Coefficients().calc_coeff_C(equation)
    def __str__(self) -> str:
        return f"Уравнение:\n {self.equation} \n {self.__coeff_A}  {self.__coeff_B}  {self.__coeff_C}"
    @property
    def coeff_A(self):
        return self.__coeff_A
    @property
    def coeff_B(self):
        return self.__coeff_B
    @property
    def coeff_C(self):
        return self.__coeff_C
    
    def calcul_Disc(self): return self.coeff_B**2 - 4*self.coeff_A*self.coeff_C
        
        

class Calculater():

    def calculate_Quadratic_Equation(self,equation):
        equation_cl = Equation(equation)
        Discriminant = equation_cl.calcul_Disc()
        if isinstance(Discriminant,complex):
            if Discriminant.imag == 0:
                x1 = (-equation_cl.coeff_B + math.sqrt(Discriminant.real))/(2*equation_cl.coeff_A)
                x2 = (-equation_cl.coeff_B - math.sqrt(Discriminant.real))/(2*equation_cl.coeff_A)
                print(f'Ответ: x1 = {x1}  x2 = {x2}')
        elif Discriminant > 0:
            x1 = (-equation_cl.coeff_B + math.sqrt(Discriminant))/(2*equation_cl.coeff_A)
            x2 = (-equation_cl.coeff_B - math.sqrt(Discriminant))/(2*equation_cl.coeff_A)
            print(f'Ответ: x1 = {x1}  x2 = {x2}')
        elif Discriminant == 0:
            x1 = -equation_cl.coeff_B /(2*equation_cl.coeff_A)
            print(f'Ответ: x1 = {x1}')
        else:
            print('Корней нет')


'''equation = input('Введите квадратное уравнение: ')'''
equation = 'x^2 + (3+2i)x - 5 + 3i = 0'.replace(" ",'')

calculator = Calculater()
ans = calculator.calculate_Quadratic_Equation(equation)


