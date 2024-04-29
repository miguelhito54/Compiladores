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

def p_expression_plus(p):
    'expression : expression SUMA expression'
    p[0] = ('plus', p[1], p[3])

def p_expression_minus(p):
    'expression : expression RESTA expression'
    p[0] = ('minus', p[1], p[3])    

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

def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])

def p_expression_parenthesis(p):
    'expression : PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO'
    p[0] = p[2]

def p_expression_mayorque(p):
    'expression : expression MAYORQUE expression'
    p[0] = ('mayorque', p[1], p[3])

def p_expression_menorque(p):
    'expression : expression MENORQUE expression'
    p[0] = ('menorque', p[1], p[3])

def p_preprocessor_ignore(p):
    'preprocessor : PREPROCESSOR'
    pass

def p_error(p):
    print("Syntax error at '%s'" % p.value)


with open('testinput.cpp', 'r') as file:
    codigo = file.read()

parser = yacc.yacc()

result = parser.parse(codigo, lexer=lexer)
print(result)