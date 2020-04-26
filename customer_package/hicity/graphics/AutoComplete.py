import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion


class CNameCompleter(Completer):
    CNamePool = []
    completionCache = []

    def __init__(self, CNamePool):
        self.CNamePool = CNamePool

    def prepare_completions(self, text):
        """
        If the text is a prefix for some city names, these names will be the result
        otherwise it turns to be the most similar one among the names
        """
        self.completionCache = []
        for item in self.CNamePool:
            if item.startswith(text):
                self.completionCache.append(item)
        if len(self.completionCache) == 0:
            self.completionCache = difflib.get_close_matches(text, self.CNamePool)

    def get_completions(self, *args):
        """
        Following the rules in 'prepare_completions', return completions
        """
        document = args[0]
        if len(args) == 2:
            document = document.text_before_cursor
        self.prepare_completions(document)
        for item in self.completionCache:
            yield Completion(item, start_position=-len(document))


if __name__ == '__main__':
    """ Unit Tests """
    pool = ['沈阳', '北京', '上海', '深圳']
    completer = CNameCompleter(pool)
    while True:
        prompt(completer=completer, complete_while_typing=True)
