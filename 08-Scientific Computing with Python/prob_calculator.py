import copy
import random

class Hat:
    def __init__(self, **hats) -> None:
        self.hats = dict( filter( lambda x : x[1]>0, hats.items() ) )
        self.contents = list( self.hats.keys() )
        self.hats_copy = copy.deepcopy( self.hats )
    def draw(self):
        if len(self.contents) == 0:
            self.hats = copy.deepcopy( self.hats_copy )
            self.contents = list( self.hats.keys() )
        ball_color = self.contents[ int(random.random() * len(self.contents)) ]
        self.hats[ball_color] -= 1
        if self.hats[ball_color] == 0:
            self.contents.pop( self.contents.index(ball_color) )
        return ball_color

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    draw_succes = 0

    for experiments in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_balls_copy = copy.deepcopy(expected_balls)
        for draw in range(num_balls_drawn):
            ball_color = hat_copy.draw()
            if ball_color in expected_balls_copy and expected_balls_copy[ball_color] > 0:
                expected_balls_copy[ball_color] -= 1
                if expected_balls_copy[ball_color] == 0:
                    expected_balls_copy.pop(ball_color)
                if len(expected_balls_copy) == 0:
                    draw_succes += 1
                    break
    return draw_succes / num_experiments



if __name__=='__main__':
    # hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=3)

    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                    expected_balls={"red":2,"green":1},
                    num_balls_drawn=5,
                    num_experiments=2000)

    print(probability)
    pass

