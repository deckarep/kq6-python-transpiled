#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1009
import sci_sh
import Main
import Kq6Talker
import Kq6Window
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	tlkGateGuard1 = 14,
	tlkGateGuard2 = 15,
)

@SCI.instance
class tlkGateGuard1(Kq6Talker):
	#property vars (may be empty)
	x = 10
	y = 10
	view = 890
	cel = 1
	talkWidth = 190
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		y = x = 10
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		(cond
			case (global90 == 1):
				textY = 10
				(super init: 0 0 0 &rest)
			#end:case
			case ((global11 == 220) and (((ScriptID 220 3) y:) == 97)):
				textY = 0
				(gd1Mouth loop: 6)
				x = 91
				y = 58
				(super init: 0 0 gd1Mouth &rest)
			#end:case
			case ((global11 == 220) and (((ScriptID 220 3) y:) == 119)):
				textY = 0
				(gd1Mouth loop: 6)
				x = 102
				y = 80
				(super init: 0 0 gd1Mouth &rest)
			#end:case
			case 
				(and
					(global11 == 220)
					(((ScriptID 220 3) loop:) == 0)
					(((ScriptID 220 3) cel:) == 0)
				):
				textY = 0
				(gd1Mouth loop: 6)
				x = 95
				y = 71
				(super init: 0 0 gd1Mouth &rest)
			#end:case
			case (proc913_0 162):
				textY = 0
				(gd1Mouth loop: 6)
				x = 100
				y = 70
				(super init: 0 0 gd1Mouth &rest)
			#end:case
			else:
				(gd1Mouth loop: 4)
				x = 94
				y = 70
				textY = 0
				(super init: 0 0 gd1Mouth &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tlkGateGuard2(Kq6Talker):
	#property vars (may be empty)
	x = 20
	y = 10
	view = 890
	cel = 1
	talkWidth = 190
	textY = -10
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		x = 20
		y = 10
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		if ((global90 == 1) or (proc913_0 162)):
			textY = 10
			(super init: 0 0 0 &rest)
		else:
			x = 133
			y = 70
			textY = -10
			(super init: 0 0 gd2Mouth &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class gd1Mouth(Prop):
	#property vars (may be empty)
	view = 224
	loop = 4
	
#end:class or instance

@SCI.instance
class gd2Mouth(Prop):
	#property vars (may be empty)
	view = 224
	loop = 5
	
#end:class or instance

