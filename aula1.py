
n= int (input ('Informe o valor inteiro a ser analisado: '))

clc_triangular =  0 
y = 1
while clc_triangular >= n:
    clc_triangular = y* (y + 1) * (y+2)
    y+=  1  #  ou y = y + 1

    if calculo_nr_triangular == n: 
        print (f'E triangular')
    else:
        print (f'não é triangular')
    




