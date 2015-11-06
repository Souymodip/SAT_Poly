__author__ = 'souy'
import lex

s = set()

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'TIMES',
    'LEQ',
    'GEQ',
    'EQ',
    'VAR'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LEQ     = r'<='
t_GEQ     = r'>='
t_EQ      = r'\='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+[.| ]+[0-9]*'
    t.value = float(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    s.add(t.value)
   # t.type = reserved.get(t.value,'ID')    # Check for reserved words
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

d = "3.0"
lexer.input(d)

'''
# Test it out
data = "x3 >= 20.2"


# Give the lexer some input
lexer.input(data)

print ("THIS!")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)


print (s)

'''