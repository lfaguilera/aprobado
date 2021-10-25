def Memotest_e1():
    fichas={1:'D',2:'D',3:'s',4:'s'}
    posiciones=[1,2,3,4]
    print('Fichas y Posiciones: ',posiciones)
    
    opcion_1 = int(input('1er Posicion:'))
    posiciones[opcion_1-1] = fichas[opcion_1] 
    print(posiciones)
    
    opcion_2 = int(input('2do Posicion:')) 
    posiciones[opcion_2-1] = fichas[opcion_2]
   
    print(posiciones)
Memotest_e1()
# hasta aca llege. no se como hacer el ciclo para que vuelva si no son gemelas.
