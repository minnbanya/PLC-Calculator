from components.lexicalAnalyzer import MyLexer
from sly import Parser

class MyParserEval(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T[0], p.T[1], p.T[2]])
        return [p.T[0], p.T[1], p.T[2]]
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F[0], p.F[1], p.F[2]])
        return [p.F[0], p.F[1], p.F[2]]

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+'])
        return [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+']

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', p.E * p.T)
        return p.E * p.T
    
    @_('N')
    def F(self, p):
        print('F -> N', p.N)
        return p.N
    
class MyParserPrefix(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T[0], p.T[1], p.T[2]])
        return [p.T[0], p.T[1], p.T[2]]
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F[0], p.F[1], p.F[2]])
        return [p.F[0], p.F[1], p.F[2]]

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+'])
        return [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+']

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', [p.E[0] + p.T[0], f'*{p.E[1]}{p.T[1]}', f'{p.E[2]}{p.T[2]}*'])
        return f'*{p.E}{p.T}'
    
    @_('N')
    def F(self, p):
        print('F -> N', [p.N, p.N, p.N])
        return p.N
    
class MyParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T[0], p.T[1], p.T[2]])
        return [p.T[0], p.T[1], p.T[2]]
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F[0], p.F[1], p.F[2]])
        return [p.F[0], p.F[1], p.F[2]]

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+'])
        return [p.T[0] + p.F[0], f'+{p.T[1]}{p.F[1]}', f'{p.T[2]}{p.F[2]}+']

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', [p.E[0] + p.T[0], f'*{p.E[1]}{p.T[1]}', f'{p.E[2]}{p.T[2]}*'])
        return [p.E[0] * p.T[0], f'*{p.E[1]}{p.T[1]}', f'{p.E[2]}{p.T[2]}*']
    
    @_('N')
    def F(self, p):
        print('F -> N', [p.N, p.N, p.N])
        return [p.N, p.N, p.N]

if __name__ == "__main__":
    lexer = MyLexer()
    parser = MyParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Result:", result[0])
    print("Prefix:", result[1])
    print("Postfix:", result[2])
