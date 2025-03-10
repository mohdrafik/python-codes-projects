import open3d as o3d

mesh = o3d.io.read_triangle_mesh("cubemine.obj")
# o3d.visualization.draw_geometries([mesh],window_name="Custom Window Name", width=800, height=600)
o3d.visualization.draw_geometries([mesh],window_name="Custom Window Name")
# """ above lines are uisng the o3d and below given code using the  the openGPL library pygame
# """
# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from pywavefront import Wavefront

# # Initialize Pygame
# pygame.init()

# # Window settings
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)

# # Load OBJ model (replace 'cube.obj' with your OBJ file)
# obj = Wavefront('cube1.obj')

# # Main rendering loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     glRotatef(1, 3, 1, 1)  # Rotate the model

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#     # Render the model by iterating through its vertices and faces
#     for name, material in obj.materials.items():
#         glBindTexture(GL_TEXTURE_2D, material.texture)
#         for face in obj.groups[name]:
#             glBegin(GL_TRIANGLES)
#             for vertex_i in face:
#                 vertex = obj.vertices[vertex_i]
#                 glNormal3fv(obj.normals[vertex[2]])
#                 glVertex3fv(vertex[:2])
#             glEnd()

#     pygame.display.flip()
#     pygame.time.wait(10)

