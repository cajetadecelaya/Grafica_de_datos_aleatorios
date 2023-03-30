#########Simulación de la Máquina de Galton

import random
import matplotlib.pyplot as plt


def grafica():
     """Se define funcion que se encargara de generar la grafica,incluyendo titulo y 
     nombre de ejes """
     plt.hist(lista_decisiones)
     plt.title('Simulacion de la maquina de Galton') 
     plt.xlabel('Contenedores')
     plt.ylabel('Cantidad de canicas')      
     plt.show()

bola = 3000    
""""Se define las 3000 pelotas que pide el ejercicio"""
lista_decisiones = [] 
'''Aqui se almacenaran los resultados de la ubicacione final de cada bola'''

for i in range(bola):
    """Se inicia ciclo for el que se encargara de generar desiciones aleatorias y 
    almacenarlas en una lita, observando """
    def decisiones (num_tiros):
        posicion = 12 
        '''Posicion central en la que iniciaria la bola a caer en el primer nivel.'''
        
        for dado in range(num_tiros):
            rd = int(random.randint(1,2))
            
            if rd <= 1:
                posicion = posicion - 1
                

            elif rd >= 2:
                posicion = posicion + 1
        """Segun el resultado del numero aleatorio se decide
          si si avnacza o retrosede la pelota y despues de tomar de referencia varios intentos
          se tomo como numero o deposito central el numero 12 como puede apreciarse en el video de muestra
          y asi despues de tomar bifurcar 12 veces se muestra un resultado"""     
        
        
        #print(f'Ubicacion final de la pelota {i} se ubica en a casilla :{posicion}') 
        '''Esta imprecion es para poder dar seguimiento al resultado de cada bola'''  

        return posicion
        

    x = decisiones(12)  
    """Aqui defino los niveles, o la cantidad de veces en la que la bola
        tomara la decicion de avanzar o retroceder de ubicacion."""   
    lista_decisiones.append(x)


#print(lista_decisiones)
grafica()
"""Inicio de funcion"""
    
