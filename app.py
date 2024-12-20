import random

# Ukuran papan
BOARD_SIZE = 8
NUM_MINES = 10

# Membuat papan permainan
def create_board(size, num_mines):
    board = [[" " for _ in range(size)] for _ in range(size)]
    mines = set()
    
    while len(mines) < num_mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        mines.add((x, y))
    
    for (x, y) in mines:
        board[x][y] = "M"  # M untuk ranjau
    
    return board, mines

# Menampilkan papan
def display_board(board, revealed):
    print("   " + " ".join([str(i) for i in range(len(board))]))
    print("  +" + "-+" * len(board))
    for i, row in enumerate(board):
        print(f"{i} |" + "|".join([cell if revealed[i][j] else "?" for j, cell in enumerate(row)]) + "|")
        print("  +" + "-+" * len(row))

# Menghitung ranjau di sekitar kotak tertentu
def count_adjacent_mines(board, x, y):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == "M":
            count += 1
    return count

# Mengungkap kotak
def reveal(board, revealed, x, y):
    if revealed[x][y]:
        return
    revealed[x][y] = True
    if board[x][y] == " ":
        board[x][y] = str(count_adjacent_mines(board, x, y))
        if board[x][y] == "0":  # Jika tidak ada ranjau di sekitar
            board[x][y] = " "
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    reveal(board, revealed, nx, ny)

# Mengecek kemenangan
def check_win(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "M" and not revealed[i][j]:
                return False
    return True

# Main loop permainan
def play_minesweeper():
    board, mines = create_board(BOARD_SIZE, NUM_MINES)
    revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    while True:
        display_board(board, revealed)
        try:
            x, y = map(int, input("Masukkan koordinat (x y): ").split())
            if (x, y) in mines:
                print("Boom! Anda terkena ranjau. Game Over!")
                break
            reveal(board, revealed, x, y)
            if check_win(board, revealed):
                display_board(board, revealed)
                print("Selamat! Anda menang!")
                break
        except (ValueError, IndexError):
            print("Input tidak valid. Masukkan koordinat yang benar.")

# Jalankan permainan
play_minesweeper()
