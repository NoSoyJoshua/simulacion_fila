#Esta tarea fue realizada por los estudiantes:
    #Luis Fonseca Chinchilla
    #Joshua Quesada Leon
    #Daniela Haug Leiva

import time
import random as r
import sys as s

try:
    opcion = int(input("Por favor ingrese:\n1. Retiro de efectivo.\n2. Prestamos.\n3. Aperturas de cuentas.\n4. Pagos.\nSeleccione la funcion que desea utiliza: "))
except:
    print("Lo sentimos, la opcion seleccionada no es valida.")
else:
    if 1<=opcion<=4:
        try:
            tamanofila = int(input("Ingrese el tamano de la fila que desea: "))
            duracion = int(input("Ingrese durante cuantos segundos desea que funcione la simulacion: "))
            velocidad = int(input("Ingrese un multiplicador de la velocidad a la que funciona la simulacion: "))
            neutraltime = int(input("Ingrese despues de cuantos segundos el cliente deja de estar feliz con el tiempo de espera: "))
            distribucion = int(input("El tiempo de espera de los clientes (en segundos) es aleatorio.\nIngrese 1 si desea una distribucion normal o 2 si desea una distribucion uniforme: "))
            if distribucion == 1:
                media = int(input("Ingrese la media de la distribucion: "))
                standev = int(input("Ingrese la desviacion estandar de la distribucion: "))
                if media < 1 or standev < 1:
                    print("Lo sentimos, alguno de los datos ingresados no esta de acuerdo al formato requerido.")
                    s.exit()
            elif distribucion == 2:
                mini = int(input("Ingrese el valor minimo de la distribucion: "))
                maxi = int(input("Ingrese el valor maximo de la distribucion: "))
                if maxi < mini or mini < 1:
                    print("Lo sentimos, alguno de los datos ingresados no esta de acuerdo al formato requerido.")
                    s.exit()
        except:
            print("Lo sentimos, alguno de los datos ingresados no esta de acuerdo al formato requerido.")
        else:
            if neutraltime>=1 and duracion>=1 and velocidad>=1 and tamanofila>=2 and (distribucion==1 or distribucion==2):

                cont_seg = 0
                
                fila_caja1, fila_caja2= [], []
                copia_f1, copia_f2 = [], []
                fila_enojada1, fila_enojada2 = [], []
                
                #Aqui se crea una lista del tamano solicitado en donde estaran las personas de la fila 1
                fila1 = []
                for i in range(0, tamanofila+1):
                    fila1.append("_")
                fila1[tamanofila]="T"
                
                #Aqui se crea una lista del tamano solicitado en donde estaran las personas de la fila 2
                fila2 = []
                for j in range(0, tamanofila+1):
                    fila2.append("_")
                fila2[tamanofila]="T"
                
                #Se genera el primer momento en que llegara un cliente
                llegada = -1
                while llegada <= 0:
                    llegada = int( r.gauss( 70, 30 )  )
                    
                salida1, salida2 = -1, -1
                   
                #Variables que ayudaran a mantener el orden de las filas
                a1, a2 = 1, 1
                b1, b2 = 2, 2
                c1, c2 = True, True
                d1, d2 = 0, 0
                tamanofila1, tamanofila2 = tamanofila, tamanofila
                
                #Variables que ayudaran a responder las preguntas finales
                llegadas = 0
                salidas = 0
                atendidas = 0
                enojadas = 0
                tiempos_espera = []
                    
                while cont_seg < duracion:
                    
                    #Variable que ayuda a saber si un cliente ya entro a una fila
                    asignado = False
                    
                    horas = int(cont_seg/3600)
                    minutos = int((cont_seg-3600*horas)/60)
                    segundos = cont_seg - 3600*horas - 60*minutos
                    
                    tamanofila3 = tamanofila - 1
                    tamanofila4 = tamanofila - 1
                    
                    #Esto determina si en el segundo actual entra una persona
                    if cont_seg == llegada:
                        llegadas = llegadas + 1
                        #Esto determina si el ciente entra a la fila 1 o a la fila 2
                        if fila1.count("_") >= fila2.count("_") and asignado == False:
                            #Esto me dice si la fila esta llena o no
                            if a1<=tamanofila1:
                                print("\n",horas,":",minutos,":",segundos)
                                print("Llego un cliente a la caja 1" )
                                fila1[tamanofila1-a1]="F"
                                print(fila1)
                                #Esta variable "a" ayuda a saber en que posicion debo poner al cliente que entro
                                a1 = a1 + 1
                                #Esta variable "d" ayuda a saber cuantos clientes hay en la fila
                                d1 = d1 + 1
                                fila_caja1.append( cont_seg )
                                #Ya que entro la persona, se genera un nuevo tiempo de llegada
                                llegada = cont_seg + int( r.gauss( 20, 5 ))
                                while llegada <= cont_seg:
                                    llegada = cont_seg + int( r.gauss( 20, 5 ))
                            else:
                                salidas = salidas + 1
                                llegada = cont_seg + int( r.gauss( 20, 5 ))
                                while llegada <= cont_seg:
                                    llegada = cont_seg + int( r.gauss( 20, 5 ))
                            #Esto me dice si debo generar o no un nuevo tiempo de salida (se debe generar solo si no hay uno para la persona en la primera posicion)
                            if c1 == True :
                                copia_f1.append( cont_seg )
                                #Aqui se genera un tiempo de salida aleatorio con distribucion normal
                                if distribucion == 1:
                                    rnd = int( r.gauss( media, standev ))
                                    salida1 = copia_f1[0] + rnd
                                    while salida1 <= copia_f1[0]:
                                        rnd = int( r.gauss( media, standev ))
                                        salida1 = copia_f1[0] + rnd
                                #Tiempo de salida con distribucion uniforme
                                elif distribucion == 2:
                                    rnd = r.randint(mini,maxi)
                                    salida1 = copia_f1[0] + rnd
                                tiempos_espera.append(rnd)
                                c1 = False
                            #Esto genera un tiempo de enojo para cada cliente que entra
                            for persona1 in fila_caja1:
                                if persona1 + neutraltime > cont_seg:
                                    fila_enojada1.append(persona1+neutraltime)
                                    fila_caja1.pop(0)
                                if d1 <= 1:
                                    fila_enojada1.pop(0) 
                            asignado = True
                            
                        #Los comentarios de la parte anterior sirven de manera tambien para esta parte
                        elif fila1.count("_") < fila2.count("_") and asignado == False:
                            if a2<=tamanofila2:
                                print("\n",horas,":",minutos,":",segundos)
                                print("Llego un cliente a la caja 2" )
                                fila2[tamanofila2-a2]="F"
                                print(fila2)
                                a2 = a2 + 1
                                d2 = d2 + 1
                                fila_caja2.append( cont_seg )
                                llegada = cont_seg + int( r.gauss( 20, 5 ))
                                while llegada <= cont_seg:
                                    llegada = cont_seg + int( r.gauss( 20, 5 ))
                            else:
                                salidas = salidas + 1
                                llegada = cont_seg + int( r.gauss( 20, 5 ))
                                while llegada <= cont_seg:
                                    llegada = cont_seg + int( r.gauss( 20, 5 ))
                            if c2 == True :
                                copia_f2.append( cont_seg )
                                if distribucion == 1:
                                    rnd = int( r.gauss( media, standev ))
                                    salida2 = copia_f2[0] + rnd
                                    while salida2 <= copia_f2[0]:
                                        rnd = int( r.gauss( media, standev ))
                                        salida2 = copia_f2[0] + rnd
                                elif distribucion == 2:
                                    rnd = r.randint(mini,maxi)
                                    salida2 = copia_f2[0] + rnd
                                tiempos_espera.append(rnd)
                                c2 = False             
                            for persona2 in fila_caja2:
                                if persona2 + neutraltime > cont_seg:
                                    fila_enojada2.append(persona2+neutraltime)
                                    fila_caja2.pop(0)
                                if d2 <= 1:
                                    fila_enojada2.pop(0)
                            asignado = True
                            
                    #Determina si una persona de la fila 1 se debe enojar en el segundo actual
                    if len(fila_enojada1) > 0:    
                        if fila_enojada1[0] == cont_seg:
                            enojadas = enojadas + 1
                            if b1<=tamanofila1:
                                print("\n",horas,":",minutos,":",segundos)
                                print("Se enojo un cliente en la caja 1")
                                fila1[tamanofila1-b1]="E"
                                print(fila1)
                                b1 = b1 + 1
                            fila_enojada1.pop(0)
                          
                    #Determina si una persona de la fila 2 se debe enojar en el segundo actual
                    if len(fila_enojada2) > 0:    
                        if fila_enojada2[0] == cont_seg:
                            enojadas = enojadas + 1
                            if b2<=tamanofila2:
                                print("\n",horas,":",minutos,":",segundos)
                                print("Se enojo un cliente en la caja 2")
                                fila2[tamanofila2-b2]="E"
                                print(fila2)
                                b2 = b2 + 1
                            fila_enojada2.pop(0)
                            
                    #Determina si una persona de la fila 1 debe salir en el segundo actual
                    if cont_seg == salida1:
                        atendidas = atendidas + 1
                        if b1 == 2:
                            a1 = a1 - 1
                            d1 = d1 - 1
                            copia_f1.pop(0)
                            print("\n",horas,":",minutos,":",segundos)
                            print("Salio un cliente de la caja 1")
                            while tamanofila3>=1:
                                fila1[tamanofila3]=fila1[tamanofila3-1]
                                tamanofila3 = tamanofila3 - 1
                            fila1[0] = "_"
                            print(fila1)
                            if len(fila_enojada1) > 0:
                                fila_enojada1.pop(0)
                        elif b1 > 2:
                            b1 = b1 - 1
                            a1 = a1 - 1
                            d1 = d1 - 1
                            copia_f1.pop(0)
                            print("\n",horas,":",minutos,":",segundos)
                            print("Salio un cliente de la caja 1")
                            while tamanofila3>=1:
                                fila1[tamanofila3]=fila1[tamanofila3-1]
                                tamanofila3 = tamanofila3 - 1
                            fila1[0] = "_"
                            print(fila1)
                        c1 = True
                            
                    #Determina si una persona de la fila 2 debe salir en el segundo actual
                    if cont_seg == salida2:
                        atendidas = atendidas + 1
                        if b2 == 2:
                            a2 = a2 - 1
                            d2 = d2 - 1
                            copia_f2.pop(0)
                            print("\n",horas,":",minutos,":",segundos)
                            print("Salio un cliente de la caja 2")
                            while tamanofila4>=1:
                                fila2[tamanofila4]=fila2[tamanofila4-1]
                                tamanofila4 = tamanofila4 - 1
                            fila2[0] = "_"
                            print(fila2)
                            if len(fila_enojada2) > 0:
                                fila_enojada2.pop(0)
                        elif b2 > 2:
                            b2 = b2 - 1
                            a2 = a2 - 1
                            d2 = d2 - 1
                            copia_f2.pop(0)
                            print("\n",horas,":",minutos,":",segundos)
                            print("Salio un cliente de la caja 2")
                            while tamanofila4>=1:
                                fila2[tamanofila4]=fila2[tamanofila4-1]
                                tamanofila4 = tamanofila4 - 1
                            fila2[0] = "_"
                            print(fila2)
                        c2 = True
                    
                    time.sleep( 1 / velocidad )
                    cont_seg = cont_seg + 1 
                
                #Datos del tiempo de espera
                suma = 0
                for i in range(len(tiempos_espera)):
                    suma = suma + tiempos_espera[i]
                promedio = suma/len(tiempos_espera)
                max_espera = max(tiempos_espera)
                
                print("\nLlego un total de ", llegadas, " personas.")
                print("Se fue un total de ", salidas, " personas.")
                print("Se atendio un total de ", atendidas, " personas.")
                print("Se enojaron un total de ", enojadas, " personas.")
                print("El tiempo promedio de atencion fue de ", promedio, " segundos.")
                print("El maximo tiempo de espera fue de ", max_espera, " segundos.")