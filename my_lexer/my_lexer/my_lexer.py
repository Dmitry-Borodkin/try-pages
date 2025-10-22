from pygments.lexer import RegexLexer
from pygments.token import *

class MyCustomLexer(RegexLexer):
    name = 'MyCustomLanguage'
    aliases = ['mycustom']
    filenames = ['*.my']

    tokens = {
        'root': [
            (r'\b(if|else|while|for)\b', Keyword),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'[0-9]+', Number.Integer),
            (r'"[^"]*"', String),
            (r'//.*$', Comment.Single),
            (r'\s+', Text),
            (r'.', Punctuation),
        ]
    }

