#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1026
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Saladin = 13,
)

@SCI.instance
class Saladin(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8921
	talkWidth = 213
	textX = 76
	textY = 8
	raveName = r"""SALADIN"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (((global2 curPic:) == 165) and (global11 == 740)):
				(self cel: 1 x: 1 y: 1 textX: 5 textY: 8 keepWindow: 0)
				(super init: 0 0 0 &rest)
			#end:case
			case (global11 == 150):
				(self cel: 1 x: 288 y: 16 textX: -240 textY: -10 keepWindow: 0)
				(super init: 0 tEyesA tMouthA &rest)
			#end:case
			case proc913_0(99):
				(self cel: 1 x: 10 y: 24 textX: 5 textY: 88)
				(super init: 0 0 wedMouth &rest)
			#end:case
			else:
				(self
					view: 8921
					loop: 0
					cel: 0
					x: 5
					y: 5
					textX: 78
					textY: 8
					talkWidth: 213
				)
				(super init: tBust tEyes tMouth &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8921
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 19
	nsLeft = 31
	view = 8921
	loop = 2
	
#end:class or instance

@SCI.instance
class tEyesA(Prop):
	#property vars (may be empty)
	nsTop = -16
	nsLeft = 4
	view = 150
	loop = 10
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 25
	view = 8921
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouthA(Actor):
	#property vars (may be empty)
	view = 150
	loop = 4
	
#end:class or instance

@SCI.instance
class wedMouth(Prop):
	#property vars (may be empty)
	view = 161
	loop = 1
	
#end:class or instance

