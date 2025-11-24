from textx import metamodel_from_file


# interpretiranje modela
class Robot(object):

    def __init__(self):
        # Initial position is (0,0)
        self.x = 0
        self.y = 0

    def __str__(self):
        return "Robot position is {}, {}.".format(self.x, self.y)

    def interpret(self, model):
        possible_moves = {
            "up": (0, 1),
            "down": (0, -1),
            "left": (-1, 0),
            "right": (1, 0)
        }
        # model je instanca klase (početnog pravila ) Program
        for c in model.commands:
            if c.__class__.__name__ == "InitialCommand":
                print("Setting position to: {}, {}".format(c.x, c.y))
                self.x = c.x
                self.y = c.y
            else:
                direction = c.direction
                print("Going {} for {} step(s).".format(direction, c.steps))
                move = possible_moves[direction]
                # Odrediti novu poziciju robota
                self.x += c.steps * move[0]
                self.y += c.steps * move[1]

            print(self)


def move_command_processor(move_cmd):
    # Pretpostavka je da parametar steps ima vrednost 0 samo ukoliko se
    # ne navede eksplicitno
    if move_cmd.steps == 0:
        move_cmd.steps = 1


if __name__ == '__main__':
    # instanciranje metamodela
    robot_mm = metamodel_from_file('robot.tx')
    # registrujemo funkciju koja ce postaviti podrazumevanu vrednost za korak MoveCommand-e
    robot_mm.register_obj_processors({'MoveCommand': move_command_processor})
    # instanciranje modela
    robot_model = robot_mm.model_from_file('example.robot')
    # interpretiranje
    robot = Robot()
    robot.interpret(robot_model)
