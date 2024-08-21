import copy
import random

class Hat:
    __slots__ = ('contents', 'init_colors')

    def __init__(self, **colors):
        self.contents = [color for color in colors for num in range(colors[color])]
        self.init_colors = colors

    def __str__(self):
        output = ''
        for color in sorted(self.init_colors, key=self.init_colors.get, reverse=True):
            output += (f"{self.init_colors[color]} : {color}\n")
        return output

    def draw(self, num_to_draw):
        random_balls = []

        if num_to_draw > len(self.contents):
            random_balls = copy.deepcopy(self.contents)
            self.contents = []
        else:
            for _ in range(num_to_draw):
                random_balls.append(self.contents.pop(random.randrange(0, len(self.contents))))
        return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ball_matches = 0 

    for _ in range(num_experiments):
        test_hat = copy.deepcopy(hat).draw(num_balls_drawn)
        result = True
        for color in expected_balls:
            print(f"Color: {color}\nExpected: {expected_balls[color]}\ntest_hat: {test_hat}")
            matches = [ ball for ball in test_hat if ball == color]
            if len(matches) < expected_balls[color]:
                result = False
            print(f"{result}\n ")
        if result:
            ball_matches += 1
    print(ball_matches/ num_experiments)
    return ball_matches / num_experiments


hat1 = Hat(yellow=3, blue=2, green=4, red=3)
# hat1.draw(31)
# print(hat1.draw(31))
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat3)
hat = Hat(black=6, red=4, green=3)
probability = experiment(
                hat=hat,
                expected_balls={'red':2,'green':1},
                num_balls_drawn=5,
                num_experiments=20)
