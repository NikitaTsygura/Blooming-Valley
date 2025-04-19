import pygame
import sys
from game.menu import MainMenu
from game.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blooming Valley")

    menu = MainMenu(screen)  # Создаем объект главного меню
    game = Game(screen)  # Создаем объект игры

    running = True
    in_menu = True  # Статус: находимся ли мы в меню

    while running:
        if in_menu:
            menu.run()  # Запускаем меню
            button_clicked = menu.get_button_clicked()  # Получаем выбранную кнопку
            if button_clicked == "Start":
                in_menu = False  # Переходим в игру
            elif button_clicked == "Quit":
                running = False  # Выход из игры

        else:
            game.run()  # Запускаем игру
            in_menu = True  # Возвращаемся в меню после завершения игры

    pygame.quit()

if __name__ == "__main__":
    main()
