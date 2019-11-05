###############################################################
# Etapa 1
# 	- Archivo: Parser
#   - Lenguaje: Python
#   - Version: 3
# 	- Septiembre-Diciembre 2019
# 	- CI-3725
# 	- Funcion: Parser del lenguaje GuardedUSB
# 	
#	 - Autores:
#       -Luis  Marval  12-10620
#       -Fabio Suarez  12-10578
################################################################

import ply.yacc as yacc
import ply.lex as lex
import sys
import re
# from lexer import

# Clase node que permite la creacion de los node del arbol sintactico.
class Node:
	def __init__(self,type,children=None,leaf=None):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = [ ]
		self.leaf = leaf
	def __str__(self):
		return str(self.type)

	#Cambia el type del nodo. hace falta?
	def changeType(self,newType):
		self.type = newType

	#Obtiene el type del nodo.
	def getType(self):
		return self.type

	#Agrega hijos a un nodo.
	def addChildren(self,newChildren):
		self.children = [newChildren] + self.children
'''
block: TkOBlock TkCBlock
	  |TkBlock declare_variables Instruction_Block TkCBlock 
	  |TkOblock Instruction_Block TkCBlock

declare_variables: TkDeclare variable_List

variables_List: TkId TkComma variable_List
				| TkId TkTwoPoints type tkComma variable_List
				| TkId TkTwoPoints type
				| type TkComma variable_List
				| type

type: TkArray TkOBracket TkNum TkPunto TkPunto TkNum TkCBracket TkSemicolon
	  |TkInt TkSemicolon
	  |TkBool TkSemicolon
	  |TkArray TKOBracket TkNum TkPunto TkPunto TkNum TkCBracket
	  |TkInt
	  |TkBool

instruction_block: Instruction
				   |Instruction TkSemicolon instruction_block

instructions: assign_inst
     		  |input_inst
     		  |output_inst
     		  |if_guard_inst
     		  |iteration_for_inst
     		  |iteration_inst
     		  |iteration_mult_guard_inst
     		  |block

assign_inst: TkId TkAssign assign_inst
			 |expression TkComma
			 |expression

array_exp: TkId TkOpenPar expression TkTwoPoints expression TkClosePar array_exp 
		  |TkOpenPar expression TkTwoPoints expression TkClosePar array_exp
		  |TkId TkOBracket expression TkCBracket
		  |TkOBracket expression TkCBracket
		  |TkAtoi TkOpenPar TkId TkClosePar
		  |TkSize
		  |TkMax
		  |TkMin

expression: expression TkPlus expression
		   |expression TkMinus expression
		   |expression TkMult expression
		   |expression TkDiv expression
		   |expression TkMod expression
		   |expression TkLeq expression
		   |expression TkGeq expression
		   |expression TkLess expression
		   |expression TkGreater expression
		   |expression TkNEqual expression
		   |expression TkEqual expression
		   |expression TkOr expression
		   |expression TkAnd expression
		   |TkUminus expression
		   |TkNot expression
		   |array_exp
		   |TkId
		   |TkNum
		   |TkFalse
		   |TkTrue
		   |TkString

input_inst: TkRead TkId

output_inst: TkPrint expression
			|TkPrintln expression

if_guard_inst: TkIf expression TkArrow instructions if_guard_inst TkFi
			  |TkGuard expression TkArrow instructions

iteration_for_inst: TkFor TkId TkIn expression TkTo expression TkArrow block TkRof

iteration_do_inst: TkDo expression TkArrow instructions TkOd

iteration_mult_guard_int: TkDo expression TkArrow instructions guards TkOd
						 |TkDo expression TkArrow instructions TkOd

guards: TkGuard expression TkArrow instructions guards
	   |TkGuard expression TkArrow instructions


'''

def main():
	if (len(sys.argv) != 2):
		print("Usage: python3 parser.py nombreArchivo")
		return -1
		
	# Construyendo el parser
	parser = yacc.yacc(errorlog=yacc.NullLogger())
		
	# Se abre el archivo con permisos de lectura
	string = str(open(str(sys.argv[1]),'r').read())
	result = parser.parse(string)
	
	#Si no hay errores, imprime el arbol.
	if (not lexerErrorFound) and (not parserErrorFound):
		printTree(result, 0)

#Llamada a la funcion
main()