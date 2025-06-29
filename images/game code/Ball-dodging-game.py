import pygame
import random
import sys

# เริ่มต้น pygame
pygame.init()

# ขนาดหน้าต่าง
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("เกมหลบบอล")

# สี
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# ตัวละครผู้เล่น
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# ลูกบอล
ball_size = 30
ball_x = random.randint(0, WIDTH - ball_size)
ball_y = -ball_size
ball_speed = 5

# คะแนน
score = 0
font = pygame.font.SysFont("Arial", 30)

# เกมหลัก
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # เฟรมต่อวินาที
    win.fill(WHITE)

    # จับ event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # กดปุ่มเคลื่อนที่
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # อัปเดตตำแหน่งลูกบอล
    ball_y += ball_speed

    # ถ้าลูกบอลตกถึงพื้น
    if ball_y > HEIGHT:
        ball_y = -ball_size
        ball_x = random.randint(0, WIDTH - ball_size)
        score += 1
        ball_speed += 0.3  # เพิ่มความเร็วเมื่อเล่นนานขึ้น

    # ตรวจสอบการชน
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

    if player_rect.colliderect(ball_rect):
        text = font.render("Game Over! คะแนน: " + str(score), True, RED)
        win.blit(text, (50, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False
        continue

    # วาดภาพ
    pygame.draw.rect(win, BLUE, player_rect)
    pygame.draw.ellipse(win, RED, ball_rect)

    # แสดงคะแนน
    score_text = font.render("คะแนน: " + str(score), True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    # อัปเดตหน้าจอ
    pygame.display.update()

pygame.quit()
sys.exit()
