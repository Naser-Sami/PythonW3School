
class Car:
    """Car Class (Encapsulates the car state and actions)"""

    def __init__(self):
        self.started = False

    def start(self):
        if self.started:
            return "Car is already started."

        self.started = True
        return "Car started."

    def stop(self):
        if not self.started:
            return "Car is already stopped."
        self.started = False
        return "Car stopped."

    def move(self, direction):
        if not self.started:
            return "Cannot move the car while it's not started."
        return f"Car moved {direction}"

    @staticmethod
    def help():
        return (
            "Command:\n"
            "start      - Start the car\n"
            "stop       - Stop the car\n"
            "left       - Move the car left\n"
            "right      - Move the car right\n"
            "forward    - Move the car forward\n"
            "backward   - Move the car backward\n"
            "help       - Display all instructions with descriptions\n"
            "quit       - Exit the program"
        )
