#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 100
import sci_sh
import Main
import KQ6Room
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm100 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.instance
class rm100(KQ6Room):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if ((global87 == 0) or (not global169)):
			(Palette 4 0 255 0)
			(Load 129 100)
			(presents init:)
			(DrawPic 99)
		#endif
		(global1 setCursor: blankCursor)
		(global69 disable:)
		(global2 setScript: introScript)
	#end:method

	@classmethod
	def doVerb():#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 height: 0 activateHeight: 0)
		(super newRoom: &rest)
	#end:method

#end:class or instance

@SCI.instance
class introScript(Script):
	#property vars (may be empty)
	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (((param1 type:) & 0x0004) and ((param1 message:) == 27)):
			(param1 claimed: 1)
		#endif
		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global72 add: self)
				if (and global169 (Platform 7) (global87 > 0)):
					(self setScript: winLogo self)
				else:
					(self setScript: dosLogo self)
				#endif
			#end:case
			case 1:
				(global2 drawPic: 100 9)
				cycles = 1
			#end:case
			case 2:
				if global169:
					cycles = 1
				else:
					(FadeCode init: 100 1 self)
				#endif
			#end:case
			case 3:
				(six init:)
				(global102 number: 2 loop: 1 play: self)
				seconds = 5
			#end:case
			case 4:
				(six setCycle: End)
			#end:case
			case 5:
				(global1 handsOn:)
				seconds = 10
				(global69
					enable:
					disable: 0 1 2 3 4 5
					height: -100
					activateHeight: -100
				)
				(Portrait 0 r"""ALEX""")
				(Cursor showCursor: 1)
				(global1 setCursor: global20)
				(six stopUpd:)
				(openingBut init: stopUpd:)
				(playBut init: stopUpd:)
				(helpBut init: stopUpd:)
				(restoreBut init: stopUpd:)
			#end:case
			case 6:#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class FadeCode(Code):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local3 = 0
		if (argc >= 1):
			local2 = param1
			if (argc >= 2):
				local1 = param2
				if (argc >= 3):
					local3 = param3
				#endif
			#endif
		#endif
		(global78 add: self)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local0 != local2):
			(local0 += (1 * local1))
			(Palette 4 0 255 local0)
			temp0 = 0
			while (temp0 < 10): # inline for
			#end:loop
		else:
			(global78 delete: self)
			if (local3 and (IsObject local3)):
				(local3 cue:)
				local3 = 0
			#endif
		#endif
	#end:method

#end:class or instance

@SCI.instance
class glint(Prop):
	#property vars (may be empty)
	x = 161
	y = 124
	view = 100
	
#end:class or instance

@SCI.instance
class presents(Prop):
	#property vars (may be empty)
	x = 132
	y = 182
	view = 100
	loop = 1
	
#end:class or instance

@SCI.instance
class blankCursor(Cursor):
	#property vars (may be empty)
	view = 998
	cel = 1
	
#end:class or instance

class ButtonActor(Actor):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global72 add: self)
		(global73 add: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 delete: self)
		(global73 delete: self)
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
					(((param1 type:) & 0x0004) and ((param1 message:) == 13))
				)
				(<= nsLeft (param1 x:) nsRight)
				(<= nsTop (param1 y:) nsBottom)
			)
			((global2 script:) seconds: 0)
			if (self flash: ((param1 type:) & 0x0004)):
				(self cue:)
			#endif
			(param1 claimed: 1)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def flash(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = 0
		(self startUpd:)
		while ((temp0 = (Event new:) type:) != (8 if param1 else 2)):

			(temp0 localize:)
			(self cel: (super onMe: temp0))
			(Animate (global5 elements:) 1)
			(temp0 dispose:)
		#end:loop
		if (cel == 1):
			temp1 = 1
		#endif
		(self cel: 0 stopUpd:)
		(Animate (global5 elements:) 1)
		(temp0 dispose:)
		if (not temp1):
			((global2 script:) seconds: 8)
		#endif
		return temp1
	#end:method

#end:class or instance

@SCI.instance
class openingBut(ButtonActor):
	#property vars (may be empty)
	x = 110
	y = 174
	view = 100
	loop = 3
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (and global169 (Platform 7) (DoSound 4)):
				(global2 newRoom: 108)
			#end:case
			case 
				(and
					(not global169)
					(not (global87 == 0))
					((Graph 2) == 256)
					(DoSound 4)
				):
				(global2 newRoom: 105)
			#end:case
			else:
				(global2 newRoom: 106)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class playBut(ButtonActor):
	#property vars (may be empty)
	x = 220
	y = 173
	view = 100
	loop = 5
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2 newRoom: 200)
	#end:method

#end:class or instance

@SCI.instance
class helpBut(ButtonActor):
	#property vars (may be empty)
	x = 165
	y = 174
	view = 100
	loop = 4
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2 newRoom: 205)
	#end:method

#end:class or instance

@SCI.instance
class restoreBut(ButtonActor):
	#property vars (may be empty)
	x = 55
	y = 174
	view = 100
	loop = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 restore:)
		(global1 setCursor: global20)
		((global2 script:) seconds: 8)
	#end:method

#end:class or instance

@SCI.instance
class six(Prop):
	#property vars (may be empty)
	x = 113
	y = 74
	view = 101
	
#end:class or instance

@SCI.instance
class dosLogo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(Cursor showCursor: 0)
				(global102 number: 1 loop: 1)
				(global102 play: self)
			#end:case
			case 1:
				if (not global169):
					if (global87 == 0):
						(FadeCode init: 100 1 self)
					else:
						(FadeCode init: 100 1)
					#endif
				#endif
			#end:case
			case 2:
				(glint init: setCycle: End)
			#end:case
			case 3:
				(glint posn: 148 143 setCycle: End)
			#end:case
			case 4:
				cycles = 1
			#end:case
			case 5:
				if global169:
					cycles = 1
				else:
					(FadeCode init: 0 -1 self)
				#endif
			#end:case
			case 6:
				(presents dispose:)
				(glint dispose:)
				if global169:
					(global2 drawPic: 98)
				#endif
				cycles = 1
			#end:case
			case 7:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class winLogo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global2 drawPic: 98)
				cycles = 1
			#end:case
			case 1:
				if (not (ShowMovie 0 r"""hdlogo.avi""")):
					(ShowMovie 1 0 5)
					(ShowMovie 2 0 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(ShowMovie 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

