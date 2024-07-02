import math  # Importing the math library to use mathematical functions such as infinity.
import random  # Importing the random library to generate random numbers for certain decisions.

# Definition of the Game class that holds the game state and logic.
class Game:
    def __init__(self):  # Initialization method to set up initial game state.
        self.number = 0  # The current number in the game, to be manipulated by player moves.
        self.player_score = 0  # The player's score.
        self.computer_score = 0  # The computer's score.

    def start_game(self):  # Method to start the game by asking the player to input a starting number.
        self.number = int(input("Enter a number between 8 and 18 to start the game: "))
        while self.number < 8 or self.number > 18:  # Ensuring the starting number is within the allowed range.
            self.number = int(input("Please enter a number between 8 and 18: "))
        print("\nGame started with number:", self.number)

    def make_move(self, player, multiplier):  # Method to apply a player's move to the game state.
        new_number = self.number * multiplier  # Multiplies the current number by the chosen multiplier.
        # Adjust scores based on whether the new number is even or odd.
        if new_number % 2 == 0:
            if player == "user":
                self.computer_score -= 1
            else:
                self.player_score -= 1
        else:
            if player == "user":
                self.player_score += 1
            else:
                self.computer_score += 1
        self.number = new_number  # Update the game's current number to the new number.

    def print_scores(self):  # Method to print the current scores of the player and computer.
        print("User score:", self.player_score)
        print("Computer score:", self.computer_score)

    def is_game_over(self):  # Method to check if the game is over based on the current number.
        return self.number >= 1200  # Returns True if the game should end, False otherwise.

    def determine_winner(self):  # Method to determine the winner of the game.
        # Compares scores and returns the winner.
        if self.player_score > self.computer_score:
            return "User"
        elif self.player_score < self.computer_score:
            return "Computer"
        else:
            return "Draw"

# Alpha-beta pruning algorithm function.
def alpha_beta(game, depth, alpha, beta, maximizing_player):
    # Base case: checks if we've reached the maximum depth or if the game is over.
    if depth == 0 or game.is_game_over():
        return game.player_score - game.computer_score  # Returns the heuristic value of the game state.

    # If it's the maximizing player's (computer's) turn.
    if maximizing_player:
        max_eval = -math.inf  # Initialize max evaluation to negative infinity.
        for multiplier in [2, 3, 4]:  # Iterates over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("computer", multiplier)  # Make the move for the computer.
            # Adjust scores based on the current number being even or odd after the move.
            if game.number % 2 == 0:
                game.computer_score += 1
            else:
                game.player_score -= 1

            eval = alpha_beta(game, depth - 1, alpha, beta, False)  # Recursive call to alpha_beta for the next depth.
            max_eval = max(max_eval, eval)  # Update max_eval if the current evaluation is greater.
            alpha = max(alpha, eval)  # Update alpha if the current evaluation is greater.

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

            if beta <= alpha:  # Pruning condition.
                break  # Break the loop if we can prune the branch.
        return max_eval  # Return the evaluation of the best move.
    else:
        min_eval = math.inf  # Initialize min evaluation to infinity for the minimizing player (user).
        for multiplier in [2, 3, 4]:  # Iterate over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("user", multiplier)  # Make the move for the user.
            # Adjust scores based on the current number being even or odd.
            if game.number % 2 == 0:
                game.player_score += 1
            else:
                game.computer_score -= 1

            eval = alpha_beta(game, depth - 1, alpha, beta, True)  # Recursive call to alpha_beta for the next depth.
            min_eval = min(min_eval, eval)  # Update min_eval if the current evaluation is lower.
            beta = min(beta, eval)  # Update beta if the current evaluation is lower.

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

            if beta <= alpha:  # Pruning condition.
                break  # Break the loop if we can prune the branch.
        return min_eval  # Return the evaluation of the best move.

