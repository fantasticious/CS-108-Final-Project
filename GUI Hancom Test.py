"""
This GUI Test.py tests the winner_message method from the HancomApp class. In the original game, the user needs to reach 50 points
to view the winner message, but in this GUI Test.py, the user just needs 5 points. Also, the GUI Test.py prints the words inside the
falling_words_list and the length of this list to check whether the falling words are correctly added to the falling_words_list. 

Created Fall, 2022

@author1: Si Chan(Daniel) Park (sp56)
@author2: Hye Chan Lee (hl63)
@date: Fall, 2022 
"""

from guizero import App, Box, Text, TextBox, PushButton, Drawing, Window

from Hancom_Word import Hancom, Word

from random import randint


class HancomApp:
    def __init__(self, app):
        """This class implements a GUI for the Hancom game."""

        # Configure the application GUI.
        app.title = 'Hancom Game'
        app.width = 700
        app.height = 630
        app.font = 'Helvetica'
        app.text_size = 13
        app.bg = 'white'
        
        # Instantiate a single Hancom object for repeated use.
        self.hancom = Hancom()
        
        #A list that contains the words as Word object that fall from the gui canvas
        self.falling_words_list = []
    
        #A list that contains words from the txt file opened in the Hancom class
        self.storing_words_list = []
        
        #List for checkings whether the user input is one of the falling words. 
        self.check_list = []
                
        #Creates a drawing canvas
        self.drawing = Drawing(app, width = 700, height = 550)
        self.drawing.image(0, 0, 'image.png', 700, 550)
        self.drawing.line(0,500,700,500, color = 'red')
        
        #Create boxes for widgets
        box_top = Box(app, width = 'fill', border = True)
        box = Box(app, width = 'fill', align = 'bottom', border =True)
        box_left = Box(box, align = 'left', border = True)
        box_right = Box(box, align = 'right', layout = 'grid', border = True)
        
        
        #Create widgets in boxes
        self.user_input = TextBox(box, height = 'fill', width = 'fill', align = 'left')
        start_button = PushButton(box_left, text = 'Start', align = 'left', command = self.start)
        quit_button = PushButton(box_left, text = 'Quit', align = 'left', command = app.destroy)
        life_text = Text(box_right, text = 'Life: ', grid = [0,0], align = 'left')
        self.life_result = Text(box_right, text = self.hancom.life, grid = [1,0])
        points_text = Text(box_right, text = 'Points: ', align = 'left', grid = [0,1])
        self.points_result = Text(box_right, text = self.hancom.points, grid = [1,1])
        self.user_input.when_key_pressed = self.process_key_event
        
        #Creates an instructions text
        self.instructions = Text(box_top, text = 'Press start to begin the game. Type the falling word in the textbox and press the enter key to check.', size = 11)
        
        #Create a 2nd window and widgets for the GameOver message
        self.window1 = Window(app, title = 'GameOver Message', height = 200, width = 300)
        self.window1.bg = 'red'
        self.window_text_game_over = Text(self.window1, text = 'GAME OVER', color = 'yellow', font = 'Helvetica', size = 180)
        box_window1 = Box(self.window1, width = 130, height = 50, layout = 'grid')
        self.window1_text_points = Text(box_window1, text = 'Points: ', font = 'Helvetica', size = 20, grid = [0,0])
        self.window1_text_points_value = Text(box_window1, text = self.hancom.points, font = 'Helvetica', size = 20, grid = [1,0])
        exit_button1 = PushButton(self.window1, text = 'Quit', command = app.destroy)
        exit_button1.bg = 'white'
        self.window1.hide()
        
        #Create a 3nd window and widgets for the Winner message
        self.window2 = Window(app, title = 'Winner Message', height = 200, width = 300)
        self.window2.bg = 'green'
        self.window_text_winner1 = Text(self.window2, text = 'You are too good for this game!', color = 'yellow', font = 'Helvetica', size = 80)
        self.window_text_winner2 = Text(self.window2, text = 'Please wait for next update!', color = 'yellow', font = 'Helvetica', size = 80)
        box_window2 = Box(self.window2, width = 130, height = 50, layout = 'grid')
        self.window2_text_points = Text(box_window2, text = 'Points: ', font = 'Helvetica', size = 20, grid = [0,0])
        self.window2_text_points_value = Text(box_window2, text = self.hancom.points, font = 'Helvetica', size = 20, grid = [1,0])
        exit_button2 = PushButton(self.window2, text = 'Quit', command = app.destroy)
        exit_button2.bg = 'white'
        self.window2.hide()
        
        
    #Methods used in the HancomApp class
    def start(self):
        '''Starts the Hancom Typing Game'''
        self.get_word()
        app.repeat(20, self.animation)
        app.repeat(2150, self.add_falling_word)
        
                 
    def get_word(self):
        '''Gets word from the txt file and stores in the storing_words_list.'''
        #The line of code below was found in https://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
        f = open(self.hancom.filename).read().splitlines()
        for self.line in f:
            self.line = Word(randint(0,550), -10, self.line)
            self.storing_words_list.append(self.line)
        
                           
    def animation(self):
        '''Creates the animation for Gui canvas. If the word reaches the red line before typed by the user,
           the user loses a life and the word disappears.  '''
        self.drawing.clear()
        self.drawing.image(0, 0, 'image.png', 700, 550)
        self.drawing.line(0,500,700,500, color = 'red')
        
        #Makes the word to fall in the screen 
        #If the word reaches the red line, the word gets removed and user losses a life
        if self.hancom.life > 0:
            for word in self.falling_words_list:
                word.fall()
                if word.y >= 490:
                    self.remove_word_fwl(word)
                    self.remove_word_cl(str(word))
                    self.update_life()
                word.draw_word(self.drawing, word)
    
        
    def add_falling_word(self):
        '''Adds words from storing_words_list to the falling_words_list.'''
        random_index = randint(0, len(self.storing_words_list)-1)
        self.falling_words_list.append(self.storing_words_list[random_index])
        self.check_list.append(str(self.storing_words_list[random_index]))
        self.storing_words_list.remove(self.storing_words_list[random_index])
        
        #Prints the words inside the falling_words_list and the length of the list
        print(self.falling_words_list, len(self.falling_words_list))
    
        
    def process_key_event(self,event):
        '''checks the input word when enter key is pressed'''
        if event.key == '\r':
            self.check_word()
        
        
    def remove_word_fwl(self, word):
        '''Removes the falling word from falling_words_list'''
        self.falling_words_list.remove(word)
        
        
    def remove_word_cl(self, word):
        '''Removes word from check_list'''
        self.check_list.remove(word)


    def check_word(self):
        '''Checks whether the user input is in the falling_words_list
            and if the word is inside the list, the word gets removed from the list.
            Also, as the user reaches certain points, the game moves onto the next level.'''
        if self.user_input.value in self.check_list:
            index = self.check_list.index(self.user_input.value)
            self.remove_word_fwl(self.falling_words_list[index])
            self.remove_word_cl(self.check_list[index])
            self.update_points()
            #Changes the value of self.instructions to show that the spelling is correct.
            self.instructions.value = "Correct"
            
        else:
            #Changes the value of self.instructions to show that the spelling is incorrect
            self.instructions.value = 'Please Check Your Spelling'
        self.user_input.value = ''
        
        #After the user earns a total of 5 points, the game ends.  
        if self.hancom.points == 5:
            self.winner_message()
            
        
            
            
    def update_points(self):
        '''Updates the points'''
        #Increase the user's point value. 
        self.hancom.gain_points()
        
        #Updates the point value text.
        self.points_result.value = self.hancom.get_points()
        self.window1_text_points_value.value = self.hancom.get_points()
        self.window2_text_points_value.value = self.hancom.get_points()
        
        
    def update_life(self):
        '''Updates the remaining life'''
        self.hancom.lose_life()
        self.life_result.value = self.hancom.get_life()
        
        #Shows the gameover window if the life gets to 0.
        if self.hancom.life == 0:
            self.game_over()
            
            
    def game_over(self):
        '''Shows the gameover window when life becomes 0'''
        self.window1.show()
        self.window1.set_full_screen()
        self.window2.destroy()
    
    
    def next_stage(self):
        '''Opens the next file which has longer words'''
        self.storing_words_list.clear()
        self.hancom.change_filename()
        self.get_word()


    def winner_message(self):
        '''Shows the winner window when the user types all the provided words correctly with the given life'''
        self.window2.show()
        self.window2.set_full_screen()
        self.window1.destroy()
   
   
app = App()
Hancom_game = HancomApp(app)
app.display()


