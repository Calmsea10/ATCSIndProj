# ATCS_checkers
Ennio Sim

Release 1.0 - 5/23/2024

ATCS_checkers uses the negamax algorithm to play a game of checkers against the user. 

The pygame library is required to run this program. For information on installing pygame, visit https://www.pygame.org.
To run this program, run ATCS_checkers.py. A pygame window should open. 
You play as white. Click on any white piece to select it. Selected pieces are outlined in yellow.
Valid moves are represented as solid yellow circles. Click on a valid move to move to that location.
To select another piece, click anywhere else to deselect the current piece, then click again to select another piece.
Captures are forced. If multiple pieces can capture, you may choose which capture to take.
After you have moved, clicking anywhere will end your turn and the computer will move.

Known Issues:
*Placeholder sprites for king pieces
*Poor performance on negamax implementation
*Negamax does not implement quiet position search
*Negamax does not force captures for king pieces