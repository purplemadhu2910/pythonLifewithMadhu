def print_board(board):
    print("\n")
    print(" 1  2  3 ")
    print("-------------")
    
    for i in range(3):
        print(f"{i+1}| {board[i][0]} | {board[i][1]} | {board[i][2]} |") 
        print("\n")
        
def check_winner(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)):
            return True
        if all(board[j][i]==player for j in range(3)):
            return True
        if all(board[i][i]==player for i in range(3)):
            return True
        if all(board[i][2-i]==player for i in range(3)):
            return True
    return False

def is_draw(board):
    return all(board[i][j] != '' for i in range(3) for j in range(3))

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        board=[['' for _ in range(3)]for _ in range(3)]
        current_player='X'
        game_over=False
        
        while not game_over:
            print_board(board)
            print(f"Player{current_player}'s turn.")
            
            try:
                row=int(input("Enter row (1-3): "))-1
                col=int(input("Enter column(1-3): "))-1
                
                if row not in range(3) or col not in range(3):
                    print("Invalid input! PLease enter numbers between 1 and 3")
                    continue
                if board[row][col] !='':
                    print("cell alreay taken! Choose another one!")
                    continue
                
                board[row][col]=current_player
                
                if check_winner(board, current_player):
                    print_board(board) 
                    print(f" Player {current_player} wins! ") 
                    game_over = True 
                elif is_draw(board): 
                    print_board(board) 
                    print(" It's a draw!") 
                    game_over = True 
                else: 
                    current_player = 'O' if current_player == 'X' else 'X' 
 
            except ValueError: 
                print(" Invalid input! Please enter numeric values.") 
 
        play_again = input("Do you want to play again? (y/n): ").lower() 
        if play_again != 'y': 
            print("Thanks for playing Tic-Tac-Toe! Goodbye!") 
            break 
 
if __name__ == "__main__": 
    tic_tac_toe() 
