tokens = (
    'ATOM',
    'NOT', 'AND', 'OR', 'IF', 'THEN', 'ELSE', 'IFF',
    'LPAREN', 'RPAREN',
)

t_ATOM = r'[a-zA-Z_0-9][a-zA-Z_0-9]*'
t_NOT = r'¬'
t_AND = r'∧'
t_OR = r'∨'
t_IF = r'if'
t_THEN = r'→'
t_ELSE = r'else'
t_IFF = r'↔'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

