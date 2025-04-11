#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 286
import sci_sh
import Main
import rm280
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	ownerGiveScr = 0,
	alexGiveScr = 1,
	alexShowScr = 2,
	alexTakeMapScr = 3,
	genericShowScr = 4,
	fullMsgShowScr = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class ownerGiveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if register:
					((ScriptID 280 2) view: 286 loop: 1 cel: 0)
					cycles = 2
				else:
					(state += 4)
					(self cue:)
				#endif
			#end:case
			case 1:
				((ScriptID 280 2) setCycle: CT 2 1 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				((ScriptID 280 2) setCycle: Beg self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				((ScriptID 280 2) view: 284 loop: 2 cel: 0)
				cycles = 2
			#end:case
			case 6:
				((ScriptID 280 2) setCycle: CT 1 1 self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(global0
					normal: 0
					setSpeed: 6
					posn: 188 135
					view: 2811
					loop: 1
					setScale: 0
					cel: 0
				)
				cycles = 2
			#end:case
			case 9:
				(global0 setCycle: CT 2 1 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				((ScriptID 280 2) setCycle: Beg self)
				(global0 setCycle: End self)
			#end:case
			case 12: 0#end:case
			case 13:
				((ScriptID 280 2) view: 2841 loop: 0 cel: 0)
				(global0
					posn:
						((ScriptID 280 2) approachX:)
						((ScriptID 280 2) approachY:)
					view: 280
					loop: 7
					cel: 0
					setScale: Scaler 105 90 139 121
				)
				cycles = 2
			#end:case
			case 14:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 286)
	#end:method

#end:class or instance

@SCI.instance
class arm(Prop):
	#property vars (may be empty)
	x = 199
	y = 102
	view = 281
	priority = 15
	signal = 16
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class alexShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					normal: 0
					setSpeed: 6
					posn: 188 135
					view: 2811
					setScale: 0
					loop: 1
					cel: 0
				)
				if register:
					(arm
						loop:
							match register
								case 3: 5#end:case
								case 2: 6#end:case
								case 0: 7#end:case
								case 1: 8#end:case
							#end:match
						cel: 0
						init:
					)
				#endif
				cycles = 2
			#end:case
			case 1:
				(global0 setCycle: CT 2 1 self)
				if register:
					(arm setCycle: CT 2 1)
				#endif
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				if register:
					local0 = 1
					register = 0
				#endif
				(client cue:)
			#end:case
			case 4:
				if local0:
					(arm dispose:)
				#endif
				if register:
					(arm
						loop:
							match register
								case 3: 5#end:case
								case 2: 6#end:case
								case 0: 7#end:case
								case 1: 8#end:case
							#end:match
						cel: 2
						init:
					)
				#endif
				cycles = 2
			#end:case
			case 5:
				(global0 setCycle: End self)
				if register:
					(arm setCycle: End arm)
				#endif
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global0
					posn:
						((ScriptID 280 2) approachX:)
						((ScriptID 280 2) approachY:)
					view: 280
					loop: 7
					cel: 0
					setScale: Scaler 105 90 139 121
				)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (proc999_5 client fullMsgShowScr genericShowScr)):
			temp0 = 1
		else:
			temp0 = 0
		#endif
		(super dispose:)
		if temp0:
			(DisposeScript 286)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class alexGiveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					normal: 0
					setSpeed: 6
					posn: 188 135
					view: 2811
					loop: 1
					cel: 0
					setScale: 0
				)
				cycles = 2
			#end:case
			case 1:
				(global0 setCycle: CT 2 1 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(client cue:)
			#end:case
			case 4:
				((ScriptID 280 2) view: 284 loop: 2 cel: 0)
				cycles = 2
			#end:case
			case 5:
				((ScriptID 280 2) setCycle: CT 1 1 self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global0 setCycle: End self)
				if (register & 0x4000):
					((ScriptID 280 2) setCycle: End self)
				else:
					(state += 3)
					(self cue:)
				#endif
			#end:case
			case 8: 0#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(client cue:)
			#end:case
			case 11:
				((ScriptID 280 2) setCycle: Beg self)
			#end:case
			case 12:
				if (not (register & 0x4000)):
					0
				else:
					(self cue:)
				#endif
			#end:case
			case 13:
				cycles = 2
			#end:case
			case 14:
				if (register & 0x8000):
					((ScriptID 280 2)
						view: 286
						loop: 1
						cel: 1
						setCycle: CT 2 1 self
					)
				else:
					(state += 2)
					(self cue:)
				#endif
			#end:case
			case 15:
				cycles = 2
			#end:case
			case 16:
				((ScriptID 280 2) setCycle: Beg self)
			#end:case
			case 17:
				cycles = 2
			#end:case
			case 18:
				(global0
					posn:
						((ScriptID 280 2) approachX:)
						((ScriptID 280 2) approachY:)
					view: 280
					loop: 7
					cel: 0
					setScale: Scaler 105 90 139 121
				)
				((ScriptID 280 2) view: 280 loop: 8 cel: 0)
				cycles = 2
			#end:case
			case 19:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 286)
	#end:method

#end:class or instance

@SCI.instance
class alexTakeMapScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					normal: 0
					setSpeed: 6
					view: 2861
					posn: 199 143
					loop: 0
					setScale: 0
				)
				if (not register):
					(global0 cel: 0)
				else:
					(global0 cel: 4)
				#endif
				cycles = 2
			#end:case
			case 1:
				(global0 setCycle: CT 2 (-1 if register else 1) self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				if register:
					((ScriptID 280 1) init:)
				else:
					((ScriptID 280 1) dispose:)
				#endif
				cycles = 2
			#end:case
			case 4:
				if register:
					(global0 setCycle: Beg self put: 0)
				else:
					(global0 setCycle: End self get: 0)
				#endif
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global0
					posn:
						((ScriptID 280 2) approachX:)
						((ScriptID 280 2) approachY:)
					view: 280
					loop: 7
					cel: 0
					setScale: Scaler 105 90 139 121
				)
				ticks = 12
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 286)
	#end:method

#end:class or instance

@SCI.instance
class fullMsgShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc280_10 self)
				(global0 normal: 0 view: 280 loop: 7 cel: 0)
				cycles = 2
			#end:case
			case 1:
				(UnLoad 128 900)
			#end:case
			case 2:
				(self setScript: alexShowScr self)
			#end:case
			case 3:
				(global91 say: 4 register 0 1 alexShowScr)
			#end:case
			case 4:
				(global91 say: 4 register 0 2 self)
			#end:case
			case 5:
				(global0 reset: 0)
				((ScriptID 280 2) setScript: (ScriptID 280 9))
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 286)
	#end:method

#end:class or instance

@SCI.instance
class genericShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc280_10 self)
				(global0 normal: 0 view: 280 loop: 7 cel: 0)
				cycles = 2
			#end:case
			case 1:
				(UnLoad 128 900)
			#end:case
			case 2:
				(self setScript: alexShowScr self)
			#end:case
			case 3:
				if (not register):
					register = 0
				#endif
				(global91 say: 4 0 0 1 alexShowScr)
			#end:case
			case 4:
				(global91 say: 4 register 0 (2 if (register == 0) else 1) self)
			#end:case
			case 5:
				((ScriptID 280 2) setScript: (ScriptID 280 9))
				(global0 reset: 0)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 286)
	#end:method

#end:class or instance

