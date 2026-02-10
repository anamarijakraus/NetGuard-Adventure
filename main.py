import pygame
import random
import asyncio

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
GRAY = (128, 128, 128)
PURPLE = (147, 112, 219)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
BLUE_BOX = (50, 50, 200)

# Game states
MENU = 0
PLAYING = 1
QUESTION = 2
SHOP = 3
GAME_OVER = 4
LEVEL_COMPLETE = 5
VICTORY = 6
MODE_VICTORY = 7
INSTRUCTIONS = 8
PROFILE = 9
HINT = 10

DIFFICULTY_SETTINGS = {
    'easy': {
        'lives': 3,
        'auto_run': True,
        'scroll_speed_base': 5,
        'level_count': 5
    },
    'normal': {
        'lives': 3,
        'time_limit_base': 120,
        'gravity': 0.9,
        'jump_power': -16,
        'has_bouncy': True,
        'enemy_speed_base': 2,
        'auto_run': False,
        'is_vertical': False,
        'level_count': 5
    },
    'hard': {
        'lives': 3,
        'time_limit_base': 150,
        'gravity': 0.8,
        'jump_power': -16,
        'has_bouncy': True,
        'enemy_speed_base': 3,
        'auto_run': False,
        'is_vertical': True,
        'max_jumps': 2,
        'level_count': 5
    }
}

TRANSLATIONS = {
    'en': {
        'title': 'NetGuard Adventure',
        'easy': 'Easy (8-10 years) - Auto Runner',
        'normal': 'Normal (10-12 years) - Platform',
        'hard': 'Hard (12-14 years) - Vertical Climber',
        'shop': 'Shop',
        'lives': 'Lives',
        'coins': 'Coins',
        'time': 'Time',
        'distance': 'Distance',
        'altitude': 'Height',
        'level': 'Level',
        'best': 'Best',
        'correct': 'Correct! +10 coins',
        'wrong': 'Wrong! -1 life',
        'game_over': 'Game Over!',
        'level_complete': 'Level Complete!',
        'victory': 'VICTORY! All Levels Complete!',
        'total_coins': 'Total Coins',
        'total_time': 'Total Time',
        'press_enter': 'Press ENTER to continue',
        'press_space': 'Press SPACE to restart',
        'press_space_menu': 'Press SPACE for menu',
        'jump': 'Press SPACE or UP to JUMP',
        'shop_hint': 'Press S for Shop',
        'q_title': 'Security Question',
        'shield': 'Shield (50 coins)',
        'back': 'Back (B)',
        'language': 'Language: English (L to change)',
        'life': 'Life',
        'time_item': 'Time',
        'price': '30 coins',
        'success': 'Successfully bought',
        'not_enough': 'Not enough coins',
        'easy_controls': 'SPACE or Arrow Key UP: Jump\n- S : Open shop\n- Answer questions with numbers: 1, 2, 3',
        'easy_objective': 'Auto-runner: You move forward automatically\n- Jump over obstacles\n- Collect coins\n- Answer questions to win coins\n- Reach the door at the end to complete level',
        'normal_controls': 'Arrow Keys LEFT/RIGHT: Move left / right\n- SPACE or Arrow Key UP : Jump\n- S : Open shop\n- Answer questions with numbers: 1, 2, 3',
        'normal_objective': '- Navigate platforms and avoid enemies\n- Navyblue platforms give bounce\n- Collect coins\n- Answer questions to win coins\n- Reach the door at the end to complete level',
        'hard_controls': 'Arrow Keys LEFT/RIGHT: Move left / right\n- SPACE or Arrow Key UP: Jump (double jump enabled)\n- Answer questions with numbers: 1, 2, 3',
        'hard_objective': 'Climb upward\n- Dont fall off of the platforms \n- Use double jump to reach higher platforms\n- Navyblue platforms give bounce\n- Reach the door at the top to complete level',
        'fall_warning': 'Be careful!',
        # Screen titles, buttons
        'instructions_title': 'INSTRUCTIONS',
        'shop_title': 'SHOP',
        'play_button': 'PLAY',
        'next_button': 'NEXT',
        'menu_button': 'MENU',
    },
    'mk': {
        'title': 'НетГард Авантура',
        'easy': 'Лесно (8-10 години) - Авто Трчање',
        'normal': 'Нормално (10-12 години) - Платформа',
        'hard': 'Тешко (12-14 години) - Вертикално искачување',
        'shop': 'Продавница',
        'lives': 'Животи',
        'coins': 'Пари',
        'time': 'Време',
        'distance': 'Растојание',
        'altitude': 'Висина',
        'level': 'Ниво',
        'best': 'Најдобро',
        'correct': 'Точно! +10 пари',
        'wrong': 'Грешно! -1 живот',
        'game_over': 'Крај на игра!',
        'level_complete': 'Ниво завршено!',
        'victory': 'ПОБЕДА! Сите нивоа завршени!',
        'total_coins': 'Вкупно пари',
        'total_time': 'Вкупно време',
        'press_enter': 'Притисни ENTER за продолжување',
        'press_space': 'Притисни SPACE за рестарт',
        'press_space_menu': 'Притисни SPACE за мени',
        'jump': 'Притисни SPACE или UP за СКОК',
        'shop_hint': 'Притисни S за продавница',
        'q_title': 'Прашање за безбедност',
        'shield': 'Штит (50 пари)',
        'back': 'Назад (B)',
        'language': 'Јазик: Македонски (L за промена)',
        'life': 'Живот',
        'time_item': 'Време',
        'price': '30 пари',
        'success': 'Успешно купено',
        'not_enough': 'Немате доволно пари',
        'easy_controls': 'SPACE или Arrow Key UP: Скокање\n- S : Отвори продавница\n- Одговори на прашања со броеви: 1, 2, 3',
        'easy_objective': 'Автоматско трчање напред\n- Скокај преку пречки\n- Собирај парички\n- Одговарај на прашања за парички\n- Дојди до вратата за да го завршиш нивото',
        'normal_controls': 'Arrow Keys LEFT/RIGHT: Движење лево / десно\n- SPACE или Arrow Key UP: Скокање\n- S : Отвори продавница\n- Одговори на прашања со броеви: 1, 2, 3',
        'normal_objective': '- Избегнувај непријатели\n- Виолетовите платформи даваат одскок\n- Собирај парички\n- Одговарај на прашања за парички\n- Дојди до вратата за да го завршиш нивото',
        'hard_controls': 'Arrow Keys LEFT/RIGHT: Движење лево / десно\n- SPACE или Arrow Key UP: Скокање (двоен скок)\n- Одговори на прашања со броеви: 1, 2, 3',
        'hard_objective': 'Искачување нагоре\n- Пад надвор од платформа = можеби и крај на игра\n- Користи двоен скок за повисоки платформи\n- Виолетовите платформи даваат одскок\n- Дојди до вратата на врвот за да го завршиш нивото',
        'fall_warning': 'Внимавај!',
        # Screen titles, buttons
        'instructions_title': 'ИНСТРУКЦИИ',
        'shop_title': 'ПРОДАВНИЦА',
        'play_button': 'ИГРАЈ',
        'next_button': 'СЛЕДНО',
        'menu_button': 'МЕНИ',
    }
}

# ========== SESSION STATS (IN-MEMORY) ==========
stats = {
    "easy": {
        "coins": 0,
        "completions": 0,
    },
    "normal": {
        "coins": 0,
        "completions": 0,
    },
    "hard": {
        "coins": 0,
        "completions": 0,
    },
    "questions": {
        "total": 0,
        "correct": 0,
        "incorrect": 0,
    },
    "total_xp": 0,
}

# ========== FONT AND TEXT HELPERS ==========

HANDJET_FONT_PATH = 'assets/fonts/Handjet-Medium.ttf'


def load_game_fonts():
    try:
        base_font_large = pygame.font.Font(HANDJET_FONT_PATH, 64)
        base_font_medium = pygame.font.Font(HANDJET_FONT_PATH, 48)
        base_font_small = pygame.font.Font(HANDJET_FONT_PATH, 32)
    except Exception:
        # Fallback to default pygame font but still single source of truth
        base_font_large = pygame.font.Font(None, 64)
        base_font_medium = pygame.font.Font(None, 48)
        base_font_small = pygame.font.Font(None, 32)

    return base_font_large, base_font_medium, base_font_small


def draw_text_centered(surface, text, rect, font, color):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)


# ========== IMAGE LOADING ==========
def load_image(filename, size, fallback_color):
    try:
        image = pygame.image.load(filename).convert_alpha()
        return pygame.transform.smoothscale(image, size)
    except:
        surface = pygame.Surface(size)
        # surface.fill(fallback_color)
        return surface


# ========== SOUND MANAGER CLASS ==========
class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.music_playing = None
        self.music_was_playing = False  # Track if music was playing before stopping
        self.instruction_audio_playing = None  # Track currently playing instruction audio
        self.load_sounds()

    def load_sounds(self):
        sound_files = {
            'click': 'assets/sounds/mouse_click.mp3',
            'coin': 'assets/sounds/coin_sound.mp3',
            'victory': 'assets/sounds/victory_sound.mp3',
            'game_over': 'assets/sounds/game_over_sound.mp3',
            'background_music': 'assets/sounds/background_music2.mp3',
            'hit_obstacle': 'assets/sounds/hit_obstacle_sound.mp3',
            'hit_villain': 'assets/sounds/monster_kill_sound.mp3',
            'easy_instructions': 'assets/sounds/easy_mode_instructions.wav',
            'normal_instructions': 'assets/sounds/normal_mode_instructions.wav',
            'hard_instructions': 'assets/sounds/hard_mode_instructions.wav'
        }

        for name, path in sound_files.items():
            try:
                if name == 'background_music':
                    self.sounds[name] = path
                elif name.endswith('_instructions'):
                    self.sounds[name] = pygame.mixer.Sound(path)
                else:
                    self.sounds[name] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Warning: Could not load sound {name} from {path}: {e}")
                self.sounds[name] = None

    def play_click(self):
        if self.sounds.get('click'):
            try:
                self.sounds['click'].play()
            except:
                pass

    def play_coin(self):
        if self.sounds.get('coin'):
            try:
                self.sounds['coin'].play()
            except:
                pass

    def play_hit_villain(self):
        if self.sounds.get('hit_villain'):
            try:
                self.sounds['hit_villain'].play()
            except:
                pass

    def play_hit_obstacle(self):
        if self.sounds.get('hit_obstacle'):
            try:
                self.sounds['hit_obstacle'].play()
            except:
                pass

    def play_victory(self):
        if self.sounds.get('victory'):
            try:
                self.sounds['victory'].play()
            except:
                pass

    def play_game_over(self):
        if self.sounds.get('game_over'):
            try:
                self.sounds['game_over'].play()
            except:
                pass

    def play_background_music(self):
        music_path = self.sounds.get('background_music')
        if music_path and self.music_playing != music_path:
            try:
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1)  # -1 means loop forever
                self.music_playing = music_path
                self.music_was_playing = True
            except:
                pass
        elif music_path and self.music_playing == music_path:
            # Music already playing
            self.music_was_playing = True

    def stop_music(self):
        try:
            self.music_was_playing = (self.music_playing is not None)
            pygame.mixer.music.stop()
            self.music_playing = None
        except:
            pass

    def resume_music_if_was_playing(self):
        if self.music_was_playing:
            self.play_background_music()

    def play_instruction_audio(self, mode):
        # Stop any currently playing instruction audio to prevent overlap
        if self.instruction_audio_playing:
            try:
                self.instruction_audio_playing.stop()
            except:
                pass

        audio_key = None
        if mode == 'easy':
            audio_key = 'easy_instructions'
        elif mode == 'normal':
            audio_key = 'normal_instructions'
        elif mode == 'hard':
            audio_key = 'hard_instructions'

        if audio_key and self.sounds.get(audio_key):
            try:
                self.instruction_audio_playing = self.sounds[audio_key]
                self.instruction_audio_playing.play()
            except:
                self.instruction_audio_playing = None

    def stop_instruction_audio(self):
        if self.instruction_audio_playing:
            try:
                self.instruction_audio_playing.stop()
                self.instruction_audio_playing = None
            except:
                self.instruction_audio_playing = None

    def change_music(self, new_music_path=None):
        self.stop_music()
        if new_music_path:
            try:
                pygame.mixer.music.load(new_music_path)
                pygame.mixer.music.play(-1)
                self.music_playing = new_music_path
            except:
                pass


# ========== TEXT RENDERING ==========
def render_text_with_outline(font, text, text_color, outline_color=BLACK, outline_width=2):
    outlines = []
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                outline_surf = font.render(text, True, outline_color)
                outlines.append((outline_surf, (dx, dy)))

    text_surf = font.render(text, True, text_color)

    final_surf = pygame.Surface(
        (text_surf.get_width() + outline_width * 2,
         text_surf.get_height() + outline_width * 2),
        pygame.SRCALPHA
    )

    for outline_surf, (dx, dy) in outlines:
        final_surf.blit(outline_surf, (outline_width + dx, outline_width + dy))

    final_surf.blit(text_surf, (outline_width, outline_width))

    return final_surf


# ========== TEXT WRAPPING ==========
def wrap_text(font, text, max_width, padding=15):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        # Test if adding this word would exceed width
        test_line = ' '.join(current_line + [word])
        test_surface = font.render(test_line, True, WHITE)

        if test_surface.get_width() <= max_width - (padding * 2):
            current_line.append(word)
        else:
            # Current line is full, save it and start new line
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    # Add the last line
    if current_line:
        lines.append(' '.join(current_line))

    rendered_lines = []
    for line in lines:
        rendered_lines.append(font.render(line, True, WHITE))

    return rendered_lines


