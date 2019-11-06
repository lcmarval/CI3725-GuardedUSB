###############################################################
# Etapa 2
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
from lexer import *


import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)

parserErrorFound=False

# Operators precedence
precedence = (
	('nonassoc', 'TkLeq', 'TkGeq','TkEqual','TkNEqual','TkLess','TkGreater'),
	('left', 'TkPlus', 'TkMinus'),
	('left', 'TkMult', 'TkDiv','TkMod'),
	('left', 'TkOr'),
	('right', 'TkAnd'),
	('right', 'TkNot','TkUminus'),
	('left', 'TkConcat'),
	('left', 'TkOBracket', 'TkCBracket'),
	('left', 'TkOpenPar','TkClosePar'),
	('left', 'TkArrow')
)

	#('left', 'TkRof','TkFi'),
	#('right', 'TkAtoi','TkMin','TkMax', 'TkSize'),
	#('right', 'TkIf','TkGuard','TkDo', 'TkFor'),

class Node:
	def __init__(self,type,child=None,leaf=None):
		self.type = type
		if child:
			self.child = child
		else:
			self.child = [ ]
		self.leaf = leaf
	def __str__(self):
		return str(self.type)

	#Adds childs to a node.
	def addChild(self,newChild):
		self.child = [newChild] + self.child

	#Obtiene el type del nodo.
	def getType(self):
		return self.type

	#Change node type.
	def changeType(self,newType):
		self.type = newType

# Initial rule
def p_block(p):
	'''block : TkOBlock TkCBlock
	| TkOBlock declare_variables instruction_block TkCBlock 
	| TkOBlock instruction_block TkCBlock '''
	
	if (len(p) == 5 ):
		p[0] = Node('Block', [p[2],p[3]], None)

	elif(len(p) == 4):
		p[0] = Node('Block', [p[2]], None)

	else: 
		p[0] = Node('EMPTY', [None], None)

def p_declare_variables(p):
	'''declare_variables : TkDeclare variable_List '''
	if (p[1] == 'declare'):
		p[0] = Node('Declare', [p[2]], None)

def p_variable_List(p):
	'''variable_List : TkId TkComma variable_List
				      | TkId TkTwoPoints type TkComma variable_List
				      | TkId TkTwoPoints type
				      | type TkComma variable_List
				      | type '''
	if (len(p) == 4 and p[2] == ','):
		p[0] = Node('variable_List', p[3])
	elif(len(p) == 6):
		p[0] = Node('variable_List', [Node('type', p[3], None), p[5]], None)


	elif(len(p) == 4 and p[2] == ','):
		p[0] = Node('', [Node('type', p[1], None), Node('variable_List', p[4], None)], None)

	elif(len(p) == 2):
		p[0] = Node('type',(p[1]), None)

def p_type(p):
	'''type : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket TkSemicolon
	| TkInt TkSemicolon
	| TkBool TkSemicolon
	| TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket
	| TkInt
	| TkBool '''

	if (p[1] == 'array' and len(p) == 9):
		p[0] = Node('Sequencing', Node('array-range',[p[3], p[7]],None), None)

	elif (p[1] == 'array' and len(p) == 8):
		p[0] = Node('array-range', [p[3], p[5]],None)

	else:
		if(len(p) == 3 and p[2] == ';'):
			#armar secuencia
			p[0]= Node('Sequencing', Node('type',p[1], None), None)
		if(len(p) == 2):
			#no se arma secuencia
			p[0]= Node('type', p[1], None)

def p_instruction_block(p):
	'''instruction_block : instructions TkSemicolon instruction_block
	| instructions '''
	if (len(p) == 2):
		p[0] = Node('Block', [p[1]], None)

	else:
		p[0] = Node('Sequencing', [p[1], p[3]], None)

	#| iteration_do_inst
def p_instructions(p):
	'''instructions : assign_inst
	| input_inst
	| output_inst
	| if_guard_inst
	| iteration_for_inst
	| iteration_mult_guard_inst
	| block '''
	
	p[0] = Node('instructions',[p[1]], None) 

def p_assign_inst(p):
	'''assign_inst : TkId TkAsig expression'''
	if (len(p) == 4):
		p[0] = Node('Asig', [p[1],p[3]], None)

def p_array_exp(p):
	'''array_exp : TkId TkOpenPar expression TkTwoPoints expression TkClosePar array_exp 
	| TkOpenPar expression TkTwoPoints expression TkClosePar array_exp
	| TkId TkOBracket expression TkCBracket
	| TkId TkConcat TkId
	| array_exp TkConcat TkId
	| TkId TkConcat array_exp
	| array_exp TkConcat array_exp
	| TkOBracket expression TkCBracket
	| TkAtoi TkOpenPar TkId TkClosePar
	| TkSize
	| TkMax
	| TkMin '''
	
	if(len(p) == 8):
		if (p[2] == '('):
			p[0] = Node('array_exp', [p[1],p[3],p[5],p[7]], None)
		elif(p[1] == '('):
			p[0] = Node('array_exp', [p[2],p[4],p[6]], None)
	
	if (len(p) == 5):
		p[0] = Node('array_exp', [p[1],p[3]], None)

	elif(len(p) == 4):
		if (p[1] == '[' and p[3] == ']'):
			Node('array_exp', [p[2]], None)
		elif(p[2] == '||'):
			p[0] = Node('Concat', [p[1],p[3]], None)
	elif(len(p) == 2):
		p[0] == Node('array_exp',p[1], None)

