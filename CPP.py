INT = 'INT'
FLOAT = 'FLOAT'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'

DIGITS = '0123456789'

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details 
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class illegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class Token:
    def __init__(self, type, value = None):
        self.type = type_ 
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f"{self.type}"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos.idx] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(PLUS, self.current_char))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS, self.current_char))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL, self.current_char))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV, self.current_char))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAREN, self.current_char))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAREN, self.current_char))
                self.advance()
            else:
                pos_start = self.pos.copy()

                char = self.current_char
                self.advance()
                return [], illegalCharError(pos_start, self.pos, "'" + char + "'")
        return tokens
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error