import pygame
import random
 

# Define some colors
BACKGROUND_COLOR = [255, 255, 255]
BALL_COLOR = [0, 0, 0]
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

def race():
    pygame.init()
 
    print('Guess which ball will win!')

    nob = int(input('How many balls you want?\n'))

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Ball Race")
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    ball_size = 25
    ball_rows = [50]* nob
    frozen = False

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit to 30 frames per second
        clock.tick(30)
 
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
 
        # move a ball
        if not frozen:
            ball_to_move = random.randrange(nob)
            ball_rows[ball_to_move] += 1
            if ball_rows[ball_to_move] > SCREEN_HEIGHT - ball_size:
                print('Ball', ball_to_move+1, 'is the winner!')
                print('(Press Escape to end.)')
                frozen = True
        
        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for i in range(nob):
            pygame.draw.circle(screen, BALL_COLOR,
                               [100 * (i+1), ball_rows[i]], ball_size)
 
        # Update the screen
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 

if __name__ == "__main__":
    race()
