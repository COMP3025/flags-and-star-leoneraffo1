import pygame
import math

# Inicializar o pygame
pygame.init()

# Definir a largura e a altura da tela
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir a cor do fundo
background_color = (0, 0, 0)

# Definir a cor da estrela
star_color = (255, 255, 0)

# Definir o raio da estrela
star_radius = 100

# Definir o número de pontas da estrela
star_points = 5

# Definir o ângulo entre as pontas da estrela
star_angle = math.pi / star_points

# Definir o fator de escala entre o raio externo e o interno da estrela
star_scale = 0.4

# Criar uma lista vazia para armazenar os vértices da estrela
star_vertices = []

# Calcular os vértices da estrela usando trigonometria
for i in range(star_points * 2):
    # Alternar entre o raio externo e o interno da estrela
    if i % 2 == 0:
        radius = star_radius
    else:
        radius = star_radius * star_scale
    
    # Calcular a coordenada x do vértice
    x = screen_width / 2 + radius * math.cos(i * star_angle - math.pi / 2)
    
    # Calcular a coordenada y do vértice
    y = screen_height / 2 + radius * math.sin(i * star_angle - math.pi / 2)
    
    # Adicionar o vértice à lista
    star_vertices.append((x, y))

# Criar um loop para lidar com os eventos do pygame
running = True
while running:
    # Verificar se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preencher a tela com a cor do fundo
    screen.fill(background_color)
    
    # Desenhar a estrela usando os vértices calculados
    pygame.draw.polygon(screen, star_color, star_vertices)
    
    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()
