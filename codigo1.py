import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

#carrega e processar o arquivo .obj
def load_obj(filename):
    vertices = []  #lista para armazenar os vertices
    faces = []     #lista para armazenar as faces

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()

            if parts:
                #adiciona vertices
                if parts[0] == 'v':
                    vertices.append([float(coord) for coord in parts[1:]])

                #adiciona as faces
                elif parts[0] == 'f':
                    faces.append([int(i.split('/')[0]) - 1 for i in parts[1:]])

    return np.array(vertices), faces

#funcao para desenhar o modelo
def draw_model(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
    glEnd()

#inicia Pygame e OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#defini parametros de camera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, -1.0, -5)

#carrega o arquivo .obj
file_path = './models/sylvanas/Files/Sylvanas Windrunner Posed.obj'
vertices, faces = load_obj(file_path)

#controle a rotacao
rotation_y = 0

#loop principal do PyGame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #limpa a tela
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #aplicar a rotacao    
    rotation_y += 10  #incremento para rotação no eixo Y
    
    glPushMatrix()  #salva o estado atual da transformada  
    glRotatef(rotation_y, 0, 1, 0)  #aplica rotacao no eixo Y

    #desenha o modelo
    draw_model(vertices, faces)

    # Restaura a matriz de transformada
    glPopMatrix()

    #atualiza a tela
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
