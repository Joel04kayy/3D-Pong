from visual import *
import random
import math

# Difficulty Variables to Initialize what Difficulty
# the user chose in Single Player Mode
easyMode = 0
mediumMode = 0
hardMode = 0

# Title Screen Directions
def TitleScreen():
       menuDisplay = display(title='Pong', x=0, y=0, width=950,
                        height=950, center=(5,0,0), background=(1,1,1))

       #autoscale
       menuDisplay.autoscale = False

       # Black Back Wall
       wallBack = box(pos = vector(5,0,-20), size=(20,20,0.2), color = color.yellow)
       
       # Front Invisible Wall
       wallFront = box(pos=vector(5,0,0), size=(20,20,0.2), opacity = 0.01)

       # Top Wall
       wallTop = box(pos=vector(5,10,-10), size= (20,0.2,20), color=color.yellow)
       # Left Wall
       wallLeft = box(pos=vector(-5,0,-10), size=(0.2,20,20), color=color.black)
       # Right Wall
       wallRight = box(pos=vector(15,0,-10), size=(0.2,20,20), color=color.black)
       # Bottom Wall
       wallBottom = box(pos=vector(5,-10,-10),size = (20,0.2,20), color=color.yellow)

       # Ball
       menuBall = sphere(pos=vector(5,0,-8), radius=0.4)
       #Paddles
       StartingPaddleScreen1 = box(pos=vector(-4, 0,-10), size = (0.2,3,3), color=color.yellow)
       StartingPaddleScreen2 = box(pos=vector(14,0,-10), size = (0.2,3,3), color=color.yellow)

       # Title Text
       titleScreenText = text(text = "3D Pong", pos = (5,8, 0), align = "center",
                           depth = 0.10, height = 1.5, width = 1.5,
                           color = color.white)
       # Start Game Single Player
       titleScreenText = text(text = "Press Q for 1 player", pos = (-0.5,-4.5, 0),
                           depth = 0.10, height = 1, width = 1,
                           color = color.white)
       # 2 Player Mode
       titleScreenText = text(text = "Press W for 2 players", pos = (-1,-6, 0),
                           depth = 0.10, height = 1, width = 1,
                           color = color.white)

       # 4 Player Mode
       titleScreenText = text(text = "Press E for 4 players", pos = (-1,-7.5, 0),
                           depth = 0.10, height = 1, width = 1,
                           color = color.white)

       titleScreenText = text(text = "Press R for Practice Mode", pos = (-2.3,-8.9,0),
                              depth = 0.10, height = 1, width = 1,
                              color = color.white)

       while True:
              rate(30)
              if menuDisplay.kb.keys:
                     key = menuDisplay.kb.getkey()
                     if key == "q":
                            menuDisplay.delete()
                            # Single Player Mode
                            difficultySet(easyMode, mediumMode, hardMode)

                     if key == "w":
                            menuDisplay.delete()
                            # 2 Player Mode
                            player2Main()

                     if key == "e":
                            menuDisplay.delete()
                            # 4 Player Mode
                            player4Main()

                     if key == "r":
                            menuDisplay.delete()
                            # Practice Mode
                            practiceMain()
                            
                            
# Difficulty Settings when Single Player is Chosen
def difficultySet(easyMode, mediumMode, hardMode):
       
       # Difficulty Variables
       easyMode = 0
       mediumMode = 0
       hardMode = 0
       
       # Difficulty Screen
       difficultyDisplay = display(title='Difficulties', x=0, y=0,
                                   width = 950, height = 950, center=(5,0,0), background = (1,1,1))
       
       difficultyDisplay.autoscale = False
       
       # Title
       titleScreenText = text(text = "Difficulty Presets", pos = (-0.2,8.5, 0),
                           depth = 0.01, height = 1, width = 1,
                           color = color.black)
       # Easy Mode Text
       titleScreenText = text(text = "Press Q for Easy Mode", pos = (-2,-3.5, 0),
                           depth = 0.01, height = 1, width = 1,
                           color = color.black)

       titleScreenText = text(text = "Press W for Medium Mode", pos = (-3,-5.5, 0),
                           depth = 0.01, height = 1, width = 1,
                           color = color.black)

       titleScreenText = text(text = "Press E for Hard Mode", pos = (-2,-7.5, 0),
                           depth = 0.01, height = 1, width = 1,
                           color = color.black)

       titleScreenText = text(text = "Press R to return to the menu", pos = (-4,-9.5, 0),
                              depth = 0.01, height = 1,
                              width = 1,
                              color = color.black)

       titleScreenText = text(text = "While in the game", pos = (-0.5,1,0), depth = 0.01, height = 1, width = 1, color=color.black)
       titleScreenText = text(text = "Press P to pause and O to unpause", pos = (-4.5,-0.5,0), depth = 0.01, height = 1, width = 1, color=color.black)
       
       while True:
              rate(30)
              if difficultyDisplay.kb.keys:
                     keyDifficulty = difficultyDisplay.kb.getkey()
                     # Easy Mode
                     if keyDifficulty == "q":
                            easyMode = easyMode + 1
                            difficultyDisplay.delete()
                            Pong3DMain(easyMode, mediumMode, hardMode)
                            return easyMode
                     # Medium Mode
                     if keyDifficulty == "w":
                            mediumMode = mediumMode + 1
                            difficultyDisplay.delete()
                            Pong3DMain(easyMode, mediumMode, hardMode)
                            return mediumMode
                     # Hard Mode
                     if keyDifficulty == "e":
                            hardMode = hardMode + 1
                            difficultyDisplay.delete()
                            Pong3DMain(easyMode, mediumMode, hardMode)
                            return hardMode
                     # Return to the Main Menu
                     if keyDifficulty == "r":
                            difficultyDisplay.delete()
                            TitleScreen()

