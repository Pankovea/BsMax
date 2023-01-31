############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation,either version 3 of the License,or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not,see <https://www.gnu.org/licenses/>.
############################################################################

import bpy
from primitive.primitive import Primitive_Geometry_Class, Draw_Primitive

def get_monkey_mesh(radius):
	verts = [(0.4375,-0.765625,0.1640625),(-0.4375,-0.765625,0.1640625),(0.5,-0.6875,0.09375),
	(-0.5,-0.6875,0.09375),(0.546875,-0.578125,0.0546875),(-0.546875,-0.578125,0.0546875),
	(0.3515625,-0.6171875,-0.0234375),(-0.3515625,-0.6171875,-0.0234375),(0.3515625,-0.71875,0.03125),
	(-0.3515625,-0.71875,0.03125),(0.3515625,-0.78125,0.1328125),(-0.3515625,-0.78125,0.1328125),
	(0.2734375,-0.796875,0.1640625),(-0.2734375,-0.796875,0.1640625),(0.203125,-0.7421875,0.09375),
	(-0.203125,-0.7421875,0.09375),(0.15625,-0.6484375,0.0546875),(-0.15625,-0.6484375,0.0546875),
	(0.078125,-0.65625,0.2421875),(-0.078125,-0.65625,0.2421875),(0.140625,-0.7421875,0.2421875),
	(-0.140625,-0.7421875,0.2421875),(0.2421875,-0.796875,0.2421875),(-0.2421875,-0.796875,0.2421875),
	(0.2734375,-0.796875,0.328125),(-0.2734375,-0.796875,0.328125),(0.203125,-0.7421875,0.390625),
	(-0.203125,-0.7421875,0.390625),(0.15625,-0.6484375,0.4375),(-0.15625,-0.6484375,0.4375),
	(0.3515625,-0.6171875,0.515625),(-0.3515625,-0.6171875,0.515625),(0.3515625,-0.71875,0.453125),
	(-0.3515625,-0.71875,0.453125),(0.3515625,-0.78125,0.359375),(-0.3515625,-0.78125,0.359375),
	(0.4375,-0.765625,0.328125),(-0.4375,-0.765625,0.328125),(0.5,-0.6875,0.390625),
	(-0.5,-0.6875,0.390625),(0.546875,-0.578125,0.4375),(-0.546875,-0.578125,0.4375),
	(0.625,-0.5625,0.2421875),(-0.625,-0.5625,0.2421875),(0.5625,-0.671875,0.2421875),
	(-0.5625,-0.671875,0.2421875),(0.46875,-0.7578125,0.2421875),(-0.46875,-0.7578125,0.2421875),
	(0.4765625,-0.7734375,0.2421875),(-0.4765625,-0.7734375,0.2421875),(0.4453125,-0.78125,0.3359375),
	(-0.4453125,-0.78125,0.3359375),(0.3515625,-0.8046875,0.375),(-0.3515625,-0.8046875,0.375),
	(0.265625,-0.8203125,0.3359375),(-0.265625,-0.8203125,0.3359375),(0.2265625,-0.8203125,0.2421875),
	(-0.2265625,-0.8203125,0.2421875),(0.265625,-0.8203125,0.15625),(-0.265625,-0.8203125,0.15625),
	(0.3515625,-0.828125,0.2421875),(-0.3515625,-0.828125,0.2421875),(0.3515625,-0.8046875,0.1171875),
	(-0.3515625,-0.8046875,0.1171875),(0.4453125,-0.78125,0.15625),(-0.4453125,-0.78125,0.15625),
	(0,-0.7421875,0.4296875),(0,-0.8203125,0.3515625),(0,-0.734375,-0.6796875),
	(0,-0.78125,-0.3203125),(0,-0.796875,-0.1875),(0,-0.71875,-0.7734375),
	(0,-0.6015625,0.40625),(0,-0.5703125,0.5703125),(0,0.546875,0.8984375),
	(0,0.8515625,0.5625),(0,0.828125,0.0703125),(0,0.3515625,-0.3828125),
	(0.203125,-0.5625,-0.1875),(-0.203125,-0.5625,-0.1875),(0.3125,-0.5703125,-0.4375),
	(-0.3125,-0.5703125,-0.4375),(0.3515625,-0.5703125,-0.6953125),(-0.3515625,-0.5703125,-0.6953125),
	(0.3671875,-0.53125,-0.890625),(-0.3671875,-0.53125,-0.890625),(0.328125,-0.5234375,-0.9453125),
	(-0.328125,-0.5234375,-0.9453125),(0.1796875,-0.5546875,-0.96875),(-0.1796875,-0.5546875,-0.96875),
	(0,-0.578125,-0.984375),(0.4375,-0.53125,-0.140625),(-0.4375,-0.53125,-0.140625),
	(0.6328125,-0.5390625,-0.0390625),(-0.6328125,-0.5390625,-0.0390625),(0.828125,-0.4453125,0.1484375),
	(-0.828125,-0.4453125,0.1484375),(0.859375,-0.59375,0.4296875),(-0.859375,-0.59375,0.4296875),
	(0.7109375,-0.625,0.484375),(-0.7109375,-0.625,0.484375),(0.4921875,-0.6875,0.6015625),
	(-0.4921875,-0.6875,0.6015625),(0.3203125,-0.734375,0.7578125),(-0.3203125,-0.734375,0.7578125),
	(0.15625,-0.7578125,0.71875),(-0.15625,-0.7578125,0.71875),(0.0625,-0.75,0.4921875),
	(-0.0625,-0.75,0.4921875),(0.1640625,-0.7734375,0.4140625),(-0.1640625,-0.7734375,0.4140625),
	(0.125,-0.765625,0.3046875),(-0.125,-0.765625,0.3046875),(0.203125,-0.7421875,0.09375),
	(-0.203125,-0.7421875,0.09375),(0.375,-0.703125,0.015625),(-0.375,-0.703125,0.015625),
	(0.4921875,-0.671875,0.0625),(-0.4921875,-0.671875,0.0625),(0.625,-0.6484375,0.1875),
	(-0.625,-0.6484375,0.1875),(0.640625,-0.6484375,0.296875),(-0.640625,-0.6484375,0.296875),
	(0.6015625,-0.6640625,0.375),(-0.6015625,-0.6640625,0.375),(0.4296875,-0.71875,0.4375),
	(-0.4296875,-0.71875,0.4375),(0.25,-0.7578125,0.46875),(-0.25,-0.7578125,0.46875),
	(0,-0.734375,-0.765625),(0.109375,-0.734375,-0.71875),(-0.109375,-0.734375,-0.71875),
	(0.1171875,-0.7109375,-0.8359375),(-0.1171875,-0.7109375,-0.8359375),(0.0625,-0.6953125,-0.8828125),
	(-0.0625,-0.6953125,-0.8828125),(0,-0.6875,-0.890625),(0,-0.75,-0.1953125),(0,-0.7421875,-0.140625),
	(0.1015625,-0.7421875,-0.1484375),(-0.1015625,-0.7421875,-0.1484375),(0.125,-0.75,-0.2265625),
	(-0.125,-0.75,-0.2265625),(0.0859375,-0.7421875,-0.2890625),(-0.0859375,-0.7421875,-0.2890625),
	(0.3984375,-0.671875,-0.046875),(-0.3984375,-0.671875,-0.046875),(0.6171875,-0.625,0.0546875),
	(-0.6171875,-0.625,0.0546875),(0.7265625,-0.6015625,0.203125),(-0.7265625,-0.6015625,0.203125),
	(0.7421875,-0.65625,0.375),(-0.7421875,-0.65625,0.375),(0.6875,-0.7265625,0.4140625),
	(-0.6875,-0.7265625,0.4140625),(0.4375,-0.796875,0.546875),(-0.4375,-0.796875,0.546875),
	(0.3125,-0.8359375,0.640625),(-0.3125,-0.8359375,0.640625),(0.203125,-0.8515625,0.6171875),
	(-0.203125,-0.8515625,0.6171875),(0.1015625,-0.84375,0.4296875),(-0.1015625,-0.84375,0.4296875),
	(0.125,-0.8125,-0.1015625),(-0.125,-0.8125,-0.1015625),(0.2109375,-0.7109375,-0.4453125),
	(-0.2109375,-0.7109375,-0.4453125),(0.25,-0.6875,-0.703125),(-0.25,-0.6875,-0.703125),
	(0.265625,-0.6640625,-0.8203125),(-0.265625,-0.6640625,-0.8203125),(0.234375,-0.6328125,-0.9140625),
	(-0.234375,-0.6328125,-0.9140625),(0.1640625,-0.6328125,-0.9296875),(-0.1640625,-0.6328125,-0.9296875),
	(0,-0.640625,-0.9453125),(0,-0.7265625,0.046875),(0,-0.765625,0.2109375),(0.328125,-0.7421875,0.4765625),
	(-0.328125,-0.7421875,0.4765625),(0.1640625,-0.75,0.140625),(-0.1640625,-0.75,0.140625),
	(0.1328125,-0.7578125,0.2109375),(-0.1328125,-0.7578125,0.2109375),(0.1171875,-0.734375,-0.6875),
	(-0.1171875,-0.734375,-0.6875),(0.078125,-0.75,-0.4453125),(-0.078125,-0.75,-0.4453125),
	(0,-0.75,-0.4453125),(0,-0.7421875,-0.328125),(0.09375,-0.78125,-0.2734375),(-0.09375,-0.78125,-0.2734375),
	(0.1328125,-0.796875,-0.2265625),(-0.1328125,-0.796875,-0.2265625),(0.109375,-0.78125,-0.1328125),
	(-0.109375,-0.78125,-0.1328125),(0.0390625,-0.78125,-0.125),(-0.0390625,-0.78125,-0.125),
	(0,-0.828125,-0.203125),(0.046875,-0.8125,-0.1484375),(-0.046875,-0.8125,-0.1484375),
	(0.09375,-0.8125,-0.15625),(-0.09375,-0.8125,-0.15625),(0.109375,-0.828125,-0.2265625),
	(-0.109375,-0.828125,-0.2265625),(0.078125,-0.8046875,-0.25),(-0.078125,-0.8046875,-0.25),
	(0,-0.8046875,-0.2890625),(0.2578125,-0.5546875,-0.3125),(-0.2578125,-0.5546875,-0.3125),
	(0.1640625,-0.7109375,-0.2421875),(-0.1640625,-0.7109375,-0.2421875),(0.1796875,-0.7109375,-0.3125),
	(-0.1796875,-0.7109375,-0.3125),(0.234375,-0.5546875,-0.25),(-0.234375,-0.5546875,-0.25),
	(0,-0.6875,-0.875),(0.046875,-0.6875,-0.8671875),(-0.046875,-0.6875,-0.8671875),
	(0.09375,-0.7109375,-0.8203125),(-0.09375,-0.7109375,-0.8203125),(0.09375,-0.7265625,-0.7421875),
	(-0.09375,-0.7265625,-0.7421875),(0,-0.65625,-0.78125),(0.09375,-0.6640625,-0.75),
	(-0.09375,-0.6640625,-0.75),(0.09375,-0.640625,-0.8125),(-0.09375,-0.640625,-0.8125),
	(0.046875,-0.6328125,-0.8515625),(-0.046875,-0.6328125,-0.8515625),(0,-0.6328125,-0.859375),
	(0.171875,-0.78125,0.21875),(-0.171875,-0.78125,0.21875),(0.1875,-0.7734375,0.15625),
	(-0.1875,-0.7734375,0.15625),(0.3359375,-0.7578125,0.4296875),(-0.3359375,-0.7578125,0.4296875),
	(0.2734375,-0.7734375,0.421875),(-0.2734375,-0.7734375,0.421875),(0.421875,-0.7734375,0.3984375),
	(-0.421875,-0.7734375,0.3984375),(0.5625,-0.6953125,0.3515625),(-0.5625,-0.6953125,0.3515625),
	(0.5859375,-0.6875,0.2890625),(-0.5859375,-0.6875,0.2890625),(0.578125,-0.6796875,0.1953125),
	(-0.578125,-0.6796875,0.1953125),(0.4765625,-0.71875,0.1015625),(-0.4765625,-0.71875,0.1015625),
	(0.375,-0.7421875,0.0625),(-0.375,-0.7421875,0.0625),(0.2265625,-0.78125,0.109375),
	(-0.2265625,-0.78125,0.109375),(0.1796875,-0.78125,0.296875),(-0.1796875,-0.78125,0.296875),
	(0.2109375,-0.78125,0.375),(-0.2109375,-0.78125,0.375),(0.234375,-0.7578125,0.359375),
	(-0.234375,-0.7578125,0.359375),(0.1953125,-0.7578125,0.296875),(-0.1953125,-0.7578125,0.296875),
	(0.2421875,-0.7578125,0.125),(-0.2421875,-0.7578125,0.125),(0.375,-0.7265625,0.0859375),
	(-0.375,-0.7265625,0.0859375),(0.4609375,-0.703125,0.1171875),(-0.4609375,-0.703125,0.1171875),
	(0.546875,-0.671875,0.2109375),(-0.546875,-0.671875,0.2109375),(0.5546875,-0.671875,0.28125),
	(-0.5546875,-0.671875,0.28125),(0.53125,-0.6796875,0.3359375),(-0.53125,-0.6796875,0.3359375),
	(0.4140625,-0.75,0.390625),(-0.4140625,-0.75,0.390625),(0.28125,-0.765625,0.3984375),
	(-0.28125,-0.765625,0.3984375),(0.3359375,-0.75,0.40625),(-0.3359375,-0.75,0.40625),
	(0.203125,-0.75,0.171875),(-0.203125,-0.75,0.171875),(0.1953125,-0.75,0.2265625),
	(-0.1953125,-0.75,0.2265625),(0.109375,-0.609375,0.4609375),(-0.109375,-0.609375,0.4609375),
	(0.1953125,-0.6171875,0.6640625),(-0.1953125,-0.6171875,0.6640625),(0.3359375,-0.59375,0.6875),
	(-0.3359375,-0.59375,0.6875),(0.484375,-0.5546875,0.5546875),(-0.484375,-0.5546875,0.5546875),
	(0.6796875,-0.4921875,0.453125),(-0.6796875,-0.4921875,0.453125),(0.796875,-0.4609375,0.40625),
	(-0.796875,-0.4609375,0.40625),(0.7734375,-0.375,0.1640625),(-0.7734375,-0.375,0.1640625),
	(0.6015625,-0.4140625,0.0),(-0.6015625,-0.4140625,0.0),(0.4375,-0.46875,-0.09375),
	(-0.4375,-0.46875,-0.09375),(0,-0.2890625,0.8984375),(0,0.078125,0.984375),(0,0.671875,-0.1953125),
	(0,-0.1875,-0.4609375),(0,-0.4609375,-0.9765625),(0,-0.34375,-0.8046875),(0,-0.3203125,-0.5703125),
	(0,-0.28125,-0.484375),(0.8515625,-0.0546875,0.234375),(-0.8515625,-0.0546875,0.234375),
	(0.859375,0.046875,0.3203125),(-0.859375,0.046875,0.3203125),(0.7734375,0.4375,0.265625),
	(-0.7734375,0.4375,0.265625),(0.4609375,0.703125,0.4375),(-0.4609375,0.703125,0.4375),
	(0.734375,-0.0703125,-0.046875),(-0.734375,-0.0703125,-0.046875),(0.59375,0.1640625,-0.125),
	(-0.59375,0.1640625,-0.125),(0.640625,0.4296875,-0.0078125),(-0.640625,0.4296875,-0.0078125),
	(0.3359375,0.6640625,0.0546875),(-0.3359375,0.6640625,0.0546875),(0.234375,-0.40625,-0.3515625),
	(-0.234375,-0.40625,-0.3515625),(0.1796875,-0.2578125,-0.4140625),(-0.1796875,-0.2578125,-0.4140625),
	(0.2890625,-0.3828125,-0.7109375),(-0.2890625,-0.3828125,-0.7109375),(0.25,-0.390625,-0.5),
	(-0.25,-0.390625,-0.5),(0.328125,-0.3984375,-0.9140625),(-0.328125,-0.3984375,-0.9140625),
	(0.140625,-0.3671875,-0.7578125),(-0.140625,-0.3671875,-0.7578125),(0.125,-0.359375,-0.5390625),
	(-0.125,-0.359375,-0.5390625),(0.1640625,-0.4375,-0.9453125),(-0.1640625,-0.4375,-0.9453125),
	(0.21875,-0.4296875,-0.28125),(-0.21875,-0.4296875,-0.28125),(0.2109375,-0.46875,-0.2265625),
	(-0.2109375,-0.46875,-0.2265625),(0.203125,-0.5,-0.171875),(-0.203125,-0.5,-0.171875),
	(0.2109375,-0.1640625,-0.390625),(-0.2109375,-0.1640625,-0.390625),(0.296875,0.265625,-0.3125),
	(-0.296875,0.265625,-0.3125),(0.34375,0.5390625,-0.1484375),(-0.34375,0.5390625,-0.1484375),
	(0.453125,0.3828125,0.8671875),(-0.453125,0.3828125,0.8671875),(0.453125,0.0703125,0.9296875),
	(-0.453125,0.0703125,0.9296875),(0.453125,-0.234375,0.8515625),(-0.453125,-0.234375,0.8515625),
	(0.4609375,-0.4296875,0.5234375),(-0.4609375,-0.4296875,0.5234375),(0.7265625,-0.3359375,0.40625),
	(-0.7265625,-0.3359375,0.40625),(0.6328125,-0.28125,0.453125),(-0.6328125,-0.28125,0.453125),
	(0.640625,-0.0546875,0.703125),(-0.640625,-0.0546875,0.703125),(0.796875,-0.125,0.5625),
	(-0.796875,-0.125,0.5625),(0.796875,0.1171875,0.6171875),(-0.796875,0.1171875,0.6171875),
	(0.640625,0.1953125,0.75),(-0.640625,0.1953125,0.75),(0.640625,0.4453125,0.6796875),
	(-0.640625,0.4453125,0.6796875),(0.796875,0.359375,0.5390625),(-0.796875,0.359375,0.5390625),
	(0.6171875,0.5859375,0.328125),(-0.6171875,0.5859375,0.328125),(0.484375,0.546875,0.0234375),
	(-0.484375,0.546875,0.0234375),(0.8203125,0.203125,0.328125),(-0.8203125,0.203125,0.328125),
	(0.40625,-0.1484375,-0.171875),(-0.40625,-0.1484375,-0.171875),(0.4296875,0.2109375,-0.1953125),
	(-0.4296875,0.2109375,-0.1953125),(0.890625,0.234375,0.40625),(-0.890625,0.234375,0.40625),
	(0.7734375,0.125,-0.140625),(-0.7734375,0.125,-0.140625),(1.0390625,0.328125,-0.1015625),
	(-1.0390625,0.328125,-0.1015625),(1.28125,0.4296875,0.0546875),(-1.28125,0.4296875,0.0546875),
	(1.3515625,0.421875,0.3203125),(-1.3515625,0.421875,0.3203125),(1.234375,0.421875,0.5078125),
	(-1.234375,0.421875,0.5078125),(1.0234375,0.3125,0.4765625),(-1.0234375,0.3125,0.4765625),
	(1.015625,0.2890625,0.4140625),(-1.015625,0.2890625,0.4140625),(1.1875,0.390625,0.4375),
	(-1.1875,0.390625,0.4375),(1.265625,0.40625,0.2890625),(-1.265625,0.40625,0.2890625),
	(1.2109375,0.40625,0.078125),(-1.2109375,0.40625,0.078125),(1.03125,0.3046875,-0.0390625),
	(-1.03125,0.3046875,-0.0390625),(0.828125,0.1328125,-0.0703125),(-0.828125,0.1328125,-0.0703125),
	(0.921875,0.21875,0.359375),(-0.921875,0.21875,0.359375),(0.9453125,0.2890625,0.3046875),
	(-0.9453125,0.2890625,0.3046875),(0.8828125,0.2109375,-0.0234375),(-0.8828125,0.2109375,-0.0234375),
	(1.0390625,0.3671875,0.0),(-1.0390625,0.3671875,0.0),(1.1875,0.4453125,0.09375),
	(-1.1875,0.4453125,0.09375),(1.234375,0.4453125,0.25),(-1.234375,0.4453125,0.25),
	(1.171875,0.4375,0.359375),(-1.171875,0.4375,0.359375),(1.0234375,0.359375,0.34375),
	(-1.0234375,0.359375,0.34375),(0.84375,0.2109375,0.2890625),(-0.84375,0.2109375,0.2890625),
	(0.8359375,0.2734375,0.171875),(-0.8359375,0.2734375,0.171875),(0.7578125,0.2734375,0.09375),
	(-0.7578125,0.2734375,0.09375),(0.8203125,0.2734375,0.0859375),(-0.8203125,0.2734375,0.0859375),
	(0.84375,0.2734375,0.015625),(-0.84375,0.2734375,0.015625),(0.8125,0.2734375,-0.015625),
	(-0.8125,0.2734375,-0.015625),(0.7265625,0.0703125,0.0),(-0.7265625,0.0703125,0.0),
	(0.71875,0.171875,-0.0234375),(-0.71875,0.171875,-0.0234375),(0.71875,0.1875,0.0390625),
	(-0.71875,0.1875,0.0390625),(0.796875,0.2109375,0.203125),(-0.796875,0.2109375,0.203125),
	(0.890625,0.265625,0.2421875),(-0.890625,0.265625,0.2421875),(0.890625,0.3203125,0.234375),
	(-0.890625,0.3203125,0.234375),(0.8125,0.3203125,-0.015625),(-0.8125,0.3203125,-0.015625),
	(0.8515625,0.3203125,0.015625),(-0.8515625,0.3203125,0.015625),(0.828125,0.3203125,0.078125),
	(-0.828125,0.3203125,0.078125),(0.765625,0.3203125,0.09375),(-0.765625,0.3203125,0.09375),
	(0.84375,0.3203125,0.171875),(-0.84375,0.3203125,0.171875),(1.0390625,0.4140625,0.328125),
	(-1.0390625,0.4140625,0.328125),(1.1875,0.484375,0.34375),(-1.1875,0.484375,0.34375),
	(1.2578125,0.4921875,0.2421875),(-1.2578125,0.4921875,0.2421875),(1.2109375,0.484375,0.0859375),
	(-1.2109375,0.484375,0.0859375),(1.046875,0.421875,0.0),(-1.046875,0.421875,0.0),
	(0.8828125,0.265625,-0.015625),(-0.8828125,0.265625,-0.015625),(0.953125,0.34375,0.2890625),
	(-0.953125,0.34375,0.2890625),(0.890625,0.328125,0.109375),(-0.890625,0.328125,0.109375),
	(0.9375,0.3359375,0.0625),(-0.9375,0.3359375,0.0625),(1.0,0.3671875,0.125),(-1.0,0.3671875,0.125),
	(0.9609375,0.3515625,0.171875),(-0.9609375,0.3515625,0.171875),(1.015625,0.375,0.234375),
	(-1.015625,0.375,0.234375),(1.0546875,0.3828125,0.1875),(-1.0546875,0.3828125,0.1875),
	(1.109375,0.390625,0.2109375),(-1.109375,0.390625,0.2109375),(1.0859375,0.390625,0.2734375),
	(-1.0859375,0.390625,0.2734375),(1.0234375,0.484375,0.4375),(-1.0234375,0.484375,0.4375),
	(1.25,0.546875,0.46875),(-1.25,0.546875,0.46875),(1.3671875,0.5,0.296875),(-1.3671875,0.5,0.296875),
	(1.3125,0.53125,0.0546875),(-1.3125,0.53125,0.0546875),(1.0390625,0.4921875,-0.0859375),
	(-1.0390625,0.4921875,-0.0859375),(0.7890625,0.328125,-0.125),(-0.7890625,0.328125,-0.125),
	(0.859375,0.3828125,0.3828125),(-0.859375,0.3828125,0.3828125)]
	edges = []
	faces = [[46,0,2,44],[3,1,47,45],[44,2,4,42],[5,3,45,43],[2,8,6,4],[7,9,3,5],[0,10,8,2],
	[9,11,1,3],[10,12,14,8],[15,13,11,9],[8,14,16,6],[17,15,9,7],[14,20,18,16],[19,21,15,17],
	[12,22,20,14],[21,23,13,15],[22,24,26,20],[27,25,23,21],[20,26,28,18],[29,27,21,19],[26,32,30,28],
	[31,33,27,29],[24,34,32,26],[33,35,25,27],[34,36,38,32],[39,37,35,33],[32,38,40,30],[41,39,33,31],
	[38,44,42,40],[43,45,39,41],[36,46,44,38],[45,47,37,39],[46,36,50,48],[51,37,47,49],[36,34,52,50],
	[53,35,37,51],[34,24,54,52],[55,25,35,53],[24,22,56,54],[57,23,25,55],[22,12,58,56],[59,13,23,57],
	[12,10,62,58],[63,11,13,59],[10,0,64,62],[65,1,11,63],[0,46,48,64],[49,47,1,65],[60,64,48],
	[49,65,61],[62,64,60],[61,65,63],[60,58,62],[63,59,61],[60,56,58],[59,57,61],[60,54,56],[57,55,61],
	[60,52,54],[55,53,61],[60,50,52],[53,51,61],[60,48,50],[51,49,61],[88,173,175,90],[175,174,89,90],
	[86,171,173,88],[174,172,87,89],[84,169,171,86],[172,170,85,87],[82,167,169,84],[170,168,83,85],
	[80,165,167,82],[168,166,81,83],[78,91,145,163],[146,92,79,164],[91,93,147,145],[148,94,92,146],
	[93,95,149,147],[150,96,94,148],[95,97,151,149],[152,98,96,150],[97,99,153,151],[154,100,98,152],
	[99,101,155,153],[156,102,100,154],[101,103,157,155],[158,104,102,156],[103,105,159,157],
	[160,106,104,158],[105,107,161,159],[162,108,106,160],[107,66,67,161],[67,66,108,162],
	[109,127,159,161],[160,128,110,162],[127,178,157,159],[158,179,128,160],[125,155,157,178],
	[158,156,126,179],[123,153,155,125],[156,154,124,126],[121,151,153,123],[154,152,122,124],
	[119,149,151,121],[152,150,120,122],[117,147,149,119],[150,148,118,120],[115,145,147,117],
	[148,146,116,118],[113,163,145,115],[146,164,114,116],[113,180,176,163],[176,181,114,164],
	[109,161,67,111],[67,162,110,112],[111,67,177,182],[177,67,112,183],[176,180,182,177],
	[183,181,176,177],[134,136,175,173],[175,136,135,174],[132,134,173,171],[174,135,133,172],
	[130,132,171,169],[172,133,131,170],[165,186,184,167],[185,187,166,168],[130,169,167,184],
	[168,170,131,185],[143,189,188,186],[188,189,144,187],[184,186,188,68],[188,187,185,68],
	[129,130,184,68],[185,131,129,68],[141,192,190,143],[191,193,142,144],[139,194,192,141],
	[193,195,140,142],[138,196,194,139],[195,197,138,140],[137,70,196,138],[197,70,137,138],
	[189,143,190,69],[191,144,189,69],[69,190,205,207],[206,191,69,207],[70,198,199,196],
	[200,198,70,197],[196,199,201,194],[202,200,197,195],[194,201,203,192],[204,202,195,193],
	[192,203,205,190],[206,204,193,191],[198,203,201,199],[202,204,198,200],[198,207,205,203],
	[206,207,198,204],[138,139,163,176],[164,140,138,176],[139,141,210,163],[211,142,140,164],
	[141,143,212,210],[213,144,142,211],[143,186,165,212],[166,187,144,213],[80,208,212,165],
	[213,209,81,166],[208,214,210,212],[211,215,209,213],[78,163,210,214],[211,164,79,215],
	[130,129,71,221],[71,129,131,222],[132,130,221,219],[222,131,133,220],[134,132,219,217],
	[220,133,135,218],[136,134,217,216],[218,135,136,216],[216,217,228,230],[229,218,216,230],
	[217,219,226,228],[227,220,218,229],[219,221,224,226],[225,222,220,227],[221,71,223,224],
	[223,71,222,225],[223,230,228,224],[229,230,223,225],[224,228,226],[227,229,225],[182,180,233,231],
	[234,181,183,232],[111,182,231,253],[232,183,112,254],[109,111,253,255],[254,112,110,256],
	[180,113,251,233],[252,114,181,234],[113,115,249,251],[250,116,114,252],[115,117,247,249],
	[248,118,116,250],[117,119,245,247],[246,120,118,248],[119,121,243,245],[244,122,120,246],
	[121,123,241,243],[242,124,122,244],[123,125,239,241],[240,126,124,242],[125,178,235,239],
	[236,179,126,240],[178,127,237,235],[238,128,179,236],[127,109,255,237],[256,110,128,238],
	[237,255,257,275],[258,256,238,276],[235,237,275,277],[276,238,236,278],[239,235,277,273],
	[278,236,240,274],[241,239,273,271],[274,240,242,272],[243,241,271,269],[272,242,244,270],
	[245,243,269,267],[270,244,246,268],[247,245,267,265],[268,246,248,266],[249,247,265,263],
	[266,248,250,264],[251,249,263,261],[264,250,252,262],[233,251,261,279],[262,252,234,280],
	[255,253,259,257],[260,254,256,258],[253,231,281,259],[282,232,254,260],[231,233,279,281],
	[280,234,232,282],[66,107,283,72],[284,108,66,72],[107,105,285,283],[286,106,108,284],
	[105,103,287,285],[288,104,106,286],[103,101,289,287],[290,102,104,288],[101,99,291,289],
	[292,100,102,290],[99,97,293,291],[294,98,100,292],[97,95,295,293],[296,96,98,294],
	[95,93,297,295],[298,94,96,296],[93,91,299,297],[300,92,94,298],[307,308,327,337],
	[328,308,307,338],[306,307,337,335],[338,307,306,336],[305,306,335,339],[336,306,305,340],
	[88,90,305,339],[305,90,89,340],[86,88,339,333],[340,89,87,334],[84,86,333,329],[334,87,85,330],
	[82,84,329,331],[330,85,83,332],[329,335,337,331],[338,336,330,332],[329,333,339,335],
	[340,334,330,336],[325,331,337,327],[338,332,326,328],[80,82,331,325],[332,83,81,326],
	[208,341,343,214],[344,342,209,215],[80,325,341,208],[342,326,81,209],[78,214,343,345],
	[344,215,79,346],[78,345,299,91],[300,346,79,92],[76,323,351,303],[352,324,76,303],
	[303,351,349,77],[350,352,303,77],[77,349,347,304],[348,350,77,304],[304,347,327,308],
	[328,348,304,308],[325,327,347,341],[348,328,326,342],[295,297,317,309],[318,298,296,310],
	[75,315,323,76],[324,316,75,76],[301,357,355,302],[356,358,301,302],[302,355,353,74],
	[354,356,302,74],[74,353,315,75],[316,354,74,75],[291,293,361,363],[362,294,292,364],
	[363,361,367,365],[368,362,364,366],[365,367,369,371],[370,368,366,372],[371,369,375,373],
	[376,370,372,374],[313,377,373,375],[374,378,314,376],[315,353,373,377],[374,354,316,378],
	[353,355,371,373],[372,356,354,374],[355,357,365,371],[366,358,356,372],[357,359,363,365],
	[364,360,358,366],[289,291,363,359],[364,292,290,360],[73,359,357,301],[358,360,73,301],
	[283,285,287,289],[288,286,284,290],[283,289,359,73],[360,290,284,73],[72,283,73],[73,284,72],
	[293,295,309,361],[310,296,294,362],[309,311,367,361],[368,312,310,362],[311,381,369,367],
	[370,382,312,368],[313,375,369,381],[370,376,314,382],[347,349,385,383],[386,350,348,384],
	[317,383,385,319],[386,384,318,320],[297,299,383,317],[384,300,298,318],[299,343,341,383],
	[342,344,300,384],[341,347,383],[384,348,342],[299,345,343],[344,346,300],[313,321,379,377],
	[380,322,314,378],[315,377,379,323],[380,378,316,324],[319,385,379,321],[380,386,320,322],
	[349,351,379,385],[380,352,350,386],[323,379,351],[352,380,324],[399,387,413,401],
	[414,388,400,402],[399,401,403,397],[404,402,400,398],[397,403,405,395],[406,404,398,396],
	[395,405,407,393],[408,406,396,394],[393,407,409,391],[410,408,394,392],[391,409,411,389],
	[412,410,392,390],[409,419,417,411],[418,420,410,412],[407,421,419,409],[420,422,408,410],
	[405,423,421,407],[422,424,406,408],[403,425,423,405],[424,426,404,406],[401,427,425,403],
	[426,428,402,404],[401,413,415,427],[416,414,402,428],[317,319,443,441],[444,320,318,442],
	[319,389,411,443],[412,390,320,444],[309,317,441,311],[442,318,310,312],[381,429,413,387],
	[414,430,382,388],[411,417,439,443],[440,418,412,444],[437,445,443,439],[444,446,438,440],
	[433,445,437,435],[438,446,434,436],[431,447,445,433],[446,448,432,434],[429,447,431,449],
	[432,448,430,450],[413,429,449,415],[450,430,414,416],[311,447,429,381],[430,448,312,382],
	[311,441,445,447],[446,442,312,448],[441,443,445],[446,444,442],[415,449,451,475],
	[452,450,416,476],[449,431,461,451],[462,432,450,452],[431,433,459,461],[460,434,432,462],
	[433,435,457,459],[458,436,434,460],[435,437,455,457],[456,438,436,458],[437,439,453,455],
	[454,440,438,456],[439,417,473,453],[474,418,440,454],[427,415,475,463],[476,416,428,464],
	[425,427,463,465],[464,428,426,466],[423,425,465,467],[466,426,424,468],[421,423,467,469],
	[468,424,422,470],[419,421,469,471],[470,422,420,472],[417,419,471,473],[472,420,418,474],
	[457,455,479,477],[480,456,458,478],[477,479,481,483],[482,480,478,484],[483,481,487,485],
	[488,482,484,486],[485,487,489,491],[490,488,486,492],[463,475,485,491],[486,476,464,492],
	[451,483,485,475],[486,484,452,476],[451,461,477,483],[478,462,452,484],[457,477,461,459],
	[462,478,458,460],[453,473,479,455],[480,474,454,456],[471,481,479,473],[480,482,472,474],
	[469,487,481,471],[482,488,470,472],[467,489,487,469],[488,490,468,470],[465,491,489,467],
	[490,492,466,468],[463,491,465],[466,492,464],[391,389,503,501],[504,390,392,502],
	[393,391,501,499],[502,392,394,500],[395,393,499,497],[500,394,396,498],[397,395,497,495],
	[498,396,398,496],[399,397,495,493],[496,398,400,494],[387,399,493,505],[494,400,388,506],
	[493,501,503,505],[504,502,494,506],[493,495,499,501],[500,496,494,502],[495,497,499],
	[500,498,496],[313,381,387,505],[388,382,314,506],[313,505,503,321],[504,506,314,322],
	[319,321,503,389],[504,322,320,390]]

	for i in range(len(verts)):
		verts[i] = (verts[i][0]*radius, verts[i][1]*radius, verts[i][2]*radius)

	return verts, edges, faces



