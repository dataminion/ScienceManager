from .workflow import Workflow


class Configuration(object):
    """ A model for configuration data """
    def __init__(self):
        self.workflow = Workflow()

    def set_config(self):
        pass

    def set_args(self, args):
        pass