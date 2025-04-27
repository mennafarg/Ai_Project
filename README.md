                                                                            # Ai_Project
                                                                            # 2048 AI Game 🎮🤖

                                                                        
📜 Description
This project is an AI-powered 2048 game built with Python and Pygame.
The AI agent plays automatically using the Expectimax algorithm combined with multiple heuristics to maximize its score and reach the 2048 tile.
_______________________________________________________________________________________________________________________________________________________________
_______________________________________________________________________________________________________________________________________________________________

🛠 Used Technologies
  Python
  Pygame
  Artificial Intelligence (Expectimax Search)
  Heuristic Evaluation Functions

🚀 How the User Can Play
  In this version, the AI plays the game automatically without any user control.
  Simply run the project, and the AI will start moving the tiles smartly to merge numbers and create higher values.
  
  Winning Condition:
    You win the game when any tile reaches 2048.
    A "You Win!" message will appear on the screen. 🎉
  Losing Condition:
    If the grid becomes full and no more moves are possible, the game ends with a "Game Over!" message. ❌
    User Interaction:
    No manual moves needed — just watch the AI play and see how it plans to win!

🎯 AI Strategy
  Algorithm: Expectimax
  Heuristics:
    Number of empty tiles
    Maximum tile value
    Board smoothness
    Board monotonicity

🧠 PEAS Description
  Performance Measure: Achieving the highest possible score, reaching 2048 tile.  
  Environment: 4x4 grid of numbered tiles.  
  Actuators: Move tiles (up, down, left, right).  
  Sensors: Read the current state of the board.

🕹 ODESA
  Objective: Win the game by reaching 2048.
  Data: Current board configuration.
  Environment: Static and fully observable.
  Sensors: Grid scanning.
  Actuators: Movement commands.

🤖 Agent Type
  Type: Autonomous agent, reflex-based but enhanced with Expectimax search.

🧩 Problem Formulation
  State: Current arrangement of numbers in the 4x4 grid.
  Actions: Move Up, Down, Left, or Right.
  Goal State: Achieve a tile with the value 2048.
  Path Cost: Maximize the score by making strategic moves.

📸 Project Preview
  1-You win
  ![you win](https://github.com/user-attachments/assets/7d257993-053b-478b-a5f2-f1bac35f59bb)

  2-Game Over
  ![Game Over](https://github.com/user-attachments/assets/8619f375-626a-4fb1-9c18-1bb94afe6f72)
