import tkinter as tk
from tkinter import messagebox
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        entry_font=("Arial",14)
        self.entries = [[tk.Entry(master, width=3, font=entry_font) for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)

        solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku,width=20,height=2)
        solve_button.grid(row=9, columnspan=9,padx=5,pady=5)

    def solve_sudoku(self):
        sudoku_grid = [[int(entry.get()) if entry.get() else 0 for entry in row] for row in self.entries]

        if solve_sudoku(sudoku_grid):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(sudoku_grid[i][j]))

            tk.messagebox.showinfo("Solved", "Sudoku puzzle has been solved!")
        else:
            tk.messagebox.showinfo("No Solution", "No solution exists for the given Sudoku puzzle.")
def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    print("Welcome to the Sudoku Solver!")
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()