print(" ")
print("Asegurate de que hay el mismo número de incognitas que de ecuaciones")
print(" ")
numero_ecuaciones = int(input("Escribe el numero de incognitas que tiene tu sistema(de 2 a 4): "))
print(" ")


def dos_ecuaciones(a1, a2, b1, b2, c1, c2):
    determinante_principal = a1 * b2 - a2 * b1
    determinante_x = c1 * b2 - c2 * b1
    determinante_y = c2 * a1 - c1 * a2

    if determinante_principal != 0:
        x = determinante_x / determinante_principal
        y = determinante_y / determinante_principal
       
        print("x = ", x)
        print("y = ", y)
        print("(Sistema compatible determinado)")

    elif determinante_x == 0 and determinante_y == 0:
        print("El sistema tiene infinitas soluciones (Sistema compatible indeterminado)")

    elif determinante_x != 0 and determinante_y != 0:
        print("El sistema no tiene solucion (Sistema incompatible)")

def tres_ecuaciones(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
    determinante_principal = (a1 * b2 * c3) + (b1 * c2 * a3) + (c1 * a2 * b3) - (b1 * a2 * c3) - (a1 * c2 * b3) - (c1 * b2 * a3)
    determinante_x = (d1 * b2 * c3) + (b1 * c2 * d3) + (c1 * d2 * b3) - (b1 * d2 * c3) - (d1 * c2 * b3) - (c1 * b2 * d3)
    determinante_y = (a1 * d2 * c3) + (d1 * c2 * a3) + (c1 * a2 * d3) - (d1 * a2 * c3) - (a1 * c2 * d3) - (c1 * d2 * a3)
    determinante_z = (a1 * b2 * d3) + (b1 * d2 * a3) + (d1 * a2 * b3) - (b1 * a2 * d3) - (a1 * d2 * b3) - (d1 * b2 * a3)

    print ("determinante pricipal = ", determinante_principal)

    if determinante_principal != 0:
        x = determinante_x / determinante_principal
        y = determinante_y / determinante_principal
        z = determinante_z / determinante_principal

        print("x = ", x)
        print("y = ", y)
        print("z = ", z)
        print("(Sistema compatible determinado)")
    
    elif determinante_x == 0 and determinante_y == 0 and determinante_z == 0:
        print("El sistema tiene infinitas soluciones (Sistema compatible indeterminado)")
    
    elif determinante_x != 0 and determinante_y != 0 and determinante_z != 0:
        print("EL sistema no tiene solucion (Sistema incompatible)")

def cuatro_ecuaciones(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4):
    determinante_principal = a1*(b2*(c3*d4 - d3*c4) - c2*(b3*d4 - d3*b4) + d2*(b3*c4 - c3*b4)) - b1*(a2*(c3*d4 - d3*c4) - c2*(a3*d4 - d3*a4) + d2*(a3*c4 - c3*a4)) + c1*(a2*(b3*d4 - d3*b4) - b2*(a3*d4 - d3*a4) + d2*(a3*b4 - b3*a4)) - d1*(a2*(b3*c4 - c3*b4) - b2*(a3*c4 - c3*a4) + c2*(a3*b4 - b3*a4))
    determinante_x = e1*(b2*(c3*d4 - d3*c4) - c2*(b3*d4 - d3*b4) + d2*(b3*c4 - c3*b4)) - b1*(e2*(c3*d4 - d3*c4) - c2*(e3*d4 - d3*e4) + d2*(e3*c4 - c3*e4)) + c1*(e2*(b3*d4 - d3*b4) - b2*(e3*d4 - d3*e4) + d2*(e3*b4 - b3*e4)) - d1*(e2*(b3*c4 - c3*b4) - b2*(e3*c4 - c3*e4) + c2*(e3*b4 - b3*e4))
    determinante_y = a1*(e2*(c3*d4 - d3*c4) - c2*(e3*d4 - d3*e4) + d2*(e3*c4 - c3*e4)) - e1*(a2*(c3*d4 - d3*c4) - c2*(a3*d4 - d3*a4) + d2*(a3*c4 - c3*a4)) + c1*(a2*(e3*d4 - d3*e4) - e2*(a3*d4 - d3*a4) + d2*(a3*e4 - e3*a4)) - d1*(a2*(e3*c4 - c3*e4) - e2*(a3*c4 - c3*a4) + c2*(a3*e4 - e3*a4))
    determinante_z = a1*(b2*(e3*d4 - d3*e4) - e2*(b3*d4 - d3*b4) + d2*(b3*e4 - e3*b4)) - b1*(a2*(e3*d4 - d3*e4) - e2*(a3*d4 - d3*a4) + d2*(a3*e4 - e3*a4)) + e1*(a2*(b3*d4 - d3*b4) - b2*(a3*d4 - d3*a4) + d2*(a3*b4 - b3*a4)) - d1*(a2*(b3*e4 - e3*b4) - b2*(a3*e4 - e3*a4) + e2*(a3*b4 - b3*a4))
    determinante_w = a1*(b2*(c3*e4 - e3*c4) - c2*(b3*e4 - e3*b4) + e2*(b3*c4 - c3*b4)) - b1*(a2*(c3*e4 - e3*c4) - c2*(a3*e4 - e3*a4) + e2*(a3*c4 - c3*a4)) + c1*(a2*(b3*e4 - e3*b4) - b2*(a3*e4 - e3*a4) + e2*(a3*b4 - b3*a4)) - e1*(a2*(b3*c4 - c3*b4) - b2*(a3*c4 - c3*a4) + c2*(a3*b4 - b3*a4))

    print("determinante principal = ", determinante_principal)

    if determinante_principal != 0:
        x = determinante_x / determinante_principal
        y = determinante_y / determinante_principal
        z = determinante_z / determinante_principal
        w = determinante_w / determinante_principal

        print("x = ", x)
        print("y = ", y)
        print("z = ", z)
        print("w = ", w)
        print("(Sistema compatible determinado)")
    
    elif determinante_x == 0 and determinante_y == 0 and determinante_z == 0 and determinante_w == 0:
        print("El sistema tiene infinitas soluciones (Sistema compatible indeterminado)")
    
    elif determinante_x != 0 or determinante_y != 0 or determinante_z != 0 or determinante_w != 0:
        print("EL sistema no tiene solucion (Sistema incompatible)")



if numero_ecuaciones == 2:
    print("Recuerda que las ecuaciones tienen que estar en la forma ax + by = c")
    print(" ")

    print("Escribe los coeficientes de las incognitas de la primera ecuación")
    x1 = float(input("Escribe el coeficiente de x en la primera ecuación: "))
    y1 = float(input("Escribe el coeficiente de y en la primera ecuación: "))
    res1 = float(input("Escribe el resultado de la primera ecuación: "))
    print(" ")
   
    print("Escribe los coeficientes de las incognitas de la segunda ecuación ")
    x2 = float(input("Escribe el coeficiente de x en la segunda ecuación: "))
    y2 = float(input("Escribe el coeficiente de y en la segunda ecuación: "))
    res2 = float(input("Escribe el resultado de la segunda ecuación: "))
    print(" ")
   
    dos_ecuaciones(x1, x2, y1, y2, res1, res2)

elif numero_ecuaciones == 3:
    print("Recuerda que las ecuaciones tienen que estar en la forma ax + by + cz = d")
    print(" ")
    
    print("Escribe los coeficientes de las incognitas de la primera ecuación")
    x1 = float(input("Escribe el coeficiente de x en la primera ecuación: "))
    y1 = float(input("Escribe el coeficiente de y en la primera ecuación: "))
    z1 = float(input("Escribe el coeficiente de z en la primera ecuación: "))
    res1 = float(input("Escribe el resultado de la primera ecuación: "))
    print(" ")

    print("Escribe los coeficientes de las incognitas de la segunda ecuación")
    x2 = float(input("Escribe el coeficiente de x en la segunda ecuación: "))
    y2 = float(input("Escribe el coeficiente de y en la segunda ecuación: "))
    z2 = float(input("Escribe el coeficiente de z en la segunda ecuación: "))
    res2 = float(input("Escribe el resultado de la segunda ecuación: "))
    print(" ")

    print("Escribe los coeficientes de las incognitas de la tercera ecuación")
    x3 = float(input("Escribe el coeficiente de x en la tercera ecuación: "))
    y3 = float(input("Escribe el coeficiente de y en la tercera ecuación: "))
    z3 = float(input("Escribe el coeficiente de z en la tercera ecuación: "))
    res3 = float(input("Escribe el resultado de la tercera ecuación: "))
    print(" ")

    tres_ecuaciones(x1, x2, x3, y1, y2, y3, z1, z2, z3, res1, res2, res3)

elif numero_ecuaciones == 4:
    print("Recuerda que las ecuaciones tienen que estar en la forma ax + by + cz + dw = e")
    print(" ")
    
    print("Escribe los coeficientes de las incognitas de la primera ecuación")
    x1 = float(input("Escribe el coeficiente de x en la primera ecuación: "))
    y1 = float(input("Escribe el coeficiente de y en la primera ecuación: "))
    z1 = float(input("Escribe el coeficiente de z en la primera ecuación: "))
    w1 = float(input("Escribe el coeficiente de w en la primera ecuación: "))
    res1 = float(input("Escribe el resultado de la primera ecuación: "))
    print(" ")

    print("Escribe los coeficientes de las incognitas de la segunda ecuación")
    x2 = float(input("Escribe el coeficiente de x en la segunda ecuación: "))
    y2 = float(input("Escribe el coeficiente de y en la segunda ecuación: "))
    z2 = float(input("Escribe el coeficiente de z en la segunda ecuación: "))
    w2 = float(input("Escribe el coeficiente de 2 en la segunda ecuación: "))
    res2 = float(input("Escribe el resultado de la segunda ecuación: "))
    print(" ")

    print("Escribe los coeficientes de las incognitas de la tercera ecuación")
    x3 = float(input("Escribe el coeficiente de x en la tercera ecuación: "))
    y3 = float(input("Escribe el coeficiente de y en la tercera ecuación: "))
    z3 = float(input("Escribe el coeficiente de z en la tercera ecuación: "))
    w3 = float(input("Escribe el coeficiente de w en la tercera ecuación: "))
    res3 = float(input("Escribe el resultado de la tercera ecuación: "))
    print(" ")

    x4 = float(input("Escribe el coeficiente de x en la cuarta ecuación: "))
    y4 = float(input("Escribe el coeficiente de y en la cuarta ecuación: "))
    z4 = float(input("Escribe el coeficiente de z en la cuarta ecuación: "))
    w4 = float(input("Escribe el coeficiente de w en la cuarta ecuación: "))
    res4 = float(input("Escribe el resultado de la cuarta ecuación: "))
    print(" ")

    cuatro_ecuaciones(x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4, w1, w2, w3, w4, res1, res2, res3, res4)

else:
    print("Has puesto un numero de incognitas que mi sistema no puede calcular")

blabla = input("Si le das a enter esta pestaña se cerrará")