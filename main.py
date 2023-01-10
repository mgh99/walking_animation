import pygame

pygame.init()
width, height = 500, 140 # Inicializo el tamaño de la pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Character")

# Cargo las imagenes
right_images = [pygame.image.load("./assets/sprites/walking_animation_stopRight.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight1.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight2.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight3.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight4.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight5.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight6.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight7.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight8.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopRight9.png")]

left_images = [pygame.image.load("./assets/sprites/walking_animation_stopLeft.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft1.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft2.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft3.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft4.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft5.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft6.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft7.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft8.png"),
                pygame.image.load("./assets/sprites/walking_animation_stopLeft9.png")]

character_direction = "right"
character_x = 0
character_y = 0
current_image_index = 0
character_speed = 15

count_iteration = 0
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Actualizo la posicion del personaje
    character_x += character_speed
    # Compruebo el tamaño de la pantalla
    if character_x > width:
        character_direction = "left"
        character_speed = -15
    elif character_x < 0:
        character_direction = "right"
        character_speed = 15
    

    #Defino el color del fondo de la pantalla y pongo al personaje en los límites
    screen.fill((255, 255, 255))

    if character_direction == "left":
        screen.blit(left_images[current_image_index], (character_x, character_y))
    else:
        screen.blit(right_images[current_image_index], (character_x, character_y))

      

    # Actualizo la animacion del frame
    count_iteration += 1
    if count_iteration % 1 == 0:
        current_image_index = (current_image_index + 1) % len(right_images)

    # Actualizo la información
    pygame.time.delay(90) # espero unos segundos antes de empezar de nuevo el bucle
    pygame.display.update()

pygame.quit()
