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

class UV_OT_Turn(bpy.types.Operator):
	bl_idname = "uv.turn"
	bl_label = "Turn (UV)"
	ccw: bpy.props.BoolProperty(name="CCW")

	@classmethod
	def poll(self, ctx):
		return True

	def execute(self, ctx):
		value = 1.5708 if self.ccw else -1.5708
		bpy.ops.transform.rotate(value=value,orient_axis='Z',orient_type='VIEW',
						orient_matrix=((-1,-0,-0),(-0,-1,-0),(-0,-0,-1)),
						orient_matrix_type='VIEW',mirror=True,
						use_proportional_edit=False,proportional_edit_falloff='SMOOTH',
						proportional_size=1,use_proportional_connected=False,
						use_proportional_projected=False)
		return{"FINISHED"}

def register_edit():
	bpy.utils.register_class(UV_OT_Turn)

def unregister_edit():
	bpy.utils.unregister_class(UV_OT_Turn)