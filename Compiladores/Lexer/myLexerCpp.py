import shlex

def lexer(input):
    lexer = shlex.shlex(input)
    lexer.wordchars += '.'
    lexer.whitespace = ' '
    lexer.commenters = ''
    lexer.quotes = ''
    lexer.escape = ''
    lexer.quotes = ''
    lexer.commenters = ''
    lexer.whitespace_split = True
    return list(lexer)




CppWords = [
"auto",
"else",
"long",
"switch",
"break",
"enum",	
"register",	
"typedef",
"case",	
"extern",	
"return",
"union",
"char",
"float",	
"short",	
"unsigned",
"const",	
"for", 
"signed",	
"void",
"continue",	
"goto",
"sizeof",	
"volatile",
"default",	
"if",	
"static",	
"while",
"do",	
"int",	
"struct",	
"_Packed",
"double",
]