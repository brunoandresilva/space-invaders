# space-invaders

This is an implementation of the classic game "Space Invaders" developed using pygame. Right now the player can control the ship (blue square) in both axels (x and y), using the **w a s d keys**, and can also shoot against the enemies (red circles) that come in thier direction using the letter **M**. 

The player can loose the game in 2 different ways:
- Letting more than 3 enemies get to the end of the screen (I will most likely remove this feature if I implement shooting in the enemies)
- Hitting an enemy

When the player looses, is redirected to a red screen letting him know he lost and showing him his score and how to proceed to play again.


## To-Do
- Decrease the fire rate (if the player just holds **m** can pretty much just go left and right and kill everyone)
- Implement shooting for the enemies
- Change the background (maybe add some stars to make it look more like space)
- Change the ship and enemies to real images and not just shapes (might be harder (?))
- Add different types of enemies that give different amounts of score when killed
