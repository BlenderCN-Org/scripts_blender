import bpy
from pyasn1.type import constraint

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

        # OBJECT PROPERTIES
        layout.separator()

        row = layout.row()
        row.label(text="PROPRIEDADES DO OBJETO ATIVO")

        split = layout.split(percentage=0.70)

        row = split.row()
        row.prop(obj, "name", text="Nome")

        row = split.row()
        row.prop(obj, "select", text="Selecionar")

        row = layout.row(align=True)
        row.prop(obj, "hide", text="View")
        row.prop(obj, "hide_select", text="Seleção")
        row.prop(obj, "hide_render", text="Render")

        row = layout.row()
        row.prop(obj, "color", text="Cor")
        row.prop(obj, "active_material", text="Material")

        # SMOOTH, FLAT
        row = layout.row(align=True)
        row.operator("object.shade_smooth", text="Smooth")
        row.operator("object.shade_flat", text="Flat")

        mesh = obj.data  # captura do mesh do ativo

        split = layout.box().split()

        col = split.column()
        col.prop(mesh, "use_auto_smooth")
        sub = col.column()
        sub.active = mesh.use_auto_smooth and not mesh.has_custom_normals
        sub.prop(mesh, "auto_smooth_angle", text="Angle")

        split.prop(mesh, "show_double_sided")

        row = layout.row()
        row.prop(obj, "parent", text="Pai")

        # GROUPS
        row = layout.row()
        row.label(text="Grupos")

        row = layout.row(align=True)
        if bpy.data.groups:
            row.operator("object.group_link", text="Adicionar ao Grupo")
        else:
            row.operator("object.group_add", text="Adicionar ao Grupo")
        row.operator("object.group_add", text="", icon='ZOOMIN')

        col = layout.column(align=True)

        if obj.users_group:
            row = col.box().row()

            for group in bpy.data.groups:
                if obj.name in group.objects:
                    row.context_pointer_set("group", group)
                    row.prop(group, "name", text="")
                    row.operator("object.group_remove", text="", icon='X', emboss=False)

        # MODIFIERS
        layout.separator()

        row = layout.row()
        row.label(text="MODIFICADORES")

        row = layout.row(align=True)
        row.label(text="Remover")
        row.operator("object.remover_modificadores")
        row.operator("object.remover_modificadores_ativo")
        row.operator("object.remover_modificadores_selecionados")

        row = layout.row()
        row.operator("object.copiar_modificadores")

        # CONSTRAINTS
        layout.separator()

        row = layout.row()
        row.label(text="LIMITAÇÕES(CONSTRAINTS)")

        row = layout.row(align=True)
        row.label(text="Remover")
        row.operator("object.remover_limitacoes")
        row.operator("object.remover_limitacoes_ativo")
        row.operator("object.remover_limitacoes_selecionados")

        row = layout.row()
        row.operator("object.copiar_limitacoes")

        layout.separator()

        row = layout.row()
        row.label(text="BLOQUEAR/DESBLOQUEAR")

        row = layout.row(align=True)
        row.label(text="Selecionados")
        row.operator("object.bloquear_localizacao")
        row.operator("object.bloquear_rotacao")
        row.operator("object.bloquear_escala")

        layout.separator()

        row = layout.row()
        row.operator("object.teste")


class RemoverModificadores(bpy.types.Operator):
    """ Operator 'Remover modificadores'.
    Remove todos os modificadores de todos os objetos MESH da cena. """
    # ref. a função remover_all_modifiers()
    bl_idname = "object.remover_modificadores"
    bl_label = "TODOS"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_modifiers(context)
        return {'FINISHED'}


class RemoverModificadoresAtivo(bpy.types.Operator):
    """ Operator 'Remover modificadores de ativo'.
    Remove todos os modificadores do objeto MESH ativo na cena. """
    # ref. a função remover_all_modifiers_ativo()
    bl_idname = "object.remover_modificadores_ativo"
    bl_label = "ATIVO"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_modifiers_active(context)
        return {'FINISHED'}


class RemoverModificadoresSelecionados(bpy.types.Operator):
    """ Operator 'Remover modificadores de selecionados'.
    Remove todos os modificadores dos objetos MESH selecionados na cena. """
    # ref. a função remover_all_modifiers()
    bl_idname = "object.remover_modificadores_selecionados"
    bl_label = "SELECIONADOS"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        remove_all_modifiers_selected(context)
        return {'FINISHED'}


class RemoverLimitacoes(bpy.types.Operator):
    """ Operator 'Remover limitacoes'.
    Remove todos as limitações(constraints) de todos os objetos da cena. """
    # ref. a função remover_all_constraints()
    bl_idname = "object.remover_limitacoes"
    bl_label = "TODOS"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_constraints(context)
        return {'FINISHED'}


