import pygame
import sys
import random
import time

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((675, 360))
pygame.display.set_caption("Героиня в Беге: Сквозь Пределы")
icon = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/icon.png")
pygame.display.set_icon(icon)

bg_main = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/bg/bg_main2.jpg").convert()
bg1 = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/bg/bg06.jpg").convert()
bg2 = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/bg/bg05.jpg").convert()
bg_load = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/bg/bg_main3.jpg")
bg_end = pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/bg/bg_main4.jpg").convert()
font_path = "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/VT323-Regular.ttf"
font = pygame.font.Font(font_path, 32)

walk_left = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/left (1).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/left (2).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/left (3).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/left (4).png").convert_alpha(),
]
walk_right = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/right (1).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/right (2).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/right (3).png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/player/right (4).png").convert_alpha(),
]
attack25 = pygame.image.load(
    "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/items/attack25.png").convert_alpha()
health25 = pygame.image.load(
    "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/items/health25.png").convert_alpha()
health100 = pygame.image.load(
    "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/items/health100.png").convert_alpha()
book = pygame.image.load(
    "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/items/book.png").convert_alpha()
ring = pygame.image.load(
    "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/items/ring.png").convert_alpha()
book_count = 0
ring_count = 0
attack_f = 0.003
health25_f = 0.003
health100_f = 0.001
book_f = 0.0005
ring_f = 0.0003

attack = [
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/1e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/2e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/3e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/4e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/5e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/6e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/7e.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/8e.png").convert_alpha(),
]
attacks = []
at_anim = 0
attack_left = 5
attack_bar = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/a1.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/a2.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/a3.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/a4.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/a5.gif").convert_alpha(),
]  # violet
health_bar = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/h1.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/h2.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/h3.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/h4.gif").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/progress bar/h5.gif").convert_alpha(),
]  # red
h_c = 5

gob_walk_left = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/left/left1.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/left/left2.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/left/left3.png").convert_alpha(),
]
gob_walk_right = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/right/right1.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/right/right2.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/magician/right/right3.png").convert_alpha(),
]
gob_list = []
gob_anim_count = 0
gob_speed = 50

gob_walk_left2 = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/left/01.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/left/02.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/left/03.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/left/04.png").convert_alpha(),
]
gob_walk_right2 = [
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/right/01.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/right/02.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/right/03.png").convert_alpha(),
    pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/enemies/goblin/right/04.png").convert_alpha(),
]
gob_list2 = []
gob_anim_count2 = 0
gob_speed2 = 50

vanish = [
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/v1.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/v2.png").convert_alpha(),
    pygame.image.load("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/effect/v3.png").convert_alpha(),
]
v_anim = 0

player_anim_count = 0
bg_x = 0
jump_music = None