# The Minimax algorithm function, similar in structure to alpha_beta but without pruning.
def minimax(game, depth, maximizing_player):
    # Base case: checks if we've reached the maximum depth or if the game is over.
    if depth == 0 or game.is_game_over():
        return game.player_score - game.computer_score  # Returns the heuristic value of the game state.

    # If it's the maximizing player's (computer's) turn.
    if maximizing_player:
        max_eval = -math.inf  # Initialize max evaluation to negative infinity.
        for multiplier in [2, 3, 4]:  # Iterates over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("computer", multiplier)  # Make the move for the computer.
            # Adjust scores based on the current number being even or odd after the move.
            if game.number % 2 == 0:
                game.computer_score += 1
            else:
                game.player_score -= 1

            eval = minimax(game, depth - 1, False)  # Recursive call to minimax for the next depth.
            max_eval = max(max_eval, eval)  # Update max_eval if the current evaluation is greater.

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

        return max_eval  # Return the evaluation of the best move.
    else:
        min_eval = math.inf  # Initialize min evaluation to infinity for the minimizing player (user).
        for multiplier in [2, 3, 4]:  # Iterate over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("user", multiplier)  # Make the move for the user.
            # Adjust scores based on the current number being even or odd.
            if game.number % 2 == 0:
                game.player_score += 1
            else:
                game.computer_score -= 1

            eval = minimax(game, depth - 1, True)  # Recursive call to minimax for the next depth.
            min_eval = min(min_eval, eval)  # Update min_eval if the current evaluation is lower.

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

        return min_eval  # Return the evaluation of the best move.

# Function for the computer to decide on its move based on the chosen algorithm.
def computer_move(game, algorithm):
    if algorithm == "AB":  # If the Alpha-Beta algorithm is chosen.
        best_move = None
        max_eval = -math.inf
        moves_with_heuristic_one = []  # List to store moves that lead directly to a win.

        for multiplier in [2, 3, 4]:  # Iterate over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("computer", multiplier)  # Make the move for the computer.

            # If the move results in a game-over state, add it to the list of winning moves.
            if game.number >= 1200:
                moves_with_heuristic_one.append(multiplier)

            eval = alpha_beta(game, 4, -math.inf, math.inf, False)  # Call alpha_beta to evaluate the move.
            if eval > max_eval:  # Update max_eval and best_move if the current evaluation is greater.
                max_eval = eval
                best_move = multiplier

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

        # If there are winning moves, choose one at random.
        if moves_with_heuristic_one:
            best_move = random.choice(moves_with_heuristic_one)

        game.make_move("computer", best_move)  # Make the best move for the computer.
    else:  # If the Minimax algorithm is chosen.
        best_move = None
        max_eval = -math.inf
        for multiplier in [2, 3, 4]:  # Iterate over possible multipliers.
            # Save the original state before making a move.
            original_number = game.number
            original_computer_score = game.computer_score
            original_player_score = game.player_score

            game.make_move("computer", multiplier)  # Make the move for the computer.

            eval = minimax(game, 4, False)  # Call minimax to evaluate the move.
            if eval > max_eval:  # Update max_eval and best_move if the current evaluation is greater.
                max_eval = eval
                best_move = multiplier

            # Restore the original game state before trying the next move.
            game.number = original_number
            game.computer_score = original_computer_score
            game.player_score = original_player_score

        game.make_move("computer", best_move)  # Make the best move for the computer.

# Main function to run the game.
def main():
    game = Game()  # Create a new game instance.
    game.start_game()  # Start the game by having the player choose a starting number.

    # Determine if the user wants to start the game.
    user_starts = input("Do you want to start the game? (yes/no): ").lower() == "yes"

    # Set the current player based on the user's choice.
    if user_starts:
        current_player = "user"
    else:
        current_player = "computer"

    # Ask the user to choose the algorithm for the computer.
    algorithm = input("Choose algorithm for the computer (MiniM/AB): ").upper()

    # Main game loop, runs until the game is over.
    while not game.is_game_over():
        if current_player == "user":  # If it's the user's turn.
            print("\nCurrent number:", game.number)
            print("Your turn.")
            # Ask the user to choose a multiplier.
            multiplier = int(input("Choose a multiplier (2, 3, or 4): "))
            # Ensure the multiplier is valid.
            while multiplier not in [2, 3, 4]:
                multiplier = int(input("Invalid multiplier. Choose again (2, 3, or 4): "))
            game.make_move("user", multiplier)  # Make the move for the user.
            current_player = "computer"  # Switch the turn to the computer.
        else:  # If it's the computer's turn.
            print("\nCurrent number:", game.number)
            print("Computer's turn.")
            computer_move(game, algorithm)  # The computer makes its move.
            current_player = "user"  # Switch the turn to the user.
        game.print_scores()  # Print the current scores.

    # Game over logic.
    print("\nCurrent number:", game.number)
    print("\nGame over!")
    winner = game.determine_winner()  # Determine the winner.
    print("Winner:", winner)

    # Ask if the user wants to play again.
    play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"
    if play_again:
        main()  # Restart the game.
    else:
        print("Thanks for playing!")  # Exit the game.

# Python's way to run the main function if the file is executed directly.
if __name__ == "__main__":
    main()
