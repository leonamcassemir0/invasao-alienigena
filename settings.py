"""
Sempre que for criar um projeto, crie um arquivo para configurações padrão,
para que você não precise modificar sempre cada arquivo do projeto.
"""


class Settings():
    """
    Uma classe para armazenar todas as configurações da Invasão Alienpigena.
    """

    def __init__(self):
        # Inicializa as configurações do jogo
        # Configurações da tela:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