down_font = pygame.font.Font(None, 20)
down_text1 = down_font.render("@2024 Endterm Project ITP.", True, (210, 145, 255))
down_rect1 = down_text1.get_rect(center=(675 // 2, 328))
down_text2 = down_font.render("Directed by Zhalgassova Aida(SE - 2334)", True, (210, 145, 255))
down_rect2 = down_text2.get_rect(center=(675 // 2, 340))

shadow_offset = 4
shadow_color = (66, 0, 109)
myfont = pygame.font.Font("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/VT323-Regular.ttf", 70)
text_surface_shadow1 = myfont.render("Mystic Sprint:", True, shadow_color)
text_surface_shadow2 = myfont.render("Across Dimensions", True, shadow_color)
text_rect_shadow1 = text_surface_shadow1.get_rect(center=(675 // 2 + shadow_offset, 130 + shadow_offset))
text_rect_shadow2 = text_surface_shadow2.get_rect(center=(675 // 2 + shadow_offset, 177 + shadow_offset))
text_surface1 = myfont.render("Mystic Sprint:", True, (243, 225, 255))
text_surface2 = myfont.render("Across Dimensions", True, (243, 225, 255))
text_rect1 = text_surface1.get_rect(center=(675 // 2, 130))
text_rect2 = text_surface2.get_rect(center=(675 // 2, 177))

button_font = pygame.font.Font(None, 36)
button_text_shadow = button_font.render("PRESS START !", True, shadow_color)
button_text_shadow_rect = button_text_shadow.get_rect(center=(330 + shadow_offset, 271 + shadow_offset))
start_button = pygame.Rect(210, 250, 230, 50)
button_text = button_font.render("PRESS START !", False, (210, 145, 255))

end_font = pygame.font.Font("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/VT323-Regular.ttf", 70)
end_surface_shadow = end_font.render("You lose!", True, shadow_color)
end_rect_shadow = end_surface_shadow.get_rect(center=(675 // 2 + shadow_offset, 160 + shadow_offset))
end_surface = end_font.render("You lose!", True, (243, 225, 255))
end_rect = end_surface.get_rect(center=(675 // 2, 160))

end_button = pygame.Rect(210, 250, 230, 50)
end_button_text_shadow = button_font.render("TRY AGAIN", True, shadow_color)
end_button_text_shadow_rect = end_button_text_shadow.get_rect(center=(330 + shadow_offset, 271 + shadow_offset))
end_button_text = button_font.render("TRY AGAIN", False, (210, 145, 255))

show_main_screen = True
bg_music = None
bg_music2 = None
bgm_main = None
player_x = 50
player_y = 235
player_x2 = 50
player_y2 = 235
player_speed = 8
is_jump = False
jump_count = 7

gob_timer = pygame.USEREVENT + 1
pygame.time.set_timer(gob_timer, 6000)

gob_timer2 = pygame.USEREVENT + 1
pygame.time.set_timer(gob_timer2, 5000)


def display_text(screen, font, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(675 // 2, 360 // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    fade_out(screen, text_surface, text_rect)


def fade_out(screen, text_surface, text_rect):
    for alpha in range(255, 0, -10):
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(20)


class Item:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.x = random.randint(0, 660)
            self.rect.y = 235

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Decorations:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.x = random.randint(0, 660)
            self.rect.y = 235

    def draw(self, screen):
        screen.blit(self.image, self.rect)


items = []
item_speed = 10
dec_speed = 10

teleport_images = [
    pygame.transform.scale(pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/teleport/01.png").convert_alpha(), (40, 80)),
    pygame.transform.scale(pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/teleport/02.png").convert_alpha(), (40, 80)),
    pygame.transform.scale(pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/teleport/03.png").convert_alpha(), (40, 80)),
    pygame.transform.scale(pygame.image.load(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/teleport/04.png").convert_alpha(), (40, 80)),
]
t_anim = 0


class Teleport:
    def __init__(self, images, x, y, speed):
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
teleport = Teleport(teleport_images, 1000, 230, 1)
t_timer = pygame.USEREVENT + 1
pygame.time.set_timer(t_timer, 3000)


def draw_loading_screen(progress):
    screen.blit(bg_load, (0, 0))
    pygame.draw.rect(screen, (0, 100, 0), (100, 250, 500, 30))
    pygame.draw.rect(screen, (144, 238, 144), (100, 250, progress * 5, 30))
    load_font = pygame.font.Font("C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/VT323-Regular.ttf",
                                 50)
    load_surface_shadow = load_font.render("Loading...", True, (0, 0, 0))
    load_rect_shadow = load_surface_shadow.get_rect(center=(675 // 2 + 2, 160 + 2))
    screen.blit(load_surface_shadow, load_rect_shadow)
    load_surface = load_font.render("Loading...", True, (243, 225, 255))
    load_rect = load_surface.get_rect(center=(675 // 2, 160))
    screen.blit(load_surface, load_rect)

    load_clue_font = pygame.font.Font(
        "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/VT323-Regular.ttf", 30)
    load_clue_surface_shadow = load_clue_font.render("Collect 5 books and learn a new attack/spell!", True,
                                                     (69, 75, 27))
    load_clue_rect_shadow = load_clue_surface_shadow.get_rect(topleft=(90 + 2, 220 + 2))
    screen.blit(load_clue_surface_shadow, load_clue_rect_shadow)
    load_clue_surface = load_clue_font.render("Collect 5 books and learn a new attack/spell!", True, (243, 225, 255))
    load_clue_rect = load_clue_surface.get_rect(topleft=(90, 220))

    screen.blit(load_clue_surface, load_clue_rect)
    pygame.display.update()


max_goblins = 10


def loading_screen():
    progress = 0
    episode2 = False
    while progress < 100:
        draw_loading_screen(progress)
        time.sleep(0.1)
        progress += 1
    draw_loading_screen(100)
    episode2 = True
    return episode2


episode2 = False
gameplay1 = True
gameplay2 = False
running = True
episode1 = False
loading = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type==t_timer:
        #     print("Timer event triggered")
        #     teleport_ready=True
        elif gameplay1 and event.type == gob_timer:
            gob_list.append(gob_walk_left[gob_anim_count].get_rect(topleft=(680, 243)))
        elif gameplay2 and event.type == gob_timer2:
            gob_list2.append(gob_walk_left2[gob_anim_count2].get_rect(topleft=(680, 235)))
        elif gameplay1 and event.type == pygame.KEYUP and event.key == pygame.K_f and attack_left > 0:
            attack_music = pygame.mixer.Sound(
                "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/mixkit-fantasy-game-sweep-notification-255.wav")
            attack_music.play()
            attacks.append(attack[at_anim].get_rect(topleft=(player_x + 10, player_y)))
            attack_left -= 1
        elif gameplay2 and event.type == pygame.KEYUP and event.key == pygame.K_f and attack_left > 0:
            attack_music = pygame.mixer.Sound(
                "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/mixkit-fantasy-game-sweep-notification-255.wav")
            attack_music.play()
            attacks.append(attack[at_anim].get_rect(topleft=(player_x2 + 10, player_y2)))
            attack_left -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if start_button.collidepoint(event.pos):
                    show_main_screen = False
                    episode1 = True
                    gameplay1=True

    if show_main_screen:
        screen.blit(bg_main, (0, 0))
        screen.blit(down_text1, down_rect1)
        screen.blit(down_text2, down_rect2)
        screen.blit(text_surface_shadow1, text_rect_shadow1)
        screen.blit(text_surface_shadow2, text_rect_shadow2)
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)
        screen.blit(button_text_shadow, button_text_shadow_rect)
        screen.blit(button_text, (start_button.x + 35, start_button.y + 10))

    if episode1:
        screen.blit(bg1, (bg_x, 0))
        screen.blit(bg1, (bg_x + 675, 0))
        if bg_music is None:
            bg_music = pygame.mixer.Sound(
                "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/bgm3.mp3")
            bg_music.play(-1)
        if gameplay1:
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            # if teleport_ready:
            #     teleport = Teleport(teleport_images, teleport_x, 230, 1)
            #     teleport.update()
            #     teleport.draw(screen)
            #     if teleport.rect.colliderect(player_rect):
            #         loading = True
            #         print("Teleporting...")
            #         episode1 = False
            #         gameplay1 = False
            #         bg_music.stop()
            #         bg_music = None
            #         gameplay2 = True
            #         player_x = 50
            #         attack_left = 5
            #         h_c = 5
            #         gob_list.clear()
            #         attacks.clear()
            #         items.clear()
            #         episode2 = loading_screen()

            if random.random() < attack_f:
                items.append(Item(attack25, 650, 235, item_speed))
            if random.random() < health25_f:
                items.append(Item(health25, 650, 235, item_speed))
            if random.random() < health100_f:
                items.append(Item(health100, 650, 235, item_speed))
            if random.random() < book_f:
                items.append(Item(book, 650, 235, item_speed))
            if random.random() < ring_f:
                items.append(Item(ring, 650, 235, item_speed))

            for item in items:
                item.move()
                item.draw(screen)

            for item in items:
                if player_rect.colliderect(item.rect):
                    if item.image == attack25:
                        attack_left += 1
                    elif item.image == health25:
                        if h_c < 4:
                            h_c += 1
                    elif item.image == health100:
                        h_c = 5
                    elif item.image == book:
                        book_count += 1
                        book_text = f"You purchased Book {book_count}/5"
                        display_text(screen, font, book_text)
                    elif item.image == ring:
                        ring_count += 1
                        ring_text = f"You purchased Ring {ring_count}/7"
                        display_text(screen, font, ring_text)
                    items.remove(item)
                elif item.rect == (0, 235):
                    items.remove(item)

            if gob_list:
                for (i, el) in enumerate(gob_list):
                    if player_x < el.x + 50:
                        if player_x < el.x:
                            screen.blit(gob_walk_left[gob_anim_count], el)
                            el.x -= 7
                        else:
                            screen.blit(gob_walk_right[gob_anim_count], el)
                            el.x += 2
                    else:
                        screen.blit(gob_walk_left[gob_anim_count], el)
                        el.x -= 7
                    if el.x < -10 or el.x > 675:
                        gob_list.pop(i)
                    if player_rect.colliderect(el):
                        if h_c > 1:
                            h_c -= 1
                        if h_c == 1:
                            gob_list.pop(i)
                            gob_list.clear()
                            attacks.clear()
                            bg_music.stop()
                            bg_music=None
                            gameplay1 = False
                            break
            if h_c == len(health_bar) or h_c == 5:
                screen.blit(health_bar[4], (0, 0))
            if h_c > 0 and h_c < len(health_bar):
                screen.blit(health_bar[h_c - 1], (0, 0))
            if h_c == 0:
                screen.blit(health_bar[0], (0, 0))
            if attack_left == len(attack_bar):
                screen.blit(attack_bar[4], (65, 0))
            if attack_left > 1 and attack_left < len(attack_bar):
                screen.blit(attack_bar[attack_left - 1], (65, 0))
            if attack_left == 1 or attack_left == 0:
                screen.blit(attack_bar[0], (65, 0))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))

            if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 50:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 600:
                player_x += player_speed

            if attacks:
                for (i, el) in enumerate(attacks):
                    screen.blit(attack[at_anim], (el.x, el.y))
                    el.x += 7
                    if el.x > 675:
                        attacks.pop(i)
                    if gob_list:
                        for (index, goblin) in enumerate(gob_list):
                            if el.colliderect(goblin):
                                gob_list.pop(index)
                                attacks.pop(i)
                                screen.blit(vanish[v_anim], (goblin.x, goblin.y - 23))

            if not is_jump:
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    if jump_music is None:
                        jump_music = pygame.mixer.Sound(
                            "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/cartoon-jump-6462.mp3")
                        jump_music.play()
                        jump_music = None
                    is_jump = True
            else:
                if jump_count >= -7:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 7

            if player_anim_count >= len(walk_right) - 1:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if gob_anim_count >= len(gob_walk_right) - 1:
                gob_anim_count = 0
            else:
                gob_anim_count += 1

            if at_anim >= len(attack) - 1:
                at_anim = 0
            else:
                at_anim += 1

            if v_anim >= len(vanish) - 1:
                v_anim = 0
            else:
                v_anim += 1
            bg_x -= 6
            if bg_x <= -675:
                bg_x = 0

            teleport.update()
            teleport.draw(screen)
            if teleport.rect.colliderect(player_rect):
                loading = True
                print("Teleporting...")
                episode1 = False
                gameplay1 = False
                bg_music.stop()
                gameplay2 = True
                player_x = 50
                attack_left = 5
                h_c = 5
                gob_list.clear()
                attacks.clear()
                items.clear()
                episode2 = loading_screen()

        else:
            screen.blit(bg_end, (0, 0))
            screen.blit(end_surface_shadow, end_rect_shadow)
            screen.blit(end_surface, end_rect)
            screen.blit(end_button_text_shadow, end_button_text_shadow_rect)
            screen.blit(end_button_text, (end_button.x + 55, end_button.y + 10))
            mouse = pygame.mouse.get_pos()
            if end_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                h_c = 5
                player_x = 50
                attack_left = 5
                teleport_x=680
                gameplay1 = True
                bg_music.play(-1)

    if episode2:
        screen.blit(bg2, (bg_x, 0))
        screen.blit(bg2, (bg_x + 675, 0))
        if bg_music2 is None:
            bg_music2 = pygame.mixer.Sound(
                "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/bgm4.mp3")
            bg_music2.play(-1)
        if gameplay2:
            player_rect = walk_left[0].get_rect(topleft=(player_x2, player_y2))
            if random.random() < attack_f:
                items.append(Item(attack25, 650, 230, item_speed))
            if random.random() < health25_f:
                items.append(Item(health25, 650, 230, item_speed))
            if random.random() < health100_f:
                items.append(Item(health100, 650, 230, item_speed))
            if random.random() < book_f:
                items.append(Item(book, 650, 230, item_speed))
            if random.random() < ring_f:
                items.append(Item(ring, 650, 230, item_speed))

            for item in items:
                item.move()
                item.draw(screen)
                if player_rect.colliderect(item.rect):
                    items.remove(item)
                    if item.image == attack25:
                        attack_left += 1
                    elif item.image == health25:
                        if h_c < 5:
                            h_c += 1
                    elif item.image == health100:
                        h_c = 5
                    elif item.image == book:
                        book_count += 1
                        book_text = f"You purchased Book {book_count}/5"
                        display_text(screen, font, book_text)
                    elif item.image == ring:
                        ring_count += 1
                        ring_text = f"You purchased Ring {ring_count}/7"
                        display_text(screen, font, ring_text)

                elif item.rect.right < 0:
                    items.remove(item)

            if gob_list2:
                for (i, el) in enumerate(gob_list2):
                    if player_x2 < el.x + 100:
                        if player_x2 < el.x:
                            screen.blit(gob_walk_left2[gob_anim_count2], el)
                            el.x -= 7
                        else:
                            screen.blit(gob_walk_right2[gob_anim_count2], el)
                            el.x += 2
                    else:
                        screen.blit(gob_walk_left2[gob_anim_count2], el)
                        el.x -= 7
                    if el.x < -10 or el.x > 675:
                        gob_list2.pop(i)
                    if player_rect.colliderect(el):
                        if h_c > 1:
                            h_c -= 1
                        if h_c == 1:
                            gameplay2 = False
                            gob_list2.pop(i)
                            gob_list2.clear()
                            attacks.clear()
                            items.clear()
                            bg_music2.stop()
                            bg_music2 = None
                            break
            if h_c == len(health_bar):
                screen.blit(health_bar[4], (0, 0))
            if h_c > 0 and h_c < len(health_bar):
                screen.blit(health_bar[h_c - 1], (0, 0))
            if h_c == 0:
                screen.blit(health_bar[0], (0, 0))
            if attack_left == len(attack_bar):
                screen.blit(attack_bar[4], (65, 0))
            if attack_left > 1 and attack_left < len(attack_bar):
                screen.blit(attack_bar[attack_left - 1], (65, 0))
            if attack_left == 1 or attack_left == 0:
                screen.blit(attack_bar[0], (65, 0))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                screen.blit(walk_left[player_anim_count], (player_x2, player_y2))
            else:
                screen.blit(walk_right[player_anim_count], (player_x2, player_y2))
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 50:
                player_x2 -= player_speed
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 600:
                player_x2 += player_speed

            if player_x2 < 0:
                player_x2 = 0
            elif player_x2 > 675:
                player_x2 = 675

            if attacks:
                for (i, el) in enumerate(attacks[:]):
                    screen.blit(attack[at_anim], (el.x, el.y))
                    el.x += 7
                    if el.x > 675:
                        try:
                            attacks.remove(el)
                        except ValueError:
                            pass
                    if gob_list2:
                        for (index, goblin) in enumerate(gob_list2):
                            if el.colliderect(goblin):
                                gob_list2.pop(index)
                                try:
                                    attacks.remove(el)  # Удаляем атаку только при успешном попадании в гоблина
                                except ValueError:
                                    pass
                                screen.blit(vanish[v_anim], (goblin.x, goblin.y - 23))

            if not is_jump:
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    if jump_music is None:
                        jump_music = pygame.mixer.Sound(
                            "C:/Users/Админ/PycharmProjects/pythonProject/ITP/Endterm/images/sounds/cartoon-jump-6462.mp3")
                        jump_music.play()
                        jump_music = None
                    is_jump = True
            else:
                if jump_count >= -7:
                    if jump_count > 0:
                        player_y2 -= (jump_count ** 2) / 2
                    else:
                        player_y2 += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 7

            if player_anim_count >= len(walk_right) - 1:
                player_anim_count = 0
            else:
                player_anim_count += 1

            if gob_anim_count2 >= len(gob_walk_right2) - 1:
                gob_anim_count2 = 0
            else:
                gob_anim_count2 += 1

            if at_anim >= len(attack) - 1:
                at_anim = 0
            else:
                at_anim += 1

            if v_anim >= len(vanish) - 1:
                v_anim = 0
            else:
                v_anim += 1
            bg_x -= 6
            if bg_x <= -675:
                bg_x = 0
        else:
            screen.blit(bg_end, (0, 0))
            screen.blit(end_surface_shadow, end_rect_shadow)
            screen.blit(end_surface, end_rect)
            screen.blit(end_button_text_shadow, end_button_text_shadow_rect)
            screen.blit(end_button_text, (end_button.x + 35, end_button.y + 10))
            mouse = pygame.mouse.get_pos()
            if end_button.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay2 = False
                episode2 = False
                attack_left = 5
                h_c = 5
                gameplay1 = True
                player_x = 50
                player_x2 = 50
                attack_left = 5
                h_c = 5
                teleport_x = 680
                bg_music2.stop()
                bg_music2 = None
                episode1 = True
                gameplay1 = True
                bg_music.play(-1)

    pygame.display.update()
    clock.tick(20)
