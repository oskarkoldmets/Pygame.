import pygame

# Initsialiseerime pygame'i
pygame.init()

# Loome ekraani mõõtudega 300x300 pikslit
screen = pygame.display.set_mode([300, 300])

# Seame aknale pealkirja
pygame.display.set_caption("Lumememm")

# Täidame tausta helesinise värviga
screen.fill([173, 216, 230])

# Joonistame kolm valget ringi lumememme kehaks
pygame.draw.circle(screen, [255, 255, 255], [150, 80], 30, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 150], 40, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 240], 50, 0)

# Joonistame kaks musta silma
pygame.draw.circle(screen, [0, 0, 0], [140, 75], 5, 0)
pygame.draw.circle(screen, [0, 0, 0], [160, 75], 5, 0)

# Määratleme kolmnurga tipud (nina jaoks)
tipp1 = [150, 80 - 20 + 45]
tipp2 = [140, 80 - 40 + 45]
tipp3 = [160, 80 - 40 + 45]

# Joonistame täidetud kolmnurga ninaks
pygame.draw.polygon(screen, [255, 153, 51], [tipp1, tipp2, tipp3], 0)

# Joonistame käed
pygame.draw.line(screen, [139, 69, 19], [120, 130], [90, 100], 5)
pygame.draw.line(screen, [139, 69, 19], [180, 130], [210, 100], 5)

# Joonistame kolm nööpi
pygame.draw.circle(screen, [0, 0, 0], [150, 120], 3, 0)
pygame.draw.circle(screen, [0, 0, 0], [150, 150], 3, 0)
pygame.draw.circle(screen, [0, 0, 0], [150, 180], 3, 0)

# Joonistame mütsi
pygame.draw.rect(screen, [0, 0, 0], [130, 50, 40, 20], 0)
pygame.draw.polygon(screen, [0, 0, 0], [[130, 50], [170, 50], [150, 20]], 0)

# Joonistame harja
pygame.draw.line(screen, [139, 69, 19], [90, 100], [90, 50], 3)
pygame.draw.polygon(screen, [139, 69, 19], [[85, 50], [95, 50], [90, 30]], 0)


# Joonistame päikese
pygame.draw.circle(screen, [255, 255, 0], [250, 50], 30, 0)
pygame.draw.line(screen, [255, 255, 0], [250, 20], [250, 80], 2)
pygame.draw.line(screen, [255, 255, 0], [280, 50], [220, 50], 2)
pygame.draw.line(screen, [255, 255, 0], [270, 30], [230, 70], 2)
pygame.draw.line(screen, [255, 255, 0], [270, 70], [230, 30], 2)

# Joonistame pilved
pygame.draw.circle(screen, [255, 255, 255], [50, 50], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [80, 50], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [110, 50], 20, 0)

pygame.draw.circle(screen, [255, 255, 255], [200, 20], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [230, 20], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [260, 20], 20, 0)

pygame.draw.circle(screen, [255, 255, 255], [280, 80], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [310, 80], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [340, 80], 20, 0)

# Värskendame ekraani
pygame.display.flip()

# Pealoog
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Lõpetame pygame'i kasutamise
pygame.quit()
