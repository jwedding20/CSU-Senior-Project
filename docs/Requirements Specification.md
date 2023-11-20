Jeffrey Wedding

Computer Science (B.S)

Dr. Sean Hayes

Requirements Specification

1.
  1. ID – 1
  2. Type – Appearance
  3. Description – Create an 8x8 visual board that the game will be played on.
  4. Rationale – The game needs a board that will be played on. This will make it easier for the players to visualize the game and make moves.
  5. Fit Criterion – The board will be visible once it is implemented.
  6. Priority – High
  7. Dependencies – n/a
2.
  1. ID – 2
  2. Type – Appearance
  3. Description – Create the pieces (red or black dots) that players will use to move.
  4. Rationale – The players need to know where their pieces are.
  5. Fit Criterion – The pieces will be visible once they are implemented.
  6. Priority – High
  7. Dependencies – 1
3.
  1. ID – 3
  2. Type – Usability
  3. Description – Small portion of the screen lets players know how many of their pieces remain.
  4. Rationale – Having a part of the screen dedicated to how many pieces each player has remaining will be much more convenient to the player than having to manually count how many pieces they have left.
  5. Fit Criterion – The "piece count" will be visible to players once it is implemented.
  6. Priority – Low
  7. Dependencies – n/a
4.
  1. ID – 4
  2. Type – Functionality
  3. Description – When a player clicks on their piece, they can then move it.
  4. Rationale – Players must be able to move their pieces.
  5. Fit Criterion – The piece will have a Boolean property that will determine if it has been selected or not.
  6. Priority – High
  7. Dependencies – 8
5.
  1. ID – 5
  2. Type – Functionality
  3. Description – When a player clicks on an open space after they selected one of their pieces, that piece moves to the open space that was clicked on. The turn will then end.
  4. Rationale – Players need to be able to move their pieces.
  5. Fit Criterion – The selected piece will be moved to the desired open space.
  6. Priority – High
  7. Dependencies – 4, 8
6.
  1. ID – 6
  2. Type – Functionality
  3. Description – If a player clicks on a piece and then clicks on a part of the screen that is not an open space, the piece will no longer be moveable.
  4. Rationale – Players may select a piece to move and then change their mind.
  5. Fit Criterion – The Boolean property of the piece will be set to false.
  6. Priority – High
  7. Dependencies – 4
7. .
  1. ID – 7
  2. Type – Functionality
  3. Description – If a player's piece reaches the opponent's side of the board, that piece will turn into a king.
  4. Rationale – King pieces are a critical part of the game of checkers.
  5. Fit Criterion – The piece will have a Boolean property that determines whether it is a king piece.
  6. Priority – High
  7. Dependencies – 8, 9
8.
  1. ID – 8
  2. Type – Functionality
  3. Description – The board will be implemented as a 2-dimensional array of Booleans. Each entry in the array can either be a 0 (space is empty) or 1 (space is occupied).
  4. Rationale – Implementing the board as a 2-dimensional array is the easiest way to visualize the board and where pieces are for me. This will also make it easier when selecting pieces to move.
  5. Fit Criterion – Program will run without error if this is implemented correctly.
  6. Priority – High
  7. Dependencies – n/a
9.
  1. ID – 9
  2. Type – Functionality
  3. Description – A "piece" class will be created containing information about pieces such as which team they are on, whether they have been selected, whether they are a king, etc.
  4. Rationale – This will make it much easier for me to write code for the rest of the project.
  5. Fit Criterion – Program will run without error if this is implemented correctly.
  6. Priority – Medium
  7. Dependencies – n/a
10.
  1. ID – 10
  2. Type – Appearance
  3. Description – The program will alert a player when it is their turn.
  4. Rationale – Player's need to know when they are free to make a move.
  5. Fit Criterion – Player's will be able to see whose turn it is.
  6. Priority – Medium
  7. Dependencies – 5
11.
  1. ID – 11
  2. Type – Usability
  3. Description – Once the game is over, there will be an option to play again. If both players agree, the game will reset.
  4. Rationale – Players may want to play more than one game.
  5. Fit Criterion – Players will see the message pop up at the end of the game.
  6. Priority – Low
  7. Dependencies – 22
12.
  1. ID – 12
  2. Type – Appearance
  3. Description – The win total of each player will be displayed.
  4. Rationale – If multiple games are played then players will want to know how many games each player has won.
  5. Fit Criterion – The win total of each player will be visible.
  6. Priority – Low
  7. Dependencies – n/a
13.
  1. ID – 13
  2. Type – Functionality
  3. Description – Players will be prompted to double or triple jump if possible.
  4. Rationale – Double and triple jumping is an essential part of the game of checkers.
  5. Fit Criterion – The spaces that can be used to double and triple jump will be highlighted.
  6. Priority – High
  7. Dependencies – 1, 5, 8
14.
  1. ID – 14
  2. Type – Functionality
  3. Description – Pieces will be able to move forward and diagonally forward.
  4. Rationale – Pieces need to be able to move.
  5. Fit Criterion – Pieces will visibly move.
  6. Priority – High
  7. Dependencies – 13
15.
  1. ID – 15
  2. Type – Functionality
  3. Description – The king piece will be able to move diagonally, forwards, and backwards.
  4. Rationale – King pieces are an essential part of the game of checkers.
  5. Fit Criterion – Pieces will visibly move.
  6. Priority – High
  7. Dependencies – 13
16.
  1. ID – 16
  2. Type – Functionality
  3. Description – Players will be put into a waiting room until both players join the game.
  4. Rationale – Players likely will not join the game at the same exact time, so a waiting room is necessary.
  5. Fit Criterion – A message will come across the screen letting players know that they are waiting for the other player to join.
  6. Priority – Low
  7. Dependencies – n/a
17.
  1. ID – 17
  2. Type – Functionality
  3. Description – Two players will be connected to each other to play.
  4. Rationale – Players need to be connected to play.
  5. Fit Criterion – Players will be in the waiting room until they are connected.
  6. Priority – High
  7. Dependencies – 16
18.
  1. ID – 18
  2. Type – Functionality
  3. Description – There will be a chat room where players can communicate in real time.
  4. Rationale – Players should be able to communicate with each other.
  5. Fit Criterion – A message will appear in the chat room section that let's players know they can now communicate with each other.
  6. Priority – Low
  7. Dependencies – 17
19.
  1. ID – 19
  2. Type – Support
  3. Description – A '?' button will appear at the bottom of the screen to remind players of the rules of checkers.
  4. Rationale – Most games have a help section like this in case players do not know how to play.
  5. Fit Criterion – When the button is clicked on, the rules will come up.
  6. Priority – Low
  7. Dependencies – n/a
20.
  1. ID – 20
  2. Type – Functionality
  3. Description – Players will capture the opponent's pieces by hopping over it.
  4. Rationale – The most important part of checkers is capturing pieces.
  5. Fit Criterion – A "piece captured" message will appear on the screen when a player captures a piece.
  6. Priority – High
  7. Dependencies – 14
21.
  1. ID – 21
  2. Type – Usability
  3. Description – If a player clicks on one of their pieces and that piece can capture an opponent piece, the space where they should jump will be highlighted.
  4. Rationale – This will make it a lot easier for players to see where they should jump.
  5. Fit Criterion – The spaces will be highlighted yellow.
  6. Priority – Medium
  7. Dependencies – 4
22.
  1. ID – 22
  2. Type – Functionality
  3. Description – The game will end once a player has captured all the opponent's pieces.
  4. Rationale – The game needs to end.
  5. Fit Criterion – A message saying the game is over will come up on the screen.
  6. Priority – High
  7. Dependencies – 3