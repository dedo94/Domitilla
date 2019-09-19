import platform
from global_graph_parser.G_grammarListener import G_grammarListener
from graphviz import Digraph


class MyListener(G_grammarListener):
    """
    There are 2 methods (enter and exit) for each rule of the grammar.
    As the walker encounters the node for rule Choice, for example,
    it triggers enterChoice(). After the walker visits all children
    of the Choice node, it triggers exitChoice().

    NOTE: For our purpose, we can't do anything in enter methods
    (except for the enterInit), so we'll leave empty. We need to
    go down in parse tree and store informations in stack, before
    we'll be able to build the graph.
    """

    def __init__(self, graph_name):

        self.graph_name = graph_name
        self.stack = []     # in stack we save some informations meanwhile we walk between nodes.
        self.count = 0      # needed to number each node
        self.g = Digraph(graph_name, filename=graph_name, format='pdf')     # initializes graph

        # some stuff to recognize location where we'll save the graph.
        path_file = open("path.txt", 'r')
        paths = []
        for line in path_file:
            paths.append(line.strip())
        path_file.close()
        # Windows
        if platform.system() == "Windows":
            pass
        # macOs
        if platform.system() == "Darwin":
            self.path = paths[0]
        # Linux
        if platform.system() == "Linux":
            self.path = paths[1]

    # Enter a parse tree produced by a Init production.
    def enterInit(self, ctx):
        self.g.node(str(self.count), label="", shape="circle")      # start node
        self.count += 1

    # Exit a parse tree produced by a Init production.
    def exitInit(self, ctx):
        node = self.stack.pop()
        self.g.edge("0", str(node[1]))
        self.g.edge(str(node[2]), str(self.count))
        self.g.node(str(self.count), label="", shape="doublecircle")        # end node
        self.g.view(self.graph_name, self.path, False)      # draw the graph

    # Enter a parse tree produced by a interaction production.
    def enterInteraction(self, ctx):
        pass

    # Exit a parse tree produced by a interaction production.
    def exitInteraction(self, ctx):
        node = ['interaction', self.count, self.count]
        self.stack.append(node)
        self.count += 1
        self.g.node(str(node[1]), label=ctx.getText(), shape="rect")

    # Enter a parse tree produced by a Sequential production.
    def enterSequential(self, ctx):
        pass

    # Exit a parse tree produced by a Sequential production.
    def exitSequential(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        node = ['sequential', left[1], right[2]]
        self.stack.append(node)
        self.g.edge(str(left[2]), str(right[1]))

    # Enter a parse tree produced by a Choice production.
    def enterChoice(self, ctx):
        pass

    # Exit a parse tree produced by a Choice production.
    def exitChoice(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if left[0] == 'choice':
            # in the case we have 3 or more choice nested,
            # we'll merge together with the same start node
            # and end node. If this behaviour is not required,
            # just commented out this if-statement.
            node = ['choice', left[1], left[2]]
            self.stack.append(node)
            self.g.edge(str(left[1]), str(right[1]))
            self.g.edge(str(right[2]), str(left[2]))
        else:
            choice_node_start = str(self.count)
            self.count += 1
            choice_node_end = str(self.count)
            self.count += 1
            node = ['choice', choice_node_start, choice_node_end]
            self.stack.append(node)
            self.g.node(choice_node_start, label="+", shape="diamond")
            self.g.edge(choice_node_start, str(left[1]))
            self.g.edge(choice_node_start, str(right[1]))
            self.g.node(choice_node_end, label="+", shape="diamond")
            self.g.edge(str(left[2]), choice_node_end)
            self.g.edge(str(right[2]), choice_node_end)

    # Enter a parse tree produced by a fork production.
    def enterFork(self, ctx):
        pass

    # Exit a parse tree produced by a fork production.
    def exitFork(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if left[0] == 'fork':
            # in the case we have 3 or more fork nested,
            # we'll merge together with the same start node
            # and end node. If this behaviour is not required,
            # just commented out this if-statement.
            node = ['fork', left[1], left[2]]
            self.stack.append(node)
            self.g.edge(str(left[1]), str(right[1]))
            self.g.edge(str(right[2]), str(left[2]))
        else:
            fork_node_start = str(self.count)
            self.count += 1
            fork_node_end = str(self.count)
            self.count += 1
            node = ['fork', fork_node_start, fork_node_end]
            self.stack.append(node)
            self.g.node(fork_node_start, label="|", shape="square")
            self.g.edge(fork_node_start, str(left[1]))
            self.g.edge(fork_node_start, str(right[1]))
            self.g.node(fork_node_end, label="|", shape="square")
            self.g.edge(str(left[2]), fork_node_end)
            self.g.edge(str(right[2]), fork_node_end)

    # Enter a parse tree produced by a loop production.
    def enterLoop(self, ctx):
        pass

    # Exit a parse tree produced by a loop production.
    def exitLoop(self, ctx):
        node_to_loop = self.stack.pop()
        loop_node_start = str(self.count)
        self.count += 1
        loop_node_end = str(self.count)
        self.count += 1
        node = ['loop', loop_node_start, loop_node_end]
        self.stack.append(node)
        self.g.node(loop_node_start, label="+", shape="diamond")
        self.g.edge(loop_node_start, str(node_to_loop[1]))
        self.g.node(loop_node_end, label="+", shape="diamond")
        self.g.edge(str(node_to_loop[2]), loop_node_end)
        self.g.edge(loop_node_end, loop_node_start)

    # Enter a parse tree produced by a Parenthesis production.
    def enterParenthesis(self, ctx):
        pass

    # Exit a parse tree produced by a Parenthesis production.
    def exitParenthesis(self, ctx):
        pass
