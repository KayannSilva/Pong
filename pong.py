import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)

# Define as dimensões das raquetes e da bola
paddle_width = 10
paddle_height = 100
ball_size = 10

# Define as posições iniciais das raquetes e da bola
paddle1_x = 50
paddle1_y = (screen_height - paddle_height) // 2
paddle2_x = screen_width - 50 - paddle_width
paddle2_y = (screen_height - paddle_height) // 2
ball_x = screen_width // 2
ball_y = screen_height // 2

# Define as velocidades das raquetes e da bola
paddle_speed = 2 
ball_speed_x = 0.3 * random.choice((1, -1)) 
ball_speed_y = 0.3 * random.choice((1, -1)) 

# Define os pontos dos jogadores
player1_score = 0
player2_score = 0

# Define a fonte para o placar e a mensagem de vitória
font = pygame.font.Font(None, 74)
win_font = pygame.font.Font(None, 100)

# Função para desenhar as raquetes, a bola e o placar
def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
    
    # Desenha o placar
    score_text = font.render(f"{player1_score}  {player2_score}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))
    
    pygame.display.flip()

# Função para exibir a mensagem de vitória
def show_winner(winner):
    screen.fill(black)
    win_text = win_font.render(f"{winner} venceu!", True, white)
    screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimenta as raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += paddle_speed

    # Movimenta a bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verifica colisões com as paredes
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Verifica colisões com as raquetes
    if (ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height) or \
       (ball_x >= paddle2_x - ball_size and paddle2_y <= ball_y <= paddle2_y + paddle_height):
        ball_speed_x *= -1

    # Verifica se a bola saiu da tela
    if ball_x <= 0:
        player2_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    elif ball_x >= screen_width:
        player1_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Verifica se algum jogador alcançou 5 pontos
    if player1_score == 5:
        show_winner("Jogador 1")
        running = False
    elif player2_score == 5:
        show_winner("Jogador 2")
        running = False

    draw_objects()

pygame.quit()