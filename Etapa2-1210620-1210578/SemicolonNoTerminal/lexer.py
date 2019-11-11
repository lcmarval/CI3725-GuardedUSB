###############################################################
# Etapa 1
# 	- Archivo: Lex
#   - Lenguaje: Python
#   - Version: 3
# 	- Septiembre-Diciembre 2019
# 	- CI-3725
# 	- Funcion: Analizador lexicográfico del lenguaje GuardedUSB
# 	
#	 - Autores:
#       -Luis  Marval  12-10620
#       -Fabio Suarez  12-10578
################################################################

import ply.lex as lex
import re
import codecs
import os
import sys

arrToks = []
errToks = []
row = 0
col = 0

tokens = [  
            'TkNum','TkId','TkPlus','TkMinus',
            'TkMult','TkDiv','TkMod', 'TkPunto','TkSemicolon','TkConjuncion',
            'TkDisyuncion','TkMenor','TkMenorIgual','TkMayor',
            'TkMayorIgual','TkIgual','TkDesigualdad','TkSiguienteCar',
            'TkAnteriorCar','TkValorAscii','TkConcatenacion','TkDosPuntos',
            'TkShift','TkCorcheteAbre','TkCorcheteCierra','TkParAbre',
            'TkParCierra','TkLlaveAbre','TkLlaveCierra','TkHacer',     
            'TkAsignacion','TkComa','TkSaltoDeLinea', 'TkTab',              
            'TkComillaSimple','TkBarraInversa','TkComments'
]

reservadas = {
            'atoi':'TkAtoi',
            'size':'TkSize',
            'max':'TkMax',
            'min':'TkMin',
            'declare': 'TkDeclare',
            'read': 'TkRead',
            'print': 'TkPrint',
            'println': 'TkPrintln',
            'if':'TkIf',        
            'fi': 'TkFi',
            'for': 'TkFor',
            'rof': 'TkRof',
            'in': 'TkIn',
            'to': 'TkTo',
            'do':'TkDo',
            'od':'TkOd',
            'int':'TkInt',
            'array':'TkArray',
            'true':'TkTrue', 
            'false':'TkFalse',
            'bool':'TkBool'
}

tokens = list(reservadas.values())+ [ 'TkString','TkId', 'TkNum', 'TkUminus', 'TkGuard', 'TkComments', 'TkOBlock', 'TkCBlock', 'TkSoForth', 'TkComma',
         'TkOpenPar', 'TkClosePar', 'TkAsig', 'TkSemicolon','TkArrow', 'TkPlus',
         'TkMinus', 'TkMult', 'TkDiv', 'TkMod', 'TkPunto', 'TkOr', 'TkAnd', 'TkNot',
         'TkLess', 'TkLeq', 'TkGreater', 'TkGeq', 'TkEqual', 'TkNEqual', 'TkOBracket',
         'TkCBracket', 'TkTwoPoints', 'TkConcat']

# Regular expression rules for simple tokens
t_TkGuard = r'\[\]'
t_TkOBlock = r'\|\['
t_TkCBlock = r'\]\|'
t_TkSoForth = r'\.\.'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r'\:\='
t_TkSemicolon = r';'
t_TkArrow = r'\-\-\>'
t_TkPlus       = r'\+'
t_TkMinus      = r'-'
t_TkMult       = r'\*'
t_TkDiv        = r'/'
t_TkMod        = r'%'
t_TkPunto      = r'\.'
t_TkOr = r'\\\/'
t_TkAnd = r'\/\\'
t_TkNot = r'!'
t_TkLeq = r'<='
t_TkGeq = r'>='
t_TkLess = r'<'
t_TkGreater = r'>'
t_TkEqual = r'=='
t_TkNEqual = r'!='
t_TkOBracket = r'\['
t_TkCBracket = r'\]'
t_TkTwoPoints = r'\:'
t_TkConcat = r'\|\|'
#t_TkComments = r'\/\/'

# A regular expression rule with some action code
def t_TkId(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = reservadas.get(t.value, None)
    return t

def t_TkNum(t):
    r'[\d]+|[-][\d]+'
    t.value = int(t.value) 
    return t

def t_TkUminus(t):
    r'[-][a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = reservadas.get(t.value, None)
    return t

def t_TkString(t):
    r'["][\"\|\\\]\#\%\&\(\)\*\=\¬\/\$\?\¡\!\¿\.\{\}\[\ñ\á\é\í\ó\ú\Á\É\Í\Ó\Ú\{\}\^\,\:\;\~\°\_\-\sa-zA-Z0-9]*["]'
    if t.value in reservadas:
        t.type = reservadas.get(t.value, None)
    return t

def t_TkComment(t):
    r'\/\/.*'
    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignoramos espacios y tabs

# Compute column.
#     input es el texto que entra como string
#     token es una instancia de un token
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Funcion: t_error
# Maneja el proceso de tokens no validos
# almacenandolos en una lista.
def t_error(t):
    temp = "Error: Unexpected character "+str(t.value[0])+" in row "+str(row)+", column "+ str(t.lexpos+1)
    errToks.append(temp)
    t.lexer.skip(1)

def imprimir():
    if len(errToks) != 0:
        for i in range(len(errToks)):
            if str(errToks[i])!="":
                print (errToks[i])
    else:    
        for i in range(len(arrToks)):
            if str(arrToks[i])!= "":
                print (arrToks[i])

# Funcion: inputError
#Return:
#   -True si existe parametro de entrada desde terminal
#   -False en caso contrario
def inputError():
    if (len(sys.argv)==2):
        return True
    else:
        return False

# Funcion: exist_File
# Entrada:
#   -String que representa el nombre de un archivo
# Return:
#   -True si existe un archivo con el nombre ingresado
#   -False en caso contrario

def exist_File(fname):
    if (os.path.isfile(fname)):
        return True
    else:
        return False

# Build the lexer
lex.lex()
#Funcion Principal main
def main():
    if (inputError()):
        first_arg = sys.argv[1]
        if (exist_File(first_arg)):
            if (first_arg.endswith('.gusb')):
                archivo = open(first_arg)
                linea= archivo.readline()
                contador = 0
                global row 
                while linea != '':
	                # procesar linea
                    lex.input(linea)
                    row= row + 1
                    arrToks.append("")

                    while True:
                        tok = lex.token()
                        if not tok or tok.type == "TkComments" : break

                        else:
                            col = tok.lexpos + 1
                            if tok.type == "TkId":
                                temp = str(tok.type)+"(\""+str(tok.value)+"\")"+" "+str(row)+" "+str(col)
                                arrToks.append(temp)

                            elif tok.type == "TkString":
                                temp = str(tok.type)+"("+str(tok.value)+")"+" "+str(row)+" "+str(col)
                                arrToks.append(temp)

                            elif tok.type == "TkNum":
                                temp = str(tok.type)+"("+str(tok.value)+")"+" "+str(row)+" "+str(col)
                                arrToks.append(temp)

                            elif tok.type == "TkUminus":
                                temp = str(tok.type)+"(\""+str(tok.value)+"\")"+" "+str(row)+" "+str(col)
                                arrToks.append(temp)

                            else:
                                temp = str(tok.type)+" "+str(row)+" "+str(col)
                                arrToks.append(temp)
                    contador +=1
                    linea=archivo.readline()
                imprimir()
            
            else:
                print("El archivo pasado no es un programa de GuardedUSB dado que no tiene la extensión .gusb")
        
        else:
            print("IOError: el archivo \""+str(first_arg)+"\" no se encuentra en el directorio actual") 
    else:
        print("Error: Entrada vacia")

if __name__ == '__main__':
      main()
