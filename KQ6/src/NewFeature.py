#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 83
import sci_sh
import kernel
import Main
import PolyPath
import Feature

class NewFeature(Feature):
	#property vars (may be empty)
	normal = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		super._send('init:', &rest)
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
				(not normal)
				(param1._send('type:') & 0x4000)
				self._send('onMe:', param1)
				(_approachVerbs & global66._send('doit:', param1._send('message:')))
			)
			CueObj._send('state:', 0, 'cycles:', 0, 'client:', self, 'theVerb:', param1._send('message:'))
			self._send('doSpecial:', CueObj._send('theVerb:'))
			param1._send('claimed:', 1)
			return
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

	@classmethod
	def doSpecial():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('cue:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global0._send('setMotion:', PolyPath, approachX, approachY, CueObj)
	#end:method

#end:class or instance

