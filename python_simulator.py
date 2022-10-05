from numpy import random


class Tile:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour  # red, white, or zero
        self.even_o_odd = is_even(number)  # returns a string
        self.low_o_high = get_low_o_high(number)

    # Getters, should be no need for setters
    def get_number(self):
        return self.number

    def get_colour(self):
        return self.colour

    def get_even_o_odd(self):
        return self.even_o_odd

    def get_low_o_high(self):
        return self.low_o_high


def get_low_o_high(number_to_check):
    if number_to_check == 0:
        return "zero"
    if 18 >= number_to_check > 0:
        return "low"
    elif number_to_check <= 36:
        return "high"
    else:
        print("ERROR: Number is not 0, 1-18, or 19-36 terminating program")
        exit(1)


def is_even(number_to_check):
    if number_to_check == 0:
        return "zero"
    if number_to_check % 2 == 0:
        return "even"
    else:
        return "odd"


def make_game_board():
    new_board = [Tile(0, "zero")]
    new_board.append(Tile(1, "red"))
    new_board.append(Tile(2, "black"))
    new_board.append(Tile(3, "red"))
    new_board.append(Tile(4, "black"))
    new_board.append(Tile(5, "red"))
    new_board.append(Tile(6, "black"))
    new_board.append(Tile(7, "red"))
    new_board.append(Tile(8, "black"))
    new_board.append(Tile(9, "red"))
    new_board.append(Tile(10, "black"))
    new_board.append(Tile(11, "black"))
    new_board.append(Tile(12, "red"))
    new_board.append(Tile(13, "black"))
    new_board.append(Tile(14, "red"))
    new_board.append(Tile(15, "black"))
    new_board.append(Tile(16, "red"))
    new_board.append(Tile(17, "black"))
    new_board.append(Tile(18, "red"))
    new_board.append(Tile(19, "red"))
    new_board.append(Tile(20, "black"))
    new_board.append(Tile(21, "red"))
    new_board.append(Tile(22, "black"))
    new_board.append(Tile(23, "red"))
    new_board.append(Tile(24, "black"))
    new_board.append(Tile(25, "red"))
    new_board.append(Tile(26, "black"))
    new_board.append(Tile(27, "red"))
    new_board.append(Tile(28, "black"))
    new_board.append(Tile(29, "black"))
    new_board.append(Tile(30, "red"))
    new_board.append(Tile(31, "black"))
    new_board.append(Tile(32, "red"))
    new_board.append(Tile(33, "black"))
    new_board.append(Tile(34, "red"))
    new_board.append(Tile(35, "black"))
    new_board.append(Tile(36, "red"))
    return new_board


STARTING_BALANCE = 100  # in dollars
MINIMUM_BET = 5  # in dollars, per type of bet
MAXIMUM_BET = 165  # in dollars, 500/ 3 rounded down a bit
STARTING_BET = {"colour": "red", "odd_o_even": "even", "low_o_high": "low"}  # easier than randomising it.


def main():
    print("Alex's roulette strategy simulator")
    game_board = make_game_board()  # makes the roulette board and gives the tiles the correct variables.

    balance = STARTING_BALANCE
    bet = STARTING_BET  # colour, odd or even, low or high
    bet_amount = MINIMUM_BET

    # These variables are for stats
    highest_balance = balance
    highest_spin = 0
    lowest_balance = balance
    win_log = []

    num_spins = 0
    while num_spins in range(0, 1001):
        bet_colour = bet["colour"]
        bet_odd_o_even = bet["odd_o_even"]
        bet_low_o_high = bet["low_o_high"]
        # print("My bet:", bet_colour, bet_low_o_high, bet_odd_o_even)

        win_amount = 0
        num_wins = 0

        balance -= bet_amount * 3
        spin = random.randint(0, 36)
        tile_rolled = game_board[spin]

        spin_colour = tile_rolled.get_colour()
        spin_odd_o_even = tile_rolled.get_even_o_odd()
        spin_low_o_high = tile_rolled.get_low_o_high()

        if spin_colour == bet_colour:
            win_amount += bet_amount * 2
            num_wins += 1
        else:
            bet["colour"] = spin_colour

        if spin_odd_o_even == bet_odd_o_even:
            win_amount += bet_amount * 2
            num_wins += 1
        else:
            bet["odd_o_even"] = spin_odd_o_even

        if spin_low_o_high == bet_low_o_high:
            win_amount += bet_amount * 2
            num_wins += 1
        else:
            bet["low_o_high"] = spin_low_o_high

        balance += win_amount

        if balance > highest_balance:
            highest_balance = balance
            highest_spin = num_spins + 1
        elif balance < lowest_balance:
            lowest_balance = balance
        else:
            pass
        win_log.append(num_wins)
        # print("Number rolled:", spin, spin_colour, spin_low_o_high, spin_odd_o_even)
        # print("You won: $" + str(win_amount - (bet_amount * 3)))
        # print("Rolling balance: $" + str(balance))

        num_spins += 1
        if balance < 15:
            break
    # end while loop

    print("Balance after", num_spins , "games:", balance)
    if balance == STARTING_BALANCE:
        print("you win some, you lose some, and sometimes you go round in circles")
    elif balance > STARTING_BALANCE:
        print("You made a profit of: $" + str((balance - STARTING_BALANCE)))
    elif balance >= 0:
        print("You lost $" + str(STARTING_BALANCE - balance))
    else:
        print("You are in debt, you owe: $" + str(balance * -1))

    print("Highest balance was: $" + str(highest_balance) + " on spin: " + str(highest_spin))
    print("Lowest balance was: $" + str(lowest_balance))

    no_wins = 0
    two_third_wins = 0
    two_to_one_wins = 0
    three_to_one_wins = 0
    for x in win_log:
        if x == 0:
            no_wins += 1
        elif x == 1:
            two_third_wins += 1
        elif x == 2:
            two_to_one_wins += 1
        elif x == 3:
            three_to_one_wins += 1
        else:
            print("Something went wrong")

    print("Percent of 'no bets win': " + str((no_wins / num_spins) * 100) + "%")
    print("Percent of two thirds back: " + str((two_third_wins / num_spins) * 100) + "%")
    print("Percent of two to one: " + str((two_to_one_wins / num_spins) * 100) + "%")
    print("Percent of three to one': " + str((three_to_one_wins / num_spins) * 100) + "%")


if __name__ == "__main__":
    main()
