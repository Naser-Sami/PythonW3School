
from abstact_command_class import Command


class StartCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        return self.car.start()


class StopCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        return self.car.stop()


class MoveCommand(Command):
    def __init__(self, car, direction):
        self.car = car
        self.direction = direction

    def execute(self):
        return self.car.move(self.direction)


class HelpCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        return self.car.help()


class QuitCommand(Command):
    def execute(self):
        return "quit"
