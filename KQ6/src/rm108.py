#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 108
import sci_sh
import kernel
import Main
import KQ6Room
import System

# Public Export Declarations
SCI.public_exports(
	rm108 = 0,
)

@SCI.instance
class rm108(KQ6Room):
	#property vars (may be empty)
	picture = 98
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global1._send('handsOff:')
		global69._send('disable:', 'height:', -100, 'activateHeight:', -100)
		global74._send('addToFront:', self)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		super._send('init:', &rest)
		self._send('setScript:', sShowMovieWin)
	#end:method

	@classmethod
	def handleEvent():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.ShowMovie(3)
		kernel.ShowMovie(6)
		global69._send('disable:', 'height:', 0, 'activateHeight:', 0)
		global1._send('restart:', 1)
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global74._send('delete:', self)
		global72._send('delete:', self)
		global73._send('delete:', self)
		global69._send('disable:', 'height:', 0, 'activateHeight:', 0)
		super._send('newRoom:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class sShowMovieWin(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 10
			#end:case
			case 1:
				if (not kernel.ShowMovie(0, r"""toon.avi""")):
					kernel.ShowMovie(1, 0, 0)
					kernel.ShowMovie(2, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				kernel.ShowMovie(6)
				cycles = 1
			#end:case
			case 3:
				global2._send('newRoom:', 200)
			#end:case
		#end:match
	#end:method

#end:class or instance

