#!/usr/bin/python3
import random
import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clean_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        # Count adjacent mines
                        count = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                nx, ny = x + dx, y + dy
                                if (0 <= nx < self.width and 0 <= ny < self.height and
                                    (ny * self.width + nx) in self.mines):
                                    count += 1
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        if self.revealed[y][x]:
            return True
        if (y * self.width + x) in self.mines:
            return False
        
        self.revealed[y][x] = True
        
        # If no adjacent mines, reveal neighbors
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width and 0 <= ny < self.height and
                    (ny * self.width + nx) in self.mines):
                    count += 1
        
        if count == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        self.reveal(x + dx, y + dy)
        
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine!")
                    break
                
                # Check if all non-mine cells are revealed
                all_revealed = True
                for y_pos in range(self.height):
                    for x_pos in range(self.width):
                        if (y_pos * self.width + x_pos) not in self.mines and not self.revealed[y_pos][x_pos]:
                            all_revealed = False
                            break
                    if not all_revealed:
                        break
                
                if all_revealed:
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break
                    
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
