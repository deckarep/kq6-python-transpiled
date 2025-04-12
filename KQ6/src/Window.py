#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 981
import sci_sh
import kernel
import System

class SysWindow(Obj):
	#property vars (may be empty)
	top = 0
	left = 0
	bottom = 0
	right = 0
	color = 0
	back = 15
	priority = 15
	window = 0
	type = 0
	title = 0
	brTop = 0
	brLeft = 0
	brBottom = 190
	brRight = 320
	lsTop = 0
	lsLeft = 0
	lsBottom = 0
	lsRight = 0
	eraseOnly = 0
	
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= window
			kernel.NewWindow(top, left, bottom, right, lsTop, lsLeft, lsBottom, lsRight, title, type, priority, color, back)
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if window:
			kernel.DisposeWindow(window, eraseOnly)
			window = 0
		#endif
		(super dispose:)
	#end:method

#end:class or instance

class Window(SysWindow):
	#property vars (may be empty)
	priority = -1
	underBits = 0
	
	@classmethod
	def center():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self
			moveTo:
				(((brRight - left) - (right - left)) / 2)
				(((brBottom - top) - (bottom - top)) / 2)
		)
	#end:method

	@classmethod
	def move(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(left += param1)
		(right += param2)
		(right += param1)
		(bottom += param2)
	#end:method

	@classmethod
	def moveTo(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self move: (param1 - left) (param2 - top))
	#end:method

	@classmethod
	def inset(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(top += param2)
		(left += param1)
		(bottom -= param2)
		(right -= param1)
	#end:method

	@classmethod
	def setMapSet():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		if (-1 != color):
			(temp0 |= 0x0001)
		#endif
		if (-1 != priority):
			(temp0 |= 0x0002)
		#endif
		return temp0
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Graph(12, top, left, bottom, right, (self setMapSet:))
	#end:method

	@classmethod
	def draw(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			color = param1
		#endif
		if (argc >= 2):
			priority = param2
		#endif
		kernel.Graph(11, top, left, bottom, right, (self setMapSet:), color, priority)
	#end:method

	@classmethod
	def save():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		underBits = kernel.Graph(7, top, left, bottom, right, (self setMapSet:))
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if underBits:
			kernel.Graph(8, underBits)
		#endif
	#end:method

	@classmethod
	def doit():#end:method

	@classmethod
	def handleEvent():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self restore:)
		if window:
			kernel.DisposeWindow(window)
			window = 0
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def erase():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self draw: back -1)
	#end:method

#end:class or instance

