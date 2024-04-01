import ply.yacc as yacc
from lexer import tokens, lexer

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    'statements : statement statements'
    p[0] = [p[1]] + p[2]

def p_statements_empty(p):
    'statements : '
    p[0] = []

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | print'''
    p[0] = p[1]

def p_declaration(p):
    'declaration : PALABRA_RESERVADA IDENTIFICADOR PUNTO_COMA'
    p[0] = ('declaration', p[2])

def p_assignment(p):
    'assignment : IDENTIFICADOR ASIGNACION expression PUNTO_COMA'
    p[0] = ('assignment', p[1], p[3])

def p_expression(p):
    'expression : IDENTIFICADOR'
    p[0] = ('identifier', p[1])

def p_print(p):
    'print : PALABRA_RESERVADA MENOR_MENOR expression PUNTO_COMA'
    p[0] = ('print', p[3])

def p_expression_number(p):
    'expression : NUMERO'
    p[0] = ('number', p[1])

def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()

codigo = """
int a;
int b;
a = 10;
b = 20;
cout << a;
cout << b;
"""

result = parser.parse(codigo, lexer=lexer)
print(result)