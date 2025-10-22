from setuptools import setup, find_packages

setup(
    name='mylexerpackage',
    packages=find_packages(),
    entry_points="""
        [pygments.lexers]
        mycustomlexer = my_lexer.my_lexer:MyCustomLexer
    """,
)
