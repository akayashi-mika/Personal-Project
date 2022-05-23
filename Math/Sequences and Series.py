import math
import numpy

choice  =   int(input("""\n[1] Arithmetic Series
[2] Geometric Series
> """))

def ArithmeticSeries():
    firstTerm   =   int and float(input("First Term = "))
    d   =   int and float(input("d = "))
    p   =   int and float(input("p = "))
    q   =   int and float(input("q = "))

    pthTerm =   (d * p) + (d - firstTerm)
    qthTerm =   (d * q) + (d - firstTerm)
    mean    =   (pthTerm + qthTerm) / 2

    print(f"Mean = {mean}")

def GeometricSeries():
    firstTerm   =   int and float(input("First Term = "))
    ratio   =   int and float(input("r = "))
    k   =   int and float(input("k = "))
    m   =   int and float(input("m = "))

    kthTerm =   firstTerm * (ratio ** (k - 1))
    mthTerm =   firstTerm * (ratio ** (m - 1))
    mean    =   (kthTerm + mthTerm) / 2

    print(f"Mean = {mean}")

def SeriesChoice():
    if choice == 1:
        return ArithmeticSeries()

    if choice == 2:
        return GeometricSeries()
SeriesChoice()