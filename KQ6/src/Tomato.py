#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1051
import sci_sh
import kernel
import Main
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Tomato = 50,
)

@SCI.instance
class Tomato(Kq6Talker):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case ((global11 == 470) and (((global9 at: 49) owner:) == global11)):
				(self
					view: 475
					loop: 7
					x: 259
					y: 123
					textX: -239
					textY: -117
					talkWidth: 213
				)
				(super init: 0 0 tSwampMater &rest)
			#end:case
			case ((global11 == 470) and (global2 script:)):
				(self
					view: 474
					loop: 7
					x: 17
					y: 171
					textX: 3
					textY: -165
					talkWidth: 213
				)
				(super init: 0 0 tBumpMater &rest)
			#end:case
			case ((global11 == 480) and (((global9 at: 49) owner:) == global11)):
				(self
					view: 4802
					loop: 1
					x: 122
					y: 141
					textX: -74
					textY: -130
					talkWidth: 213
				)
				(super init: 0 0 tGroundMater &rest)
			#end:case
			else:
				(self
					view: 890
					loop: 0
					cel: 1
					x: 255
					y: 5
					textX: -209
					textY: 8
					talkWidth: 213
				)
				(super init: 0 0 0 &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 2004
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 21
	nsLeft = 25
	view = 2004
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 30
	nsLeft = 25
	view = 2004
	
#end:class or instance

@SCI.instance
class tBumpMater(Prop):
	#property vars (may be empty)
	view = 474
	loop = 7
	
#end:class or instance

@SCI.instance
class tSwampMater(Prop):
	#property vars (may be empty)
	view = 475
	loop = 7
	
#end:class or instance

@SCI.instance
class tGroundMater(Prop):
	#property vars (may be empty)
	view = 4802
	loop = 1
	
#end:class or instance

