__author__ = 'souy'

import ply.lex as lex
import re

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'LEQ',
    'GEQ',
    'EQ',
    'VAR'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_LEQ     = r'<='
t_GEQ     = r'>='
t_EQ      = r'\='

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #s.add(t.value)
    t.value = int(re.split("[a-zA-Z]+",t.value)[-1])
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+[.| ]+[0-9]*'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer

lexer = lex.lex()

lexer.input("x1*x3 = 2")


# Test it out


# Give the lexer some input


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
