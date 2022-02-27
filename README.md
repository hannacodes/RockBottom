# RockBottom
Createed by Hanna Koh, Lucy Hu, Esther Loo, and Alyssa Sfravara for WiCHacks 2022 

Rock Bottom is a platformer game that is centered around the story of a pet rock

## Story
This game tells the story of a pet rock who has been accidentally dropped down a drain. Join it on its way back to its home!

## Description
This is a 2D platformer game that we created with Pygame and Pygame_Gui.

--- 

## Want to try it out?
Install these three api's by typing into terminal/command prompt: 
```
$ pip install pygame
```
```
$ pip install pygame_gui
```
```
$ pip install opencv-python
```

For mac users:
```
$ pip3 install pygame
```
```
$ pip3 install pygame_gui
```
```
$ pip3 install opencv-python
```

---

## Inspiration
We knew that we wanted to do a game since when we saw the categories, since it is something that none of us have ever done throughly before. 
We asked our friends for ideas, and we came up with a story of a pet rock that gets dropped into a drain and has to find their way back home 
to its owner. 

The beauty of making games is being able to tell a story in most interactive form. Using our creativity, we wanted to recreate our fond memories 
of the simple times when all we worried about was taking care of our pet rocks.

--- 

## What it does
This two-level platformer game is exactly that. The player plays as our main character, a pet rock, as they travel through different ecosystems. 

--- 

## How we built it
We built this entirely in python, using the python games api: pygame.

--- 

## Challenges we ran into
- Game Physics
  - our limited physics knowledge resulted in problems with:
    - Collision
      - in pygame: can easily tell if it collided but not where exactly 
      - had to figure out vertical & horizontal movement and collision 
      - many edge cases (ex: corners)
    - Camera Scrolling 
      - vertical camera scrolling dealt w/ gravity, acceleration, velocity 

--- 

## Accomplishments that we're proud of
We're proud of being able to complete a whole game in just 24 hours!
- Playable Game
  - loading map levels
  - event handlers 
  - moving, jumping 
  - basic collision detection
  - different types of platforms
- Player animation 
  - rock rolling 
  - rock standing  
- Sprites 
  - art for game assets
- Game states
  - linking menu with game
    - game over, help, credits, main menu, win

--- 

## What we learned
We learned about python, using APIs, and we learned a lot about game design. 
- Using python 
  - syntax 
  - initializing classes and using functions
- pygame 
  - using its built in functions to display and make a game
- Game Design
  - how to make fun levels and assets 

--- 

## What's next for Rock Bottom
Hope to implement these in the future:
- Additional Levels
  - Underwater ocean level 
  - Sewer pipes level 
- Moving Platforms
- Collectibles
  - incentivize player to reach difficult places
  - for completion 
  - function as power-up
- Checkpoints 
  - makes dying less frustrating 
  - can lengthen the levels 
- Lives
  - 3 Lives 
  - lose all three, respawn to checkpoint rather than start


