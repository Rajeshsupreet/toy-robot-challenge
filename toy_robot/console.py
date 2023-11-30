import re

from toy_robot import action


def start_program() -> None:
    action.start_new_session()

    while True:
        try:
            user_input = input("Please enter a command: ")
            user_input = user_input.strip().upper()
            if user_input == "LEFT":
                action.turn_left()
            elif user_input == "RIGHT":
                action.turn_right()
            elif user_input == "MOVE":
                action.move()
                input_dict = matches.groupdict()

                x = int(input_dict["x"])
                y = int(input_dict["y"])
                facing = Direction[input_dict["facing"]]

                action.place(x, y, facing)
            elif user_input == "REPORT":
                print(action.report())
            else:
                print("Invalid input Could you please try again?")
        except (InvalidPositionError, RobotHasNotBeenPlacedError):
            print("Ignored the command since it is an invalid move")
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(f"Unknown error: {e}")
