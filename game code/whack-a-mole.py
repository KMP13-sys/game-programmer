import pygame
import random
import sys
import time

# เริ่มต้น pygame
pygame.init()

# ขนาดหน้าจอ
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("เกมตีตัวตุ่น (Whack-a-Mole)")

# สี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("TH SarabunPSK", 30)

# กำหนดตำแหน่งที่ตัวตุ่นสามารถโผล่ได้
positions = [
    (100, 100), (250, 100), (400, 100),
    (100, 220), (250, 220), (400, 220),
]

# ขนาดตัวตุ่น
MOLE_SIZE = 80

# ตัวแปรเกม
score = 0
mole_pos = random.choice(positions)
last_mole_time = time.time()

# ตัวจับเวลาเฟรม
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # จำกัดเฟรมเรท
    win.fill(WHITE)

    # แสดงคะแนน
    score_text = font.render(f"คะแนน: {score}", True, BLACK)
    win.blit(score_text, (10, 10))

    # โหลดภาพตุ่น
    mole_img = pygame.image.load("images/mole.png")
    mole_img = pygame.transform.scale(mole_img, (80, 80))

    # วาดตัวตุ่น (จากภาพแทนวงกลม)
    mole_rect = pygame.Rect(mole_pos[0], mole_pos[1], MOLE_SIZE, MOLE_SIZE)
    win.blit(mole_img, mole_pos)

    # สุ่มเปลี่ยนตำแหน่งทุก 1 วินาที
    if time.time() - last_mole_time > 1:
        mole_pos = random.choice(positions)
        last_mole_time = time.time()

    # ตรวจจับ event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rect.collidepoint(event.pos):
                score += 1
                mole_pos = random.choice(positions)
                last_mole_time = time.time()

    # อัปเดตหน้าจอ
    pygame.display.update()

pygame.quit()
sys.exit()
