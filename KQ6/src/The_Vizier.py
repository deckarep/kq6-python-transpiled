#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1029
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	The_Vizier = 24,
)

@SCI.instance
class The_Vizier(Kq6Talker):
	#property vars (may be empty)
	name = r"""The Vizier"""
	x = 5
	y = 5
	view = 892
	talkWidth = 213
	textX = 76
	textY = 8
	raveName = r"""VIZIER"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case proc913_0(59):
				self._send('cel:', 1)
				super._send('init:', 0, 0, 0, &rest)
			#end:case
			case proc913_0(99):
				self._send('cel:', 1, 'x:', 135, 'y:', 43, 'talkWidth:', 150, 'textX:', -44, 'textY:', 53)
				super._send('init:', 0, 0, wedMouth, &rest)
			#end:case
			case (global11 == 145):
				self._send('cel:', 1, 'x:', 42, 'y:', 58, 'textX:', -32, 'textY:', -50)
				tMouth._send('view:', 1466, 'loop:', 2, 'nsLeft:', 0, 'nsTop:', 0)
				super._send('init:', 0, 0, tMouth, &rest)
			#end:case
			case (global11 == 150):
				self._send(
					'cel:', 1,
					'x:', 54,
					'y:', 48,
					'talkWidth:', 160,
					'textX:', -44,
					'textY:', 53,
					'keepWindow:', 0
				)
				super._send('init:', 0, tEyes150, tMouth150, &rest)
			#end:case
			else:
				if (global11 == 750):
					winPosn = 0
				#endif
				self._send(
					'view:', 892,
					'loop:', 0,
					'cel:', 0,
					'x:', 5,
					'y:', 5,
					'textX:', 76,
					'textY:', 8,
					'talkWidth:', 213
				)
				super._send('init:', tBust, tEyes, tMouth, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 892
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			self._send('cel:', 1)
		#endif
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 32
	nsLeft = 26
	view = 892
	loop = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			self._send('cel:', 1)
		#endif
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 41
	nsLeft = 24
	view = 892
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouth150(Prop):
	#property vars (may be empty)
	view = 150
	loop = 3
	
#end:class or instance

@SCI.instance
class wedMouth(Prop):
	#property vars (may be empty)
	view = 161
	loop = 2
	
#end:class or instance

@SCI.instance
class tEyes150(Prop):
	#property vars (may be empty)
	nsTop = -7
	nsLeft = -2
	view = 150
	loop = 8
	
#end:class or instance

