import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)

# Вершины и поверхности куба
cube_vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
]

cube_surfaces = [
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
]

# Главная функция для рисования куба
def draw_cube():
    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        for vertex in surface:
            glVertex3fv(cube_vertices[vertex])
    glEnd()

# Главное меню
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.button_font = pygame.font.SysFont('Arial', 30)

        # Загрузка шрифта для названия игры с размером 100
        self.title_font = pygame.font.Font('assets/fonts/LittleLordFontleroyNF.ttf', 100)  # Установим размер шрифта 100

        # Создаем кнопки
        self.buttons = {
            "Start": pygame.Rect(300, 220, 200, 50),
            "About": pygame.Rect(300, 290, 200, 50),
            "Exit": pygame.Rect(300, 360, 200, 50),
        }

    def draw_rounded_button(self, text, rect, hover):
        # Рисуем кнопку с округлыми углами и изменяющимся цветом при наведении
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, rect, border_radius=15)
        label = self.button_font.render(text, True, BLACK)
        self.screen.blit(label, (rect.x + (rect.width - label.get_width()) // 2,
                                 rect.y + (rect.height - label.get_height()) // 2))

    def draw_game_title(self):
        # Отображаем название игры с использованием пользовательского шрифта
        title_text = "Blooming Valley"
        title_label = self.title_font.render(title_text, True, BLACK)
        self.screen.blit(title_label, (self.screen.get_width() // 2 - title_label.get_width() // 2, 50))

    def handle_button_click(self, mouse_pos):
        # Обработка кликов по кнопкам
        for button_text, button_rect in self.buttons.items():
            if button_rect.collidepoint(mouse_pos):
                return button_text
        return None

    def run(self):
        running = True
        game_started = False  # Переменная для отслеживания состояния игры (запущена ли анимация)

        while running:
            self.screen.fill(WHITE)

            # Если игра не началась, показываем главное меню
            if not game_started:
                # Отображаем название игры
                self.draw_game_title()

                # Получаем позицию мыши
                mouse_pos = pygame.mouse.get_pos()

                # Отображаем кнопки с округлыми углами
                for button_text, button_rect in self.buttons.items():
                    hover = button_rect.collidepoint(mouse_pos)
                    self.draw_rounded_button(button_text, button_rect, hover)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левый клик
                        button_clicked = self.handle_button_click(mouse_pos)
                        if button_clicked == "Start":
                            game_started = True  # Запускаем анимацию
                        elif button_clicked == "About":
                            print("About this game...")
                        elif button_clicked == "Exit":
                            running = False

            # Если игра началась, показываем анимацию
            else:
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран
                glRotatef(1, 3, 1, 1)  # Вращаем куб
                draw_cube()  # Рисуем куб
                pygame.display.flip()  # Обновляем экран
                pygame.time.wait(10)  # Замедление анимации для плавности

                # Обработка событий
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    menu = MainMenu(screen)
    menu.run()
