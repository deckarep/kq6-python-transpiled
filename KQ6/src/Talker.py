#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 928
import sci_sh
import kernel
import Main
import Print
import Sync
import RandCycle
import Motion
import Actor
import System

class Blink(Cycle):
	#property vars (may be empty)
	waitCount = 0
	lastCount = 0
	waitMin = 0
	waitMax = 0
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			waitMin = (param2 / 2)
			waitMax = (param2 + waitMin)
			super._send('init:', param1)
		else:
			super._send('init:')
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case waitCount:
				if ((global88 - waitCount) > 0):
					waitCount = 0
					self._send('init:')
				#endif
			#end:case
			case 
				((temp0 = self._send('nextCel:') > client._send('lastCel:')) or (temp0 < 0)):
				cycleDir = -cycleDir
				self._send('cycleDone:')
			#end:case
			else:
				client._send('cel:', temp0)
			#end:else
		)
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (cycleDir == -1):
			self._send('init:')
		else:
			waitCount = (kernel.Random(waitMin, waitMax) + global88)
		#endif
	#end:method

#end:class or instance

class Narrator(Prop):
	#property vars (may be empty)
	x = -1
	y = -1
	caller = 0
	disposeWhenDone = 1
	ticks = 0
	talkWidth = 0
	keepWindow = 0
	modeless = 0
	font = 0
	cueVal = 0
	initialized = 0
	showTitle = 0
	color = 0
	back = 7
	curVolume = 0
	saveCursor = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global90 & 0x0002):
			curVolume = global1._send('masterVolume:')
			if (curVolume >= 4):
				global1._send('masterVolume:', curVolume)
				temp2 = curVolume
				
					(temp0 = curVolume)
					(temp0 >= proc999_3(3, (curVolume / 2)))
					(temp0.post('--'))
					
					global1._send('masterVolume:', temp0)
					temp1 = 0
					while (temp1 <= 400): # inline for
					#end:loop
					# for:reinit
					temp0.post('--')
				#end:loop
			#endif
		#endif
		if (((global90 & 0x0002) and (not modeless)) or (not kernel.HaveMouse())):
			saveCursor = global1._send('setCursor:', global21, 1)
		#endif
		global88 = (global86 + kernel.GetTime())
		initialized = 1
	#end:method

	@classmethod
	def say(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global69:
			global69._send('disable:')
		#endif
		if (not initialized):
			self._send('init:')
		#endif
		caller = (param2 if ((argc > 1) and param2) else 0)
		if (global90 & 0x0001):
			self._send('startText:', param1)
		#endif
		if (global90 & 0x0002):
			self._send('startAudio:', param1)
		#endif
		(cond
			case modeless:
				global73._send('addToFront:', self)
				global72._send('addToFront:', self)
				global78._send('add:', self)
			#end:case
			case kernel.IsObject(global84):
				global84._send('add:', self)
			#end:case
			else:
				global84 = EventHandler._send('new:')._send(
					'name:', r"""fastCast""",
					'add:', self
				)
			#end:else
		)
		(ticks += (60 + global88))
		return 1
	#end:method

	@classmethod
	def startText(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (global90 & 0x0002)):
			ticks = proc999_3(240, (* global94 2 temp0 = kernel.StrLen(param1)))
		#endif
		if global25:
			global25._send('dispose:')
		#endif
		self._send('display:', param1)
		return temp0
	#end:method

	@classmethod
	def display(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((x + talkWidth) > 318):
			temp0 = (318 - x)
		else:
			temp0 = talkWidth
		#endif
		temp1 = global38._send('new:')._send('color:', color, 'back:', back)
		if ((not kernel.HaveMouse()) and (global19 != 996)):
			saveCursor = global19
			global1._send('setCursor:', 996)
		else:
			saveCursor = 0
		#endif
		if showTitle:
			Print._send('addTitle:', name)
		#endif
		Print._send(
			'window:', temp1,
			'posn:', x, y,
			'font:', font,
			'width:', temp0,
			'addText:', param1,
			'modeless:', 1,
			'init:'
		)
	#end:method

	@classmethod
	def startAudio(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = proc999_6(param1, 0)
		temp1 = proc999_6(param1, 1)
		temp2 = proc999_6(param1, 2)
		temp3 = proc999_6(param1, 3)
		temp4 = proc999_6(param1, 4)
		ticks = kernel.DoAudio(2, temp0, temp1, temp2, temp3, temp4)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(ticks != -1)
				((global88 - ticks) > 0)
				if (global90 & 0x0002):
					(kernel.DoAudio(6) == -1)
				else:
					1
				#endif
				((not keepWindow) or (global90 & 0x0002))
			)
			self._send('dispose:', disposeWhenDone)
			return 0
		#endif
		return 1
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case param1._send('claimed:'):#end:case
			case (ticks == -1):
				return 0
			#end:case
			else:
				if (not cueVal):
					match param1._send('type:')
						case 256:
							cueVal = 0
						#end:case
						case 1:
							cueVal = (param1._send('modifiers:') & 0x0003)
						#end:case
						case 4:
							cueVal = (param1._send('message:') == 27)
						#end:case
					#end:match
				#endif
				if 
					(or
						(param1._send('type:') & 0x4101)
						(and
							(param1._send('type:') & 0x0004)
							proc999_5(param1._send('message:'), 13, 27)
						)
					)
					param1._send('claimed:', 1)
					self._send('dispose:', disposeWhenDone)
				#endif
			#end:else
		)
	#end:method

	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		ticks = -1
		if ((not argc) or (param1 == 1)):
			(cond
				case modeless:
					global72._send('delete:', self)
					global73._send('delete:', self)
					global78._send('delete:', self)
				#end:case
				case (global84 and global84._send('contains:', self)):
					global84._send('delete:', self)
					if global84._send('isEmpty:'):
						global84._send('dispose:')
						global84 = 0
					#endif
				#end:case
			)
			if (global90 & 0x0002):
				kernel.DoAudio(3)
			#endif
			modNum = -1
			initialized = 0
		#endif
		if global25:
			global25._send('dispose:')
		#endif
		if (global90 & 0x0002):
			
				(temp0 = global1._send('masterVolume:'))
				(temp0 <= curVolume)
				(temp0.post('++'))
				
				global1._send('masterVolume:', temp0)
				temp1 = 0
				while (temp1 <= 400): # inline for
				#end:loop
				# for:reinit
				temp0.post('++')
			#end:loop
		#endif
		if (((global90 & 0x0002) and (not modeless)) or (not kernel.HaveMouse())):
			global1._send('setCursor:', saveCursor)
		#endif
		if caller:
			caller._send('cue:', cueVal)
		#endif
		cueVal = 0
		kernel.DisposeClone(self)
	#end:method

#end:class or instance

class Talker(Narrator):
	#property vars (may be empty)
	talkWidth = 318
	bust = 0
	eyes = 0
	mouth = 0
	viewInPrint = 0
	textX = 0
	textY = 0
	useFrame = 0
	blinkSpeed = 100
	raving = 0
	raveName = 0
	saveX = 0
	saveY = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if raving:
			mouth = eyes = bust = 0
		else:
			if argc:
				bust = param1
				if (argc > 1):
					eyes = param2
					if (argc > 2):
						mouth = param3
					#endif
				#endif
			#endif
			self._send('setSize:')
		#endif
		super._send('init:')
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
				))
			)
		)
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not underBits):
			underBits = kernel.Graph(7, nsTop, nsLeft, nsBottom, nsRight, 3)
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
		kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
		kernel.PicNotValid(temp0)
	#end:method

	@classmethod
	def showRave(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not underBits):
			(= underBits
				kernel.Graph(15, y, x, (y + ((kernel.CelHigh(5, 0, 0) * 5) / 11)), (+
					x
					(kernel.CelWide(5, 0, 0) / 2)
				))
			)
			kernel.DrawCel(5, 0, 0, 0, 0, -1, 0, underBits)
			temp0 = 0
		else:
			temp0 = 1
		#endif
		if 
			(==
				kernel.Portrait(1, raveName, (x + 4), (y - 7), param1, param2, param3, param4, param5, temp0)
				2
			)
			cueVal = 27
		else:
			cueVal = 0
		#endif
	#end:method

	@classmethod
	def say():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((view > 0) and (not underBits)):
			self._send('init:')
		#endif
		super._send('say:', &rest)
	#end:method

	@classmethod
	def startText():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not viewInPrint):
			self._send('show:')
		#endif
		temp0 = super._send('startText:', &rest)
		if mouth:
			mouth._send('setCycle:', RandCycle, (4 * temp0), 0, 1)
		#endif
		if (eyes and (not eyes._send('cycler:'))):
			eyes._send('setCycle:', Blink, blinkSpeed)
		#endif
	#end:method

	@classmethod
	def display(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp3 = global38._send('new:')._send('color:', color, 'back:', back)
		if ((not kernel.HaveMouse()) and (global19 != 996)):
			saveCursor = global19
			global1._send('setCursor:', 996)
		else:
			saveCursor = 0
		#endif
		if viewInPrint:
			(= temp0
				if useFrame:
					loop
				else:
					bust._send('loop:')
				#endif
			)
			if showTitle:
				Print._send('addTitle:', name)
			#endif
			Print._send(
				'window:', temp3,
				'posn:', x, y,
				'modeless:', 1,
				'font:', font,
				'addText:', param1,
				'addIcon:', view, temp0, cel, 0, 0,
				'init:'
			)
		else:
			if (not (textX + textY)):
				textX = ((nsRight - nsLeft) + 5)
			#endif
			if ((temp2 = (nsLeft + textX) + talkWidth) > 318):
				temp1 = (318 - temp2)
			else:
				temp1 = talkWidth
			#endif
			if showTitle:
				Print._send('addTitle:', name)
			#endif
			Print._send(
				'window:', temp3,
				'posn:', (x + textX), (y + textY),
				'modeless:', 1,
				'font:', font,
				'width:', temp1,
				'addText:', param1,
				'init:'
			)
		#endif
	#end:method

	@classmethod
	def startAudio(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (raving or ((not raving) and mouth)):
			temp0 = proc999_6(param1, 0)
			temp1 = proc999_6(param1, 1)
			temp2 = proc999_6(param1, 2)
			temp3 = proc999_6(param1, 3)
			temp4 = proc999_6(param1, 4)
		#endif
		if (raving and raveName):
			self._send('showRave:', temp0, temp1, temp2, temp3, temp4)
		else:
			self._send('show:')
			if mouth:
				if kernel.ResCheck(147, temp0, temp1, temp2, temp3, temp4):
					mouth._send('setCycle:', MouthSync, temp0, temp1, temp2, temp3, temp4)
					super._send('startAudio:', param1)
				else:
					temp18 = super._send('startAudio:', param1)
					mouth._send('setCycle:', RandCycle, (temp18 * 4), 0, 1)
				#endif
			else:
				super._send('startAudio:', param1)
			#endif
			if (eyes and (not eyes._send('cycler:'))):
				eyes._send('setCycle:', Blink, blinkSpeed)
			#endif
		#endif
	#end:method

	@classmethod
	def cycle(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 and param1._send('cycler:')):
			temp0 = param1._send('cel:')
			param1._send('cycler:')._send('doit:')
			if (temp0 != param1._send('cel:')):
				kernel.DrawCel(param1._send('view:'), param1._send('loop:'), param1._send(
					'cel:'
				), (param1._send('nsLeft:') + nsLeft), (param1._send('nsTop:') + nsTop), -1)
				param1._send(
					'nsRight:', (+
							param1._send('nsLeft:')
							kernel.CelWide(param1._send('view:'), param1._send('loop:'), param1._send(
								'cel:'
							))
						)
				)
				param1._send(
					'nsBottom:', (+
							param1._send('nsTop:')
							kernel.CelHigh(param1._send('view:'), param1._send('loop:'), param1._send(
								'cel:'
							))
						)
				)
				kernel.Graph(12, (param1._send('nsTop:') + nsTop), (+
					param1._send('nsLeft:')
					nsLeft
				), (param1._send('nsBottom:') + nsTop), (+
					param1._send('nsRight:')
					nsLeft
				), 1)
			#endif
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (super._send('doit:') and mouth):
			self._send('cycle:', mouth)
		#endif
		if eyes:
			self._send('cycle:', eyes)
		#endif
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Graph(8, underBits)
		underBits = 0
		kernel.Graph(13, nsTop, nsLeft, nsBottom, nsRight)
		if global69:
			global69._send('enable:')
		#endif
	#end:method

	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (mouth and underBits):
			mouth._send('cel:', 0)
			kernel.DrawCel(mouth._send('view:'), mouth._send('loop:'), 0, (+
				mouth._send('nsLeft:')
				nsLeft
			), (mouth._send('nsTop:') + nsTop), -1)
		#endif
		if (mouth and mouth._send('cycler:')):
			if mouth._send('cycler:')._send('respondsTo:', #cue):
				mouth._send('cycler:')._send('cue:')
			#endif
			mouth._send('setCycle:', 0)
		#endif
		if ((not argc) or (param1 == 1)):
			if raving:
				kernel.Graph(8, underBits)
				kernel.Graph(13, (y - 10), (x - 10), (+
					10
					(y - 10)
					((kernel.CelHigh(5, 0, 0) * 5) / 11)
				), (+ 10 (x - 10) (kernel.CelWide(5, 0, 0) / 2)))
				raving = underBits = 0
			#endif
			if (eyes and underBits):
				eyes._send('setCycle:', 0, 'cel:', 0)
				kernel.DrawCel(eyes._send('view:'), eyes._send('loop:'), 0, (+
					eyes._send('nsLeft:')
					nsLeft
				), (eyes._send('nsTop:') + nsTop), -1)
			#endif
			if saveX:
				x = saveX
				y = saveY
			#endif
			saveY = saveX = 0
			self._send('hide:')
		#endif
		super._send('dispose:', param1)
	#end:method

#end:class or instance

