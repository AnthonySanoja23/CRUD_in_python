# Hello World program in Python
    
import sys
clientes = ['Anthony','Alejandro']


def agregarcliente_a_la_lista_de_clientes(cliente_nuevo):
    global clientes #Agarra cualquier variable global para poder ser usada
    if cliente_nuevo not in clientes:
            clientes.append(cliente_nuevo)
            
    else:
        print("El cliente que digito ya esta Registardo ")



def borrar_clientes(cliente_nuevo):
    global clientes 
    if cliente_nuevo in clientes :
       clientes.remove(cliente_nuevo)
    else:
       print('El cliente que ingreso no se pudo eliminar por que no esta registrado ')  

def listar_clientes():
    for idx, clientes in enumerate(clientes):
        print('{}: {}'.format(idx,client))
     


def _obtener_nombre_del_cliente():
    cliente_nuevo = None #En python es como decirle que no hay ningun valor en la variable  

    while not cliente_nuevo:
      cliente_nuevo = input ('Cual es el nombre del cliente: ')

      if cliente_nuevo == 'exit':
          cliente_nuevo = None
          break # Funciona para terminar el programa 

    if not cliente_nuevo:
           sys.exit()  

    return cliente_nuevo         

def actualizar_cliente(cliente_nuevo,updated_name):
    global clientes

    if cliente_nuevo in clientes:
       index = clientes.index(cliente_nombre)
       clientes[index] = updated_name
     
    
    else:
          print('No hizo ningun cambio en el nombre')

    else:
       print('El cliente no esta registrado en la lista ')

def buscar_cliente(cliente_nuevo):

  for nombres in clientes:
    if nombres != cliente_nuevo:
        continue
    else:
        return True
           



def _menu():

   
    print('\t'+'*'*35)
    print('\t'+'* Bienvenido al Sistema de Ventas * ')
    print('\t'+'*'*35)

    print('Que quieres hacer tu hoy ?')
    print('Crear Cliente [C]')
    print('Actualizar Clientes [A]')
    print('Listar clientes [L]')
    print('Buscar Cliente [B]')
    print('Eliminar Clientes [D]')      
 

if __name__=='__main__':
    _menu()
    print('\n')
    comando = input('Digite su opción: ') #Es el cin>> de python 
    comando = comando.upper() # Prevenir que el usuario digite el comando en minuscula 

    if comando == 'C':
        cliente_nuevo = _obtener_nombre_del_cliente()
        agregarcliente_a_la_lista_de_clientes(cliente_nuevo)
        listar_clientes()

    elif comando == 'A':
       cliente_nuevo = _obtener_nombre_del_cliente()
       actualizar_cliente(cliente_nuevo)
       listar_clientes()

    elif comando == 'L':
         listar_clientes()   

    elif comando == 'D':
       cliente_nuevo = _obtener_nombre_del_cliente()
       borrar_clientes(cliente_nuevo)
       listar_clientes()
    
    elif comando == 'B':
        cliente_nuevo = _obtener_nombre_del_cliente()
        cliente_encontrado = buscar_cliente(cliente_nuevo)
        
        if cliente_encontrado:
           print('El cliente',cliente_nuevo,'esta en la lista ')
        else :
           print('El cliente',cliente_nuevo,'no esta en la lista ')         
        
    else:
        print('Este comando no existe')
       







    