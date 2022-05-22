# Solve for equations
# Linear, Quadratic
import math

def Equation():
    print('''Equations:
    1 - Linear
    2 - Quadratic''')

    Equation = int(input('Equation: '))

    if Equation == 1:

        def Linear():

            form = int(input('''[1] Slope-Intercept Form 
[2] General Form
> '''))

            if form == 1:
                
                def Slope_Intercept_Form():
                    print('\n'+'y = mx + b')
                    m = int and float(input('m = '))
                    b = int and float(input('b = '))
        
                    slope = m
                    x_intercept = -(b/m)
                    y_intercept = b
        
                    print(f'''\nslope = {slope}
    x-intercept = ({x_intercept}, 0)
    y-intercept = (0, {y_intercept})''')

                Slope_Intercept_Form()


            if form == 2:

                def General_Form():
                    print('\nAx + By = C')
                    A = int and float(input('A = '))
                    B = int and float(input('B = '))
                    C = int and float(input('C = '))

                    slope = - (A / B)
                    x_intercept = C / A
                    y_intercept = C / B

                    print(f'''\nslope = {slope}
x-intercept = {x_intercept}
y-intercept = {y_intercept}''')

                General_Form()

        Linear()



    if Equation == 2:

        def Quadratic():
            print('\n'+'f(x) = ax\u00b2 + bx + c')
            a = int and float(input('a = '))
            b = int and float(input('b = '))
            c = int and float(input('c = '))

            D = math.pow(b, 2) - (4 * a * c)

            def Discriminant():

                print('\nDiscrimants:')
                print(f'D = {D}')

                if D > 0:
                    if math.sqrt(D) == math.floor(math.sqrt(D)):
                        print('2 real rational unequal roots')
                    else:
                        print('2 real irrational unequal roots')

                if D == 0:
                    print('1 real rational root')

                if D < 0:
                    print('0 real roots / 2 imaginary roots')

            Discriminant()

            def Roots():

                aa = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                bb = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                sum = aa + bb
                product = aa * bb

                print('\nRoots:')
                if D == 0:
                    print(f'x = {aa}')
                    print(f'sum = {aa}')
                    print(f'product = {aa}')

                else:

                    if D > 0:
                        if math.sqrt(D) == math.floor(math.sqrt(D)):
                            print(f'x = {aa}, {bb}')
                            print(f'sum = {sum}')
                            print(f'product = {product}')

                        else:
                            print(f'x = {aa}, {bb}')
                            print(f'sum = {sum}')
                            print(f'product = {product}')

                    if D < 0:
                        print(f'x = {aa}, {bb}')
                        print(f'sum = {sum}')
                        print(f'product = {product}')

            Roots()

        Quadratic()
        
        
    else:
        print('choose numbers 1-2 only')

Equation()
