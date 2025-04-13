#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 983
import sci_sh
import kernel
import Print
import Motion

class Path(MoveTo):
	#property vars (may be empty)
	intermediate = 0
	value = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			client = param1
			caller = (param2 if (argc >= 2) else 0)
			intermediate = (param3 if (argc == 3) else 0)
			value = -1
			x = client._send('x:')
			y = client._send('y:')
		#endif
		if self._send('atEnd:'):
			self._send('moveDone:')
		else:
			self._send('next:')
			super._send('init:', client, x, y)
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if self._send('atEnd:'):
			super._send('moveDone:')
		else:
			if intermediate:
				intermediate._send('cue:', (value / 2))
			#endif
			self._send('next:')
			super._send('init:', client, x, y)
		#endif
	#end:method

	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = self._send('at:', value.post('++'))
		y = self._send('at:', value.post('++'))
	#end:method

	@classmethod
	def atEnd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(or
				(self._send('at:', (value + 1)) == -32768)
				(self._send('at:', (value + 2)) == -32768)
			)
		)
	#end:method

	@classmethod
	def at():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		Print._send('addTextF:', r"""%s needs an 'at:' method.""", name, 'init:')
		return 0
	#end:method

#end:class or instance

class RelPath(Path):
	#property vars (may be empty)
	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(x += self._send('at:', value.post('++')))
		(y += self._send('at:', value.post('++')))
	#end:method

#end:class or instance

