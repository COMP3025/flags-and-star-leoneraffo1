import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # cor de fundo branca
# desenha a faixa branca
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 800, 300))
# desenha a faixa vermelha
pygame.draw.rect(screen, (255, 0, 0), (0, 300, 800, 300))
# desenha o quadrado azul
pygame.draw.rect(screen, (0, 0, 255), (0, 0, 300, 300))
# desenha a estrela branca
pygame.draw.polygon(screen,
                    (255, 255, 255), [(150, 100), (175, 175), (250, 175),
                                      (200, 225), (225, 300), (150, 250),
                                      (75, 300), (100, 225), (50, 175),
                                      (125, 175)])
pygame.display.flip()
