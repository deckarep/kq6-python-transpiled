#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1037
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	Gnomes = 36,
	GSmell = 61,
	GSound = 65,
	GTaste = 66,
	GTouch = 67,
	GSight = 68,
)

class GnomeTalker(Kq6Talker):
	#property vars (may be empty)
	extra = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			bust = param1
			if (argc >= 2):
				eyes = param2
				if (argc >= 3):
					mouth = param3
					if (raving and (argc >= 4)):
						extra = param4
					#endif
				#endif
			#endif
		#endif
		if ((global90 == 2) and argc and kernel.IsObject(param1)):
			self._send('x:', 59, 'y:', 15)
		#endif
		self._send('setSize:')
		super._send('init:')
	#end:method

	@classmethod
	def doit():
		if (raving and extra):
			kernel.DrawCel(extra._send('view:'), extra._send('loop:'), extra._send(
				'cel:'
			), (extra._send('nsLeft:') + nsLeft), (extra._send('nsTop:') + nsTop), -1)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def setSize():
		nsLeft = x
		nsTop = y
		(= nsRight
			(+
				nsLeft
				proc999_3(if view:
					kernel.CelWide(view, loop, cel)
				else:
					0
				#endif, (and
					kernel.IsObject(bust)
					(+
						bust._send('nsLeft:')
						kernel.CelWide(bust._send('view:'), bust._send('loop:'), bust._send('cel:'))
					)
				), (and
					kernel.IsObject(eyes)
					(+
						eyes._send('nsLeft:')
						kernel.CelWide(eyes._send('view:'), eyes._send('loop:'), eyes._send('cel:'))
					)
				), (and
					kernel.IsObject(mouth)
					(+
						mouth._send('nsLeft:')
						kernel.CelWide(mouth._send('view:'), mouth._send('loop:'), mouth._send('cel:'))
					)
				), (and
					kernel.IsObject(extra)
					(+
						extra._send('nsLeft:')
						kernel.CelWide(extra._send('view:'), extra._send('loop:'), extra._send('cel:'))
					)
				))
			)
		)
		(= nsBottom
			(+
				nsTop
				proc999_3(if view:
					kernel.CelHigh(view, loop, cel)
				else:
					0
				#endif, (and
					kernel.IsObject(bust)
					(+
						bust._send('nsTop:')
						kernel.CelHigh(bust._send('view:'), bust._send('loop:'), bust._send('cel:'))
					)
				), (and
					kernel.IsObject(eyes)
					(+
						eyes._send('nsTop:')
						kernel.CelHigh(eyes._send('view:'), eyes._send('loop:'), eyes._send('cel:'))
					)
				), (and
					kernel.IsObject(mouth)
					(+
						mouth._send('nsTop:')
						kernel.CelHigh(mouth._send('view:'), mouth._send('loop:'), mouth._send('cel:'))
					)
				), (and
					kernel.IsObject(extra)
					(+
						extra._send('nsTop:')
						kernel.CelHigh(extra._send('view:'), extra._send('loop:'), extra._send('cel:'))
					)
				))
			)
		)
	#end:method

	@classmethod
	def show():
		if (not underBits):
			underBits = kernel.Graph(7, nsTop, nsLeft, nsBottom, nsRight, 1)
		#endif
		temp0 = kernel.PicNotValid()
		kernel.PicNotValid(1)
		if bust:
			kernel.DrawCel(bust._send('view:'), bust._send('loop:'), bust._send('cel:'), (+
				bust._send('nsLeft:')
				nsLeft
			), (bust._send('nsTop:') + nsTop), -1)
		#endif
		if eyes:
			kernel.DrawCel(eyes._send('view:'), eyes._send('loop:'), eyes._send('cel:'), (+
				eyes._send('nsLeft:')
				nsLeft
			), (eyes._send('nsTop:') + nsTop), -1)
		#endif
		if mouth:
			kernel.DrawCel(mouth._send('view:'), mouth._send('loop:'), mouth._send(
				'cel:'
			), (mouth._send('nsLeft:') + nsLeft), (mouth._send('nsTop:') + nsTop), -1)
		#endif
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1)
		if (extra and raving):
			kernel.DrawCel(extra._send('view:'), extra._send('loop:'), extra._send(
				'cel:'
			), (extra._send('nsLeft:') + nsLeft), (extra._send('nsTop:') + nsTop), -1)
		#endif
		kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
		kernel.PicNotValid(temp0)
	#end:method

#end:class or instance

