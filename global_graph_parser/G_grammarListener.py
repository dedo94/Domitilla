# Generated from G_grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .G_grammarParser import G_grammarParser
else:
    from G_grammarParser import G_grammarParser

# This class defines a complete listener for a parse tree produced by G_grammarParser.
class G_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by G_grammarParser#init.
    def enterInit(self, ctx:G_grammarParser.InitContext):
        pass

    # Exit a parse tree produced by G_grammarParser#init.
    def exitInit(self, ctx:G_grammarParser.InitContext):
        pass


    # Enter a parse tree produced by G_grammarParser#fork.
    def enterFork(self, ctx:G_grammarParser.ForkContext):
        pass

    # Exit a parse tree produced by G_grammarParser#fork.
    def exitFork(self, ctx:G_grammarParser.ForkContext):
        pass


    # Enter a parse tree produced by G_grammarParser#loop.
    def enterLoop(self, ctx:G_grammarParser.LoopContext):
        pass

    # Exit a parse tree produced by G_grammarParser#loop.
    def exitLoop(self, ctx:G_grammarParser.LoopContext):
        pass


    # Enter a parse tree produced by G_grammarParser#sequential.
    def enterSequential(self, ctx:G_grammarParser.SequentialContext):
        pass

    # Exit a parse tree produced by G_grammarParser#sequential.
    def exitSequential(self, ctx:G_grammarParser.SequentialContext):
        pass


    # Enter a parse tree produced by G_grammarParser#interaction.
    def enterInteraction(self, ctx:G_grammarParser.InteractionContext):
        pass

    # Exit a parse tree produced by G_grammarParser#interaction.
    def exitInteraction(self, ctx:G_grammarParser.InteractionContext):
        pass


    # Enter a parse tree produced by G_grammarParser#choice.
    def enterChoice(self, ctx:G_grammarParser.ChoiceContext):
        pass

    # Exit a parse tree produced by G_grammarParser#choice.
    def exitChoice(self, ctx:G_grammarParser.ChoiceContext):
        pass


    # Enter a parse tree produced by G_grammarParser#parenthesis.
    def enterParenthesis(self, ctx:G_grammarParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by G_grammarParser#parenthesis.
    def exitParenthesis(self, ctx:G_grammarParser.ParenthesisContext):
        pass


