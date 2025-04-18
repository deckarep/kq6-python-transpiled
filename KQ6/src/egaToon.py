#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 106
import sci_sh
import kernel
import Main
import KQ6Room
import System

# Public Export Declarations
SCI.public_exports(
	egaToon = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local400 = None
local401 = None
local402 = 1
local403 = None
local404
local408 = None


@SCI.instance
class egaToon(KQ6Room):
	#property vars (may be empty)
	picture = 107
	autoLoad = 0
	
	@classmethod
	def handleEvent():
		Cursor._send('showCursor:', 1)
		global1._send('restart:', 1)
	#end:method

	@classmethod
	def init():
		global1._send('handsOff:')
		Cursor._send('showCursor:', 0)
		global69._send('disable:', 'height:', -100, 'activateHeight:', -100)
		self._send('setScript:', openingScript)
		openingScript._send('setScript:', playMusic)
		super._send('init:', &rest)
		global74._send('addToFront:', self)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		kernel.Palette(1, 999)
	#end:method

	@classmethod
	def newRoom():
		global69._send('disable:', 'height:', 0, 'activateHeight:', 0)
		Cursor._send('showCursor:', 1)
		global74._send('delete:', self)
		global72._send('delete:', self)
		global73._send('delete:', self)
		super._send('newRoom:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class findSize(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		kernel.TextSize(@local404, param1, 3110, 315)
		return ((180 - (local404[2] - local404[0])) / 2)
	#end:method

#end:class or instance

@SCI.instance
class openingScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 15
			#end:case
			case 1:
				kernel.Display(106, 0, 108, local400)
				temp1 = kernel.Message(1, 0)
				if local403:
					kernel.Message(0, 105, 2, 0, 2, local402, @local0)
					local408 = kernel.Message(2, 105, 2, 0, 2, local402)
				else:
					kernel.Message(0, 105, 2, 0, 0, local402, @local0)
					local408 = kernel.Message(2, 105, 2, 0, 0, local402)
				#endif
				temp2 = findSize._send('doit:', @local0)
				match temp1
					case 12:
						(= local400
							kernel.Display(@local0, 100, 12, temp2, 106, 300, 102, 6, 105, 3110, 101, 1, 107)
						)
					#end:case
					case 2:
						(= local400
							kernel.Display(@local0, 100, 12, temp2, 106, 300, 102, 20, 105, 3110, 101, 1, 107)
						)
					#end:case
					case 28:
						(= local400
							kernel.Display(@local0, 100, 12, temp2, 106, 300, 102, 30, 105, 3110, 101, 1, 107)
						)
					#end:case
					else:
						(= local400
							kernel.Display(@local0, 100, 12, temp2, 106, 300, 102, 40, 105, 3110, 101, 1, 107)
						)
					#end:else
				#end:match
				cycles = 1
			#end:case
			case 2:
				match local403
					case 0:
						if proc999_5(local402, 17, 19, 26):
							playMusic._send('cue:')
						#endif
					#end:case
					case 1:
						if proc999_5(local402, 3, 9):
							playMusic._send('cue:')
						#endif
					#end:case
				#end:match
				cycles = 1
			#end:case
			case 3:
				if (local408 < 15):
					seconds = 5
				else:
					seconds = (local408 / 8)
				#endif
			#end:case
			case 4:
				(cond
					case ((temp0 = local402.post('++') == 12) and local403):
						kernel.Display(106, 0, 108, local400)
						cycles = 2
					#end:case
					case ((not local403) and (temp0 == 28)):
						local403 = 1
						local402 = 1
						self._send('init:')
					#end:case
					else:
						self._send('init:')
					#end:else
				)
			#end:case
			case 5:
				self._send('setScript:', kernel.ScriptID(107, 0), self)
			#end:case
			case 6:
				global2._send('newRoom:', 200)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class playMusic(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global102._send('loop:', -1, 'number:', 105, 'play:')
			#end:case
			case 1:
				global102._send('number:', 106, 'play:')
			#end:case
			case 2:
				global102._send('number:', 107, 'play:')
			#end:case
			case 3:
				global102._send('loop:', 1, 'number:', 108, 'play:')
			#end:case
			case 4:
				global102._send('stop:', 'number:', 109, 'loop:', -1, 'play:')
			#end:case
			case 5:
				global102._send('stop:', 'number:', 110, 'loop:', 1, 'play:')
			#end:case
		#end:match
	#end:method

#end:class or instance

