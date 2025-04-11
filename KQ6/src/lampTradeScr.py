#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 11
import sci_sh
import Main
import n913
import Inset
import Scaler
import PolyPath
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	lampTradeScr = 2,
	talkToSellerScr = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class lampTradeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				((ScriptID 10 0) setIt: 16)
				if (not ((ScriptID 10 0) isSet: 4)):
					((ScriptID 10 0) setIt: 4)
					register = 22
				else:
					register = 23
				#endif
				(global91 say: 4 43 register 1 self 240)
			#end:case
			case 1:
				((ScriptID 241 0) setPri: -1 loop: 6 cel: 0 setCycle: End self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0 hide:)
				((ScriptID 241 0)
					view: 245
					loop: 2
					cel: 0
					posn: 41 128
					scaleX: 102
					scaleY: 102
					setScale:
					setSpeed: 6
					setCycle: End self
				)
			#end:case
			case 4:
				(global91 say: 4 43 register 2 self 240)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				((ScriptID 241 0) hide:)
				(global0
					show:
					normal: 0
					view: 247
					loop: 0
					cel: 0
					setSpeed: 6
					setCycle: End self
				)
			#end:case
			case 7:
				(global0 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 8:
				ticks = 60
			#end:case
			case 9:
				(lampSellerInset init: self global2)
			#end:case
			case 10:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 11:
				if (not local0):
					(global91 say: 39 0 0 1 self 240)
				else:
					(global91 say: 34 5 0 1 self 240)
				#endif
			#end:case
			case 12:
				if local0:
					cycles = 1
				else:
					(global0 reset: 1 loop: 9 cel: 1)
					((ScriptID 241 0)
						show:
						setScale: 0
						view: 2431
						loop: 6
						cel: 6
						setPri: 7
						posn: 19 128
						setCycle: Beg self
					)
					(state += 2)
				#endif
			#end:case
			case 13:
				(global0 hide:)
				((ScriptID 241 0)
					show:
					view: 245
					loop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				if (not local0):
					(global91 say: 39 0 0 2 self 240)
				else:
					state++
					(self cue:)
				#endif
			#end:case
			case 16:
				((ScriptID 241 0)
					setScale: 0
					posn: 19 128
					view: 2431
					loop: 6
					cel: ((ScriptID 241 0) lastCel:)
					setCycle: Beg self
				)
				(global0 reset: 1)
				(global1 handsOn:)
				(client setScript: (ScriptID 241 1))
			#end:case
			case 17:
				((ScriptID 241 0)
					posn: 19 128
					view: 243
					loop: 0
					setCycle: Walk
					setScale: Scaler 90 72 188 95
				)
				(global0 reset: 1)
				(client setScript: sealTheDealScr self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lamp(Prop):
	#property vars (may be empty)
	view = 245
	
#end:class or instance

@SCI.instance
class sealTheDealScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 34 5 0 2 self 240)
			#end:case
			case 1:
				(global91 say: 34 5 0 3 self 240)
			#end:case
			case 2:
				(global2 notify:)
				cycles = 2
			#end:case
			case 3:
				((ScriptID 241 0)
					moveSpeed: 3
					cycleSpeed: 3
					setMotion: PolyPath 274 187 self
				)
				(proc913_1 12)
			#end:case
			case 4:
				((ScriptID 241 0) loop: 0)
				cycles = 2
			#end:case
			case 5:
				((ScriptID 241 0)
					moveSpeed: 6
					cycleSpeed: 6
					view: 254
					loop: 0
					cel: 0
					setCycle: End self
				)
			#end:case
			case 6:
				((ScriptID 241 0) loop: 1 cel: 0 setCycle: Fwd self)
				seconds = 4
			#end:case
			case 7:
				(global91 say: 34 5 0 4 self 240)
			#end:case
			case 8:
				cycles = 3
			#end:case
			case 9:
				((ScriptID 241 0) loop: 0 cel: ((ScriptID 241 0) lastCel:))
				cycles = 2
			#end:case
			case 10:
				((ScriptID 241 0) setCycle: Beg self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				((ScriptID 241 0)
					moveSpeed: 3
					cycleSpeed: 3
					view: 243
					setCycle: Walk
					setMotion: MoveTo 274 230 self
				)
			#end:case
			case 13:
				(global1 handsOn:)
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToSellerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				((ScriptID 241 0) loop: 0 cel: 0 setCycle: 0)
				if (register == -1):
					(global0
						view: 272
						loop: 1
						cel: 0
						setSpeed: 6
						setCycle: End self
					)
				else:
					(global91 say: 4 2 register 0 self 240)
					(state += 4)
				#endif
			#end:case
			case 1:
				(global91 say: 4 0 0 0 self 240)
			#end:case
			case 2:
				(global0 setCycle: Beg self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global0 reset: 1)
				cycles = 2
			#end:case
			case 5:
				(global1 handsOn:)
				(client setScript: (ScriptID 241 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lampSellerInset(Inset):
	#property vars (may be empty)
	picture = 245
	hideTheCast = 1
	disposeNotOnMe = 1
	noun = 9
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return (proc999_4 83 48 232 136 (param1 x:) (param1 y:))
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script doit:)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self drawInset:)
		(super init: &rest)
		(lamps init:)
		(global1 handsOn:)
		(global69 disable: 0 3 4 5 6 curIcon: (global69 at: 1))
		(global1 setCursor: ((global69 curIcon:) cursor:))
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doVerb: param1 &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class lamps(Feature):
	#property vars (may be empty)
	y = 1
	onMeCheck = 118
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(= noun
				match (OnControl 4 (param1 x:) (param1 y:))
					case 2:
						(lampTradeScr register: 0)
						((global9 at: 25)
							message: 57
							noun: 25
							cel: 11
							setCursor: 990 1 11
						)
						34
					#end:case
					case 4:
						(lampTradeScr register: 3)
						((global9 at: 25)
							message: 56
							noun: 24
							loop: 2
							cel: 9
							setCursor: 990 2 9
						)
						7
					#end:case
					case 8:
						(lampTradeScr register: 4)
						((global9 at: 25)
							message: 58
							noun: 26
							cel: 13
							setCursor: 990 1 13
						)
						35
					#end:case
					case 16:
						(lampTradeScr register: 3)
						((global9 at: 25)
							message: 59
							noun: 27
							cel: 15
							setCursor: 990 1 15
						)
						36
					#end:case
					case 32:
						(lampTradeScr register: 4)
						((global9 at: 25)
							message: 60
							noun: 28
							cel: 14
							setCursor: 990 1 14
						)
						37
					#end:case
					case 64:
						((global9 at: 25)
							message: 96
							noun: 65
							cel: 12
							setCursor: 990 1 12
						)
						6
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global1 givePoints: 1)
				(global0 put: 19)
				(global1 handsOff:)
				(cond
					case (noun == 7):
						(global0 get: 25)
					#end:case
					case (not (global0 has: 25)):
						(global0 get: 25)
					#end:case
				)
				local0 = 1
				(lampSellerInset dispose:)
			#end:case
			else:
				if (param1 != 1):
					noun = 34
				#endif
				(global91 say: noun param1 0 0 0 240)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self sightAngle: 26505)
	#end:method

#end:class or instance

