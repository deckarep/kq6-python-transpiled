#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 410
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm410 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local100 = None
local101
local123 = [113, 121, 107, 129, 72, 129, 82, 121, 139, 129, 107, 129, 113, 121, 141, 121, 173, 129, 139, 129, 142, 121, 172, 121, 206, 129, 174, 129, 173, 121, 203, 121, 243, 129, 207, 129, 204, 121, 235, 121, 101, 139, 61, 139, 70, 130, 108, 130, 135, 139, 101, 139, 109, 129, 138, 130, 176, 139, 136, 139, 139, 130, 174, 130, 215, 139, 178, 139, 174, 130, 207, 130, 253, 139, 215, 139, 209, 130, 245, 130, 99, 140, 89, 154, 45, 154, 61, 140, 131, 154, 90, 154, 100, 139, 135, 140, 179, 154, 132, 154, 136, 139, 178, 140, 225, 154, 181, 154, 178, 139, 216, 140, 277, 154, 226, 154, 217, 140, 257, 140, 76, 171, 27, 168, 45, 154, 87, 155, 126, 169, 77, 170, 89, 155, 130, 155, 181, 166, 127, 169, 131, 155, 180, 155, 241, 171, 182, 165, 181, 155, 226, 155, 292, 166, 241, 171, 227, 155, 278, 155]
local283 = [91, 121, 156, 189, 222, 77, 115, 156, 194, 231, 69, 111, 159, 202, 244, 59, 105, 162, 212, 262]
local303 = [123, 123, 123, 123, 123, 134, 134, 134, 134, 134, 146, 146, 146, 146, 146, 166, 166, 166, 166, 166]
local323 = [1, 1, 4, 1, 3, 4, 2, 3, 4, 2, 0, 4, 5, 2, 0, 1, 3, 2, 5, 2]
local343 = [0, 8, 0, 0, 0, 9, 0, 7, 0, 3, 10, 0, 6, 4, 2, 0, 0, 5, 0, 0]
local363 = [5, 6, 6, 7, 8, 10, 10, 11, 12, 8, 0, 10, 11, 12, 13, 10, 10, 11, 12, 18]
local383 = [6, 7, 8, 8, 9, 6, 7, 13, 14, 14, 11, 12, 13, 14, 0, 16, 12, 13, 14, 14]
local403 = None
local404 = None
local405 = None
local406 = None
local407 = [104, 0, 1, 91, 78, 92, 124, 155, 186, 220, 236, 0, 0, 0, 8, 6]
local423 = [115, 0, 1, 102, 70, 85, 120, 155, 189, 225, 240, 1, 0, 0, 9, 6]
local439 = [127, 0, 1, 114, 50, 74, 115, 155, 196, 237, 268, 2, 0, 0, 12, 6]
local455 = [147, 0, 1, 134, 26, 58, 107, 155, 205, 253, 290, 3, 0, 0, 13, 6]
local471 = [104, 1, 0, 91, 236, 220, 186, 155, 124, 92, 78, 0, 0, 0, 8, 6]
local487 = [115, 1, 0, 102, 240, 225, 189, 155, 120, 85, 70, 1, 0, 0, 9, 6]
local503 = [127, 1, 0, 114, 268, 237, 196, 155, 115, 74, 50, 2, 0, 0, 12, 6]
local519 = [147, 1, 0, 134, 290, 253, 205, 155, 107, 58, 26, 3, 0, 0, 13, 6]
local535 = None
local536
local540 = None


@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, param4 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if 
		(and
			((param1 - 32) == param3)
			(param2 == (global0 x:))
			(<= (param4 - 10) param2 (param4 + 10))
		)
		return 1
	else:
		return 0
	#endif
#end:procedure

