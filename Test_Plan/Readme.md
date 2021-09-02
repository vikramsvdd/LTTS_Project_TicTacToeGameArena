# TEST PLAN:

## Table no:1  High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  H_01|Display of Menu| None | "Menu(1).Tic Tac Toe(2).player (X) player (O)(3)board(4)player 1 or 2(alternate fashion)Enter the choice | PASS | Scenario|
|  H_02|Initiation of the game |The assigned player must first choose the position to place his symbol | The Board gets updated and asks for next person to provide input| PASS | Requirement based |
|  H_03|Show Board | Updates the marks on the board| Displays the progress of the game |SUCCESS|Requirement based |
| H_03_01| Draw| Checking if the game will encounter a draw situation| Displays that the Game has been drawn | SUCCESS | Requirement based |
| H_03_02| Win | Checking if the game will encounter a win situation| Displays that the Game has been won and the player who has achieved the feat | SUCCESS | Requirement based |
| H_03_03| In Progress | Checking if the game is still in progress| Displays that the Game is still continuing | SUCCESS | Requirement based |




## Table no:2  Low level test plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|-----|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  L_01|H_02|The game starts and the players have to interact with console to place their response| player should enter a choice for the placing mark on given position| Game in progress| SUCCESS |Requirement based |
|  L_02|H_03|TO check the progress of the Game|None |Displays that the Game has been won and by the repected player by returning 1 |SUCCESS | Requirement based |
|  L_02|H_03|TO check the progress of the Game|None |Displays that the Game has been drawn by returning 0 |SUCCESS | Requirement based |
|  L_02|H_03|TO check the progress of the Game|None |Displays that the Game is in progress by returning -1 |SUCCESS | Requirement based |
