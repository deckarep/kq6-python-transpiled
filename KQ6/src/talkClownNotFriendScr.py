#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 277
import sci_sh
import kernel
import Main
import n913
import PolyPath
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	talkClownNotFriendScr = 0,
	talkClownFriendScr = 1,
	showClownScr = 2,
	showItemScr = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class talkClownNotFriendScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if proc913_0(78):
					register = 16
				else:
					proc913_1(78)
					register = 8
				#endif
				(global1 handsOff:)
				(global91 say: 10 2 register 1 self)
			#end:case
			case 1:
				(kernel.ScriptID(274, 0)
					setScript: 0
					view: 2721
					loop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global91 say: 10 2 register 2 self)
			#end:case
			case 3:
				(kernel.ScriptID(274, 0) setCycle: Beg self)
			#end:case
			case 4:
				(global1 handsOn:)
				(kernel.ScriptID(274, 0) setScript: kernel.ScriptID(274, 2))
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class talkClownFriendScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					setMotion:
						PolyPath
						(kernel.ScriptID(274, 0) approachX:)
						(kernel.ScriptID(274, 0) approachY:)
						self
				)
			#end:case
			case 1:
				(global0 setHeading: 270 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				register = (14 if (global153 == 3) else 15)
				(global91 say: 10 2 register 1 self)
			#end:case
			case 4:
				(kernel.ScriptID(274, 0)
					setScript: 0
					view: 274
					loop: 0
					cel: 0
					setCycle: CT 3 1 self
				)
			#end:case
			case 5:
				kernel.UnLoad(128, 2721)
				(kernel.ScriptID(270, 3) init:)
				cycles = 2
			#end:case
			case 6:
				(kernel.ScriptID(274, 0) setCycle: CT 5 1 self)
			#end:case
			case 7:
				(global91 say: 10 2 register 2 self)
			#end:case
			case 8:
				(global91 say: 10 2 register 3 self)
			#end:case
			case 9:
				(global91 say: 10 2 register 4 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(global91
					say:
						19
						0
						if (global153 == 3):
							28
						else:
							proc913_1(52)
							29
						#endif
						0
						self
				)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				if (global153 == 3):
					(global91 say: 10 2 register 5 self)
				else:
					cycles = 2
				#endif
			#end:case
			case 14:
				(kernel.ScriptID(274, 0) view: 274 loop: 0 cel: 5 setCycle: End self)
			#end:case
			case 15:
				(client setScript: kernel.ScriptID(274, 1))
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class showClownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(274, 0) setScript: 0)
				if register:
					local0 = register
				#endif
				register = (7 if proc913_0(10) else 8)
				(self setScript: showItemScr self)
			#end:case
			case 1:
				(global91 say: 10 0 register 1 self)
			#end:case
			case 2:
				(kernel.ScriptID(274, 0) view: 2721 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 3:
				if local0:
					(global91 say: 10 local0 0 0 self)
				else:
					(global91 say: 10 0 register 2 self)
				#endif
			#end:case
			case 4:
				(script cue:)
				(kernel.ScriptID(274, 0) setCycle: Beg)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global1 handsOn:)
				(kernel.ScriptID(274, 0) setScript: kernel.ScriptID(274, 2))
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		register = local0 = 0
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class showItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					setSpeed: 6
					normal: 0
					view: 272
					loop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 1:
				(client cue:)
			#end:case
			case 2:
				(global0 setCycle: Beg self)
			#end:case
			case 3:
				if register:
					(client cue:)
				else:
					cycles = 2
				#endif
			#end:case
			case 4:
				(global0
					posn:
						(kernel.ScriptID(274, 0) approachX:)
						(kernel.ScriptID(274, 0) approachY:)
					reset: 7
				)
				cycles = 2
			#end:case
			case 5:
				kernel.UnLoad(128, 272)
				register = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

