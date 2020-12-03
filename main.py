import pygame
from pygame import mixer
import sys
import random
from time import sleep


# Displays the welcome Message
def welcome_msg():
    # Font for the current menu
    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 64)
    font2 = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 32)

    while True:
        screen.blit(background, (0, 0))

        welcome_message = font.render("Welcome to Tic-Tac-Toe!", True, (0, 0, 0))
        screen.blit(welcome_message, (27, 100))

        enter_message = font2.render("Press ENTER to continue", True, (0, 0, 0))
        screen.blit(enter_message, (200, 300))

        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        pygame.display.update()


# Gets the player's choice of game mode and returns it
def game_mode():
    # Font for the current menu
    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 20)

    cursor_selection = 1

    cursor_position = (115, 252)

    while True:
        # Header and backround

        # Background
        screen.blit(background, (0, 0))

        # Tic-Tac-Toe header text
        font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
        header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
        screen.blit(header, (25, 30))

        # Choice 1 button
        choice_1_button = font.render("1. Do you want to play against the computer", True, (0, 0, 0))
        screen.blit(choice_1_button, (165, 250))

        # Or button
        or_button = font.render("(or)", True, (0, 0, 0))
        screen.blit(or_button, (375, 290))

        # Choice 2 button
        choice_2_button = font.render("2. Do you want to play against another player ", True, (0, 0, 0))
        screen.blit(choice_2_button, (165, 330))

        select_message = font.render("(Press ENTER to select)", True, (0, 0, 0))
        screen.blit(select_message, (275, 380))

        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # To check if a key is pressed
            if event.type == pygame.KEYDOWN:
                # To check if DOWN key or UP key is pressed
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:

                    # Change the cursor position when arrow key is pressed
                    if cursor_selection == 1:
                        cursor_selection = 2
                    else:
                        cursor_selection = 1

                # Returns the selection when ENTER key is pressed
                if event.key == pygame.K_RETURN:
                    return cursor_selection

            # To check if a key is released
            if event.type == pygame.KEYUP:
                # To check if DOWN key or UP key is released
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:

                    # Change the position of the cursor based on the selection
                    if cursor_selection == 1:
                        cursor_position = (115, 252)
                    else:
                        cursor_position = (115, 332)

        # Displays the cursor
        screen.blit(cursor, cursor_position)

        # Updates the display
        pygame.display.update()


# Game mode 1 (1 player)
def game_1(score):
    while True:

        moves_count = 0

        # Initial board
        board_list = ['#']
        for i in range(9):
            board_list.append(empty_marker)

        # Initially the winning condition is set False
        winning = False

        players = ['Computer', 'Player']
        random.shuffle(players)

        display_firstplayer_msg(players[0])

        # Loop until there's a winner
        while not winning:

            # Player_1 turn

            # Header and backround

            # Background
            screen.blit(background, (0, 0))

            # Tic-Tac-Toe header text
            font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
            header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
            screen.blit(header, (25, 30))

            for event in pygame.event.get():

                # To quit the game if the close button is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Displaying moves count
            moves_count += 1
            font_moves = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
            moves = font_moves.render("Move : ", True, (0, 0, 0))
            moves_count_str = font_moves.render(str(moves_count), True, (0, 0, 0))
            screen.blit(moves, (20, 320))
            screen.blit(moves_count_str, (128, 321))

            # Gets the player 1 choice of position
            player_message = font.render(f"{players[0]} (X) turn", True, (0, 0, 0))
            screen.blit(player_message, (275, 550))
            if players[0] == 'Computer':
                position = computer_choice(board_list, player_1_marker, player_2_marker)
            else:
                position = player_choice(board_list)

            # Place the marker in the user's postion
            board_list = place_marker(board_list, player_1_marker, position)

            display_board(board_list)

            # Checking if player_1 has won the game
            if isWin(board_list):
                if players[0] == 'Computer':
                    result = 3
                    display_result(result, board_list)
                    score[0] += 1
                    return score
                else:
                    result = 1
                    display_result(result, board_list)
                    score[1] += 1
                    return score

            # Condition to check if the game is a draw
            if isFull(board_list):
                result = 0
                display_result(result, board_list)
                return score

            # Player_2 turn

            # Header and backround

            # Background
            screen.blit(background, (0, 0))

            # Tic-Tac-Toe header text
            font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
            header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
            screen.blit(header, (25, 30))

            # Displaying moves count
            moves_count += 1
            font_moves = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
            moves = font_moves.render("Move : ", True, (0, 0, 0))
            moves_count_str = font_moves.render(str(moves_count), True, (0, 0, 0))
            screen.blit(moves, (20, 320))
            screen.blit(moves_count_str, (128, 321))

            # Gets the player 2 choice of position
            player_message = font.render(f"{players[1]} (O) turn", True, (0, 0, 0))
            screen.blit(player_message, (275, 550))
            if players[1] == 'Computer':
                position = computer_choice(board_list, player_2_marker, player_1_marker)
            else:
                position = player_choice(board_list)

            # Place the marker in the user's postion
            board_list = place_marker(board_list, player_2_marker, position)

            display_board(board_list)

            # Checking if player_1 has won the game
            if isWin(board_list):
                if players[1] == 'Computer':
                    result = 3
                    display_result(result, board_list)
                    score[0] += 1
                    return score
                else:
                    result = 1
                    display_result(result, board_list)
                    score[1] += 1
                    return score

            # Condition to check if the game is a draw
            if isFull(board_list):
                result = 0
                display_result(result, board_list)
                return score

            pygame.display.update()

        pygame.display.update()


