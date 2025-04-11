#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 400
import sci_sh
import kernel
import Main
import rLab
import KQ6Print
import n401
import n402
import n403
import n404
import n913
import Print
import System

# Public Export Declarations
SCI.public_exports(
	LBRoom = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local100 = [-430, 1, -435, 7, -420, 20, -408, 51, -425, 66, -410, 68, -415, 71, -405, 117, -406, 152, -407, 180, -409, 181, -440, 182]


class LBRoom(LabRoom):
	#property vars (may be empty)
	@classmethod
	def makeDoors(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			proc999_5(param1, 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243)
			(kernel.ScriptID(30, 7) addToPic:)
		#endif
		if 
			proc999_5(param1, 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228)
			(kernel.ScriptID(30, 5) addToPic:)
			(kernel.ScriptID(30, 9) addToPic:)
		#endif
		if 
			proc999_5(param1, 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227)
			(kernel.ScriptID(30, 6) addToPic:)
			(kernel.ScriptID(30, 10) addToPic:)
		#endif
		if 
			(not
				proc999_5(param1, 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227)
			)
			(kernel.ScriptID(30, 8) addToPic:)
		#endif
		(kernel.ScriptID(30, 3) show:)
	#end:method

	@classmethod
	def makePolys(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 149, 177):
				proc401_4()
				(kernel.ScriptID(30, 4) dispose:)
			#end:case
			case proc999_5(param1, 67, 113, 115, 146, 131, 179, 213):
				proc403_0()
				(kernel.ScriptID(30, 4) dispose:)
			#end:case
			case proc999_5(param1, 147, 214, 227):
				proc403_1()
				(kernel.ScriptID(30, 0) initCrypt: 1)
			#end:case
			case proc999_5(param1, 22, 87, 117, 184):
				proc403_2()
				(kernel.ScriptID(30, 0) initCrypt: 2)
			#end:case
			case proc999_5(param1, 19, 85):
				proc403_3()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:case
			case proc999_5(param1, 35, 51, 97, 99, 101, 161, 163, 168, 193, 197, 200):
				proc402_0()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:case
			case 
				proc999_5(param1, 2, 20, 21, 66, 68, 82, 86, 114, 116, 148, 150, 151, 178, 215):
				proc402_1()
				(kernel.ScriptID(30, 0) initCrypt: 1)
			#end:case
			case proc999_5(param1, 216, 228):
				proc402_2()
				(kernel.ScriptID(30, 0) initCrypt: 2)
			#end:case
			case proc999_5(param1, 38, 209, 226):
				proc402_3()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:case
			case proc999_5(param1, 3, 69, 83, 152, 210):
				proc402_4()
				(kernel.ScriptID(30, 0) initCrypt: 2)
			#end:case
			case proc999_5(param1, 6, 81, 145, 212):
				proc402_5()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:case
			case 
				proc999_5(param1, 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243):
				proc401_0()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:case
			case 
				proc999_5(param1, 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227):
				proc401_1()
				(kernel.ScriptID(30, 0) initCrypt: 2)
			#end:case
			case 
				proc999_5(param1, 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228):
				proc401_2()
				(kernel.ScriptID(30, 0) initCrypt: 1)
			#end:case
			else:
				proc401_3()
				(kernel.ScriptID(30, 0) initCrypt: 4)
			#end:else
		)
	#end:method

	@classmethod
	def dumpPolys():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global2 obstacles:):
			((global2 obstacles:) dispose:)
		#endif
		(global2 obstacles: 0)
	#end:method

	@classmethod
	def calcRoom(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (temp1 = param1 < 0):
			temp0 = 0
			while local100[temp0]: # inline for
				if (param1 == local100[temp0]):
					temp1 = local100[(temp0 + 1)]
					match param2
						case 1:
							(temp1 -= 16)
						#end:case
						case 3:
							(temp1 += 16)
						#end:case
						case 2:
							temp1.post('++')
						#end:case
						case 4:
							temp1.post('--')
						#end:case
						else:
							proc921_0(r"""No oldDir coming in""")
						#end:else
					#end:match
					(kernel.ScriptID(30, 0) labCoords: temp1)
					return temp1
				#endif
				# for:reinit
				(temp0 += 2)
			#end:loop
			if (temp1 < 0):
				(KQ6Print
					addTextF:
						r"""Bad labyrinth room: room %d, direction %d"""
						temp1
						param2
				)
				temp1 = 117
				param2 = 3
				(global0 posn: 160 80)
			#endif
		#endif
		match param2
			case 1:
				(temp1 -= 16)
			#end:case
			case 3:
				(temp1 += 16)
			#end:case
			case 2:
				temp1.post('++')
			#end:case
			case 4:
				temp1.post('--')
			#end:case
			else:
				proc921_0(r"""No oldDir going out""")
			#end:else
		#end:match
		(kernel.ScriptID(30, 0) labCoords: temp1)
		temp0 = 1
		while (temp0 < 24): # inline for
			if (temp1 == local100[temp0]):
				return local100[(temp0 - 1)]
			#endif
			# for:reinit
			(temp0 += 2)
		#end:loop
		if proc999_5(temp1, 65, 103, 112, 130, 165, 183, 230):
			return -411
		#endif
		return temp1
	#end:method

	@classmethod
	def initPseudoRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: kernel.ScriptID(30, 12)):
			(kernel.ScriptID(30, 12) dispose:)
		#endif
		if (global5 contains: kernel.ScriptID(30, 13)):
			(kernel.ScriptID(30, 13) dispose:)
		#endif
		if proc913_0(48):
			(self drawPic: 98 10)
		else:
			(self drawPic: 98 -32761)
		#endif
		(self
			setScript: kernel.ScriptID(30, 1)
			makePolys: param1
			makeDoors: param1
			makeCritters:
		)
		if ((kernel.ScriptID(30, 0) holeCoords:) == (kernel.ScriptID(30, 0) labCoords:)):
			proc404_1()
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		if ((global102 number:) != 400):
			(global102 number: 400 setLoop: -1 play:)
		#endif
		if (global12 == 99):
			(kernel.ScriptID(30, 0) prevEdgeHit: 1)
			global12 = 405
		#endif
		if (global12 == 411):
			temp0 = (kernel.ScriptID(30, 0) labCoords:)
			match (kernel.ScriptID(30, 0) prevEdgeHit:)
				case 1:
					(temp0 -= 16)
				#end:case
				case 3:
					(temp0 += 16)
				#end:case
				case 2:
					temp0.post('++')
				#end:case
				case 4:
					temp0.post('--')
				#end:case
				else:
					proc921_0(r"""No oldDir coming in from 411""")
				#end:else
			#end:match
			(kernel.ScriptID(30, 0) labCoords: temp0)
		else:
			(= temp0
				(self calcRoom: (0 - global12) (kernel.ScriptID(30, 0) prevEdgeHit:))
			)
		#endif
		(self initPseudoRoom: temp0 (kernel.ScriptID(30, 0) prevEdgeHit:))
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (kernel.ScriptID(30, 0) holeIsUp:):
			(kernel.ScriptID(30, 0) holeIsUp: 0)
			proc404_2()
		#endif
		(self dumpPolys:)
		if 
			(<
				(= param1
					(self
						calcRoom:
							(kernel.ScriptID(30, 0) labCoords:)
							(kernel.ScriptID(30, 0) prevEdgeHit:)
					)
				)
				0
			)
			(super newRoom: -param1)
		else:
			(self initPseudoRoom: param1 (kernel.ScriptID(30, 0) prevEdgeHit:))
		#endif
	#end:method

#end:class or instance

