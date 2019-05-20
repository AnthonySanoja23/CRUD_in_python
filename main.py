import sys
import os
import json

from pathlib import Path

my_file = Path("/home/anthony/Escritorio/Cursos de platzi /Python/App_Platzi/clientes.json")

clientes = []


if my_file.exists():

	archivo = open("clientes.json", "r")
	datos = archivo.read()
	archivo.close()
	clientes = json.loads(datos)	

else:

	print("No hay data cargada debido a que el archivo no existe ")
	input("Presione una tecla para continuar")

def agregarcliente_a_la_lista_de_clientes(cliente):
		global clientes #Agarra cualquier variable global para poder ser usada
		if cliente not in clientes:
						clientes.append(cliente)
						guardar_en_json()
						
		else:
				print("El cliente que digito ya esta Registardo ")



def borrar_clientes(client_id):
		global clients

		for idx, cliente in enumerate(clientes):
				if idx == cliente_id:
						del clientes[idx]
						guardar_en_json() 
						break
		else:
			 print('El cliente que ingreso no se pudo eliminar por que no esta registrado ')  


def listar_clientes():
	
			print('\n')
			global clientes
							 
			for idx, cliente in enumerate(clientes):

					print('{uid} | {nombre} | {apellido} | {edad} | {cargo} | {email} | {compañia}'.format(
					uid=idx,
					nombre=cliente['nombre'],
					apellido=cliente['apellido'],
					edad=cliente['edad'],
					cargo=cliente['cargo'],
					email=cliente['email'],
					compañia=cliente['compañia']))
			
	
		 
def _obtener_cliente_campo(nombre_campo):
		campo = None
	
		while not campo:
				campo = input('Cual es el {} del cliente :'.format(nombre_campo))
	
		return campo

	


def actualizar_cliente(cliente_id,actr_cliente):
		global clientes

		if len(clientes) - 1 >= cliente_id:
				clientes[cliente_id] = actr_cliente

				guardar_en_json()

		else:
			 print('El cliente no esta registrado en la lista ')



def buscar_cliente(cliente_nombre):

	for cliente in clientes:

			if cliente['nombre'] != cliente_nombre:
					continue
			else:
					return True



def obtener_informacion_completa() :
		cliente = {
				'nombre':_obtener_cliente_campo('nombre'),
				'apellido':_obtener_cliente_campo('apellido'),
				'edad':_obtener_cliente_campo('edad'),
				'cargo':_obtener_cliente_campo('cargo'),
				'email':_obtener_cliente_campo('email'),
				'compañia':_obtener_cliente_campo('compañia'),    
		}

		return cliente	


def guardar_en_json():

	datos = json.dumps(clientes)
	f = open('clientes.json','w')
	f.write(datos)
	f.close()					 



def _menu():

		os.system('clear')
		print('\t'+'*'*35)
		print('\t'+'* Bienvenido al Sistema de Ventas * ')
		print('\t'+'*'*35)

		print('Que quieres hacer tu hoy ?')
		print('[C]rear Cliente ')
		print('[A]ctualizar Clientes ')
		print('[L]istar clientes ')
		print('[B]uscar Cliente ')
		print('[E]liminar Clientes ')
		print('[S]alir ')      
 

if __name__=='__main__':
	
	while True:

		_menu()
		print('\n')
		comando = input('Digite su opción: ') #Es el cin>> de python 
		comando = comando.upper() # Prevenir que el usuario digite el comando en minuscula 

		if comando == 'C':
			cliente= obtener_informacion_completa()		
			agregarcliente_a_la_lista_de_clientes(cliente)
			listar_clientes()
			input("Presione cualquier tecla para continuar")

		elif comando == 'A':
			
			 cliente_id= int(_obtener_cliente_campo('id'))
			 actr_cliente = obtener_informacion_completa()

			 actualizar_cliente(cliente_id,actr_cliente)
				
			 listar_clientes()
			 input("Presione cualquier tecla para continuar")

		elif comando == 'L':
				 listar_clientes() 
				 input("Presione cualquier tecla para continuar")


		elif comando == 'E':
			 cliente_id = int(_obtener_cliente_campo('id'))
			 borrar_clientes(cliente_id)
			 listar_clientes()
			 input("Presione cualquier tecla para continuar")
		
		elif comando == 'B':
				cliente_nombre=_obtener_cliente_campo('nombre')
				cliente_encontrado = buscar_cliente(cliente_nombre)
				
				if cliente_encontrado:
					 print('El cliente',cliente_nombre,'esta en la lista ')
					 input("Presione cualquier tecla para continuar")
				else :
					 print('El cliente',cliente_nombre,'no esta en la lista ')
					 input("Presione cualquier tecla para continuar") 

		elif comando =='S':
			print("Gracias por usar el sistema. Regrese pronto")
			break 			         
				
		else:
				print('Este comando no existe')
				input("Presione cualquier tecla para continuar")
			 
