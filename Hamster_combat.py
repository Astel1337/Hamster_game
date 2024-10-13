import pygame
import os

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hamster Combat")

# Загрузка и масштабирование фона
background_img = pygame.image.load('harry_potter_background.jpg')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Загрузка изображений для анимации
def load_animation_images(folder_name):
    images = []
    for file_name in os.listdir(folder_name):
        img = pygame.image.load(os.path.join(folder_name, file_name))
        images.append(img)
    return images

# Персонаж с анимацией
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = load_animation_images('hamster_walk')
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.animation_speed = 0.1  # скорость анимации
        self.velocity = pygame.math.Vector2(0, 0)  # вектор скорости персонажа

    def update(self):
        # Смена кадров анимации
        self.current_image += self.animation_speed
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[int(self.current_image)]

        # Движение персонажа
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Границы персонажа
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def move(self, direction):
        if direction == 'left':
            self.velocity.x = -5
        elif direction == 'right':
            self.velocity.x = 5
        elif direction == 'up':
            self.velocity.y = -5
        elif direction == 'down':
            self.velocity.y = 5

    def stop(self):
        self.velocity = pygame.math.Vector2(0, 0)

# Основной цикл игры
def main():
    clock = pygame.time.Clock()
    running = True

    # Создаем персонажа и группу спрайтов
    hamster = Character()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(hamster)

    while running:
        # FPS
        clock.tick(60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление персонажем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            hamster.move('left')
        elif keys[pygame.K_RIGHT]:
            hamster.move('right')
        elif keys[pygame.K_UP]:
            hamster.move('up')
        elif keys[pygame.K_DOWN]:
            hamster.move('down')
        else:
            hamster.stop()

        # Обновление всех спрайтов
        all_sprites.update()

        # Отрисовка
        screen.blit(background_img, (0, 0))  # отрисовка фона
        all_sprites.draw(screen)  # рисуем спрайты
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
