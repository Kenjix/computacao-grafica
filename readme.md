# Exibição de Modelo 3D com Pygame e OpenGL (codigo1)

## Bibliotecas Utilizadas:
- **Pygame**:
  - Inicialização e controle da janela e eventos.
  - Suporte para gráficos 3D com OpenGL.
  
- **OpenGL (pyOpenGL)**:
  - Renderização de gráficos 3D e transformações.
  - Funções para desenhar, rotacionar e transladar objetos 3D.
  
- **NumPy**:
  - Manipulação de arrays para armazenar vértices e faces do modelo.

## Processo de Implementação:
1. **Carregamento do Modelo (.obj)**:
   - Lê vértices (v) e faces (f) do arquivo .obj.
   - Armazena dados em listas e converte em arrays NumPy.

2. **Configuração do OpenGL**:
   - `gluPerspective()` para definir perspectiva.
   - `glTranslatef()` para mover o modelo na cena.

3. **Desenho e Rotação**:
   - `draw_model()` desenha o modelo com triângulos.
   - Rotação contínua com `glRotatef()`, controlada por `rotation_y`.

4. **Loop Principal**:
   - Captura eventos (como fechamento de janela).
   - Atualiza a tela e aplica rotação a cada quadro.

---

# Exibição de Modelo 3D com Trimesh (codigo2)

## Bibliotecas Utilizadas:
- **Trimesh**:
  - Carregamento, visualização e manipulação de modelos 3D.
  - Suporte para renderização com configurações de luz e fundo personalizados.

## Processo de Implementação:
1. **Carregamento do Modelo 3D**:
   - O método `trimesh.load_mesh()` é utilizado para carregar o modelo 3D a partir de um arquivo `.obj`. 
   - O caminho para o arquivo `.obj` deve ser fornecido corretamente para que o modelo seja carregado.
    
     
   ```python
   mesh = trimesh.load_mesh('./models/Enterprise NCC 1701 D/enterprise1701d.obj')


2. **Configuração de Iluminação**:
  - A luz ambiente (ambient_light) é definida para fornecer uma iluminação uniforme e suave sobre o modelo.
  - A cor da luz direcional (light_color) é configurada para branca, de modo a simular uma luz natural.
  - A direção da luz direcional (directional_light) é especificada, com a luz vindo de cima para baixo (eixo Y positivo).


3. **Exibição do Modelo 3D**:
  - O método mesh.show() é utilizado para exibir o modelo 3D, com várias configurações:
  - background: Define a cor de fundo da cena (preto, neste caso).
  - ambient_light: Aplica a luz ambiente no modelo.
  - light_color: Aplica a cor da luz direcional.
  - directional_light: Aplica a direção da luz, criando o efeito de sombreamento no modelo.
    
```python
mesh.show(
    background=[0, 0, 0],  # Fundo preto
    ambient_light=ambient_light,  # Luz ambiente
    light_color=light_color,  # Cor da luz
    directional_light=directional_light  # Luz direcional)

