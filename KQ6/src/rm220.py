#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 220
import sci_sh
import kernel
import Main
import rgCrown
import walkEgoInScr
import KQ6Print
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import DPath
import Rev
import Grooper
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm220 = 0,
	guardOpenDoorScr = 1,
	guardCloseDoorScr = 2,
	guard1 = 3,
	guard2 = 4,
	castleDoor = 5,
	saladin = 6,
	secondGuardDoorScr = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = 1
local4 = None


@SCI.instance
class rm220(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 220
	horizon = 0
	south = 210
	west = 230
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global2
			addObstacle:
				((Polygon new:)
					type: 0
					init: 60 229 -99 229 -99 124 119 122 150 135 154 149 54 189
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 30 138 134 138 134 149 30 149
					yourself:
				)
				((Polygon new:)
					type: 3
					init:
						-100
						289
						419
						289
						419
						176
						281
						178
						281
						168
						285
						168
						285
						163
						270
						163
						270
						167
						276
						167
						276
						178
						223
						165
						215
						158
						235
						150
						212
						145
						237
						133
						202
						126
						233
						116
						216
						110
						175
						116
						93
						116
						82
						112
						-100
						112
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 182 229 182 185 235 185 235 229
					yourself:
				)
		)
		proc958_0(128, 725, 224, 220)
		if (global0 has: 5):
			proc958_0(128, 221, 733)
		#endif
		(super init: &rest)
		proc913_1(162)
		(global0
			init:
			actions: egoDoVerbCode
			reset: 3
			setScale: Scaler 100 94 189 95
		)
		match global12
			case 150:
				(global0 reset: 2 hide:)
			#end:case
			case 230:
				proc12_1(12, 118)
			#end:case
			else:
				proc12_1(155, 184, 38)
			#end:else
		#end:match
		(castleDoor init:)
		(guard1 init:)
		(guard2 init:)
		(genericFeatures init:)
		(guardHut init:)
		(kernel.ScriptID(10, 4) onMeCheck: 1024 init:)
		(backOffScr client: guard1)
		(cond
			case (global12 == 150):
				(self setScript: kernel.ScriptID(221, 0))
			#end:case
			case (kernel.ScriptID(10, 0) isSet: 2):
				local2 = 1
				proc10_2(kernel.ScriptID(224, 0))
				if ((global153 == 3) and (not proc913_0(18))):
					proc913_1(135)
				#endif
			#end:case
			case 
				(or
					(and
						(global153 == 3)
						((not proc913_0(18)) or proc913_0(135))
					)
					((global153 == 5) and (global0 has: 5) and (not proc913_0(18)))
				):
				local2 = 1
				proc10_2(kernel.ScriptID(223, 0))
				proc913_2(135)
			#end:case
		)
		(global102 number: 220 loop: -1 play:)
		proc913_1(18)
	#end:method

	@classmethod
	def edgeToRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 3:
				proc12_0(param1, 38)
				0
			#end:case
			case 4:
				proc12_0(param1)
				0
			#end:case
			case 2:
				(self setScript: bumpedTheEdgeScr)
				0
			#end:case
			else:
				(super edgeToRoom: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			if (param1 == 1):
				(global91 say: noun param1 (23 if proc913_0(64) else 22))
				1
			else:
				(super doVerb: param1)
			#endif
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = proc999_4(106, 110, 140, 118, (global0 x:), (global0 y:))
		if ((local2 == 1) and (kernel.ScriptID(10, 0) isSet: 4096)):
			local2 = 0
			(global0 setHeading: 0)
		#endif
		(cond
			case script: 0#end:case
			case 
				(and
					((temp0 and (not local0)) or ((not temp0) and local0))
					(not (guard1 script:))
					(not (guard2 script:))
				):
				(global2 setScript: guardStanceScr)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose: &rest)
		kernel.DisposeScript(964)
		kernel.DisposeScript(969)
		if (global13 == 210):
			(global102 fadeTo: 917 -1)
		else:
			(global102 fade:)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setScript: 88)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 87:
				(global91 say: 0 0 1 0 0 899)
				return 1
			#end:case
			case 88:
				if (global0 inRect: 252 148 308 178):
					(global91 say: 7 0 16 1 0 0 0)
					return 0
				else:
					return 1
				#endif
			#end:case
			else:
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerbCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		match param1
			case 45:
				(global2 setScript: wearClothingScr)
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class bumpedTheEdgeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff: 1)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 1 0 24 0 self)
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardCloseDoorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(guard1
					view: 725
					setLoop: Grooper
					setCycle: Walk
					setMotion: MoveTo 108 97 self
				)
			#end:case
			case 1:
				(guard1 setHeading: 0 self)
			#end:case
			case 2:
				(castleDoor setCycle: Beg self)
			#end:case
			case 3:
				(global105 number: 223 loop: 1 play:)
				(guard1 setHeading: 180 self)
			#end:case
			case 4:
				(guard1 setMotion: MoveTo 100 109 self)
			#end:case
			case 5:
				(guard1 setHeading: 90 self)
			#end:case
			case 6:
				(guard1 view: 224 setLoop: -1 loop: 0 cel: 0)
				cycles = 2
			#end:case
			case 7:
				(guard1 stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardOpenDoorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(guard1
					view: 725
					setLoop: Grooper
					setCycle: Walk
					setMotion: MoveTo 112 105 self
				)
			#end:case
			case 1:
				(guard1 setMotion: MoveTo 108 97 self)
			#end:case
			case 2:
				(guard1 setHeading: 0 self)
			#end:case
			case 3:
				(castleDoor setCycle: End self)
				(global105 number: 222 loop: 1 play:)
			#end:case
			case 4:
				if (not register):
					(guard1 setMotion: MoveTo 108 92 self)
				else:
					(guard1 setMotion: MoveTo 90 97 self)
				#endif
			#end:case
			case 5:
				if (not register):
					(guard1
						setPri: 2
						setScale: Scaler 70 100 103 95
						setMotion: MoveTo 75 100 self
					)
				else:
					(guard1 setHeading: 90 self)
				#endif
			#end:case
			case 6:
				(client cue:)
			#end:case
			case 7:
				if (not register):
					(guard1 setMotion: MoveTo 108 92 self)
					(state += 3)
				#endif
				(guard1 setMotion: MoveTo 108 97 self)
			#end:case
			case 8:
				(guard1 setHeading: 0 self)
			#end:case
			case 9:
				(castleDoor setCycle: Beg self)
			#end:case
			case 10:
				(global105 number: 223 loop: 1 play:)
				(guard1 setHeading: 180 self)
			#end:case
			case 11:
				(guard1 setScale: 0 setPri: -1 setMotion: MoveTo 100 109 self)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				(guard1 setHeading: 90 self)
			#end:case
			case 14:
				(guard1 view: 224 setLoop: -1 loop: 0 cel: 0)
				cycles = 2
			#end:case
			case 15:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		register = 0
	#end:method

#end:class or instance

@SCI.instance
class guardStanceScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (local4 and (not (global0 isStopped:))):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 1:
				local4 = 0
				if (not local0):
					(guard1 loop: 2)
					(guard2 loop: 3)
					(guard1 setCycle: End)
					(guard2 setCycle: End self)
				else:
					(guard1 setCycle: Beg)
					(guard2 setCycle: Beg self)
				#endif
			#end:case
			case 2:
				if ((not local0) and (not register) and (not local1)):
					(cond
						case (not proc913_0(20)):
							(global91 say: 4 3 8 1 self)
						#end:case
						case 
							(or
								((global153 == 1) and proc913_0(72))
								(global153 > 1)
							):
							(global91 say: 4 3 17 1 self)
						#end:case
						else:
							(global91 say: 4 3 18 1 self)
						#end:else
					)
				else:
					(self cue:)
				#endif
				local1 = 0
			#end:case
			case 3:
				if ((guard1 cel:) == 0):
					(guard1 loop: 0)
					(guard2 loop: 1)
					local0 = 0
					proc913_1(162)
				else:
					local0 = 1
					proc913_2(162)
				#endif
				(guard1 stopUpd:)
				(guard2 stopUpd:)
				if register:
					(global78
						add: (CueObj client: guard1 state: 1 cue: yourself:)
					)
				#endif
				cycles = 2
			#end:case
			case 4:
				register = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wearClothingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(guardHut approachX:)
						(guardHut approachY:)
						self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global91 say: 2 45 0 1 self)
			#end:case
			case 3:
				(global0
					setSpeed: 6
					normal: 0
					view: 221
					loop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 4:
				cycles = 1
			#end:case
			case 5:
				(global0 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 6:
				cycles = 1
			#end:case
			case 7:
				(global0 view: 733 normal: 1 setCycle: Walk)
				cycles = 2
			#end:case
			case 8:
				proc913_1(59)
				(global91 say: 2 45 0 2 self)
			#end:case
			case 9:
				(global0 setMotion: MoveTo 277 181 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(KQ6Print
					font: global22
					posn: 195 65
					width: 100
					say: 0 2 45 0 3
					init: self
				)
			#end:case
			case 12:
				(global0 setMotion: PolyPath 125 118 self)
			#end:case
			case 13:
				(global0 setHeading: 0 self)
			#end:case
			case 14:
				ticks = 45
			#end:case
			case 15:
				(self setScript: secondGuardDoorScr self)
			#end:case
			case 16:
				(global91 say: 2 45 0 4 self)
			#end:case
			case 17:
				(KQ6Print font: global22 posn: -1 20 say: 0 2 45 0 5 init: self)
			#end:case
			case 18:
				(global1 givePoints: 4)
				(global0 ignoreActors: 1 setMotion: DPath 125 110 107 93 self)
			#end:case
			case 19:
				(global0
					setPri: 2
					setScale: Scaler 64 94 103 95
					moveSpeed: 8
					setMotion: MoveTo 75 100 self
				)
			#end:case
			case 20:
				(global0 hide:)
				(secondGuardDoorScr cue:)
			#end:case
			case 21:
				(global2 newRoom: 730)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class secondGuardDoorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(guard2
					view: 725
					posn: 139 108
					setLoop: Grooper
					loop: 1
					setCycle: Walk
					setMotion: DPath 120 108 108 97 self
				)
			#end:case
			case 1:
				(castleDoor setCycle: End self)
				(global105 number: 222 loop: 1 play:)
			#end:case
			case 2:
				(guard2 setMotion: MoveTo 129 96 self)
			#end:case
			case 3:
				(guard2 setHeading: 270 self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(guard2 stopUpd:)
				(client cue:)
			#end:case
			case 6:
				(guard2 startUpd: setMotion: MoveTo 108 97 self)
			#end:case
			case 7:
				(guard2 setHeading: 0 self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				(castleDoor setCycle: Beg self)
			#end:case
			case 10:
				(global105 number: 223 loop: 1 play:)
				(guard2 setMotion: DPath 120 108 139 109 self)
			#end:case
			case 11:
				(guard2 setHeading: 270 self)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				(guard2 view: 224 setLoop: -1 loop: 1 cel: 0 posn: 139 109)
				cycles = 2
			#end:case
			case 14:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardHutScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(guardHut approachX:)
						(guardHut approachY:)
						self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global0 setHeading: 0 self)
			#end:case
			case 3:
				ticks = 45
			#end:case
			case 4:
				(global0 setMotion: MoveTo 277 181 self)
			#end:case
			case 5:
				(global91 say: 6 5 0 0 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class castleDoor(Prop):
	#property vars (may be empty)
	x = 107
	y = 94
	noun = 4
	approachX = 122
	approachY = 115
	view = 220
	priority = 1
	signal = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (not local3):
					local4 = 1
					local3 = 1
					return
				#endif
				(cond
					case (not proc913_0(20)):
						(global91 say: 4 3 8 1 self)
					#end:case
					case 
						(or
							((global153 == 1) and proc913_0(72))
							(global153 > 1)
						):
						(global91 say: 4 3 17 1 self)
					#end:case
					else:
						(global91 say: 4 3 18 1 self)
					#end:else
				)
			#end:case
			case 2:
				(global91 say: noun param1)
			#end:case
			case 35:
				(global91 say: noun param1)
			#end:case
			case 1:
				if (cel == 0):
					(global91 say: noun 1 6)
				else:
					(global91 say: noun 1 7)
				#endif
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local4 = 0
		if (self onMe: param1):
			if 
				(or
					(and
						((global0 x:) == approachX)
						((global0 y:) == approachY)
					)
					proc999_4(106, 110, 140, 118, (global0 x:), (global0 y:))
				)
				local3 = 1
			else:
				local3 = 0
			#endif
		#endif
		(super handleEvent: param1 &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 5 stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class genericCoinShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if proc913_0(64):
					(global0
						setSpeed: 6
						normal: 0
						view: 221
						loop: 0
						cel: 0
						setCycle: End self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global91 say: 5 40 register 1 self)
			#end:case
			case 2:
				if proc913_0(64):
					(state += 3)
					(self cue:)
				else:
					(guardStanceScr register: 0)
					local1 = 1
					if (not (((global0 x:) == 125) and ((global0 y:) == 118))):
						(global0 setMotion: PolyPath 125 118 self)
					else:
						state.post('++')
						(self cue:)
					#endif
				#endif
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				if ((global2 script:) == guardStanceScr):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 5:
				(global0
					setSpeed: 6
					normal: 0
					view: 221
					loop: 0
					cel: 0
					setCycle: End self
				)
			#end:case
			case 6:
				if (not proc913_0(64)):
					(global91 say: 5 40 register 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 7:
				(global0 setCycle: Beg self)
			#end:case
			case 8:
				if (not proc913_0(64)):
					(global91 say: 5 40 register 3 self)
				else:
					(global91 say: 5 40 register 2 self oneOnly: 0)
				#endif
			#end:case
			case 9:
				if (not proc999_5(register, 8, 22)):
					(self cue:)
				else:
					state.post('++')
					(backOffScr client: self cue:)
				#endif
			#end:case
			case 10:
				(global0 reset: 7)
				cycles = 2
			#end:case
			case 11:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericGiveAllScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setSpeed: 6
					normal: 0
					view: 221
					loop: 0
					cel: 0
					setCycle: End self
				)
			#end:case
			case 1:
				register = 1
				(global91
					say:
						5
						0
						(cond
							case (proc913_0(72) or (global153 > 1)):
								register = 0
								17
							#end:case
							case (not proc913_0(20)): 8#end:case
							case ((global153 == 1) and proc913_0(20)): 18#end:case
						)
						0
						self
				)
			#end:case
			case 2:
				(global0 setCycle: Beg self)
			#end:case
			case 3:
				if register:
					(self cue:)
				else:
					state.post('++')
					(backOffScr client: self cue:)
				#endif
			#end:case
			case 4:
				(global0 reset: 7)
				cycles = 1
			#end:case
			case 5:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class backOffScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 reset: 7)
				cycles = 2
				(global78 add: self)
			#end:case
			case 1:
				(global0
					setCycle: Rev
					setLoop: 3
					setMotion: MoveTo 125 123 self
				)
			#end:case
			case 2:
				(global0 reset: 3)
				cycles = 2
			#end:case
			case 3:
				if ((global2 script:) == guardStanceScr):
					((global2 script:) caller: self)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(global78 delete: self)
				state = -1
				if (not (client == guard1)):
					(client cue:)
					client = guard1
				else:
					(global1 handsOn:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class notAct1NotNameScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				proc913_1(72)
				proc913_1(20)
				(global0 setHeading: 0 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global91 say: 5 register 12 1 self)
			#end:case
			case 3:
				if (register == 70):
					(global0
						normal: 0
						setSpeed: 6
						view: 221
						loop: 0
						cel: 0
						setCycle: End self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(roomConv add: -1 5 70 12 2 add: -1 5 70 12 3 init: self)
			#end:case
			case 6:
				if (register == 70):
					(global0 setCycle: Beg self)
				else:
					(state += 2)
					cycles = 2
				#endif
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(global0 reset: 3)
				cycles = 2
			#end:case
			case 9:
				(global91 say: 5 70 12 4 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(roomConv add: -1 5 70 12 5 add: -1 5 70 12 6 init: self)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				(backOffScr client: self cue:)
			#end:case
			case 14:
				(global91 say: 5 70 12 7 self)
			#end:case
			case 15:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((global0 loop:) != 9) or ((global0 cel:) != 3)):
					(global0 setHeading: 0 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				if ((register == 10) and local0):
					(global91 say: 5 2 register 2 self oneOnly: 0)
				else:
					(global91 say: 5 2 register 0 self)
				#endif
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

class GateGuardDog(Actor):
	#property vars (may be empty)
	noun = 5
	approachX = 125
	approachY = 118
	view = 224
	signal = 20481
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(global93 addToFront: self)
		(self approachVerbs: 2)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (super onMe: param1)
		if ((param1 message:) == 2):
			sightAngle = 26505
		else:
			sightAngle = 40
		#endif
		if temp0:
			temp1 = (global66 doit: 0)
			if 
				(and
					(not proc913_0(64))
					((global69 curIcon:) == (global69 useIconItem:))
					proc999_5((global69 curInvIcon:), (global9 at: 39), (global9
						at: 9
					))
				)
				(self _approachVerbs: ((~ temp1) & (self _approachVerbs:)))
			else:
				(self _approachVerbs: (| (self _approachVerbs:) temp1))
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super handleEvent: param1 &rest)
		if 
			(and
				(self onMe: param1)
				(not local0)
				(not ((param1 message:) == 3))
				(_approachVerbs & (global66 doit: (param1 message:)))
			)
			(guardStanceScr register: 1)
			(CueObj client: 0)
		else:
			(guardStanceScr register: 0)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 3:
				(global0 setMotion: PolyPath global70 (global71 - 10))
			#end:case
			case 2:
				(cond
					case (not proc913_0(64)):
						proc913_1(64)
						(self setScript: genericTalkScr 0 22)
					#end:case
					case 
						(or
							((global153 == 1) and proc913_0(72))
							((global153 > 1) and proc913_0(20))
						):
						(self setScript: genericTalkScr 0 17)
					#end:case
					case ((global153 == 1) and proc913_1(19)):
						if (kernel.ScriptID(10, 0) isSet: 8192):
							(self setScript: genericTalkScr 0 16)
						else:
							(kernel.ScriptID(10, 0) setIt: 8192)
							proc913_1(20)
							(self setScript: genericTalkScr 0 15)
						#endif
					#end:case
					case (global153 == 1):
						(self setScript: genericTalkScr 0 10)
					#end:case
					else:
						(self setScript: notAct1NotNameScr 0 param1)
					#end:else
				)
			#end:case
			case 70:
				if (not proc913_0(64)):
					(global91 say: noun param1 22)
				else:
					(cond
						case 
							(or
								proc913_0(72)
								((global153 > 1) and proc913_0(20))
							):
							(self setScript: genericGiveAllScr)
						#end:case
						case ((global153 == 1) and proc913_0(20)):
							proc913_1(162)
							(self setScript: kernel.ScriptID(222, 0) 0 18)
						#end:case
						case (global153 == 1):
							proc913_1(162)
							(self setScript: kernel.ScriptID(222, 0) 0 14)
						#end:case
						else:
							(self setScript: notAct1NotNameScr 0 param1)
						#end:else
					)
					proc913_1(19)
					proc913_1(20)
					(kernel.ScriptID(10, 0) setIt: 8192)
				#endif
			#end:case
			case 5:
				(global91 say: noun param1)
			#end:case
			case 1:
				(global91
					say:
						noun
						param1
						(cond
							case (not proc913_0(20)): 8#end:case
							case ((global153 == 1) and proc913_0(72)): 17#end:case
							case (global153 == 1): 18#end:case
							else: 17#end:else
						)
				)
			#end:case
			case 40:
				(cond
					case (not proc913_0(64)):
						(self setScript: genericCoinShowScr 0 22)
					#end:case
					case (not proc913_0(20)):
						(self setScript: genericCoinShowScr 0 8)
					#end:case
					case 
						(or
							((global153 == 1) and proc913_0(72))
							(global153 > 1)
						):
						(self setScript: genericGiveAllScr)
					#end:case
					case (not proc913_0(66)):
						(self setScript: genericCoinShowScr 0 20)
						proc913_1(66)
					#end:case
					else:
						(global91 say: noun param1 21)
					#end:else
				)
			#end:case
			else:
				(self setScript: genericGiveAllScr)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		(global93 delete: self)
	#end:method

#end:class or instance

@SCI.instance
class myHeadingCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param2 == CueObj) and ((CueObj client:) isKindOf: GateGuardDog)):
			param1 = 0
		#endif
		if argc:
			(global0 heading: param1)
		#endif
		if (global0 looper:):
			((global0 looper:)
				doit: global0 (global0 heading:) ((argc >= 2) and param2)
			)
		else:
			kernel.DirLoop(global0, (global0 heading:))
			if ((argc >= 2) and kernel.IsObject(param2)):
				(param2 cue: &rest)
			#endif
		#endif
		return param1
	#end:method

#end:class or instance

@SCI.instance
class guard1(GateGuardDog):
	#property vars (may be empty)
	x = 100
	y = 109
	
#end:class or instance

@SCI.instance
class guard2(GateGuardDog):
	#property vars (may be empty)
	x = 139
	y = 109
	sightAngle = 180
	loop = 1
	
#end:class or instance

@SCI.instance
class saladin(Actor):
	#property vars (may be empty)
	x = 75
	y = 100
	view = 736
	loop = 2
	xStep = 4
	
	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not argc):
			param1 = 0
		#endif
		(self
			setPri: 1
			setScale: Scaler 64 94 103 95
			moveSpeed: 8
			setMotion: MoveTo 75 100 param1
		)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self
			setScale: Scaler 64 94 103 95
			setPri: 1
			setLoop: Grooper
			setCycle: StopWalk -1
			ignoreActors:
		)
	#end:method

#end:class or instance

@SCI.instance
class guardHut(Feature):
	#property vars (may be empty)
	x = 280
	y = 170
	noun = 6
	sightAngle = 40
	onMeCheck = 16384
	approachX = 279
	approachY = 165
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 45:
				(global2 setScript: wearClothingScr)
			#end:case
			case 5:
				(global2 setScript: guardHutScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(genericFeatures x: (param1 x:) y: (param1 y:))
		(return
			(= noun
				match kernel.OnControl(4, (param1 x:), (param1 y:))
					case 8192: 8#end:case
					case 4096: 11#end:case
					case 2048: 9#end:case
					case 512: 12#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

