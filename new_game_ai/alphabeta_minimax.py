# import math


# class Game:
#     def __init__(self):
#         self.number = 0
#         self.player_score = 0
#         self.computer_score = 0

#     def start_game(self):
#         self.number = int(input("Enter a number between 8 and 18 to start the game: "))
#         while self.number < 8 or self.number > 18:
#             self.number = int(input("Please enter a number between 8 and 18: "))

#         print("\nGame started with number:", self.number)

#     def make_move(self, player, multiplier):
#         new_number = self.number * multiplier
#         if new_number % 2 == 0:
#             if player == "user":
#                 self.computer_score -= 1
#             else:
#                 self.player_score -= 1
#         else:
#             if player == "user":
#                 self.player_score += 1
#             else:
#                 self.computer_score += 1

#         self.number = new_number

#     def print_scores(self):
#         print("User score:", self.player_score)
#         print("Computer score:", self.computer_score)

#     def is_game_over(self):
#         return self.number >= 1200

#     def determine_winner(self):
#         if self.player_score > self.computer_score:
#             return "User"
#         elif self.player_score < self.computer_score:
#             return "Computer"
#         else:
#             return "Draw"


# def alpha_beta(game, depth, alpha, beta, maximizing_player):
#     if depth == 0 or game.is_game_over():
#         return game.player_score - game.computer_score

#     if maximizing_player:
#         max_eval = -math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("computer", multiplier)
#             if game.number % 2 == 0:
#                 game.computer_score += 1
#             else:
#                 game.player_score -= 1

#             eval = alpha_beta(game, depth - 1, alpha, beta, False)
#             max_eval = max(max_eval, eval)
#             alpha = max(alpha, eval)

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score

#             if beta <= alpha:
#                 break
#         return max_eval
#     else:
#         min_eval = math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("user", multiplier)
#             if game.number % 2 == 0:
#                 game.player_score += 1
#             else:
#                 game.computer_score -= 1

#             eval = alpha_beta(game, depth - 1, alpha, beta, True)
#             min_eval = min(min_eval, eval)
#             beta = min(beta, eval)

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score

#             if beta <= alpha:
#                 break
#         return min_eval


# def minimax(game, depth, maximizing_player):
#     if depth == 0 or game.is_game_over():
#         return game.player_score - game.computer_score

#     if maximizing_player:
#         max_eval = -math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("computer", multiplier)
#             if game.number % 2 == 0:
#                 game.computer_score += 1
#             else:
#                 game.player_score -= 1

#             eval = minimax(game, depth - 1, False)
#             max_eval = max(max_eval, eval)

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score

#         return max_eval
#     else:
#         min_eval = math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("user", multiplier)
#             if game.number % 2 == 0:
#                 game.player_score += 1
#             else:
#                 game.computer_score -= 1

#             eval = minimax(game, depth - 1, True)
#             min_eval = min(min_eval, eval)

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score

#         return min_eval

# def computer_move(game, algorithm):
#     if algorithm == "AB":
#         best_move = None
#         max_eval = -math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("computer", multiplier)

#             eval = alpha_beta(game, 4, -math.inf, math.inf, False)
#             if eval > max_eval:
#                 max_eval = eval
#                 best_move = multiplier

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score
#     else:
#         best_move = None
#         max_eval = -math.inf
#         for multiplier in [2, 3, 4]:
#             original_number = game.number
#             original_computer_score = game.computer_score
#             original_player_score = game.player_score

#             game.make_move("computer", multiplier)

#             eval = minimax(game, 4, False)
#             if eval > max_eval:
#                 max_eval = eval
#                 best_move = multiplier

#             game.number = original_number
#             game.computer_score = original_computer_score
#             game.player_score = original_player_score
#     return best_move;

# def main():
#     game = Game()
#     game.start_game()

#     user_starts = input("Do you want to start the game? (yes/no): ").lower() == "yes"

#     if user_starts:
#         current_player = "user"
#     else:
#         current_player = "computer"

#     algorithm = input("Choose algorithm for the computer (MiniM/AB): ").upper()

#     while not game.is_game_over():
#         if current_player == "user":
#             print("\nCurrent number:", game.number)
#             print("Your turn.")
#             multiplier = int(input("Choose a multiplier (2, 3, or 4): "))
#             while multiplier not in [2, 3, 4]:
#                 multiplier = int(input("Invalid multiplier. Choose again (2, 3, or 4): "))
#             game.make_move("user", multiplier)
#             current_player = "computer"
#         else:
#             print("\nCurrent number:", game.number)
#             print("Computer's turn.")
#             computer_move(game, algorithm)
#             current_player = "user"
#         game.print_scores()

#     print("\nCurrent number:", game.number)
#     print("\nGame over!")
#     winner = game.determine_winner()
#     print("Winner:", winner)

#     play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"
#     if play_again:
#         main()
#     else:
#         print("Thanks for playing!")

# if __name__ == "__main__":
#     main()

# addition?

import math

# Simplify the game logic as required. 
# This example focuses on determining the best move without directly modifying the game state.

def minimax(current_number, depth, maximizing_player):
    if depth == 0:
        return None  

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for multiplier in [2, 3, 4]:  
            
            eval = multiplier  
            if eval > max_eval:
                max_eval = eval
                best_move = multiplier
        return best_move
    else:
        min_eval = math.inf
        for multiplier in [2, 3, 4]:
            eval = multiplier  
            if eval < min_eval:
                min_eval = eval
                best_move = multiplier
        return best_move

def alpha_beta(current_number, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return None  

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for multiplier in [2, 3, 4]:
            eval = multiplier 
            if eval > max_eval:
                max_eval = eval
                best_move = multiplier
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move
    else:
        min_eval = math.inf
        for multiplier in [2, 3, 4]:
            eval = multiplier
            if eval < min_eval:
                min_eval = eval
                best_move = multiplier
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move

def computer_move(current_number, algorithm):
    depth = 4  # Example depth, adjust as needed
    if algorithm == "alpha_beta":
        return alpha_beta(current_number, depth, -math.inf, math.inf, True)
    else:  # Default to minimax
        return minimax(current_number, depth, True)


