#Programming 3 group project
#Group Members: Darragh Foley (22785781), John Cullen (22536103),
#               Jody English (22514069), Matthew Mongan (22320036).
# Our group project is: Maze Game
# references in project. Overall bibliography of references at bottom of script
import random
import sys
import time


#Matthew Mongan
class Player:   # class used to make player objects, with their stored positions(row,column)
  def __init__(self, row, column):
    self.row = row
    self.column = column
    
#Darragh 
class Maze:
  def __init__(self, rows, columns):
    self.rows = rows     # no. rows in maze
    self.columns = columns   #no.columns in maze
    #Reference 2 logic used below
    self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]  # create grid of empty spaces '',  specified by the rows and columns
    # _ (dummy variable) used as no need to track index of rows/columns, looking over the rows and columns creating a list for each one
    self.player = Player(0,0)  #currently initialised as 0,0 position so recognised in code
    self.end_symbol = '○'   #exit symbol
    self.start_time = None
    self.end_position = (0,0) 

  def add_entity(self, symbol, entity_row, entity_column):   # to allow for symbols to be added at grid positions
    self.grid[entity_row][entity_column] = symbol   # symbol at that position
    if symbol == '𖨆':
      self.player = Player(entity_row, entity_column)
    elif symbol == self.end_symbol:  # sets end position att to co-ords of exit
      self.end_position = (entity_row, entity_column)

  def add_random_walls(self, num_walls): #adds walls to maze,randint used for random wall placement
    for _ in range(num_walls): #random row and column index for wall placement
      #-1 used to keep index inside row/column grid list
      row = random.randint(0, self.rows - 1)
      column = random.randint(0, self.columns - 1)
      if self.grid[row][column] == ' ': # if position is empty, wall can be set
        self.grid[row][column] = '■'

  def move_player(self, direction):
    directions = {'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)} #directions dict
    move = directions.get(direction.upper(), (0, 0)) #direction key can be inputted as lowercase but still work
    new_row = self.player.row + move[0] #row in move tuple
    new_column = self.player.column + move[1] # column in move tuple

    if not self.start_time:
      self.start_time = time.time()
# new position is in maze and not in a wall position
    if 0 <= new_row < self.rows and 0 <= new_column < self.columns and self.grid[
        new_row][new_column] != '■':
      #updates grid
      self.grid[self.player.row][self.player.column] = ' '
      self.player.row = new_row
      self.player.column = new_column
      self.grid[new_row][new_column] = '𖨆'
#
      if (new_row, new_column) == self.end_position:
        return True #player reaches end position

    return False  #player didnt reach end position

  def display(self): #prints current maze after move made
    print('\n' * 5)
    border = '■' + '■' * self.columns + '■' #top border of maze
    print(border)
    for row in range(self.rows):   
      row_str = '■'
      for column in range(self.columns):
        if (row, column) == (self.player.row, self.player.column):
          row_str += '𖨆'
        else:
          row_str += self.grid[row][column]
      row_str += '■'
      print(row_str)
    print(border)


#John Cullen
class Setup:
  def __init__(self):
    self.player_name = None #initializing player name
    self.selected_difficulty = None #initalizing maze difficulty

  def get_player_name(self):
    self.player_name = input("Hello! What's your name? ") #Asking the user for their name

  def get_difficulty_choice(self):
    while True:
      difficulty_choice = input(
             "Choose the difficulty level:\n1 for Easy\n2 for Intermediate\n3 for Hard\nYour choice: "
        ) #Asking the user to choose their difficulty level 1,2 or 3
      if difficulty_choice in ['1', '2', '3']:
          self.selected_difficulty = int(difficulty_choice) #sets the difficulty based on the user choice
          break
      else:
          print("Invalid input. Please choose 1, 2, or 3.") #Prints invalid input if 1,2 or 3 isn't chosen

  def determine_maze_difficulty(self):
    if self.selected_difficulty == 1:
        return 30  # Easy number of walls
    elif self.selected_difficulty == 2:
        return 45  # Intermediate number of walls
    elif self.selected_difficulty == 3:
        return 60  # Hard number of walls
          
#Jody English - following class is to run the maze game
class run_maze_game:
  def __init__(self):
    self.setup = Setup() # Initialize setup for player name and difficulty choice

  def start_game(self):
    print("Welcome to our CA278 Project")
    print("This is the maze game !! Enter the following details to get started\n")
    self.setup.get_player_name() # Get player's name
    self.setup.get_difficulty_choice() # Get player's chosen difficulty
    print(" ")
    print("Instructions: Use W,A,S,D to move the player 𖨆 to the exit ○, if you want to exit, type 'quit' as your input!!")

    maze = Maze(20, 20) # Create a maze with 20 rows and 20 columns
    maze.add_entity('𖨆', 1, 1) # Add player entity to the maze
    end_col = random.randint(1, 18)
    maze.add_entity('○', 18, end_col) # Add end point entity to the maze
    num_walls = self.setup.determine_maze_difficulty()
    maze.add_random_walls(num_walls)
    maze.display()

    start_time = None

    while True:
      move = input("Enter W, A, S, D to move: ").upper()
      if move == 'QUIT':
        break
      if move in ['W', 'A', 'S', 'D']:
        #logic from reference 1 video used below
        if not start_time:
          start_time = time.time()
        if maze.move_player(move):
          maze.display()
          total_time = time.time() - start_time
          print(
              f"Congratulations {self.setup.player_name}! You completed the maze in {total_time:.2f} seconds!"
          )
          print("Play again to beat your best time!")
          sys.exit()
        else:
          maze.display()
      else:
        print("Invalid input. Use W, A, S, D to move or type 'quit' to end game")

#Matthew Mongan
def main():
  maze_game_start = run_maze_game()  #calling the class that runs the game
  maze_game_start.start_game()   #calling the start_game function in the class to start game


if __name__ == "__main__":
  main()

# Reference 1:
# we used the following video to help us with the logic of the timer, logic was used in def start game, def move player 
# TokyoEdtech (2020). Python Game Coding: How to Make a Game Timer. [online] www.youtube.com. Available at: https://www.youtube.com/watch?v=juSH7hmYUGA.

# Reference 2:
#Maranan, M. (n.d.). How to Make a Maze Game in Python - The Python Code. [online] thepythoncode.com. Available at: https://thepythoncode.com/article/build-a-maze-game-in-python?utm_content=cmp-true [Accessed 4 Apr. 2024].