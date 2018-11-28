''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction



class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, GameState):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        

                

      #  self.random_next_move(gamestate)
        self.make_move(self,GameState)
    
    def make_move(self,GameState):
        bestscore=0
        
        bestdirection=0
        bestrotate=0
        for y in range (4):
            for x in range (-1.9,1):
                clone = GameState.clone(True)
                while True:
                    currentposition = clone.get_falling_block_position()[0]
                    currentrotate = clone.get_falling_block_angle()

                    if GameState.get_falling_block_position()[0] < 5:
                        if GameState.get_falling_block_position()[0] > x:
                            clone.move(Direction.left)
                    elif GameState.get_falling_block_position()[0] > 5:
                        if GameState.get_falling_block_position()[0] > x:
                            clone.move(Direction.right)
                    else:
                        clone.move(Direction)

                    if GameState.get_falling_block_angle()[1] < y:
                        clone.rotate(Direction.right)
                    landed = clone.update()
                    if landed:
                        break
                    clone.get_score
                currentscore=clone.get_score()
                currenttile = clone.get_tiles()
                if currentscore > bestscore:
                    bestscore=currentscore  
                    besttile = clone.get_tiles()
                    if x > GameState.get_falling_block_position()[0]:
                        bestdirection = 1
                    elif x < GameState.get_falling_block_position()[0]:
                        bestdirection = -1
                    else:
                        bestdirection = 0
                    if y > GameState.get_falling_block_angle():
                        bestrotate = 1
                    elif y < GameState.get_falling_block_angle():
                        bestrotate = -1
                    else:
                        bestrotate = 0
                    
        if  bestdirection == 1:
            direction = Direction.RIGHT
        elif bestdirection == -1:
            direction = Direction.LEFT
        if bestdirection != 0:
            GameState.move(direction)
        if bestrotate == 1:
            direction = Direction.RIGHT
        elif bestrotate == -1:
            direction = Direction.LEFT
        if bestrotate != 0:
            GameState.rotate(direction)


                

               

        
    def score(self):
        
        score = -0.510066*self.sumheright +  0.760666*self.numcompleteline -0.35663*self.holes -0.184483*self.bumpiness

        return score

    def gridheight(self):
        tiles = GameState.get_tiles()
        r=0
        for _x in range (0,9):
            for _y in range (0,21):
                if tiles[_y][_x] != 0:
                    height[r] = 22- _y +1
                    break
                    return height[r]
                r += 1

        sumheright = height[0] + height[1] + height[2] + height[3] + height[4] + height[5] + height[6] + height[7] + height[8] + height[9]

    def completeline(self,numcompleteline,completeness):
        tiles = GameState.get_tiles()
        numcompleteline =0
        completeness = 0
        for _y in range (0,21):
            for _x in range (0,9):
                if tiles[_y][_x] == 1:
                    completeness += 1
                    if completeness == 10:
                        numcompleteline += 1
        return numcompleteline
    
    def holes(self,holes):
        tiles = GameState.get_tiles()
        holes =0
        for _x in range (0,9):
            for _y in range (0,21):
                if tiles[_y][_x] == 1:
                    toptile = _y
                    break 
            for _y in range (toptile,21):
                if tiles[_y][_x] == 0:
                    holes += 1
        return holes

    def bumpiness(self,bump):
        tiles = GameState.get_tiles()
        highesttile=0
        highest = 0
        r = 0
        for _x in range (0,9):
            for _y in range (0,21):
                if tiles[_y][_x] == 1:
                    if 22- _y +1 > highest:
                        self.highest =_y
                    bump[r] = 22- _y +1 
                    break
                r += 1
        bumpiness = 10 * highest - bump[0]-bump[1]-bump[2]-bump[3]-bump[4]-bump[5]-bump[6]-bump[7]-bump[8]-bump[9]
        return  bumpiness










