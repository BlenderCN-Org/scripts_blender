import bpy

""" Para debugar o script, execute o Blender pelo terminal. 
 As docstring dos operators são visíveis como dicas(tag) blender. """


class ToolsPanel(bpy.types.Panel):
    """ Painel de ferramentas personalizado. Acesso 3D View->Região tools->Aba Custom tools. """
    bl_label = "Painel de ferramentas"
    bl_idname = "OBJECT_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Custom tools"

    def draw(self, context):
        layout = self.layout

        # obtendo objeto ativo na cena
        obj = context.object

        row = layout.row()
        row.label(text="O objeto ativo é: " + obj.name)

        row = layout.row()
        row.label(text="Trocar:")
        row.template_ID(get_objects_scene(context), "active")

        layout.separator()

        row = layout.row()
        row.label(text="Propriedades:")

        row = layout.row()
        row.prop(obj, "name")

        layout.separator()

        row = layout.row()
        row.label(text="Operadores:")

        row = layout.row()
        row.operator("object.remover_modificadores")

        row = layout.row()
        row.operator("object.bloquear_localizacao")

        row = layout.row()
        row.operator("object.bloquear_rotacao")

        row = layout.row()
        row.operator("object.bloquear_escala")

        row = layout.row()
        row.operator("object.teste")


class RemoverModificadores(bpy.types.Operator):
    """ Operator 'Remover modificadores'. Remove todos os modificadores de todos os objetos MESH da cena. """
    # ref. a função remover_all_modifiers()
    bl_idname = "object.remover_modificadores"
    bl_label = "Remover modificadores"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_modifiers(context)
        return {'FINISHED'}


class BloquearLocalizacao(bpy.types.Operator):
    """ Operator 'Bloquear localização'. Bloqueia todos os eixos de localização do objeto ativo. """
    # Ref. a função lock()
    bl_idname = "object.bloquear_localizacao"
    bl_label = "Bloquear localização"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        lock(context, 'location')
        return {'FINISHED'}


class BloquearRotacao(bpy.types.Operator):
    """ Operator 'Bloquear rotação'. Bloqueia todos os eixos de rotação do objeto ativo. """
    # Ref. a função lock()
    bl_idname = "object.bloquear_rotacao"
    bl_label = "Bloquear rotação"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        lock(context, 'rotation')
        return {'FINISHED'}


class BloquearEscala(bpy.types.Operator):
    """ Operator 'Bloquear escala'. Bloqueia todos os eixos de escala do objeto ativo. """
    # Ref. a função lock_location()
    bl_idname = "object.bloquear_escala"
    bl_label = "Bloquear escala"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        lock(context, 'scale')
        return {'FINISHED'}


class Teste(bpy.types.Operator):
    """ Operator 'teste'. Teste de funções. """
    # ref. a função teste()
    bl_idname = "object.teste"
    bl_label = "Teste"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        teste(context)
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


def remove_all_modifiers(context, obj_type='MESH'):
    """ Remove todos os modificadores de todos os objetos do tipo informado na cena atual. """
    for i, obj in enumerate(get_objects_scene(context)):
        if obj.type == obj_type:
            cont = 0
            for modifier in obj.modifiers.values():
                obj.modifiers.remove(modifier)
                cont += 1

            impressao_formatada("[{}] Removido {} modificador{} de {} {}",
                                i, cont, '' if cont == 1 else 'es', obj_type, obj.name)


def teste(context):
    objeto_ativo = context.active_object
    print("Objeto ativo: {}".format(objeto_ativo))
    # print(dir(objeto_ativo))

    # os valores de rotação então en radianos,
    # usar a sintaxe abaixo para converter em angulo
    # from math import radians
    # angulo = randians(objeto_ativo.rotation_euler[0])
    #
    # location e scale estão em vector, usar
    # from mathutils import Vector
    # objeto_ativo.location += Vector((4, 0, 0))  # para incrementar
    # print(objeto_ativo.location,
    #       objeto_ativo.rotation_euler,
    #       objeto_ativo.scale,
    #       sep='\n')
    print(dir(context))
    print(get_list_selected_objects(context))


def lock(context, type_operation):
    obj = context.active_object
    if type_operation == 'location':
        tipo = 'localizacao'
        operacao = obj.lock_location
    elif type_operation == 'rotation':
        tipo = 'rotação'
        operacao = obj.lock_rotation
    elif type_operation == 'scale':
        tipo = 'escala'
        operacao = obj.lock_scale
    else:
        impressao_formatada('Tipo de operação inválida: {}', type_operation)

    lock = not operacao[0]
    for i in range(3):
        operacao[i] = lock

    condicao = "Bloqueado " if lock else "Desbloqueado "

    impressao_formatada(condicao + tipo + " de {}", obj.name)


# Registradores do blender para as classes de UI e Operators
def register():
    bpy.utils.register_class(RemoverModificadores)
    bpy.utils.register_class(BloquearLocalizacao)
    bpy.utils.register_class(BloquearRotacao)
    bpy.utils.register_class(BloquearEscala)
    bpy.utils.register_class(Teste)
    bpy.utils.register_class(ToolsPanel)


def unregister():
    bpy.utils.unregister_class(RemoverModificadores)
    bpy.utils.unregister_class(BloquearLocalizacao)
    bpy.utils.unregister_class(BloquearRotacao)
    bpy.utils.unregister_class(BloquearEscala)
    bpy.utils.unregister_class(Teste)
    bpy.utils.unregister_class(ToolsPanel)


if __name__ == "__main__":
    register()
