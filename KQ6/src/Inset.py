#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 923
import sci_sh
import kernel
import Main
import Actor
import System

class Inset(Code):
	#property vars (may be empty)
	picture = 0
	anOverlay = 0
	style = 100
	view = 0
	loop = 0
	cel = 0
	x = 0
	y = 0
	priority = 14
	register = 0
	hideTheCast = 0
	caller = 0
	owner = 0
	script = 0
	oldCast = 0
	oldFeatures = 0
	oldATPs = 0
	oldMH = 0
	oldKH = 0
	oldDH = 0
	oldWH = 0
	oldObstacles = 0
	oldStyle = 0
	inset = 0
	disposeNotOnMe = 0
	modNum = -1
	noun = 0
	insetView = 0
	
	@classmethod
	def setInset(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if inset:
			(inset dispose:)
		#endif
		if (argc and param1):
			(param1
				init:
					(param2 if (argc >= 2) else 0)
					self
					(param3 if (argc >= 3) else 0)
			)
		#endif
	#end:method

	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		owner = param2
		(owner inset: self)
		register = param3
		caller = param1
		if hideTheCast:
			(self hideCast: 1)
		#endif
		oldCast = global5
		oldFeatures = global32
		oldATPs = global10
		oldMH = global73
		oldKH = global72
		oldDH = global74
		oldWH = global93
		oldObstacles = (global2 obstacles:)
		(global2 obstacles: ((List new:) add: yourself:))
		(global5 = (EventHandler new:) name: r"""newCast""" add:)
		(global32 = (EventHandler new:) name: r"""newFeatures""" add: self)
		(global10 = (EventHandler new:) name: r"""newATPs""" add:)
		(global73 = (EventHandler new:) name: r"""newMH""" add: self)
		(global72 = (EventHandler new:) name: r"""newKH""" add: self)
		(global74 = (EventHandler new:) name: r"""newDH""" add: self)
		(global93 = (EventHandler new:) name: r"""newWH""" add:)
		(global78 add: self)
		(self drawInset:)
	#end:method

	@classmethod
	def drawInset():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (picture > 0):
			if global169:
				kernel.DrawPic(picture, 15, (0 if anOverlay else 1))
			else:
				kernel.DrawPic(picture, (100 if anOverlay else style), if 
					anOverlay
					0
				else:
					1
				#endif)
			#endif
		#endif
		if view:
			(= insetView
				((inView new:)
					view: view
					loop: loop
					cel: cel
					x: x
					y: y
					setPri: priority
					ignoreActors: 1
					init:
					yourself:
				)
			)
		#endif
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self drawInset:)
		if inset:
			((inset oldATPs:) doit:)
			(inset restore:)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (inset and (inset handleEvent: param1)): 0#end:case
			case ((param1 type:) & 0x4000):
				(cond
					case (self onMe: param1):
						(param1 claimed: 1)
						(self doVerb: (param1 message:))
					#end:case
					case disposeNotOnMe:
						(param1 claimed: 1)
						(self dispose:)
					#end:case
					else:
						return 0
					#end:else
				)
			#end:case
		)
	#end:method

	@classmethod
	def onMe(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(param1):
			temp0 = (param1 x:)
			temp1 = (param1 y:)
		else:
			temp0 = param1
			temp1 = param2
		#endif
		if view:
			return (insetView onMe: param1 param2)
		else:
			return 1
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (modNum == -1):
			modNum = global11
		#endif
		if (global90 and kernel.Message(0, modNum, noun, param1, 0, 1)):
			(global91 say: noun param1 0 0 0 modNum)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			(script doit:)
		#endif
		if (not hideTheCast):
			kernel.Animate((oldCast elements:), 0)
		#endif
	#end:method

	@classmethod
	def refresh():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case view:
				if global169:
					kernel.DrawPic((global2 picture:), 15)
				else:
					kernel.DrawPic((global2 picture:), 100)
				#endif
			#end:case
			case global169:
				kernel.DrawPic((global2 picture:), 15)
			#end:case
			else:
				kernel.DrawPic((global2 picture:), style)
			#end:else
		)
		(global2 style: oldStyle)
		if (global36 != -1):
			if global169:
				kernel.DrawPic(global36, 15, 0)
			else:
				kernel.DrawPic(global36, 100, 0)
			#endif
		#endif
		if (global2 inset:):
			((global2 inset:) restore:)
		#endif
	#end:method

	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global32 delete: self)
		(global73 delete: self)
		(global72 delete: self)
		(global74 delete: self)
		(global93 delete: self)
		(global78 delete: self)
		if inset:
			(inset dispose: 0)
		#endif
		(global5
			eachElementDo: #dispose
			eachElementDo: #delete
			release:
			dispose:
		)
		(global10 dispose:)
		(global32 dispose:)
		(global73 dispose:)
		(global72 dispose:)
		(global74 dispose:)
		(global93 dispose:)
		((global2 obstacles:) dispose:)
		(owner inset: 0)
		if ((not argc) or param1):
			(self refresh:)
		#endif
		if ((not argc) or param1):
			(global10 = oldATPs doit:)
		#endif
		(global2 obstacles: oldObstacles)
		global5 = oldCast
		global32 = oldFeatures
		global73 = oldMH
		global72 = oldKH
		global74 = oldDH
		global93 = oldWH
		if hideTheCast:
			(self hideCast: 0)
		#endif
		if (((not argc) or param1) and caller):
			temp0 = caller
			caller = 0
			(temp0 cue:)
		#endif
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(script):
			(script dispose:)
		#endif
		script = (param1 if argc else 0)
		if script:
			(script init: self &rest)
		#endif
	#end:method

	@classmethod
	def hideCast(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		temp1 = (1000 if param1 else -1000)
		while (temp0 < (global5 size:)):

			((global5 at: temp0) z: (((global5 at: temp0) z:) + temp1))
			temp0.post('++')
		#end:loop
		kernel.Animate((global5 elements:), 0)
	#end:method

#end:class or instance

@SCI.instance
class inView(View):
	#property vars (may be empty)
	@classmethod
	def handleEvent():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 0
	#end:method

#end:class or instance

