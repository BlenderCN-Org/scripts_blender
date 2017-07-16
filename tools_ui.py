import bpy


class RemoverModificadores(bpy.types.Operator):
    """ Operator 'Remover modificadores' """
    bl_idname = "object.remover_modificadores"
    bl_label = "Remover modificadores"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_all_modifiers(context)
        return {'FINISHED'}


class ToolsPanel(bpy.types.Panel):
    """ Painel de ferramentas personalizado. Acesso 3D View->Região tools->Aba Custom tools. """
    bl_label = "Painel de ferramentas"
    bl_idname = "OBJECT_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Custom tools"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="O objeto ativo é: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.label(text="Operadores:")

        row = layout.row()
        row.operator("object.remover_modificadores")


# Funções personalizadas
def get_active_scene(context):
    """ Retorna a cena ativa """
    return context.scene


def get_objects_scene(context):
    """ Retorna uma tupla com todos o objetos da cena. """
    return get_active_scene(context).objects


def remove_all_modifiers(context, obj_type='MESH'):
    """ Remove todos os modificadores de todos os objetos MESH da cena atual. """
    for obj in get_objects_scene(context):
        print(obj)
        if obj.type == obj_type:
            for modifier in obj.modifiers.values():
                obj.modifiers.remove(modifier)


# Registradores do blender para as classes de UI e Operators
def register():
    bpy.utils.register_class(RemoverModificadores)
    bpy.utils.register_class(ToolsPanel)


def unregister():
    bpy.utils.unregister_class(RemoverModificadores)
    bpy.utils.unregister_class(ToolsPanel)


if __name__ == "__main__":
    register()
