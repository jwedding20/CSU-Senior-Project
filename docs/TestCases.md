Jeff Wedding

Computer Science (B.S)

Dr. Sean Hayes

| Test No. | Action | Input | Expected Output | Actual Output | P/F |
| --- | --- | --- | --- | --- | --- |
| 1   | Launch game | “Python3 main.py” | Game opens | Game opens | P   |
| 2   | Players can move once their pawn forward and diagonally | Click on pawn then click on open space | Pawn moves |     |     |
| 3   | Available spots to move are highlighted | Click on pawn | Pawn and available spots to jump are highlighted |     |     |
| 4   | Players’ turn ends once it is over | Click on open space | Other player is able to move |     |     |
| 5   | A piece that is clicked on will no longer be movable if a different part of the screen is clicked | Click on a pawn and then click on a different part of the screen | Pawn will no longer be movable |     |     |
| 6   | Pawn turns into king when it reaches the other side of the board | Reach other side of board with pawn | Pawn will become king |     |     |
| 7   | Game states the winner | Win game with black | “Black wins” |     |     |
| 8   | Players will ‘take’ pawns when they jump over them | Jump over a pawn | Pawn will disappear |     |     |
| 9   | Invalid moves are rejected | Click on a pawn to move | Spots that are occupied |     |     |
| 10  | Game will state the game has ended with no winner if a player exits the game | Exit out of game | “No winner. Game exited.” |     |     |
| 11  | Working chat room | “Test” | “Player one: ‘Test’” |     |     |
| 12  | Help section | Click on the ‘?’ | Blurb explaining the rules of checkers |     |     |
| 13  | Players must jump pawns if they are able to | Set up a pawn that can be jumped | Player is forced to jump the available pawn |     |     |
| 14  | A message will appear saying who’s turn it is | Player 1 makes the first move | “Player 2’s move” |     |     |
| 15  | Players are put into a waiting room until the other play joins | Player 1 joins the game | “Waiting for Player 2 to join.” |     |     |
| 16  | Game closes when there is a winner | Player 1 wins the game | “Player 1 wins!” (on command line) |     |     |