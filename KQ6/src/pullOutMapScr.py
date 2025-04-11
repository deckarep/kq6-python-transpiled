#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 130
import sci_sh
import Main
import n913
import PolyPath
import Feature
import Sound
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	pullOutMapScr = 0,
	MapScr = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7 = None
local8 = None
local9 = None
local10


@SCI.instance
class pullOutMapScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				temp0 = 0
				while (temp0 < 6): # inline for
					local10[temp0] = (((global69 at: temp0) signal:) & 0x0004)
					# for:reinit
					temp0++
				#end:loop
				(global1 handsOff:)
				(global69 disable:)
				(global91 say: 1 12 5 0 self 0)
			#end:case
			case 1:
				match global11
					case 200:
						if (not (global0 inRect: 93 98 284 183)):
							(global0 setMotion: PolyPath 182 126 self)
						else:
							cycles = 2
						#endif
					#end:case
					case 450:
						if (not (global0 inRect: 24 103 252 155)):
							(global0 setMotion: PolyPath 176 131 self)
						else:
							cycles = 2
						#endif
					#end:case
					case 550:
						if (not (global0 inRect: 0 79 274 133)):
							(global0 setMotion: PolyPath 167 101 self)
						else:
							cycles = 2
						#endif
					#end:case
					case 500:
						if (not (global0 inRect: 86 89 318 159)):
							(global0 setMotion: PolyPath 203 129 self)
						else:
							cycles = 2
						#endif
					#end:case
					else:
						cycles = 2
					#end:else
				#end:match
			#end:case
			case 2:
				if ((global0 cel:) != 2):
					(global0 setHeading: 180 self)
				else:
					cycles = 2
				#endif
			#end:case
			case 3:
				(global0
					normal: 0
					cycleSpeed: 10
					view: 207
					setLoop: 2
					cel: 0
					setCycle: End self
				)
			#end:case
			case 4:
				seconds = 2
			#end:case
			case 5:
				if next:
					((ScriptID 130 1) next: next)
					next = 0
				#endif
				(global2 setScript: (ScriptID 130 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

class MapScr(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = global5
		local1 = global32
		local2 = global10
		local3 = global73
		local4 = global72
		local6 = global93
		local7 = (global2 obstacles:)
		(global2 obstacles: ((List new:) add: yourself:))
		(global5 = (EventHandler new:) name: r"""newCast""" add:)
		(global32 = (EventHandler new:) name: r"""newFeatures""")
		(global10 = (EventHandler new:) name: r"""newATPs""" add:)
		(global73 = (EventHandler new:) name: r"""newMH""" add: self)
		(global72 = (EventHandler new:) name: r"""newKH""" add: self)
		(global93 = (EventHandler new:) name: r"""newWH""" add:)
		if register:
			(global9 hide:)
			register = 0
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def resetHandlers():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global73 delete: self dispose:)
		(global72 delete: self dispose:)
		(global93 delete: self dispose:)
		global73 = local3
		global72 = local4
		global93 = local6
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(not (param1 modifiers:))
				((param1 type:) & 0x0005)
				(not (param1 claimed:))
			)
			(cond
				case 
					(and
						(User canControl:)
						local8 = (global5 firstTrue: #onMe param1)
					):
					if (local8 == mistsProp):
						local8 = mists
					#endif
					(param1 claimed: 1)
					(local8 doVerb: ((global69 curIcon:) message:))
				#end:case
				case (User canControl:):
					(global32 delete: MapScr)
					local8 = (global32 firstTrue: #onMe param1)
					(param1 claimed: 1)
					(local8 doVerb: ((global69 curIcon:) message:))
				#end:case
			)
			return 1
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(DrawPic 130 10)
				(sacredMountain init:)
				(wonder init:)
				(crown init:)
				(beast init:)
				(northMarker init:)
				(mists init:)
				(mapTitle init:)
				(exitFeature init:)
				(theMap init:)
				(mapSound number: 130 loop: 1 play:)
				cycles = 10
			#end:case
			case 1:
				(global1 handsOn:)
				(global69 enable: disable: 0 3 4 5 6)
			#end:case
			case 2:
				if (global5 contains: mistsProp):
					(mistsProp dispose:)
				#endif
				if global25:
					(global25 dispose:)
				#endif
				(global1 setCursor: global21)
				(global5
					eachElementDo: #dispose
					eachElementDo: #delete
					release:
					dispose:
				)
				(global10 dispose:)
				(global32 delete: self dispose:)
				((global2 obstacles:) dispose:)
				(global2 obstacles: local7)
				global5 = local0
				global32 = local1
				global10 = local2
				(UnLoad 128 131)
				(DrawPic (global2 picture:) 100)
				if global10:
					(global10 doit:)
				#endif
				if register:
					(global69 enable: disable: 2 1)
					cycles = 15
				else:
					next = 0
					seconds = 2
				#endif
			#end:case
			case 3:
				if register:
					(global0
						normal: 0
						cycleSpeed: 10
						view: 207
						setLoop: 2
						lastCel:
						setCycle: Beg self
					)
				else:
					seconds = 2
				#endif
			#end:case
			case 4:
				if register:
					(global0 reset: 2)
					(global1 handsOn:)
					(global69 enable: 6)
					temp0 = 0
					while (temp0 < 6): # inline for
						if (local10[temp0] != 0):
							(global69 disable: (global69 at: temp0))
						#endif
						# for:reinit
						temp0++
					#end:loop
					(self dispose:)
				else:
					(mapSound loop: 1 number: 947 play:)
					(global0 cel: 0 setLoop: 0 setCycle: End self)
				#endif
			#end:case
			case 5:
				seconds = 1
			#end:case
			case 6:
				(global69 enable: enable: 6)
				(proc913_1 103)
				match (local8 tpRoom:)
					case 200:
						(global0 posn: 182 126)
					#end:case
					case 300:
						(global0 posn: 151 134)
					#end:case
					case 450:
						(global0 posn: 176 131)
					#end:case
					case 550:
						(global0 posn: 167 101)
					#end:case
					case 500:
						(global0 posn: 203 129)
					#end:case
				#end:match
				(global2 newRoom: (local8 tpRoom:))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theMap(Feature):
	#property vars (may be empty)
	noun = 6
	modNum = 130
	nsBottom = 200
	nsRight = 320
	
#end:class or instance

class HighliteMap(Feature):
	#property vars (may be empty)
	modNum = 130
	view = 0
	loop = 0
	tpRoom = 0
	theMapObj = 0
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local8 = self
		if (param1 == 5):
			(MapScr resetHandlers:)
		#endif
		(cond
			case ((param1 == 5) and (global11 == tpRoom)):
				(global69 enable:)
				(MapScr register: 1 cue:)
			#end:case
			case (param1 == 5):
				if (not (proc913_0 128)):
					(proc913_1 128)
					(global1 givePoints: 1)
				#endif
				(global91 say: noun param1 0 0 self 130)
				(global69 enable:)
				(global1 handsOff:)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(theMapObj = (Actor new:)
			view: view
			setPri: 15
			loop: loop
			illegalBits: 0
			ignoreActors: 1
			ignoreHorizon: 1
			posn: x y
			init:
			setCycle: End MapScr
		)
		(mapSound number: 131 loop: 1 play:)
	#end:method

#end:class or instance

@SCI.instance
class mistsProp(Prop):
	#property vars (may be empty)
	x = 256
	y = 142
	onMeCheck = 128
	view = 132
	loop = 2
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(mists doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class sacredMountain(HighliteMap):
	#property vars (may be empty)
	x = 156
	y = 49
	noun = 9
	onMeCheck = 2
	view = 131
	tpRoom = 300
	
#end:class or instance

@SCI.instance
class crown(HighliteMap):
	#property vars (may be empty)
	x = 124
	y = 129
	noun = 1
	onMeCheck = 8
	view = 131
	loop = 1
	tpRoom = 200
	
#end:class or instance

@SCI.instance
class wonder(HighliteMap):
	#property vars (may be empty)
	x = 82
	y = 81
	noun = 5
	onMeCheck = 4
	view = 132
	tpRoom = 450
	
#end:class or instance

@SCI.instance
class beast(HighliteMap):
	#property vars (may be empty)
	x = 213
	y = 92
	noun = 2
	onMeCheck = 16
	view = 132
	loop = 1
	tpRoom = 500
	
#end:class or instance

@SCI.instance
class mists(HighliteMap):
	#property vars (may be empty)
	x = 256
	y = 142
	noun = 3
	onMeCheck = 128
	view = 132
	loop = 2
	tpRoom = 550
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 3):
			(mistsLabel init:)
			(mistsProp init:)
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def onMe():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 3):
			noun = 3
		else:
			noun = 4
		#endif
		return (super onMe: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (proc913_0 3)
		(cond
			case ((param1 == 5) and temp0):
				(super doVerb: param1 &rest)
			#end:case
			case (and (param1 == 1) temp0 (not (proc913_0 80))):
				(proc913_1 80)
				(global91 say: noun param1 12 0 0 modNum)
			#end:case
			case ((param1 == 1) and temp0):
				(global91 say: noun param1 11 0 0 modNum)
			#end:case
			else:
				(global91 say: noun param1 0 0 0 modNum)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class northMarker(Feature):
	#property vars (may be empty)
	noun = 8
	modNum = 130
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 5):
			(global91 say: 6 param1 0 0 0 130)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class mapTitle(Feature):
	#property vars (may be empty)
	noun = 7
	modNum = 130
	onMeCheck = 64
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 5):
			(global91 say: 6 param1 0 0 0 130)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class mistsLabel(Actor):
	#property vars (may be empty)
	x = 207
	y = 156
	noun = 3
	view = 132
	loop = 3
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(mists doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class exitFeature(Feature):
	#property vars (may be empty)
	onMeCheck = 256
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(MapScr resetHandlers: register: 1 cue:)
	#end:method

#end:class or instance

@SCI.instance
class mapSound(Sound):
	#property vars (may be empty)
#end:class or instance