# Practice Mode
def practiceMain():

       playerScore = 0

       # Display
       practiceDisplay = display(title='Practice Mode', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))

       practiceDisplay.autoscale = False

       # Black Back Wall
       wallBack = box(pos = vector(5,0,-20), size=(20,20,0.2), color = color.yellow)
       # Front Invisible Wall
       wallFront = box(pos=vector(5,0,0), size=(20,20,0.2), opacity = 0.1)
       # Top Wall
       wallTop = box(pos=vector(5,10,-10), size= (20,0.2,20), color=color.yellow)
       # Left Wall
       wallLeft = box(pos=vector(-5,0,-10), size=(0.2,20,20), color=color.black)
       # Right Wall
       wallRight = box(pos=vector(15,0,-10), size=(0.2,20,20), color=color.black)
       # Bottom Wall
       wallBottom = box(pos=vector(5,-10,-10),size = (20,0.2,20), color=color.yellow)

       # Player's Paddle
       paddle1LEFT = box(pos=vector(-4, 0,-10), size = (0.2,3,3), color=color.yellow)

       mainBall = sphere(pos=vector(5,0,-8), radius=0.4, color=color.yellow)
       
       t = 0.0
       deltaT = 0.005
       # Ball Speed X
       ballVelocityX = random.randint(10,13)
       ballVelocityX = -ballVelocityX
       # Ball Speed Y
       ballVelocityY = random.randint(5,7)
       # Ball Speed Z
       ballVelocityZ = random.randint(4,6)

       player1 = text(text = "{}".format(playerScore),
                         pos=(5,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)

       while True:
              rate(100)
              t = t + deltaT

              # Balls Velocity
              mainBall.velocity = vector(ballVelocityX, ballVelocityY, ballVelocityZ)

              while True:
                     rate(100)

                     mainBall.pos = mainBall.pos + mainBall.velocity*deltaT

                     # Key Movements
                     if practiceDisplay.kb.keys:
                            key = practiceDisplay.kb.getkey()
                            # Up Movement
                            if key == "w":
                                   paddle1LEFT.pos.y = paddle1LEFT.pos.y + 1.5
                            # Down Movement
                            if key == "s":
                                   paddle1LEFT.pos.y = paddle1LEFT.pos.y - 1.5
                            # Right Movement
                            if key == "a":
                                   paddle1LEFT.pos.z = paddle1LEFT.pos.z + 1.5
                            # Left Movement
                            if key == "d":
                                   paddle1LEFT.pos.z = paddle1LEFT.pos.z - 1.5

                                   
                     # Collision Detecion Left Paddle
                     # Bottom Collision Y
                     if paddle1LEFT.pos.y < -8:
                            paddle1LEFT.pos.y = -8
                     # Top Collision Y
                     if paddle1LEFT.pos.y > 8.25:
                            paddle1LEFT.pos.y = 8.25
                     # Left Wall Collision Z
                     if paddle1LEFT.pos.z > -2:
                            paddle1LEFT.pos.z = -2
                     # Right Wall Collision Z       
                     if paddle1LEFT.pos.z < -17.5:
                            paddle1LEFT.pos.z = -17.5

                     # Wall Detections
                     # If Ball hits Right Wall
                     if mainBall.pos.x > wallRight.pos.x:
                            mainBall.velocity.x = -mainBall.velocity.x
                            playerScore = playerScore + 1
                            player1.text = str(playerScore)
##                            # 3D Square in the middle, creating an X, Y, Z coordinates for randomized position WITHIN the 3D box
##                            # Random X Coordinate
##                            randomPosX = random.randint(0,11)
##                            # Random Y Coordinate
##                            randomPosY = random.uniform(-5, 6)
##                            # Random Z Coordinate
##                            randomPosZ = random.uniform(-10, 10)
                                   
                     # If Ball hits Left Wall
                     if mainBall.pos.x < wallLeft.pos.x:
                            mainBall.velocity.x = -mainBall.velocity.x
                            # 3D Square in the middle, creating an X, Y, Z coordinates for randomized position WITHIN the 3D box
                            # Random X Coordinate
                            randomPosX = random.randint(0,11)
                            # Random Y Coordinate
                            randomPosY = random.uniform(-5, 6)
                            # Random Z Coordinate
                            randomPosZ = random.uniform(-10, 10)
                            mainBall.pos = (randomPosX, randomPosY, randomPosZ)
                            
                            
                     # If Ball hits Top Wall
                     if mainBall.pos.y > wallTop.pos.y:
                            mainBall.velocity.y = -mainBall.velocity.y
                     # If Ball hits Bottom Wall
                     if mainBall.pos.y < wallBottom.pos.y:
                            mainBall.velocity.y = -mainBall.velocity.y
                     # If Ball hits Front Invisible Wall
                     if mainBall.pos.z < wallFront.pos.z:
                            mainBall.velocity.z = -mainBall.velocity.z
                     # If Ball Hits Back Wall
                     if mainBall.pos.z > wallBack.pos.z:
                             mainBall.velocity.z = -mainBall.velocity.z

                     # If Ball hits Left Paddle
                     if (mainBall.pos.x < paddle1LEFT.pos.x) and abs(mainBall.pos.y - paddle1LEFT.pos.y) and abs(mainBall.pos.z - paddle1LEFT.pos.z) < 2.5:
                            mainBall.velocity.x = mainBall.velocity.x *-1
                            mainBall.velocity.y = mainBall.velocity.y -1


# Single Player Mode
def Pong3DMain(easyMode, mediumMode, hardMode):
       
       # Easy Mode Speed
       # Ball Speed X
       ballVelocityX1 = random.randint(8,11)
       # Ball Speed Y
       ballVelocityY1 = random.randint(4,6)
       # Ball Speed Z
       ballVelocityZ1 = random.randint(3,5)

       # Medium Mode Speed
       # Ball Speed X
       ballVelocityX2 = random.randint(10,14)
       # Ball Speed Y
       ballVelocityY2 = random.randint(6,8)
       # Ball Speed Z
       ballVelocityZ2 = random.randint(5,7)

       # Hard Mode Speed
       # Ball Speed X
       ballVelocityX3 = random.randint(12,15)
       # Ball Speed Y
       ballVelocityY3 = random.randint(7,10)
       # Ball Speed Z
       ballVelocityZ3 = random.randint(5,8)

 
       # Game Display
       newDisplay = display(title='Single Player', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))

       newDisplay.autoscale = False

       # Black Back Wall
       wallBack = box(pos = vector(5,0,-20), size=(20,20,0.2), color = color.yellow)
       # Front Invisible Wall
       wallFront = box(pos=vector(5,0,0), size=(20,20,0.2), opacity = 0.1)
       # Top Wall
       wallTop = box(pos=vector(5,10,-10), size= (20,0.2,20), color=color.yellow)
       # Left Wall
       wallLeft = box(pos=vector(-5,0,-10), size=(0.2,20,20), color=color.black)
       # Right Wall
       wallRight = box(pos=vector(15,0,-10), size=(0.2,20,20), color=color.black)
       # Bottom Wall
       wallBottom = box(pos=vector(5,-10,-10),size = (20,0.2,20), color=color.yellow)

       # Paddles
       paddle1LEFT = box(pos=vector(-4, 0,-10), size = (0.2,3,3), color=color.yellow)
       paddle2RIGHT = box(pos=vector(14,0,-10), size = (0.2,3,3), color=color.yellow)

       # Ball
       mainBall = sphere(pos=vector(5,0,-15), radius=0.4, color=color.yellow)

       
       t = 0.0
       deltaT = 0.005

       
       # Player Scores
       player1Score = 0
       player2Score = 0

       # Scoreboard Texts
       player1 = text(text = "{}".format(player1Score),
                         pos=(4,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)

       player2 = text(text = "{}".format(player2Score),
                         pos=(6,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)
       
       colon = text(text = ":".format(player2Score),
                         pos=(5,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)
       
       # Main Game Loop
       while True:
              rate(100)
              t = t + deltaT

              # Initialize Different X, Y, Z coordinates for when the Ball resets
              # Random X Coordinate
              randomPosX1 = random.randint(0,11)
              # Random Y Coordinate
              randomPosY1 = random.uniform(-5, 6)
              # Random Z Coordinate
              randomPosZ1 = random.uniform(-10, 10)
              
              # Ball Velocity For Different Difficulties
              # Easy Mode Difficulty
              if easyMode == 1:
                     mainBall.velocity = vector(ballVelocityX1,
                                                ballVelocityY1,
                                                ballVelocityZ1)

                     while True:
                            rate(100)
                            
                            # Ball Position Updated
                            mainBall.pos = mainBall.pos + mainBall.velocity*deltaT
                            
                            # Player 1 Movements
                            if newDisplay.kb.keys:
                                   key = newDisplay.kb.getkey()
                                   if key == "w":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y + 1
                                   if key == "s":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y - 1
                                   if key == "a":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z + 1
                                   if key == "d":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z - 1

                                   # Pause Functions
                                   # Pause
                                   if key == "p":
                                          # Pause Ball Speed
                                          mainBall.velocity = vector(0,0,0)
                                   # Unpause
                                   if key == "o":
                                          # Reset ball Speed
                                          mainBall.velocity = vector(ballVelocityX1,
                                                                     ballVelocityY1,
                                                                     ballVelocityZ1)


                            # Collision Detecion Left Paddle
                            # Bottom Collision Y
                            if paddle1LEFT.pos.y < -8:
                                   paddle1LEFT.pos.y = -8
                            # Top Collision Y
                            if paddle1LEFT.pos.y > 8.25:
                                   paddle1LEFT.pos.y = 8.25
                            # Left Wall Collision Z
                            if paddle1LEFT.pos.z > -2:
                                   paddle1LEFT.pos.z = -2
                            # Right Wall Collision Z       
                            if paddle1LEFT.pos.z < -17.5:
                                   paddle1LEFT.pos.z = -17.5

                            # Paddle Tracking The Ball (AI)
                            paddle2RIGHT.pos.y = mainBall.pos.y
                            paddle2RIGHT.pos.z = mainBall.pos.z

                            # Collision Detection Right Paddle
                            # Bottom Collision Y
                            if paddle2RIGHT.pos.y < -8:
                                   paddle2RIGHT.pos.y = -8
                            # Top Collision Y
                            if paddle2RIGHT.pos.y > 8.25:
                                   paddle2RIGHT.pos.y = 8.25
                            # Z Axis IF Paddle Colides at the Closest Point to The Camera
                            if paddle2RIGHT.pos.z < -17.5:
                                   paddle2RIGHT.pos.z = -17.5
                            # Z Axis If Paddle Colides at the Furthers Point to the Camera
                            if paddle2RIGHT.pos.z > -2:
                                   paddle2RIGHT.pos.z = -2
                     
                            # If Ball hits Right Wall
                            if mainBall.pos.x > wallRight.pos.x:
                                   # Scoreboard Update
                                   player1Score = player1Score + 1
                                   player1.text = str(player1Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX, randomPosY, randomPosZ)
                                   
                            # If Ball hits Left Wall
                            if mainBall.pos.x < wallLeft.pos.x:
                                   # Scoreboard Update
                                   player2Score = player2Score + 1
                                   player2.text = str(player2Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX1, randomPosY1, randomPosZ1)
                            
                            # If Ball hits Top Wall
                            if mainBall.pos.y > wallTop.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y
                            # If Ball hits Bottom Wall
                            if mainBall.pos.y < wallBottom.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y

                            # If Ball hits Front Invisible Wall
                            if mainBall.pos.z < wallFront.pos.z:
                                   mainBall.velocity.z = -mainBall.velocity.z
                            # If Ball Hits Back Wall
                            if mainBall.pos.z > wallBack.pos.z:
                                    mainBall.velocity.z = -mainBall.velocity.z

                            # If Ball hits Right Paddle
                            if (mainBall.pos.x > paddle2RIGHT.pos.x) and abs(mainBall.pos.y + paddle2RIGHT.pos.y) and abs(mainBall.pos.z - paddle2RIGHT.pos.z)< 2.5:
                                   mainBall.velocity.x = mainBall.velocity.x -1
                                   mainBall.velocity.y = mainBall.velocity.y *-1
                                   
                                   
                            # If Ball hits Left Paddle
                            if (mainBall.pos.x < paddle1LEFT.pos.x) and abs(mainBall.pos.y - paddle1LEFT.pos.y) and abs(mainBall.pos.z - paddle1LEFT.pos.z) < 2.5:
                                   mainBall.velocity.x = mainBall.velocity.x *-1
                                   mainBall.velocity.y = mainBall.velocity.y -1

                            # If Player 1 Wins
                            if player1Score == 10:
                                   newDisplay.delete()
                                   winScreen()

                            if player2Score == 10:
                                   newDisplay.delete()
                                   loseScreen()
                                   
                                   

                     
              # Medium Mode Difficulty
              if mediumMode == 1:
                     # Declare the Medium Difficulty Speed
                     mainBall.velocity = vector(ballVelocityX2,
                                                ballVelocityY2,
                                                ballVelocityZ2)

                     while True:
                            rate(100)
                            mainBall.pos = mainBall.pos + mainBall.velocity*deltaT

                            # Movement Keys
                            if newDisplay.kb.keys:
                                   key = newDisplay.kb.getkey()
                                   # Up
                                   if key == "w":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y + 1
                                   # Down
                                   if key == "s":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y - 1
                                   # Left
                                   if key == "a":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z + 1
                                   # Right
                                   if key == "d":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z - 1

                                   # Pause Functions
                                   # Pause
                                   if key == "p":
                                          # Pause Ball Speed
                                          mainBall.velocity = vector(0,0,0)
                                   # Unpause
                                   if key == "o":
                                          # Reset ball Speed
                                          mainBall.velocity = vector(ballVelocityX1,
                                                                     ballVelocityY1,
                                                                     ballVelocityZ1)

                            # Collision Detecion Left Paddle
                            # Bottom Collision Y
                            if paddle1LEFT.pos.y < -8:
                                   paddle1LEFT.pos.y = -8
                            # Top Collision Y
                            if paddle1LEFT.pos.y > 8.25:
                                   paddle1LEFT.pos.y = 8.25
                            # Left Wall Collision Z
                            if paddle1LEFT.pos.z > -2:
                                   paddle1LEFT.pos.z = -2
                            # Right Wall Collision Z       
                            if paddle1LEFT.pos.z < -17.5:
                                   paddle1LEFT.pos.z = -17.5
                            
                            # Paddle Tracking Ball to make it bounce
                            paddle2RIGHT.pos.y = mainBall.pos.y
                            paddle2RIGHT.pos.z = mainBall.pos.z

                            # Collision Detection Right Paddle
                            # Bottom Collision Y
                            if paddle2RIGHT.pos.y < -8:
                                   paddle2RIGHT.pos.y = -8
                            # Top Collision Y
                            if paddle2RIGHT.pos.y > 8.25:
                                   paddle2RIGHT.pos.y = 8.25
                            # Z Axis IF Paddle Colides at the Closest Point to The Camera
                            if paddle2RIGHT.pos.z < -17.5:
                                   paddle2RIGHT.pos.z = -17.5
                            # Z Axis If Paddle Colides at the Furthers Point to the Camera
                            if paddle2RIGHT.pos.z > -2:
                                   paddle2RIGHT.pos.z = -2
                            
                            # If Ball hits Right Wall
                            if mainBall.pos.x > wallRight.pos.x:
                                   # Scoreboard Update
                                   player1Score = player1Score + 1
                                   player1.text = str(player1Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX1, randomPosY1, randomPosZ1)
                                   #mainBall.pos = (5,0,-8)
                                                   
                            # If Ball hits Left Wall
                            if mainBall.pos.x < wallLeft.pos.x:
                                   # Scoreboard Update
                                   player2Score = player2Score + 1
                                   player2.text = str(player2Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX1, randomPosY1, randomPosZ1)
                                   #mainBall.pos = (5,0,-8)
                                                   
                            # If Ball hits Top Wall
                            if mainBall.pos.y > wallTop.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y
                            # If Ball hits Bottom Wall
                            if mainBall.pos.y < wallBottom.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y

                            # If Ball hits Front Invisible Wall
                            if mainBall.pos.z < wallFront.pos.z:
                                   mainBall.velocity.z = -mainBall.velocity.z
                            # If Ball Hits Back Wall
                            if mainBall.pos.z > wallBack.pos.z:
                                    mainBall.velocity.z = -mainBall.velocity.z

                            # If Ball hits Right Paddle
                            if (mainBall.pos.x > paddle2RIGHT.pos.x) and abs(mainBall.pos.y + paddle2RIGHT.pos.y) and abs(mainBall.pos.z-paddle2RIGHT.pos.z) < 1.5:
                                   mainBall.velocity.x = mainBall.velocity.x -1
                                   mainBall.velocity.y = mainBall.velocity.y *-1
                                   
                            # If Ball hits Left Paddle                       # Y Axis Barrier Removed               # Z Axis Barrier Removed
                            if (mainBall.pos.x < paddle1LEFT.pos.x) and abs(mainBall.pos.y-paddle1LEFT.pos.y) and abs(mainBall.pos.z-paddle1LEFT.pos.z) < 1.5:
                                   mainBall.velocity.x = mainBall.velocity.x *-1
                                   mainBall.velocity.y = mainBall.velocity.y -1

                            # If Player 1 Wins
                            if player1Score == 10:
                                   newDisplay.delete()
                                   winScreen()
                                   
                            # If Player 2 Wins
                            if player2Score == 10:
                                   newDisplay.delete()
                                   loseScreen()



                    
              # Hard Mode Difficulty
              if hardMode == 1:
                     mainBall.velocity = vector(ballVelocityX3,
                                                    ballVelocityY3,
                                                    ballVelocityZ3)
                     while True:
                            rate(100)

                            mainBall.pos = mainBall.pos + mainBall.velocity*deltaT
                            # Movement Keys
                            if newDisplay.kb.keys:
                                   key = newDisplay.kb.getkey()
                                   # Up
                                   if key == "w":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y + 1
                                   # Down
                                   if key == "s":
                                          paddle1LEFT.pos.y = paddle1LEFT.pos.y - 1
                                   # Left 
                                   if key == "a":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z + 1
                                   # Right
                                   if key == "d":
                                          paddle1LEFT.pos.z = paddle1LEFT.pos.z - 1

                                   # Pause Functions
                                   # Pause
                                   if key == "p":
                                          # Pause Ball Speed
                                          mainBall.velocity = vector(0,0,0)
                                   # Unpause
                                   if key == "o":
                                          # Reset ball Speed
                                          mainBall.velocity = vector(ballVelocityX1,
                                                                     ballVelocityY1,
                                                                     ballVelocityZ1)

                            # Collision Detecion Left Paddle
                            # Bottom Collision Y
                            if paddle1LEFT.pos.y < -8:
                                   paddle1LEFT.pos.y = -8
                            # Top Collision Y
                            if paddle1LEFT.pos.y > 8.25:
                                   paddle1LEFT.pos.y = 8.25
                            # Left Wall Collision Z
                            if paddle1LEFT.pos.z > -2:
                                   paddle1LEFT.pos.z = -2
                            # Right Wall Collision Z       
                            if paddle1LEFT.pos.z < -17.5:
                                   paddle1LEFT.pos.z = -17.5
                            
                            # Paddle Tracking to Bounce the Ball (AI)
                            paddle2RIGHT.pos.y = mainBall.pos.y
                            paddle2RIGHT.pos.z = mainBall.pos.z

                            # Collision Detection Right Paddle
                            # Bottom Collision Y
                            if paddle2RIGHT.pos.y < -8:
                                   paddle2RIGHT.pos.y = -8
                            # Top Collision Y
                            if paddle2RIGHT.pos.y > 8.25:
                                   paddle2RIGHT.pos.y = 8.25
                            # Z Axis IF Paddle Colides at the Closest Point to The Camera
                            if paddle2RIGHT.pos.z < -17.5:
                                   paddle2RIGHT.pos.z = -17.5
                            # Z Axis If Paddle Colides at the Furthers Point to the Camera
                            if paddle2RIGHT.pos.z > -2:
                                   paddle2RIGHT.pos.z = -2
                            
                            # If Ball hits Right Wall
                            if mainBall.pos.x > wallRight.pos.x:
                                   # Scoreboard Update
                                   player1Score = player1Score + 1
                                   player1.text = str(player1Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX1, randomPosY1, randomPosZ1)
                                   #mainBall.pos = (5,0,-8)
                                                   
                            # If Ball hits Left Wall
                            if mainBall.pos.x < wallLeft.pos.x:
                                   # Scoreboard Update
                                   player2Score = player2Score + 1
                                   player2.text = str(player2Score)
                                   # Reset Ball Position
                                   mainBall.pos = (randomPosX1, randomPosY1, randomPosZ1)
                                   #mainBall.pos = (5,0,-8)

                                                   
                            # If Ball hits Top Wall
                            if mainBall.pos.y > wallTop.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y
                            # If Ball hits Bottom Wall
                            if mainBall.pos.y < wallBottom.pos.y:
                                   mainBall.velocity.y = -mainBall.velocity.y

                            # If Ball hits Front Invisible Wall
                            if mainBall.pos.z < wallFront.pos.z:
                                   mainBall.velocity.z = -mainBall.velocity.z
                            # If Ball Hits Back Wall
                            if mainBall.pos.z > wallBack.pos.z:
                                    mainBall.velocity.z = -mainBall.velocity.z

                            # If Ball hits Right Paddle
                            if (mainBall.pos.x > paddle2RIGHT.pos.x) and abs(mainBall.pos.y + paddle2RIGHT.pos.y) and abs(mainBall.pos.z - paddle2RIGHT.pos.z) < 2.5:
                                   mainBall.velocity.x = mainBall.velocity.x -1
                                   mainBall.velocity.y = mainBall.velocity.y *-1
                                   
                            # If Ball hits Left Paddle
                            if (mainBall.pos.x < paddle1LEFT.pos.x) and abs(mainBall.pos.y - paddle1LEFT.pos.y) and abs(mainBall.pos.z - paddle1LEFT.pos.z) < 2.5:
                                   mainBall.velocity.x = mainBall.velocity.x *-1
                                   mainBall.velocity.y = mainBall.velocity.y -1

                            # If Player 1 Wins
                            if player1Score == 10:
                                   newDisplay.delete()
                                   winScreen()
                            # If the AI wins
                            if player2Score == 10:
                                   newDisplay.delete()
                                   loseScreen() 
                                   
# 2 Player Mode
def player2Main():
    
        # Game Display
       secondDisplay = display(title='Pong', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))

       secondDisplay.autoscale = False

       # Black Back Wall
       wallBack2 = box(pos = vector(5,0,-20), size=(20,20,0.2), color = color.yellow)
       # Front Invisible Wall
       wallFront2 = box(pos=vector(5,0,0), size=(20,20,0.2), opacity = 0.1)
       # Top Wall
       wallTop2 = box(pos=vector(5,10,-10), size= (20,0.2,20), color=color.yellow)
       # Left Wall
       wallLeft2 = box(pos=vector(-5,0,-10), size=(0.2,20,20), color=color.black)
       # Right Wall
       wallRight2 = box(pos=vector(15,0,-10), size=(0.2,20,20), color=color.black)
       # Bottom Wall
       wallBottom2 = box(pos=vector(5,-10,-10),size = (20,0.2,20), color=color.yellow)

       # Ball
       mainBall2 = sphere(pos=vector(5,0,-8), radius=0.4, color=color.white)

       # Paddles
       paddle1LEFT2 = box(pos=vector(-4, 0,-10), size = (0.2,3,3), color=color.yellow)
       paddle2RIGHT2 = box(pos=vector(14,0,-10), size = (0.2,3,3), color=color.yellow)

       t = 0.0
       deltaT = 0.005

       # Different X, Y, Z Ball Speeds
       # Ball Speed X
       ballVelocityX2 = random.randint(6,11)
       # Ball Speed Y
       ballVelocityY2 = random.randint(4,6)
       # Ball Speed Z
       ballVelocityZ2 = random.randint(4,8)
       # Ball Velocity Full
       mainBall2.velocity = vector(ballVelocityX2, ballVelocityY2, ballVelocityZ2)

       # Player Scores Variables
       player1Score = 0
       player2Score = 0
       
       # Scoreboard
       player1 = text(text = "{}".format(player1Score),
                         pos=(4,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)

       player2 = text(text = "{}".format(player2Score),
                         pos=(6,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)

       colon = text(text = ":".format(player2Score),
                         pos=(5,8,0), align = "center", depth = 0.1, height = 1.5,
                         width=1.5,color=color.black)

       while True:
              rate(100)
              t = t + deltaT
              mainBall2.pos = mainBall2.pos + mainBall2.velocity*deltaT

              # Resseting Ball Positions after Point was Scored / Reset
              # Random X Coordinate       (0 to 10)
              randomPosX2 = random.randint(0,11)
              # Random Y Coordinate       (-5 to 5)
              randomPosY2 = random.uniform(-5, 6)
              # Random Z Coordinate       (-10 to 10)
              randomPosZ2 = random.uniform(-10, -2)
              
              if secondDisplay.kb.keys:
                     key = secondDisplay.kb.getkey()
                     
                     # Player 1 Movements
                     # Up Movement
                     if key == "w":
                            paddle1LEFT2.pos.y = paddle1LEFT2.pos.y + 1
                     # Down Movement
                     if key == "s":
                            paddle1LEFT2.pos.y = paddle1LEFT2.pos.y - 1
                     # Left Movement
                     if key == "a":
                            paddle1LEFT2.pos.z = paddle1LEFT2.pos.z + 1
                     # Right Movement
                     if key == "d":
                            paddle1LEFT2.pos.z = paddle1LEFT2.pos.z - 1

                    # Player 2 Movements
                    # Up Movement
                     if key == "up":
                            paddle2RIGHT2.pos.y = paddle2RIGHT2.pos.y + 1
                    # Down Movement
                     if key == "down":
                             paddle2RIGHT2.pos.y = paddle2RIGHT2.pos.y - 1
                    # Left Movement
                     if key == "left":
                             paddle2RIGHT2.pos.z = paddle2RIGHT2.pos.z - 1
                    # Right Movement
                     if key == "right":
                             paddle2RIGHT2.pos.z = paddle2RIGHT2.pos.z + 1

                     # Pause Functions
                     # Pause
                     if key == "p":
                            # Pause Ball Speed
                            mainBall2.velocity = vector(0,0,0)
                     # Unpause
                     if key == "o":
                            # Reset ball Speed
                            mainBall2.velocity = vector(ballVelocityX2,
                                                       ballVelocityY2,
                                                       ballVelocityZ2)
                             
            # Collision Detecion Left Paddle
              # Bottom Collision Y
              if paddle1LEFT2.pos.y < -8:
                     paddle1LEFT2.pos.y = -8
              # Top Collision Y
              if paddle1LEFT2.pos.y > 8.25:
                     paddle1LEFT2.pos.y = 8.25
              # Left Wall Collision Z
              if paddle1LEFT2.pos.z > -2:
                     paddle1LEFT2.pos.z = -2
              # Right Wall Collision Z       
              if paddle1LEFT2.pos.z < -17.5:
                     paddle1LEFT2.pos.z = -17.5
                     
              # Collision Detection Right Paddle
              # Bottom Collision Y
              if paddle2RIGHT2.pos.y < -8:
                  paddle2RIGHT2.pos.y = -8
              # Top Collision Y
              if paddle2RIGHT2.pos.y > 8.25:
                  paddle2RIGHT2.pos.y = 8.25
              # Z Axis IF Paddle Colides at the Closest Point to The Camera
              if paddle2RIGHT2.pos.z < -17.5:
                  paddle2RIGHT2.pos.z = -17.5
              # Z Axis If Paddle Colides at the Furthers Point to the Camera
              if paddle2RIGHT2.pos.z > -2:
                  paddle2RIGHT2.pos.z = -2

              # If Ball hits Right Wall
              if mainBall2.pos.x > wallRight2.pos.x:
                     # Scoreboard Update
                     player1Score = player1Score + 1
                     player1.text = str(player1Score)
                     # Reset Ball Position
                     mainBall2.pos = (randomPosX2,randomPosY2,randomPosZ2)

                # If Ball hits Left Wall
              if mainBall2.pos.x < wallLeft2.pos.x:
                  # Scoreboard Update
                     player1Score = player1Score + 1
                     player1.text = str(player1Score)
                     # Reset Ball Position
                     mainBall2.pos = (randomPosX2,randomPosY2,randomPosZ2)

              # If Ball hits Top Wall
              if mainBall2.pos.y > wallTop2.pos.y:
                     mainBall2.velocity.y = -mainBall2.velocity.y
              # If Ball hits Bottom Wall
              if mainBall2.pos.y < wallBottom2.pos.y:
                     mainBall2.velocity.y = -mainBall2.velocity.y

              # If Ball hits Front Invisible Wall
              if mainBall2.pos.z < wallFront2.pos.z:
                     mainBall2.velocity.z = -mainBall2.velocity.z
              if mainBall2.pos.z > wallBack2.pos.z:
                      mainBall2.velocity.z = -mainBall2.velocity.z

              #If Ball hits Right Paddle
              if (mainBall2.pos.x > paddle2RIGHT2.pos.x) and abs(paddle2RIGHT2.pos.y - mainBall2.pos.y) and abs(paddle2RIGHT2.pos.z - mainBall2.pos.z) < 2.5: #and abs(mainBall2.pos.z - paddle2RIGHT2.pos.z) < 2.5: 
                     mainBall2.velocity.x = mainBall2.velocity.x -1
                     mainBall2.velocity.y = mainBall2.velocity.y *-1

                     
              # If Ball hits Left Paddle
              if (mainBall2.pos.x < paddle1LEFT2.pos.x) and abs(mainBall2.pos.y - paddle1LEFT2.pos.y) and abs(mainBall2.pos.z - paddle1LEFT2.pos.z) < 2.5: # and abs(mainBall2.pos.z - paddle1LEFT2.pos.z) < 1.5:
                     mainBall2.velocity.x = mainBall2.velocity.x *-1
                     mainBall2.velocity.y = mainBall2.velocity.y -1

                     
                     
# 4 Player
def player4Main():
        # Game Display
       thirdDisplay = display(title='Pong', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))

       thirdDisplay.autoscale = False

       # Black Back Wall
       wallBack2 = box(pos = vector(5,0,-20), size=(20,20,0.2), color = color.yellow)
       # Front Invisible Wall
       wallFront2 = box(pos=vector(5,0,0), size=(20,20,0.2), opacity = 0.1)
       # Top Wall
       wallTop2 = box(pos=vector(5,10,-10), size= (20,0.2,20), color=color.yellow)
       # Left Wall
       wallLeft2 = box(pos=vector(-5,0,-10), size=(0.2,20,20), color=color.black)
       # Right Wall
       wallRight2 = box(pos=vector(15,0,-10), size=(0.2,20,20), color=color.black)
       # Bottom Wall
       wallBottom2 = box(pos=vector(5,-10,-10),size = (20,0.2,20), color=color.yellow)

       # Ball
       mainBall2 = sphere(pos=vector(5,0,-8), radius=0.4, color=color.white)

       # Paddles
       paddle1LEFT2 = box(pos=vector(-4, 0,-10), size = (0.2,3,3), color=color.yellow)
       paddle2RIGHT2 = box(pos=vector(14,0,-10), size = (0.2,3,3), color=color.yellow)
       paddle3TOP2 = box(pos=vector(5,9,-10), size = (3,0.2,3), color=color.black)
       paddle4BOTTOM2 = box(pos=vector(5,-9,-10), size = (3,0.2,3), color=color.black)

       t = 0.0
       deltaT = 0.005

       # Ball Speed X
       ballVelocityX3 = random.randint(6,8)
       # Ball Speed Y
       ballVelocityY3 = random.randint(4,5)
       # Ball Speed Z
       ballVelocityZ3 = random.randint(4,7)
       # Ball Velocity Full
       mainBall2.velocity = vector(ballVelocityX3, ballVelocityY3, ballVelocityZ3)

       #Score Variables
       player1Score2 = 0
       player2Score2 = 0
       player3Score2 = 0
       player4Score2 = 0
       
##       # Scoreboard
##       player1 = text(text = "{}".format(player1Score2),
##                         pos=(4,8,0), align = "center", depth = 0.1, height = 1.5,
##                         width=1.5,color=color.black)
##
##       player2 = text(text = "{}".format(player2Score2),
##                         pos=(6,8,0), align = "center", depth = 0.1, height = 1.5,
##                         width=1.5,color=color.black)
##
##       player3 = text(text = "{}".format(player3Score2),
##                         pos=(5,6.5,0), align = "center", depth = 0.1, height = 1.5,
##                         width=1.5,color=color.black)
##
##       player4 = text(text = "{}".format(player4Score2),
##                         pos=(5,5,0), align = "center", depth = 0.1, height = 1.5,
##                         width=1.5,color=color.black)

       while True:
              rate(100)
              t = t + deltaT
              mainBall2.pos = mainBall2.pos + mainBall2.velocity*deltaT


              # Random X Coordinate       (0 to 10)
              randomPosX3 = random.randint(0,9)
              # Random Y Coordinate       (-5 to 5)
              randomPosY3 = random.uniform(-5, 6)
              # Random Z Coordinate       (-10 to 10)
              randomPosZ3 = random.uniform(-10, -2)
              
              if thirdDisplay.kb.keys:
                     key = thirdDisplay.kb.getkey()
                     
                     # Player 1 Movements (Right Paddle)
                     # Up Movement
                     if key == "w":
                            paddle1LEFT2.pos.y = paddle1LEFT2.pos.y + 1
                     # Down Movement
                     if key == "s":
                            paddle1LEFT2.pos.y = paddle1LEFT2.pos.y - 1
                     # Left Movement
                     if key == "a":
                            paddle1LEFT2.pos.z = paddle1LEFT2.pos.z + 1
                     # Right Movement
                     if key == "d":
                            paddle1LEFT2.pos.z = paddle1LEFT2.pos.z - 1

                    # Player 2 Movements (Left Paddle)
                    # Up Movement
                     if key == "t":
                            paddle2RIGHT2.pos.y = paddle2RIGHT2.pos.y + 1
                    # Down Movement
                     if key == "g":
                             paddle2RIGHT2.pos.y = paddle2RIGHT2.pos.y - 1
                    # Left Movement
                     if key == "f":
                             paddle2RIGHT2.pos.z = paddle2RIGHT2.pos.z - 1
                    # Right Movement
                     if key == "h":
                             paddle2RIGHT2.pos.z = paddle2RIGHT2.pos.z + 1

                    # Player 3 Movements (Top Paddle)
                    # Up Movement
                     if key == "i":
                           paddle3TOP2.pos.z = paddle3TOP2.pos.z - 1
                     # Down Movement
                     if key == "k":
                            paddle3TOP2.pos.z = paddle3TOP2.pos.z + 1
                     # Left Movement
                     if key == "j":
                            paddle3TOP2.pos.x = paddle3TOP2.pos.x - 1
                            print(paddle3TOP2.pos.x)
                     # Right Movement
                     if key == "l":
                            paddle3TOP2.pos.x = paddle3TOP2.pos.x + 1

                     # Player 4 Movements
                     # Left Movement Movement
                     if key == "left":
                            paddle4BOTTOM2.pos.x = paddle4BOTTOM2.pos.x - 1
                     # Right Movement
                     if key == "right":
                            paddle4BOTTOM2.pos.x = paddle4BOTTOM2.pos.x + 1
                     # Forward Movement
                     if key == "up":
                            paddle4BOTTOM2.pos.z = paddle4BOTTOM2.pos.z - 1
                     # Backward Movement
                     if key == "down":
                            paddle4BOTTOM2.pos.z = paddle4BOTTOM2.pos.z + 1

                     # Pausing Function
                     # Pause
                     if key == "p":
                            # Pause Ball Speed
                            mainBall2.velocity = vector(0,0,0)
                     # Unpause
                     if key == "o":
                            # Reset ball Speed
                            mainBall2.velocity = vector(ballVelocityX3,
                                                        ballVelocityY3,
                                                        ballVelocityZ3)

                                        
            # Collision Detecion Left Paddle
              # Bottom Collision Y
              if paddle1LEFT2.pos.y < -8:
                     paddle1LEFT2.pos.y = -8
              # Top Collision Y
              if paddle1LEFT2.pos.y > 8.25:
                     paddle1LEFT2.pos.y = 8.25
              # Left Wall Collision Z
              if paddle1LEFT2.pos.z > -2:
                     paddle1LEFT2.pos.z = -2
              # Right Wall Collision Z       
              if paddle1LEFT2.pos.z < -17.5:
                     paddle1LEFT2.pos.z = -17.5
                     
              # Collision Detection Right Paddle
              # Bottom Collision Y
              if paddle2RIGHT2.pos.y < -8:
                  paddle2RIGHT2.pos.y = -8
              # Top Collision Y
              if paddle2RIGHT2.pos.y > 8.25:
                  paddle2RIGHT2.pos.y = 8.25
              # Z Axis IF Paddle Colides at the Closest Point to The Camera
              if paddle2RIGHT2.pos.z < -17.5:
                  paddle2RIGHT2.pos.z = -17.5
              # Z Axis If Paddle Colides at the Furthers Point to the Camera
              if paddle2RIGHT2.pos.z > -2:
                  paddle2RIGHT2.pos.z = -2

              # Collision Detection Top Paddle
              # Left Collision X
              if paddle3TOP2.pos.x < -3:
                     paddle3TOP2.pos.x = -3
              # Right Collision X
              if paddle3TOP2.pos.x > 12:
                     paddle3TOP2.pos.x = 12
              # Z Axis IF Paddle Colides at the Closest Point to The Camera
              if paddle3TOP2.pos.z < -17.5:
                     paddle3TOP2.pos.z = -17.5
              # Z Axis If Paddle Colides at the Furthers Point to the Camera
              if paddle3TOP2.pos.z > -2:
                     paddle3TOP2.pos.z = -2

              # Collision Detection Bottom Paddle
              # Left Collision X
              if paddle4BOTTOM2.pos.x < -3:
                     paddle4BOTTOM2.pos.x = -3
              # Right Collision X
              if paddle4BOTTOM2.pos.x > 12:
                     paddle4BOTTOM2.pos.x = 12
              # Front Collision
              if paddle4BOTTOM2.pos.z > -2:
                     paddle4BOTTOM2.pos.z = -2
              # Back Collision
              if paddle4BOTTOM2.pos.z < -17.5:
                     paddle4BOTTOM2.pos.z = -17.5

              # If Ball hits Right Wall
              if mainBall2.pos.x > wallRight2.pos.x:
                  player1Score2 = player1Score2 + 1
                  mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)

              # If Ball hits Left Wall
              if mainBall2.pos.x < wallLeft2.pos.x:
                     #Figure out the point system
                  #player2Score2= player2Score2 + 1
                  mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)

              # If Ball hits Top Wall
              if mainBall2.pos.y > wallTop2.pos.y:
                     #Figure out the point system
                     #player3Score = player3Score + 1
                     mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)