@SCI.procedure
def localproc_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 20): # inline for
		(local101[temp0] = (aTile new:)
			x: local283[temp0]
			y: local303[temp0]
			tileType: local323[temp0]
			tileCheck: local343[temp0]
			tilePointer: temp0
			setOnMeCheck:
				2
				((Polygon new:)
					type: 0
					init:
						local123[(temp0 * 8)]
						local123[((temp0 * 8) + 1)]
						local123[((temp0 * 8) + 2)]
						local123[((temp0 * 8) + 3)]
						local123[((temp0 * 8) + 4)]
						local123[((temp0 * 8) + 5)]
						local123[((temp0 * 8) + 6)]
						local123[((temp0 * 8) + 7)]
					yourself:
				)
			init:
		)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 20): # inline for
		(local101[temp0] dispose:)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_3():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	proc913_1(95)
	(global1 givePoints: 3)
#end:procedure

@SCI.instance
class rm410(KQ6Room):
	#property vars (may be empty)
	noun = 2
	picture = 410
	style = 10
	east = 400
	west = 400
	walkOffEdge = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						232
						123
						83
						123
						69
						134
						81
						136
						73
						144
						0
						144
						0
						0
						319
						0
						319
						146
						242
						146
						236
						138
						245
						134
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						66
						151
						46
						163
						27
						165
						5
						184
						298
						185
						307
						185
						283
						166
						263
						162
						249
						152
						319
						152
						319
						189
						0
						189
						0
						151
					yourself:
				)
		)
		(global1 handsOn:)
		(super init: &rest)
		if ((kernel.ScriptID(30, 0) prevEdgeHit:) == 2):
			local404 = 10
			local403 = 10
		else:
			local404 = 14
			local403 = 2
		#endif
		(kernel.ScriptID(30, 0) cue:)
		if (not proc913_0(1)):
			(global72 addToFront: self)
			(global73 addToFront: self)
		#endif
		(localproc_1)
		(kernel.ScriptID(30, 3) init:)
		(door init:)
		(backOfDoors init:)
		(hall init:)
		(global2 setScript: egoEnters)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not proc913_0(1)):
			(global72 delete: self)
			(global73 delete: self)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(or
				(and
					((param1 type:) & 0x0044)
					(or
						((param1 message:) == 1)
						((param1 message:) == 2)
						((param1 message:) == 3)
						((param1 message:) == 4)
						((param1 message:) == 5)
						((param1 message:) == 6)
						((param1 message:) == 7)
						((param1 message:) == 8)
					)
				)
				(and
					(User canInput:)
					((param1 type:) != 16384)
					(not (param1 modifiers:))
					(((param1 message:) == 13) or ((param1 type:) == 1))
					((global69 curIcon:) == (global69 at: 0))
				)
			)
			(param1 claimed: 1)
		else:
			(param1 claimed: 0)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc913_0(1):
			(cond
				case (global2 script:):#end:case
				case ((global0 onControl: 1) == 8192):
					(kernel.ScriptID(30, 0) prevEdgeHit: 2)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
				case ((global0 onControl: 1) == 16384):
					(kernel.ScriptID(30, 0) prevEdgeHit: 4)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
			)
		#endif
		(super doit:)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global91 say: 0 0 154 1 0 899)
		return 0
	#end:method

#end:class or instance

@SCI.instance
class aSpike(View):
	#property vars (may be empty)
	view = 412
	loop = 4
	signal = 18432
	
#end:class or instance

@SCI.instance
class aSandBlast(Prop):
	#property vars (may be empty)
	view = 412
	signal = 16384
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self dispose:)
	#end:method

#end:class or instance

