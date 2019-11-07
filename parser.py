###############################################################
# Etapa 2
#   - Archivo: Parser
#   - Lenguaje: Python
#   - Version: 3
#   - Septiembre-Diciembre 2019
#   - CI-3725
#   - Funcion: Parser del lenguaje GuardedUSB
#   
#    - Autores:
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
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv','TkMod'),
    ('left', 'TkOr'),
    ('right', 'TkAnd'),
    ('right', 'TkNot','TkUminus'),
    ('left', 'TkConcat'),
    ('left', 'TkOBracket', 'TkCBracket'),
    ('nonassoc', 'TkLeq', 'TkGeq','TkEqual','TkNEqual','TkLess','TkGreater'),
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
    | TkOBlock TkDeclare variable_List instruction_block TkCBlock 
    | TkOBlock instruction_block TkCBlock '''
    
    if (len(p) == 6 ):
        p[0] = Node('Block', [p[3],p[4]], None)

    elif(len(p) == 4):
        p[0] = Node('Block', [p[2]], None)

    else: 
        p[0] = Node('EMPTY', None, None)

def p_variable_List(p):
    '''variable_List : TkId TkComma variable_List   
                      | TkId TkTwoPoints type TkComma variable_List
                      | TkId TkTwoPoints type TkSemicolon
                      | TkId TkTwoPoints type
                      | type TkComma variable_List
                      | type TkSemicolon
                      | type  '''  

    if (len(p) == 6):
        p[0] = Node('variable_List', [p[3],p[5]], None)

    elif(len(p) == 4):
        p[0] = Node('variable_List', [p[3]], None)

    elif(len(p) == 3):
        p[0] = Node('variable_List',[p[2]], None)

    else:
        p[0] = Node('variable_List',[p[1]], None)

def p_type(p):
    '''type : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket
    | TkInt
    | TkBool '''

    if (p[1] == 'array' and len(p) == 7):
        p[0] = Node('array-range', [p[3], p[5]],None)

    else:
        p[0] = p[1]

def p_instruction_block(p):
    '''instruction_block : instructions TkSemicolon instruction_block
    | instructions TkSemicolon
    | instructions '''
    if (len(p) == 2):
        p[0] = Node('Ins_Block', [p[1]], None)

    elif(len(p)==4):
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
        p[0] = Node('Asig', [p[3]], p[1])

def p_array_exp(p):
    '''array_exp : TkId TkOpenPar expression TkTwoPoints expression TkClosePar array_exp 
    | TkOpenPar expression TkTwoPoints expression TkClosePar array_exp
    | TkId TkOBracket expression TkCBracket
    | TkId TkConcat literal
    | array_exp TkConcat literal
    | TkOBracket expression TkCBracket
    | TkAtoi TkOpenPar TkId TkClosePar
    | TkSize TkOpenPar TkId TkClosePar
    | TkMax TkOpenPar TkId TkClosePar
    | TkMin TkOpenPar TkId TkClosePar
    '''
    
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
        p[0] == Node('array_exp',[p[1]], None)

def p_array_exp1(p):
    ''' array_exp1 : TkOpenPar array_exp TkClosePar '''
    p[0] = Node('array_exp1',[p[2]], None)

def p_expression(p):
    '''expression : TkOpenPar binop TkClosePar
    | TkOpenPar TkUminus expression TkClosePar
    | TkOpenPar TkNot expression TkClosePar
    | TkOpenPar literal TkClosePar
    | TkUminus expression
    | TkNot expression
    | literal
    | binop  '''       

    if(len(p) == 6):
        p[0] = Node('Expression', [p[2],p[4]], p[3])
    
    elif(len(p) == 5):
        p[0] = Node('Expression', [p[3]], p[2])
    
    elif(len(p) == 4):
        if (p[1] == '(' and p[3] == ')'):
            p[0] = Node('Expression', None, [p[2]])
        else:
            p[0] = Node('Expression',[p[1],p[3]],p[2])

    elif(len(p) == 3):
        p[0] = Node('Expression', [p[2]],None)

    else:
        p[0] = Node('Expression',None, p[1])

def p_binop(p):
    '''binop : expression TkPlus expression
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
    | expression TkConcat expression
    '''
    if (len(p) == 4):
        if (p[2] == '+'):
            p[0] = Node('+', None, [p[1],p[2]])
        elif (p[2] == '-'):
            p[0] = Node('-', None, [p[1],p[2]])
        elif (p[2] == '*'):
            p[0] = Node('*', None, [p[1],p[2]])
        elif (p[2] == '/'):
            p[0] = Node('/', None, [p[1],p[2]])
        elif (p[2] == '%'):
            p[0] = Node('%', None, [p[1],p[2]])
        elif (p[2] == '<='):
            p[0] = Node('<=', None, [p[1],p[2]])
        elif (p[2] == '>='):
            p[0] = Node('>=', None, [p[1],p[2]])
        elif (p[2] == '<'):
            p[0] = Node('<', None, [p[1],p[2]])
        elif (p[2] == '>'):
            p[0] = Node('>', None, [p[1],p[2]])
        elif (p[2] == '!='):
            p[0] = Node('!=', None, [p[1],p[2]])
        elif (p[2] == '=='):
            p[0] = Node('==', None, [p[1],p[2]])
        elif (p[2] == '\\\/'):
            p[0] = Node('Or', None, [p[1],p[2]])
        elif (p[2] == '\/\\'):
            p[0] = Node('And', None, [p[1],p[2]])  
        elif (p[2] == '||'):
            p[0] = Node('Concat', None, [p[1],p[2]])

def p_literal(p):
    '''literal : array_exp
    | TkId
    | TkNum
    | TkFalse
    | TkTrue
    | TkString      
    | array_exp1 '''
    p[0] = Node('literal', None, p[1])

def p_input_inst(p):
    ''' input_inst : TkRead TkId '''
    p[0] = Node('Input', [p[2]],p[1])

def p_output_inst(p):
    '''output_inst : TkPrint expression
    | TkPrintln expression '''
    p[0] = Node('output_inst',[p[2]],p[1])

def p_if_guard_inst(p):
    '''if_guard_inst : TkIf expression TkArrow instructions TkFi 
    | TkIf expression TkArrow instructions guards
    '''
    if (len(p) == 6 and (p[5] == 'Fi')):
        p[0] = Node('If', [p[2],p[4]],None)
    else:
        p[0] = Node('If',[p[2],p[4],p[5]], None)
def p_guards(p):
    '''guards : TkGuard expression TkArrow instructions TkFi
    | TkGuard expression TkArrow instructions guards '''
    if (len(p) == 6 and (p[5] == 'Fi')):
        p[0] = Node('Guard',[p[2],p[4]], None)
    else:
        p[0] = Node('Guard',[p[2],p[4],p[5]], None)

def p_iteration_for_inst(p):
    ''' iteration_for_inst : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof
    '''
    p[0] = Node('iteration_for_inst', [p[4],p[6],p[8]], None)

def p_iteration_mult_guard_inst(p):
    '''iteration_mult_guard_inst : TkDo expression TkArrow instructions guards TkOd
    | TkDo expression TkArrow instructions TkOd '''
    if(len(p) == 7):
        p[0] = Node('Do',[p[2],p[4],p[5]] , None)
    else:
        p[0] = Node('Do',[p[2],p[4]] , None)

#Regla de los errores sintacticos
def p_error(p):
    global parserErrorFound
    parserErrorFound = True
    print('Error Token= ' + str(p))
    exit()

# Funcion que recorre el arbol y lo imprime. 
def printTree(nodo, tabs):
    print('\t'*tabs + str(nodo))
    if not (isinstance(nodo, Node)):
        return
    for i in range(len(nodo.child)):
            if nodo.child[i] != None:
                printTree(nodo.child[i], tabs+1)

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 parser.py nombreArchivo")
        return -1
        
    # Construyendo el parser
    parser = yacc.yacc(debug=True)  
    # Se abre el archivo con permisos de lectura
    string = str(open(str(sys.argv[1]),'r').read())
    log = logging.getLogger()
    result = parser.parse(string,lex,debug=log)
    
    #Si no hay errores, imprime el arbol.
    if (not parserErrorFound):
        printTree(result, 0)

if __name__ == "__main__":
    main()
    print ("All tests passed.")