##              # If Ball hits Bottom Wall
##              if mainBall2.pos.y < wallBottom2.pos.y:
##                     #Figure out the point system
##                     #player4Score = player4Score + 1
##                     mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)
                     
              # If Ball hits Bottom Wall
              if mainBall2.pos.y < wallBottom2.pos.y:
                     mainBall2.velocity.y = -mainBall2.velocity.y
                     mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)

              # If Ball hits Front Invisible Wall
              if mainBall2.pos.z < wallFront2.pos.z:
                     mainBall2.velocity.z = -mainBall2.velocity.z
              if mainBall2.pos.z > wallBack2.pos.z:
                      mainBall2.velocity.z = -mainBall2.velocity.z

              #If Ball hits Right Paddle
              if (mainBall2.pos.x > paddle2RIGHT2.pos.x) and abs(mainBall2.pos.y-paddle2RIGHT2.pos.y) and abs(mainBall2.pos.z - paddle2RIGHT2.pos.z) < 2.5:
                     mainBall2.velocity.x = mainBall2.velocity.x -1
                     mainBall2.velocity.y = mainBall2.velocity.y *-1
##                     # Point system if the ball hits the paddle and hits any other wall, it will give the point to that Paddle player, In this Case player 2 (paddle2)
##                     # If Ball hits Bottom Wall
##                     if mainBall.pos.y < wallBottom2.pos.y:
##                            # Give Point
##                            player1Score2 = player1Score2 + 1
##                            # Update Score
##                            player1.text = str(player1Score2)
##                            # Reset Ball Position
##                            mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)
##                     # If Ball hits Top Wall
##                     if mainBall.pos.y > wallTop2.pos.y:
##                            # Give Point
##                            player1Score2 = player1Score2 + 1
##                            # Update Score
##                            player1.text = str(player1Score2)
##                            # Reset Ball Position
##                            mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)
##                     # If Ball Hits Left Wall
##                     if mainBall2.pos.x > wallRight2.pos.x:
##                            # Give Point
##                            player1Score2 = player1Score2 + 1
##                            # Update Score
##                            player1.text = str(player1Score2)
##                            # Reset Ball Position
##                            mainBall2.pos = (randomPosX3,randomPosY3,randomPosZ3)
                            
                     
              # If Ball hits Left Paddle
              if (mainBall2.pos.x < paddle1LEFT2.pos.x) and abs(mainBall2.pos.y-paddle1LEFT2.pos.y) and abs(mainBall2.pos.z - paddle2RIGHT2.pos.z) < 2.5:
                     mainBall2.velocity.x = mainBall2.velocity.x *-1
                     mainBall2.velocity.y = mainBall2.velocity.y -1

              # If Ball Hits Top Paddle
              if (mainBall2.pos.y > paddle3TOP2.pos.y) and abs(mainBall2.pos.z-paddle3TOP2.pos.z) < 2.5:
                     #mainBall2.velocity.x = mainBall2.velocity.x -1
                     mainBall2.velocity.y = mainBall2.velocity.y -1
                     mainBall2.velocity.z = mainBall2.velocity.z *-1

              # If Ball Hits Bottom Paddle
              if (mainBall2.pos.y < paddle4BOTTOM2.pos.y) and abs(mainBall2.pos.z-paddle4BOTTOM2.pos.z) < 2.5:
                     mainBall2.velocity.y = mainBall2.velocity.y *-1
                     mainBall2.velocity.z = mainBall2.velocity.z -1