class RemoverLimitacoesAtivo(bpy.types.Operator):
    """ Operator 'Remover limitações de ativo'.
    Remove todos as limitações(constraints) do objeto ativo na cena. """
    # ref. a função remover_all_constraints_ativo()
    bl_idname = "object.remover_limitacoes_ativo"
    bl_label = "ATIVO"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_constraints_active(context)
        return {'FINISHED'}


class RemoverLimitacoesSelecionados(bpy.types.Operator):
    """ Operator 'Remover limitações de selecionados'.
    Remove todos as limitações(constraints) dos objetos selecionados na cena. """
    # ref. a função remover_all_constraints_selecionados()
    bl_idname = "object.remover_limitacoes_selecionados"
    bl_label = "SELECIONADOS"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        remove_all_constraints_selected(context)
        return {'FINISHED'}


class BloquearLocalizacao(bpy.types.Operator):
    """ Operator 'Bloquear localização'.
    Bloqueia todos os eixos de localização do objeto selecionado baseado no ativo. """
    # Ref. a função lock()
    bl_idname = "object.bloquear_localizacao"
    bl_label = "Location"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        lock(context, 'location')
        return {'FINISHED'}


class BloquearRotacao(bpy.types.Operator):
    """ Operator 'Bloquear rotação'.
    Bloqueia todos os eixos de rotação do objeto selecionado baseado no ativo. """
    # Ref. a função lock()
    bl_idname = "object.bloquear_rotacao"
    bl_label = "Rotation"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        lock(context, 'rotation')
        return {'FINISHED'}


class BloquearEscala(bpy.types.Operator):
    """ Operator 'Bloquear escala'.
    Bloqueia todos os eixos de escala do objeto selecionado baseado no ativo. """
    # Ref. a função lock_location()
    bl_idname = "object.bloquear_escala"
    bl_label = "Scale"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        lock(context, 'scale')
        return {'FINISHED'}


class CopiarModificadores(bpy.types.Operator):
    """ Operator 'Copiar modificadores'.
    Copia todos os modificadores do objeto ativo para todos os objetos MESH selecionados da cena. """
    # ref. a função copy_all_modifiers()
    bl_idname = "object.copiar_modificadores"
    bl_label = "Copiar modificadores"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        copy_all_modifiers(context)
        return {'FINISHED'}


class CopiarLimitacoes(bpy.types.Operator):
    """ Operator 'Copiar limitacoes'.
    Copia todos as limitações(constraints) do objeto ativo para todos os objetos selecionados da cena. """
    # ref. a função copy_all_constraints()
    bl_idname = "object.copiar_limitacoes"
    bl_label = "Copiar limitações"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)

    def execute(self, context):
        copy_all_constraints(context)
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


def get_active_object(context):
    """ Retorna o objeto ativo de acordo com contexto informado. """
    return context.active_object


def get_selected_objects(context):
    """ Retorna uma lista de objetos de acordo com contexto informado. """
    return context.selected_objects


def get_list_selected_objects(context):
    """ Retorna uma lista com todos os objetos selecionados na cena """
    return context.selected_objects


def remove_all_modifiers(context, obj_type='MESH', objects=None):
    """ Remove todos os modificadores de todos os objetos do tipo informado na cena atual. """

    if objects is None:
        objects = get_objects_scene(context)

    for i, obj in enumerate(objects):
        if obj.type == obj_type:
            cont = 0
            for modifier in obj.modifiers.values():
                obj.modifiers.remove(modifier)
                cont += 1

            impressao_formatada("[{}] Removido {} modificador{} de {} {}",
                                i, cont, '' if cont == 1 else 'es', obj_type, obj.name)


def remove_all_modifiers_active(context, obj_type='MESH'):
    """ Remove todos os modificadores do objeto ativo do tipo informado na cena atual. """
    # o objeto ativo deve ser informado em uma lista por causa o enumarate de remove_all_modifiers
    objeto_ativo = [get_active_object(context)]
    remove_all_modifiers(context, obj_type=obj_type, objects=objeto_ativo)


def remove_all_modifiers_selected(context, obj_type='MESH'):
    """ Remove todos os modificadores dos objetos selecionados do tipo informado na cena atual. """
    objeto_selecionado = get_selected_objects(context)
    remove_all_modifiers(context, obj_type=obj_type, objects=objeto_selecionado)


def remove_all_constraints(context, objects=None):
    """ Remove todos os limitaçoes de todos os objetos do tipo informado na cena atual. """

    if objects is None:
        objects = get_objects_scene(context)

    for i, obj in enumerate(objects):
        cont = 0
        for constraint in obj.constraints.values():
            obj.constraints.remove(constraint)
            cont += 1

        impressao_formatada("[{}] Removido {} limitaç{} de {} {}",
                            i, cont, 'ão' if cont == 1 else 'ões', obj.type, obj.name)


