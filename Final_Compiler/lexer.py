import ply.lex as lex

tokens = (
    "PUNTO_COMA",
    "PARENTESIS_IZQUIERDO",
    "PARENTESIS_DERECHO",
    "LLAVE_IZQUIERDA",
    "LLAVE_DERECHA",
    "NUMERO",
    "IDENTIFICADOR",
    "STRING",
    "OPERADOR_ASIGNACION",
    "OPERADOR_SUMA",
    "PALABRA_RESERVADA",
    "ASIGNACION",
    "SUMA",
    "RESTA",
    "MULTIPLICACION",
    "DIVISION",
    "MENOR_MENOR",
    "CONSTANTE",
    "MENORQUE",
    "MAYORQUE",
    "PREPROCESSOR",
    "CONSTANTE",
    

)


t_ignore = ' \t\n'

def t_PUNTO_COMA(t):
    r'\;'
    return t

def t_PARENTESIS_IZQUIERDO(t):
    r'\('
    return t

def t_PARENTESIS_DERECHO(t):
    r'\)'
    return t

def t_LLAVE_IZQUIERDA(t):
    r'\{'
    return t

def t_LLAVE_DERECHA(t):
    r'\}'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_MAYORQUE(t):
    r'>'
    return t

def t_MENORQUE(t):
    r'<'
    return t

def t_PALABRA_RESERVADA(t):
    r'main|for|if|else|while|do|break|continue|return|switch|case|default|try|catch|char|class|const|delete|auto|else|friend|float|long|new|operator|private|protected|public|short|signed|sizeof|static|struct|template|this|throw|union|unsigned|virtual|void|volatile|goto|enum|extern|inline|register|typedef|typeid|using|namespace|std|cin|cout|endl|int'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_ASIGNACION(t):
    r'='
    return t

def t_SUMA(t):
    r'\+'
    return t

def t_RESTA(t):
    r'-'
    return t

def t_MULTIPLICACION(t):
    r'\*'
    return t

def t_DIVISION(t):
    r'/'
    return t

def t_MENOR_MENOR(t):
    r'<<'
    return t

def t_STRING(t):
    r'\".*?\"'
    return t    

def t_PREPROCESSOR(t):
    r'\#.*'
    return t

def t_CONSTANTE(t):
    r'[A-Z_][A-Z0-9_]*'
    return t


def t_error(t):
    print("Error léxico: '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


with open('testinput.cpp', 'r') as file:
    codigo = file.read()

lexer.input(codigo)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
