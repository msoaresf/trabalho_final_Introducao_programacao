import pygame
import random

# Inicialização
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1300, 750))
pygame.display.set_caption("Jogo Exemplo - Pygame")
clock = pygame.time.Clock()

# Sons
pygame.mixer.music.load("musica.mp3")  
pygame.mixer.music.play(-1)  # toca em loop
som_ponto = pygame.mixer.Sound("pulo.mp3")  # som de ponto

# Cores
azul = (176,224,230)

# Imagens
celeste = pygame.image.load("celeste.png").convert_alpha()
celeste = pygame.transform.scale(celeste, (120, 120))

peixe = pygame.image.load("peixe.png").convert_alpha()
peixe = pygame.transform.scale(peixe, (80, 80))

# Sprite do jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = celeste
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.velocidade = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade

# Sprite do inimigo/objeto
class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = peixe
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(0, 570)

# Grupos de sprites
jogador = Jogador()
all_sprites = pygame.sprite.Group()
estrelas = pygame.sprite.Group()
all_sprites.add(jogador)

for _ in range(5):
    estrela = Estrela()
    estrelas.add(estrela)
    all_sprites.add(estrela)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont(None, 36)

# Loop do jogo
rodando = True
while rodando:
    clock.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualização
    all_sprites.update()

    # Colisões
    colisoes = pygame.sprite.spritecollide(jogador, estrelas, True)
    for estrela in colisoes:
        som_ponto.play()
        pontos += 1
        nova = Estrela()
        estrelas.add(nova)
        all_sprites.add(nova)

    # Desenho
    screen.fill(azul)
    all_sprites.draw(screen)
    texto = fonte.render(f"Pontos: {pontos}", True, (0, 0, 0))
    screen.blit(texto, (10, 10))
    pygame.display.flip()

pygame.quit()