def remove_all_constraints_active(context):
    """ Remove todos os limitações do objeto ativo do tipo informado na cena atual. """
    # o objeto ativo deve ser informado em uma lista por causa o enumarate de remove_all_constraints
    objeto_ativo = [get_active_object(context)]
    remove_all_constraints(context, objects=objeto_ativo)


def remove_all_constraints_selected(context):
    """ Remove todos os limitações dos objetos selecionados do tipo informado na cena atual. """
    objeto_selecionado = get_selected_objects(context)
    remove_all_constraints(context, objects=objeto_selecionado)


def copy_all_modifiers(context, obj_type='MESH'):
    """ Copia todos os modificadores do objeto ativo para os objetos selecionados. """
    ativo = get_active_object(context)
    selecionados = get_selected_objects(context)
    selecionados.remove(ativo)

    for i, obj in enumerate(selecionados):
        if obj.type == obj_type:
            cont = 0
            for modifier in ativo.modifiers.values():
                obj.modifiers.new(modifier.name, modifier.type)
                cont += 1

            impressao_formatada("[{}] Copiado de {} {} modificador{} de {} {}",
                                i, ativo.name, cont, '' if cont == 1 else 'es', obj_type, obj.name)


def copy_all_constraints(context):
    """ Copia todos as limitações do objeto ativo para os objetos selecionados. """
    ativo = get_active_object(context)
    selecionados = get_selected_objects(context)
    selecionados.remove(ativo)

    for i, obj in enumerate(selecionados):
        cont = 0
        for constraint in ativo.constraints.values():
            obj.constraints.new(constraint.type)
            cont += 1

        impressao_formatada("[{}] Copiado de {} {} limitaç{} de {} {}",
                            i, ativo.name, cont, 'ão' if cont == 1 else 'ões', obj.type, obj.name)


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
    # print(dir(context))
    # print(get_list_selected_objects(context))        


def lock(context, type_operation):
    """ Bloqueia/desbloqueia location/rotation/scale de objetos selecionados de acordo com estado de objeto ativo. """
    for i, obj in enumerate(get_selected_objects(context)):
        tipo = ''
        operacao = False
        condicao_ativo = False

        if type_operation == 'location':
            tipo = 'localizacao'
            operacao = obj.lock_location
            condicao_ativo = get_active_object(context).lock_location
        elif type_operation == 'rotation':
            tipo = 'rotação'
            operacao = obj.lock_rotation
            condicao_ativo = get_active_object(context).lock_rotation
        elif type_operation == 'scale':
            tipo = 'escala'
            operacao = obj.lock_scale
            condicao_ativo = get_active_object(context).lock_scale
        else:
            impressao_formatada('Tipo de operação inválida: {}', type_operation)

        lock = not condicao_ativo[0]
        for j in range(3):
            operacao[j] = lock

        condicao = "Bloqueado" if lock else "Desbloqueado"

        impressao_formatada("[{}] {} {} de {}", i, condicao, tipo, obj.name)


# Registradores do blender para as classes de UI e Operators
def register():
    bpy.utils.register_class(RemoverModificadores)
    bpy.utils.register_class(RemoverModificadoresAtivo)
    bpy.utils.register_class(RemoverModificadoresSelecionados)
    bpy.utils.register_class(CopiarModificadores)
    bpy.utils.register_class(RemoverLimitacoes)
    bpy.utils.register_class(RemoverLimitacoesAtivo)
    bpy.utils.register_class(RemoverLimitacoesSelecionados)
    bpy.utils.register_class(CopiarLimitacoes)
    bpy.utils.register_class(BloquearLocalizacao)
    bpy.utils.register_class(BloquearRotacao)
    bpy.utils.register_class(BloquearEscala)
    bpy.utils.register_class(Teste)
    bpy.utils.register_class(ToolsPanel)


def unregister():
    bpy.utils.unregister_class(RemoverModificadores)
    bpy.utils.unregister_class(RemoverModificadoresAtivo)
    bpy.utils.unregister_class(RemoverModificadoresSelecionados)
    bpy.utils.unregister_class(CopiarModificadores)
    bpy.utils.unregister_class(RemoverLimitacoes)
    bpy.utils.unregister_class(RemoverLimitacoesAtivo)
    bpy.utils.unregister_class(RemoverLimitacoesSelecionados)
    bpy.utils.unregister_class(CopiarLimitacoes)
    bpy.utils.unregister_class(BloquearLocalizacao)
    bpy.utils.unregister_class(BloquearRotacao)
    bpy.utils.unregister_class(BloquearEscala)
    bpy.utils.unregister_class(Teste)
    bpy.utils.unregister_class(ToolsPanel)


if __name__ == "__main__":
    register()
