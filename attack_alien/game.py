import sys, pygame


class AlienAttack:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Вороги напали!")

    def run_game(self):
        while True:
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == '__main__':
    aa = AlienAttack()
    aa.run_game()