# Game mode 2 (2 players)
def game_2(score):
    while True:

        moves_count = 0

        # Initial board
        board_list = ['#']
        for i in range(9):
            board_list.append(empty_marker)

        # Initially the winning condition is set False
        winning = False

        # Loop until there's a winner
        while not winning:
            # Player_1 turn

            # Header and backround

            # Background
            screen.blit(background, (0, 0))

            # Tic-Tac-Toe header text
            font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
            header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
            screen.blit(header, (25, 30))

            for event in pygame.event.get():

                # To quit the game if the close button is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Displaying moves count
            moves_count += 1
            font_moves = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
            moves = font_moves.render("Move : ", True, (0, 0, 0))
            moves_count_str = font_moves.render(str(moves_count), True, (0, 0, 0))
            screen.blit(moves, (20, 320))
            screen.blit(moves_count_str, (128, 321))

            # Gets the user choice of position
            player_message = font.render("Player 1 (X) turn", True, (0, 0, 0))
            screen.blit(player_message, (275, 550))
            position = player_choice(board_list)

            # Place the marker in the user's postion
            board_list = place_marker(board_list, player_1_marker, position)

            display_board(board_list)

            # Checking if player_1 has won the game
            if isWin(board_list):
                score[0] += 1
                result = 1
                display_result(result, board_list)
                return score

            # Condition to check if the game is a draw
            if isFull(board_list):
                result = 0
                display_result(result, board_list)
                return score

            # Player_2 turn

            # Header and backround

            # Background
            screen.blit(background, (0, 0))

            # Tic-Tac-Toe header text
            font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
            header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
            screen.blit(header, (25, 30))

            # Displaying moves count
            moves_count += 1
            font_moves = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
            moves = font_moves.render("Move : ", True, (0, 0, 0))
            moves_count_str = font_moves.render(str(moves_count), True, (0, 0, 0))
            screen.blit(moves, (20, 320))
            screen.blit(moves_count_str, (128, 321))

            # Gets the user choice of position
            player_message = font.render("Player 2 (O) turn", True, (0, 0, 0))
            screen.blit(player_message, (275, 550))
            position = player_choice(board_list)

            # Place the marker in the user's postion
            board_list = place_marker(board_list, player_2_marker, position)

            display_board(board_list)

            # Checking if player_1 has won the game
            if isWin(board_list):
                score[1] += 1
                result = 2
                display_result(result, board_list)
                return score

            # Condition to check if the game is a draw
            if isFull(board_list):
                result = 0
                display_result(result, board_list)
                return score

            pygame.display.update()

        pygame.display.update()