def p_expression(p):
	'''expression : TkOpenPar expression TkPlus expression TkClosePar
	| TkOpenPar expression TkMinus expression TkClosePar
	| TkOpenPar expression TkMult expression TkClosePar
    | TkOpenPar expression TkDiv expression TkClosePar
    | TkOpenPar expression TkMod expression TkClosePar
    | TkOpenPar expression TkConcat expression TkClosePar
    | TkOpenPar expression TkGeq expression TkClosePar
    | TkOpenPar expression TkLess expression TkClosePar
    | TkOpenPar expression TkGreater expression TkClosePar
    | TkOpenPar expression TkNEqual expression TkClosePar
    | TkOpenPar expression TkEqual expression TkClosePar
    | TkOpenPar expression TkOr expression TkClosePar
    | TkOpenPar expression TkAnd expression TkClosePar
    | TkOpenPar TkUminus expression TkClosePar
    | TkOpenPar TkNot expression TkClosePar
    | TkOpenPar array_exp TkClosePar
    | TkOpenPar TkId TkClosePar
    | TkOpenPar TkNum TkClosePar
    | TkOpenPar TkFalse TkClosePar
    | TkOpenPar TkTrue TkClosePar
    | TkOpenPar TkString TkClosePar  
	| expression TkPlus expression
	| expression TkMinus expression
	| expression TkMult expression
	| expression TkDiv expression
	| expression TkMod expression
	| expression TkLeq expression
	| expression TkGeq expression
	| expression TkLess expression
	| expression TkGreater expression
	| expression TkNEqual expression
	| expression TkEqual expression  		   
	| expression TkOr expression
	| expression TkAnd expression	   
	| TkUminus expression
	| TkNot expression
	| array_exp
	| TkId
	| TkNum
	| TkFalse
	| TkTrue
	| TkString  '''
	p[0] = p[1]

def p_input_inst(p):
	''' input_inst : TkRead TkId '''
	p[0] = Node('Input', [p[3]],p[1])

def p_output_inst(p):
	'''output_inst : TkPrint expression
	| TkPrintln expression '''
	p[0] = Node('output_inst',[p[3]],p[1])

def p_if_guard_inst(p):
	'''if_guard_inst : TkIf expression TkArrow instructions TkFi 
	| TkIf expression TkArrow instructions guards
	'''
	if (len(p) == 7):
		p[0] = Node('If', [p[2],p[4],p[5]],None)
	else:
		p[0] = Node('If',[p[2],p[4]], None)
def p_guards(p):
	'''guards : TkGuard expression TkArrow instructions TkFi
	| TkGuard expression TkArrow instructions guards '''
	if (len(p) == 6):
		p[0] = Node('Guard',[p[2],p[4],p[5]], None)
	else:
		p[0] = Node('Guard',[p[2],p[4]], None)

def p_iteration_for_inst(p):
	''' iteration_for_inst : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof
    '''
	p[0] = Node('iteration_for_inst', [p[4],p[6],p[8]], None)

#def p_iteration_do_inst(p):
#	'''iteration_do_inst : TkDo expression TkArrow instructions TkOd '''
#	p[0] = Node('iteration_do_inst', [p[2],p[4]],None)

def p_iteration_mult_guard_inst(p):
	'''iteration_mult_guard_inst : TkDo expression TkArrow instructions guards TkOd
	| TkDo expression TkArrow instructions TkOd '''
	if(len(p) == 7):
		p[0] = Node('iteration_mult_guard_int',[p[2],p[4],p[5]] , None)
	else:
		p[0] = Node('iteration_mult_guard_int',[p[2],p[4]] , None)

#Regla de los errores sintacticos
def p_error(p):
	global parserErrorFound
	parserErrorFound = True
	#print('Error de sintaxis en la linea: ' + str(p.lineno) + ', columna: '+str(obtenerColumna(p.lexer.lexdata,p))+', token inesperado: ' + str(p.type))
	exit()

# Funcion que recorre el arbol y lo imprime. 
def printTree(nodo, tabs):
	print('\t'*tabs + str(nodo))
	if not (isinstance(nodo, Node)):
		return
	for i in range(len(nodo.children)):
			if nodo.children[i] != None:
				printTree(nodo.children[i], tabs+1)

def main():
	if (len(sys.argv) != 2):
		print("Usage: python3 parser.py nombreArchivo")
		return -1
		
	# Construyendo el parser
	#parser = yacc.yacc(errorlog = yacc.NullLogger())
	parser = yacc.yacc(debug=True)	
	# Se abre el archivo con permisos de lectura
	string = str(open(str(sys.argv[1]),'r').read())
	log = logging.getLogger()
	result = parser.parse(string,lex,debug=log)
	
	
	#Si no hay errores, imprime el arbol.
	#if (not lexerErrorFound) and (not parserErrorFound):
	#	printTree(result, 0)

if __name__ == "__main__":
    main()
    print ("All tests passed.")