def get_task(name, file=None):
    if name == 'game24':
        from .game24 import Game24Task
        return Game24Task(file)
    elif name == 'text':
        from .text import TextTask
        return TextTask(file)
    elif name == 'crosswords':
        from .crosswords import MiniCrosswordsTask
        return MiniCrosswordsTask(file)
    else:
        raise NotImplementedError