# Conditon to check if the player has won
def isWin(board):
    if board[1] == board[2] == board[3] != empty_marker:
        return True
    elif board[4] == board[5] == board[6] != empty_marker:
        return True
    elif board[7] == board[8] == board[9] != empty_marker:
        return True
    elif board[1] == board[4] == board[7] != empty_marker:
        return True
    elif board[2] == board[5] == board[8] != empty_marker:
        return True
    elif board[3] == board[6] == board[9] != empty_marker:
        return True
    elif board[3] == board[5] == board[7] != empty_marker:
        return True
    elif board[1] == board[5] == board[9] != empty_marker:
        return True
    else:
        return False


# Checks and return if win is possible in the current position
def isWinPossible(board, marker, position):
    board[position] = marker
    result = isWin(board)
    board[position] = empty_marker
    return result


# Condition to check if the position is free
def isSpacefree(board, position):
    return board[position] == empty_marker


# Condition to check if the board is full
def isFull(board):
    for pos in board:
        if pos == empty_marker:
            return False
    return True


# Rerurns the win position to place the cross
def win_position(board):
    if board[1] == board[2] == board[3] != empty_marker:
        return 1
    elif board[4] == board[5] == board[6] != empty_marker:
        return 2
    elif board[7] == board[8] == board[9] != empty_marker:
        return 3
    elif board[1] == board[4] == board[7] != empty_marker:
        return 4
    elif board[2] == board[5] == board[8] != empty_marker:
        return 5
    elif board[3] == board[6] == board[9] != empty_marker:
        return 6
    elif board[3] == board[5] == board[7] != empty_marker:
        return 7
    elif board[1] == board[5] == board[9] != empty_marker:
        return 8
    else:
        return 0


# Displays the board
def display_board(board_list):
    board_matrix = pygame.image.load("Assets/Board/Board.png").convert_alpha()

    screen.blit(board_matrix, (250, 200))
    # pygame.draw.rect(screen, (0, 0, 0), (265, 200, 77, 77))

    # Displaying the marker at position 1
    screen.blit(board_list[1], (265, 405))
    # Displaying the marker at position 2
    screen.blit(board_list[2], (360, 405))
    # Displaying the marker at position 3
    screen.blit(board_list[3], (450, 405))
    # Displaying the marker at position 4
    screen.blit(board_list[4], (265, 300))
    # Displaying the marker at position 5
    screen.blit(board_list[5], (360, 300))
    # Displaying the marker at position 6
    screen.blit(board_list[6], (450, 300))
    # Displaying the marker at position 7
    screen.blit(board_list[7], (265, 210))
    # Displaying the marker at position 8
    screen.blit(board_list[8], (360, 210))
    # Displaying the marker at position 9
    screen.blit(board_list[9], (450, 210))

    for event in pygame.event.get():

        # To quit the game if the close button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


# Displays the result after the game has ended
def display_result(result, board):
    while True:
        # Header and backround

        # Background
        screen.blit(background, (0, 0))

        # Tic-Tac-Toe header text
        font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
        header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
        screen.blit(header, (25, 30))

        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for event in pygame.event.get():
            # Returning when ENTER key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        font2 = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 45)
        cong_msg = font2.render("CONGRATULATIONS!", True, (0, 0, 0))

        if result == 1:
            winner_msg = font.render("Player 1 has won the game", True, (0, 0, 0))
            screen.blit(cong_msg, (150, 150))
            screen.blit(winner_msg, (185, 520))
        elif result == 2:
            winner_msg = font.render("Player 2 has won the game", True, (0, 0, 0))
            screen.blit(cong_msg, (150, 150))
            screen.blit(winner_msg, (185, 520))
        elif result == 3:
            winner_msg = font.render("Sorry, you lost to the computer", True, (0, 0, 0))
            screen.blit(winner_msg, (150, 520))
        else:
            winner_msg = font.render("The game has ended in a draw!", True, (0, 0, 0))
            screen.blit(winner_msg, (150, 520))

        font3 = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 20)
        enter_message = font3.render("(Press ENTER to continue)", True, (0, 0, 0))
        # screen.blit(enter_message, (265, 565))

        if win_position(board) == 4:
            screen.blit(cross_vertical, (275, 205))
        elif win_position(board) == 5:
            screen.blit(cross_vertical, (375, 205))
        elif win_position(board) == 6:
            screen.blit(cross_vertical, (465, 205))
        elif win_position(board) == 3:
            screen.blit(cross_horizontal, (250, 225))
        elif win_position(board) == 2:
            screen.blit(cross_horizontal, (250, 320))
        elif win_position(board) == 1:
            screen.blit(cross_horizontal, (250, 425))
        elif win_position(board) == 7:
            screen.blit(cross_diagonal1, (250, 202))
        elif win_position(board) == 8:
            screen.blit(cross_diagonal2, (250, 202))
        display_board(board)

        sleep(3)
        return

        pygame.display.update()


