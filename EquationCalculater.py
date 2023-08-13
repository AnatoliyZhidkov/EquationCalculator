import math
import re


class Convertor:

    def normalization_equation_form(self,equation):
        equation = equation.replace(" ",'').replace("i",'j')
        equation = re.sub(r'[qwertyuopasdfghklzxcvbnm]','x',equation)
        return equation
    
    def convert_To_Comlpex(self,number):

        if number =='+j' or number == 'j':
            number = complex(0,1)
        elif number =='-j':
            number = complex(0,-1)
        else:
            if '-(' in number:      # -(5 + 2i)
                number = -complex(number[2:len(number)-1])  
            elif '+(' in number: number = complex(number[2:len(number)-1])
            elif '(' in number: number = complex(number[1:len(number)-1])
            else: number = complex(number)

        return number
    
    def convert_Str_To_Num(self,number):
        if  number == '+':  number = 1
        elif number == '-': number = -1
        else:
            try:
                number = int(number)
            except ValueError:
                try: number = self.convert_To_Comlpex(number)
                except ValueError:
                    print('Incorrect equation')
                    quit()
        return number




class Coefficients(Convertor):
    
    

    def calculate_coeff(self,equation):
        equation = self.normalization_equation_form(equation)

        coeff_A = re.search(r'(?<!x\^2).+?(?=x\^2)(?!i|j)',equation)
        if coeff_A == None: coeff_A = 1
        else: coeff_A = self.convert_Str_To_Num(coeff_A[0])

        coeff_B = re.search(r'(?<=x\^2).+?(?=x)(?!i|j)',equation)
        if coeff_B == None: coeff_B = 0
        else: coeff_B = self.convert_Str_To_Num(coeff_B[0])

        if equation.count('x') == 2:
            if equation[equation.rfind('x')+1:equation.find('=')] =='': coeff_C = 0
            else: coeff_C = self.convert_Str_To_Num(equation[equation.rfind('x')+1:equation.find('=')])
        else:
            coeff_C = re.search(r'(?<=x\^2).+?(?==)',equation)
            if coeff_C == None: coeff_C = 0
            else: coeff_C = self.convert_Str_To_Num(coeff_C[0])
        
        coeffs = [coeff_A, coeff_B , coeff_C]
        
        return coeffs


class Equation(Coefficients):

    def __init__(self,equation):                                                                            #   Изучить       '-> None:'
        super().__init__()
        self.equation = equation
        self.__coeff_A = Coefficients().calculate_coeff(equation)[0]
        self.__coeff_B = Coefficients().calculate_coeff(equation)[1]
        self.__coeff_C = Coefficients().calculate_coeff(equation)[2]
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
            else:
                print('hz')
        elif Discriminant > 0:
            Discriminant = math.sqrt(Discriminant)
            x1 = (-equation_cl.coeff_B + Discriminant)/(2*equation_cl.coeff_A)
            x2 = (-equation_cl.coeff_B - Discriminant)/(2*equation_cl.coeff_A)
            print(f'Ответ: x1 = {x1}  x2 = {x2}')
        elif Discriminant == 0:
            x1 = -equation_cl.coeff_B /(2*equation_cl.coeff_A)
            print(f'Ответ: x1 = {x1}')
        else:
            Discriminant = complex(0,math.sqrt(Discriminant * -1))
            x1 = (-equation_cl.coeff_B + Discriminant)/(2*equation_cl.coeff_A)
            x2 = (-equation_cl.coeff_B - Discriminant)/(2*equation_cl.coeff_A)
            print(f'Ответ: x1 = {x1}  x2 = {x2}')


'''equation = input('Введите квадратное уравнение: ')'''
equation = 'x^2 + (3+2i)x - 5 + 3i = 0'.replace(" ",'')

calculator = Calculater()
ans = calculator.calculate_Quadratic_Equation(equation)


'x^2 + (3+2i)x - 5 + 3i = 0'
'x^2 - 6x + 34 = 0'