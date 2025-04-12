#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 802
import sci_sh
import kernel
import Main
import rm800
import Print
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	guardsScript = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class guardsScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global1 handsOn:)
		(super dispose:)
		kernel.DisposeScript(802)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91
					say: 6 1 (24 + (kernel.ScriptID(80, 0) tstFlag: 709 32)) 1 self
				)
			#end:case
			case 1:
				local0 = (global0 x:)
				local1 = (global0 y:)
				(global0
					normal: 0
					view: 802
					loop: 0
					cel: 0
					posn: 297 173
					setScale: 0
					scaleX: 128
					scaleY: 128
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 2:
				(global5 eachElementDo: #startUpd)
				cycles = 4
			#end:case
			case 3:
				(global69 disable:)
				(global5 eachElementDo: #hide)
				(global2 drawPic: 802 10)
				(background addToPic:)
				(guard1 init: stopUpd:)
				(guard2 init: stopUpd:)
				if (not (kernel.ScriptID(80, 0) tstFlag: 709 32)):
					(global1 givePoints: 2)
					(saladin init: stopUpd:)
				#endif
				cycles = 4
			#end:case
			case 4:
				(global69 enable:)
				if (not (kernel.ScriptID(80, 0) tstFlag: 709 32)):
					(self setScript: overHearGuards self)
				else:
					(self setScript: guardsNotHere self)
				#endif
			#end:case
			case 5:
				(background dispose:)
				(guard1 dispose: delete:)
				(guard2 dispose: delete:)
				(saladin dispose: delete:)
				proc800_1()
				(global0 setCycle: Beg self)
			#end:case
			case 6:
				(global69 enable:)
				(global0 posn: local0 local1 reset: 0)
				cycles = 2
			#end:case
			case 7:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class overHearGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(kernel.ScriptID(80, 0) setFlag: 709 32)
				cycles = 3
			#end:case
			case 1:
				(global91 say: 6 1 24 2 self oneOnly: 0)
			#end:case
			case 2:
				(Print
					font: global22
					width: 250
					posn: 20 139
					addText:
						r"""He was speakin' to that door--black magic, is what I say! I heard him say 'Ali', but then Bay came up and started yappin at me."""
					modeless: 1
					init:
				)
				seconds = 10
			#end:case
			case 3:
				if global25:
					(global25 dispose:)
				#endif
				cycles = 10
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsNotHere(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				(global91 say: 6 1 25 2 self oneOnly: 0)
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class background(View):
	#property vars (may be empty)
	x = 77
	y = 54
	view = 803
	signal = 16400
	
#end:class or instance

@SCI.instance
class guard1(View):
	#property vars (may be empty)
	x = 144
	y = 125
	view = 724
	loop = 4
	cel = 3
	scaleSignal = 1
	scaleX = 147
	scaleY = 147
	
#end:class or instance

@SCI.instance
class guard2(View):
	#property vars (may be empty)
	x = 127
	y = 110
	view = 726
	loop = 4
	scaleSignal = 1
	scaleX = 121
	scaleY = 121
	
#end:class or instance

@SCI.instance
class saladin(View):
	#property vars (may be empty)
	x = 167
	y = 110
	view = 736
	loop = 4
	cel = 2
	scaleSignal = 1
	scaleX = 112
	scaleY = 112
	
#end:class or instance

