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
			inset._send('dispose:')
		#endif
		if (argc and param1):
			param1._send(
				'init:', (param2 if (argc >= 2) else 0), self, if (argc >= 3):
						param3
					else:
						0
					#endif
			)
		#endif
	#end:method

	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		owner = param2
		owner._send('inset:', self)
		register = param3
		caller = param1
		if hideTheCast:
			self._send('hideCast:', 1)
		#endif
		oldCast = global5
		oldFeatures = global32
		oldATPs = global10
		oldMH = global73
		oldKH = global72
		oldDH = global74
		oldWH = global93
		oldObstacles = global2._send('obstacles:')
		global2._send('obstacles:', List._send('new:')._send('add:', 'yourself:'))
		global5 = EventHandler._send('new:')._send('name:', r"""newCast""", 'add:')
		global32 = EventHandler._send('new:')._send('name:', r"""newFeatures""", 'add:', self)
		global10 = EventHandler._send('new:')._send('name:', r"""newATPs""", 'add:')
		global73 = EventHandler._send('new:')._send('name:', r"""newMH""", 'add:', self)
		global72 = EventHandler._send('new:')._send('name:', r"""newKH""", 'add:', self)
		global74 = EventHandler._send('new:')._send('name:', r"""newDH""", 'add:', self)
		global93 = EventHandler._send('new:')._send('name:', r"""newWH""", 'add:')
		global78._send('add:', self)
		self._send('drawInset:')
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
				inView._send('new:')._send(
					'view:', view,
					'loop:', loop,
					'cel:', cel,
					'x:', x,
					'y:', y,
					'setPri:', priority,
					'ignoreActors:', 1,
					'init:',
					'yourself:'
				)
			)
		#endif
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('drawInset:')
		if inset:
			inset._send('oldATPs:')._send('doit:')
			inset._send('restore:')
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (inset and inset._send('handleEvent:', param1)): 0#end:case
			case (param1._send('type:') & 0x4000):
				(cond
					case self._send('onMe:', param1):
						param1._send('claimed:', 1)
						self._send('doVerb:', param1._send('message:'))
					#end:case
					case disposeNotOnMe:
						param1._send('claimed:', 1)
						self._send('dispose:')
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
			temp0 = param1._send('x:')
			temp1 = param1._send('y:')
		else:
			temp0 = param1
			temp1 = param2
		#endif
		if view:
			return insetView._send('onMe:', param1, param2)
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
			global91._send('say:', noun, param1, 0, 0, 0, modNum)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('doit:')
		#endif
		if (not hideTheCast):
			kernel.Animate(oldCast._send('elements:'), 0)
		#endif
	#end:method

	@classmethod
	def refresh():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case view:
				if global169:
					kernel.DrawPic(global2._send('picture:'), 15)
				else:
					kernel.DrawPic(global2._send('picture:'), 100)
				#endif
			#end:case
			case global169:
				kernel.DrawPic(global2._send('picture:'), 15)
			#end:case
			else:
				kernel.DrawPic(global2._send('picture:'), style)
			#end:else
		)
		global2._send('style:', oldStyle)
		if (global36 != -1):
			if global169:
				kernel.DrawPic(global36, 15, 0)
			else:
				kernel.DrawPic(global36, 100, 0)
			#endif
		#endif
		if global2._send('inset:'):
			global2._send('inset:')._send('restore:')
		#endif
	#end:method

	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global32._send('delete:', self)
		global73._send('delete:', self)
		global72._send('delete:', self)
		global74._send('delete:', self)
		global93._send('delete:', self)
		global78._send('delete:', self)
		if inset:
			inset._send('dispose:', 0)
		#endif
		global5._send(
			'eachElementDo:', #dispose,
			'eachElementDo:', #delete,
			'release:',
			'dispose:'
		)
		global10._send('dispose:')
		global32._send('dispose:')
		global73._send('dispose:')
		global72._send('dispose:')
		global74._send('dispose:')
		global93._send('dispose:')
		global2._send('obstacles:')._send('dispose:')
		owner._send('inset:', 0)
		if ((not argc) or param1):
			self._send('refresh:')
		#endif
		if ((not argc) or param1):
			global10 = oldATPs._send('doit:')
		#endif
		global2._send('obstacles:', oldObstacles)
		global5 = oldCast
		global32 = oldFeatures
		global73 = oldMH
		global72 = oldKH
		global74 = oldDH
		global93 = oldWH
		if hideTheCast:
			self._send('hideCast:', 0)
		#endif
		if (((not argc) or param1) and caller):
			temp0 = caller
			caller = 0
			temp0._send('cue:')
		#endif
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(script):
			script._send('dispose:')
		#endif
		script = (param1 if argc else 0)
		if script:
			script._send('init:', self, &rest)
		#endif
	#end:method

	@classmethod
	def hideCast(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		temp1 = (1000 if param1 else -1000)
		while (temp0 < global5._send('size:')):

			global5._send('at:', temp0)._send('z:', (global5._send('at:', temp0)._send('z:') + temp1))
			temp0.post('++')
		#end:loop
		kernel.Animate(global5._send('elements:'), 0)
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

