# Generated from SimpleLang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,21,128,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,13,1,13,1,14,4,14,77,8,14,11,14,12,14,78,1,15,4,15,82,
        8,15,11,15,12,15,83,1,15,1,15,5,15,88,8,15,10,15,12,15,91,9,15,1,
        16,1,16,5,16,95,8,16,10,16,12,16,98,9,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,115,8,18,
        1,19,3,19,118,8,19,1,19,1,19,1,20,4,20,123,8,20,11,20,12,20,124,
        1,20,1,20,1,96,0,21,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,
        21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,
        1,0,2,1,0,48,57,2,0,9,9,32,32,134,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,1,43,1,0,0,0,3,45,1,0,
        0,0,5,47,1,0,0,0,7,49,1,0,0,0,9,51,1,0,0,0,11,53,1,0,0,0,13,55,1,
        0,0,0,15,57,1,0,0,0,17,59,1,0,0,0,19,62,1,0,0,0,21,65,1,0,0,0,23,
        68,1,0,0,0,25,71,1,0,0,0,27,73,1,0,0,0,29,76,1,0,0,0,31,81,1,0,0,
        0,33,92,1,0,0,0,35,101,1,0,0,0,37,114,1,0,0,0,39,117,1,0,0,0,41,
        122,1,0,0,0,43,44,5,42,0,0,44,2,1,0,0,0,45,46,5,47,0,0,46,4,1,0,
        0,0,47,48,5,43,0,0,48,6,1,0,0,0,49,50,5,45,0,0,50,8,1,0,0,0,51,52,
        5,37,0,0,52,10,1,0,0,0,53,54,5,94,0,0,54,12,1,0,0,0,55,56,5,60,0,
        0,56,14,1,0,0,0,57,58,5,62,0,0,58,16,1,0,0,0,59,60,5,60,0,0,60,61,
        5,61,0,0,61,18,1,0,0,0,62,63,5,62,0,0,63,64,5,61,0,0,64,20,1,0,0,
        0,65,66,5,61,0,0,66,67,5,61,0,0,67,22,1,0,0,0,68,69,5,33,0,0,69,
        70,5,61,0,0,70,24,1,0,0,0,71,72,5,40,0,0,72,26,1,0,0,0,73,74,5,41,
        0,0,74,28,1,0,0,0,75,77,7,0,0,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,
        1,0,0,0,78,79,1,0,0,0,79,30,1,0,0,0,80,82,7,0,0,0,81,80,1,0,0,0,
        82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,89,5,
        46,0,0,86,88,7,0,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,
        90,1,0,0,0,90,32,1,0,0,0,91,89,1,0,0,0,92,96,5,34,0,0,93,95,9,0,
        0,0,94,93,1,0,0,0,95,98,1,0,0,0,96,97,1,0,0,0,96,94,1,0,0,0,97,99,
        1,0,0,0,98,96,1,0,0,0,99,100,5,34,0,0,100,34,1,0,0,0,101,102,5,39,
        0,0,102,103,9,0,0,0,103,104,5,39,0,0,104,36,1,0,0,0,105,106,5,116,
        0,0,106,107,5,114,0,0,107,108,5,117,0,0,108,115,5,101,0,0,109,110,
        5,102,0,0,110,111,5,97,0,0,111,112,5,108,0,0,112,113,5,115,0,0,113,
        115,5,101,0,0,114,105,1,0,0,0,114,109,1,0,0,0,115,38,1,0,0,0,116,
        118,5,13,0,0,117,116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,
        120,5,10,0,0,120,40,1,0,0,0,121,123,7,1,0,0,122,121,1,0,0,0,123,
        124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,
        127,6,20,0,0,127,42,1,0,0,0,8,0,78,83,89,96,114,117,124,1,6,0,0
    ]

class SimpleLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    INT = 15
    FLOAT = 16
    STRING = 17
    CHAR = 18
    BOOL = 19
    NEWLINE = 20
    WS = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'%'", "'^'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'!='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "STRING", "CHAR", "BOOL", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "INT", "FLOAT", "STRING", "CHAR", "BOOL", "NEWLINE", "WS" ]

    grammarFileName = "SimpleLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


