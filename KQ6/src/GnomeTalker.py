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
			(self x: 59 y: 15)
		#endif
		(self setSize:)
		(super init:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (raving and extra):
			kernel.DrawCel((extra view:), (extra loop:), (extra cel:), (+
				(extra nsLeft:)
				nsLeft
			), ((extra nsTop:) + nsTop), -1)
		#endif
		(super doit:)
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
						(bust nsLeft:)
						kernel.CelWide((bust view:), (bust loop:), (bust cel:))
					)
				), (and
					kernel.IsObject(eyes)
					(+
						(eyes nsLeft:)
						kernel.CelWide((eyes view:), (eyes loop:), (eyes cel:))
					)
				), (and
					kernel.IsObject(mouth)
					(+
						(mouth nsLeft:)
						kernel.CelWide((mouth view:), (mouth loop:), (mouth cel:))
					)
				), (and
					kernel.IsObject(extra)
					(+
						(extra nsLeft:)
						kernel.CelWide((extra view:), (extra loop:), (extra cel:))
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
						(bust nsTop:)
						kernel.CelHigh((bust view:), (bust loop:), (bust cel:))
					)
				), (and
					kernel.IsObject(eyes)
					(+
						(eyes nsTop:)
						kernel.CelHigh((eyes view:), (eyes loop:), (eyes cel:))
					)
				), (and
					kernel.IsObject(mouth)
					(+
						(mouth nsTop:)
						kernel.CelHigh((mouth view:), (mouth loop:), (mouth cel:))
					)
				), (and
					kernel.IsObject(extra)
					(+
						(extra nsTop:)
						kernel.CelHigh((extra view:), (extra loop:), (extra cel:))
					)
				))
			)
		)
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not underBits):
			underBits = kernel.Graph(7, nsTop, nsLeft, nsBottom, nsRight, 1)
		#endif
		temp0 = kernel.PicNotValid()
		kernel.PicNotValid(1)
		if bust:
			kernel.DrawCel((bust view:), (bust loop:), (bust cel:), (+
				(bust nsLeft:)
				nsLeft
			), ((bust nsTop:) + nsTop), -1)
		#endif
		if eyes:
			kernel.DrawCel((eyes view:), (eyes loop:), (eyes cel:), (+
				(eyes nsLeft:)
				nsLeft
			), ((eyes nsTop:) + nsTop), -1)
		#endif
		if mouth:
			kernel.DrawCel((mouth view:), (mouth loop:), (mouth cel:), (+
				(mouth nsLeft:)
				nsLeft
			), ((mouth nsTop:) + nsTop), -1)
		#endif
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1)
		if (extra and raving):
			kernel.DrawCel((extra view:), (extra loop:), (extra cel:), (+
				(extra nsLeft:)
				nsLeft
			), ((extra nsTop:) + nsTop), -1)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: tBust 0 tMouth &rest)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(super init: tSmellBust 0 tSmellMouth &rest)
		else:
			(super init: tSmellBust 0 tSmellMouth tSmellPin &rest)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(super init: tSoundBust 0 tSoundMouth &rest)
		else:
			(super init: tSoundBust 0 tSoundMouth tSoundMuffs &rest)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: tTasteBust 0 tTasteMouth &rest)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(super init: tTouchBust 0 tTouchMouth &rest)
		else:
			(super init: tTouchBust 0 tTouchMouth tTouchGloves &rest)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(super init: tSightBust tSightEyes tSightMouth 0 &rest)
		else:
			(super init: tSightBust tSightLids tSightMouth 0 &rest)
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