# ========== CONFETTI ==========
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (255, 165, 0),
            (255, 192, 203),
        ]
        self.color = random.choice(colors)
        self.size = random.randint(4, 8)
        self.vel_x = random.uniform(-3, 3)
        self.vel_y = random.uniform(-5, -2)
        self.gravity = 0.3
        self.lifetime = random.uniform(1.5, 2.5)  # Seconds
        self.age = 0.0
        self.shape = random.choice(['rect', 'circle'])

    def update(self, dt):
        self.age += dt
        self.vel_y += self.gravity
        self.x += self.vel_x
        self.y += self.vel_y

    def is_alive(self):
        return self.age < self.lifetime

    def draw(self, screen):
        alpha = int(255 * (1.0 - self.age / self.lifetime))
        if self.shape == 'rect':
            pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size, self.size))
        else:
            pygame.draw.circle(screen, self.color, (int(self.x + self.size // 2), int(self.y + self.size // 2)),
                               self.size // 2)


# ========== IMAGE BUTTON ==========
class ImageButton:
    def __init__(self, x, y, image, hover_image=None):
        self.image = image
        self.hover_image = hover_image if hover_image else image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_hovered = False

    def draw(self, screen, text=None, font=None, color=BLACK):
        img = self.hover_image if self.is_hovered else self.image
        screen.blit(img, self.rect)

        if text and font:
            draw_text_centered(screen, text, self.rect, font, color)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    def check_click(self, pos):
        return self.rect.collidepoint(pos)


# ========== AUTO-RUNNER CLASSES (EASY MODE) ==========

class RunnerPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, player_image=None):
        super().__init__()
        if player_image:
            self.image = player_image.copy()
        else:
            self.image = load_image('assets/images/player.png', (65, 70), RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.on_ground = False
        self.jump_power = -18
        self.gravity = 0.8

    def update(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power


class ScrollingObstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, scroll_speed):
        super().__init__()
        try:
            obstacle_img = pygame.image.load('assets/images/obstacle_image.png').convert_alpha()
            self.image = pygame.transform.smoothscale(obstacle_img, (width, height))
        except:
            self.image = load_image('obstacle.png', (width, height), GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()


class ScrollingCoin(pygame.sprite.Sprite):
    def __init__(self, x, y, scroll_speed):
        super().__init__()
        self.image = load_image('assets/images/coin.png', (35, 35), YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()


class ScrollingHint(pygame.sprite.Sprite):
    def __init__(self, x, y, scroll_speed, question_data):
        super().__init__()
        self.image = load_image('assets/images/knowledge.png', (30, 38), YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed
        self.question_data = question_data

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()


class ScrollingQuestionTrigger(pygame.sprite.Sprite):
    def __init__(self, x, y, scroll_speed, question_data):
        super().__init__()
        self.image = load_image('assets/images/question.png', (70, 50), ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll_speed = scroll_speed
        self.question_data = question_data
        self.triggered = False

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()


class FinishLine(pygame.sprite.Sprite):
    def __init__(self, x, scroll_speed):
        super().__init__()
        self.image = load_image('assets/images/finish.png', (60, 100), BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = SCREEN_HEIGHT - 150
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed


# ========== PLATFORMER CLASSES (NORMAL/HARD MODE) ==========

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, settings, player_image_right=None, player_image_left=None):
        super().__init__()

        # Load right-facing image
        if player_image_right:
            self.image_right = player_image_right.copy()
        else:
            self.image_right = load_image('assets/images/player_right.png', (65, 70), RED)

        # Load left-facing image
        if player_image_left:
            self.image_left = player_image_left.copy()
        else:
            try:
                loaded_left = pygame.image.load('assets/images/player_left.png').convert_alpha()
                self.image_left = pygame.transform.smoothscale(loaded_left, (65, 70))
            except:
                # If left image not found, flip the right image
                self.image_left = pygame.transform.flip(self.image_right, True, False)

        # Start facing right
        self.image = self.image_right
        self.facing_right = True

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.on_ground = False
        self.settings = settings
        self.jumps_left = settings.get('max_jumps', 1)

    def update(self, platforms, bouncy_platforms):
        keys = pygame.key.get_pressed()

        # Horizontal movement with direction change
        move_speed = 7
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= move_speed
            # Change to left-facing sprite
            self.facing_right = False
            self.image = self.image_left
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += move_speed
            # Change to right-facing sprite
            self.facing_right = True
            self.image = self.image_right

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        self.vel_y += self.settings['gravity']
        self.rect.y += self.vel_y

        # Platform collision
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    if self.rect.bottom - self.vel_y <= platform.rect.top + 10:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                        self.jumps_left = self.settings.get('max_jumps', 1)
                elif self.vel_y < 0:
                    if self.rect.top - self.vel_y >= platform.rect.bottom - 10:
                        self.rect.top = platform.rect.bottom
                        self.vel_y = 0

        # Bouncy platform collision
        for bouncy in bouncy_platforms:
            if self.rect.colliderect(bouncy.rect) and self.vel_y > 0:
                if self.rect.bottom - self.vel_y <= bouncy.rect.top + 10:
                    self.rect.bottom = bouncy.rect.top
                    self.vel_y = self.settings['jump_power'] * 1.6
                    self.on_ground = False
                    self.jumps_left = self.settings.get('max_jumps', 1)

        # Floor collision (only for non-vertical modes)
        if not self.settings.get('is_vertical'):
            if self.rect.bottom > SCREEN_HEIGHT - 50:
                self.rect.bottom = SCREEN_HEIGHT - 50
                self.vel_y = 0
                self.on_ground = True
                self.jumps_left = self.settings.get('max_jumps', 1)

    def jump(self):
        if self.on_ground or self.jumps_left > 0:
            self.vel_y = self.settings['jump_power']
            self.jumps_left -= 1
            self.on_ground = False


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=GREEN):
        super().__init__()
        self.image = load_image('assets/images/platform.png', (width, height), color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class BouncyPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = load_image('assets/images/bouncy_platform.png', (width, height), GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('assets/images/coin.png', (35, 35), YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Hint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('assets/images/knowledge.png', (35, 35), YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, patrol_start=None, patrol_end=None):
        super().__init__()
        try:
            villain_img = pygame.image.load('assets/images/villain_image.png').convert_alpha()
            self.image = pygame.transform.smoothscale(villain_img, (65, 65))
        except:
            self.image = load_image('enemy.png', (30, 30), RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 1
        self.patrol_start = patrol_start if patrol_start else 0
        self.patrol_end = patrol_end if patrol_end else SCREEN_WIDTH

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left < self.patrol_start or self.rect.right > self.patrol_end:
            self.direction *= -1


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('assets/images/door.png', (60, 90), BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class QuestionTrigger(pygame.sprite.Sprite):
    def __init__(self, x, y, question_data):
        super().__init__()
        self.image = load_image('assets/images/question.png', (70, 50), ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.question_data = question_data
        self.answered = False


# ========== MAIN GAME CLASS ==========

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("NetGuard Adventure")
        self.clock = pygame.time.Clock()
        self.game_font, self.game_font_small, self.game_font_tiny = load_game_fonts()

        self.font = self.game_font_small
        self.small_font = self.game_font_tiny

        try:
            self.profile_font_title = pygame.font.Font('assets/fonts/Handjet-Medium.ttf', 64)
            self.profile_font_text = pygame.font.Font('assets/fonts/Handjet-Medium.ttf', 32)
        except Exception:
            self.profile_font_title = self.game_font
            self.profile_font_text = self.game_font_small

        self.language = 'en'
        self.state = MENU
        self.difficulty = None
        self.current_level = 1
        self.max_level = 5

        self.lives = 3
        self.coins = 0
        self.total_coins = 0
        self.time_left = 0
        self.total_time_spent = 0
        self.distance = 0
        self.altitude = 0
        self.high_score_hard = 0
        self.shield_active = False
        # Hard mode fall tracking
        self.hard_mode_fall_count = 0
        self.show_fall_warning = False
        self.fall_warning_timer = 0

        # Background scrolling
        self.bg_scroll = 0
        self.bg_speed = 2
        # Camera offset for vertical mode
        self.camera_y = 0

        # Button references
        self.game_over_menu_button = None
        self.level_complete_next_button = None
        self.level_complete_menu_button = None
        self.mode_victory_menu_button = None

        # Profile screen buttons
        self.profile_button = None
        self.profile_back_button = None

        # Shop message display
        self.shop_message = None
        self.shop_message_timer = 0

        # Instructions screen
        self.pending_difficulty = None
        self.instructions_play_button = None
        self.instructions_sound_button = None

        # Question feedback system
        self.confetti_particles = []
        self.shake_timer = 0.0
        self.shake_intensity = 0.0
        self.shake_offset_x = 0
        self.shake_offset_y = 0
        self.feedback_popup_text = None
        self.feedback_popup_timer = 0.0
        self.feedback_popup_correct = False

        # Hint system
        self.current_hint_text = None
        self.hint_popup_timer = 0
        self.current_question_data = None

        # Used question indices per mode
        self.used_question_indices = {'easy': set(), 'normal': set(), 'hard': set()}

        self.sound_manager = SoundManager()

        self.load_images()

        self.questions = self.load_questions()

        self.sound_manager.play_background_music()

    def load_images(self):
        # Load directional player images
        try:
            self.player_image_right = pygame.image.load('assets/images/player_right.png').convert_alpha()
            self.player_image_right = pygame.transform.smoothscale(self.player_image_right, (65, 70))
        except:
            self.player_image_right = None

        try:
            self.player_image_left = pygame.image.load('assets/images/player_left.png').convert_alpha()
            self.player_image_left = pygame.transform.smoothscale(self.player_image_left, (65, 70))
        except:
            # If left image not found, flip the right image
            if self.player_image_right:
                self.player_image_left = pygame.transform.flip(self.player_image_right, True, False)
            else:
                self.player_image_left = None

        # Set default player_image to right-facing
        self.player_image = self.player_image_right

        try:
            self.heart_image = pygame.image.load('assets/images/heart.png').convert_alpha()
            self.heart_image = pygame.transform.smoothscale(self.heart_image, (20, 20))
        except:
            self.heart_image = None

        self.menu_bg = load_image(
            'assets/images/menu_bg.png',
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            RED
        )

        try:
            easy_bg_original = pygame.image.load('assets/images/easy_bg.png').convert()
            original_width = easy_bg_original.get_width()
            original_height = easy_bg_original.get_height()
            scale_factor = SCREEN_HEIGHT / original_height
            new_width = int(original_width * scale_factor)
            self.easy_bg = pygame.transform.scale(easy_bg_original, (new_width, SCREEN_HEIGHT))
            self.easy_bg_width = new_width
        except:
            self.easy_bg = None
            self.easy_bg_width = SCREEN_WIDTH

        try:
            normal_bg_original = pygame.image.load('assets/images/normal_bg.png').convert()
            original_width = normal_bg_original.get_width()
            original_height = normal_bg_original.get_height()
            scale_factor = SCREEN_HEIGHT / original_height
            new_width = int(original_width * scale_factor)
            self.normal_bg = pygame.transform.scale(normal_bg_original, (new_width, SCREEN_HEIGHT))
            self.normal_bg_width = new_width
        except:
            self.normal_bg = None
            self.normal_bg_width = SCREEN_WIDTH

        try:
            hard_bg_original = pygame.image.load('assets/images/hard_bg.png').convert()
            original_width = hard_bg_original.get_width()
            original_height = hard_bg_original.get_height()
            scale_factor = SCREEN_WIDTH / original_width
            new_height = int(original_height * scale_factor)
            new_width = SCREEN_WIDTH
            self.hard_bg = pygame.transform.scale(hard_bg_original, (new_width, new_height))
            self.hard_bg_width = new_width
            self.hard_bg_height = new_height
        except:
            self.hard_bg = None
            self.hard_bg_width = SCREEN_WIDTH
            self.hard_bg_height = SCREEN_HEIGHT

        try:
            if self.language == 'en':
                level_up_original = pygame.image.load('assets/images/level_up_image.png').convert()
                self.level_up_bg = pygame.transform.scale(level_up_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
            else:
                level_up_original = pygame.image.load('assets/images/level_up_image_mk.jpg').convert()
                self.level_up_bg = pygame.transform.scale(level_up_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.level_up_bg = None

        try:
            if self.language == 'en':
                victory_original = pygame.image.load('assets/images/victory_image.png').convert()
                self.victory_bg = pygame.transform.scale(victory_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
            else:
                victory_original = pygame.image.load('assets/images/victory_image_mk.png').convert()
                self.victory_bg = pygame.transform.scale(victory_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.victory_bg = None

        try:
            if self.language == 'en':
                game_over_original = pygame.image.load('assets/images/game_over_image.png').convert()
                self.game_over_bg = pygame.transform.scale(game_over_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
            else:
                game_over_original = pygame.image.load('assets/images/game_over_image_mk.png').convert()
                self.game_over_bg = pygame.transform.scale(game_over_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.game_over_bg = None

        try:
            menu_button_original = pygame.image.load('assets/images/button.png').convert_alpha()
            self.menu_button_img = pygame.transform.smoothscale(menu_button_original, (180, 60))
            self.menu_button_hover = self.menu_button_img.copy()
            self.menu_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.menu_button_img = None
            self.menu_button_hover = None

        try:
            next_button_original = pygame.image.load('assets/images/button2.png').convert_alpha()
            self.next_button_img = pygame.transform.smoothscale(next_button_original, (180, 60))
            self.next_button_hover = self.next_button_img.copy()
            self.next_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.next_button_img = None
            self.next_button_hover = None

        try:
            profile_button_original = pygame.image.load('assets/images/profile_button.png').convert_alpha()
            self.profile_button_img = pygame.transform.smoothscale(profile_button_original, (60, 60))
            self.profile_button_hover = self.profile_button_img.copy()
            self.profile_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.profile_button_img = None
            self.profile_button_hover = None

        try:
            back_button_original = pygame.image.load('assets/images/back_button.png').convert_alpha()
            self.back_button_img = pygame.transform.smoothscale(back_button_original, (70, 40))
            self.back_button_hover = self.back_button_img.copy()
            self.back_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.back_button_img = None
            self.back_button_hover = None

        try:
            shop_original = pygame.image.load('assets/images/shop.png').convert()
            self.shop_bg = pygame.transform.scale(shop_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            try:
                shop_original = pygame.image.load('assets/images/shop.jpg').convert()
                self.shop_bg = pygame.transform.scale(shop_original, (SCREEN_WIDTH, SCREEN_HEIGHT))
            except:
                self.shop_bg = None

        try:
            self.shop_heart_img = pygame.image.load('assets/images/heart.png').convert_alpha()
            self.shop_heart_img = pygame.transform.smoothscale(self.shop_heart_img, (100, 100))
        except:
            self.shop_heart_img = None

        try:
            self.shop_time_img = pygame.image.load('assets/images/time.png').convert_alpha()
            self.shop_time_img = pygame.transform.smoothscale(self.shop_time_img, (100, 100))
        except:
            self.shop_time_img = None

        try:
            play_button_original = pygame.image.load('assets/images/button.png').convert_alpha()
            self.play_button_img = pygame.transform.smoothscale(play_button_original, (180, 60))
            self.play_button_hover = self.play_button_img.copy()
            self.play_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.play_button_img = None
            self.play_button_hover = None

        try:
            sound_button_original = pygame.image.load('assets/images/sound_button.png').convert_alpha()
            self.sound_button_img = pygame.transform.smoothscale(sound_button_original, (50, 50))
            self.sound_button_hover = self.sound_button_img.copy()
            self.sound_button_hover.fill((50, 50, 50, 0), special_flags=pygame.BLEND_RGBA_ADD)
        except:
            self.sound_button_img = None
            self.sound_button_hover = None

    def load_questions(self):
        return {
            'easy': [
                {
                    'en': {'question': 'Someone online offers you a free iPhone. What do you do?',
                           'options': ['Accept it!', 'Ignore and block'], 'correct': 1,
                           'hint': 'Free prizes from strangers are often scams.'},
                    'mk': {'question': 'Некој онлајн ти нуди бесплатен iPhone. Што правиш?',
                           'options': ['Прифаќам!', 'Игнорирам и блокирам'], 'correct': 1,
                           'hint': 'Бесплатни награди од непознати често се измама.'}
                },
                {
                    'en': {'question': 'A stranger asks "Where do you live?" What do you do?',
                           'options': ['Tell them', 'Block them'], 'correct': 1,
                           'hint': 'Private and sensitive information should not be shared with strangers.'},
                    'mk': {'question': 'Непознат прашува "Каде живееш?" Што правиш?',
                           'options': ['Му кажувам', 'Го блокирам'], 'correct': 1,
                           'hint': 'Приватните и сензитивни информации не треба да се споделуваат со непознати.'}
                },
                {
                    'en': {'question': 'Should you share your full name online?',
                           'options': ['Yes, always', 'No, be careful'], 'correct': 1,
                           'hint': 'Your full name can help strangers find you. Share less personal info online.'},
                    'mk': {'question': 'Треба ли да го споделуваш целото име онлајн?',
                           'options': ['Да, секогаш', 'Не, биди внимателен'], 'correct': 1,
                           'hint': 'Целото име може да помогне непознати да те пронајдат. Споделувај помалку лични податоци.'}
                },
                {
                    'en': {'question': 'Is it safe to use the same password for everything?',
                           'options': ['Yes', 'No'], 'correct': 1,
                           'hint': 'If one account gets hacked, all accounts are at risk. Use different passwords.'},
                    'mk': {'question': 'Дали е безбедно да користиш иста лозинка за сè?',
                           'options': ['Да', 'Не'], 'correct': 1,
                           'hint': 'Ако една сметка биде хакирана, сите се во ризик. Користи различни лозинки.'}
                },
                {
                    'en': {'question': 'Should you share your password with your best friend?',
                           'options': ['Yes', 'No'], 'correct': 1,
                           'hint': 'Passwords are like keys, only you should have them. Keep them secret.'},
                    'mk': {'question': 'Треба ли да ја споделиш лозинката со најдобриот пријател?',
                           'options': ['Да', 'Не'], 'correct': 1,
                           'hint': 'Лозинките се како клучеви, само ти треба да ги имаш. Чувај ги во тајност.'}
                },
                {
                    'en': {'question': 'Which is a strong password?',
                           'options': ['12345', 'MyDog8!xZ'], 'correct': 1,
                           'hint': 'Strong passwords have letters, numbers, and symbols. They are not easy to guess.'},
                    'mk': {'question': 'Која е силна лозинка?',
                           'options': ['12345', 'MyDog8!xZ'], 'correct': 1,
                           'hint': 'Силните лозинки имаат букви, бројки и знаци. Тешко се погодуваат.'}
                },
                {
                    'en': {'question': 'Someone online is being mean. What should you do?',
                           'options': ['Be mean back', 'Block and tell adult'], 'correct': 1,
                           'hint': 'Don’t fight back online. Block the person and tell a trusted adult.'},
                    'mk': {'question': 'Некој онлајн е лош и злобен. Што треба да направиш?',
                           'options': ['Да бидам груб и јас', 'Блокирај и кажи на возрасен'], 'correct': 1,
                           'hint': 'Не се расправај онлајн. Блокирај го и кажи на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Your friend shares your photo without asking. What do you do?',
                           'options': ['It\'s okay', 'Ask them to remove it'], 'correct': 1,
                           'hint': 'Your photos are your choice. You can ask them to delete it politely.'},
                    'mk': {'question': 'Твојот пријател ја сподели твојата фотографија без да праша. Што правиш?',
                           'options': ['Во ред е', 'Побарај да ја избрише'], 'correct': 1,
                           'hint': 'Твоите фотографии се твој избор. Можеш да побараш да ја избрише љубезно.'}
                },
                {
                    'en': {'question': 'Someone posts an embarrassing photo of you. What do you do?',
                           'options': ['Ignore it', 'Tell an adult'], 'correct': 1,
                           'hint': 'If something hurts or embarrasses you online, get help. Tell an adult you trust.'},
                    'mk': {'question': 'Некој постира срамна фотографија од тебе. Што правиш?',
                           'options': ['Игнорирам', 'Кажувам на возрасен'], 'correct': 1,
                           'hint': 'Ако нешто те повредува онлајн, побарај помош. Кажи на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Someone sends you a link saying "Click for prizes!" What do you do?',
                           'options': ['Click it!', 'Don\'t click'], 'correct': 1,
                           'hint': 'Prize links can be scams or viruses. Don’t click suspicious links.'},
                    'mk': {'question': 'Некој ти испраќа линк "Кликни за награди!" Што правиш?',
                           'options': ['Кликнувам!', 'Не кликнувам'], 'correct': 1,
                           'hint': 'Линкови за награди може да се измама или вирус. Не кликнувај сомнителни линкови.'}
                },
                {
                    'en': {'question': 'A message says "Your account is in danger! Click here!" What do you do?',
                           'options': ['Click immediately', 'Ask parent first'], 'correct': 1,
                           'hint': 'Scammers use scary messages to rush you. Pause and ask a parent/adult first.'},
                    'mk': {'question': 'Порака вели "Твојата сметка е во опасност! Кликни тука!" Што правиш?',
                           'options': ['Веднаш кликнувам', 'Прашувам родител'], 'correct': 1,
                           'hint': 'Измамници користат страв за да те брзаат. Застани и прашај родител/возрасен прво.'}
                },
                {
                    'en': {'question': 'Can you trust every link your friends send?',
                           'options': ['Yes, always', 'No, check first'], 'correct': 1,
                           'hint': 'Even friends can send unsafe links by mistake. Always check before clicking.'},
                    'mk': {'question': 'Дали можеш да им веруваш на сите линкови што ти ги испраќаат пријателите?',
                           'options': ['Да, секогаш', 'Не, провери прво'], 'correct': 1,
                           'hint': 'И пријател може да прати опасен линк по грешка. Секогаш провери пред да кликнеш.'}
                },
                {
                    'en': {'question': 'Should you tell strangers what school you go to?',
                           'options': ['Yes', 'No'], 'correct': 1,
                           'hint': 'Your school is personal information. Keep it private from strangers online.'},
                    'mk': {'question': 'Треба ли да им кажуваш на непознати во кое училиште одиш?',
                           'options': ['Да', 'Не'], 'correct': 1,
                           'hint': 'Училиштето е лична информација. Не го споделувај со непознати онлајн.'}
                },
                {
                    'en': {'question': 'Is it okay to post your vacation plans online?',
                           'options': ['Yes, tell everyone', 'No, wait until back'], 'correct': 1,
                           'hint': 'Posting plans can tell strangers when you’re away. Share after you return.'},
                    'mk': {'question': 'Дали е во ред да ги постираш плановите за одмор онлајн?',
                           'options': ['Да, кажи на сите', 'Не, почекај да се вратиш'], 'correct': 1,
                           'hint': 'Плановите може да покажат дека не си дома. Сподели откако ќе се вратиш.'}
                },
                {
                    'en': {'question': 'Who should know your home address online?',
                           'options': ['Everyone', 'Only trusted people'], 'correct': 1,
                           'hint': 'Your address should stay private. Only trusted people should know it.'},
                    'mk': {'question': 'Кој треба да ја знае твојата домашна адреса онлајн?',
                           'options': ['Сите', 'Само доверливи луѓе'], 'correct': 1,
                           'hint': 'Адресата треба да е приватна. Само доверливи луѓе треба да ја знаат.'}
                },
                {
                    'en': {'question': 'Someone you don’t know sends you a message. What should you do?',
                           'options': ['Reply', 'Ignore and tell an adult'], 'correct': 1,
                           'hint': 'Strangers online might not be safe. Don’t reply and tell a trusted adult.'},
                    'mk': {'question': 'Некој што не го познаваш ти праќа порака. Што треба да направиш?',
                           'options': ['Одговарам', 'Игнорирам и кажувам на возрасен'], 'correct': 1,
                           'hint': 'Непознати личности онлајн можат да бидат небезбедни. Не одговарај и кажи на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Is it okay to share your password online?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'Passwords protect your account. Sharing them can let others control it.'},
                    'mk': {'question': 'Дали е во ред да ја споделиш лозинката онлајн?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Лозинките го штитат твојот профил. Ако ги споделиш, некој може да го преземе.'}
                },
                {
                    'en': {'question': 'Someone online asks for your age. What do you do?',
                           'options': ['Tell them', 'Be careful and ask an adult'], 'correct': 1,
                           'hint': 'Age is personal information. If you’re unsure, ask an adult before sharing.'},
                    'mk': {'question': 'Некој онлајн те прашува за твојата возраст. Што правиш?',
                           'options': ['Му велам', 'Бидам внимателен и прашувам возрасен'], 'correct': 1,
                           'hint': 'Возраста е лична информација. Ако не си сигурен, прашај возрасен пред да споделиш.'}
                },
                {
                    'en': {'question': 'Should you click links from strangers?',
                           'options': ['Yes', 'No'], 'correct': 1,
                           'hint': 'Links from strangers can lead to scams or bad websites. It’s safer not to click.'},
                    'mk': {'question': 'Треба ли да кликнуваш линкови од непознати?',
                           'options': ['Да', 'Не'], 'correct': 1,
                           'hint': 'Линкови од непознати може да водат до измами или лоши страници. Побезбедно е да не кликнеш.'}
                },
                {
                    'en': {'question': 'Is it safe to tell strangers where you live?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'Your location can put you in danger. Keep your address private.'},
                    'mk': {'question': 'Дали е безбедно да им кажеш на непознати каде живееш?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Локацијата може да те доведе во опасност. Чувај ја адресата приватна.'}
                },
                {
                    'en': {'question': 'Someone makes you feel uncomfortable online. What should you do?',
                           'options': ['Keep chatting', 'Tell someone you trust'], 'correct': 1,
                           'hint': 'If something feels wrong, you don’t have to continue. Tell a trusted adult.'},
                    'mk': {'question': 'Некој те прави да се чувствуваш непријатно онлајн. Што правиш?',
                           'options': ['Продолжувам разговор', 'Кажувам на некој кому му верувам'], 'correct': 1,
                           'hint': 'Ако нешто не е во ред, не мора да продолжиш. Пренеси на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Should you share photos with people you don’t know?',
                           'options': ['Yes', 'No'], 'correct': 1,
                           'hint': 'Photos can be saved and shared by others. Only share with people you trust.'},
                    'mk': {'question': 'Треба ли да споделуваш фотографии со луѓе што не ги познаваш?',
                           'options': ['Да', 'Не'], 'correct': 1,
                           'hint': 'Фотографии може да се зачуваат и споделуваат. Споделувај само со луѓе на кои им веруваш.'}
                },
                {
                    'en': {'question': 'Someone asks for your full name. What do you do?',
                           'options': ['Tell them', 'Be careful and don’t share'], 'correct': 1,
                           'hint': 'Your full name is personal and can help strangers find you. Don’t share it.'},
                    'mk': {'question': 'Некој те прашува за твоето цело име. Што правиш?',
                           'options': ['Му велам', 'Бидам внимателен и не споделувам'], 'correct': 1,
                           'hint': 'Целото име е личен податок и може да помогне некој да те пронајде. Не го споделувај.'}
                },
                {
                    'en': {'question': 'A game says “Click here for free coins”. What do you do?',
                           'options': ['Click it', 'Ignore it'], 'correct': 1,
                           'hint': 'Free coins offers can be tricks. It’s safer to ignore suspicious pop-ups.'},
                    'mk': {'question': 'Игра вели „Кликни тука за бесплатни поени“. Што правиш?',
                           'options': ['Кликнувам', 'Го игнорирам'], 'correct': 1,
                           'hint': 'Понуди за бесплатни поени може да се измама. Побезбедно е да ги игнорираш сомнителните пораки.'}
                },
                {
                    'en': {'question': 'Is it safe to download games from unknown websites?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'Unknown websites can contain viruses. Download only from trusted sources.'},
                    'mk': {'question': 'Дали е безбедно да симнуваш игри од непознати веб-страници?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Непознати страници може да имаат вируси. Симнувај само од доверливи извори.'}
                },
                {
                    'en': {'question': 'Someone sends you a link and says “Trust me”. What should you do?',
                           'options': ['Click it', 'Check first or ask an adult'], 'correct': 1,
                           'hint': 'Even if someone says “trust me,” links can be unsafe. Check first or ask an adult.'},
                    'mk': {'question': 'Некој ти праќа линк и вели „Верувај ми“. Што треба да направиш?',
                           'options': ['Кликнувам', 'Проверам или прашувам возрасен'], 'correct': 1,
                           'hint': 'И кога некој вели „верувај ми“, линкот може да е опасен. Провери или прашај возрасен.'}
                },
                {
                    'en': {'question': 'Should you use your real name in online games?',
                           'options': ['Always', 'Only if safe'], 'correct': 1,
                           'hint': 'Using your real name shares personal info. It’s safer to use a nickname.'},
                    'mk': {'question': 'Треба ли да го користиш вистинското име во онлајн игри?',
                           'options': ['Секогаш', 'Само ако е безбедно'], 'correct': 1,
                           'hint': 'Вистинското име е личен податок. Побезбедно е да користиш прекар.'}
                },
                {
                    'en': {'question': 'Someone is being mean to you online. What should you do?',
                           'options': ['Be mean back', 'Block and tell an adult'], 'correct': 1,
                           'hint': 'Being mean back can make it worse. Block them and get help from an adult.'},
                    'mk': {'question': 'Некој е груб кон тебе онлајн. Што треба да направиш?',
                           'options': ['Да бидам груб назад', 'Блокирам и кажувам на возрасен'], 'correct': 1,
                           'hint': 'Ако вратиш со грубост, може да стане полошо. Блокирај и побарај помош од возрасен.'}
                },
                {
                    'en': {'question': 'Is it okay to share your school name online?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'School details can reveal where you are. Keep that information private.'},
                    'mk': {'question': 'Дали е во ред да го споделиш името на училиштето онлајн?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Училиштето може да открие каде си. Чувај ја таа информација приватно.'}
                },
                {
                    'en': {'question': 'What should you do if you see something scary online?',
                           'options': ['Keep watching', 'Close it and tell an adult'], 'correct': 1,
                           'hint': 'You don’t have to watch scary content. Close it and tell a trusted adult.'},
                    'mk': {'question': 'Што треба да направиш ако видиш нешто страшно онлајн?',
                           'options': ['Продолжувам да гледам', 'Затворам и кажувам на возрасен'], 'correct': 1,
                           'hint': 'Не мора да гледаш страшна содржина. Затвори и кажи на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Should you meet online friends alone?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'Meeting someone from the internet can be dangerous. Never meet alone and tell an adult.'},
                    'mk': {'question': 'Треба ли сам да се сретнеш со онлајн пријатели?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Средба со онлајн лице може да е опасно. Никогаш сам, кажи на возрасен.'}
                },
                {
                    'en': {'question': 'Is it safe to use the same password everywhere?',
                           'options': ['No', 'Yes'], 'correct': 0,
                           'hint': 'One leaked password can unlock many accounts. Use different passwords for safety.'},
                    'mk': {'question': 'Дали е безбедно да користиш иста лозинка насекаде?',
                           'options': ['Не', 'Да'], 'correct': 0,
                           'hint': 'Една откриена лозинка може да отвори многу сметки. Користи различни лозинки.'}
                },
                {
                    'en': {'question': 'What should you do before downloading something?',
                           'options': ['Ask an adult', 'Download immediately'], 'correct': 0,
                           'hint': 'Downloads can contain viruses or bad apps. Ask an adult or check the source first.'},
                    'mk': {'question': 'Што треба да направиш пред да симнеш нешто?',
                           'options': ['Прашај возрасен', 'Веднаш симнувам'], 'correct': 0,
                           'hint': 'Симнувања може да имаат вируси или лоши апликации. Прашај возрасен или провери извор.'}
                },
                {
                    'en': {'question': 'Someone asks you to keep a secret online. What do you do?',
                           'options': ['Keep it secret', 'Tell a trusted adult'], 'correct': 1,
                           'hint': 'Secrets online can be unsafe. If it feels wrong, tell a trusted adult.'},
                    'mk': {'question': 'Некој бара да чуваш тајна онлајн. Што правиш?',
                           'options': ['Ја чувам тајната', 'Кажувам на доверлив возрасен'], 'correct': 1,
                           'hint': 'Тајни онлајн може да бидат опасни. Ако не ти е пријатно, кажи на доверлив возрасен.'}
                },
                {
                    'en': {'question': 'Is it okay to ask for help if something feels wrong online?',
                           'options': ['Yes', 'No'], 'correct': 0,
                           'hint': 'Getting help is smart, not bad. Trusted adults can keep you safe.'},
                    'mk': {'question': 'Дали е во ред да побараш помош ако нешто не е во ред онлајн?',
                           'options': ['Да', 'Не'], 'correct': 0,
                           'hint': 'Барање помош е паметно. Доверливи возрасни можат да те заштитат.'}
                }
            ],
            'normal': [
                {
                    'en': {
                        'question': 'You receive an email: "Your account will be closed! Click here!" What do you do?',
                        'options': ['Click immediately', 'Check if real first', 'Delete the email'], 'correct': 2,
                        'hint': 'Scammers use fear to rush you into clicking. It’s safer to delete suspicious emails.'},
                    'mk': {'question': 'Добиваш е-пошта: "Твојата сметка ќе биде затворена! Кликни тука!" Што правиш?',
                           'options': ['Веднаш кликнувам', 'Проверувам дали е вистинска', 'Ја бришам е-поштата'],
                           'correct': 2,
                           'hint': 'Измамници користат страв за да те натераат да кликнеш. Побезбедно е да ја избришеш сомнителната порака.'}
                },
                {
                    'en': {'question': 'An email from "bank" has spelling mistakes. Is it safe?',
                           'options': ['Yes, it\'s fine', 'No, it\'s suspicious', 'Maybe'], 'correct': 1,
                           'hint': 'Real companies usually write carefully. Many spelling mistakes can be a warning sign.'},
                    'mk': {'question': 'Е-пошта од "банка" има правописни грешки. Дали е безбедна?',
                           'options': ['Да, во ред е', 'Не, е сомнителна', 'Можеби'], 'correct': 1,
                           'hint': 'Вистинските компании најчесто пишуваат внимателно. Многу правописни грешки се предупредувачки знак.'}
                },
                {
                    'en': {'question': 'What should you check before clicking a link?',
                           'options': ['Nothing', 'The sender', 'The URL'], 'correct': 2,
                           'hint': 'The link address (URL) shows where you will really go. Always look before you click.'},
                    'mk': {'question': 'Што треба да провериш пред да кликнеш на линк?',
                           'options': ['Ништо', 'Испраќачот', 'URL-то'], 'correct': 2,
                           'hint': 'URL-то покажува каде навистина води линкот. Секогаш провери пред да кликнеш.'}
                },
                {
                    'en': {'question': 'Who should see your social media posts?',
                           'options': ['Everyone', 'Friends only', 'Anyone who asks'], 'correct': 1,
                           'hint': 'Not everyone online is trustworthy. Using “friends only” helps protect your privacy.'},
                    'mk': {'question': 'Кој треба да ги гледа твоите постови на социјалните мрежи?',
                           'options': ['Сите', 'Само пријатели', 'Секој што праша'], 'correct': 1,
                           'hint': 'Не секој онлајн е доверлив. „Само пријатели“ подобро ја штити приватноста.'}
                },
                {
                    'en': {'question': 'Someone you don\'t know wants to be your friend online. What do you do?',
                           'options': ['Accept immediately', 'Check profile first', 'Decline'], 'correct': 2,
                           'hint': 'Some profiles are fake. If you don’t know them in real life, it’s safer to decline.'},
                    'mk': {'question': 'Некој што не го познаваш сака да биде твој пријател онлајн. Што правиш?',
                           'options': ['Веднаш прифаќам', 'Проверувам профил прво', 'Одбивам'], 'correct': 2,
                           'hint': 'Некои профили се лажни. Ако не го познаваш во живо, побезбедно е да одбиеш.'}
                },
                {
                    'en': {'question': 'What info should NOT be in your profile?',
                           'options': ['Hobbies', 'Home address', 'Favorite color'], 'correct': 1,
                           'hint': 'Some information can reveal where you live. Your address should stay private.'},
                    'mk': {'question': 'Која информација НЕ треба да биде во твојот профил?',
                           'options': ['Хобија', 'Домашна адреса', 'Омилена боја'], 'correct': 1,
                           'hint': 'Некои информации откриваат каде живееш. Домашната адреса треба да остане приватна.'}
                },
                {
                    'en': {'question': 'Someone online is being mean to you. What\'s the best response?',
                           'options': ['Be mean back', 'Block and tell adult', 'Ignore completely'], 'correct': 1,
                           'hint': 'Answering back can make it worse. Block them and ask a trusted adult for help.'},
                    'mk': {'question': 'Некој онлајн е груб кон тебе. Што е најдобар одговор?',
                           'options': ['Да бидам груб назад', 'Блокирај и кажи на возрасен', 'Целосно игнорирај'],
                           'correct': 1,
                           'hint': 'Ако вратиш со грубост, може да стане полошо. Блокирај и побарај помош од доверлив возрасен.'}
                },
                {
                    'en': {'question': 'You see someone being bullied online. What should you do?',
                           'options': ['Join in', 'Tell an adult', 'Do nothing'], 'correct': 1,
                           'hint': 'Bullying online is serious. Getting help from an adult is the safest choice.'},
                    'mk': {'question': 'Гледаш некој да биде малтретиран онлајн. Што треба да направиш?',
                           'options': ['Придружи се', 'Кажи на возрасен', 'Не прави ништо'], 'correct': 1,
                           'hint': 'Онлајн малтретирање е сериозно. Најбезбедно е да побараш помош од возрасен.'}
                },
                {
                    'en': {'question': 'Is it okay to share screenshots of private conversations?',
                           'options': ['Yes, always', 'No, never', 'Only if funny'], 'correct': 1,
                           'hint': 'Private chats are not meant for everyone. Sharing screenshots can hurt trust and privacy.'},
                    'mk': {'question': 'Дали е во ред да споделуваш скриншоти од приватни разговори?',
                           'options': ['Да, секогаш', 'Не, никогаш', 'Само ако е смешно'], 'correct': 1,
                           'hint': 'Приватни разговори не се за сите. Скриншоти можат да ја нарушат довербата и приватноста.'}
                },
                {
                    'en': {
                        'question': 'A website looks like your favorite store but the URL is different. What do you do?',
                        'options': ['Shop anyway', 'Close it', 'Enter card details'], 'correct': 1,
                        'hint': 'Fake websites copy real stores. If the URL looks wrong, leave the site.'},
                    'mk': {
                        'question': 'Веб-страница изгледа како твојата омилена продавница но URL-то е различно. Што правиш?',
                        'options': ['Купувам секако', 'Ја затворам', 'Внесувам детали за картичка'], 'correct': 1,
                        'hint': 'Лажни страници копираат вистински продавници. Ако URL-то е чудно, излези од страницата.'}
                },
                {
                    'en': {'question': 'How can you tell if a website is secure?',
                           'options': ['It has ads', 'It has https://', 'It has colors'], 'correct': 1,
                           'hint': 'Secure sites usually start with https://. It helps protect information you send.'},
                    'mk': {'question': 'Како можеш да провериш дали веб-страницата е безбедна?',
                           'options': ['Има реклами', 'Има https://', 'Има бои'], 'correct': 1,
                           'hint': 'Безбедни страници најчесто почнуваат со https://. Тоа помага да се заштитат податоците.'}
                },
                {
                    'en': {'question': 'A pop-up says "You won $1000!" What should you do?',
                           'options': ['Click it', 'Close it', 'Share it'], 'correct': 1,
                           'hint': 'Many pop-ups are scams or ads. Closing it is the safest choice.'},
                    'mk': {'question': 'Скокачки прозорец вели "Освои $1000!" Што треба да направиш?',
                           'options': ['Кликни', 'Затвори', 'Сподели'], 'correct': 1,
                           'hint': 'Многу скокачки прозорци се измама или реклами. Најбезбедно е да го затвориш.'}
                },
                {
                    'en': {'question': 'Is it safe to download files from unknown websites?',
                           'options': ['Yes', 'No', 'Sometimes'], 'correct': 1,
                           'hint': 'Unknown sites can contain viruses or unsafe files. Use only trusted sources.'},
                    'mk': {'question': 'Дали е безбедно да симнуваш фајлови од непознати веб-страници?',
                           'options': ['Да', 'Не', 'Понекогаш'], 'correct': 1,
                           'hint': 'Непознати страници може да имаат вируси или небезбедни фајлови. Користи само доверливи извори.'}
                },
                {
                    'en': {'question': 'A free game download asks for your phone number. What do you do?',
                           'options': ['Give it', 'Don\'t download', 'Use fake number'], 'correct': 1,
                           'hint': 'Games don’t usually need your phone number. If it asks, it can be risky, don’t download.'},
                    'mk': {'question': 'Бесплатна игра за симнување бара твој телефонски број. Што правиш?',
                           'options': ['Го давам', 'Не симнувам', 'Користам лажен број'], 'correct': 1,
                           'hint': 'Игрите најчесто не бараат телефонски број. Ако бара, може да е ризик, не симнувај.'}
                },
                {
                    'en': {'question': 'What should you do before downloading anything?',
                           'options': ['Nothing', 'Ask parent/guardian', 'Tell friends'], 'correct': 1,
                           'hint': 'Downloads can include unsafe apps or viruses. Ask a parent/guardian before you install.'},
                    'mk': {'question': 'Што треба да направиш пред да симнеш нешто?',
                           'options': ['Ништо', 'Прашај родител/старател', 'Кажи на пријатели'], 'correct': 1,
                           'hint': 'Симнувања може да имаат небезбедни апликации или вируси. Прашај родител/старател пред да инсталираш.'}
                },
                {
                    'en': {
                        'question': 'You get a message saying “I need your help urgently!”. What should you do first?',
                        'options': ['Reply immediately', 'Check who sent it', 'Ignore it forever'], 'correct': 1,
                        'hint': 'Urgent messages can be fake. First confirm who is messaging you.'},
                    'mk': {'question': 'Добиваш порака „Итно ми треба твоја помош!“. Што правиш прво?',
                           'options': ['Веднаш одговарам', 'Проверувам кој ја испратил', 'Ја игнорирам засекогаш'],
                           'correct': 1,
                           'hint': 'Итни пораки може да бидат лажни. Прво провери кој ти пишува.'}
                },
                {
                    'en': {'question': 'Which password is safer?',
                           'options': ['football123', 'MyCat!9A', '123456'], 'correct': 1,
                           'hint': 'Safe passwords mix letters, numbers, and symbols. Simple words and numbers are easy to guess.'},
                    'mk': {'question': 'Која лозинка е побезбедна?',
                           'options': ['football123', 'MyCat!9A', '123456'], 'correct': 1,
                           'hint': 'Побезбедни лозинки имаат букви, бројки и знаци. Едноставни зборови и броеви лесно се погодуваат.'}
                },
                {
                    'en': {'question': 'Why should you keep your social media account private?',
                           'options': ['To get more likes', 'To stay safer', 'To hide from friends'], 'correct': 1,
                           'hint': 'Private accounts limit who can see your information. This helps protect your privacy.'},
                    'mk': {'question': 'Зошто треба да ја држиш сметката на социјалните мрежи приватна?',
                           'options': ['За повеќе лајкови', 'За поголема безбедност', 'Да се криеш од пријатели'],
                           'correct': 1,
                           'hint': 'Приватните сметки ограничуваат кој ги гледа твоите информации. Така подобро се штити приватноста.'}
                },
                {
                    'en': {'question': 'Someone you don’t know asks to video chat. What do you do?',
                           'options': ['Accept', 'Ask why first', 'Block them'], 'correct': 2,
                           'hint': 'Video chat can reveal your face and location. If you don’t know them, blocking is safest.'},
                    'mk': {'question': 'Некој што не го познаваш бара видео разговор. Што правиш?',
                           'options': ['Прифаќам', 'Прашувам зошто', 'Го блокирам'], 'correct': 2,
                           'hint': 'Видео разговор може да открие лице и информации. Ако не го познаваш, најбезбедно е да блокираш.'}
                },
                {
                    'en': {'question': 'A website asks for your email to win a prize. What should you do?',
                           'options': ['Enter email', 'Check if site is real', 'Share with friends'], 'correct': 1,
                           'hint': 'Some “prize” sites only collect personal info. Check if it’s a real, trusted website first.'},
                    'mk': {'question': 'Веб-страница бара е-пошта за да освоиш награда. Што правиш?',
                           'options': ['Ја внесувам е-поштата', 'Проверувам дали е вистинска',
                                       'Ја споделувам со пријатели'], 'correct': 1,
                           'hint': 'Некои „награди“ само собираат лични податоци. Прво провери дали страницата е вистинска и доверлива.'}
                },
                {
                    'en': {'question': 'Someone’s profile has no photo and very few posts. What does this mean?',
                           'options': ['It’s safe', 'It could be fake', 'It’s popular'], 'correct': 1,
                           'hint': 'Fake accounts often have little information. Be careful with profiles that look empty.'},
                    'mk': {'question': 'Нечиј профил нема фотографија и има малку објави. Што може да значи ова?',
                           'options': ['Безбеден е', 'Може да е лажен', 'Не е многу е популарен'], 'correct': 1,
                           'hint': 'Лажни сметки често имаат малку информации. Биди внимателен со профили што изгледаат празно.'}
                },
                {
                    'en': {'question': 'Why should you log out of accounts on shared devices?',
                           'options': ['To save battery', 'To protect your account', 'To help others'], 'correct': 1,
                           'hint': 'If you stay logged in, others can use your account. Logging out keeps it protected.'},
                    'mk': {'question': 'Зошто треба да се одјавиш од сметки на заеднички уреди?',
                           'options': ['За штедење батерија', 'За заштита на сметката', 'За да им помогнеш на другите'],
                           'correct': 1,
                           'hint': 'Ако останеш најавен, други можат да ја користат твојата сметка. Одјавување значи поголема заштита.'}
                },
                {
                    'en': {'question': 'A player offers rare items if you share your login. What is this?',
                           'options': ['Fair trade', 'Scam', 'Game rule'], 'correct': 1,
                           'hint': 'Sharing login details can let someone steal your account. Real trades don’t need your password.'},
                    'mk': {'question': 'Играч нуди ретки предмети ако ја споделиш најавата. Што е ова?',
                           'options': ['Фер размена', 'Измама', 'Правило на играта'], 'correct': 1,
                           'hint': 'Ако ја споделиш најавата, некој може да ти ја украде сметката. Вистинска размена не бара лозинка.'}
                },
                {
                    'en': {'question': 'Someone pressures you to act fast online. Why is that risky?',
                           'options': ['You might not think', 'It saves time', 'It helps safety'], 'correct': 0,
                           'hint': 'Scammers rush people so they don’t think. Taking a moment helps you avoid mistakes.'},
                    'mk': {'question': 'Некој те притиска брзо да реагираш онлајн. Зошто е тоа ризично?',
                           'options': ['Можеш да не размислиш', 'Штеди време', 'Ја зголемува безбедноста'],
                           'correct': 0,
                           'hint': 'Измамници брзаат за да не размислиш. Ако застанеш и размислиш, избегнуваш грешки.'}
                },
                {
                    'en': {'question': 'What should you do if an app asks for unnecessary permissions?',
                           'options': ['Allow all', 'Deny or uninstall', 'Ignore it'], 'correct': 1,
                           'hint': 'Apps should only ask for permissions they truly need. If it seems unnecessary, deny or remove it.'},
                    'mk': {'question': 'Што треба да направиш ако апликација бара непотребни дозволи?',
                           'options': ['Дозволи сè', 'Одбиј или избриши', 'Игнорирај'], 'correct': 1,
                           'hint': 'Апликации треба да бараат само потребни дозволи. Ако е непотребно, одбиј или избриши ја.'}
                },
                {
                    'en': {'question': 'Is it safe to use the same username everywhere?',
                           'options': ['Yes', 'No', 'Only in games'], 'correct': 1,
                           'hint': 'Using one username everywhere makes it easier to track you. It’s safer to vary usernames.'},
                    'mk': {'question': 'Дали е безбедно да користиш исто корисничко име насекаде?',
                           'options': ['Да', 'Не', 'Само во игри'], 'correct': 1,
                           'hint': 'Едно корисничко име насекаде те прави полесен за следење. Побезбедно е да менуваш кориснички имиња.'}
                },
                {
                    'en': {'question': 'A post sounds shocking but has no source. What should you do?',
                           'options': ['Share it', 'Check other sources', 'Comment angrily'], 'correct': 1,
                           'hint': 'Not everything online is true. Checking sources helps you avoid spreading misinformation.'},
                    'mk': {'question': 'Објава споделува шокантни вести, но нема извор. Што правиш?',
                           'options': ['Ја споделувам', 'Проверувам други извори', 'Луто коментирам'], 'correct': 1,
                           'hint': 'Не е сè онлајн вистинито. Проверка на извори помага да не шириш лажни информации.'}
                },
                {
                    'en': {'question': 'Why do scammers pretend to be friends?',
                           'options': ['For fun', 'To gain trust', 'To help you'], 'correct': 1,
                           'hint': 'Scammers try to earn trust so you share information. Being cautious keeps you safer.'},
                    'mk': {'question': 'Зошто измамниците се преправаат дека ти се пријатели?',
                           'options': ['За забава', 'За да стекнат доверба', 'За да помогнат'], 'correct': 1,
                           'hint': 'Измамници градат доверба за да добијат информации. Внимателноста те штити.'}
                },
                {
                    'en': {
                        'question': 'Someone asks you to keep online behavior secret from parents. What does this signal?',
                        'options': ['Normal', 'Warning sign', 'Game rule'], 'correct': 1,
                        'hint': 'Trusted people don’t ask kids to hide things from parents. This is a red flag.'},
                    'mk': {'question': 'Некој бара онлајн однесувањето да го криеш од родители. Што значи тоа?',
                           'options': ['Нормално е', 'Предупредувачки знак', 'Правило на играта'], 'correct': 1,
                           'hint': 'Доверливи луѓе не бараат да криеш нешта од родители. Ова е предупредувачки знак.'}
                },
                {
                    'en': {'question': 'Is everything you see online true?',
                           'options': ['Yes', 'No', 'Only videos'], 'correct': 1,
                           'hint': 'Anyone can post online, even if it’s false. It’s smart to question and check information.'},
                    'mk': {'question': 'Дали сè што гледаш онлајн е вистинито?',
                           'options': ['Да', 'Не', 'Само видеата'], 'correct': 1,
                           'hint': 'Секој може да објави онлајн, дури и ако не е вистина. Паметно е да се проверуваат информации.'}
                },
                {
                    'en': {'question': 'What should you do if your account is acting strangely?',
                           'options': ['Ignore it', 'Change password', 'Post about it'], 'correct': 1,
                           'hint': 'Strange behavior can mean someone has access. Changing your password helps secure the account.'},
                    'mk': {'question': 'Што треба да направиш ако профилот твој има работи што ти не ги објави?',
                           'options': ['Ја игнорирам', 'Ја менувам лозинката', 'Објавувам за тоа'], 'correct': 1,
                           'hint': 'Чудно однесување може да значи дека некој има пристап. Менување лозинка помага да го заштитиш профилот.'}
                },
                {
                    'en': {'question': 'Why is it important to think before posting?',
                           'options': ['Posts disappear', 'Posts can stay online', 'Posts give points'], 'correct': 1,
                           'hint': 'Posts can be saved, shared, and seen later. Think about privacy and consequences first.'},
                    'mk': {'question': 'Зошто е важно да размислиш пред да објавиш нешто?',
                           'options': ['Објавите исчезнуваат', 'Објавите остануваат онлајн достапни засекогаш',
                                       'Објавите даваат поени'],
                           'correct': 1,
                           'hint': 'Објави можат да се зачуваат и споделуваат и подоцна. Прво размисли за приватност и последици.'}
                },
                {
                    'en': {'question': 'What is the safest reaction to online pressure?',
                           'options': ['Give in', 'Pause and ask for help', 'Argue'], 'correct': 1,
                           'hint': 'Pressure is used to make you decide fast. Pausing and asking for help keeps you safer.'},
                    'mk': {'question': 'Која е најбезбедна реакција на онлајн притисок?',
                           'options': ['Попуштам', 'Застанувам и барам помош', 'Се расправам'], 'correct': 1,
                           'hint': 'Притисок се користи за брза одлука. Ако застанеш и побараш помош, си побезбеден.'}
                },
                {
                    'en': {'question': 'Who should you talk to if something online worries you?',
                           'options': ['No one', 'Trusted adult', 'Strangers online'], 'correct': 1,
                           'hint': 'Adults you trust can help and protect you. Strangers online may not have good intentions.'},
                    'mk': {'question': 'Со кого треба да разговараш ако нешто онлајн те загрижува?',
                           'options': ['Со никого', 'Со доверлив возрасен', 'Со непознати онлајн'], 'correct': 1,
                           'hint': 'Доверливи возрасни можат да помогнат и да те заштитат. Непознати онлајн можат да имаат лоши намери.'}
                }
            ],
            'hard': [
                {
                    'en': {'question': 'A website asks for your password to "verify your account". What do you do?',
                           'options': ['Enter password', 'Contact official support', 'Close the site'],
                           'correct': 2,
                           'hint': 'Real websites usually don’t ask for your password like this. Close it and use official support channels.'},
                    'mk': {'question': 'Веб-страница бара твоја лозинка за да "ја потврди сметката". Што правиш?',
                           'options': ['Ја внесувам лозинката', 'Го контактирам службената поддршка',
                                       'Ја затворам страницата'],
                           'correct': 2,
                           'hint': 'Вистински страници ретко бараат лозинка на ваков начин.'}
                },
                {
                    'en': {'question': 'An email from "PayPal" uses @paypa1.com (with number 1). What is this?',
                           'options': ['Legitimate email', 'Phishing attempt', 'Typo'],
                           'correct': 1,
                           'hint': 'Scammers often use look-alike addresses (like 1 instead of l). A small change can mean phishing.'},
                    'mk': {'question': 'Е-пошта од "PayPal" користи @paypa1.com (со број 1). Што е ова?',
                           'options': ['Легитимна е-пошта', 'Обид за фишинг', 'Грешка во пишување'],
                           'correct': 1,
                           'hint': 'Измамници користат слични адреси (1 наместо l). Мала промена често значи фишинг.'}
                },
                {
                    'en': {'question': 'What is two-factor authentication (2FA)?',
                           'options': ['Two passwords', 'Extra security layer', 'Double login'],
                           'correct': 1,
                           'hint': '2FA adds a second step, like a code on your phone. It makes accounts harder to hack.'},
                    'mk': {'question': 'Што е двофакторска автентикација (2FA)?',
                           'options': ['Две лозинки', 'Дополнителен безбедносен слој', 'Двојна најава'],
                           'correct': 1,
                           'hint': '2FA додава втор чекор, како код на телефон. Така профилите потешко се пробиваат.'}
                },
                {
                    'en': {'question': 'Someone claims to be tech support and asks for remote access. What do you do?',
                           'options': ['Give access', 'Verify identity first', 'Hang up'],
                           'correct': 2,
                           'hint': 'Real support won’t pressure you for remote access unexpectedly. If unsure, stop and contact official support yourself.'},
                    'mk': {'question': 'Некој тврди дека е техничка поддршка и бара далечински пристап. Што правиш?',
                           'options': ['Давам пристап', 'Проверувам идентитет прво', 'Затворам'],
                           'correct': 2,
                           'hint': 'Вистинска техничка поддршка не бара пристап наеднаш со притисок.'}
                },
                {
                    'en': {'question': 'What is "social engineering" in cybersecurity?',
                           'options': ['Making friends online', 'Manipulating people for info', 'Social media design'],
                           'correct': 1,
                           'hint': 'Social engineering tricks people into giving information. It uses emotions like fear or trust.'},
                    'mk': {'question': 'Што е "социјално инженерство" во кибер безбедноста?',
                           'options': ['Склучување пријателства онлајн', 'Манипулирање луѓе за информации',
                                       'Дизајн на социјални медиуми'],
                           'correct': 1,
                           'hint': 'Социјално инженерство е кога некој те измамува да дадеш информации. Често користи страв или доверба.'}
                },
                {
                    'en': {'question': 'A message says "Your friend is in trouble, send money!" What should you do?',
                           'options': ['Send money', 'Call friend directly', 'Reply to message'],
                           'correct': 1,
                           'hint': 'Messages like this can be scams. Verify by calling your friend or a trusted person directly.'},
                    'mk': {
                        'question': 'Порака вели "Твојот пријател е во неволја, испрати пари!" Што треба да направиш?',
                        'options': ['Испраќам пари', 'Го јавувам пријателот директно', 'Одговарам на порака'],
                        'correct': 1,
                        'hint': 'Вакви пораки може да се измама. Провери така што ќе се јавиш на пријателот директно.'}
                },
                {
                    'en': {'question': 'You see a post with false information spreading. What should you do?',
                           'options': ['Share it quickly', 'Report it and don\'t share', 'Comment angrily'],
                           'correct': 1,
                           'hint': 'Sharing spreads misinformation faster. Reporting and not sharing helps stop it.'},
                    'mk': {'question': 'Видиш објава со лажни информации што се шират. Што треба да направиш?',
                           'options': ['Брзо да ја споделам', 'Да ја пријавам и да не ја споделам',
                                       'Лутаво да коментирам'],
                           'correct': 1,
                           'hint': 'Споделувањето побрзо шири лажни информации. Пријави ја и не ја споделувај.'}
                },
                {
                    'en': {'question': 'How can you verify if news is real?',
                           'options': ['Check multiple sources', 'Trust the headline', 'Ask friends'],
                           'correct': 0,
                           'hint': 'Headlines can be misleading. Checking several reliable sources helps confirm the truth.'},
                    'mk': {'question': 'Како можеш да провериш дали вестите се вистински?',
                           'options': ['Провери повеќе извори', 'Верувај на насловот', 'Прашај пријатели'],
                           'correct': 0,
                           'hint': 'Насловите можат да бидат измамни. Провери повеќе доверливи извори за да бидеш сигурен.'}
                },
                {
                    'en': {'question': 'What is a "deepfake"?',
                           'options': ['Deep web', 'Fake AI-generated media', 'Fake profile'],
                           'correct': 1,
                           'hint': 'A deepfake is media made with AI to look real. It can trick people with fake videos or voices.'},
                    'mk': {'question': 'Што е "deepfake"?',
                           'options': ['Длабок веб', 'Лажни АИ-генерирани медиуми', 'Лажен профил'],
                           'correct': 1,
                           'hint': 'Deepfake е содржина направена со АИ што изгледа вистинито. Може да измами со лажни видеа или глас.'}
                },
                {
                    'en': {'question': 'What makes a password most secure?',
                           'options': ['Length only', 'Complexity only', 'Length + complexity + unique'],
                           'correct': 2,
                           'hint': 'Strong passwords are long, hard to guess, and different for each account. Using one password everywhere is risky.'},
                    'mk': {'question': 'Што прави лозинката најбезбедна?',
                           'options': ['Само должина', 'Само сложеност', 'Должина + сложеност + уникатност'],
                           'correct': 2,
                           'hint': 'Силни лозинки се долги, тешки за погодување и различни за секој профил. Иста лозинка насекаде е ризик.'}
                },
                {
                    'en': {'question': 'Your account was hacked. What should you do FIRST?',
                           'options': ['Delete account', 'Change password', 'Tell friends'],
                           'correct': 1,
                           'hint': 'The first goal is to stop the attacker from staying in. Changing the password quickly can protect the account.'},
                    'mk': {'question': 'Твојата сметка беше хакирана. Што треба да направиш ПРВО?',
                           'options': ['Избриши сметка', 'Смени лозинка', 'Кажи на пријатели'],
                           'correct': 1,
                           'hint': 'Прво треба да спречиш напаѓачот да има пристап. Брза промена на лозинка го штити профилот.'}
                },
                {
                    'en': {'question': 'What is a "password manager"?',
                           'options': ['Person who manages passwords', 'Tool that stores passwords securely',
                                       'Password creator'],
                           'correct': 1,
                           'hint': 'A password manager is an app that stores passwords safely. It helps you use strong, unique passwords.'},
                    'mk': {'question': 'Што е "менаџер на лозинки"?',
                           'options': ['Личност која управува со лозинки', 'Алатка која безбедно чува лозинки',
                                       'Креатор на лозинки'],
                           'correct': 1,
                           'hint': 'Менаџер на лозинки е алатка што безбедно ги чува лозинките. Помага да користиш силни и уникатни лозинки.'}
                },
                {
                    'en': {'question': 'What does "end-to-end encryption" mean?',
                           'options': ['Messages are private', 'Messages are public', 'Messages are deleted'],
                           'correct': 0,
                           'hint': 'End-to-end encryption means only the sender and receiver can read messages. Others can’t easily see them.'},
                    'mk': {'question': 'Што значи "енд-ту-енд енкрипција"?',
                           'options': ['Пораките се приватни', 'Пораките се јавни', 'Пораките се избришани'],
                           'correct': 0,
                           'hint': 'End-to-end енкрипција значи дека само испраќачот и примачот можат да ги прочитаат пораките. Други тешко можат да ги видат.'}
                },
                {
                    'en': {
                        'question': 'An app asks for access to contacts, camera, location. What should you consider?',
                        'options': ['Allow all', 'Check if necessary', 'Deny all'],
                        'correct': 1,
                        'hint': 'Apps should only get permissions they need to work. If it’s not needed, don’t allow it.'},
                    'mk': {'question': 'Апликација бара пристап до контакти, камера, локација. Што треба да размислиш?',
                           'options': ['Дозволи сè', 'Провери дали е потребно', 'Одбиј сè'],
                           'correct': 1,
                           'hint': 'Апликации треба да добијат само дозволи што им се потребни. Ако не е потребно, не дозволувај.'}
                },
                {
                    'en': {'question': 'What is "digital footprint"?',
                           'options': ['Foot size online', 'Trail of data you leave', 'Walking tracker'],
                           'correct': 1,
                           'hint': 'Your digital footprint is the information you leave online. Posts, likes, and searches can be part of it.'},
                    'mk': {'question': 'Што е "дигитален отпечаток"?',
                           'options': ['Број на нога онлајн', 'Трага на податоци што ја оставаш', 'Следач на чекори'],
                           'correct': 1,
                           'hint': 'Дигитален отпечаток е трага од информации што ја оставаш онлајн. Објави, лајкови и пребарувања се дел од тоа.'}
                },
                {
                    'en': {'question': 'Which situation is most likely a phishing attempt?',
                           'options': ['Email from a known contact', 'Message asking for urgent login',
                                       'Saved bookmark'],
                           'correct': 1,
                           'hint': 'Phishing often pressures you to log in quickly. Urgent login messages are a common scam.'},
                    'mk': {'question': 'Која ситуација најчесто е обид за фишинг?',
                           'options': ['Е-пошта од познат контакт', 'Порака што бара итна најава',
                                       'Зачуван обележувач'],
                           'correct': 1,
                           'hint': 'Фишинг често те брза да се најавиш веднаш. Итни пораки за најава се честа измама.'}
                },
                {
                    'en': {'question': 'Why should you avoid clicking shortened links?',
                           'options': ['They load slowly', 'They can hide real destinations', 'They cost money'],
                           'correct': 1,
                           'hint': 'Short links can hide the real website address. You may not know where you are being sent.'},
                    'mk': {'question': 'Зошто треба да избегнуваш скратени линкови?',
                           'options': ['Се вчитуваат бавно', 'Можат да ја сокријат вистинската адреса', 'Чинат пари'],
                           'correct': 1,
                           'hint': 'Скратени линкови можат да ја сокријат вистинската адреса. Можеш да не знаеш каде навистина одиш.'}
                },
                {
                    'en': {'question': 'What makes two-factor authentication effective?',
                           'options': ['Two usernames', 'Extra verification step', 'Double passwords'],
                           'correct': 1,
                           'hint': '2FA requires something extra, like a code or app approval. It adds protection even if a password leaks.'},
                    'mk': {'question': 'Што ја прави двофакторската автентикација ефикасна?',
                           'options': ['Две кориснички имиња', 'Дополнителен чекор за потврда', 'Две лозинки'],
                           'correct': 1,
                           'hint': '2FA бара дополнително нешто, како код или потврда преку апликација. Штити дури и ако лозинката се открие.'}
                },
                {
                    'en': {'question': 'An app requests microphone access without reason. What should you do?',
                           'options': ['Allow it', 'Deny and review permissions', 'Ignore it'],
                           'correct': 1,
                           'hint': 'If an app doesn’t need the microphone, it shouldn’t have access. Review and deny unnecessary permissions.'},
                    'mk': {'question': 'Апликација бара пристап до микрофон без причина. Што правиш?',
                           'options': ['Дозволувам', 'Одбивам и ги проверувам дозволите', 'Игнорирам'],
                           'correct': 1,
                           'hint': 'Ако апликацијата не му треба микрофон, не треба да има пристап. Одбиј и провери ги дозволите.'}
                },
                {
                    'en': {'question': 'Why do attackers impersonate trusted companies?',
                           'options': ['To look professional', 'To gain user trust', 'To advertise'],
                           'correct': 1,
                           'hint': 'Attackers copy trusted brands so you feel safe. Trust can make people share information or click links.'},
                    'mk': {'question': 'Зошто напаѓачите се претставуваат како доверливи компании?',
                           'options': ['За да изгледаат професионално', 'За да стекнат доверба', 'За реклама'],
                           'correct': 1,
                           'hint': 'Напаѓачите копираат познати компании за да се чувствуваш безбедно. Довербата може да те натера да кликнеш или да споделиш информации.'}
                },
                {
                    'en': {'question': 'Someone asks for a one-time code you received. What is the risk?',
                           'options': ['No risk', 'Account takeover', 'Spam messages'],
                           'correct': 1,
                           'hint': 'One-time codes are meant only for you. Sharing them can let someone log in as you.'},
                    'mk': {'question': 'Некој бара еднократен код што си го добил. Кој е ризикот?',
                           'options': ['Нема ризик', 'Преземање на сметката', 'Несакани пораки'],
                           'correct': 1,
                           'hint': 'Еднократните кодови се само за тебе. Ако ги споделиш, некој може да се најави како тебе.'}
                },
                {
                    'en': {'question': 'What is the main danger of deepfake videos?',
                           'options': ['Low quality', 'Spreading false information', 'Large file size'],
                           'correct': 1,
                           'hint': 'Deepfakes can look real and trick people. They are dangerous because they can spread lies.'},
                    'mk': {'question': 'Која е главната опасност од deepfake видеа?',
                           'options': ['Низок квалитет', 'Ширење лажни информации', 'Голема големина на фајл'],
                           'correct': 1,
                           'hint': 'Deepfake може да изгледа како вистинско и да измами. Опасно е затоа што може да шири лаги.'}
                },
                {
                    'en': {'question': 'How can you best verify online news?',
                           'options': ['Check multiple reliable sources', 'Trust comments', 'Believe headlines'],
                           'correct': 0,
                           'hint': 'One post isn’t enough to prove something. Checking reliable sources helps confirm it.'},
                    'mk': {'question': 'Како најдобро можеш да провериш онлајн вести?',
                           'options': ['Провери повеќе доверливи извори', 'Верувај на коментари',
                                       'Верувај на насловот'],
                           'correct': 0,
                           'hint': 'Една објава не е доказ. Проверка на доверливи извори помага да потврдиш дали е вистина.'}
                },
                {
                    'en': {
                        'question': 'You notice login alerts from places you don’t recognize. What should you do first?',
                        'options': ['Ignore them', 'Secure the account settings', 'Post about it online'],
                        'correct': 1,
                        'hint': 'Unknown login alerts can mean someone is trying to access your account. Secure your settings and protections first.'},
                    'mk': {
                        'question': 'Забележуваш најави од локации што не ги препознаваш. Што треба да направиш прво?',
                        'options': ['Ги игнорирам', 'Ги обезбедувам поставките на сметката', 'Објавувам за тоа онлајн'],
                        'correct': 1,
                        'hint': 'Непознати најави може да значат обид за пристап. Прво обезбеди го профилот.'}
                },
                {
                    'en': {'question': 'Why is using a password manager recommended?',
                           'options': ['Stores passwords securely', 'Creates usernames', 'Deletes accounts'],
                           'correct': 0,
                           'hint': 'Password managers store passwords safely and help you use strong, unique ones. This reduces account risk.'},
                    'mk': {'question': 'Зошто се препорачува користење менаџер на лозинки?',
                           'options': ['Безбедно чува лозинки', 'Креира кориснички имиња', 'Брише сметки'],
                           'correct': 0,
                           'hint': 'Менаџерите на лозинки ги чуваат лозинките безбедно и помагаат да користиш силни и уникатни. Така се намалува ризикот.'}
                }
            ]
        }

    def get_level_questions(self, difficulty, level):
        all_questions = self.questions[difficulty]
        used = self.used_question_indices[difficulty]
        available = [i for i in range(len(all_questions)) if i not in used]
        n = 2 if (difficulty == 'normal' and level == 1) else 3
        k = min(n, len(available))
        if k == 0:
            return []
        picked = random.sample(available, k)
        used.update(picked)
        return [all_questions[i] for i in picked]

    def create_level_easy(self):
        """Auto-runner level for Easy mode"""
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()
        self.question_triggers = pygame.sprite.Group()
        self.hints_group = pygame.sprite.Group()
        self.finish_line_group = pygame.sprite.Group()

        self.player = RunnerPlayer(150, SCREEN_HEIGHT - 100, self.player_image)
        self.all_sprites.add(self.player)

        base_speed = DIFFICULTY_SETTINGS['easy']['scroll_speed_base']
        scroll_speed = base_speed + (self.current_level - 1) * 1.5

        level_length = 4000 + (self.current_level * 1000)
        obstacle_chance = 0.20 + (self.current_level * 0.05)  # 0.20
        min_spacing = 100 - (self.current_level * 10)
        max_spacing = 200 - (self.current_level * 15)

        current_x = 800
        questions = self.get_level_questions('easy', self.current_level)
        question_positions = []

        for i in range(len(questions)):
            pos = 1000 + (i * (level_length - 1000) // len(questions))
            question_positions.append(pos)

        question_index = 0

        while current_x < level_length:
            if random.random() < obstacle_chance:
                height = random.randint(40, 60 + self.current_level * 10)
                width = random.randint(40, 50 + self.current_level * 5)
                obstacle = ScrollingObstacle(current_x, SCREEN_HEIGHT - 50 - height, width, height, scroll_speed)
                self.obstacles.add(obstacle)
                self.all_sprites.add(obstacle)
                current_x += width + random.randint(min_spacing, max_spacing)

            if random.random() < 0.85:
                coin_height = random.choice([
                    SCREEN_HEIGHT - 150,
                    SCREEN_HEIGHT - 250,
                    SCREEN_HEIGHT - 80
                ])
                coin = ScrollingCoin(current_x, coin_height, scroll_speed)
                self.coins_group.add(coin)
                self.all_sprites.add(coin)

            if question_index < len(question_positions) and current_x >= question_positions[question_index]:
                if question_index < len(questions):
                    q = ScrollingQuestionTrigger(
                        current_x,
                        SCREEN_HEIGHT - 200,
                        scroll_speed,
                        questions[question_index]
                    )
                    self.question_triggers.add(q)
                    self.all_sprites.add(q)
                    if 'hint' in questions[question_index].get('en', {}) and questions[question_index]['en'].get(
                            'hint'):
                        hint_height = random.choice([
                            SCREEN_HEIGHT - 150,
                            SCREEN_HEIGHT - 250,
                            SCREEN_HEIGHT - 80
                        ])
                        hint = ScrollingHint(current_x + random.randint(-200, 200), hint_height, scroll_speed,
                                             questions[question_index])
                        self.hints_group.add(hint)
                        self.all_sprites.add(hint)
                question_index += 1
                current_x += 300

            current_x += random.randint(150, 300)

        finish = FinishLine(level_length, scroll_speed)
        self.finish_line_group.add(finish)
        self.all_sprites.add(finish)

    def create_level_platformer(self):
        """Platform level for Normal mode with 5 level designs"""
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.bouncy_platforms = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.question_triggers = pygame.sprite.Group()
        self.hints_group = pygame.sprite.Group()

        settings = DIFFICULTY_SETTINGS[self.difficulty].copy()
        settings['enemy_speed'] = settings['enemy_speed_base'] + (self.current_level - 1) * 0.8
        settings['time_limit'] = settings['time_limit_base'] - (self.current_level - 1) * 10

        self.player = Player(50, SCREEN_HEIGHT - 100, settings, self.player_image_right, self.player_image_left)
        self.all_sprites.add(self.player)

        questions = self.get_level_questions('normal', self.current_level)

        if self.current_level == 1:
            p1 = Platform(200, 400, 150, 20)
            p2 = Platform(500, 300, 150, 20)
            p3 = Platform(750, 400, 150, 20)
            self.platforms.add(p1, p2, p3)
            self.all_sprites.add(p1, p2, p3)

            b1 = BouncyPlatform(350, 450, 100, 15)
            self.bouncy_platforms.add(b1)
            self.all_sprites.add(b1)

            for x in [250, 550, 800]:
                c = Coin(x, 350)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            door_x = 900
            e = Enemy(400, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            self.enemies.add(e)
            self.all_sprites.add(e)

            for i, q_data in enumerate(questions):
                q = QuestionTrigger(300 + i * 300, 250, q_data)
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in q_data.get('en', {}) and q_data['en'].get('hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)
                    hint_y = random.randint(100, SCREEN_HEIGHT - 100)
                    hint = Hint(hint_x, hint_y)
                    hint.question_data = q_data
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

            door = Door(door_x, SCREEN_HEIGHT - 130)
            self.doors.add(door)
            self.all_sprites.add(door)

        elif self.current_level == 2:
            p1 = Platform(150, 380, 120, 20)
            p2 = Platform(400, 280, 120, 20)
            p3 = Platform(650, 350, 120, 20)
            p4 = Platform(220, 200, 100, 20)
            self.platforms.add(p1, p2, p3, p4)
            self.all_sprites.add(p1, p2, p3, p4)

            b1 = BouncyPlatform(300, 450, 100, 15)
            b2 = BouncyPlatform(550, 450, 100, 15)
            self.bouncy_platforms.add(b1, b2)
            self.all_sprites.add(b1, b2)

            for x in [200, 450, 700, 270]:
                c = Coin(x, 320)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            door_x = 880
            e1 = Enemy(300, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e2 = Enemy(600, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            self.enemies.add(e1, e2)
            self.all_sprites.add(e1, e2)

            for i, q_data in enumerate(questions):
                q = QuestionTrigger(250 + i * 250, 230, q_data)
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in q_data.get('en', {}) and q_data['en'].get('hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)
                    hint_y = random.randint(100, SCREEN_HEIGHT - 100)
                    hint = Hint(hint_x, hint_y)
                    hint.question_data = q_data
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

            door = Door(door_x, SCREEN_HEIGHT - 130)
            self.doors.add(door)
            self.all_sprites.add(door)

        elif self.current_level == 3:
            p1 = Platform(100, 400, 110, 20)
            p2 = Platform(300, 300, 110, 20)
            p3 = Platform(500, 200, 110, 20)
            p4 = Platform(700, 300, 110, 20)
            p5 = Platform(850, 400, 100, 20)
            self.platforms.add(p1, p2, p3, p4, p5)
            self.all_sprites.add(p1, p2, p3, p4, p5)

            b1 = BouncyPlatform(220, 450, 80, 15)
            b2 = BouncyPlatform(620, 450, 80, 15)
            self.bouncy_platforms.add(b1, b2)
            self.all_sprites.add(b1, b2)

            for x in [150, 350, 550, 750, 900]:
                c = Coin(x, 280)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            door_x = 920
            e1 = Enemy(250, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e2 = Enemy(500, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e3 = Enemy(350, 280, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            self.enemies.add(e1, e2, e3)
            self.all_sprites.add(e1, e2, e3)

            for i, q_data in enumerate(questions):
                q = QuestionTrigger(300 + i * 200, 150, q_data)
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in q_data.get('en', {}) and q_data['en'].get('hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)
                    hint_y = random.randint(100, SCREEN_HEIGHT - 100)
                    hint = Hint(hint_x, hint_y)
                    hint.question_data = q_data
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

            door = Door(door_x, SCREEN_HEIGHT - 130)
            self.doors.add(door)
            self.all_sprites.add(door)

        elif self.current_level == 4:
            p1 = Platform(120, 380, 100, 20)
            p2 = Platform(280, 280, 100, 20)
            p3 = Platform(450, 200, 90, 20)
            p4 = Platform(600, 280, 100, 20)
            p5 = Platform(750, 380, 100, 20)
            p6 = Platform(350, 120, 80, 20)
            self.platforms.add(p1, p2, p3, p4, p5, p6)
            self.all_sprites.add(p1, p2, p3, p4, p5, p6)

            b1 = BouncyPlatform(200, 450, 70, 15)
            b2 = BouncyPlatform(520, 450, 70, 15)
            b3 = BouncyPlatform(680, 450, 70, 15)
            self.bouncy_platforms.add(b1, b2, b3)
            self.all_sprites.add(b1, b2, b3)

            for x in [170, 330, 500, 650, 800]:
                c = Coin(x, 250)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            door_x = 900
            e1 = Enemy(200, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e2 = Enemy(500, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e3 = Enemy(330, 260, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            self.enemies.add(e1, e2, e3)
            self.all_sprites.add(e1, e2, e3)

            for i, q_data in enumerate(questions):
                q = QuestionTrigger(280 + i * 180, 100, q_data)
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in q_data.get('en', {}) and q_data['en'].get('hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)
                    hint_y = random.randint(100, SCREEN_HEIGHT - 100)
                    hint = Hint(hint_x, hint_y)
                    hint.question_data = q_data
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

            door = Door(door_x, SCREEN_HEIGHT - 130)
            self.doors.add(door)
            self.all_sprites.add(door)

        else:  # Level 5
            p1 = Platform(80, 420, 90, 20)
            p2 = Platform(220, 340, 90, 20)
            p3 = Platform(360, 260, 80, 20)
            p4 = Platform(500, 180, 80, 20)
            p5 = Platform(640, 260, 80, 20)
            p6 = Platform(780, 340, 90, 20)
            p7 = Platform(900, 420, 90, 20)
            p8 = Platform(400, 100, 70, 20)
            self.platforms.add(p1, p2, p3, p4, p5, p6, p7, p8)
            self.all_sprites.add(p1, p2, p3, p4, p5, p6, p7, p8)

            b1 = BouncyPlatform(160, 470, 60, 15)
            b2 = BouncyPlatform(440, 390, 60, 15)
            b3 = BouncyPlatform(720, 390, 60, 15)
            self.bouncy_platforms.add(b1, b2, b3)
            self.all_sprites.add(b1, b2, b3)

            for x in [130, 270, 410, 550, 690, 830]:
                c = Coin(x, 200)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            door_x = 950
            e1 = Enemy(150, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e2 = Enemy(450, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e3 = Enemy(750, SCREEN_HEIGHT - 80, settings['enemy_speed'], patrol_start=0, patrol_end=door_x - 20)
            e4 = Enemy(270, 320, settings['enemy_speed'] * 0.5, patrol_start=0, patrol_end=door_x - 20)
            self.enemies.add(e1, e2, e3, e4)
            self.all_sprites.add(e1, e2, e3, e4)

            for i, q_data in enumerate(questions):
                q = QuestionTrigger(250 + i * 200, 80, q_data)
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in q_data.get('en', {}) and q_data['en'].get('hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)
                    hint_y = random.randint(100, SCREEN_HEIGHT - 100)
                    hint = Hint(hint_x, hint_y)
                    hint.question_data = q_data
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

            door = Door(door_x, SCREEN_HEIGHT - 130)
            self.doors.add(door)
            self.all_sprites.add(door)

    def create_level_vertical(self):
        """Hard Mode: Vertical scrolling"""
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.bouncy_platforms = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()
        self.question_triggers = pygame.sprite.Group()
        self.hints_group = pygame.sprite.Group()

        settings = DIFFICULTY_SETTINGS['hard']
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, settings, self.player_image_right,
                             self.player_image_left)
        self.all_sprites.add(self.player)

        floor = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30, 100, 30, GREEN)
        self.platforms.add(floor)
        self.all_sprites.add(floor)

        current_y = SCREEN_HEIGHT - 120
        # Level-based target heights: Level 1=300m, 2=400m, 3=500m, 4=600m, 5=700m
        target_height_meters = 200 + (self.current_level * 100)
        target_height = -target_height_meters * 10

        min_platform_width = 180 - (self.current_level * 15)
        max_platform_width = 240 - (self.current_level * 20)
        min_gap = 75 + (self.current_level * 8)
        max_gap = 110 + (self.current_level * 10)
        bouncy_chance = 0.15 - (self.current_level * 0.02)

        questions = self.get_level_questions('hard', self.current_level)
        question_counter = 0

        while current_y > target_height:
            w = random.randint(max(80, min_platform_width), max_platform_width)
            x = random.randint(50, SCREEN_WIDTH - w - 50)

            p = Platform(x, current_y, w, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

            if random.random() < bouncy_chance:
                b = BouncyPlatform(x + 10, current_y - 12, 60, 12)
                self.bouncy_platforms.add(b)
                self.all_sprites.add(b)

            if random.random() < 0.18:
                c = Coin(x + w // 2, current_y - 35)
                self.coins_group.add(c)
                self.all_sprites.add(c)

            elif random.random() < 0.1 and question_counter < len(questions):
                q = QuestionTrigger(x + w // 2, current_y - 45, questions[question_counter])
                self.question_triggers.add(q)
                self.all_sprites.add(q)

                if 'hint' in questions[question_counter].get('en', {}) and questions[question_counter]['en'].get(
                        'hint'):
                    hint_x = random.randint(50, SCREEN_WIDTH - 50)

                    low_y = current_y - 140
                    high_y = current_y - 60
                    if high_y < low_y:
                        high_y = low_y

                    hint_y = random.randint(low_y, high_y)

                    hint = Hint(hint_x, hint_y)
                    hint.question_data = questions[question_counter]
                    self.hints_group.add(hint)
                    self.all_sprites.add(hint)

                question_counter += 1

            current_y -= random.randint(min_gap, max_gap)

        self.finish_door = Platform(SCREEN_WIDTH // 2 - 50, target_height, 100, 40, BROWN)
        self.all_sprites.add(self.finish_door)

    def find_nearest_platform_below(self, player_y):
        nearest_platform = None
        min_distance = float('inf')

        # Target: find platform closest to screen bottom (most accessible)
        # This ensures player respawns in a visible/accessible area
        target_y = SCREEN_HEIGHT - 50

        # Check all platforms - find the one closest to screen bottom
        for platform in self.platforms:
            platform_y = platform.rect.top
            if platform_y >= target_y - 200:  # Consider platforms near screen bottom
                distance = abs(platform_y - target_y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_platform = platform

        # If no suitable platform found, use the floor platform
        if nearest_platform is None:
            for platform in self.platforms:
                if platform.rect.y >= SCREEN_HEIGHT - 50:  # Floor platform
                    nearest_platform = platform
                    break

        return nearest_platform

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.lives = DIFFICULTY_SETTINGS[difficulty]['lives']
        self.coins = 0
        self.total_coins = 0
        self.current_level = 1
        self.distance = 0
        self.altitude = 0
        self.total_time_spent = 0
        self.shield_active = False
        self.bg_scroll = 0
        self.camera_y = 0
        # Reset hard mode fall counter
        self.hard_mode_fall_count = 0
        self.show_fall_warning = False
        self.fall_warning_timer = 0

        if DIFFICULTY_SETTINGS[difficulty]['auto_run']:
            self.create_level_easy()
        elif DIFFICULTY_SETTINGS[difficulty]['is_vertical']:
            self.create_level_vertical()
        else:
            self.time_left = DIFFICULTY_SETTINGS[difficulty]['time_limit_base']
            self.create_level_platformer()
            self.start_time = pygame.time.get_ticks()

        # Resume background music when leaving Instructions screen
        self.sound_manager.resume_music_if_was_playing()

        self.state = PLAYING

    def _reset_used_questions_for_run_end(self):
        if self.difficulty is not None:
            self.used_question_indices[self.difficulty] = set()

    def show_question(self, question_data):
        self.current_question = question_data[self.language]
        self.current_question_data = question_data
        self.state = QUESTION
        self.show_result = False
        self.result_timer = 0

    def show_hint(self, question_data):
        if self.state == QUESTION:
            return
        self.current_question_data = question_data
        if self.language == 'mk' and 'mk' in question_data:
            hint_text = question_data['mk'].get('hint', 'Нема достапен совет.')
        elif 'en' in question_data:
            hint_text = question_data['en'].get('hint', 'No hint available.')
        else:
            hint_text = 'No hint available.' if self.language == 'en' else 'Нема достапен совет.'
        self.current_hint_text = hint_text
        self.state = HINT
        self.hint_popup_timer = pygame.time.get_ticks()

    def answer_question(self, option_index):
        correct = option_index == self.current_question['correct']
        t = TRANSLATIONS[self.language]

        stats["questions"]["total"] += 1

        if correct:
            self.coins += 10
            if self.difficulty in stats:
                stats[self.difficulty]["coins"] += 10
            stats["questions"]["correct"] += 1
            self.sound_manager.play_coin()
            self.show_result = True
            self.result_correct = True

            # Create confetti particles
            self.confetti_particles = []
            center_x = SCREEN_WIDTH // 2
            center_y = SCREEN_HEIGHT // 2
            for _ in range(250):
                self.confetti_particles.append(Particle(
                    center_x + random.randint(-100, 100),
                    center_y + random.randint(-100, 100)
                ))

            self.feedback_popup_text = t['correct']
            self.feedback_popup_timer = 0.0
            self.feedback_popup_correct = True
        else:
            stats["questions"]["incorrect"] += 1
            if self.shield_active:
                self.shield_active = False
            else:
                self.lives -= 1
            self.show_result = True
            self.result_correct = False

            # Trigger camera shake
            self.shake_timer = 0.0
            self.shake_intensity = 15.0  # Initial shake intensity

            self.feedback_popup_text = t['wrong']
            self.feedback_popup_timer = 0.0
            self.feedback_popup_correct = False

        self.result_timer = pygame.time.get_ticks()

    def handle_menu_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.sound_manager.play_click()
            if event.key == pygame.K_1:
                self.pending_difficulty = 'easy'
                self.sound_manager.stop_music()
                self.state = INSTRUCTIONS
            elif event.key == pygame.K_2:
                self.pending_difficulty = 'normal'
                self.sound_manager.stop_music()
                self.state = INSTRUCTIONS
            elif event.key == pygame.K_3:
                self.pending_difficulty = 'hard'
                self.sound_manager.stop_music()
                self.state = INSTRUCTIONS
            elif event.key == pygame.K_l:
                self.language = 'mk' if self.language == 'en' else 'en'
                self.load_images()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.sound_manager.play_click()
            if self.profile_button and self.profile_button.check_click(event.pos):
                self.state = PROFILE

    def handle_playing_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.sound_manager.play_click()
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                self.player.jump()
            elif event.key == pygame.K_s:
                self.state = SHOP
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.sound_manager.play_click()

    def handle_question_input(self, event):
        if event.type == pygame.KEYDOWN and not self.show_result:
            self.sound_manager.play_click()
            num_options = len(self.current_question['options'])
            if event.key == pygame.K_1 and num_options >= 1:
                self.answer_question(0)
            elif event.key == pygame.K_2 and num_options >= 2:
                self.answer_question(1)
            elif event.key == pygame.K_3 and num_options >= 3:
                self.answer_question(2)
            elif event.key == pygame.K_4 and num_options >= 4:
                self.answer_question(3)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.sound_manager.play_click()

    def handle_hint_input(self, event):
        # Hint popup auto-closes after 7 seconds, no manual input needed
        pass

    def handle_instructions_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.sound_manager.play_click()
            # Check if sound button was clicked
            if hasattr(self, 'instructions_sound_button') and self.instructions_sound_button:
                if self.instructions_sound_button.check_click(event.pos):
                    if self.pending_difficulty:
                        self.sound_manager.play_instruction_audio(self.pending_difficulty)
                    return
            if hasattr(self, 'instructions_play_button') and self.instructions_play_button:
                if self.instructions_play_button.check_click(event.pos):
                    # Stop any playing instruction audio before starting gameplay
                    self.sound_manager.stop_instruction_audio()
                    if self.pending_difficulty:
                        self.start_game(self.pending_difficulty)

    def handle_shop_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.sound_manager.play_click()
            if event.key == pygame.K_b:
                self.state = PLAYING
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.sound_manager.play_click()
            mouse_pos = event.pos
            item_price = 30

            life_item_rect = pygame.Rect(SCREEN_WIDTH // 4 - 100, SCREEN_HEIGHT // 2 - 100, 200, 250)
            time_item_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - 100, SCREEN_HEIGHT // 2 - 100, 200, 250)

            if life_item_rect.collidepoint(mouse_pos):
                # Life item clicked
                if self.coins >= item_price:
                    self.coins -= item_price
                    self.lives += 1
                    t = TRANSLATIONS[self.language]
                    self.shop_message = t['success']
                    self.shop_message_timer = pygame.time.get_ticks()
                else:
                    t = TRANSLATIONS[self.language]
                    self.shop_message = t['not_enough']
                    self.shop_message_timer = pygame.time.get_ticks()
            elif time_item_rect.collidepoint(mouse_pos):
                # Time item clicked
                if self.coins >= item_price:
                    self.coins -= item_price
                    if hasattr(self, 'time_left') and self.time_left is not None:
                        self.time_left += 5
                        if hasattr(self, 'start_time'):
                            self.start_time += 5000
                    t = TRANSLATIONS[self.language]
                    self.shop_message = t['success']
                    self.shop_message_timer = pygame.time.get_ticks()
                else:
                    t = TRANSLATIONS[self.language]
                    self.shop_message = t['not_enough']
                    self.shop_message_timer = pygame.time.get_ticks()

    def update_playing(self):
        settings = DIFFICULTY_SETTINGS[self.difficulty]

        if settings['auto_run']:
            self.player.update()
            self.obstacles.update()
            self.coins_group.update()
            self.question_triggers.update()
            self.hints_group.update()
            self.finish_line_group.update()

            base_speed = settings['scroll_speed_base']
            scroll_speed = base_speed + (self.current_level - 1) * 1.5
            self.distance += scroll_speed

            self.bg_scroll += self.bg_speed
            if self.bg_scroll >= self.easy_bg_width:
                self.bg_scroll = 0

            collected_coins = pygame.sprite.spritecollide(self.player, self.coins_group, True)
            coin_count = len(collected_coins)
            if coin_count > 0:
                self.sound_manager.play_coin()
                if self.difficulty in stats:
                    stats[self.difficulty]["coins"] += coin_count
            self.coins += coin_count

            collected_hints = pygame.sprite.spritecollide(self.player, self.hints_group, True)
            for hint in collected_hints:
                if hasattr(hint, 'question_data') and hint.question_data:
                    stats["total_xp"] += 10
                    self.show_hint(hint.question_data)
                break

            if pygame.sprite.spritecollide(self.player, self.obstacles, False):
                self.sound_manager.play_hit_obstacle()
                pygame.time.delay(125)

                if self.shield_active:
                    self.shield_active = False
                    for obstacle in self.obstacles:
                        if abs(obstacle.rect.x - self.player.rect.x) < 100:
                            obstacle.kill()
                else:
                    self.lives -= 1
                    for obstacle in self.obstacles:
                        if abs(obstacle.rect.x - self.player.rect.x) < 100:
                            obstacle.kill()

            triggered = pygame.sprite.spritecollide(self.player, self.question_triggers, False)
            for trigger in triggered:
                if not trigger.triggered:
                    trigger.triggered = True
                    self.show_question(trigger.question_data)
                    trigger.kill()
                    break

            if pygame.sprite.spritecollide(self.player, self.finish_line_group, False):
                if self.current_level >= 5:
                    self.total_coins = self.coins
                    self.sound_manager.stop_music()
                    self.sound_manager.play_victory()
                    if self.difficulty in stats:
                        stats[self.difficulty]["completions"] += 1
                    self._reset_used_questions_for_run_end()
                    self.state = MODE_VICTORY
                else:
                    self.sound_manager.play_victory()
                    self.state = LEVEL_COMPLETE

        elif settings['is_vertical']:
            # Handle fall warning display and pause
            if self.show_fall_warning:
                if pygame.time.get_ticks() - self.fall_warning_timer > 1000:
                    self.show_fall_warning = False
                # Pause gameplay while warning is shown
            else:
                # Normal gameplay
                self.player.update(self.platforms, self.bouncy_platforms)

                # Camera follows player vertically - track scroll amount for background
                if self.player.rect.top <= SCREEN_HEIGHT // 2 and self.player.vel_y < 0:
                    scroll = -self.player.vel_y
                    self.player.rect.y += scroll
                    self.altitude += scroll / 10
                    self.camera_y += scroll

                    for sprite in self.all_sprites:
                        if sprite != self.player:
                            sprite.rect.y += scroll

            # Hard mode fall & respawn logic
            if self.player.rect.top > SCREEN_HEIGHT:
                if self.difficulty == 'hard':
                    self.hard_mode_fall_count += 1

                    if self.hard_mode_fall_count < 3:
                        self.show_fall_warning = True
                        self.fall_warning_timer = pygame.time.get_ticks()
                        self.lives -= 1
                        if self.lives < 0:
                            self.lives = 0

                        # Find nearest platform below for respawn
                        nearest_platform = self.find_nearest_platform_below(self.player.rect.y)
                        if nearest_platform:
                            # Respawn slightly above the platform
                            self.player.rect.y = nearest_platform.rect.top - self.player.rect.height - 10
                            self.player.rect.x = nearest_platform.rect.centerx - self.player.rect.width // 2
                            # Keep player on screen
                            if self.player.rect.left < 0:
                                self.player.rect.left = 0
                            if self.player.rect.right > SCREEN_WIDTH:
                                self.player.rect.right = SCREEN_WIDTH
                        else:
                            # Fallback: respawn at starting position
                            self.player.rect.y = SCREEN_HEIGHT - 100
                            self.player.rect.x = SCREEN_WIDTH // 2

                        self.player.vel_y = 0
                    else:
                        # Third fall: game over
                        self.lives = 0
                else:
                    self.lives = 0

            if self.altitude > self.high_score_hard:
                self.high_score_hard = int(self.altitude)

            collected_coins = pygame.sprite.spritecollide(self.player, self.coins_group, True)
            coin_count = len(collected_coins)
            if coin_count > 0:
                self.sound_manager.play_coin()
                if self.difficulty in stats:
                    stats[self.difficulty]["coins"] += coin_count
            self.coins += coin_count

            collected_hints = pygame.sprite.spritecollide(self.player, self.hints_group, True)
            for hint in collected_hints:
                if hasattr(hint, 'question_data') and hint.question_data:
                    stats["total_xp"] += 10
                    self.show_hint(hint.question_data)
                break

            triggered_questions = pygame.sprite.spritecollide(self.player, self.question_triggers, False)
            for trigger in triggered_questions:
                if not trigger.answered:
                    trigger.answered = True
                    self.show_question(trigger.question_data)
                    trigger.kill()
                    break

            if self.player.rect.colliderect(self.finish_door.rect):
                if self.current_level >= 5:
                    self.total_coins = self.coins
                    self.sound_manager.stop_music()
                    self.sound_manager.play_victory()
                    if self.difficulty in stats:
                        stats[self.difficulty]["completions"] += 1
                    self._reset_used_questions_for_run_end()
                    self.state = MODE_VICTORY
                else:
                    self.sound_manager.play_victory()
                    self.state = LEVEL_COMPLETE

        else:
            settings_copy = DIFFICULTY_SETTINGS[self.difficulty]
            time_limit = settings_copy['time_limit_base'] - (self.current_level - 1) * 10
            elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
            self.time_left = max(0, time_limit - elapsed)
            if self.time_left <= 0:
                self.sound_manager.stop_music()
                self.sound_manager.play_game_over()
                self._reset_used_questions_for_run_end()
                self.state = GAME_OVER

            self.player.update(self.platforms, self.bouncy_platforms)
            self.enemies.update()

            collected_coins = pygame.sprite.spritecollide(self.player, self.coins_group, True)
            coin_count = len(collected_coins)
            if coin_count > 0:
                self.sound_manager.play_coin()
                if self.difficulty in stats:
                    stats[self.difficulty]["coins"] += coin_count
            self.coins += coin_count

            collected_hints = pygame.sprite.spritecollide(self.player, self.hints_group, True)
            for hint in collected_hints:
                if hasattr(hint, 'question_data') and hint.question_data:
                    stats["total_xp"] += 10
                    self.show_hint(hint.question_data)
                break

            if pygame.sprite.spritecollide(self.player, self.enemies, False):
                self.sound_manager.play_hit_villain()
                pygame.time.delay(125)

                if self.shield_active:
                    self.shield_active = False
                else:
                    self.lives -= 1
                    self.player.rect.x = 50
                    self.player.rect.y = SCREEN_HEIGHT - 100
                    self.player.vel_y = 0

            triggered_questions = pygame.sprite.spritecollide(self.player, self.question_triggers, False)
            for trigger in triggered_questions:
                if not trigger.answered:
                    trigger.answered = True
                    self.show_question(trigger.question_data)
                    trigger.kill()
                    break

            if pygame.sprite.spritecollide(self.player, self.doors, False):
                if self.current_level >= 5:
                    self.total_coins = self.coins
                    if not DIFFICULTY_SETTINGS[self.difficulty]['auto_run'] and not \
                            DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
                        settings_copy = DIFFICULTY_SETTINGS[self.difficulty]
                        base_time = settings_copy['time_limit_base']
                        self.total_time_spent += (base_time - (self.current_level - 1) * 10 - self.time_left)
                    self.sound_manager.stop_music()
                    self.sound_manager.play_victory()
                    if self.difficulty in stats:
                        stats[self.difficulty]["completions"] += 1
                    self._reset_used_questions_for_run_end()
                    self.state = MODE_VICTORY
                else:
                    self.sound_manager.play_victory()
                    self.state = LEVEL_COMPLETE

        if self.lives <= 0:
            self.sound_manager.stop_music()
            self.sound_manager.play_game_over()
            self.sound_manager.play_background_music()
            self._reset_used_questions_for_run_end()
            self.state = GAME_OVER

    def draw_menu(self):
        self.screen.blit(self.menu_bg, (0, 0))

        t = TRANSLATIONS[self.language]

        self.title_original = pygame.image.load('assets/images/title.png').convert_alpha()
        self.title_image = pygame.transform.smoothscale(self.title_original, (300, 150))
        self.screen.blit(self.title_image, (SCREEN_WIDTH // 2 - 150, 50))

        # Profile button
        if self.profile_button_img:
            profile_button = ImageButton(
                SCREEN_WIDTH - self.profile_button_img.get_width() - 20,
                20,
                self.profile_button_img,
                self.profile_button_hover
            )
            profile_button.check_hover(pygame.mouse.get_pos())
            profile_button.draw(self.screen)
            self.profile_button = profile_button
        else:
            self.profile_button = None

        easy = self.font.render(f"1. {t['easy']}", True, (27, 51, 135))
        normal = self.font.render(f"2. {t['normal']}", True, (27, 51, 135))
        hard = self.font.render(f"3. {t['hard']}", True, (27, 51, 135))
        lang = self.small_font.render(t['language'], True, (27, 51, 135))

        self.screen.blit(easy, (SCREEN_WIDTH // 2 - easy.get_width() // 2, 225))
        self.screen.blit(normal, (SCREEN_WIDTH // 2 - normal.get_width() // 2, 295))
        self.screen.blit(hard, (SCREEN_WIDTH // 2 - hard.get_width() // 2, 365))
        self.screen.blit(lang, (SCREEN_WIDTH // 2 - lang.get_width() // 2, 475))

    def draw_playing(self):
        if DIFFICULTY_SETTINGS[self.difficulty]['auto_run']:
            # Easy mode
            if self.easy_bg:
                self.screen.blit(self.easy_bg, (-self.bg_scroll, 0))
                self.screen.blit(self.easy_bg, (self.easy_bg_width - self.bg_scroll, 0))
            else:
                self.screen.fill(SKY_BLUE)
        elif DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
            # Hard mode
            if self.hard_bg:
                # As camera_y increases (player goes up), background scrolls down
                bg_y = self.camera_y % self.hard_bg_height
                start_y = bg_y - self.hard_bg_height
                while start_y < SCREEN_HEIGHT:
                    self.screen.blit(self.hard_bg, (0, start_y))
                    start_y += self.hard_bg_height
            else:
                self.screen.fill(SKY_BLUE)
        else:
            # Normal mode
            if self.normal_bg:
                if self.normal_bg_width != SCREEN_WIDTH:
                    scaled_bg = pygame.transform.scale(self.normal_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    self.screen.blit(scaled_bg, (0, 0))
                else:
                    self.screen.blit(self.normal_bg, (0, 0))
            else:
                self.screen.fill(SKY_BLUE)

        self.all_sprites.draw(self.screen)

        t = TRANSLATIONS[self.language]

        level_text = self.small_font.render(f"{t['level']} {self.current_level}/5", True, (27, 51, 135))
        self.screen.blit(level_text, (SCREEN_WIDTH - 150, 10))

        lives_text = self.small_font.render(f"{t['lives']}: ", True, RED)

        if self.heart_image:
            heart_x = 10
            for i in range(self.lives):
                self.screen.blit(self.heart_image, (heart_x + (i * 25), 12))
        else:
            lives_num = self.small_font.render(str(self.lives), True, RED)
            self.screen.blit(lives_num, (10 + lives_text.get_width(), 10))

        coins_text = self.small_font.render(f"{t['coins']}: {self.coins}", True, (27, 51, 135))
        self.screen.blit(coins_text, (10, 40))

        if DIFFICULTY_SETTINGS[self.difficulty]['auto_run']:
            distance_text = self.small_font.render(f"{t['distance']}: {int(self.distance // 10)}m", True, (27, 51, 135))
            self.screen.blit(distance_text, (10, 70))

            # hint_text = self.small_font.render(t['jump'], True, BLACK)
            # self.screen.blit(hint_text, (SCREEN_WIDTH // 2 - hint_text.get_width() // 2, 20))

        elif DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
            altitude_text = self.small_font.render(f"{t['altitude']}: {int(self.altitude)}m", True, (27, 51, 135))
            self.screen.blit(altitude_text, (10, 70))

            best_text = self.small_font.render(f"{t['best']}: {self.high_score_hard}m", True, (27, 51, 135))
            self.screen.blit(best_text, (10, 100))

            # Display fall warning message if active
            if self.show_fall_warning:
                warning_text = render_text_with_outline(
                    self.game_font,
                    t['fall_warning'],
                    WHITE,
                    BLACK,
                    2
                )
                self.screen.blit(
                    warning_text,
                    (SCREEN_WIDTH // 2 - warning_text.get_width() // 2,
                     SCREEN_HEIGHT // 2 - warning_text.get_height() // 2)
                )
        else:
            time_text = self.small_font.render(f"{t['time']}: {int(self.time_left)}s", True, (27, 51, 135))
            self.screen.blit(time_text, (10, 70))

        shop_text = self.small_font.render(t['shop_hint'], True, (27, 51, 135))
        self.screen.blit(shop_text, (SCREEN_WIDTH // 2 - shop_text.get_width() // 2, 20))

    def draw_question(self):
        # Apply camera shake offset
        shake_x = int(self.shake_offset_x)
        shake_y = int(self.shake_offset_y)

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (shake_x, shake_y))

        t = TRANSLATIONS[self.language]

        box_rect = pygame.Rect(150 + shake_x, 150 + shake_y, 700, 300)
        pygame.draw.rect(self.screen, BLUE_BOX, box_rect, border_radius=15)
        pygame.draw.rect(self.screen, WHITE, box_rect, 4, border_radius=15)

        question_text = self.current_question['question']
        max_width = 680
        padding = 15

        test_lines = wrap_text(self.small_font, question_text, max_width, padding)
        total_height = sum(line.get_height() for line in test_lines) + (len(test_lines) - 1) * 5  # 5px spacing

        question_font = self.small_font
        if total_height > 120:  # Max height for question area
            test_lines = wrap_text(self.game_font_tiny, question_text, max_width, padding)
            total_height = sum(line.get_height() for line in test_lines) + (len(test_lines) - 1) * 5
            if total_height <= 120:
                question_font = self.game_font_tiny
            else:
                question_font = self.game_font_tiny

        wrapped_lines = wrap_text(question_font, question_text, max_width, padding)
        question_start_y = 160 + shake_y
        line_spacing = 5

        total_text_height = sum(line.get_height() for line in wrapped_lines) + (len(wrapped_lines) - 1) * line_spacing
        question_y = question_start_y + (120 - total_text_height) // 2

        for i, line_surface in enumerate(wrapped_lines):
            y_pos = question_y + i * (line_surface.get_height() + line_spacing)
            x_pos = SCREEN_WIDTH // 2 - line_surface.get_width() // 2 + shake_x
            self.screen.blit(line_surface, (x_pos, y_pos))

        for i, option in enumerate(self.current_question['options']):
            opt_text = self.small_font.render(f"{i + 1}. {option}", True, WHITE)
            self.screen.blit(opt_text, (200 + shake_x, 270 + (i * 50) + shake_y))

        for particle in self.confetti_particles[:]:
            particle.draw(self.screen)

        if self.feedback_popup_text and self.feedback_popup_timer < 1.5:
            progress = min(self.feedback_popup_timer / 1.5, 1.0)

            if progress < 0.3:
                scale = 0.5 + (progress / 0.3) * 0.5
            else:
                scale = 1.0

            alpha = 255
            if progress > 0.8:
                alpha = int(255 * (1.0 - (progress - 0.8) / 0.2))

            feedback_font = self.game_font
            if self.feedback_popup_correct:
                color, bg = WHITE, GREEN
            else:
                color, bg = WHITE, RED
            result_text = feedback_font.render(self.feedback_popup_text, True, color, bg)

            if scale != 1.0:
                scaled_width = int(result_text.get_width() * scale)
                scaled_height = int(result_text.get_height() * scale)
                result_text = pygame.transform.scale(result_text, (scaled_width, scaled_height))

            x_pos = SCREEN_WIDTH // 2 - result_text.get_width() // 2 + shake_x
            y_pos = SCREEN_HEIGHT // 2 - result_text.get_height() // 2 + shake_y

            if alpha < 255:
                result_text.set_alpha(alpha)

            self.screen.blit(result_text, (x_pos, y_pos))

        if self.show_result and not self.feedback_popup_text:
            if pygame.time.get_ticks() - self.result_timer < 1500:
                if self.result_correct:
                    result_text = self.font.render(t['correct'], True, GREEN)
                else:
                    result_text = self.font.render(t['wrong'], True, RED)
                self.screen.blit(result_text,
                                 (SCREEN_WIDTH // 2 - result_text.get_width() // 2 + shake_x, 400 + shake_y))
            else:
                self.state = PLAYING

    def draw_hint(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        t = TRANSLATIONS[self.language]

        box_rect = pygame.Rect(150, 150, 700, 300)
        pygame.draw.rect(self.screen, BLUE_BOX, box_rect, border_radius=15)
        pygame.draw.rect(self.screen, WHITE, box_rect, 4, border_radius=15)

        hint_text = self.current_hint_text or 'No hint available.'
        max_width = 680
        padding = 15

        test_lines = wrap_text(self.small_font, hint_text, max_width, padding)
        total_height = sum(line.get_height() for line in test_lines) + (len(test_lines) - 1) * 5

        hint_font = self.small_font
        if total_height > 200:
            test_lines = wrap_text(self.game_font_tiny, hint_text, max_width, padding)
            total_height = sum(line.get_height() for line in test_lines) + (len(test_lines) - 1) * 5
            if total_height <= 200:
                hint_font = self.game_font_tiny
            else:
                hint_font = self.game_font_tiny

        wrapped_lines = wrap_text(hint_font, hint_text, max_width, padding)
        hint_start_y = 200
        line_spacing = 5

        total_text_height = sum(line.get_height() for line in wrapped_lines) + (len(wrapped_lines) - 1) * line_spacing
        hint_y = hint_start_y + (200 - total_text_height) // 2

        for i, line_surface in enumerate(wrapped_lines):
            y_pos = hint_y + i * (line_surface.get_height() + line_spacing)
            x_pos = SCREEN_WIDTH // 2 - line_surface.get_width() // 2
            self.screen.blit(line_surface, (x_pos, y_pos))

    def draw_instructions(self):
        if self.menu_bg:
            TMP_image = load_image('assets/images/instructions.png', (SCREEN_WIDTH, SCREEN_HEIGHT), RED)
            self.screen.blit(TMP_image, (0, 0))
        else:
            self.screen.fill(BLACK)

        t = TRANSLATIONS[self.language]

        title_rect = pygame.Rect(0, 0, 1023, 161)
        draw_text_centered(self.screen, t['instructions_title'], title_rect, self.game_font, WHITE)

        if self.pending_difficulty == 'easy':
            controls_text = t['easy_controls']
            objective_text = t['easy_objective']
        elif self.pending_difficulty == 'normal':
            controls_text = t['normal_controls']
            objective_text = t['normal_objective']
        elif self.pending_difficulty == 'hard':
            controls_text = t['hard_controls']
            objective_text = t['hard_objective']
        else:
            controls_text = ""
            objective_text = ""

        y_offset = 150
        line_height = 30

        for line in controls_text.split('\n'):
            if line.strip():
                line_surface = render_text_with_outline(self.game_font_tiny, line.strip(), (27, 51, 135), BLACK, 0)
                self.screen.blit(line_surface, (SCREEN_WIDTH // 2 - line_surface.get_width() // 2, y_offset))
                y_offset += line_height

        y_offset += 20

        for line in objective_text.split('\n'):
            if line.strip():
                line_surface = render_text_with_outline(self.game_font_tiny, line.strip(), (27, 51, 135), BLACK, 0)
                self.screen.blit(line_surface, (SCREEN_WIDTH // 2 - line_surface.get_width() // 2, y_offset))
                y_offset += line_height

        if self.sound_button_img:
            sound_button = ImageButton(
                SCREEN_WIDTH - 80,
                20,
                self.sound_button_img,
                self.sound_button_hover
            )
            sound_button.check_hover(pygame.mouse.get_pos())
            sound_button.draw(self.screen)
            self.instructions_sound_button = sound_button
        else:
            self.instructions_sound_button = None

        if self.play_button_img:
            play_button = ImageButton(
                SCREEN_WIDTH // 2 - 100,
                SCREEN_HEIGHT - 150,
                self.play_button_img,
                self.play_button_hover
            )
            play_button.check_hover(pygame.mouse.get_pos())
            play_button.draw(self.screen, TRANSLATIONS[self.language]['play_button'], self.game_font_small, WHITE)
            self.instructions_play_button = play_button
        else:
            self.instructions_play_button = None

    def draw_profile(self):
        TMP_image = load_image('assets/images/profile.png', (SCREEN_WIDTH, SCREEN_HEIGHT), RED)
        self.screen.blit(TMP_image, (0, 0))

        if self.language == 'mk':
            title_text = "ПРОФИЛ"
            easy_label = "Лесен режим"
            normal_label = "Нормален режим"
            hard_label = "Тежок режим"
            coins_label = "Пари"
            completions_label = "Завршувања"
            questions_answered_label = "Одговорени прашања"
            correct_label = "Точни"
            incorrect_label = "Неточни"
        else:
            title_text = "PROFILE"
            easy_label = "Easy Mode"
            normal_label = "Normal Mode"
            hard_label = "Hard Mode"
            coins_label = "Coins"
            completions_label = "Completions"
            questions_answered_label = "Questions Answered"
            correct_label = "Correct"
            incorrect_label = "Incorrect"

        title_surface = self.profile_font_title.render(title_text, True, WHITE)
        title_rect = title_surface.get_rect(center=(500, 68))
        self.screen.blit(title_surface, title_rect)

        easy_title_surf = self.profile_font_text.render(easy_label, True, (27, 51, 135))
        easy_title_rect = easy_title_surf.get_rect(center=(230, 200))
        self.screen.blit(easy_title_surf, easy_title_rect)

        normal_title_surf = self.profile_font_text.render(normal_label, True, (27, 51, 135))
        normal_title_rect = normal_title_surf.get_rect(center=(500, 200))
        self.screen.blit(normal_title_surf, normal_title_rect)

        hard_title_surf = self.profile_font_text.render(hard_label, True, (27, 51, 135))
        hard_title_rect = hard_title_surf.get_rect(center=(770, 200))
        self.screen.blit(hard_title_surf, hard_title_rect)

        easy_stats = stats["easy"]
        normal_stats = stats["normal"]
        hard_stats = stats["hard"]
        question_stats = stats["questions"]

        easy_coins_surf = self.profile_font_text.render(f"{coins_label}: {easy_stats['coins']}", True, (27, 51, 135))
        easy_coins_rect = easy_coins_surf.get_rect(topleft=(105, 223))
        self.screen.blit(easy_coins_surf, easy_coins_rect)

        normal_coins_surf = self.profile_font_text.render(f"{coins_label}: {normal_stats['coins']}", True,
                                                          (27, 51, 135))
        normal_coins_rect = normal_coins_surf.get_rect(topleft=(395, 223))
        self.screen.blit(normal_coins_surf, normal_coins_rect)

        hard_coins_surf = self.profile_font_text.render(f"{coins_label}: {hard_stats['coins']}", True, (27, 51, 135))
        hard_coins_rect = hard_coins_surf.get_rect(topleft=(650, 223))
        self.screen.blit(hard_coins_surf, hard_coins_rect)

        easy_comp_surf = self.profile_font_text.render(
            f"{completions_label}: {easy_stats['completions']}", True, (27, 51, 135)
        )
        easy_comp_rect = easy_comp_surf.get_rect(topleft=(105, 255))
        self.screen.blit(easy_comp_surf, easy_comp_rect)

        normal_comp_surf = self.profile_font_text.render(
            f"{completions_label}: {normal_stats['completions']}", True, (27, 51, 135)
        )
        normal_comp_rect = normal_comp_surf.get_rect(topleft=(395, 255))
        self.screen.blit(normal_comp_surf, normal_comp_rect)

        hard_comp_surf = self.profile_font_text.render(
            f"{completions_label}: {hard_stats['completions']}", True, (27, 51, 135)
        )
        hard_comp_rect = hard_comp_surf.get_rect(topleft=(650, 255))
        self.screen.blit(hard_comp_surf, hard_comp_rect)

        q_total_surf = self.profile_font_text.render(
            f"{questions_answered_label}: {question_stats['total']}", True, (27, 51, 135)
        )
        q_total_rect = q_total_surf.get_rect(topleft=(170, 345))
        self.screen.blit(q_total_surf, q_total_rect)

        q_correct_surf = self.profile_font_text.render(
            f"{correct_label}: {question_stats['correct']}", True, (27, 51, 135)
        )
        q_correct_rect = q_correct_surf.get_rect(topleft=(170, 385))
        self.screen.blit(q_correct_surf, q_correct_rect)

        q_incorrect_surf = self.profile_font_text.render(
            f"{incorrect_label}: {question_stats['incorrect']}", True, (27, 51, 135)
        )
        q_incorrect_rect = q_incorrect_surf.get_rect(topleft=(170, 425))
        self.screen.blit(q_incorrect_surf, q_incorrect_rect)

        total_xp = stats.get("total_xp", 0)

        if total_xp < 100:
            badge_name = "beginner"
        elif total_xp < 200:
            badge_name = "intermediate"
        else:
            badge_name = "advanced"

        badge_path = f'assets/images/{badge_name}_{self.language}.png'
        try:
            badge_image = load_image(badge_path, (150, 150), YELLOW)
            self.screen.blit(badge_image, (550, 330))
        except:
            pass

        if self.language == 'mk':
            xp_text = f"Вкупно XP: {total_xp}"
        else:
            xp_text = f"Total XP: {total_xp}"

        xp_surf = self.profile_font_text.render(xp_text, True, (27, 51, 135))
        xp_rect = xp_surf.get_rect(topleft=(720, 445))
        self.screen.blit(xp_surf, xp_rect)

        if self.back_button_img:
            back_button = ImageButton(
                30,
                20,
                self.back_button_img,
                self.back_button_hover
            )
            back_button.check_hover(pygame.mouse.get_pos())
            back_button.draw(self.screen)
            self.profile_back_button = back_button
        else:
            self.profile_back_button = None

    def draw_shop(self):
        if self.shop_bg:
            self.screen.blit(self.shop_bg, (0, 0))
        else:
            self.screen.fill(BLACK)

        t = TRANSLATIONS[self.language]

        title_rect = pygame.Rect(30, 0, 930, 150)
        draw_text_centered(self.screen, t['shop_title'], title_rect, self.game_font, WHITE)
        coins_text = render_text_with_outline(self.game_font_small, f"{t['coins']}: {self.coins}", YELLOW, BLACK, 2)
        self.screen.blit(coins_text, (SCREEN_WIDTH // 2 - coins_text.get_width() // 2, 145))

        item_y_center = SCREEN_HEIGHT // 2
        item_spacing = SCREEN_WIDTH // 2
        item_width = 200
        item_height = 250

        life_x = SCREEN_WIDTH // 4 - item_width // 2
        life_item_rect = pygame.Rect(life_x, item_y_center - item_height // 2, item_width, item_height)

        life_title = render_text_with_outline(self.game_font_small, t['life'], WHITE, BLACK, 2)
        self.screen.blit(life_title, (life_x + item_width // 2 - life_title.get_width() // 2, item_y_center - 120))

        if self.shop_heart_img:
            heart_x = life_x + item_width // 2 - self.shop_heart_img.get_width() // 2
            heart_y = item_y_center - self.shop_heart_img.get_height() // 2
            self.screen.blit(self.shop_heart_img, (heart_x, heart_y))

        life_price = render_text_with_outline(self.game_font_tiny, t['price'], YELLOW, BLACK, 2)
        self.screen.blit(life_price, (life_x + item_width // 2 - life_price.get_width() // 2, item_y_center + 60))

        time_x = 3 * SCREEN_WIDTH // 4 - item_width // 2
        time_item_rect = pygame.Rect(time_x, item_y_center - item_height // 2, item_width, item_height)

        time_title = render_text_with_outline(self.game_font_small, t['time_item'], WHITE, BLACK, 2)
        self.screen.blit(time_title, (time_x + item_width // 2 - time_title.get_width() // 2, item_y_center - 120))

        if self.shop_time_img:
            time_img_x = time_x + item_width // 2 - self.shop_time_img.get_width() // 2
            time_img_y = item_y_center - self.shop_time_img.get_height() // 2
            self.screen.blit(self.shop_time_img, (time_img_x, time_img_y))

        time_price = render_text_with_outline(self.game_font_tiny, t['price'], YELLOW, BLACK, 2)
        self.screen.blit(time_price, (time_x + item_width // 2 - time_price.get_width() // 2, item_y_center + 60))

        mouse_pos = pygame.mouse.get_pos()
        if life_item_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (255, 255, 255, 50), life_item_rect, 3)
        if time_item_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (255, 255, 255, 50), time_item_rect, 3)

        if self.shop_message:
            current_time = pygame.time.get_ticks()
            if current_time - self.shop_message_timer < 2000:
                is_success = self.shop_message == t['success']
                message_color = (27, 51, 135)  # if is_success else RED
                message_text = render_text_with_outline(self.game_font_small, self.shop_message, message_color, BLACK,
                                                        0)
                self.screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2))
            else:
                self.shop_message = None

        back_text = render_text_with_outline(self.game_font_tiny, t['back'], WHITE, BLACK, 2)
        self.screen.blit(back_text, (SCREEN_WIDTH // 2 - back_text.get_width() // 2, SCREEN_HEIGHT - 45))

    def draw_game_over(self):
        if self.game_over_bg:
            self.screen.blit(self.game_over_bg, (0, 0))
        else:
            self.screen.fill(BLACK)

        t = TRANSLATIONS[self.language]

        if self.menu_button_img:
            menu_button = ImageButton(
                SCREEN_WIDTH // 2 - 100,
                SCREEN_HEIGHT - 100,
                self.menu_button_img,
                self.menu_button_hover
            )
            menu_button.check_hover(pygame.mouse.get_pos())
            menu_button.draw(self.screen, TRANSLATIONS[self.language]['menu_button'], self.game_font_small, WHITE)
            self.game_over_menu_button = menu_button
        else:
            self.game_over_menu_button = None

    def draw_level_complete(self):
        if self.level_up_bg:
            self.screen.blit(self.level_up_bg, (0, 0))
        else:
            self.screen.fill(BLACK)

        t = TRANSLATIONS[self.language]

        stats_y = SCREEN_HEIGHT // 2 + 20

        coins_text = render_text_with_outline(self.game_font_small, f"{t['coins']}: {self.coins}", WHITE, BLACK, 2)
        self.screen.blit(coins_text, (SCREEN_WIDTH // 2 - coins_text.get_width() // 2, stats_y - 20))

        lives_text = render_text_with_outline(self.game_font_small, f"{t['lives']}: {self.lives}", WHITE, BLACK, 2)
        self.screen.blit(lives_text, (SCREEN_WIDTH // 2 - lives_text.get_width() // 2, stats_y + 20))

        level_text = render_text_with_outline(self.game_font_tiny, f"{t['level']} {self.current_level}/5", WHITE, BLACK,
                                              2)
        self.screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, stats_y + 80))

        button_y = SCREEN_HEIGHT - 100
        mouse_pos = pygame.mouse.get_pos()

        if self.next_button_img:
            next_button = ImageButton(
                SCREEN_WIDTH // 2 - 170,
                button_y,
                self.next_button_img,
                self.next_button_hover
            )
            next_button.check_hover(mouse_pos)
            next_button.draw(self.screen, TRANSLATIONS[self.language]['next_button'], self.game_font_small, WHITE)
            self.level_complete_next_button = next_button
        else:
            self.level_complete_next_button = None

        if self.menu_button_img:
            menu_button = ImageButton(
                SCREEN_WIDTH // 2 + 20,
                button_y,
                self.menu_button_img,
                self.menu_button_hover
            )
            menu_button.check_hover(mouse_pos)
            menu_button.draw(self.screen, TRANSLATIONS[self.language]['menu_button'], self.game_font_small, WHITE)
            self.level_complete_menu_button = menu_button
        else:
            self.level_complete_menu_button = None

    def draw_victory(self):
        self.draw_mode_victory()

    def draw_mode_victory(self):
        if self.victory_bg:
            self.screen.blit(self.victory_bg, (0, 0))
        else:
            self.screen.fill(BLACK)

        t = TRANSLATIONS[self.language]

        if self.menu_button_img:
            menu_button = ImageButton(
                SCREEN_WIDTH // 2 - 100,
                SCREEN_HEIGHT - 80,
                self.menu_button_img,
                self.menu_button_hover
            )
            menu_button.check_hover(pygame.mouse.get_pos())
            menu_button.draw(self.screen, TRANSLATIONS[self.language]['menu_button'], self.game_font_small, WHITE)
            self.mode_victory_menu_button = menu_button
        else:
            self.mode_victory_menu_button = None

    def update_question_feedback(self):
        dt = self.clock.get_time() / 1000.0

        for particle in self.confetti_particles[:]:
            particle.update(dt)
            if not particle.is_alive():
                self.confetti_particles.remove(particle)

        if self.shake_intensity > 0:
            self.shake_timer += dt
            if self.shake_timer < 0.3:
                self.shake_intensity = 15.0 * (1.0 - self.shake_timer / 0.3)
                self.shake_offset_x = random.uniform(-self.shake_intensity, self.shake_intensity)
                self.shake_offset_y = random.uniform(-self.shake_intensity, self.shake_intensity)
            else:
                self.shake_intensity = 0.0
                self.shake_offset_x = 0
                self.shake_offset_y = 0
                self.shake_timer = 0.0

        if self.feedback_popup_text:
            self.feedback_popup_timer += dt
            if self.feedback_popup_timer >= 1.5:
                self.feedback_popup_text = None
                self.feedback_popup_timer = 0.0
                if self.state == QUESTION:
                    self.state = PLAYING
                    self.confetti_particles = []

    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == MENU:
                    self.handle_menu_input(event)
                elif self.state == INSTRUCTIONS:
                    self.handle_instructions_input(event)
                elif self.state == PLAYING:
                    self.handle_playing_input(event)
                elif self.state == QUESTION:
                    self.handle_question_input(event)
                elif self.state == HINT:
                    self.handle_hint_input(event)
                elif self.state == SHOP:
                    self.handle_shop_input(event)
                elif self.state == PROFILE:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.sound_manager.play_click()
                        if self.profile_back_button and self.profile_back_button.check_click(event.pos):
                            self.state = MENU
                elif self.state == GAME_OVER:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.sound_manager.play_click()
                        if self.game_over_menu_button and self.game_over_menu_button.check_click(event.pos):
                            self.state = MENU
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.sound_manager.play_click()
                        self.state = MENU
                elif self.state == LEVEL_COMPLETE:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.sound_manager.play_click()
                        if self.level_complete_next_button and self.level_complete_next_button.check_click(event.pos):
                            self.current_level += 1
                            self.distance = 0
                            self.altitude = 0
                            self.bg_scroll = 0
                            self.camera_y = 0
                            if self.difficulty == 'hard':
                                self.hard_mode_fall_count = 0

                            if DIFFICULTY_SETTINGS[self.difficulty]['auto_run']:
                                self.create_level_easy()
                            elif DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
                                self.create_level_vertical()
                            else:
                                if not DIFFICULTY_SETTINGS[self.difficulty]['auto_run'] and not \
                                        DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
                                    settings_copy = DIFFICULTY_SETTINGS[self.difficulty]
                                    base_time = settings_copy['time_limit_base']
                                    self.total_time_spent += (
                                            base_time - (self.current_level - 2) * 10 - self.time_left)
                                    self.time_left = DIFFICULTY_SETTINGS[self.difficulty]['time_limit_base'] - (
                                            self.current_level - 1) * 10
                                self.create_level_platformer()
                                self.start_time = pygame.time.get_ticks()

                            # Restart background music for next level
                            self.sound_manager.play_background_music()
                            self.state = PLAYING
                        elif self.level_complete_menu_button and self.level_complete_menu_button.check_click(event.pos):
                            self.state = MENU
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.sound_manager.play_click()
                        self.current_level += 1
                        self.distance = 0
                        self.altitude = 0
                        self.bg_scroll = 0
                        self.camera_y = 0
                        if self.difficulty == 'hard':
                            self.hard_mode_fall_count = 0

                        if DIFFICULTY_SETTINGS[self.difficulty]['auto_run']:
                            self.create_level_easy()
                        elif DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
                            self.create_level_vertical()
                        else:
                            if not DIFFICULTY_SETTINGS[self.difficulty]['auto_run'] and not \
                                    DIFFICULTY_SETTINGS[self.difficulty]['is_vertical']:
                                settings_copy = DIFFICULTY_SETTINGS[self.difficulty]
                                base_time = settings_copy['time_limit_base']
                                self.total_time_spent += (base_time - (self.current_level - 2) * 10 - self.time_left)
                                self.time_left = DIFFICULTY_SETTINGS[self.difficulty]['time_limit_base'] - (
                                        self.current_level - 1) * 10
                            self.create_level_platformer()
                            self.start_time = pygame.time.get_ticks()

                        # Restart background music for next level
                        self.sound_manager.play_background_music()
                        self.state = PLAYING
                elif self.state == MODE_VICTORY:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.sound_manager.play_click()
                        if self.mode_victory_menu_button and self.mode_victory_menu_button.check_click(event.pos):
                            self.state = MENU
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.sound_manager.play_click()
                        self.state = MENU
                elif self.state == VICTORY:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.state = MENU

            if self.state == PLAYING:
                self.update_playing()

            # Update hint popup timer (auto-close after 5 seconds)
            if self.state == HINT:
                if pygame.time.get_ticks() - self.hint_popup_timer >= 3000:
                    self.state = PLAYING
                    self.current_hint_text = None

            self.update_question_feedback()

            if self.state == MENU:
                self.draw_menu()
            elif self.state == INSTRUCTIONS:
                self.draw_instructions()
            elif self.state == PLAYING:
                self.draw_playing()
            elif self.state == QUESTION:
                self.draw_playing()
                self.draw_question()
            elif self.state == HINT:
                self.draw_playing()
                self.draw_hint()
            elif self.state == SHOP:
                self.draw_shop()
            elif self.state == PROFILE:
                self.draw_profile()
            elif self.state == GAME_OVER:
                self.draw_game_over()
            elif self.state == LEVEL_COMPLETE:
                self.draw_level_complete()
            elif self.state == MODE_VICTORY:
                self.draw_mode_victory()
            elif self.state == VICTORY:
                self.draw_victory()

            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)  # dodaeno

        pygame.quit()
        # sys.exit()


if __name__ == "__main__":
    game = Game()
    # game.run()
    asyncio.run(game.run())
