def check_winner(board):
    winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)

    if winner == 'X':
        return -10 + depth
    if winner == 'O':
        return 10 - depth
    if ' ' not in board:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth+1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth+1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board):
    max_val = float('-inf')
    best_move_idx = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if move_val > max_val:
                max_val = move_val
                best_move_idx = i

    return best_move_idx
