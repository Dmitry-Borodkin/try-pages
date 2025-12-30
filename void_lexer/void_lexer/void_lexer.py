from pygments.lexer import RegexLexer, words
from pygments.token import *

class VoidLexer(RegexLexer):
    name = 'VoidLanguage'
    aliases = ['void']
    filenames = ['*.void']

    _hex_digits = r'[0-9a-fA-F](\'?[0-9a-fA-F])*'
    _dec_digits = r'[0-9](\'?[0-9])*'
    _bin_digits = r'[01](\'?[01])*'

    _int_suffix  = r'([iIuU]([1-9][0-9]*)?)?'
    _real_suffix = r'([fF]([1-9][0-9]*)?)?'

    tokens = {
        'root': [
            (r'#[a-zA-Z0-9_]+', Comment.Preproc),
            (words(('if', 'else', 'block', 'loop', 'while', 'for',
                    'switch', 'case', 'break', 'continue', 'return',
                    'const', 'volatile', 'defer', 'export', 'private',
                    'inlinehint', 'alwaysinline', 'struct', 'union',
                    'derive', 'new', 'delete', 'namespace', 'using'),
                    prefix=r'\b', suffix=r'\b'), Keyword),
            (words(('void', 'bool', 'char', 'short', 'int', 'unsigned', 'long', 'long_long',
                    'intptr_t', 'size_t', 'char32_t', 'uint64_t',
                    'uint', 'float', 'vec', 'svec'),
                    prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (r'\b(true|false|_WIN32|NDEBUG)\b', Keyword.Constant),
            (r'\b(undef)\b', Keyword.Pseudo),
            (r'(v|voidc)_[a-zA-Z0-9_]+', Name.Builtin),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),

            (r'[-+]?0[xX](' + _hex_digits + r'\.' + _hex_digits + r'|\.' + _hex_digits +
             r'|' + _hex_digits + r')[pP][+-]?' + _dec_digits + _real_suffix, Number.Float),

            (r'[-+]?(' + _dec_digits + r'\.' + _dec_digits + r'|\.' + _dec_digits + r'|' +
             _dec_digits + r')[eE][+-]?' + _dec_digits + _real_suffix, Number.Float),

            (r'[-+]?((' + _dec_digits + r'\.(' + _dec_digits + r')?|\.' +
             _dec_digits + r')' + _real_suffix + r')|(' + _dec_digits + r'[fF]([1-9][0-9]*)?)', Number.Float),

            (r'[-+]?0[xX]' + _hex_digits + _int_suffix, Number.Hex),
            (r'[-+]?0[bB]' + _bin_digits + _int_suffix, Number.Bin),
            (r'[-+]?0(\'?[0-7])*'        + _int_suffix, Number.Oct),
            (r'[-+]?'      + _dec_digits + _int_suffix, Number.Integer),

            (r'("""(?:.|\n)*?""")', String),
            (r'"', String, 'string'),
            (r"'(\\[\\nrt\"']|[^\\'\"\n\r\t])'", String.Char),

            (r"\{'[a-zA-Z_][a-zA-Z0-9_]*[^\n\r\t\']*'", Comment.Preproc),
            (r"'[a-zA-Z_][a-zA-Z0-9_]*[^\n\r\t\']*'\}", Comment.Preproc),

            (r'//.*$', Comment.Single),
            (r'\s+', Text),                 # ?
            (r'.', Punctuation),            # ?
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\[\\nrt"\']', String.Escape),
            (r'[^\\"\'\n\r\t]+', String),  # all other characters
        ],
    }