@SCI.instance
class Gnomes(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8930
	talkWidth = 208
	textX = 86
	textY = 6
	raveName = r"""GNOMES"""
	
	@classmethod
	def init():
		super._send('init:', tBust, 0, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class GSmell(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8931
	talkWidth = 208
	textX = 86
	textY = 8
	raveName = r"""SMELL"""
	
	@classmethod
	def init():
		if proc913_0(59):
			super._send('init:', tSmellBust, 0, tSmellMouth, &rest)
		else:
			super._send('init:', tSmellBust, 0, tSmellMouth, tSmellPin, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class GSound(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8932
	talkWidth = 208
	textX = 86
	textY = 8
	raveName = r"""SOUND"""
	
	@classmethod
	def init():
		if proc913_0(59):
			super._send('init:', tSoundBust, 0, tSoundMouth, &rest)
		else:
			super._send('init:', tSoundBust, 0, tSoundMouth, tSoundMuffs, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class GTaste(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8933
	talkWidth = 208
	textX = 86
	textY = 8
	raveName = r"""TASTE"""
	
	@classmethod
	def init():
		super._send('init:', tTasteBust, 0, tTasteMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class GTouch(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8934
	talkWidth = 208
	textX = 86
	textY = 8
	raveName = r"""TOUCH"""
	
	@classmethod
	def init():
		if proc913_0(59):
			super._send('init:', tTouchBust, 0, tTouchMouth, &rest)
		else:
			super._send('init:', tTouchBust, 0, tTouchMouth, tTouchGloves, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class GSight(GnomeTalker):
	#property vars (may be empty)
	x = 3
	y = 5
	view = 8935
	talkWidth = 208
	textX = 86
	textY = 8
	raveName = r"""SIGHT"""
	
	@classmethod
	def init():
		if proc913_0(59):
			super._send('init:', tSightBust, tSightEyes, tSightMouth, 0, &rest)
		else:
			super._send('init:', tSightBust, tSightLids, tSightMouth, 0, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tSmellBust(Prop):
	#property vars (may be empty)
	view = 8931
	
#end:class or instance

@SCI.instance
class tSmellEyes(Prop):
	#property vars (may be empty)
	nsTop = 15
	nsLeft = 12
	view = 8931
	loop = 1
	
#end:class or instance

@SCI.instance
class tSmellMouth(Prop):
	#property vars (may be empty)
	nsTop = 36
	nsLeft = 21
	view = 8931
	loop = 1
	
#end:class or instance

@SCI.instance
class tSmellPin(Prop):
	#property vars (may be empty)
	nsTop = 15
	nsLeft = 26
	view = 8931
	loop = 3
	
#end:class or instance

@SCI.instance
class tSoundBust(Prop):
	#property vars (may be empty)
	view = 8932
	
#end:class or instance

@SCI.instance
class tSoundEyes(Prop):
	#property vars (may be empty)
	nsTop = 15
	nsLeft = 20
	view = 8932
	loop = 1
	
#end:class or instance

@SCI.instance
class tSoundMouth(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 31
	view = 8932
	loop = 1
	
#end:class or instance

@SCI.instance
class tSoundMuffs(Prop):
	#property vars (may be empty)
	nsTop = 20
	nsLeft = 19
	view = 8932
	loop = 3
	
#end:class or instance

@SCI.instance
class tTasteBust(Prop):
	#property vars (may be empty)
	view = 8933
	
#end:class or instance

@SCI.instance
class tTasteEyes(Prop):
	#property vars (may be empty)
	nsTop = 8
	nsLeft = 20
	view = 8933
	loop = 1
	
#end:class or instance

@SCI.instance
class tTasteMouth(Prop):
	#property vars (may be empty)
	nsTop = 20
	nsLeft = 9
	view = 8933
	loop = 1
	
#end:class or instance

@SCI.instance
class tTouchBust(Prop):
	#property vars (may be empty)
	view = 8934
	
#end:class or instance

@SCI.instance
class tTouchEyes(Prop):
	#property vars (may be empty)
	nsTop = 2
	nsLeft = 16
	view = 8934
	loop = 1
	
#end:class or instance

@SCI.instance
class tTouchMouth(Prop):
	#property vars (may be empty)
	nsTop = 16
	nsLeft = 23
	view = 8934
	loop = 1
	
#end:class or instance

@SCI.instance
class tTouchGloves(Prop):
	#property vars (may be empty)
	nsTop = 28
	nsLeft = 8
	view = 8934
	loop = 3
	
#end:class or instance

@SCI.instance
class tSightBust(Prop):
	#property vars (may be empty)
	view = 8935
	
#end:class or instance

@SCI.instance
class tSightEyes(Prop):
	#property vars (may be empty)
	nsTop = 20
	nsLeft = 22
	view = 8935
	loop = 1
	
#end:class or instance

@SCI.instance
class tSightLids(Prop):
	#property vars (may be empty)
	nsTop = 19
	nsLeft = 21
	view = 8935
	loop = 3
	
#end:class or instance

@SCI.instance
class tSightMouth(Prop):
	#property vars (may be empty)
	nsTop = 30
	nsLeft = 33
	view = 8935
	loop = 2
	
#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8930
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 22
	nsLeft = 11
	view = 8930
	loop = 1
	
#end:class or instance

