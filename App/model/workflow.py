#model.workflow


class Workflow(object):
    def __init__(self):
        self.id = None
        self.name = None
#TODO: look at lists
        self.tasks = {}
        self.batch_id = None


class Task(object):
    def __init__(self):
        self.task_num = None
        self.action = Action()


class Action(object):
    def __init__(self):
        self.name = None
        self.type_id = None
        self.text = None