class FloorTile(Feature):
	#property vars (may be empty)
	tileType = 0
	tilePointer = 0
	tileCheck = 0
	script = 0
	
	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(script):
			(script dispose:)
		#endif
		if param1:
			(param1 init: self &rest)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if (not proc913_0(1)):
			(global72 addToFront: self)
			(global73 addToFront: self)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not proc913_0(1)):
			(global72 delete: self)
			(global73 delete: self)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				match tileType
					case 0:
						(global91 say: 10 1 0 1)
					#end:case
					case 1:
						(global91 say: 4 1 0 1)
					#end:case
					case 2:
						(global91 say: 3 1 0 1)
					#end:case
					case 3:
						(global91 say: 5 1 0 1)
					#end:case
					case 4:
						(global91 say: 6 1 0 1)
					#end:case
					case 5:
						(global91 say: 7 1 0 1)
					#end:case
				#end:match
			#end:case
			case 5:
				(global91 say: 3 5 0 1)
			#end:case
			case 2:
				(global91 say: 3 2 0 1)
			#end:case
			else:
				(global91 say: 3 0 0 1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(User canInput:)
				((param1 type:) != 16384)
				(not (param1 modifiers:))
				(or
					(((param1 message:) == 13) and ((param1 type:) == 4))
					((param1 type:) == 1)
				)
				((global69 curIcon:) == (global69 at: 0))
				(self onMe: param1)
			)
			(param1 claimed: 1)
			local405 = local404
			local404 = (self tilePointer:)
			(global2 setScript: goToTile 0 local101[(self tilePointer:)])
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class goToTile(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(cond
					case ((local405 == 10) and (local404 == 14)):
						register = local101[11]
					#end:case
					case ((local405 == 14) and (local404 == 10)):
						register = local101[13]
					#end:case
				)
				if (local404 != local405):
					(global0
						setMotion: PolyPath (register x:) (register y:) self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				if (not (local404 == local405)):
					if ((register tileCheck:) == (local403 - 1)):
						local403.post('--')
					else:
						local403.post('++')
					#endif
				#endif
				if 
					(or
						((register tileCheck:) == local403)
						(local404 == local405)
					)
					(global1 handsOn:)
					(self dispose:)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				(global105 number: 300 setLoop: 1 play: self)
			#end:case
			case 3:
				(global91 say: 2 3 5 1 self)
			#end:case
			case 4:
				(global91 say: 2 3 5 2 self)
			#end:case
			case 5:
				(client setScript: fireAllSpikes 0 register)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class aTile(FloorTile):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class backOfDoors(Feature):
	#property vars (may be empty)
	noun = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setOnMeCheck: 1 2 4)
		(super init: &rest)
		if (not proc913_0(1)):
			(global72 addToFront: self)
			(global73 addToFront: self)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not proc913_0(1)):
			(global72 delete: self)
			(global73 delete: self)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(User canInput:)
				((param1 type:) != 16384)
				(not (param1 modifiers:))
				(((param1 message:) == 13) or ((param1 type:) == 1))
				((global69 curIcon:) == (global69 at: 0))
				(self onMe: param1)
			)
			(cond
				case ((global0 inRect: 59 140 86 153) and (global70 < 165)):
					(param1 claimed: 1)
					if 
						(and
							(not proc913_0(95))
							((kernel.ScriptID(30, 0) prevEdgeHit:) == 4)
						)
						(localproc_3)
					#endif
					(kernel.ScriptID(30, 0) prevEdgeHit: 4)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
				case ((global0 inRect: 229 142 261 151) and (global70 > 165)):
					(param1 claimed: 1)
					if 
						(and
							(not proc913_0(95))
							((kernel.ScriptID(30, 0) prevEdgeHit:) == 2)
						)
						(localproc_3)
					#endif
					(kernel.ScriptID(30, 0) prevEdgeHit: 2)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
				case 
					(and
						(not (global0 inRect: 229 142 261 151))
						(global70 > 165)
					):
					(param1 claimed: 1)
					local406 = 1
					(global2 setScript: doorDeathMsgPause 0 2)
				#end:case
				case 
					((not (global0 inRect: 59 140 86 153)) and (global70 < 165)):
					(param1 claimed: 1)
					local406 = 1
					(global2 setScript: doorDeathMsgPause 0 4)
				#end:case
				else:
					(param1 claimed: 0)
					(global2 handleEvent: param1)
				#end:else
			)
			(param1 claimed:)
			return
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class door(Feature):
	#property vars (may be empty)
	noun = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setOnMeCheck: 1 8 16384 128 8192)
		(super init: &rest)
		if (not proc913_0(1)):
			(global72 addToFront: self)
			(global73 addToFront: self)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not proc913_0(1)):
			(global72 delete: self)
			(global73 delete: self)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(User canInput:)
				((param1 type:) != 16384)
				(not (param1 modifiers:))
				(((param1 message:) == 13) or ((param1 type:) == 1))
				((global69 curIcon:) == (global69 at: 0))
				(self onMe: param1)
			)
			(cond
				case ((global0 inRect: 59 140 86 153) and (global70 < 165)):
					(param1 claimed: 1)
					if 
						(and
							(not proc913_0(95))
							((kernel.ScriptID(30, 0) prevEdgeHit:) == 4)
						)
						(localproc_3)
					#endif
					(kernel.ScriptID(30, 0) prevEdgeHit: 4)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
				case ((global0 inRect: 229 142 261 151) and (global70 > 165)):
					(param1 claimed: 1)
					if 
						(and
							(not proc913_0(95))
							((kernel.ScriptID(30, 0) prevEdgeHit:) == 2)
						)
						(localproc_3)
					#endif
					(kernel.ScriptID(30, 0) prevEdgeHit: 2)
					(global2 setScript: kernel.ScriptID(30, 2))
				#end:case
				case 
					(and
						(not (global0 inRect: 229 142 261 151))
						(global70 > 165)
					):
					(param1 claimed: 1)
					local406 = 1
					(global2 setScript: doorDeathMsgPause 0 2)
				#end:case
				case 
					((not (global0 inRect: 59 140 86 153)) and (global70 < 165)):
					(param1 claimed: 1)
					local406 = 1
					(global2 setScript: doorDeathMsgPause 0 4)
				#end:case
				else:
					(param1 claimed: 0)
					(global2 handleEvent: param1)
				#end:else
			)
			(param1 claimed:)
			return
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class hall(Feature):
	#property vars (may be empty)
	noun = 2
	nsBottom = 189
	nsRight = 319
	
