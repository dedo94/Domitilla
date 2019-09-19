from global_graph_parser.G_grammarLexer import G_grammarLexer
from global_graph_parser.G_grammarParser import G_grammarParser
from global_graph_parser.MyErrorListener import MyErrorListener
from global_graph_parser.MyListener import MyListener
from antlr4 import *


def parse_and_draw(path, graph_name):
    """
     The purpose of this function is to take a string of the Structered Global Graph Grammar
     and to translate it in a dot (Unstructured Global Graph) file, then draw the graph (.pdf)
     """
    input_stream = FileStream(path)
    
    # tokenizes input into word (tokens)
    lexer = G_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    try:
        # parser these tokens to recognize the sentence structure
        # and build a parse tree
        parser = G_grammarParser(stream)
        parser.removeErrorListeners()  # remove DefaultErrorListener
        parser.addErrorListener(MyErrorListener())  # add MyErrorListener (See MyErrorListener.py)
        tree = parser.init()
        
        # "listener" is the mechanism through we visit
        # each node of parse tree and draw the graph
        listener = MyListener(graph_name)   # (See MyListener.py)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    except:
        pass
