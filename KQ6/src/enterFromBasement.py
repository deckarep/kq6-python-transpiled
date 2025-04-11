#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 732
import sci_sh
import kernel
import Main
import Conversation
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	enterFromBasement = 0,
)

@SCI.instance
class enterFromBasement(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 handsOff:)
		register = (kernel.ScriptID(80, 0) tstFlag: 709 2)
		if (not register):
			(kernel.ScriptID(1015, 6) talkWidth: 150 x: 15 y: 20)
			(kernel.ScriptID(1015, 7) talkWidth: 135 x: 160 y: 20)
			(kernel.ScriptID(80, 5) loop: 3 cel: 0 posn: 151 154 init:)
			(kernel.ScriptID(80, 6) loop: 0 cel: 0 posn: 133 146 init:)
			(global102 fadeTo: 700 -1)
		else:
			(global102 fade: 127 5 10 0)
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(732)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 10
			#end:case
			case 1:
				(global105 number: 901 loop: 1 play:)
				if (not register):
					state = 4
				#endif
				(kernel.ScriptID(730, 2) setCycle: CT 3 1 self)
			#end:case
			case 2:
				(EgoHead init:)
				seconds = 3
			#end:case
			case 3:
				(global91 say: 1 0 9 1 self)
			#end:case
			case 4:
				(EgoHead dispose:)
				seconds = 2
			#end:case
			case 5:
				(kernel.ScriptID(730, 2) setCycle: End self)
			#end:case
			case 6:
				(global105 stop:)
				(global0 setMotion: MoveTo 233 144 self)
			#end:case
			case 7:
				(kernel.ScriptID(730, 2) setCycle: Beg self)
			#end:case
			case 8:
				(global105 number: 902 loop: 1 play:)
				(kernel.ScriptID(730, 2) stopUpd:)
				if (not register):
					(self setScript: guardsCaptureEgo)
				else:
					(global91 say: 1 0 9 2 self)
				#endif
			#end:case
			case 9:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsCaptureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global102 stop:)
				(global103 number: 710 loop: -1 play:)
				(roomConv
					add: -1 1 0 7 1
					add: -1 1 0 7 2
					add: -1 1 0 7 3
					init: self
				)
			#end:case
			case 1:
				(global2 moveOtherGuard: 1)
				(kernel.ScriptID(80, 5) setScript: kernel.ScriptID(80, 4) self 1)
			#end:case
			case 2:
				(global91 say: 1 0 7 4 self oneOnly: 0)
			#end:case
			case 3:
				(global103 fade:)
				(kernel.ScriptID(80, 0) setFlag: 709 8192)
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class EgoHead(View):
	#property vars (may be empty)
	x = 248
	y = 113
	view = 730
	loop = 5
	
#end:class or instance