# Winning Screen
def winScreen():
       
       # Display
       winDisplay = display(title='End Screen', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))
       while True:
              rate(100)
              # Normal Texts
              winningText = text(text = "Congratulations!",
                                pos=(5,8,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              normalText = text(text = "You have just won against the AI!",
                                pos=(5,6,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              redirectText = text(text = "To return to the menu, press Q",
                                pos=(5,4,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              # Key Detections
              if winDisplay.kb.keys:
                     key = winDisplay.kb.getkey()

                     # Return to Main Menu
                     if key == "q":
                            winDisplay.delete()
                            TitleScreen()


# Losing Screen
def loseScreen():
       
       # Display
       loseDisplay = display(title='End Screen', x=0, y=0,width=950,
                        height=950, center=(5,0,0), background=(1,1,1))
       
       while True:
              rate(100)
              
              # Normal Texts
              losingText = text(text = "Unforunate",
                                pos=(5,8,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              normalText = text(text = "You've Lost! Take another go at it!",
                                pos=(5,6,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              redirectText = text(text = "To return to the menu, press Q",
                                pos=(5,4,0), align = "center", depth = 0.1, height = 1.5,
                                width=1.5,color=color.black)
              # Key Detections
              if loseDisplay.kb.keys:
                     key = loseDisplay.kb.getkey()

                     # Return to Main Menu
                     if key == "q":
                            loseDisplay.delete()
                            # Main Menu
                            TitleScreen()

                     
# Main Loop of Game
TitleScreen()
