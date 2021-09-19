from numpy import reshape
from string import ascii_uppercase
from itertools import groupby

'''Connect-Four Game winner checker
There are two players that play as 'Yellow' or 'Red'. This script checks if the player won after making a move and returns his color.

This tool accepts a list where elements are formatted as follows: letter_color  where letter spans from 'A' to 'G' and color is either 'Yellow' or 'Red'

This script requires the 'numpy' and 'itertools' modules be installed within the  Python Environment you are running this script in.
This script was created under Python 3.9.5, probably will stay functional in future versions, might face some problems regardless

This file can also be imported and contains the following function:
    * who_is_winner - returns the color of the player that won
'''

def who_is_winner(all_moves):

    """Sees who won the connect-four game

    :param all_moves: all the moves done by the two players
    :type all_moves: list
    :returns: 'Red' or 'Yellow' depending on who won
    :rtype: str
    """

    board = reshape(42*['      '], (6, 7))
    # fill up the board one move at a time
    for player_move in all_moves:
        letter, color = player_move.split('_')
        index_of_column_of_move = ascii_uppercase.index(letter)
        column_of_move = board[:, index_of_column_of_move]

        # we loop through each element of the reversed column affected by the player's move
        # because in a game of connect four the ball falls to the bottom
        # and by reversing the list we bring the bottom to the top
        # enabling to search for empty space and correctly inserting the ball
        # which will later on be "reversed again" to show the actual desired state of the board
        counter = -1
        reverse = list(column_of_move[::-1])
        for space in reverse:
            counter += 1
            if space == '      ':
                reverse[counter] = color
                # "reversed again"
                column_after_move = reverse[::-1]
                # modify column in the orignal board
                board[:, index_of_column_of_move] = column_after_move
                break
        # check if someone won:

        # check columns
        for col in range(board.shape[1]):

            consecutive_counts = [(k, sum(1 for i in g)) for k, g in groupby(list(board[:, col]))]
            for current_element,count in consecutive_counts:
                if current_element == color:
                    # if count of color>=4
                    if count >= 4:
                        # return color
                        return current_element

        # check rows
        for row in range(board.shape[0]):

            consecutive_counts = [(k, sum(1 for i in g)) for k, g in groupby(list(board[row, :]))]
            for current_element,count in consecutive_counts:
                if current_element == color:
                    # if count of color>=4
                    if count >= 4:
                        # return color
                        return current_element

        
        # diags from left to right
        diags = [board[::-1, :].diagonal(i) for i in range(-board.shape[0]+1, board.shape[1])]
        # diags from right to left
        diags.extend(board.diagonal(i) for i in range(board.shape[1]-1, -board.shape[0], -1))
        diags_list = [n.tolist() for n in diags]
        # check diagonals
        for diag in diags_list:
            consecutive_counts = [(k, sum(1 for i in g)) for k, g in groupby(diag)]
            for current_element,count in consecutive_counts:
                if current_element == color:
                    # if count of color>=4
                    if count >= 4:
                        # return color
                        return current_element
    # after all moves are done, and winner is not returned (which means no one won)
    return 'Draw'
