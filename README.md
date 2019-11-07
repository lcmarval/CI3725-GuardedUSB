


<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">GuardUSB</h3>

  <p align="center">
    Interprete de Lenguaje realizado, por profesores de la materia 
    Traductores e Interpretadores de Universidad Simon Bolivar (USB) 
    Proyecto del curso.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

  Proyecto del Curso CI-3725 para el trimestre Septiembre-Diciembre 2019

  Función: Analizador lexicográfico del lenguaje GuardedUSB

  En esta etapa se reconocen los tokens y posibles errores de estos

  Adicionalmente se revisa la gramatica del lenguaje, 

  generando el arbol sintactico del programa pasado.

  En el archivo txt se ofrece la representación de la gramática resultante para el lenguaje GuardedUSB. 

  Para esta entrega a pesar de realizar varias modificaciones, 

  no se logró desarrollar una gramática que a la hora de ser implementada con la librería Ply cubriera a 

  completitud las restricciones del parser para dicho lenguaje.

  Dentro del comprimido se entregan algunos de los programas que funcionan con la gramática propuesta.


### Built With

* [Python3](Python3)
* [Ply](Ply)
* []()



<!-- GETTING STARTED -->
## Getting Started

  Follow this steps

### Prerequisites

Python 3 must be installed. Ply its provided in the folder.

### Installation
 
No Further needed


<!-- USAGE EXAMPLES -->
## Usage

Write your program in GuardedUSB, 
you can run the lexer to see Tokens recognized,
you can run the parser to see the AST.

```sh
Python3 lexer.py yourProgram.gusb
```

```sh
Python3 parser.py yourProgram.gusb
```
Despues de ser ejecutada dicha instrucción, 

en caso de ser correcto imprime la estructura del programa ejecutado

en un arbol.

<!-- CONTACT -->
## Contact

Luis Carlos Marval - 12-10620 - luiscarm77@gmail.com 

Fabio Suarez - 12-10578 - fadasgo@gmail.com

