#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 998
import sci_sh
import kernel
import Main
import Print
import PolyPath
import Feature
import Motion
import System

class View(Feature):
	#property vars (may be empty)
	yStep = 2
	view = -1
	loop = 0
	cel = 0
	priority = 0
	underBits = 0
	signal = 257
	lsTop = 0
	lsLeft = 0
	lsBottom = 0
	lsRight = 0
	brTop = 0
	brLeft = 0
	brBottom = 0
	brRight = 0
	scaleSignal = 0
	scaleX = 128
	scaleY = 128
	maxScale = 128
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (global10 if (signal & 0x0020) else global5)
		(signal &= 0x7fff)
		if (not (temp0 contains: self)):
			lsRight = lsBottom = lsLeft = lsTop = 0
			(signal &= 0xff77)
		#endif
		kernel.BaseSetter(self)
		(temp0 add: self)
		if (temp0 == global10):
			if (not (signal & 0x0010)):
				priority = kernel.CoordPri(y)
			#endif
			kernel.SetNowSeen(self)
			(temp0 doit:)
		#endif
		(self initialize: checkDetail:)
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			x = param1
			if (argc >= 2):
				y = param2
				if (argc >= 3):
					z = param3
				#endif
			#endif
		#endif
		kernel.BaseSetter(self)
		(self forceUpd:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self startUpd: hide:)
		(signal |= 0x8000)
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal |= 0x0008)
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal &= 0xfff7)
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x8000):
			(signal &= 0x7fff)
			(cond
				case (global10 contains: self):
					(global10 delete: self)
					(signal &= 0xffdf)
				#end:case
				case (signal & 0x0020):
					(global5 delete: self)
					(global10 add: self)
					return
				#end:case
				else:
					(global5 delete: self)
				#end:else
			)
			if underBits:
				kernel.UnLoad(133, underBits)
				underBits = 0
			#endif
			(super dispose:)
			if kernel.IsObject(actions):
				(actions dispose:)
			#endif
			actions = 0
		#endif
	#end:method

	@classmethod
	def stopUpd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal |= 0x0001)
		(signal &= 0xfffd)
	#end:method

	@classmethod
	def forceUpd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal |= 0x0040)
	#end:method

	@classmethod
	def startUpd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal |= 0x0002)
		(signal &= 0xfffe)
	#end:method

	@classmethod
	def setPri(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (argc == 0):
				(signal |= 0x0010)
			#end:case
			case (param1 == -1):
				(signal &= 0xffef)
			#end:case
			else:
				priority = param1
				(signal |= 0x0010)
			#end:else
		)
		(self forceUpd:)
	#end:method

	@classmethod
	def setLoop(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (argc == 0):
				(signal |= 0x0800)
			#end:case
			case (param1 == -1):
				(signal &= 0xf7ff)
			#end:case
			else:
				loop = param1
				(signal |= 0x0800)
			#end:else
		)
		(self forceUpd:)
	#end:method

	@classmethod
	def setCel(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (argc == 0): 0#end:case
			case (param1 == -1): 0#end:case
			else:
				(= cel
					if (param1 >= (self lastCel:)):
						(self lastCel:)
					else:
						param1
					#endif
				)
			#end:else
		)
		(self forceUpd:)
	#end:method

	@classmethod
	def ignoreActors(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((0 == argc) or param1):
			(signal |= 0x4000)
		else:
			(signal &= 0xbfff)
		#endif
	#end:method

	@classmethod
	def addToPic():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global5 contains: self):
			(signal |= 0x8021)
		else:
			(signal |= 0x0020)
			(self init:)
		#endif
	#end:method

	@classmethod
	def lastCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (kernel.NumCels(self) - 1)
	#end:method

	@classmethod
	def showSelf():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(Print addText: name addIcon: view loop cel init:)
	#end:method

	@classmethod
	def motionCue():#end:method

	@classmethod
	def checkDetail():#end:method

	@classmethod
	def isNotHidden():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (not (signal & 0x0088))
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
		(return
			(cond
				case (signal & 0x0080): 0#end:case
				case ((not kernel.IsObject(onMeCheck)) and (signal & 0x1000)):
					if 
						(or
							(not (nsLeft or nsRight or nsTop or nsBottom))
							(and
								(<= nsLeft temp0 nsRight)
								(<= nsTop temp1 nsBottom)
							)
						)
						(not
							kernel.IsItSkip(view, loop, cel, (temp1 - nsTop), (-
								temp0
								nsLeft
							))
						)
					#endif
				#end:case
				else:
					(super onMe: temp0 temp1)
				#end:else
			)
		)
	#end:method

	@classmethod
	def setScale(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not argc):
				(scaleSignal |= 0x0001)
				(scaleSignal &= 0xfffd)
			#end:case
			case (not param1):
				(scaleSignal &= 0xfffc)
			#end:case
			case (param1 < (global2 vanishingY:)):
				proc921_1(r"""<%s setScale:> y value less than vanishingY""", name)
			#end:case
			else:
				temp0 = (param1 - (global2 vanishingY:))
				temp2 = (((temp1 = (190 - param1) * 100) / temp0) + 100)
				(scaleSignal |= 0x0003)
				maxScale = ((temp2 * 128) / 100)
			#end:else
		)
	#end:method

