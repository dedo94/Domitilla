# Generated from G_grammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("-\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\5\2\f\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\35\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3(\n")
        buf.write("\3\f\3\16\3+\13\3\3\3\2\3\4\4\2\4\2\2\2\60\2\13\3\2\2")
        buf.write("\2\4\34\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\f\3\2\2\2\t")
        buf.write("\n\7\3\2\2\n\f\7\2\2\3\13\6\3\2\2\2\13\t\3\2\2\2\f\3\3")
        buf.write("\2\2\2\r\16\b\3\1\2\16\17\7\r\2\2\17\20\7\4\2\2\20\21")
        buf.write("\7\r\2\2\21\22\7\5\2\2\22\35\7\16\2\2\23\24\7\t\2\2\24")
        buf.write("\25\5\4\3\2\25\26\7\n\2\2\26\27\7\r\2\2\27\35\3\2\2\2")
        buf.write("\30\31\7\13\2\2\31\32\5\4\3\2\32\33\7\f\2\2\33\35\3\2")
        buf.write("\2\2\34\r\3\2\2\2\34\23\3\2\2\2\34\30\3\2\2\2\35)\3\2")
        buf.write("\2\2\36\37\f\7\2\2\37 \7\6\2\2 (\5\4\3\b!\"\f\6\2\2\"")
        buf.write("#\7\7\2\2#(\5\4\3\7$%\f\5\2\2%&\7\b\2\2&(\5\4\3\6\'\36")
        buf.write("\3\2\2\2\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*")
        buf.write("\3\2\2\2*\5\3\2\2\2+)\3\2\2\2\6\13\34\')")
        return buf.getvalue()


class G_grammarParser ( Parser ):

    grammarFileName = "G_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'(o)'", "'->'", "':'", "';'", "'+'", 
                     "'|'", "'*'", "'@'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Partecipant", 
                      "Message", "WS" ]

    RULE_init = 0
    RULE_g = 1

    ruleNames =  [ "init", "g" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    Partecipant=11
    Message=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self):
            return self.getTypedRuleContext(G_grammarParser.GContext,0)


        def EOF(self):
            return self.getToken(G_grammarParser.EOF, 0)

        def getRuleIndex(self):
            return G_grammarParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)




    def init(self):

        localctx = G_grammarParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        try:
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G_grammarParser.T__6, G_grammarParser.T__8, G_grammarParser.Partecipant]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.g(0)
                self.state = 5
                self.match(G_grammarParser.EOF)
                pass
            elif token in [G_grammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(G_grammarParser.T__0)
                self.state = 8
                self.match(G_grammarParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G_grammarParser.RULE_g

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ForkContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(G_grammarParser.GContext)
            else:
                return self.getTypedRuleContext(G_grammarParser.GContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFork" ):
                listener.enterFork(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFork" ):
                listener.exitFork(self)


    class LoopContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def g(self):
            return self.getTypedRuleContext(G_grammarParser.GContext,0)

        def Partecipant(self):
            return self.getToken(G_grammarParser.Partecipant, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)


    class SequentialContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(G_grammarParser.GContext)
            else:
                return self.getTypedRuleContext(G_grammarParser.GContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequential" ):
                listener.enterSequential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequential" ):
                listener.exitSequential(self)


    class InteractionContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Partecipant(self, i:int=None):
            if i is None:
                return self.getTokens(G_grammarParser.Partecipant)
            else:
                return self.getToken(G_grammarParser.Partecipant, i)
        def Message(self):
            return self.getToken(G_grammarParser.Message, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteraction" ):
                listener.enterInteraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteraction" ):
                listener.exitInteraction(self)


    class ChoiceContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(G_grammarParser.GContext)
            else:
                return self.getTypedRuleContext(G_grammarParser.GContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoice" ):
                listener.enterChoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoice" ):
                listener.exitChoice(self)


    class ParenthesisContext(GContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G_grammarParser.GContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def g(self):
            return self.getTypedRuleContext(G_grammarParser.GContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)



    def g(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G_grammarParser.GContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_g, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [G_grammarParser.Partecipant]:
                localctx = G_grammarParser.InteractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(G_grammarParser.Partecipant)
                self.state = 13
                self.match(G_grammarParser.T__1)
                self.state = 14
                self.match(G_grammarParser.Partecipant)
                self.state = 15
                self.match(G_grammarParser.T__2)
                self.state = 16
                self.match(G_grammarParser.Message)
                pass
            elif token in [G_grammarParser.T__6]:
                localctx = G_grammarParser.LoopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(G_grammarParser.T__6)
                self.state = 18
                self.g(0)
                self.state = 19
                self.match(G_grammarParser.T__7)
                self.state = 20
                self.match(G_grammarParser.Partecipant)
                pass
            elif token in [G_grammarParser.T__8]:
                localctx = G_grammarParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(G_grammarParser.T__8)
                self.state = 23
                self.g(0)
                self.state = 24
                self.match(G_grammarParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = G_grammarParser.SequentialContext(self, G_grammarParser.GContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_g)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        self.match(G_grammarParser.T__3)
                        self.state = 30
                        self.g(6)
                        pass

                    elif la_ == 2:
                        localctx = G_grammarParser.ChoiceContext(self, G_grammarParser.GContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_g)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        self.match(G_grammarParser.T__4)
                        self.state = 33
                        self.g(5)
                        pass

                    elif la_ == 3:
                        localctx = G_grammarParser.ForkContext(self, G_grammarParser.GContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_g)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(G_grammarParser.T__5)
                        self.state = 36
                        self.g(4)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.g_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def g_sempred(self, localctx:GContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




