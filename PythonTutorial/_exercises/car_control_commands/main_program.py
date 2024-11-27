
from car_class import Car
from command_processor import CommandProcessor

# Applying the task using the S.O.L.I.D principles


def main():
    car = Car()
    processor = CommandProcessor(car)

    print("Enter a command or type 'help':")
    while True:
        command = input("> ").strip().lower()
        if not processor.process_command(command):
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
