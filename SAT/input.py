__author__ = 'souy'

#import Equation

import ply.yacc as yacc

from parser import tokens
import re



'''
def p_equation_le(p):
    'equation : expression LEQ NUMBER'
    p[0] = Equation.Eq(p[1],'<=',p[3])

def p_equation_ge(p):
    'equation : expression GEQ NUMBER'
    p[0] = Equation.Eq(p[1],'>=',p[3])

def p_equation_eq(p):
    'equation : expression EQ NUMBER'
    p[0] = Equation.Eq(p[1],'=',p[3])




def p_expression_plus(p):
    'expression : term PLUS expression'
    p[0] = p[1].append(p[3])


def p_expression_term(p):
    'expression : term'


def p_term_num(p):
    'term : NUMBER TIMES aterm'
    p[0] = Equation.Term(p[1],p[3])

def p_term(p):
    'term : aterm'
    p[0] = Equation.Term(1,p[1])



def p_aterm(p):
    'aterm : ID TIMES aterm'
    p[0]  = p[1].append(p[3])
'''


def p_aterm_num(p):
    'aterm : NUMBER'
    p[0] = p[1]

def p_aterm_var(p):
    'aterm : VAR'
    p[0] = re.split("[a-zA-Z]+",p[1])[-1]

# Error rule for syntax errors

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

data = "3.0"

result = parser.parse(data)

#result.show()

'''
while True:
   try:
   #    s = raw_input('calc > ')
    pass
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   #result.show()
   #print(result)
'''