import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        if balls == None:
            return "No balls"
        self.contents = []
        for item in balls:
            self.contents = self.contents + [item]*balls[item]
        #print(self.contents)

    def draw(self, num_balls):
        removedballs = []
        if num_balls >= len(self.contents):
            removedballs = self.contents
            self.contents = []
        else:
            while num_balls > 0:
                toremove = random.choice(self.contents)
                removedballs.append(toremove)
                self.contents.pop(self.contents.index(toremove))
                num_balls -= 1
                #print(toremove)
        return removedballs
        #print(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expectedballs = []
    count = 0
    for item in expected_balls:
        expectedballs = expectedballs + [item]*expected_balls[item]
    #print(expectedballs)
    for experi in range(num_experiments):
        hatinstance = copy.deepcopy(hat)
        ballsdraw = hatinstance.draw(num_balls_drawn)
        experimentresult = True
        #print("newexperiment")
        for i in expectedballs:
            if i in ballsdraw:
                ballsdraw.remove(i)
            else:
                experimentresult = False
        if experimentresult == True:
            count +=1

        #print(expectedballs)
    probability = count / num_experiments
    return probability
