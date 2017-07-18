import bpy
from math import radians

# Quantidade de rotação em graus para cada movimento
R = 90


class ToolsPanel(bpy.types.Panel):
    """ Painel de ferramentas personalizado. Acesso 3D View->Região tools->Aba Tools Magic Cube. """
    # bl_idname deve conter somente caracteres válidos, semelhante nos nomes de variáveis
    bl_label = "Ferramentas do cubo mágico"
    bl_idname = "OBJECT_PT_panel_magic_cube"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools Magic Cube"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("object.rotate90x1")
        row.operator("object.rotate_90x1")

        row = layout.row()
        row.operator("object.rotate90x2")
        row.operator("object.rotate_90x2")

        row = layout.row()
        row.operator("object.rotate90x3")
        row.operator("object.rotate_90x3")

        row = layout.row()
        row.operator("object.rotate90y1")
        row.operator("object.rotate_90y1")

        row = layout.row()
        row.operator("object.rotate90y2")
        row.operator("object.rotate_90y2")

        row = layout.row()
        row.operator("object.rotate90y3")
        row.operator("object.rotate_90y3")

        row = layout.row()
        row.operator("object.rotate90z1")
        row.operator("object.rotate_90z1")

        row = layout.row()
        row.operator("object.rotate90z2")
        row.operator("object.rotate_90z2")

        row = layout.row()
        row.operator("object.rotate90z3")
        row.operator("object.rotate_90z3")


# ROTAÇÃO DO EIXO X DOS GRUPOS REFERENTES
class Rotacionar90X1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_1 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90x1"
    bl_label = "+90º x_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_1', R)
        return {'FINISHED'}


class Rotacionar_90X1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_1 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90x1"
    bl_label = "-90º x_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_1', -R)
        return {'FINISHED'}


class Rotacionar90X2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_2 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90x2"
    bl_label = "+90º x_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_2', R)
        return {'FINISHED'}


class Rotacionar_90X2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_2 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90x2"
    bl_label = "-90º x_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_2', -R)
        return {'FINISHED'}


class Rotacionar90X3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_3 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90x3"
    bl_label = "+90º x_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_3', R)
        return {'FINISHED'}


class Rotacionar_90X3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo x_3 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90x3"
    bl_label = "-90º x_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'x_3', -R)
        return {'FINISHED'}


# ROTAÇÃO DO EIXO Y DOS GRUPOS REFERENTES
class Rotacionar90Y1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_1 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90y1"
    bl_label = "+90º y_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_1', R)
        return {'FINISHED'}


class Rotacionar_90Y1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_1 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90y1"
    bl_label = "-90º y_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_1', -R)
        return {'FINISHED'}


class Rotacionar90Y2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_2 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90y2"
    bl_label = "+90º y_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_2', R)
        return {'FINISHED'}


class Rotacionar_90Y2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_2 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90y2"
    bl_label = "-90º y_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_2', -R)
        return {'FINISHED'}


class Rotacionar90Y3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_3 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90y3"
    bl_label = "+90º y_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_3', R)
        return {'FINISHED'}


class Rotacionar_90Y3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo y_3 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90y3"
    bl_label = "-90º y_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'y_3', -R)
        return {'FINISHED'}


# ROTAÇÃO DO EIXO Z DOS GRUPOS REFERENTES
class Rotacionar90Z1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_1 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90z1"
    bl_label = "+90º z_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_1', R)
        return {'FINISHED'}


