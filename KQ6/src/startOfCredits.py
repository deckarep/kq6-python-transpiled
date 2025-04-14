#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 107
import sci_sh
import kernel
import Main
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	startOfCredits = 0,
	openingCredits = 1,
	fadeThePic = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local200
local400 = None
local401 = None
local402 = None
local403 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 0]
local427 = None
local428 = None
local429


@SCI.instance
class findSize(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		kernel.TextSize(@local429, param1, 2207, 315)
		return (((180 - (local429[2] - local429[0])) / 2) - 10)
	#end:method

#end:class or instance

@SCI.instance
class startOfCredits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (kernel.Graph(2) == 256):
					local428 = 0
				else:
					local428 = 1
				#endif
				global102._send('loop:', 1, 'number:', 111, 'play:')
				kq._send('init:')
				cycles = 2
			#end:case
			case 1:
				if local428:
					seconds = 2
				else:
					fadeThePic._send('doit:', 0, self)
				#endif
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				if local428:
					seconds = 2
				else:
					fadeThePic._send('doit:', 1, self)
				#endif
			#end:case
			case 4:
				kq._send('dispose:')
				self._send('setScript:', openingCredits, self)
			#end:case
			case 5:
				if (global102._send('prevSignal:') == -1):
					self._send('cue:')
				else:
					global102._send('client:', self)
				#endif
			#end:case
			case 6:
				cycles = 4
			#end:case
			case 7:
				self._send('dispose:')
				kernel.DisposeScript(107)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openingCredits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.Display(107, 0, 108, local400)
				kernel.Display(107, 0, 108, local401)
				if (local403[local402] == 0):
					self._send('dispose:')
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				local427.post('++')
				kernel.Message(0, 94, 0, 0, 0, local403[local402], @local0)
				temp1 = findSize._send('doit:', @local0)
				local402.post('++')
				(= local400
					kernel.Display(@local0, 102, 7, 100, 60, temp1, 106, 200, 105, 3110, 101, 1, 107)
				)
				kernel.Message(0, 94, 0, 0, 0, local403[local402], @local200)
				local402.post('++')
				(= local401
					kernel.Display(@local200, 102, 7, 100, 60, (temp1 + 15), 106, 200, 105, 2207, 101, 1, 107)
				)
				cycles = 1
			#end:case
			case 2:
				if local428:
					seconds = 2
				else:
					fadeThePic._send('doit:', 0, self)
				#endif
			#end:case
			case 3:
				seconds = 4
			#end:case
			case 4:
				if local428:
					seconds = 2
				else:
					fadeThePic._send('doit:', 1, self)
				#endif
			#end:case
			case 5:
				self._send('changeState:', 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class kq(Actor):
	#property vars (may be empty)
	x = 156
	y = 89
	view = 1092
	priority = 14
	signal = 16
	
#end:class or instance

@SCI.instance
class fadeThePic(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		if (param1 == 1):
			temp0 = 100
			while (temp0 > 0): # inline for
				kernel.Palette(4, 0, 231, temp0)
				temp1 = 0
				while (temp1 < 10): # inline for
				#end:loop
				# for:reinit
				temp0.post('--')
			#end:loop
		else:
			temp0 = 0
			while (temp0 < 100): # inline for
				kernel.Palette(4, 0, 231, temp0)
				temp1 = 0
				while (temp1 < 10): # inline for
				#end:loop
				# for:reinit
				temp0.post('++')
			#end:loop
		#endif
		temp2 = param2
		param2 = 0
		temp2._send('cue:')
	#end:method

#end:class or instance