# Returns what user wants to do after the game
def display_replay():
    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 20)

    cursor_selection = 1

    cursor_position = (165, 252)

    while True:
        # Header and backround

        # Background
        screen.blit(background, (0, 0))

        # Tic-Tac-Toe header text
        font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
        header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
        screen.blit(header, (25, 30))

        # Choice 1 button
        choice_1_button = font.render("1. Do you want to continue playing", True, (0, 0, 0))
        screen.blit(choice_1_button, (200, 250))

        # Choice 2 button
        choice_2_button = font.render("2. Do you want to change the game mode ", True, (0, 0, 0))
        screen.blit(choice_2_button, (200, 300))

        # Choice 3 button
        choice_3_button = font.render("3. Do you want to quit", True, (0, 0, 0))
        screen.blit(choice_3_button, (200, 350))

        select_message = font.render("(Press ENTER to select)", True, (0, 0, 0))
        screen.blit(select_message, (265, 420))

        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # To check if a key is pressed
            if event.type == pygame.KEYDOWN:
                # To check if DOWN key pressed
                if event.key == pygame.K_DOWN:

                    # To change the selection of the cursor when DOWN key is pressed
                    if cursor_selection == 1:
                        cursor_selection = 2
                    elif cursor_selection == 2:
                        cursor_selection = 3
                    else:
                        cursor_selection = 1

                if event.key == pygame.K_UP:

                    # To change the selection of the cursor when UP key is pressed
                    if cursor_selection == 1:
                        cursor_selection = 3
                    elif cursor_selection == 2:
                        cursor_selection = 1
                    else:
                        cursor_selection = 2

                if event.key == pygame.K_RETURN:
                    return cursor_selection

            # To check if a key is released
            if event.type == pygame.KEYUP:
                # To check if DOWN key or UP key is released
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:

                    # Change the position of the cursor based on the selection
                    if cursor_selection == 1:
                        cursor_position = (165, 252)
                    elif cursor_selection == 2:
                        cursor_position = (165, 302)
                    else:
                        cursor_position = (165, 352)

        # Displays the cursor
        screen.blit(cursor, cursor_position)

        pygame.display.update()


# Displays which player goes first
def display_firstplayer_msg(player):
    # Header and backround

    # Background
    screen.blit(background, (0, 0))

    # Tic-Tac-Toe header text
    font_header = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 120)
    header = font_header.render("TIC-TAC-TOE", True, (0, 0, 0))
    screen.blit(header, (25, 30))

    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
    first_player_msg = font.render(f"{player} is (X) and goes first", True, (0, 0, 0))
    screen.blit(first_player_msg, (200, 300))
    pygame.display.update()
    sleep(2)


# Displays the scores
def display_score(scores):
    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 30)
    score = font.render("Score", True, (0, 0, 0))
    screen.blit(score, (700, 300))


# Updates the board with the marker
def place_marker(board, marker, position):
    board[position] = marker
    return board


