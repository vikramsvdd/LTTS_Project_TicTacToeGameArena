# TicTacToeGameArena
This Project aims in creating a TIC-TAC-TOE game, that is played between two people. Based in the two people's moves, the status of the game will be decided i.e a win or a tie!



![TIC_TAC_TOE](https://github.com/vikramsvdd/TicTacToeGameArena/blob/main/tictactoecool.png)


# Project Description
In this project, object oriented programming concept within python is used when developing this project. This project contains two modules, the main function and class TTT board.

  # 1. main function:
    
       a. This function basically starts the game.
       
       b.It performs the following operations in a sequential manner. 
       b1.Creating a board on the screen
       b2.Giving the users the provision to choose a symblo (X or O)
       b3.Prompting the user to enter a number within 1 to 9
       b4.updating the move on the board
       b5.Swapping turns and,
       b6. Checking for a victory or a tie. For achieving each of these operations, the main function uses the help of a class, which contains specific functions to leverage this operation.
       
   # 2. Class TTTBoard:
        
        This is the class that contains all the specific functions within it, to perform the operations required by the main function, to create the game. It contains a constuctor which is parameterised called init and has a derieved class to assist it with certain operations. The functions are below.
        
 *getBoardStr(self): 
         
         This function is used to return a text representation of the board.
         
 *isValidSpace(self, space) :
 
         This function returns True, if the number entered by the user is a valid number, else it return False.
         
         
 *isWinner(self, player):
 
         Checks the winning status in the game. Return True, if a player had won, else it return False.
         
         
 *isBoardFull(self):
 
         Returns true, if the board is completely filled. Else it returns False.
         
         
 *updateBoard(self, space, player):
 
 
         Creates a space on the board for the player to place a mark in.
         
         
         
         

       
       




# OOPS and Python Based Implementation

## Folder Structure
Folder             | Description
-------------------| -----------------------------------------
`1_Requirements`   | Documents detailing requirements and research
`2_Design`         | Documents specifying design details
`3_Implementation` | All code and documentation
`4_Test_plan`      | Documents with test plans and procedures

## Contributors List and Summary

SF Id. |  Name   |    Features    | Issues Raised |Issues Resolved|No Test Cases|Test Case Pass
-------|---------|----------------|----------------|---------------|-------------|--------------
266453` | Vikram Vasudevan  | F_01, F_02, F_03 |  0   |0  | 6 |  6   

| Feature Id | Feature |
| -----------|---------|
|F_1| Provision to choose a symbol |
|F_2| Option to choose the Position  |
|F_3| Updating the mark on the board |

## Challenges Faced and How Was It Overcome
| No. | Challenge | Solution
|-----|-----------|--------
|1. | Output was not matching the expectation | Modified the logic of the program and code itself 
|2. | Game suddenly gets exited in the middle | Modified a segment of the code and eliminated the usage of a library called pudb | 




## Some Snapshots of Results:
![o/p 1](https://github.com/vikramsvdd/TicTacToeGameArena/blob/main/Images(output)/img1.PNG)

![o/p 2](https://github.com/vikramsvdd/TicTacToeGameArena/blob/main/Images(output)/img2.PNG)
 
![o/p 3](https://github.com/vikramsvdd/TicTacToeGameArena/blob/main/Images(output)/img3.PNG)
 
![o/p 4](https://github.com/vikramsvdd/TicTacToeGameArena/blob/main/Images(output)/img4.PNG)



## Reference
The above code was taken from sampling several sites such as ADVLEARNING.com, medium.com, github,youtube and azaz.com . My contributions to the code have been mentioned above and errors in the original code have been rectified. Let me provide the references below


https://inventwithpython.com/beyond/chapter15.html
https://github.com/jeffthemaximum/python-tic-tac-toe
https://www.youtube.com/watch?v=7Djh-Cbgi0E
https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
