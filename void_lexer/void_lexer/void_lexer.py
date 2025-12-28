from pygments.lexer import RegexLexer
from pygments.token import *

class VoidLexer(RegexLexer):
    name = 'VoidLanguage'
    aliases = ['void']
    filenames = ['*.void']

    tokens = {
        'root': [
            (r'#[a-zA-Z0-9_]+', Comment.Preproc),
            (r'\b(if|else|while|for|block|switch|case|break|continue|return|new|delete|const|volatile|defer|struct|union|namespace)\b', Keyword),
            (r'\b(void|bool|char|short|int|unsigned|long|long_long|intptr_t|size_t|char32_t|uint64_t)\b', Keyword.Type),
            (r'\b(true|false|_WIN32|NDEBUG)\b', Keyword.Constant),
            (r'\b(undef)\b', Keyword.Pseudo),
            (r'(v_|voidc_)[a-zA-Z0-9_]+', Name.Builtin),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'[0-9]+', Number.Integer),
            (r'("""(?:.|\n)*?""")', String),
            (r'"', String, 'string'),
            (r"'", String.Char, 'char'),
            (r'//.*$', Comment.Single),
            (r'\s+', Text),
            (r'.', Punctuation),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\[\\nrt"\']', String.Escape),
            (r'[^\\"\'\n\r\t]+', String),  # all other characters
        ],
        'char': [
            (r"'", String.Char, '#pop'),
            (r"\\[\\nrt\"']", String.Escape),
            (r"[^\\'\"\n\r\t]+", String.Char),  # all other characters
        ],



    }

