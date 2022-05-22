import math


som = input('\nsign of measure: ')

def Area():

    def Area_Square():
        s = int and float(input('\ns = '))
        Area = math.pow(s, 2)
        print(f'Area = {Area}{som}\u00b2')

    def Area_Rectangle():
        L = int and float(input('\nL = '))
        W = int and float(input('W = '))
        Area = L * W
        print(f'Area = {Area}{som}\u00b2')

    def Area_Circle():
        r = int and float(input('\nr = '))

        def Area_Circle_div_7():
            Area = 22/7 * math.pow(r, 2)
            print(f'Area = {Area}{som}\u00b2')

        def Area_Circle_not_div_7():
            Area = 3.14 * math.pow(r, 2)
            print(f'Area = {Area}{som}\u00b2')

        if r % 7 == 0:
            return Area_Circle_div_7()
            
        else:
            return Area_Circle_not_div_7()
            
    def Area_Trapezoid():
        b1 = int and float(input('\nb\N{subscript one} = '))
        b2 = int and float(input('b\N{subscript two} = '))
        h = int and float(input('h = '))
        Area = ((b1 + b2) * h) / 2
        print(f'Area = {Area}{som}\u00b2')

    def Area_Rhombus():
        var = int(input('''\n[1] Side x Diagonal 
[2] Diagonal x Diagonal
> '''))

        def Area_Rhombus_Side_Diagonal():
            a = int and float(input('\na = '))
            p = int and float(input('p = '))
            Area = p * math.sqrt(4 * math.pow(a, 2) - math.pow(p, 2)) / 2
            print(f'Area = {Area}{som}\u00b2')

        def Area_Rhombus_Diagonal_Diagonal():
            p = int and float(input('\np = '))
            q = int and float(input('q = '))
            Area = p * q / 2
            print(f'Area = {Area}{som}\u00b2')

        if var == 1:
            return Area_Rhombus_Side_Diagonal()

        if var == 2:
            return Area_Rhombus_Diagonal_Diagonal()

    def Area_Right_Triangle():
        l1 = int and float(input('\nl\N{subscript one} = '))
        l2 = int and float(input('l\N{subscript two} = '))
        Area = (l1 * l2) / 2
        print(f'Area = {Area}{som}\u00b2')

    def Area_Isosceles_Triangle():
        s = int and float(input('\ns = '))
        b = int and float(input('b = '))
        h = math.sqrt(math.pow(s, 2) - (math.pow(b, 2) / 4))
        Area = (b * h) / 2
        print(f'Area = {Area}{som}\u00b2')

    def Area_Equilateral_Triangle():
        s = int and float(input('\ns = '))
        Area = (math.sqrt(3) / 4) * math.pow(s, 2)
        print(f'Area = {Area}{som}\u00b2')

    shape = int(input('''\nShapes:
[1] Square
[2] Rectangle
[3] Circle
[4] Trapezoid
[5] Rhombus
[6] Right Triangle
[7] Isosceles Triangle
[8] Equilateral triangle
> '''))

    if shape == 1:
        return Area_Square()

    if shape == 2:
        return Area_Rectangle()

    if shape == 3:
        return Area_Circle()
    
    if shape == 4:
        return Area_Trapezoid()

    if shape == 5:
        return Area_Rhombus()

    if shape == 6:
        return Area_Right_Triangle()

    if shape == 7:
        return Area_Isosceles_Triangle()

    if shape == 8:
        return Area_Equilateral_Triangle()


def Perimeter():

    # def Perimeter_Square():

    # def Perimeter_Rectangle():

    # def Circumference_Circle():

    # def Perimeter_Trapezoid():

    # def Perimeter_Rhombus():

    shape = int(input('''\nShapes:
[1] Square
[2] Rectangle
[3] Circle
[4] Trapezoid
[5] Rhombus
> '''))

    # if shape == 1:
    #     return Perimeter_Square()

    # if shape == 2:
    #     return Perimeter_Rectangle()

    # if shape == 3:
    #     return Circumference_Circle()

    # if shape == 4:
    #     return Perimeter_Trapezoid()

    # if shape == 5:
    #     return Perimeter_Rhombus()


def Surface_Area():





    shape = int(input('''\nShapes:
[1] Cube
[2] Rectangular Prism
[3] Cone
[4] Pyramid
[5] Cylinder
[6] Sphere
> '''))


def Volume():


    shape = int(input('''\nShapes:
[1] Cube
[2] Rectangular Prism
[3] Cone
[4] Pyramid
[5] Cylinder
[6] Sphere
> '''))


def Geometry():

    operation = int(input('''\nOperations:    
[1] Area
[2] Perimeter
[3] Surface_Area
[4] Volume
> '''))
 
    if operation == 1:
        return Area()
    
    if operation == 2:
        return Perimeter()

    if operation == 3:
        return Surface_Area()
    
    if operation == 4:
        return Volume()

Geometry()