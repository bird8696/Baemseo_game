import pygame
import random
import sys
import math

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vampire Survivors Lite")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# 전역 그룹
enemy_bullets = pygame.sprite.Group()

# 점수, 업그레이드 상태
score = 0
upgrade_bullet_size = False
upgrade_bullet_spread = False

font = pygame.font.Font(None, 36)

# 버튼 클래스
class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, self.hover_color if self.rect.collidepoint(mouse_pos) else self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)

# UI 함수들
def main_menu():
    font = pygame.font.Font(None, 50)
    start_btn = Button(WIDTH//2-100, HEIGHT//2-50, 200, 50, "Start Game", font, RED, (200, 0, 0))
    while True:
        screen.fill(BLACK)
        start_btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if start_btn.is_clicked(event): return "start"
        pygame.display.flip()
        clock.tick(FPS)

def game_over_menu():
    font = pygame.font.Font(None, 50)
    retry_btn = Button(WIDTH//2-100, HEIGHT//2-100, 200, 50, "Retry", font, RED, (200, 0, 0))
    main_btn = Button(WIDTH//2-100, HEIGHT//2, 200, 50, "Main Menu", font, RED, (200, 0, 0))
    while True:
        screen.fill(BLACK)
        retry_btn.draw(screen)
        main_btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if retry_btn.is_clicked(event): return "retry"
            if main_btn.is_clicked(event): return "end game"
        pygame.display.flip()
        clock.tick(FPS)

def character_select_menu():
    font = pygame.font.Font(None, 50)
    btns = []
    imgs = []
    for i in range(3):
        x = WIDTH//2 - 300 + i * 225
        btns.append(Button(x, HEIGHT//2-50, 150, 150, "", font, WHITE, WHITE))
        img = pygame.image.load(f"C:/2025_AI/myPrj02/image/주인공{i+1}.png")
        imgs.append(pygame.transform.scale(img, (150, 150)))
    while True:
        screen.fill(BLACK)
        for i in range(3):
            btns[i].draw(screen)
            screen.blit(imgs[i], btns[i].rect.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, b in enumerate(btns):
                    if b.is_clicked(event):
                        return f"C:/2025_AI/myPrj02/image/주인공{i+1}.png"
        pygame.display.flip()
        clock.tick(FPS)

def upgrade_menu():
    font = pygame.font.Font(None, 50)
    size_btn = Button(WIDTH//2 - 150, HEIGHT//2 - 100, 300, 50, "Increase Bullet Size", font, RED, (200, 0, 0))
    spread_btn = Button(WIDTH//2 - 150, HEIGHT//2, 300, 50, "180-degree Spread", font, RED, (200, 0, 0))
    while True:
        screen.fill(BLACK)
        size_btn.draw(screen)
        spread_btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if size_btn.is_clicked(event): return "size"
            if spread_btn.is_clicked(event): return "spread"
        pygame.display.flip()
        clock.tick(FPS)

# 게임 클래스들
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

        # 캐릭터별 총알 색깔 설정
        if "주인공1" in image_path:
            self.bullet_color = WHITE
        elif "주인공2" in image_path:
            self.bullet_color = (255, 255, 0)  # 노란색
        elif "주인공3" in image_path:
            self.bullet_color = (0, 0, 255)  # 파란색

    def update(self, keys):
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, color, size=10):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)  # 총알 색깔 설정
        self.rect = self.image.get_rect(center=(x, y))
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        self.speed_x = (dx / dist) * 7
        self.speed_y = (dy / dist) * 7

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        self.speed_x = (dx / dist) * 3
        self.speed_y = (dy / dist) * 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, speed_mult=1.0):
        super().__init__()
        if enemy_type == "monster1":
            self.image = pygame.transform.scale(pygame.image.load("C:/2025_AI/myPrj02/image/몬스터1.png"), (45, 45))
            self.speed = random.uniform(0.5, 1.5) * speed_mult
        elif enemy_type == "monster2":
            self.image = pygame.transform.scale(pygame.image.load("C:/2025_AI/myPrj02/image/몬스터2.png"), (45, 45))
            self.speed = random.uniform(1.5, 2.5) * speed_mult
        else:
            self.image = pygame.transform.scale(pygame.image.load("C:/2025_AI/myPrj02/image/몬스터3.png"), (75, 75))
            self.speed = random.uniform(0.3, 0.7) * speed_mult
            self.shoot_timer = 0

        side = random.choice(["top", "bottom", "left", "right"])
        positions = {
            "top": (random.randint(0, WIDTH), 0),
            "bottom": (random.randint(0, WIDTH), HEIGHT),
            "left": (0, random.randint(0, HEIGHT)),
            "right": (WIDTH, random.randint(0, HEIGHT))
        }
        self.rect = self.image.get_rect(center=positions[side])

    def update(self, player):
        if player.rect.x > self.rect.x: self.rect.x += self.speed
        if player.rect.x < self.rect.x: self.rect.x -= self.speed
        if player.rect.y > self.rect.y: self.rect.y += self.speed
        if player.rect.y < self.rect.y: self.rect.y -= self.speed
        if hasattr(self, "shoot_timer"):
            self.shoot_timer += clock.get_time()
            if self.shoot_timer > 2000:
                enemy_bullets.add(EnemyBullet(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery))
                self.shoot_timer = 0

# 게임 루프
def main():
    global score, upgrade_bullet_size, upgrade_bullet_spread

    while True:
        if main_menu() == "start":
            selected = character_select_menu()
            player = Player(selected)
            player_group = pygame.sprite.GroupSingle(player)
            bullets = pygame.sprite.Group()
            enemies = pygame.sprite.Group()
            enemy_bullets.empty()
            upgrade_bullet_size = False
            upgrade_bullet_spread = False
            score = 0
            speed_mult = 1.0
            spawn_timer = 0

            for _ in range(3):
                enemies.add(Enemy(random.choice(["monster1", "monster2", "monster3"])))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mx, my = pygame.mouse.get_pos()
                        if upgrade_bullet_spread:
                            for angle in [-30, 0, 30]:
                                rad = math.radians(angle)
                                dx, dy = math.cos(rad)*50, math.sin(rad)*50
                                bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx+dx, my+dy, player.bullet_color, 20 if upgrade_bullet_size else 10))
                        else:
                            bullets.add(Bullet(player.rect.centerx, player.rect.centery, mx, my, player.bullet_color, 20 if upgrade_bullet_size else 10))

                keys = pygame.key.get_pressed()
                player_group.update(keys)
                bullets.update()
                enemy_bullets.update()
                for enemy in enemies: enemy.update(player)

                spawn_timer += clock.get_time()
                if spawn_timer > 1000:
                    enemies.add(Enemy(random.choice(["monster1", "monster2", "monster3"]), speed_mult))
                    spawn_timer = 0

                if pygame.time.get_ticks() % 5000 < clock.get_time():
                    speed_mult += 0.05

                for bullet in bullets:
                    hit = pygame.sprite.spritecollide(bullet, enemies, True)
                    if hit:
                        bullet.kill()
                        score += len(hit)

                if pygame.sprite.spritecollide(player, enemies, False) or pygame.sprite.spritecollide(player, enemy_bullets, True):
                    result = game_over_menu()
                    if result == "retry": break
                    return

                screen.fill(BLACK)
                player_group.draw(screen)
                bullets.draw(screen)
                enemies.draw(screen)
                enemy_bullets.draw(screen)
                screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
                pygame.display.flip()
                clock.tick(FPS)

if __name__ == "__main__":
    main()
