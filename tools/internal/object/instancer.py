############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################
import bpy
from bpy.types import Operator

class OBJECT_TO_Date_Auto_Rename(Operator):
	""" Object.Data.Name = Object.Name in selection """
	bl_idname = 'object.data_auto_rename'
	bl_label = 'Data Auto Rename'
	bl_description = 'Copy Object Name to Data Name much as possible'
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(self, ctx):
		return ctx.mode == 'OBJECT'
	
	def execute(self,ctx):
		for obj in ctx.selected_objects:
			obj.data.name = obj.name
		return{"FINISHED"}


class Object_TO_Instancer_Select(Operator):
	""" collect and select object may suld be instance """
	bl_idname = 'object.instancer_select'
	bl_label = 'Instancer Select'
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(self, ctx):
		return ctx.mode == 'OBJECT'
	
	def execute(self,ctx):
		# collect ans select object has data with siliar name
		return{"FINISHED"}

class Object_TO_Make_Unique(Operator):
	bl_idname = 'object.make_unique'
	bl_label = 'Make Unique'
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(self, ctx):
		return ctx.mode == 'OBJECT'
	
	def execute(self,ctx):
		# collect and select object has data with similiar name
		return{"FINISHED"}



classes = [OBJECT_TO_Date_Auto_Rename]

def register_instancer():
	for c in classes:
		bpy.utils.register_class(c)

def unregister_instancer():
	for c in classes:
		bpy.utils.unregister_class(c)

if __name__ == "__main__":
	register_instancer()