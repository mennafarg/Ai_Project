 # Ai_Project
# 2048 AI Game 🎮🤖

                                                                        
# 📜 Description  
This project is an AI-powered 2048 game built with Python and Pygame.<br>  
The AI agent plays automatically using the Expectimax algorithm combined with multiple heuristics to maximize its score and reach the 2048 tile.<br>

---

# 🛠 Used Technologies  
- Python<br>  
- Pygame<br>  
- Artificial Intelligence (Expectimax Search)<br>  
- Heuristic Evaluation Functions<br>  

---

# 🚀 How the User Can Play  
In this version, the AI plays the game automatically without any user control.<br>  
Simply run the project, and the AI will start moving the tiles smartly to merge numbers and create higher values.<br>

### 🎯 Winning Condition:  
- You win the game when any tile reaches **2048**.<br>  
- A "**You Win!**" message will appear on the screen. 🎉<br>

### ❌ Losing Condition:  
- If the grid becomes full and no more moves are possible, the game ends with a "**Game Over!**" message.<br>

### 🧑‍💻 User Interaction:  
- No manual moves needed — just watch the AI play and see how it plans to win!<br>

---

# 🎯 AI Strategy  
- **Algorithm**: Expectimax<br>  
- **Heuristics**:<br>  
  - Number of empty tiles<br>  
  - Maximum tile value<br>  
  - Board smoothness<br>  
  - Board monotonicity<br>  

---

# 🧠 PEAS Description  
- **Performance Measure**: Achieving the highest possible score, reaching 2048 tile.<br>  
- **Environment**: 4x4 grid of numbered tiles.<br>  
- **Actuators**: Move tiles (up, down, left, right).<br>  
- **Sensors**: Read the current state of the board.<br>  

---

# 🕹 ODESA  
- **Objective**: Win the game by reaching 2048.<br>  
- **Data**: Current board configuration.<br>  
- **Environment**: Static and fully observable.<br>  
- **Sensors**: Grid scanning.<br>  
- **Actuators**: Movement commands.<br>  

---

# 🤖 Agent Type  
- **Type**: Autonomous agent, reflex-based but enhanced with Expectimax search.<br>  

---

# 🧩 Problem Formulation  
- **State**: Current arrangement of numbers in the 4x4 grid.<br>  
- **Actions**: Move Up, Down, Left, or Right.<br>  
- **Goal State**: Achieve a tile with the value 2048.<br>  
- **Path Cost**: Maximize the score by making strategic moves.<br>  

---

# 🤖 Notes 
-click [2048 AI Version (canva)](https://www.canva.com/design/DAGmC6fMYg8/TG3HSk7tFXddmS3-oY64tA/view?utm_content=DAGmC6fMYg8&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hb0056a274a) to see pdf file..<br>  

---
# 📸 Project Preview  

  ![you win](https://github.com/user-attachments/assets/7d257993-053b-478b-a5f2-f1bac35f59bb)                     
          
  ![Game Over](https://github.com/user-attachments/assets/8619f375-626a-4fb1-9c18-1bb94afe6f72)
