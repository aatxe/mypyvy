from typing import Any

class Parser:
    def parse(self, input: str=None, lexer: Any=None, debug: bool=False, tracking: bool=False, tokenfunc: Any=None, filename: str=None) -> Any: ...

def yacc(start: str=None) -> Parser: ...