class Rotacionar_90Z1(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_1 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90z1"
    bl_label = "-90º z_1"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_1', -R)
        return {'FINISHED'}


class Rotacionar90Z2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_2 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90z2"
    bl_label = "+90º z_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_2', R)
        return {'FINISHED'}


class Rotacionar_90Z2(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_2 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90z2"
    bl_label = "-90º z_2"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_2', -R)
        return {'FINISHED'}


class Rotacionar90Z3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_3 +90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate90z3"
    bl_label = "+90º z_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_3', R)
        return {'FINISHED'}


class Rotacionar_90Z3(bpy.types.Operator):
    """ Operator 'rotate'. Rotaciona o grupo z_3 -90 graus. """
    # Ref. a função rotate()
    bl_idname = "object.rotate_90z3"
    bl_label = "-90º z_3"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        rotate(context, 'z_3', -R)
        return {'FINISHED'}


# Funções personalizadas
def impressao_formatada(texto, *args):
    print('SCRIPT: ' + texto.format(*args))


def get_active_scene(context):
    """ Retorna a cena ativa """
    return context.scene


def get_objects_scene(context):
    """ Retorna um bpy_prop_collection com todos o objetos da cena. Usar .values() para obter uma lista. """
    return get_active_scene(context).objects


def get_list_selected_objects(context):
    """ Retorna uma lista com todos os objetos selecionados na cena """
    return context.selected_objects


def get_list_group_objects(group_name):
    """ Retorna uma lista de objetos referente ao grupo informado. """
    return bpy.data.groups[group_name].objects.values()


def select_list_objects(list_objects):
    """ Seleciona somente os objetos informados em list_objects. """
    # retirando a seleção de todos os objetos da cena
    bpy.ops.object.select_all(action='DESELECT')

    # selecionando somente os objetos do grupo informado
    for o in list_objects:
        o.select = True


def rotate(context, group_name, degrees):
    """ Rotaciona os objetos do grupos informado de acordo com a quantidade de graus especificada. """
    assign_groups(context)

    group_objects = get_list_group_objects(group_name)

    select_list_objects(group_objects)

    if 'x' in group_name:
        axis = (1, 0, 0)
    elif 'y' in group_name:
        axis = (0, 1, 0)
    else:
        # 'z' in group_name:
        axis = (0, 0, 1)

    bpy.ops.transform.rotate(value=radians(degrees), axis=axis)

    bpy.ops.object.select_all(action='DESELECT')

    impressao_formatada("Rotacionado {}º o grupo {}", degrees, group_name)


def assign_groups(context):
    """ Atribuição de grupos de acordo com location dos objetos. """
    # base = context.scene.objects['base_cubo_magico']

    # os objetos cubo_unitario... tem como pai base_cubo_magico,
    # portando, Location e scale dos filhos são baseados no pai.
    # posicao_base = (base.location.x, base.location.y, base.location.z)

    # posições dos cubo_unitários com seus grupos respectivos
    posicoes = {}

    posicoes[(-1, 1.04, 2.54)] = ('x_1', 'y_3', 'z_3')
    posicoes[(-1, .02, 2.54)] = ('x_1', 'y_2', 'z_3')
    posicoes[(-1, -1, 2.54)] = ('x_1', 'y_1', 'z_3')
    posicoes[(-1, 1.04, 1.52)] = ('x_1', 'y_3', 'z_2')
    posicoes[(-1, .02, 1.52)] = ('x_1', 'y_2', 'z_2')
    posicoes[(-1, -1, 1.52)] = ('x_1', 'y_1', 'z_2')
    posicoes[(-1, 1.04, .5)] = ('x_1', 'y_3', 'z_1')
    posicoes[(-1, .02, .5)] = ('x_1', 'y_2', 'z_1')
    posicoes[(-1, -1, .5)] = ('x_1', 'y_1', 'z_1')

    posicoes[(.02, 1.04, .5)] = ('x_2', 'y_3', 'z_1')
    posicoes[(.02, .02, .5)] = ('x_2', 'y_2', 'z_1')
    posicoes[(.02, -1, .5)] = ('x_2', 'y_1', 'z_1')
    posicoes[(.02, 1.04, 1.52)] = ('x_2', 'y_3', 'z_2')
    posicoes[(.02, -1, 1.52)] = ('x_2', 'y_1', 'z_2')
    posicoes[(.02, 1.04, 2.54)] = ('x_2', 'y_3', 'z_3')
    posicoes[(.02, .02, 2.54)] = ('x_2', 'y_2', 'z_3')
    posicoes[(.02, -1, 2.54)] = ('x_2', 'y_1', 'z_3')

    posicoes[(1.04, -1, 2.54)] = ('x_3', 'y_1', 'z_3')
    posicoes[(1.04, .02, 2.54)] = ('x_3', 'y_2', 'z_3')
    posicoes[(1.04, 1.04, 2.54)] = ('x_3', 'y_3', 'z_3')
    posicoes[(1.04, -1, 1.52)] = ('x_3', 'y_1', 'z_2')
    posicoes[(1.04, .02, 1.52)] = ('x_3', 'y_2', 'z_2')
    posicoes[(1.04, 1.04, 1.52)] = ('x_3', 'y_3', 'z_2')
    posicoes[(1.04, -1, .5)] = ('x_3', 'y_1', 'z_1')
    posicoes[(1.04, .02, .5)] = ('x_3', 'y_2', 'z_1')
    posicoes[(1.04, 1.04, .5)] = ('x_3', 'y_3', 'z_1')

    bpy.ops.object.select_all(action='DESELECT')

    # remoção de todos os grupos existentes
    groups = bpy.data.groups
    for group in groups.values():
        groups.remove(group)

    # criação dos grupos para movimentação
    for l in 'xyz':
        for n in '123':
            groups.new('{}_{}'.format(l, n))

    objects = context.scene.objects

    # atribuição de grupo de acordo com coordenadas e grupo das posiçoes informadas
    for o in objects:
        x = round(o.location.x, 2)
        y = round(o.location.y, 2)
        z = round(o.location.z, 2)

        for pos in posicoes.keys():
            if x == pos[0] and y == pos[1] and z == pos[2]:
                impressao_formatada('Atribuído: {}, coordenadas: {}, ao grupo: {}'.format(o, pos, posicoes[pos]))
                for grupo in posicoes[pos]:
                    groups[grupo].objects.link(o)


# Registradores do blender para as classes de UI e Operators
def register():
    bpy.utils.register_class(Rotacionar90X1)
    bpy.utils.register_class(Rotacionar_90X1)
    bpy.utils.register_class(Rotacionar90X2)
    bpy.utils.register_class(Rotacionar_90X2)
    bpy.utils.register_class(Rotacionar90X3)
    bpy.utils.register_class(Rotacionar_90X3)

    bpy.utils.register_class(Rotacionar90Y1)
    bpy.utils.register_class(Rotacionar_90Y1)
    bpy.utils.register_class(Rotacionar90Y2)
    bpy.utils.register_class(Rotacionar_90Y2)
    bpy.utils.register_class(Rotacionar90Y3)
    bpy.utils.register_class(Rotacionar_90Y3)

    bpy.utils.register_class(Rotacionar90Z1)
    bpy.utils.register_class(Rotacionar_90Z1)
    bpy.utils.register_class(Rotacionar90Z2)
    bpy.utils.register_class(Rotacionar_90Z2)
    bpy.utils.register_class(Rotacionar90Z3)
    bpy.utils.register_class(Rotacionar_90Z3)

    bpy.utils.register_class(ToolsPanel)


def unregister():
    bpy.utils.unregister_class(Rotacionar90X1)
    bpy.utils.unregister_class(Rotacionar_90X1)
    bpy.utils.unregister_class(Rotacionar90X2)
    bpy.utils.unregister_class(Rotacionar_90X2)
    bpy.utils.unregister_class(Rotacionar90X3)
    bpy.utils.unregister_class(Rotacionar_90X3)

    bpy.utils.unregister_class(Rotacionar90Y1)
    bpy.utils.unregister_class(Rotacionar_90Y1)
    bpy.utils.unregister_class(Rotacionar90Y2)
    bpy.utils.unregister_class(Rotacionar_90Y2)
    bpy.utils.unregister_class(Rotacionar90Y3)
    bpy.utils.unregister_class(Rotacionar_90Y3)

    bpy.utils.unregister_class(Rotacionar90Z1)
    bpy.utils.unregister_class(Rotacionar_90Z1)
    bpy.utils.unregister_class(Rotacionar90Z2)
    bpy.utils.unregister_class(Rotacionar_90Z2)
    bpy.utils.unregister_class(Rotacionar90Z3)
    bpy.utils.unregister_class(Rotacionar_90Z3)

    bpy.utils.unregister_class(ToolsPanel)


if __name__ == "__main__":
    register()