#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if ((kernel.ScriptID(30, 0) prevEdgeHit:) == 2):
					(global0
						posn: 10 146
						init:
						actions: egoDoVerb
						illegalBits: 0
						ignoreActors:
						setScale: Scaler 100 99 190 0
						setMotion: PolyPath 69 146 self
					)
				else:
					(global0
						posn: 310 146
						init:
						actions: egoDoVerb
						illegalBits: 0
						ignoreActors:
						setScale: Scaler 100 99 190 0
						setMotion: PolyPath 244 146 self
					)
				#endif
			#end:case
			case 1:
				if ((kernel.ScriptID(30, 0) prevEdgeHit:) == 2):
					(global0 setHeading: 90)
				else:
					(global0 setHeading: 270)
				#endif
				(global1 handsOn:)
				(global69 enable: 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doorDeathMsgPause(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 2 3 7 1 self)
			#end:case
			case 1:
				temp0 = 0
				while (temp0 < 20): # inline for
					if (local404 == temp0):
						if (register == 2):
							local100 = local383[temp0]
						else:
							local100 = local363[temp0]
						#endif
					#endif
					# for:reinit
					temp0.post('++')
				#end:loop
				(cond
					case ((register == 2) and (local404 == 9)):
						local100 = 9
					#end:case
					case ((register == 4) and (local404 == 5)):
						local100 = 5
					#end:case
				)
				(global0
					setMotion:
						MoveTo
						(local101[local100] x:)
						(local101[local100] y:)
						self
				)
			#end:case
			case 2:
				cycles = 8
			#end:case
			case 3:
				(global105 number: 300 setLoop: 1 play:)
				(global91 say: 2 3 5 1 self)
			#end:case
			case 4:
				if (register == 2):
					(global0 setHeading: 90)
				else:
					(global0 setHeading: 270)
				#endif
				cycles = 10
			#end:case
			case 5:
				(global2 setScript: fireAllSpikes 0 local101[local100])
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fireAllSpikes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if ((global0 x:) < 135):
					match local540
						case 0:
							local535 = @local407
						#end:case
						case 1:
							local535 = @local455
						#end:case
						case 2:
							local535 = @local423
						#end:case
						else:
							local535 = @local439
						#end:else
					#end:match
				else:
					match local540
						case 0:
							local535 = @local471
						#end:case
						case 1:
							local535 = @local519
						#end:case
						case 2:
							local535 = @local487
						#end:case
						else:
							local535 = @local503
						#end:else
					#end:match
				#endif
				kernel.Memory(6, (local535 + 24), (register y:))
				kernel.Memory(6, (local535 + 26), (register x:))
				((aSandBlast new:)
					x: proc999_6(local535, 4)
					y: proc999_6(local535, 0)
					setLoop: proc999_6(local535, 1)
					cel: 1
					init:
					setScript: (aSpikeScript new:) 0 local535
				)
				ticks = kernel.Random(2, 6)
			#end:case
			case 1:
				if (local540.post('++') < 4):
					(state -= 2)
				#endif
				(self cue:)
			#end:case
			case 2:
				(global104 number: 410 setLoop: 1 play:)
				(localproc_2)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class aSpikeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				ticks = 4
			#end:case
			case 1:
				(client cel: 2)
				if 
					(localproc_0
						proc999_6(register, 12)
						proc999_6(register, 13)
						proc999_6(register, 3)
						proc999_6(register, 5)
					)
					(global2 setScript: killEgo)
					(client setCycle: End client)
				else:
					(local536[proc999_6(register, 11)] = (aSpike new:)
						x: proc999_6(register, 5)
						y: proc999_6(register, 3)
						cel: proc999_6(register, 2)
						setPri: proc999_6(register, 14)
						setLoop: 4
						init:
					)
					ticks = 4
				#endif
			#end:case
			case 2:
				(client cel: ((client cel:) + 1))
				if 
					(localproc_0
						proc999_6(register, 12)
						proc999_6(register, 13)
						proc999_6(register, 3)
						proc999_6(register, proc999_6(register, 15))
					)
					(global2 setScript: killEgo)
					(local536[proc999_6(register, 11)] dispose:)
					(client setCycle: End client)
				else:
					(local536[proc999_6(register, 11)]
						x: proc999_6(register, proc999_6(register, 15))
					)
					ticks = 4
				#endif
			#end:case
			case 3:
				kernel.Memory(6, (register + 30), (proc999_6(register, 15) + 1))
				if (proc999_6(register, 15) < 9):
					(state -= 2)
				#endif
				(self cue:)
			#end:case
			case 4:
				(local536[proc999_6(register, 11)] x: proc999_6(register, 10))
				ticks = 4
			#end:case
			case 5:
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class killEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if local406:
					(global91 say: 2 3 7 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global102 stop:)
				(global105 number: 411 setLoop: 1 play:)
				(cond
					case (((global0 x:) < 135) and ((global0 heading:) < 180)):
						temp0 = 1
						temp1 = 30
						temp2 = 5
					#end:case
					case (((global0 x:) < 135) and ((global0 heading:) >= 180)):
						temp0 = 2
						temp1 = 21
						temp2 = 6
					#end:case
					case (((global0 x:) >= 135) and ((global0 heading:) < 180)):
						temp0 = 3
						temp1 = -20
						temp2 = 7
					#end:case
					else:
						temp0 = 0
						temp1 = -28
						temp2 = 3
					#end:else
				)
				(global0
					view: 411
					normal: 0
					cel: 0
					cycleSpeed: 2
					setLoop: temp0
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
					setCycle: End self
				)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				proc0_1(37)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				return 0
			#end:case
			case 5:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			else:
				(global91 say: 0 0 154 1 0 899)
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