#end:class or instance

class Prop(View):
	#property vars (may be empty)
	signal = 0
	cycleSpeed = 6
	script = 0
	cycler = 0
	timer = 0
	detailLevel = 0
	scaler = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x8000):
			return
		#endif
		if script:
			(script doit:)
		#endif
		if ((signal & 0x0004) and (not (signal & 0x0002))):
			return
		#endif
		if cycler:
			(cycler doit:)
		#endif
		if scaler:
			(scaler doit:)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			(script handleEvent: param1)
		#endif
		(super handleEvent: param1)
	#end:method

	@classmethod
	def setCycle(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if cycler:
			(cycler dispose:)
		#endif
		if param1:
			(self startUpd:)
			(= cycler
				if ((param1 -info-:) & 0x8000):
					(param1 new:)
				else:
					param1
				#endif
			)
			(cycler init: self &rest)
		else:
			cycler = 0
		#endif
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x8000):
			(self setScript: 0 setCycle: 0)
			if timer:
				(timer dispose:)
			#endif
			if kernel.IsObject(scaler):
				(scaler dispose:)
				scaler = 0
			#endif
			(super delete:)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			(script cue:)
		#endif
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(script):
			(script dispose:)
		#endif
		if param1:
			(param1 init: self &rest)
		#endif
	#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (cycler and (cycler completed:)):
			(cycler motionCue:)
		#endif
	#end:method

	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						(global1 detailLevel:)
					#endif
					detailLevel
				):
				(self stopUpd:)
			#end:case
			case cycler:
				(self startUpd:)
			#end:case
		)
	#end:method

	@classmethod
	def setScale(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if scaler:
			(scaler dispose:)
			scaler = 0
		#endif
		(cond
			case (not argc):
				(super setScale:)
			#end:case
			case kernel.IsObject(param1):
				(scaleSignal |= 0x0001)
				(scaleSignal &= 0xfffd)
				(= scaler
					if ((param1 -info-:) & 0x8000):
						(param1 new:)
					else:
						param1
					#endif
				)
				(scaler init: self param2 &rest)
			#end:case
			case (param1 == -1):
				if (param2 scaleSignal:):
					scaleSignal = (param2 scaleSignal:)
					maxScale = (param2 maxScale:)
					if kernel.IsObject((param2 scaler:)):
						(scaler = ((param2 scaler:) new:) client: self)
					#endif
				#endif
			#end:case
			else:
				(super setScale: param1)
			#end:else
		)
	#end:method

#end:class or instance

class Actor(Prop):
	#property vars (may be empty)
	illegalBits = -32768
	xLast = 0
	yLast = 0
	xStep = 3
	origStep = 770
	moveSpeed = 6
	blocks = 0
	baseSetter = 0
	mover = 0
	looper = 0
	viewer = 0
	avoider = 0
	code = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		xLast = x
		yLast = y
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x8000):
			return
		#endif
		if script:
			(script doit:)
		#endif
		if code:
			(code doit: self)
		#endif
		if ((signal & 0x0004) and (not (signal & 0x0002))):
			return
		#endif
		if viewer:
			(viewer doit: self)
		#endif
		if avoider:
			(avoider doit:)
		#endif
		if mover:
			if ((scaleSignal & 0x0001) and (not (scaleSignal & 0x0004))):
				temp5 = (origStep >> 0x0008)
				temp6 = (origStep & 0x00ff)
				temp3 = (temp7 if temp7 = ((temp5 * scaleX) / 128) else 1)
				temp4 = (temp7 if temp7 = ((temp6 * scaleY) / 128) else 1)
				if ((temp3 != xStep) or (temp4 != yStep)):
					(self setStep: temp3 temp4 1)
				#endif
			#endif
			if mover:
				(mover doit:)
			#endif
		#endif
		if scaler:
			(scaler doit:)
		#endif
		if cycler:
			temp1 = brLeft
			temp2 = brRight
			(cycler doit:)
			if baseSetter:
				(baseSetter doit: self)
			else:
				kernel.BaseSetter(self)
			#endif
		#endif
		xLast = x
		yLast = y
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super posn: param1 param2 &rest)
		xLast = param1
		yLast = param2
	#end:method

	@classmethod
	def setMotion(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (mover and (mover != -1)):
			(mover dispose:)
		#endif
		if param1:
			(self startUpd:)
			(= mover
				if ((param1 -info-:) & 0x8000):
					(param1 new:)
				else:
					param1
				#endif
			)
			(mover init: self &rest)
		else:
			mover = 0
		#endif
	#end:method

	@classmethod
	def setAvoider(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if avoider:
			(avoider dispose:)
		#endif
		(= avoider
			if (kernel.IsObject(param1) and ((param1 -info-:) & 0x8000)):
				(param1 new:)
			else:
				param1
			#endif
		)
		if avoider:
			(avoider init: self &rest)
		#endif
	#end:method

	@classmethod
	def isStopped():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(or
				(not kernel.IsObject(mover))
				((x == (mover xLast:)) and (y == (mover yLast:)))
			)
		)
	#end:method

	@classmethod
	def isBlocked():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (signal & 0x0400)
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x8000):
			if (mover != -1):
				(self setMotion: 0)
			#endif
			(self setAvoider: 0)
			if baseSetter:
				(baseSetter dispose:)
				baseSetter = 0
			#endif
			if looper:
				(looper dispose:)
				looper = 0
			#endif
			if viewer:
				(viewer dispose:)
				viewer = 0
			#endif
			if blocks:
				(blocks dispose:)
				blocks = 0
			#endif
			if code:
				(code dispose:)
				code = 0
			#endif
			if kernel.IsObject(actions):
				(actions dispose:)
				actions = 0
			#endif
			(super delete:)
		#endif
	#end:method

	@classmethod
	def ignoreHorizon(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not argc) or param1):
			(signal |= 0x2000)
		else:
			(signal &= 0xdfff)
		#endif
	#end:method

	@classmethod
	def observeControl(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < argc): # inline for
			(illegalBits |= param1[temp0])
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def ignoreControl(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < argc): # inline for
			(illegalBits &= ~param1[temp0])
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def observeBlocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not blocks):
			blocks = (Set new:)
		#endif
		(blocks add: &rest)
	#end:method

	@classmethod
	def ignoreBlocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if blocks:
			(blocks delete: &rest)
			if (blocks isEmpty:):
				(blocks dispose:)
				blocks = 0
			#endif
		#endif
	#end:method

	@classmethod
	def distanceTo(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.GetDistance(x, y, (param1 x:), (param1 y:), global31)
	#end:method

	@classmethod
	def cantBeHere():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if baseSetter:
			(baseSetter doit: self)
		else:
			kernel.BaseSetter(self)
		#endif
		(= temp0
			(cond
				case kernel.CantBeHere(self, (global5 elements:)):#end:case
				case 
					(and
						(not (signal & 0x2000))
						kernel.IsObject(global2)
						(y < (global2 horizon:))
					):
					-1
				#end:case
				case (blocks and (not (blocks allTrue: #doit self))): -2#end:case
			)
		)
	#end:method

	@classmethod
	def inRect(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return ((param1 <= x) and (x <= param3) and (param2 <= y) and (y <= param4))
	#end:method

	@classmethod
	def onControl(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc and param1):
			kernel.OnControl(4, x, y)
		else:
			kernel.OnControl(4, brLeft, brTop, brRight, brBottom)
		#endif
	#end:method

	@classmethod
	def setStep(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (origStep >> 0x0008)
		temp1 = (origStep & 0x00ff)
		if ((argc >= 1) and (param1 != -1)):
			temp0 = param1
		#endif
		if ((argc >= 2) and (param2 != -1)):
			temp1 = param2
		#endif
		if ((argc < 3) or (not param3)):
			origStep = ((temp0 << 0x0008) + temp1)
		#endif
		xStep = temp0
		yStep = temp1
		if 
			(and
				kernel.IsObject(mover)
				((mover isMemberOf: MoveTo) or (mover isMemberOf: PolyPath))
			)
			(mover init:)
		#endif
	#end:method

	@classmethod
	def setDirection(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= temp0
			if (temp1 = (global2 vanishingY:) == -30000):
				x
			else:
				(global2 vanishingX:)
			#endif
		)
		if ((xStep == 0) and (yStep == 0)):
			return
		#endif
		temp5 = (32000 / proc999_3(xStep, yStep))
		match param1
			case 0:
				(self setMotion: 0)
				return
			#end:case
			case 1:
				temp2 = (temp0 - x)
				temp3 = (temp1 - y)
			#end:case
			case 5:
				temp2 = (x - temp0)
				temp3 = (y - temp1)
			#end:case
			case 3:
				temp2 = temp5
				temp3 = 0
			#end:case
			case 7:
				temp2 = -temp5
				temp3 = 0
			#end:case
			else:
				if (180 < temp4 = kernel.GetAngle(x, y, temp0, temp1)):
					(temp4 -= 360)
				#endif
				temp4 = (((temp4 + 90) / 2) + (45 * (param1 - 2)))
				temp2 = kernel.SinMult(temp4, 100)
				temp3 = -kernel.CosMult(temp4, 100)
			#end:else
		#end:match
		(temp5 /= 5)
		while ((kernel.Abs(temp3) < temp5) and (kernel.Abs(temp2) < temp5)):

			(temp2 *= 5)
			(temp3 *= 5)
		#end:loop
		if (temp7 = (global2 obstacles:) and global67):
			(= temp6
				kernel.AvoidPath(x, y, (x + temp2), (y + temp3), (temp7
					elements:
				), (temp7 size:), 0)
			)
			temp2 = (proc999_6(temp6, 2) - x)
			temp3 = (proc999_6(temp6, 3) - y)
			kernel.Memory(3, temp6)
		#endif
		(cond
			case (temp2 or temp3):
				(self setMotion: MoveTo (x + temp2) (y + temp3))
			#end:case
			case param1:
				(self setMotion: 0 setHeading: ((param1 - 1) * 45))
			#end:case
			else:
				(self setMotion: 0)
			#end:else
		)
	#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (mover and (mover completed:)):
			(mover motionCue:)
		#endif
		(super motionCue:)
	#end:method

	@classmethod
	def setLoop(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(= temp0
				(cond
					case (argc == 0):
						(super setLoop:)
						0
					#end:case
					case (not kernel.IsObject(param1)):
						(super setLoop: param1 &rest)
						0
					#end:case
					case ((param1 -info-:) & 0x8000):
						(param1 new:)
					#end:case
					else: param1#end:else
				)
			)
			if looper:
				(looper dispose:)
			#endif
			(looper = temp0 init: self &rest)
		#endif
	#end:method

	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						(global1 detailLevel:)
					#endif
					detailLevel
				):
				(self stopUpd:)
			#end:case
			case (cycler or mover):
				(self startUpd:)
			#end:case
		)
	#end:method

	@classmethod
	def setHeading(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			heading = param1
		#endif
		if looper:
			(looper doit: self heading ((argc >= 2) and param2))
		else:
			kernel.DirLoop(self, heading)
			if ((argc >= 2) and kernel.IsObject(param2)):
				(param2 cue: &rest)
			#endif
		#endif
		return heading
	#end:method

	@classmethod
	def setSpeed(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			moveSpeed = cycleSpeed = param1
		#endif
		return moveSpeed
	#end:method

#end:class or instance