class Monkey(Primitive_Geometry_Class):
	def init(self):
		self.classname = "Monkey"
		self.finishon = 2
		""" Default Settings """
		self.auto_smooth_angle = 3.14159

	def create(self, ctx):
		mesh = get_monkey_mesh(0)
		self.create_mesh(ctx, mesh, self.classname)
		pd = self.data.primitivedata
		pd.classname = self.classname
		""" Apply Default Settings """
		self.data.auto_smooth_angle = self.auto_smooth_angle

	def update(self):
		pd = self.data.primitivedata
		mesh = get_monkey_mesh(pd.radius1)
		self.update_mesh(mesh)

	def abort(self):
		bpy.ops.object.delete({'selected_objects': [self.owner]})



class Create_OT_Monkey(Draw_Primitive):
	bl_idname = "create.monkey"
	bl_label = "Monkey"
	subclass = Monkey()

	def create(self, ctx):
		self.subclass.create(ctx)
		self.params = self.subclass.owner.data.primitivedata
		self.subclass.owner.location = self.gride.location
		self.subclass.owner.rotation_euler = self.gride.rotation

	def update(self, ctx, clickcount, dimension):
		if clickcount == 1:
			self.params.radius1 = dimension.radius
		if clickcount > 0:
			self.subclass.update()



def register_monkey():
	bpy.utils.register_class(Create_OT_Monkey)
	
def unregister_monkey():
	bpy.utils.unregister_class(Create_OT_Monkey)

if __name__ == "__main__":
	register_monkey()