# Returns the player's choice of position
def player_choice(board):
    display_board(board)
    while True:
        click = False
        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # To check if the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    click = True

            # Getting the mouse Co-ordinates
            mx, my = pygame.mouse.get_pos()

            # Return position 1 when clicked in its region
            if click == True and mx in range(245, 353) and my in range(384, 513):
                position = 1
                if isSpacefree(board, position):
                    return position

            # Return position 2 when clicked in its region
            if click == True and mx in range(355, 435) and my in range(384, 513):
                position = 2
                if isSpacefree(board, position):
                    return position

            # Return position 3 when clicked in its region
            if click == True and mx in range(440, 550) and my in range(384, 513):
                position = 3
                if isSpacefree(board, position):
                    return position

            # Return position 4 when clicked in its region
            if click == True and mx in range(245, 353) and my in range(291, 380):
                position = 4
                if isSpacefree(board, position):
                    return position

            # Return position 5 when clicked in its region
            if click == True and mx in range(355, 435) and my in range(291, 380):
                position = 5
                if isSpacefree(board, position):
                    return position

            # Return position 6 when clicked in its region
            if click == True and mx in range(440, 550) and my in range(291, 380):
                position = 6
                if isSpacefree(board, position):
                    return position

            # Return position 7 when clicked in its region
            if click == True and mx in range(245, 353) and my in range(194, 288):
                position = 7
                if isSpacefree(board, position):
                    return position

            # Return position 8 when clicked in its region
            if click == True and mx in range(355, 435) and my in range(194, 288):
                position = 8
                if isSpacefree(board, position):
                    return position

            # Return position 9 when clicked in its region
            if click == True and mx in range(440, 550) and my in range(194, 288):
                position = 9
                if isSpacefree(board, position):
                    return position

            pygame.display.update()


# Returns the computer's choice of position
def computer_choice(board, computer_marker, player_marker):
    # Scanning for all available positions
    available_positions = []
    for pos in range(1, 10):
        if isSpacefree(board, pos):
            available_positions.append(pos)

    for pos in available_positions:
        # Checking is computer has a win possibility
        if isWinPossible(board, computer_marker, pos):
            return pos
    for pos in available_positions:
        # Checking if player has a win possibility
        if isWinPossible(board, player_marker, pos):
            return pos
    # Return a random position if no win is possible
    return random.choice(available_positions)


if __name__ == "__main__":
    # Initializing Pygame
    pygame.init()

    # Creating the screen
    screen = pygame.display.set_mode((800, 600))

    # Background black screen+
    screen.fill((0, 0, 0))

    # Title and Icon
    pygame.display.set_caption("Tic-Tac-Toe")
    icon = pygame.image.load("Assets/Icon/Icon.png").convert_alpha()
    pygame.display.set_icon(icon)

    # Background Image
    background = pygame.image.load("Assets/Background/Background.png").convert_alpha()

    # Importing the cursor
    cursor = pygame.image.load("Assets/Cursor/Cursor.png").convert_alpha()

    # Font
    font = pygame.font.FontType(r'Assets/Font/freesansbold.ttf', 32)

    # Importing the 'X' and 'O' marker and assigning them
    player_1_marker = pygame.image.load("Assets/Board/X_marker.png").convert_alpha()
    player_2_marker = pygame.image.load("Assets/Board/O_Marker.png").convert_alpha()
    empty_marker = pygame.image.load("Assets/Board/Empty_Marker.png").convert_alpha()

    # Importing the crosses
    cross_vertical = pygame.image.load("Assets/Board/Cross_vertical.png").convert_alpha()
    cross_horizontal = pygame.image.load("Assets/Board/Cross_horizontal.png").convert_alpha()
    cross_diagonal1 = pygame.image.load("Assets/Board/Cross_diagonal.png").convert_alpha()
    cross_diagonal2 = pygame.image.load("Assets/Board/Cross_diagonal2.png").convert_alpha()

    mixer.music.load("Assets/Audio/Tic Tac Toe Glow OST - Main Theme - Extended.mp3")
    mixer.music.play(-1)

    score = [0, 0]
    welcome_trigger = True
    game_trigger = True

    game_on = True

    # The game loop
    while game_on:

        for event in pygame.event.get():

            # To quit the game if the close button is clicked
            if event.type == pygame.QUIT:
                game_on = False

        if welcome_trigger:
            # Welcome message
            welcome_msg()

        if game_trigger:
            # Game mode
            mode = game_mode()

        if mode == 1:
            score = game_1(score)
        else:
            score = game_2(score)

        replay = display_replay()

        if replay == 1:
            welcome_trigger = False
            game_trigger = False
        elif replay == 2:
            score = [0, 0]
            welcome_trigger = False
            game_trigger = True
        if replay == 3:
            pygame.quit()
            sys.exit()
        print(score)

        # Updating the display
        pygame.display.update()
