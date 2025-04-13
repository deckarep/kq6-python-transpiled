#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 100
import sci_sh
import kernel
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		if ((global87 == 0) or (not global169)):
			kernel.Palette(4, 0, 255, 0)
			kernel.Load(129, 100)
			presents._send('init:')
			kernel.DrawPic(99)
		#endif
		global1._send('setCursor:', blankCursor)
		global69._send('disable:')
		global2._send('setScript:', introScript)
	#end:method

	@classmethod
	def doVerb():#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('height:', 0, 'activateHeight:', 0)
		super._send('newRoom:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class introScript(Script):
	#property vars (may be empty)
	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1._send('type:') & 0x0004) and (param1._send('message:') == 27)):
			param1._send('claimed:', 1)
		#endif
		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global72._send('add:', self)
				if (global169 and kernel.Platform(7) and (global87 > 0)):
					self._send('setScript:', winLogo, self)
				else:
					self._send('setScript:', dosLogo, self)
				#endif
			#end:case
			case 1:
				global2._send('drawPic:', 100, 9)
				cycles = 1
			#end:case
			case 2:
				if global169:
					cycles = 1
				else:
					FadeCode._send('init:', 100, 1, self)
				#endif
			#end:case
			case 3:
				six._send('init:')
				global102._send('number:', 2, 'loop:', 1, 'play:', self)
				seconds = 5
			#end:case
			case 4:
				six._send('setCycle:', End)
			#end:case
			case 5:
				global1._send('handsOn:')
				seconds = 10
				global69._send(
					'enable:',
					'disable:', 0, 1, 2, 3, 4, 5,
					'height:', -100,
					'activateHeight:', -100
				)
				kernel.Portrait(0, r"""ALEX""")
				Cursor._send('showCursor:', 1)
				global1._send('setCursor:', global20)
				six._send('stopUpd:')
				openingBut._send('init:', 'stopUpd:')
				playBut._send('init:', 'stopUpd:')
				helpBut._send('init:', 'stopUpd:')
				restoreBut._send('init:', 'stopUpd:')
			#end:case
			case 6:#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class FadeCode(Code):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
		global78._send('add:', self)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local0 != local2):
			(local0 += (1 * local1))
			kernel.Palette(4, 0, 255, local0)
			temp0 = 0
			while (temp0 < 10): # inline for
			#end:loop
		else:
			global78._send('delete:', self)
			if (local3 and kernel.IsObject(local3)):
				local3._send('cue:')
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global72._send('add:', self)
		global73._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('delete:', self)
		global73._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(not param1._send('modifiers:'))
				(or
					(param1._send('type:') & 0x0001)
					((param1._send('type:') & 0x0004) and (param1._send('message:') == 13))
				)
				(<= nsLeft param1._send('x:') nsRight)
				(<= nsTop param1._send('y:') nsBottom)
			)
			global2._send('script:')._send('seconds:', 0)
			if self._send('flash:', (param1._send('type:') & 0x0004)):
				self._send('cue:')
			#endif
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def flash(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = 0
		self._send('startUpd:')
		while (temp0 = Event._send('new:')._send('type:') != (8 if param1 else 2)):

			temp0._send('localize:')
			self._send('cel:', super._send('onMe:', temp0))
			kernel.Animate(global5._send('elements:'), 1)
			temp0._send('dispose:')
		#end:loop
		if (cel == 1):
			temp1 = 1
		#endif
		self._send('cel:', 0, 'stopUpd:')
		kernel.Animate(global5._send('elements:'), 1)
		temp0._send('dispose:')
		if (not temp1):
			global2._send('script:')._send('seconds:', 8)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (global169 and kernel.Platform(7) and kernel.DoSound(4)):
				global2._send('newRoom:', 108)
			#end:case
			case 
				(and
					(not global169)
					(not (global87 == 0))
					(kernel.Graph(2) == 256)
					kernel.DoSound(4)
				):
				global2._send('newRoom:', 105)
			#end:case
			else:
				global2._send('newRoom:', 106)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('newRoom:', 200)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('newRoom:', 205)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global1._send('restore:')
		global1._send('setCursor:', global20)
		global2._send('script:')._send('seconds:', 8)
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
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				Cursor._send('showCursor:', 0)
				global102._send('number:', 1, 'loop:', 1)
				global102._send('play:', self)
			#end:case
			case 1:
				if (not global169):
					if (global87 == 0):
						FadeCode._send('init:', 100, 1, self)
					else:
						FadeCode._send('init:', 100, 1)
					#endif
				#endif
			#end:case
			case 2:
				glint._send('init:', 'setCycle:', End)
			#end:case
			case 3:
				glint._send('posn:', 148, 143, 'setCycle:', End)
			#end:case
			case 4:
				cycles = 1
			#end:case
			case 5:
				if global169:
					cycles = 1
				else:
					FadeCode._send('init:', 0, -1, self)
				#endif
			#end:case
			case 6:
				presents._send('dispose:')
				glint._send('dispose:')
				if global169:
					global2._send('drawPic:', 98)
				#endif
				cycles = 1
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class winLogo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global2._send('drawPic:', 98)
				cycles = 1
			#end:case
			case 1:
				if (not kernel.ShowMovie(0, r"""hdlogo.avi""")):
					kernel.ShowMovie(1, 0, 5)
					kernel.ShowMovie(2, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				kernel.ShowMovie(6)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

