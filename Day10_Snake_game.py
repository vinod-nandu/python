"""
Python Snake Game - Windows GUI
A classic snake game built with tkinter
"""

import tkinter as tk
from tkinter import messagebox
import random

# ============================================================================
# GAME CONSTANTS
# ============================================================================

GRID_SIZE = 20  # Size of each cell
GAME_WIDTH = 400  # Game area width (20 cells × 20 pixels)
GAME_HEIGHT = 400  # Game area height (20 cells × 20 pixels)
GAME_SPEED = 100  # Game update speed in milliseconds

# Colors
COLOR_BACKGROUND = "#1a1a1a"
COLOR_SNAKE = "#00FF00"
COLOR_FOOD = "#FF0000"
COLOR_GRID = "#333333"
COLOR_TEXT = "#00FF00"


# ============================================================================
# SNAKE GAME CLASS
# ============================================================================

class SnakeGame:
    def __init__(self, root):
        """Initialize the snake game"""
        self.root = root
        self.root.title("Python Snake Game")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.configure(bg=COLOR_BACKGROUND)
        
        # Game variables
        self.snake = [(GAME_WIDTH // 2, GAME_HEIGHT // 2)]  # Snake body
        self.food = self.spawn_food()
        self.direction = (GRID_SIZE, 0)  # Initial direction (right)
        self.next_direction = (GRID_SIZE, 0)
        self.score = 0
        self.game_over = False
        self.game_paused = False
        
        # Create UI
        self.create_ui()
        
        # Bind keyboard events
        self.root.bind("<Up>", self.change_direction_up)
        self.root.bind("<Down>", self.change_direction_down)
        self.root.bind("<Left>", self.change_direction_left)
        self.root.bind("<Right>", self.change_direction_right)
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<r>", self.restart_game)
        
        # Start game loop
        self.game_loop()
    
    def create_ui(self):
        """Create the game user interface"""
        
        # Title
        title_label = tk.Label(
            self.root,
            text="SNAKE GAME",
            font=("Arial", 20, "bold"),
            fg=COLOR_TEXT,
            bg=COLOR_BACKGROUND
        )
        title_label.pack(pady=10)
        
        # Info frame
        info_frame = tk.Frame(self.root, bg=COLOR_BACKGROUND)
        info_frame.pack(pady=5)
        
        # Score display
        self.score_label = tk.Label(
            info_frame,
            text=f"Score: {self.score}",
            font=("Arial", 14),
            fg=COLOR_TEXT,
            bg=COLOR_BACKGROUND
        )
        self.score_label.pack(side="left", padx=20)
        
        # Status display
        self.status_label = tk.Label(
            info_frame,
            text="Running",
            font=("Arial", 14),
            fg=COLOR_TEXT,
            bg=COLOR_BACKGROUND
        )
        self.status_label.pack(side="right", padx=20)
        
        # Game canvas
        self.canvas = tk.Canvas(
            self.root,
            width=GAME_WIDTH,
            height=GAME_HEIGHT,
            bg=COLOR_BACKGROUND,
            highlightthickness=2,
            highlightbackground=COLOR_GRID
        )
        self.canvas.pack(pady=10)
        
        # Controls frame
        controls_frame = tk.Frame(self.root, bg=COLOR_BACKGROUND)
        controls_frame.pack(pady=10)
        
        controls_text = tk.Label(
            controls_frame,
            text="Arrow Keys: Move | SPACE: Pause | R: Restart | Q: Quit",
            font=("Arial", 10),
            fg=COLOR_TEXT,
            bg=COLOR_BACKGROUND
        )
        controls_text.pack()
        
        # Bind quit
        self.root.bind("<q>", lambda e: self.root.quit())
    
    def spawn_food(self):
        """Spawn food at a random location not on the snake"""
        while True:
            x = random.randint(0, (GAME_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
            y = random.randint(0, (GAME_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
            if (x, y) not in self.snake:
                return (x, y)
    
    def change_direction_up(self, event):
        """Change direction to up (if not moving down)"""
        if self.direction != (0, GRID_SIZE):
            self.next_direction = (0, -GRID_SIZE)
    
    def change_direction_down(self, event):
        """Change direction to down (if not moving up)"""
        if self.direction != (0, -GRID_SIZE):
            self.next_direction = (0, GRID_SIZE)
    
    def change_direction_left(self, event):
        """Change direction to left (if not moving right)"""
        if self.direction != (GRID_SIZE, 0):
            self.next_direction = (-GRID_SIZE, 0)
    
    def change_direction_right(self, event):
        """Change direction to right (if not moving left)"""
        if self.direction != (-GRID_SIZE, 0):
            self.next_direction = (GRID_SIZE, 0)
    
    def toggle_pause(self, event):
        """Toggle game pause"""
        if not self.game_over:
            self.game_paused = not self.game_paused
            self.status_label.config(
                text="PAUSED" if self.game_paused else "Running"
            )
    
    def restart_game(self, event):
        """Restart the game"""
        self.snake = [(GAME_WIDTH // 2, GAME_HEIGHT // 2)]
        self.food = self.spawn_food()
        self.direction = (GRID_SIZE, 0)
        self.next_direction = (GRID_SIZE, 0)
        self.score = 0
        self.game_over = False
        self.game_paused = False
        self.score_label.config(text=f"Score: {self.score}")
        self.status_label.config(text="Running")
    
    def update_game(self):
        """Update game state"""
        if self.game_over or self.game_paused:
            return
        
        # Update direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GAME_WIDTH or
            new_head[1] < 0 or new_head[1] >= GAME_HEIGHT):
            self.end_game()
            return
        
        # Check self collision
        if new_head in self.snake:
            self.end_game()
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw_game(self):
        """Draw the game on canvas"""
        self.canvas.delete("all")
        
        # Draw grid
        for x in range(0, GAME_WIDTH, GRID_SIZE):
            self.canvas.create_line(
                x, 0, x, GAME_HEIGHT,
                fill=COLOR_GRID, width=1
            )
        for y in range(0, GAME_HEIGHT, GRID_SIZE):
            self.canvas.create_line(
                0, y, GAME_WIDTH, y,
                fill=COLOR_GRID, width=1
            )
        
        # Draw snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + GRID_SIZE, y + GRID_SIZE,
                fill=COLOR_SNAKE,
                outline=COLOR_GRID
            )
        
        # Highlight head
        if self.snake:
            head_x, head_y = self.snake[0]
            self.canvas.create_rectangle(
                head_x, head_y, head_x + GRID_SIZE, head_y + GRID_SIZE,
                fill="#00AA00",
                outline=COLOR_GRID
            )
        
        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(
            fx + 2, fy + 2, fx + GRID_SIZE - 2, fy + GRID_SIZE - 2,
            fill=COLOR_FOOD,
            outline="orange"
        )
        
        # Draw "Game Over" text if needed
        if self.game_over:
            self.canvas.create_text(
                GAME_WIDTH // 2, GAME_HEIGHT // 2 - 20,
                text="GAME OVER",
                font=("Arial", 20, "bold"),
                fill=COLOR_FOOD
            )
            self.canvas.create_text(
                GAME_WIDTH // 2, GAME_HEIGHT // 2 + 20,
                text="Press R to Restart",
                font=("Arial", 12),
                fill=COLOR_TEXT
            )
    
    def end_game(self):
        """Handle game over"""
        self.game_over = True
        self.status_label.config(text=f"GAME OVER - Score: {self.score}")
    
    def game_loop(self):
        """Main game loop"""
        self.update_game()
        self.draw_game()
        
        # Schedule next update
        self.root.after(GAME_SPEED, self.game_loop)


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Start the snake game"""
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
