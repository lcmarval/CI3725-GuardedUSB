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
    ('right', 'TkIf'),
    ('left', 'TkAsig'),
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

# Initial rule

def p_start(p):
    ''' start : block '''
    p[0] = p[1]

# Puede haber declare, pero el instructionsBlock es obligatorio, a menos que el programa sea vacio (Enunciado)
def p_block(p):
    ''' block : TkOBlock sequencing TkCBlock
    | TkOBlock TkDeclare declare_var sequencing TkCBlock '''
    
    if(len(p) == 4):
        p[0] = p[2]

    else: 
        p[0] = Node('BLOCK', [p[3],p[4]], None)

def p_declare_var(p):
    ''' declare_var : variables TkTwoPoints type TkSemicolon declare_var
    | variables  TkTwoPoints type  '''

    if (len(p) == 5):
        p[0] = Node('DECLARE_VAR', [p[1],p[3]],None)

    else:
        p[0] = Node('DECLARE_VAR',[p[1],p[3]],None)

def p_variables(p):
    ''' variables : TkId TkComma variables
    | TkId '''

    if (len(p) == 2):
        p[0] = Node('VARIABLE', None, p[1])
    else:
        p[0] = Node ('VARIABLE', [p[3]], p[1])

# Poner los arreglos de manera explicita array
# Complementar casos

# No es trabajo del parser revisar si dicha expresion es de tipo entero
def p_array(p):
    ''' array : TkArray TkOBracket expression TkSoForth expression TkCBracket
    '''
    p[0] = Node('Array', [p[3],p[5]],None)

# Regla de la gramatica para que el parser reconozca todas las operaciones de los arreglos.
def p_op_array(p):
    '''op_array : TkAtoi TkOpenPar TkId TkClosePar
    | TkSize TkOpenPar TkId TkClosePar
    | TkMin TkOpenPar TkId TkClosePar
    | TkMax TkOpenPar TkId TkClosePar
    | TkAtoi TkOpenPar array_exp TkClosePar
    | TkSize TkOpenPar array_exp TkClosePar
    | TkMin TkOpenPar array_exp TkClosePar
    | TkMax TkOpenPar array_exp TkClosePar
    '''

    p[0] = Node('op_array',[p[3]], p[1])


def p_array_exp(p):
    ''' array_exp : array_exp TkOpenPar expression TkTwoPoints expression TkClosePar
    | TkId TkOpenPar expression TkTwoPoints expression TkClosePar
    | TkId TkOBracket expression TkCBracket
    '''
    if (len(p) == 7):
        idTk = re.compile('[a-zA-Z][a-zA-Z0-9_]*')
        if (idTk.match(p[1])):
            p[0] = Node('ARRAY-EXPRESSION', [p[3],p[5]], p[1])
        else:
            p[0] = Node('ARRAY-EXPRESSION', [p[1],p[3],p[5]], None)
    else:
        p[0] = Node('ARRAY-EXPRESSION', [p[3]], p[1])


def p_type(p):
    ''' type : TkInt
    | TkBool
    | array
    | TkInt TkComma type
    | TkBool TkComma type
    | array TkComma type '''

    if(p[1] == 'bool' ):
        p[0] = Node('TYPE-BOOL',None,None)
    elif(isinstance(p[1],int)):
        p[0] = Node('TYPE-INT',None,None)
    else:
        p[0] = Node('TYPE-ARRAY',None,None)

def p_sequencing(p):
    ''' sequencing : instruction TkSemicolon
    | instruction TkSemicolon sequencing '''

    if (len(p) == 3):
        p[0] = Node('SEQUENCING', [p[1]], None)
    else:
        p[0] = Node('SEQUENCING', [p[1], p[3]], None)

def p_instruction(p):
    '''instruction : assign_inst
    | input_inst
    | output_inst
    | if_inst
    | iteration_for_inst
    | iteration_mult_guard_inst
    | block '''

    p[0] = Node('INSTRUCTION',[p[1]],None)

