#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 451
import sci_sh
import kernel
import Main
import rm450
import n913
import Conversation
import Scaler
import PolyPath
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc451_0 = 0,
)

@SCI.procedure
def proc451_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global2 setScript: boreTheOyster 0 param1)
#end:procedure

@SCI.instance
class boreTheOyster(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if register:
					(global91 say: 1 42 5 1 self 450)
				else:
					(global91 say: 1 42 1 1 self 451)
				#endif
			#end:case
			case 1:
				(global91 say: 1 42 1 2 self 451)
			#end:case
			case 2:
				(global0 setMotion: PolyPath 132 141 self)
			#end:case
			case 3:
				proc913_1(59)
				(global0
					view: 451
					loop: 0
					cel: 0
					posn: 115 143
					normal: 0
					cycleSpeed: 6
					setCycle: End self
				)
			#end:case
			case 4:
				cycles = 3
			#end:case
			case 5:
				(global0
					loop: 2
					cel: 0
					posn: 104 146
					cycleSpeed: 6
					setCycle: End self
				)
			#end:case
			case 6:
				(OI init:)
				(kernel.ScriptID(450, 1) hide: view: 2002)
				(global0 dispose:)
				seconds = 3
			#end:case
			case 7:
				(global1 handsOn:)
				(global69 disable: 0 3 4 5)
				(book setCycle: End self)
			#end:case
			case 8:
				(book cel: 0)
				cycles = 3
			#end:case
			case 9:
				(global91 say: 1 42 1 4 self 451)
			#end:case
			case 10:
				(book setCycle: End self)
			#end:case
			case 11:
				(book cel: 0)
				cycles = 3
			#end:case
			case 12:
				(pearl y: 184 z: 80)
				(global104 number: 961 setLoop: 1 play:)
				(insetOyster view: 4532 setLoop: 0 cycleSpeed: 1 setCycle: End)
				seconds = 2
			#end:case
			case 13:
				if global25:
					(global25 dispose:)
				#endif
				(insetOyster setCycle: Beg self)
			#end:case
			case 14:
				(pearl y: 104 z: 0)
				(insetOyster view: 453 setLoop: 1 cel: 0)
				seconds = 2
			#end:case
			case 15:
				(book setCycle: End self)
			#end:case
			case 16:
				(book cel: 0)
				cycles = 3
			#end:case
			case 17:
				(global91 say: 1 42 1 6 self 451)
			#end:case
			case 18:
				(pearl y: 184 z: 80)
				(global104 number: 961 setLoop: 1 play:)
				(insetOyster view: 4532 setLoop: 0 setCycle: End)
				seconds = 3
			#end:case
			case 19:
				if global25:
					(global25 dispose:)
				#endif
				(insetOyster setCycle: Beg self)
			#end:case
			case 20:
				(pearl y: 104 z: 0)
				(insetOyster view: 453 setLoop: 1)
				seconds = 2
			#end:case
			case 21:
				(book setCycle: End self)
			#end:case
			case 22:
				(book cel: 0)
				cycles = 3
			#end:case
			case 23:
				(global91 say: 1 42 1 8 self 451)
			#end:case
			case 24:
				(pearl y: 184 z: 80)
				(global104 number: 961 setLoop: 1 play:)
				(insetOyster view: 4532 setLoop: 0 setCycle: End)
				seconds = 6
			#end:case
			case 25:
				if global25:
					(global25 dispose:)
				#endif
				(insetOyster setCycle: Beg self)
			#end:case
			case 26:
				(pearl y: 104 z: 0)
				(insetOyster view: 453 setLoop: 1)
				seconds = 1
			#end:case
			case 27:
				(global1 handsOff:)
				(book setCycle: End self)
			#end:case
			case 28:
				(book cel: 0)
				cycles = 3
			#end:case
			case 29:
				(global104 setLoop: 5 play:)
				(insetOyster view: 4533 cycleSpeed: 0 setLoop: 5 setCycle: Fwd)
				seconds = 5
			#end:case
			case 30:
				if global25:
					(global25 dispose:)
				#endif
				(global91 say: 1 42 1 11 self 451)
			#end:case
			case 31:
				(OI dispose:)
				(kernel.ScriptID(450, 1)
					view: 4531
					setLoop: 2
					show:
					cycleSpeed: 50
					setCycle: End
				)
				(global0
					view: 451
					loop: 2
					cel: 2
					posn: 104 146
					cycleSpeed: 6
					normal: 0
					setScale: Scaler 100 30 126 70
					init:
				)
				cycles = 4
			#end:case
			case 32:
				(global91 say: 1 42 1 12 self 451)
			#end:case
			case 33:
				(global0
					view: 451
					loop: 0
					cel: 7
					posn: 115 143
					setCycle: Beg self
				)
			#end:case
			case 34:
				(global0 reset: 1 posn: 132 141)
				(global2 notify:)
				(kernel.ScriptID(40, 0) oysterDozing: 1)
				cycles = 6
			#end:case
			case 35:
				proc913_2(59)
				(global1 handsOn:)
				kernel.DisposeScript(1038)
				proc450_8(0)
				cycles = 4
			#end:case
			case 36:
				(self dispose:)
				kernel.DisposeScript(451)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grabPearl(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 givePoints: 1)
				(insetOyster setCycle: 0)
				(book dispose:)
				ticks = 4
			#end:case
			case 1:
				(global91 say: 4 5 0 1 self 451)
			#end:case
			case 2:
				(arm init: setCycle: CT 1 1 self)
			#end:case
			case 3:
				(pearl dispose:)
				(arm setCycle: End self)
			#end:case
			case 4:
				(arm dispose:)
				(insetOyster setCycle: Beg self)
			#end:case
			case 5:
				(insetOyster view: 4533 cycleSpeed: 3 setLoop: 5 setCycle: Fwd)
				seconds = 3
			#end:case
			case 6:
				(OI dispose:)
				proc913_2(59)
				(kernel.ScriptID(450, 1)
					view: 4531
					setLoop: 2
					cel: 0
					show:
					cycleSpeed: 50
					setCycle: End
				)
				(global0
					view: 451
					loop: 2
					cel: 2
					posn: 104 146
					cycleSpeed: 6
					normal: 0
					cycleSpeed: 6
					get: 30
					init:
					setScale: Scaler 100 30 126 70
					setCycle: Beg self
				)
			#end:case
			case 7:
				(global91 say: 4 5 0 2 self 451)
			#end:case
			case 8:
				(global104 number: 963 setLoop: 1 play:)
				(global2 notify:)
				(kernel.ScriptID(40, 0) oysterDozing: 1)
				(global0
					view: 451
					loop: 0
					cel: 7
					posn: 115 143
					cycleSpeed: 6
					setCycle: Beg self
				)
			#end:case
			case 9:
				(global0 reset: 1 posn: 132 141)
				cycles = 6
			#end:case
			case 10:
				(global91 say: 4 5 0 3 self 451)
			#end:case
			case 11:
				(global1 handsOn:)
				(global104 setLoop: 5 play:)
				proc450_8(0)
				cycles = 4
			#end:case
			case 12:
				(self dispose:)
				proc958_0(0, 1038, 451)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class almostGotScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(arm init: setCycle: CT 1 1 self)
			#end:case
			case 1:
				(arm setCycle: Beg self)
			#end:case
			case 2:
				(arm dispose:)
				cycles = 2
			#end:case
			case 3:
				(global91 say: 3 5 2 1 self 451)
			#end:case
			case 4:
				(global1 handsOn:)
				(global69 disable: 0 3 4 5)
				(insetOyster view: 453 setLoop: 1 cel: 0)
				(boreTheOyster start: 20)
				(global2 setScript: boreTheOyster)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class OI(View):
	#property vars (may be empty)
	x = 122
	y = 113
	noun = 2
	view = 453
	priority = 11
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			case 1:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global103 number: 450 setLoop: -1 play:)
		(global73 addToFront: self)
		(global72 addToFront: self)
		(book init:)
		(pearl init:)
		(botShell init:)
		(insetOyster init:)
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global73 delete: self)
		(global72 delete: self)
		(global2 cue:)
		(global103 fade: 0 10 10)
		(book dispose:)
		(insetOyster dispose:)
		(botShell dispose:)
		(pearl dispose:)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(not (param1 modifiers:))
				(or
					((param1 type:) & 0x0001)
					(((param1 message:) & 0x000d) and ((param1 type:) & 0x0004))
				)
				(not global92)
				(not global84)
				((param1 type:) != 16384)
				(not (self onMe: param1))
			)
			(param1 claimed: 1)
			(boreTheOyster start: 31 init:)
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class book(Prop):
	#property vars (may be empty)
	x = 198
	y = 87
	onMeCheck = 0
	view = 453
	loop = 2
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class arm(Prop):
	#property vars (may be empty)
	x = 198
	y = 87
	onMeCheck = 0
	view = 4532
	loop = 1
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class insetOyster(Prop):
	#property vars (may be empty)
	x = 63
	y = 171
	z = 70
	noun = 3
	view = 453
	loop = 1
	priority = 14
	signal = 16400
	cycleSpeed = 10
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			case 1:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class botShell(View):
	#property vars (may be empty)
	x = 87
	y = 180
	z = 90
	noun = 3
	view = 453
	cel = 1
	priority = 12
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			case 1:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pearl(Prop):
	#property vars (may be empty)
	x = 93
	y = 104
	noun = 4
	view = 453
	loop = 6
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if ((insetOyster cel:) != (insetOyster lastCel:)):
					(global1 handsOff:)
					(global2 setScript: almostGotScript)
				else:
					(global1 handsOff:)
					(global2 setScript: grabPearl)
				#endif
			#end:case
			case 1:
				(global91 say: noun param1 0 1 0 451)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

