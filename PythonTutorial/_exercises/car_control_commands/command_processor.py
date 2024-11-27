
from commands import (StartCommand, StopCommand,
                      MoveCommand, HelpCommand, QuitCommand)


class CommandProcessor:
    """Command Processor (Handles user input and maps it to commands)"""
    def __init__(self, car):
        self.car = car
        self.commands = {
            "start": StartCommand(car),
            "stop": StopCommand(car),
            "left": MoveCommand(car, "left"),
            "right": MoveCommand(car, "right"),
            "forward": MoveCommand(car, "forward"),
            "backward": MoveCommand(car, "backward"),
            "help": HelpCommand(car),
            "quit": QuitCommand(),
        }

    def process_command(self, command):
        if command in self.commands:
            result = self.commands[command].execute()
            if result == "quit":
                return False  # Signal to quit the program
            print(result)
            return True
        else:
            print("Invalid command. Type 'help' for instructions.")
            return True
