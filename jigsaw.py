"""
Author: Arsene Bwasisi
Description: This program reads in a file with ordered jigsaw puzzle pieces,
             and assembles them in a specific structure. From the file the
             program puts the pieces into a list and locates pieces that
             are next to each other either left-right and top-bottom. 
             The resulting puzzle is printed out.
"""

def read_pieces_file():
    """
    Function will prompt the user for a filename, opens that file, read the
    information, and process the data into a 2d list.
    It returns: two integer value representing the width and height of the
    puzzle, as well as a 2d list containing the puzzle pieces.
    """

    puzzle_file = input('')
    open_file = open(puzzle_file, 'r')
    container = []
    pieces = []

    for line in open_file:
        if line[0] != '#' and line[0] != '\n':
            container.append(line)

    sizes = container.pop(0)
    width = int(sizes[0])
    height = int(sizes[2])

    for piece in container:
        sub_list = piece.split()
        pieces.append(sub_list)

    open_file.close()

    return width, height, pieces

def build_empty_board(wid, hei):
    """ 
    Function builds a 2d list of size wid*by*hei containing None objects.
    Returns: the 2d list with None values.
    wid: The width of the puzzle.
    hei: Height of the puzzle.
    """

    board = []

    for y in range(wid):
        sub_list = []
        for x in range(hei):
            sub_list.append(None)

        board.append(sub_list)

    return board

def match_LR(left,right):
    """ 
    Fucntion looks at value in the left list and checks whether its
    the same as the reversed version of a value in right list.
    Returns: A boolean indicating whether pieces should be place 
    together in the specified order(top, bottom).
    left: Left puzzle piece.
    right: Right puzzle piece.
    """

    if left[1] == right[3][::-1]:
        return True

    return False

def match_TB(top,bot):
    """ 
    Fucntion looks at value in the top list and checks whether its
    the same as the reversed version of a value in bot list.
    Returns: A boolean indicating whether pieces should be place 
    together in the specified order(left, right).
    top: Top puzzle piece.
    bot: Bottom puzzle piece.
    """

    if top[2] == bot[0][::-1]:
        return True

    return False

def piece_to_strs(piece):
    """ 
    Function will convert the puzzle piece into a format in which it
    will be printed as.
    Returns: A list of length five and items in list lenght five.
    piece: A single puzzle piece.
    """

    column = []
    bottom = ' ' + piece[2] + ' '
    column.append(bottom)

    for i in range(3):
        # will collect a single character in each iteration
        # and add with space to make one character
        middle = piece[3][i] + '   ' + piece[1][-(i+1)]
        column.append(middle)

    top = ' ' + piece[0] + ' '
    column.append(top)

    return column

def join_LR(left, right):
    """ 
    Function will join two list, left and right into one list.
    Returns: A joint list(left and right).
    left: Left puzzle piece.
    right: Right puzzle piece.
    """

    joint_list = []
    idx = 0

    for string in left:
        joint_str = string[:-1] + right[idx]
        joint_list.append(joint_str)
        idx += 1

    return joint_list

def join_TB(top, bot):
    """ 
    Function will join two list, top and bottom into one list.
    Returns: A joint list(top and bottom).
    top: Top puzzle piece.
    bot: Bottom puzzle piece.
    """

    for string in top:
        bot.append(string)

    return bot

def  print_strs(strs):
    """
    Function will print out values in strs, starting with the final
    value of the list.
    Returns: None
    strs: Joint list of puzzle pieces form bottom to top.
    """

    i = len(strs)

    while i > 0:
        
        # If index is divisble by 5 don't print
        # This reduces clutter of extra pieces
        if (i-1)%5 != 0 or i-1 == 0:
            print(strs[i-1])

        i -= 1

def fill_board(board, wid,hei, pieces):
    """Given an empty board (that is, a list-of-lists, filled with None's),
       and a set of pieces, searches to find the right pieces to fill the
       board.

       Finds the pieces by searching through the piece list, and matching
       edges to the bottom and left edge of already-found pieces.  The
       bottom edge of the puzzle is represented by "---" edges, and the left
       edge is represented by "|||" edges.  (The same is true for the right
       and top, but this function doesn't care about that.)

       This function always assumes that we have the perfect number of
       pieces to fill the board, and that there are no ambiguities; it doesn't
       do any backtracking, as it doesn't consider the possibility that it
       might ever fail to find a solution.

       When the function returns, the board has been completely populated with
       piece objects.
    """

    for y in range(0,hei):
        for x in range(0,wid):
            for i in range(len(pieces)):
                piece = pieces[i]

                # look for the bottom left piece of the puzzle
                # this piece will have '|||' as its last value
                # and '---' as its second to last
                if x==0:
                    if piece[3] != "|||":
                        continue
                else:
                    # compare a piece in board to the current piece
                    # in the iteration to see if they can be placed
                    # in the specified order
                    left = board[x-1][y]
                    if not match_LR(left, piece):
                        continue

                if y==0:
                    if piece[2] != "---":
                        continue
                else:
                    bot = board[x][y-1]
                    if not match_TB(piece, bot):
                        continue

                # sets board at specified index to current piece
                # removes piece from pieces list
                board[x][y] = piece
                pieces = pieces[:i]+pieces[i+1:]
                break

            assert board[x][y] is not None, (x,y, board, pieces)



def main():
    """Queries the user for a filename, then reads that file as a list of
       jigsaw puzzle pieces; each piece is represented as a tuple of 4
       3-character strings, representing the 4 edges of the piece, staring
       at the top (with the leftmost character) and proceeding through all
       of the characters in clockwise order.

       Solves the jigsaw, and prints out a depiction of the puzzle at the
       end.
    """

    (wid,hei, pieces) = read_pieces_file()

    board = build_empty_board(wid,hei)
    fill_board(board, wid,hei, pieces)

    # call piece_to_strs()
    # combine left-right pieces within second loop
    # then combine top to bottom pieces within first loop
    # print results
    output_lines = []
    for y in range(hei):
        this_row = [""]*5
        for x in range(wid):
            this_piece = piece_to_strs(board[x][y])
            this_row = join_LR(this_row, this_piece)
        output_lines = join_TB(this_row, output_lines)

    print_strs(output_lines)

main()
