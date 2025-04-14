#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 105
import sci_sh
import kernel
import Main
import Audio
import KQ6Room
import Sync
import RandCycle
import LoadMany
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm105 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1
local401 = None
local402 = None
local403 = None


@SCI.instance
class rm105(KQ6Room):
	#property vars (may be empty)
	picture = 98
	autoLoad = 0
	
	@classmethod
	def init():
		global74._send('addToFront:', self)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		self._send('setScript:', showMovie)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def cue():
		global1._send('restart:', 1)
	#end:method

	@classmethod
	def handleEvent():
		kernel.DoAudio(3)
		if local403:
			global1._send('masterVolume:', local403)
			local403 = 0
		#endif
		kernel.DrawPic(98)
		kernel.SetVideoMode(0)
		Cursor._send('showCursor:', 1)
		global1._send('restart:', 1)
	#end:method

	@classmethod
	def newRoom():
		global74._send('delete:', self)
		global72._send('delete:', self)
		global73._send('delete:', self)
		proc958_0(0, 929)
		super._send('newRoom:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class showMovie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc958_0(128, 1, 2, 3, 1091, 4)
				proc958_0(129, 1, 107, 10, 2, 11, 141, 5, 7, 6)
				global69._send('disable:', 'height:', -100, 'activateHeight:', -100)
				User._send('controls:', 1)
				Cursor._send('showCursor:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.SetVideoMode(1)
				kernel.Animate(0)
				kernel.Palette(4, 0, 256, 0)
				cycles = 1
			#end:case
			case 2:
				kernel.DrawPic(107)
				temp0 = 0
				while (temp0 < 100): # inline for
					kernel.Palette(4, 0, 256, temp0)
					temp1 = 0
					while (temp1 < 30): # inline for
					#end:loop
					# for:reinit
					temp0.post('++')
				#end:loop
				cycles = 1
			#end:case
			case 3:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 4:
				global102._send('loop:', 1, 'number:', 105, 'play:')
				kernel.Message(0, 105, 1, 0, 0, 1, @local1)
				(= local401
					kernel.Display(@local1, 100, 12, 81, 106, 300, 102, 98, 105, 3110, 101, 1, 107)
				)
				cycles = 1
			#end:case
			case 5:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 6:
				seconds = 6
			#end:case
			case 7:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 8:
				kernel.Display(105, 0, 108, local401)
				seconds = 2
			#end:case
			case 9:
				kernel.DrawPic(10)
				cycles = 1
			#end:case
			case 10:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 11:
				cycles = 1
			#end:case
			case 12:
				kernel.ShowMovie(r"""FS1.SEQ""", 10)
				kernel.ShowMovie(r"""FS2Y.SEQ""", 10)
				cycles = 1
			#end:case
			case 13:
				kernel.DrawPic(1)
				flames._send('init:')
				cycles = 1
			#end:case
			case 14:
				toonAudio._send('play:', 1, 0, 0, 2, self)
			#end:case
			case 15:
				alexMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 3)
				toonAudio._send('play:', 1, 0, 0, 3, self)
			#end:case
			case 16:
				alexMouth._send('dispose:', 'delete:')
				toonAudio._send('play:', 1, 0, 0, 4, self)
			#end:case
			case 17:
				alexMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 5)
				toonAudio._send('play:', 1, 0, 0, 5, self)
			#end:case
			case 18:
				alexMouth._send('dispose:', 'delete:')
				toonAudio._send('play:', 1, 0, 0, 6, self)
			#end:case
			case 19:
				alexMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 7)
				toonAudio._send('play:', 1, 0, 0, 7, self)
			#end:case
			case 20:
				alexMouth._send('dispose:', 'delete:')
				toonAudio._send('play:', 1, 0, 0, 8, self)
			#end:case
			case 21:
				alexMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 9)
				toonAudio._send('play:', 1, 0, 0, 9, self)
			#end:case
			case 22:
				alexMouth._send('dispose:', 'delete:')
				flames._send('dispose:')
				kernel.ShowMovie(r"""FS2Z.SEQ""", 10)
				kernel.DrawPic(2)
				seconds = 2
			#end:case
			case 23:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 24:
				kernel.DrawPic(107)
				cycles = 1
			#end:case
			case 25:
				global102._send('loop:', -1, 'number:', 120, 'play:')
				kernel.Message(0, 105, 3, 0, 0, 1, @local1)
				(= local401
					kernel.Display(@local1, 100, 12, 81, 106, 300, 102, 98, 105, 3110, 101, 1, 107)
				)
				cycles = 1
			#end:case
			case 26:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 27:
				seconds = 4
			#end:case
			case 28:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 29:
				kernel.Display(105, 0, 108, local401)
				seconds = 2
			#end:case
			case 30:
				kernel.DrawPic(11)
				cycles = 1
			#end:case
			case 31:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 32:
				kernel.ShowMovie(r"""CD1.SEQ""", 10)
				cycles = 1
			#end:case
			case 33:
				kernel.DrawPic(3)
				seconds = 5
			#end:case
			case 34:
				global102._send('stop:')
				global102._send('loop:', 1, 'number:', 125, 'play:')
				global102._send('loop:', 1, 'number:', 107, 'play:')
				kernel.ShowMovie(r"""CD6.SEQ""", 10)
				cycles = 1
			#end:case
			case 35:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 36:
				kernel.DrawPic(141)
				cycles = 1
			#end:case
			case 37:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 38:
				cassMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 10)
				toonAudio._send('play:', 1, 0, 0, 10, self)
			#end:case
			case 39:
				cassMouth._send('dispose:', 'delete:')
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
				cycles = 2
			#end:case
			case 40:
				toonAudio._send('play:', 1, 0, 0, 11, self)
			#end:case
			case 41:#end:case
			case 42:
				kernel.DrawPic(107)
				global102._send('number:', 108, 'play:')
				toonAudio._send('play:', 1, 0, 0, 12, self)
			#end:case
			case 43:
				kernel.Palette(4, 0, 231, 100)
				kernel.ShowMovie(r"""FPAN.SEQ""", 10)
				cycles = 1
			#end:case
			case 44:
				kernel.DrawPic(5)
				flames2._send('init:')
				cycles = 1
			#end:case
			case 45:
				momMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 13)
				toonAudio._send('play:', 1, 0, 0, 13, self)
			#end:case
			case 46:
				momMouth._send('dispose:', 'delete:')
				alexMouth2._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 14)
				toonAudio._send('play:', 1, 0, 0, 14, self)
			#end:case
			case 47:
				alexMouth2._send('dispose:', 'delete:')
				momMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 15)
				toonAudio._send('play:', 1, 0, 0, 15, self)
			#end:case
			case 48:
				momMouth._send('dispose:', 'delete:')
				alexMouth2._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 16)
				toonAudio._send('play:', 1, 0, 0, 16, self)
			#end:case
			case 49:
				alexMouth2._send('dispose:', 'delete:')
				momMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 17)
				toonAudio._send('play:', 1, 0, 0, 17, self)
			#end:case
			case 50:
				momMouth._send('dispose:', 'delete:')
				alexMouth2._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 18)
				toonAudio._send('play:', 1, 0, 0, 18, self)
			#end:case
			case 51:
				alexMouth2._send('dispose:', 'delete:')
				momMouth._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 19)
				toonAudio._send('play:', 1, 0, 0, 19, self)
			#end:case
			case 52:
				momMouth._send('dispose:', 'delete:')
				alexMouth2._send('init:', 'setCycle:', MouthSync, 105, 1, 0, 0, 20)
				toonAudio._send('play:', 1, 0, 0, 20, self)
			#end:case
			case 53:
				alexMouth2._send('dispose:', 'delete:')
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 54:
				flames2._send('dispose:')
				kernel.DrawPic(107)
				cycles = 2
			#end:case
			case 55:
				global102._send('stop:', 'number:', 121, 'play:')
				kernel.Message(0, 105, 1, 0, 0, 21, @local1)
				(= local401
					kernel.Display(@local1, 100, 12, 81, 106, 300, 102, 98, 105, 3110, 101, 1, 107)
				)
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 56:
				seconds = 3
			#end:case
			case 57:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 58:
				kernel.Display(105, 0, 108, local401)
				cycles = 2
			#end:case
			case 59:
				kernel.Palette(4, 0, 231, 100)
				cycles = 1
			#end:case
			case 60:
				kernel.ShowMovie(r"""CLOUD.SEQ""", 10)
				kernel.ShowMovie(r"""BIRDS.SEQ""", 10)
				global102._send('stop:', 'number:', 122, 'play:')
				kernel.ShowMovie(r"""OPEN.SEQ""", 10)
				kernel.ShowMovie(r"""OPEN2.SEQ""", 10)
				kernel.ShowMovie(r"""CLOSE.SEQ""", 10)
				kernel.ShowMovie(r"""SCAN.SEQ""", 10)
				kernel.ShowMovie(r"""SCOP.SEQ""", 10)
				toonAudio._send('play:', 1, 0, 0, 22, self)
			#end:case
			case 61:
				kernel.ShowMovie(r"""LAND.SEQ""", 10)
				cycles = 1
			#end:case
			case 62:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 63:
				kernel.DrawPic(107)
				cycles = 2
			#end:case
			case 64:
				kernel.Message(0, 105, 3, 0, 0, 2, @local1)
				(= local401
					kernel.Display(@local1, 100, 12, 81, 106, 300, 102, 98, 105, 3110, 101, 1, 107)
				)
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 65:
				seconds = 3
			#end:case
			case 66:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 67:
				kernel.Display(105, 0, 108, local401)
				cycles = 2
			#end:case
			case 68:
				global102._send('stop:', 'number:', 123, 'play:')
				kernel.DrawPic(7)
				cycles = 1
			#end:case
			case 69:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 70:
				kernel.ShowMovie(r"""BOAT.SEQ""", 10)
				cycles = 1
			#end:case
			case 71:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 72:
				kernel.DrawPic(107)
				global102._send('stop:', 'number:', 124, 'loop:', 1, 'play:', self)
				kernel.Message(0, 105, 1, 0, 0, 23, @local1)
				kernel.Display(105, 0, 108, local401)
				(= local401
					kernel.Display(@local1, 100, 12, 81, 106, 300, 102, 98, 105, 3110, 101, 1, 107)
				)
				cycles = 1
			#end:case
			case 73:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 74:
				seconds = 7
			#end:case
			case 75:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 76:
				kernel.Display(105, 0, 108, local401)
				cycles = 2
			#end:case
			case 77:
				kernel.DrawPic(6)
				cycles = 1
			#end:case
			case 78:
				kernel.ScriptID(107, 2)._send('doit:', 0, self)
			#end:case
			case 79:
				seconds = 2
			#end:case
			case 80:
				kernel.ShowMovie(r"""NSHP.SEQ""", 10)
				cycles = 2
			#end:case
			case 81:#end:case
			case 82:
				kernel.ScriptID(107, 2)._send('doit:', 1, self)
			#end:case
			case 83:
				kernel.DrawPic(107)
				self._send('setScript:', kernel.ScriptID(107, 0), self)
			#end:case
			case 84:
				temp0 = 100
				while (temp0 > 0): # inline for
					kernel.Palette(4, 0, 256, temp0)
					temp1 = 0
					while (temp1 < 30): # inline for
					#end:loop
					# for:reinit
					temp0.post('--')
				#end:loop
				cycles = 1
			#end:case
			case 85:
				kernel.DrawPic(98)
				cycles = 1
			#end:case
			case 86:
				kernel.SetVideoMode(0)
				global69._send('height:', 0, 'activateHeight:', 0)
				Cursor._send('showCursor:', 1)
				global2._send('newRoom:', 200)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toonAudio(Audio):
	#property vars (may be empty)
	@classmethod
	def play(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		global78._send('add:', self)
		if (not local403):
			local403 = global1._send('masterVolume:', (global1._send('masterVolume:') - 4))
		#endif
		local0 = 0
		(cond
			case kernel.DoAudio(2, 105, param1, param2, param3, param4):
				stopped = 0
				if kernel.IsObject(param5):
					local0 = param5
				#endif
				self._send('doit:')
			#end:case
			case (kernel.IsObject(param5) and (local0 = param5 != 0)):
				local0._send('cue:')
			#end:case
		)
	#end:method

	@classmethod
	def doit():
		if ((not stopped) and (kernel.DoAudio(6) == -1) and (loop == 1)):
			doNotStop = 0
			stopped = 1
			if (local0 != 0):
				temp0 = local0
				local0 = 0
				global78._send('delete:', self)
				global1._send('masterVolume:', local403)
				local403 = 0
				temp0._send('cue:')
			#endif
		#endif
		if ((not stopped) and (kernel.DoAudio(6) == -1) and ((loop > 1) or (loop == -1))):
			self._send('play:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class flames(Prop):
	#property vars (may be empty)
	x = 146
	y = 47
	view = 1
	cycleSpeed = 12
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('setCycle:', RandCycle)
	#end:method

#end:class or instance

@SCI.instance
class flames2(Prop):
	#property vars (may be empty)
	x = 182
	y = 94
	view = 2
	cycleSpeed = 14
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('setCycle:', RandCycle)
	#end:method

#end:class or instance

@SCI.instance
class alexMouth(Prop):
	#property vars (may be empty)
	x = 108
	y = 46
	view = 3
	
	@classmethod
	def init():
		self._send('setPri:', 14, 'ignoreActors:', 1)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class cassMouth(Actor):
	#property vars (may be empty)
	x = 111
	y = 86
	view = 1091
	cel = 7
	
#end:class or instance

@SCI.instance
class alexMouth2(Actor):
	#property vars (may be empty)
	x = 70
	y = 67
	view = 4
	cel = 1
	priority = 14
	signal = 16
	
#end:class or instance

@SCI.instance
class momMouth(Actor):
	#property vars (may be empty)
	x = 242
	y = 64
	view = 4
	loop = 1
	cel = 7
	
#end:class or instance