def p_expression(p):
    '''expression : TkOpenPar expression TkClosePar
    | expression TkConcat expression
    | expression TkPlus expression 
    | expression TkMinus expression 
    | expression TkMult expression 
    | expression TkDiv expression 
    | expression TkMod expression 
    | expression TkAnd expression
    | expression TkOr expression 
    | expression TkLess expression
    | expression TkLeq expression 
    | expression TkGreater expression 
    | expression TkGeq expression 
    | expression TkEqual expression 
    | expression TkNEqual expression
    | TkUminus expression 
    | TkNot expression
    | op_array expression  
    | TkId  
    | TkNum
    | TkTrue 
    | TkFalse
    | TkString
    | array_exp 
    '''

    if(len(p) == 2):
        strings = re.compile('[\'][a-zA-Z_][\']|["][a-zA-Z_]["]')
        idTk = re.compile('[a-zA-Z][a-zA-Z0-9_]*')
        if(p[1] == 'true'):
            p[0] = Node('TRUE-LITERAL', None, p[1])
        elif(p[1] == 'false'):
            p[0] = Node('FALSE-LITERAL', None, p[1])
        elif(isinstance(p[1],int)):
            p[0] = Node('TKNUM-LITERAL', None, p[1])
        elif isinstance(p[1],Node):
            p[0] = Node('ARRAY-LITERAL')
        elif(idTk.match(p[1])):
            p[0] = Node('ID-LITERAL',None, p[1])
        elif strings.match(p[1]):
            p[0] = Node('STRING-LITERAL',None, p[1])
        else:
            p[0] = Node('ARRAY-EXPRESSION',[p[1]], None)

    elif(len(p) == 4):
        if(p[1] == '('):
            p[0] = Node('(EXPRESION)',[p[2]],None)
        else:
            if(p[2] == '||'):
                p[0] = Node('CONCAT-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '+'):
                p[0] = Node('SUM-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '-'):
                p[0] = Node('SUBSTRACT-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '*'):
                p[0] = Node('MULT-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '/'):
                p[0] = Node('DIV-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '%'):
                p[0] = Node('MOD-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '/\\'):
                p[0] = Node('AND-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '\/'):
                p[0] = Node('OR-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '<'):
                p[0] = Node('LESS-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '<='):
                p[0] = Node('LEQ-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '>'):
                p[0] = Node('GREATER-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '>='):
                p[0] = Node('GEQ-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '=='):
                p[0] = Node('EQUAL-EXPRESSION',[p[1],p[3]],p[2])
            elif(p[2] == '!='):
                p[0] = Node('NEQUAL-EXPRESSION',[p[1],p[3]],p[2])
    else:
        if (p[1] == '-'):
            p[0]=Node("UNARY_MINUS-EXPRESSION",  [p[2]], p[1])
        elif(p[1] == '!'):
            p[0]=Node("NOT-EXPRESSION",  [p[2]], p[1])
        else:
            p[0]=Node("ARRAY-OP-EXPRESSION",  [p[2]], p[1])

def p_assign_inst(p):
    ''' assign_inst : TkId TkAsig assign_array
    | TkId TkAsig expression '''
    p[0] = Node('ASSIGN', [p[3]], p[1])

def p_assign_array(p):
    ''' assign_array : assign_array TkComma assign_array 
    | expression TkComma expression '''

    p[0] = Node('INIT-ARRAY',[p[1], p[3]],None)

def p_input_inst(p):
    ''' input_inst : TkRead TkId '''
    p[0] = Node('INPUT', [p[2]],p[1])

def p_output_inst(p):
    '''output_inst : TkPrint expression
    | TkPrintln expression '''
    p[0] = Node('OUTPUT',[p[2]],p[1])

def p_if_inst(p):
    '''if_inst : TkIf expression TkArrow block TkFi 
    | TkIf expression TkArrow block guards_inst
    '''
    if (len(p) == 6 and (p[5] == 'Fi')):
        p[0] = Node('IF', [p[2],p[4]],None)
    else:
        p[0] = Node('IF',[p[2],p[4],p[5]], None)

def p_guards_inst(p):
    '''guards_inst : TkGuard expression TkArrow block
    | TkGuard expression TkArrow block guards_inst '''
    if (len(p) == 5):
        p[0] = Node('GUARD',[p[2],p[4]], None)
    else:
        p[0] = Node('GUARD',[p[2],p[4],p[5]], None)

def p_iteration_for_inst(p):
    ''' iteration_for_inst : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof
    '''
    p[0] = Node('FOR', [p[4],p[6],p[8]], None)

def p_iteration_mult_guard_inst(p):
    '''iteration_mult_guard_inst : TkDo expression TkArrow block TkOd
    | TkDo expression TkArrow block guards_inst TkOd '''
    if(len(p) == 7):
        p[0] = Node('DO',[p[2],p[4],p[5]] , None)
    else:
        p[0] = Node('DO',[p[2],p[4]] , None)


def p_error(p):
    global parserErrorFound
    parserErrorFound = True
    print('Error Token= ' + str(p))
    #print('Error de sintaxis en la linea: ' + str(p.lineno) + ', columna: '+str(obtenerColumna(p.lexer.lexdata,p))+', token inesperado: ' + str(p.type))
    #exit()

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
    #parser = yacc.yacc(errorlog = yacc.NullLogger())
    parser = yacc.yacc(debug=True)  
    # Se abre el archivo con permisos de lectura
    string = str(open(str(sys.argv[1]),'r').read())
    log = logging.getLogger()
    result = parser.parse(string,lex,debug=log)
    
    
    #Si no hay errores, imprime el arbol.
    #if (not lexerErrorFound) and (not parserErrorFound):
    if (not parserErrorFound):
        printTree(result, 0)

if __name__ == "__main__":
    main()
    print ("All tests passed.")