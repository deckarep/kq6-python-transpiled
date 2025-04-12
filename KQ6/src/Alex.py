#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1001
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	Alex = 2,
)

@SCI.instance
class Alex(Kq6Talker):
	#property vars (may be empty)
	view = 890
	raveName = r"""ALEX"""
	winPosn = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (proc913_0(59) and (global11 != 850)):
				(self cel: 1 x: 5 y: 5 textX: 76 textY: 8 talkWidth: 213)
				(super init: 0 0 0 &rest)
			#end:case
			case (((global2 curPic:) == 165) and (global11 == 740)):
				(self cel: 1 x: 156 y: 71 textX: -120 textY: 70 talkWidth: 130)
				(super init: 0 tEyes740 tMouth740 &rest)
			#end:case
			case 
				(and
					(global11 == 406)
					((global0 view:) != 900)
					(not proc913_0(1))
				):
				(self cel: 1 x: 5 y: 5 textX: 1 textY: 8 talkWidth: 213)
				(super init: 0 0 0 &rest)
			#end:case
			case (global11 == 150):
				(self
					cel: 1
					x: 219
					y: 45
					talkWidth: 153
					textX: -70
					textY: 56
					keepWindow: 0
				)
				(super init: 0 tEyes150 tMouth150 &rest)
			#end:case
			case (global11 == 370):
				(self
					cel: 1
					x: 145
					y: 50
					talkWidth: 230
					textX: -95
					textY: -44
					keepWindow: 0
				)
				(super init: 0 0 tBigHead &rest)
			#end:case
			case (global11 == 380):
				(self
					view: 3812
					loop: 1
					x: 208
					y: 86
					textX: -188
					textY: -76 talkWidth 230
					keepWindow: 0
				)
				(super init: 0 0 tSideOfMouth &rest)
			#end:case
			case (global11 == 690):
				(self
					view: 2002
					loop: 0
					cel: 1
					x: 129
					y: 125
					textX: 32
					textY: -35
					talkWidth: 140
				)
				(super init: 0 0 tMouth690 &rest)
			#end:case
			case proc913_0(102):
				(self cel: 1 x: 176 y: 60 textX: 20 textY: -40 talkWidth: 100)
				(tEyes view: 7832 loop: 12 cel: 0 nsLeft: 0 nsTop: 0)
				(tMouth view: 7832 loop: 11 cel: 0 nsLeft: 0 nsTop: 6)
				(super init: 0 tEyes tMouth &rest)
			#end:case
			case proc913_0(99):
				(self cel: 1 x: 44 y: 41 textX: -10 textY: 71 talkWidth: 100)
				(tEyes view: 161 loop: 4 cel: 0 nsLeft: 0 nsTop: 0)
				(tMouth view: 161 loop: 3 cel: 0 nsLeft: 2 nsTop: 10)
				(super init: 0 tEyes tMouth &rest)
			#end:case
			case proc913_0(150):
				(self cel: 0 x: 5 y: 5 textX: 78 textY: 8 talkWidth: 213)
				(tEyes view: 890 loop: 2 nsTop: 27 nsLeft: 27)
				(super init: tBust tEyes 0 &rest)
			#end:case
			else:
				if 
					(or
						proc999_5(global11, 750, 290, 220, 260)
						(and
							((global0 view:) == 900)
							(or
								proc999_5((global0 loop:), 1, 5, 7)
								(and
									((global0 loop:) == 9)
									proc999_5((global0 cel:), 1, 5, 7)
								)
							)
						)
					)
					winPosn = 1
				else:
					winPosn = 0
				#endif
				(self cel: 0 x: 5 y: 5 textX: 78 textY: 8 talkWidth: 213)
				(tEyes view: 890 loop: 2 nsTop: 27 nsLeft: 27)
				(tMouth view: 890 loop: 1 nsTop: 33 nsLeft: 26)
				(super init: tBust tEyes tMouth &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tSideOfMouth(Prop):
	#property vars (may be empty)
	view = 381
	loop = 3
	
#end:class or instance

@SCI.instance
class tBigHead(Prop):
	#property vars (may be empty)
	view = 374
	loop = 4
	
#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 890
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 27
	nsLeft = 27
	view = 890
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 33
	nsLeft = 26
	view = 890
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouth150(Prop):
	#property vars (may be empty)
	view = 150
	loop = 2
	
#end:class or instance

@SCI.instance
class tEyes150(Prop):
	#property vars (may be empty)
	nsTop = -6
	nsLeft = 4
	view = 150
	loop = 9
	
#end:class or instance

@SCI.instance
class tMouth740(Prop):
	#property vars (may be empty)
	view = 165
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes740(Prop):
	#property vars (may be empty)
	nsTop = -8
	nsLeft = -1
	view = 165
	
#end:class or instance

@SCI.instance
class tMouth690(Prop):
	#property vars (may be empty)
	view = 691
	loop = 8
	
#end:class or instance

