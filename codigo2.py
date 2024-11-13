import trimesh

#carrega o modelo 3D
mesh = trimesh.load_mesh('./models/Enterprise NCC 1701 D/enterprise1701d.obj')

#iluminacao
ambient_light = [0.5, 0.5, 0.5]  #luz ambiente
light_color = [1.0, 1.0, 1.0]    #cor da luz direcionada
directional_light = [0.0, 1.0, 0.0]  #direcao da luz

#exibi o modelo 3D com as configurações de iluminação e fundo
mesh.show(background=[0, 0, 0],  #fundo preto
          ambient_light=ambient_light,  #luz ambiente
          light_color=light_color,  #cor da luz
          directional_light=directional_light)  #luz direcional
