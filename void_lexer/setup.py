from setuptools import setup, find_packages

setup(
    name='voidlexerpackage',
    packages=find_packages(),
    entry_points="""
        [pygments.lexers]
        voidlexer = void_lexer.void_lexer:VoidLexer
    """,
)

