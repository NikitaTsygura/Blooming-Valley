import pygame
import sys

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.button_font = pygame.font.SysFont('Arial', 30)
        self.title_font = pygame.font.Font('assets/fonts/LittleLordFontleroyNF.ttf', 100)

        # Кнопки
        self.buttons = {
            "Start": pygame.Rect(300, 220, 200, 50),
            "Continue": pygame.Rect(300, 290, 200, 50),
            "Quit": pygame.Rect(300, 360, 200, 50)
        }
        self.button_clicked = None  # Переменная для хранения выбранной кнопки

    def draw_rounded_button(self, text, rect, hover):
        # Рисуем кнопку с округлыми углами
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, rect, border_radius=15)
        label = self.button_font.render(text, True, BLACK)
        self.screen.blit(label, (rect.x + (rect.width - label.get_width()) // 2,
                                 rect.y + (rect.height - label.get_height()) // 2))

    def draw_game_title(self):
        # Отображаем название игры
        title_text = "Blooming Valley"
        title_label = self.title_font.render(title_text, True, BLACK)
        self.screen.blit(title_label, (self.screen.get_width() // 2 - title_label.get_width() // 2, 50))

    def handle_button_click(self, mouse_pos):
        # Обработка кликов по кнопкам
        for button_text, button_rect in self.buttons.items():
            if button_rect.collidepoint(mouse_pos):
                self.button_clicked = button_text  # Сохраняем выбранную кнопку

    def get_button_clicked(self):
        return self.button_clicked  # Возвращаем кнопку, на которую нажал пользователь

    def run(self):
        self.screen.fill(WHITE)

        # Отображаем название игры
        self.draw_game_title()

        mouse_pos = pygame.mouse.get_pos()

        # Отображаем кнопки с округлыми углами
        for button_text, button_rect in self.buttons.items():
            hover = button_rect.collidepoint(mouse_pos)
            self.draw_rounded_button(button_text, button_rect, hover)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.button_clicked = "Quit"
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_button_click(mouse_pos)

            # Закрыть игру, если нажали на "Quit"
            if self.button_clicked == "Quit":
                pygame.quit()
                sys.exit()
