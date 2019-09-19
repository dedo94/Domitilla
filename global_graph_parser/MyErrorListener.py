from antlr4.error.ErrorListener import ErrorListener
import kivy
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MyErrorListener(ErrorListener):
    '''
    MyErrorListener redirect Parsing Errors from stdout
    (normal behaviour of DefaultErrorListener)
    to pop-up in Domitilla
    '''

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        title = 'InputError in [line: ' + str(line) + ',column: ' + str(column) + ']'
        content = msg + '\n\nClick outside for dismiss.'
        pop = Popup(title=title,
                    content=Label(text=content),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
        raise Exception("syntaxError")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("reportAmbiguity")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("reportAttemptingFullContext")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("reportContextSensitivity")