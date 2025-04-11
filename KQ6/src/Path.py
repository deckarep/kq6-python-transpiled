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
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			client = param1
			caller = (param2 if (argc >= 2) else 0)
			intermediate = (param3 if (argc == 3) else 0)
			value = -1
			x = (client x:)
			y = (client y:)
		#endif
		if (self atEnd:):
			(self moveDone:)
		else:
			(self next:)
			(super init: client x y)
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (self atEnd:):
			(super moveDone:)
		else:
			if intermediate:
				(intermediate cue: (value / 2))
			#endif
			(self next:)
			(super init: client x y)
		#endif
	#end:method

	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = (self at: value.post('++'))
		y = (self at: value.post('++'))
	#end:method

	@classmethod
	def atEnd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				((self at: (value + 1)) == -32768)
				((self at: (value + 2)) == -32768)
			)
		)
	#end:method

	@classmethod
	def at():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print addTextF: r"""%s needs an 'at:' method.""" name init:)
		return 0
	#end:method

#end:class or instance

class RelPath(Path):
	#property vars (may be empty)
	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(x += (self at: value.post('++')))
		(y += (self at: value.post('++')))
	#end:method

#end:class or instance

