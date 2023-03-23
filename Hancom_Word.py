"""
The model for the Hancom game, using classes, lists and files. The word class draws the word
in the gui canvas and makes the word to fall. The Hancom class includes basic features of the
game including user's points and life and calls different files for the game. Also, the module
includes assert statements to test the game. 

Created Fall, 2022

@author1: Si Chan(Daniel) Park (sp56)
@author2: Hye Chan Lee (hl63)
@date: Fall, 2022
"""

from random import randint

class Word:
    '''This class implements the word class for the Hancom game.'''
    
    def __init__(self, x = 0, y = 0, text = 'hi'):
        '''Create a new word class'''
        #Fix the self.x value
        self.x = x
        self.y = y
        self.text = text
        self.speed = 1.5
    
    def fall(self):
        '''Makes the word to fall from the canvas'''
        self.y += self.speed
        
    def draw_word(self, drawing, text):
        '''Draws the word into the Gui canvas'''
        drawing.text(self.x, self.y, text = self.text, size = 15, font = 'Helvetica' )
        
    def __str__(self):
        '''Returns the string type of the text'''
        return self.text
        
    def __repr__(self):
        '''Just needed for testing purposes. Used for test purposes.'''
        return self.text
   

class Hancom:
    '''This class implements the game model for the Hancom game.'''
    
    def __init__(self, life = 3, points = 0):
        '''Create a new Hancom game with words read from the given file.'''
        self.life = life
        self.points = points
        self.files = ['English1.txt', 'English2.txt', 'English3.txt', 'English4.txt', 'English5.txt']
        self.file_index = 0
        self.filename = self.files[self.file_index]
    
    def change_filename(self):
        '''Changes the file using file index'''
        self.file_index += 1
        self.filename = self.files[self.file_index]
    
    def get_life(self):
        '''Gets current life'''
        return self.life
        
    def get_points(self):
        '''Get current points'''
        return self.points
        
    def lose_life(self):
        '''The User loses a life'''
        self.life -= 1
    
    def gain_points(self):
        '''The User gains points for the correct input'''
        self.points += 1
        
        
        
#Testing the classes by assert statements.
if __name__ == '__main__':
    test1 = Hancom()
    test2 = Word()

    # Tests the variables in the constructor of Hancom class
    assert test1.life == 3
    assert test1.points == 0
    assert test1.get_life() == test1.life
    assert test1.file_index == 0
    assert len(test1.files) == 5

    test1.lose_life()
    assert test1.life == 2
    test1.gain_points()
    assert test1.points == 1
    assert test1.filename == 'English1.txt'
    test1.change_filename()
    assert test1.file_index == 1
    assert test1.filename == 'English2.txt'

    
    #Tests the variables in the constructor of Word class
    assert test2.x == 0
    assert test2.y == 0
    assert test2.text == 'hi'
    assert test2.speed == 1.5

    test2.fall()
    assert test2.y == 1.5
        
        
        