#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 880
import sci_sh
import kernel
import Main
import rgCastle
import KQ6Print
import n913
import Inset
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm880 = 0,
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


@SCI.instance
class rm880(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 880
	horizon = 0
	vanishingX = 318
	vanishingY = 69
	minScaleSize = 95
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc958_0(128, 882, 881, 880)
		if 
			(and
				(kernel.ScriptID(80, 0) tstFlag: 711 512)
				(not (kernel.ScriptID(80, 0) tstFlag: 710 1))
				(not (kernel.ScriptID(80, 0) tstFlag: 709 2))
			)
			(kernel.ScriptID(80, 0) guardTimer: 0 setFlag: 710 1)
		#endif
		(self
			addObstacle:
				((Polygon new:)
					type: 3
					init:
						62
						70
						62
						135
						93
						143
						117
						148
						155
						148
						190
						149
						221
						143
						234
						134
						234
						125
						224
						116
						201
						108
						181
						104
						181
						70
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 100 118 119 115 132 113 143 117 143 125 110 125
					yourself:
				)
		)
		if ((global0 y:) <= 136):
			(global0 posn: 170 123)
		else:
			(global0 posn: 98 128)
		#endif
		(global0
			init:
			reset: 0
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		local0 = proc999_5(((global9 at: 26) owner:), 880, global0)
		(global32 add: roomFeatures pillar eachElementDo: #init)
		(portrait init: stopUpd:)
		if (((global9 at: 27) owner:) == 850):
			(bird init:)
		#endif
		if (((global9 at: 26) owner:) == 880):
			(nail init:)
		#endif
		(super init: &rest)
		(kernel.ScriptID(1015, 6) talkWidth: 150 x: 15 y: 20)
		(kernel.ScriptID(1015, 7) talkWidth: 135 x: 160 y: 20)
		(cond
			case (kernel.ScriptID(80, 0) tstFlag: 709 256):
				(kernel.ScriptID(80, 0) clrFlag: 709 256)
				(self setScript: enterRoomScr 0 guardsTakeBird)
			#end:case
			case (kernel.ScriptID(80, 0) tstFlag: 710 1):
				(self setScript: enterRoomScr 0 watchGuardsComeBack)
			#end:case
			case (((global9 at: 27) owner:) != 730):
				(kernel.ScriptID(80, 5)
					init:
					setPri: 5
					ignoreActors:
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 200 87
					setScript: guardsPatrol
				)
				(kernel.ScriptID(80, 6)
					init:
					setPri: 5
					ignoreActors:
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 212 87
				)
			#end:case
			else: 0#end:else
		)
		if (not script):
			(global1 handsOn:)
		#endif
		(kernel.ScriptID(80, 0) clrFlag: 711 256)
	#end:method

	@classmethod
	def warnUser(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(KQ6Print posn: -1 10 font: global22 say: 0 1 0 3 1 init:)
				(watchGuardsComeBack start: -1)
				if (not script):
					(self setScript: watchGuardsComeBack)
				else:
					if (global78 contains: portraitInset):
						(portraitInset dispose:)
					#endif
					(script next: watchGuardsComeBack)
				#endif
				(hideEgo caller: watchGuardsComeBack)
				((hideEgo caller:) setScript: waitForEgoToHide)
			#end:case
			case 1:
				(global91 say: 1 0 5 1)
				if (not script):
					(self setScript: waitedToLongToEscape)
				else:
					(script next: waitedToLongToEscape)
					if (global78 contains: portraitInset):
						(portraitInset dispose:)
					#endif
				#endif
			#end:case
			else:
				(super warnUser: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local6 = (global0 onControl: 1) & 0x4002):
			(self newRoom: 850)
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(80, 5) setScript: 0 setPri: -1)
		(kernel.ScriptID(80, 6) setPri: -1)
		(super dispose:)
	#end:method

	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(param1):
			if (hideEgo caller:):
				(waitForEgoToHide register: ((waitForEgoToHide register:) + 1))
				(param1 next: waitForEgoToHide)
				((hideEgo caller:) setScript: param1 &rest)
			else:
				(super setScript: param1 &rest)
			#endif
		else:
			(super setScript: param1 &rest)
		#endif
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		if (((global9 at: 27) owner:) != 730):
			(global91 say: 0 0 112 0 0 899)
		else:
			temp0 = 1
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class enterRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				match register
					case guardsTakeBird:
						(kernel.ScriptID(80, 0) setFlag: 711 128)
						(global91 say: 1 0 2 1 self)
					#end:case
					case watchGuardsComeBack:
						(global91 say: 1 0 3 1 self)
					#end:case
					else:
						cycles = 1
					#end:else
				#end:match
			#end:case
			case 2:
				(register start: -1)
				(global2 setScript: register)
				(hideEgo caller: register)
				(global1 handsOn:)
				((hideEgo caller:) setScript: waitForEgoToHide)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waitedToLongToEscape(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(964)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(80, 0) setFlag: 711 128)
				cycles = 4
			#end:case
			case 1:
				(global91 say: 1 0 5 2 self)
			#end:case
			case 2:
				(global91 say: 1 0 5 3 self)
			#end:case
			case 3:
				(self setScript: hideEgo self 1)
			#end:case
			case 4:
				seconds = 2
			#end:case
			case 5:
				(kernel.ScriptID(80, 5) setMotion: MoveTo 108 98)
				(kernel.ScriptID(80, 6) setMotion: MoveTo 79 114 self)
			#end:case
			case 6:
				(global91 say: 1 0 5 4 self)
			#end:case
			case 7:
				proc913_4(kernel.ScriptID(80, 6), kernel.ScriptID(80, 5), self)
			#end:case
			case 8:
				(global91 say: 1 0 5 5 self)
			#end:case
			case 9:
				(kernel.ScriptID(80, 5) setPri: -1)
				(kernel.ScriptID(80, 6) setPri: -1)
				(kernel.ScriptID(80, 5) setMotion: MoveTo 161 111 self)
				(kernel.ScriptID(80, 6) setMotion: DPath 94 129 122 128)
			#end:case
			case 10:
				(global91 say: 1 0 5 6 self)
			#end:case
			case 11:
				(global91 say: 1 0 5 7 self)
			#end:case
			case 12:
				(self setScript: hideEgo self)
			#end:case
			case 13:
				(global91 say: 1 0 5 8 self oneOnly: 0)
			#end:case
			case 14:
				(global2 moveOtherGuard: 1)
				(global2 spotEgo: proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkGuardsOutPartial(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if (not register):
			if (kernel.ScriptID(80, 0) tstFlag: 711 128):
				(kernel.ScriptID(80, 5) posn: 200 87)
				(kernel.ScriptID(80, 6) posn: 212 87)
			else:
				(kernel.ScriptID(80, 5) posn: 37 113)
				(kernel.ScriptID(80, 6) posn: 57 120)
			#endif
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if ((global0 x:) >= 126):
					local2 = 159
					local3 = 94
					local4 = 169
					local5 = 98
				else:
					local2 = 93
					local3 = 105
					local4 = 112
					local5 = 108
				#endif
				cycles = 1
			#end:case
			case 1:
				(kernel.ScriptID(80, 5)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					setMotion: MoveTo local2 local3
				)
				(kernel.ScriptID(80, 6)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					setMotion: MoveTo local4 local5 self
				)
			#end:case
			case 2:
				(kernel.ScriptID(80, 5) setPri: -1)
				(kernel.ScriptID(80, 6) setPri: -1)
				register = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeDownPicture(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 4 5 10 0 self)
			#end:case
			case 1:
				(nail init:)
				(portrait hide:)
				(global0
					view: 882
					setScale: 0
					scaleX: 128
					scaleY: 128
					loop: 1
					cel: 0
					x: 216
					y: 118
					cycleSpeed: 8
					normal: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(portrait show: posn: 214 111 stopUpd:)
				(global0 loop: 2 cel: 0 x: 216 y: 118 setCycle: End self)
			#end:case
			case 3:
				if ((next == waitForEgoToHide) or (not next)):
					(global1 handsOn:)
				#endif
				if (not proc913_1(87)):
					(global1 givePoints: 3)
				#endif
				local0 = 1
				(global0 reset: 6 posn: 205 112)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class replacePicture(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 4 5 12 0 self)
			#end:case
			case 1:
				(global0
					view: 882
					setScale: 0
					scaleX: 128
					scaleY: 128
					loop: 2
					cel: 4
					x: 216
					y: 118
					cycleSpeed: 8
					normal: 0
					setCycle: Beg self
				)
			#end:case
			case 2:
				(portrait hide:)
				(global0 loop: 1 cel: 6 x: 216 y: 118 setCycle: Beg self)
			#end:case
			case 3:
				(portrait posn: 223 87 show: stopUpd:)
				(nail dispose:)
				((global9 at: 26) owner: 0)
				if ((next == waitForEgoToHide) or (not next)):
					(global1 handsOn:)
				#endif
				local0 = 0
				(global0 reset: 6 posn: 205 112)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsTakeBird(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global1 givePoints: 2)
				(kernel.ScriptID(80, 0) clrFlag: 711 128)
				(self setScript: leaveConvScr self)
			#end:case
			case 1:
				(roomConv add: -1 1 0 2 2 add: -1 1 0 2 3 init: self)
			#end:case
			case 2:
				(self setScript: leaveConvScr self)
			#end:case
			case 3:
				(roomConv
					add: -1 1 0 2 4
					add: -1 1 0 2 5
					add: -1 1 0 2 6
					add: -1 1 0 2 7
					add: -1 1 0 2 8
					add: -1 1 0 2 9
					add: -1 1 0 2 10
					add: -1 1 0 2 11
					add: -1 1 0 2 12
					init: self
				)
			#end:case
			case 4:
				(self setScript: leaveConvScr self)
			#end:case
			case 5:
				(roomConv add: -1 1 0 2 13 10 10 init: self)
			#end:case
			case 6:
				(self setScript: hideEgo self)
			#end:case
			case 7:
				((global9 at: 27) owner: 730)
				(kernel.ScriptID(80, 0) guardTimer: 301 setFlag: 709 512)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class leaveConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		start = (state + 1)
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(80, 5)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 200 87
					setMotion: MoveTo 93 105 self
				)
				(kernel.ScriptID(80, 6)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 212 87
					setMotion: MoveTo 112 108 self
				)
			#end:case
			case 1: 0#end:case
			case 2:
				(kernel.ScriptID(80, 5) setHeading: 180 self)
			#end:case
			case 3:
				(self dispose:)
			#end:case
			case 4:
				(kernel.ScriptID(80, 5) setMotion: MoveTo 90 108 self)
			#end:case
			case 5:
				(kernel.ScriptID(80, 5) setHeading: 180 self)
			#end:case
			case 6:
				cycles = 4
			#end:case
			case 7:
				(kernel.ScriptID(80, 5) view: 884 loop: 0 cel: 0 setCycle: CT 5 1 self)
			#end:case
			case 8:
				(bird dispose:)
				(kernel.ScriptID(80, 5) setCycle: End self)
			#end:case
			case 9:
				(self dispose:)
			#end:case
			case 10:
				(global102 fadeTo: 700 -1)
				(kernel.ScriptID(80, 5)
					view: 724
					loop: 2
					setCycle: StopWalk -1
					setMotion: MoveTo 52 111
				)
				(kernel.ScriptID(80, 6) setMotion: MoveTo 52 120 self)
			#end:case
			case 11:
				(kernel.ScriptID(80, 5) dispose:)
				(kernel.ScriptID(80, 6) dispose:)
				state = -1
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class returningConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if param1:
			start = (state + 1)
		else:
			start = 0
		#endif
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 3
			#end:case
			case 1:
				(kernel.ScriptID(80, 5)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 37 113
					setMotion: MoveTo 93 105 self
				)
				(kernel.ScriptID(80, 6)
					init:
					setPri: 5
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 57 120
					setMotion: MoveTo 112 108 self
				)
			#end:case
			case 2: 0#end:case
			case 3:
				if proc999_5(((global9 at: 26) owner:), 880, global0):
					(state += 4)
				#endif
				(self cue:)
			#end:case
			case 4:
				proc913_4(kernel.ScriptID(80, 5), kernel.ScriptID(80, 6))
				proc913_4(kernel.ScriptID(80, 6), kernel.ScriptID(80, 5), self)
			#end:case
			case 5:
				(self dispose: 1)
			#end:case
			case 6:
				(kernel.ScriptID(80, 5) setHeading: 45)
				(kernel.ScriptID(80, 6) setHeading: 45 self)
			#end:case
			case 7:
				(self dispose: 1)
			#end:case
			case 8:
				if proc999_5(((global9 at: 26) owner:), 880, global0):
					(hideEgo caller: 0)
					caller = 0
					(global2 setScript: pictureDownGetEgo)
				else:
					(kernel.ScriptID(80, 5) setMotion: MoveTo 200 87 self)
					(kernel.ScriptID(80, 6) setMotion: MoveTo 212 87)
				#endif
			#end:case
			case 9:
				(self dispose: 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getNail(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		start = register = 0
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if register = (global0 has: 26):
					(global0 put: 26 880)
				#endif
				(global1 handsOff:)
				(global0
					view: 882
					loop: 3
					cel: 0
					x: 204
					y: 115
					normal: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					cycleSpeed: 8
					setCycle: CT 3 1 self
				)
			#end:case
			case 1:
				cycles = 5
			#end:case
			case 2:
				if register:
					(global91 say: 9 64 0 0 self)
					(nail init:)
				else:
					(global91 say: 7 5 0 0 self)
					(global0 get: 26)
					(nail dispose:)
				#endif
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(global0 reset: 6 posn: 204 110)
				if (not proc913_1(88)):
					(global1 givePoints: 1)
				#endif
				if ((next == waitForEgoToHide) or (not next)):
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtPicture(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					view: 882
					loop: 0
					cel: 0
					x: 201
					y: 122
					setScale: 0
					scaleX: 128
					scaleY: 128
					normal: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 1:
				seconds = 2
			#end:case
			case 2:
				(global91 say: 4 1 0 0 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(global69 disable: 0 1 3 4 5)
				(portraitInset init: self global2)
			#end:case
			case 4:
				(global1 handsOff:)
				register = 0
				(global0 setCycle: Beg self)
			#end:case
			case 5:
				(global0
					reset: 6
					posn: (portrait approachX:) (portrait approachY:)
				)
				if ((hideEgo caller:) or (not next)):
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hideEgo(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		register = 0
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(waitForEgoToHide register: 0)
				state.post('++')
				if 
					(= temp0
						(cond
							case 
								(and
									((global2 script:) != waitedToLongToEscape)
									(kernel.ScriptID(80, 0) tstFlag: 709 2)
								):
								state.post('--')
								15
							#end:case
							case (((global9 at: 27) owner:) == 850): 16#end:case
							case 
								(and
									(kernel.ScriptID(80, 0) tstFlag: 709 512)
									(not (kernel.ScriptID(80, 0) tstFlag: 710 1))
								):
								state.post('--')
								14
							#end:case
							else: 0#end:else
						)
					)
					(global91 say: 8 5 temp0 0 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				(global1 handsOn:)
				(self dispose:)
			#end:case
			case 2:
				if (register or register = ((global0 x:) >= 126)):
					start = 8
					(global0 setMotion: PolyPath 170 123 self)
				else:
					start = 9
					state = 4
					(global0 setMotion: PolyPath 98 128 self)
				#endif
			#end:case
			case 3:
				(global0 setHeading: 45 self)
			#end:case
			case 4:
				state = 6
				(global0
					view: 881
					setLoop: 4
					cel: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					x: 152
					y: 128
					normal: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 5:
				(global0
					view: 881
					setLoop: 0
					cel: 0
					x: 107
					y: 130
					normal: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					cycleSpeed: 8
				)
				cycles = 3
			#end:case
			case 6:
				(global0 setCycle: End self)
			#end:case
			case 7:
				if (client == global2):
					state = (start - 1)
					cycles = 10
				else:
					(self dispose:)
				#endif
			#end:case
			case 8:
				state = 12
				register = 1
				(global0 setCycle: Beg self)
			#end:case
			case 9:
				(global0 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 10:
				seconds = 2
			#end:case
			case 11:
				(global0 setCycle: Beg self)
			#end:case
			case 12:
				(global0 loop: 0 cel: 4 setCycle: Beg self)
			#end:case
			case 13:
				start = 0
				(global0 reset: 6)
				if register:
					(global0 posn: 170 123)
				else:
					(global0 posn: 98 128)
				#endif
				if (client == global2):
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsPatrol(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local6 & 0x4002):
			(global2 newRoom: 850)
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		start = 0
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				if (hideEgo client:):
					state.post('--')
					(hideEgo caller: self)
				else:
					(global91 say: 1 0 1 0 self)
					(kernel.ScriptID(80, 0) setFlag: 711 128)
				#endif
			#end:case
			case 2:
				(global1 handsOn:)
				(hideEgo caller: self)
				(self setScript: waitForEgoToHide)
			#end:case
			case 3:
				(global1 handsOff:)
				if register:
					state.post('++')
				#endif
				(self setScript: guardsWalk self)
			#end:case
			case 4:
				(global91 say: 1 0 6 2 self)
			#end:case
			case 5:
				if register:
					state.post('++')
					seconds = 3
				else:
					seconds = 2
				#endif
			#end:case
			case 6:
				(global91 say: 1 0 6 3 self)
			#end:case
			case 7:
				(kernel.ScriptID(80, 0) clrFlag: 711 128)
				if proc999_5(((global9 at: 26) owner:), 880, global0):
					(global2 setScript: pictureDownGetEgo)
				else:
					(self setScript: guardsWalk self)
				#endif
			#end:case
			case 8:
				if register:
					(global91 say: 1 0 8 2 self)
				else:
					(global91 say: 1 0 6 4 self)
				#endif
			#end:case
			case 9:
				(self setScript: hideEgo self)
			#end:case
			case 10:
				(global1 handsOn:)
				register = 1
				seconds = 8
			#end:case
			case 11:
				if (global2 script:):
					state.post('--')
					((global2 script:) caller: self)
				else:
					(global91 say: 1 0 7 0 self)
					(kernel.ScriptID(80, 0) setFlag: 711 128)
				#endif
			#end:case
			case 12:
				(hideEgo caller: self)
				(self setScript: waitForEgoToHide)
			#end:case
			case 13:
				(global1 handsOff:)
				state = 2
				(global91 say: 1 0 8 1 self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsWalk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if register:
					temp0 = 200
					temp1 = 87
					temp2 = 212
					temp3 = 87
				else:
					temp0 = 37
					temp1 = 113
					temp2 = 57
					temp3 = 120
				#endif
				(kernel.ScriptID(80, 5) setMotion: MoveTo temp0 temp1 self)
				(kernel.ScriptID(80, 6) setMotion: MoveTo temp2 temp3 self)
			#end:case
			case 1: 0#end:case
			case 2:
				register = (not register)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waitForEgoToHide(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		seconds = cycles = 0
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (register > 2):
					(self cue:)
				else:
					seconds = 7
				#endif
			#end:case
			case 1:
				(global1 handsOff:)
				if 
					(and
						(register <= 2)
						proc999_5((global2 script:), getNail, takeDownPicture, replacePicture, lookAtPicture)
					)
					state.post('--')
					((global2 script:) caller: self)
				else:
					temp0 = (hideEgo caller:)
					(hideEgo caller: 0)
					(global2 setScript: waitedTooLong 0 temp0)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waitedTooLong(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(self setScript: walkGuardsOutPartial self)
			#end:case
			case 1:
				(kernel.ScriptID(80, 6) setHeading: 180 self)
			#end:case
			case 2:
				match register
					case watchGuardsComeBack:
						(roomConv add: -1 1 0 21 1)
					#end:case
					case guardsTakeBird:
						(roomConv add: -1 1 0 20 1)
					#end:case
					else:
						(roomConv add: -1 1 0 17 1)
					#end:else
				#end:match
				(roomConv init: self)
			#end:case
			case 3:
				proc913_4(global0, kernel.ScriptID(80, 5), self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(roomConv add: -1 1 0 17 2 add: -1 1 0 17 3 init: self)
			#end:case
			case 6:
				if (global0 inRect: 57 117 124 169):
					(global2 setScript: getEgo)
				else:
					(global2 spotEgo: proc80_7())
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pictureDownGetEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				(self
					setScript:
						walkGuardsOutPartial
						self
						(not (kernel.ScriptID(80, 0) tstFlag: 711 128))
				)
			#end:case
			case 2:
				(kernel.ScriptID(80, 6) setHeading: 180 self)
			#end:case
			case 3:
				(global91 say: 1 0 19 1 self)
			#end:case
			case 4:
				(global91 say: 1 0 19 2 self)
			#end:case
			case 5:
				(self setScript: hideEgo self)
			#end:case
			case 6:
				(global91 say: 1 0 19 3 self)
			#end:case
			case 7:
				(global2 spotEgo: proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class nail(View):
	#property vars (may be empty)
	x = 226
	y = 60
	noun = 7
	approachX = 204
	approachY = 115
	view = 880
	loop = 1
	cel = 1
	priority = 6
	signal = 24593
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
		((global9 at: 26) owner: 880)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getNail)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bird(Prop):
	#property vars (may be empty)
	x = 95
	y = 110
	view = 880
	loop = 3
	signal = 24576
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: Fwd)
	#end:method

#end:class or instance

@SCI.instance
class portrait(View):
	#property vars (may be empty)
	heading = 180
	noun = 4
	sightAngle = 40
	view = 880
	loop = 2
	priority = 6
	signal = 28689
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if local0:
			(self posn: 214 111)
		else:
			(self posn: 223 87)
		#endif
		(super init: &rest)
		(self approachVerbs: 1 5)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				(super onMe: param1)
				(or
					(and
						((global69 curIcon:) == (global69 at: 2))
						approachX = 198
						approachY = 116
					)
					(approachX = 204 and approachY = 110)
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global2 setScript: lookAtPicture)
			#end:case
			case 5:
				(cond
					case (not local0):
						(global2 setScript: takeDownPicture)
					#end:case
					case (((global9 at: 26) owner:) == 880):
						(global2 setScript: replacePicture)
					#end:case
					else:
						(global91 say: noun param1 13)
					#end:else
				)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
		approachX = approachY = _approachVerbs = 0
		(return
			(or
				((not proc999_4(71, 39, 251, 144, param1)) and noun = 6)
				(and
					(0x0004 & temp0)
					noun = 9
					(or
						(and
							((global69 curIcon:) == (global69 at: 4))
							((global69 curInvIcon:) == (global9 at: 26))
							approachX = 204
							approachY = 110
							_approachVerbs = -32768
						)
						1
					)
				)
				((0x0008 & temp0) and noun = 10)
				((0x4060 & temp0) and noun = 5)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match noun
			case 9:
				match param1
					case 64:
						(global2 setScript: getNail)
					#end:case
					else:
						(super doVerb: param1)
					#end:else
				#end:match
			#end:case
			case 5:
				match param1
					case 5:
						(global91 say: noun)
					#end:case
					else:
						if ((global66 doit: param1) == -32768):
							(global91 say: noun)
						else:
							(super doVerb: param1)
						#endif
					#end:else
				#end:match
			#end:case
			case 6:
				if ((global66 doit: param1) == -32768):
					param1 = 5
				#endif
				(super doVerb: param1)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pillar(Feature):
	#property vars (may be empty)
	x = 126
	y = 123
	noun = 8
	sightAngle = 40
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 5):
			(global1 handsOff:)
			if (hideEgo caller:):
				((hideEgo caller:) setScript: hideEgo)
			else:
				(global2 setScript: hideEgo 0)
			#endif
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class portraitInset(Inset):
	#property vars (may be empty)
	view = 880
	disposeNotOnMe = 1
	noun = 11
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (90 - (kernel.CelHigh(view, loop, cel) / 2))
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class getEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global102 stop:)
				(global103 number: 710 loop: -1 play:)
				(kernel.ScriptID(80, 5) setMotion: MoveTo 78 109 self)
				(kernel.ScriptID(80, 6) setLoop: 2 setMotion: MoveTo 100 120)
			#end:case
			case 1:
				(kernel.ScriptID(80, 5) setLoop: 2 setMotion: MoveTo 76 120 self)
			#end:case
			case 2:
				ticks = 30
			#end:case
			case 3:
				(global103 fade:)
				(rgCastle
					rFlag1: (| (rgCastle rFlag1:) 0x2000)
					dungeonEntered: 3
				)
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class watchGuardsComeBack(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				proc913_1(150)
				(kernel.ScriptID(1012, 32) talkWidth: 100 x: 160 y: 10)
				(kernel.ScriptID(80, 0) clrFlag: 710 1)
				cycles = 3
			#end:case
			case 1:
				(self setScript: returningConvScr self)
			#end:case
			case 2:
				(roomConv
					add: -1 1 0 3 2
					add: -1 1 0 3 3
					add: -1 1 0 3 4
					add: -1 1 0 3 5
					add: -1 1 0 3 6
					add: -1 1 0 3 7 -1 10
					init: self
				)
			#end:case
			case 3:
				(self setScript: returningConvScr self)
			#end:case
			case 4:
				(roomConv
					add: -1 1 0 3 8
					add: -1 1 0 3 9 -1 10
					add: -1 1 0 3 10
					add: -1 1 0 3 11
					add: -1 1 0 3 12 -1 10
					add: -1 1 0 3 13
					add: -1 1 0 3 14 -1 10
					add: -1 1 0 3 15
					add: -1 1 0 3 16 -1 10
					add: -1 1 0 3 17
					add: -1 1 0 3 18
					add: -1 1 0 3 19
					init: self
				)
			#end:case
			case 5:
				(self setScript: returningConvScr self)
			#end:case
			case 6:
				(roomConv add: -1 1 0 3 20 -1 10 init: self)
			#end:case
			case 7:
				(self setScript: hideEgo self)
			#end:case
			case 8:
				(kernel.ScriptID(80, 0) weddingRemind: 125 clrFlag: 709 512)
				(kernel.ScriptID(80, 0) clrFlag: 710 1 setFlag: 709 2)
				cycles = 3
			#end:case
			case 9:
				(global1 handsOn:)
				proc913_2(150)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

