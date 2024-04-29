from pycparser import c_parser, c_ast, parse_file

archivo = './input.cpp'

ast = parse_file(archivo, use_cpp=True)

print(ast)