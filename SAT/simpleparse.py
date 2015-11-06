__author__ = 'souy'


# Yacc example

import ply.yacc as yacc
import re
import Equation

# Get the token map from the lexer.  This is required.
from simplelex import tokens

k=[]

def p_equation_leq(p):
    'equation : expression LEQ NUMBER'
    p[0] = Equation.Eq(p[1],'<=',[Equation.Term(p[3],[])])

def p_equation_geq(p):
    'equation : expression GEQ NUMBER'
    p[0] = Equation.Eq(p[1],'>=',[Equation.Term(p[3],[])])

def p_equation_eq(p):
    'equation : expression EQ NUMBER'
    p[0] = Equation.Eq(p[1],'=',[Equation.Term(p[3],[])])

def p_expression_plus(p):
    'expression : expression PLUS cterm'
    p[0] = p[1].append(p[3])

def p_expression_minus(p):
    'expression : expression MINUS cterm'
    p[3].cof = -1*p[3].cof
    p[0] = p[1].append(p[3])



def p_expression_cterm(p):
    'expression : cterm'
    p[0] = [p[1]]




def p_cterm_cof(p):
    'cterm : NUMBER TIMES A'
    p[0] = Equation.Term(p[1],k)


def p_A_var(p):
    'A : A TIMES VAR'
    p[0] = p[1].append(p[3])
    k.append(p[3])

def p_A(p):
    'A : VAR'
    p[0]=[p[1]]
    k.append(p[1])








# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

data = "2.0*x1*x2 = 8.0"

#print(data)
result = parser.parse(data)

print (k)
print(result)

#result.show()

#print(result)

'''
while True:
   try:
     #  s = raw_input('calc > ')
        pass
   except EOFError:
       break
   #if not s: continue
  # result = parser.parse(data)
   #print(result)
'''