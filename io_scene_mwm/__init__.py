bl_info = {
    "name": "Import Space Engineers Model File (.mwm)",
    "author": "Evgeny Vasilyev (Zeejfps)",
    "location": "File > Import",
    "description": "Import .mwm meshes",
    "category": "Import-Export",
}

import bpy

from . import import_mwm
from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ImportHelper

class ImportMwm(Operator, ImportHelper):

	bl_idname = "import_scene.space_engineers_mwm"
	bl_label = 'Import .mwm'
	bl_options = {'UNDO'}

	filename_ext = ".mwm"
	filter_glob = StringProperty(default="*.mwm", options={'HIDDEN'})

	def execute(self, context):
		return import_mwm.load(self, context)
		
		
# Add to a menu
def menu_func_import(self, context):
	self.layout.operator(ImportMwm.bl_idname, text="Space Engineers (.mwm)")


def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_file_import.append(menu_func_import)
	print ('register')


def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file_import.remove(menu_func_import)

	
if __name__ == "__main__":
	register()