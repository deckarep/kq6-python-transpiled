#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 928
import sci_sh
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
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			waitMin = (param2 / 2)
			waitMax = (param2 + waitMin)
			(super init: param1)
		else:
			(super init:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case waitCount:
				if ((global88 - waitCount) > 0):
					waitCount = 0
					(self init:)
				#endif
			#end:case
			case 
				((temp0 = (self nextCel:) > (client lastCel:)) or (temp0 < 0)):
				cycleDir = (- cycleDir)
				(self cycleDone:)
			#end:case
			else:
				(client cel: temp0)
			#end:else
		)
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (cycleDir == -1):
			(self init:)
		else:
			waitCount = ((Random waitMin waitMax) + global88)
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
		argc = sum(v is not None for v in locals().values())

		if (global90 & 0x0002):
			curVolume = (global1 masterVolume:)
			if (curVolume >= 4):
				(global1 masterVolume: curVolume)
				temp2 = curVolume
				
					(temp0 = curVolume)
					(temp0 >= (proc999_3 3 (curVolume / 2)))
					(temp0--)
					
					(global1 masterVolume: temp0)
					temp1 = 0
					while (temp1 <= 400): # inline for
					#end:loop
					# for:reinit
					temp0--
				#end:loop
			#endif
		#endif
		if (((global90 & 0x0002) and (not modeless)) or (not (HaveMouse))):
			saveCursor = (global1 setCursor: global21 1)
		#endif
		global88 = (global86 + (GetTime))
		initialized = 1
	#end:method

	@classmethod
	def say(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if global69:
			(global69 disable:)
		#endif
		if (not initialized):
			(self init:)
		#endif
		caller = (param2 if ((argc > 1) and param2) else 0)
		if (global90 & 0x0001):
			(self startText: param1)
		#endif
		if (global90 & 0x0002):
			(self startAudio: param1)
		#endif
		(cond
			case modeless:
				(global73 addToFront: self)
				(global72 addToFront: self)
				(global78 add: self)
			#end:case
			case (IsObject global84):
				(global84 add: self)
			#end:case
			else:
				(global84 = (EventHandler new:)
					name: r"""fastCast"""
					add: self
				)
			#end:else
		)
		(ticks += (60 + global88))
		return 1
	#end:method

	@classmethod
	def startText(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (global90 & 0x0002)):
			ticks = (proc999_3 240 (* global94 2 temp0 = (StrLen param1)))
		#endif
		if global25:
			(global25 dispose:)
		#endif
		(self display: param1)
		return temp0
	#end:method

	@classmethod
	def display(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((x + talkWidth) > 318):
			temp0 = (318 - x)
		else:
			temp0 = talkWidth
		#endif
		(temp1 = (global38 new:) color: color back: back)
		if ((not (HaveMouse)) and (global19 != 996)):
			saveCursor = global19
			(global1 setCursor: 996)
		else:
			saveCursor = 0
		#endif
		if showTitle:
			(Print addTitle: name)
		#endif
		(Print
			window: temp1
			posn: x y
			font: font
			width: temp0
			addText: param1
			modeless: 1
			init:
		)
	#end:method

	@classmethod
	def startAudio(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (proc999_6 param1 0)
		temp1 = (proc999_6 param1 1)
		temp2 = (proc999_6 param1 2)
		temp3 = (proc999_6 param1 3)
		temp4 = (proc999_6 param1 4)
		ticks = (DoAudio 2 temp0 temp1 temp2 temp3 temp4)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(ticks != -1)
				((global88 - ticks) > 0)
				if (global90 & 0x0002):
					((DoAudio 6) == -1)
				else:
					1
				#endif
				((not keepWindow) or (global90 & 0x0002))
			)
			(self dispose: disposeWhenDone)
			return 0
		#endif
		return 1
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 claimed:):#end:case
			case (ticks == -1):
				return 0
			#end:case
			else:
				if (not cueVal):
					match (param1 type:)
						case 256:
							cueVal = 0
						#end:case
						case 1:
							cueVal = ((param1 modifiers:) & 0x0003)
						#end:case
						case 4:
							cueVal = ((param1 message:) == 27)
						#end:case
					#end:match
				#endif
				if 
					(or
						((param1 type:) & 0x4101)
						(and
							((param1 type:) & 0x0004)
							(proc999_5 (param1 message:) 13 27)
						)
					)
					(param1 claimed: 1)
					(self dispose: disposeWhenDone)
				#endif
			#end:else
		)
	#end:method

	@classmethod
	def dispose(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		ticks = -1
		if ((not argc) or (param1 == 1)):
			(cond
				case modeless:
					(global72 delete: self)
					(global73 delete: self)
					(global78 delete: self)
				#end:case
				case (global84 and (global84 contains: self)):
					(global84 delete: self)
					if (global84 isEmpty:):
						(global84 dispose:)
						global84 = 0
					#endif
				#end:case
			)
			if (global90 & 0x0002):
				(DoAudio 3)
			#endif
			modNum = -1
			initialized = 0
		#endif
		if global25:
			(global25 dispose:)
		#endif
		if (global90 & 0x0002):
			
				(temp0 = (global1 masterVolume:))
				(temp0 <= curVolume)
				(temp0++)
				
				(global1 masterVolume: temp0)
				temp1 = 0
				while (temp1 <= 400): # inline for
				#end:loop
				# for:reinit
				temp0++
			#end:loop
		#endif
		if (((global90 & 0x0002) and (not modeless)) or (not (HaveMouse))):
			(global1 setCursor: saveCursor)
		#endif
		if caller:
			(caller cue: cueVal)
		#endif
		cueVal = 0
		(DisposeClone self)
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
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
			(self setSize:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		nsLeft = x
		nsTop = y
		(= nsRight
			(+
				nsLeft
				(proc999_3
					if view:
						(CelWide view loop cel)
					else:
						0
					#endif
					(and
						(IsObject bust)
						(+
							(bust nsLeft:)
							(CelWide (bust view:) (bust loop:) (bust cel:))
						)
					)
					(and
						(IsObject eyes)
						(+
							(eyes nsLeft:)
							(CelWide (eyes view:) (eyes loop:) (eyes cel:))
						)
					)
					(and
						(IsObject mouth)
						(+
							(mouth nsLeft:)
							(CelWide (mouth view:) (mouth loop:) (mouth cel:))
						)
					)
				)
			)
		)
		(= nsBottom
			(+
				nsTop
				(proc999_3
					if view:
						(CelHigh view loop cel)
					else:
						0
					#endif
					(and
						(IsObject bust)
						(+
							(bust nsTop:)
							(CelHigh (bust view:) (bust loop:) (bust cel:))
						)
					)
					(and
						(IsObject eyes)
						(+
							(eyes nsTop:)
							(CelHigh (eyes view:) (eyes loop:) (eyes cel:))
						)
					)
					(and
						(IsObject mouth)
						(+
							(mouth nsTop:)
							(CelHigh (mouth view:) (mouth loop:) (mouth cel:))
						)
					)
				)
			)
		)
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not underBits):
			underBits = (Graph 7 nsTop nsLeft nsBottom nsRight 3)
		#endif
		temp0 = (PicNotValid)
		(PicNotValid 1)
		if bust:
			(DrawCel
				(bust view:)
				(bust loop:)
				(bust cel:)
				((bust nsLeft:) + nsLeft)
				((bust nsTop:) + nsTop)
				-1
			)
		#endif
		if eyes:
			(DrawCel
				(eyes view:)
				(eyes loop:)
				(eyes cel:)
				((eyes nsLeft:) + nsLeft)
				((eyes nsTop:) + nsTop)
				-1
			)
		#endif
		if mouth:
			(DrawCel
				(mouth view:)
				(mouth loop:)
				(mouth cel:)
				((mouth nsLeft:) + nsLeft)
				((mouth nsTop:) + nsTop)
				-1
			)
		#endif
		(DrawCel view loop cel nsLeft nsTop -1)
		(Graph 12 nsTop nsLeft nsBottom nsRight 1)
		(PicNotValid temp0)
	#end:method

	@classmethod
	def showRave(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not underBits):
			(= underBits
				(Graph
					15
					y
					x
					(y + (((CelHigh 5 0 0) * 5) / 11))
					(x + ((CelWide 5 0 0) / 2))
				)
			)
			(DrawCel 5 0 0 0 0 -1 0 underBits)
			temp0 = 0
		else:
			temp0 = 1
		#endif
		if 
			(==
				(Portrait
					1
					raveName
					(x + 4)
					(y - 7)
					param1
					param2
					param3
					param4
					param5
					temp0
				)
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
		argc = sum(v is not None for v in locals().values())

		if ((view > 0) and (not underBits)):
			(self init:)
		#endif
		(super say: &rest)
	#end:method

	@classmethod
	def startText():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not viewInPrint):
			(self show:)
		#endif
		temp0 = (super startText: &rest)
		if mouth:
			(mouth setCycle: RandCycle (4 * temp0) 0 1)
		#endif
		if (eyes and (not (eyes cycler:))):
			(eyes setCycle: Blink blinkSpeed)
		#endif
	#end:method

	@classmethod
	def display(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(temp3 = (global38 new:) color: color back: back)
		if ((not (HaveMouse)) and (global19 != 996)):
			saveCursor = global19
			(global1 setCursor: 996)
		else:
			saveCursor = 0
		#endif
		if viewInPrint:
			(= temp0
				if useFrame:
					loop
				else:
					(bust loop:)
				#endif
			)
			if showTitle:
				(Print addTitle: name)
			#endif
			(Print
				window: temp3
				posn: x y
				modeless: 1
				font: font
				addText: param1
				addIcon: view temp0 cel 0 0
				init:
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
				(Print addTitle: name)
			#endif
			(Print
				window: temp3
				posn: (x + textX) (y + textY)
				modeless: 1
				font: font
				width: temp1
				addText: param1
				init:
			)
		#endif
	#end:method

	@classmethod
	def startAudio(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (raving or ((not raving) and mouth)):
			temp0 = (proc999_6 param1 0)
			temp1 = (proc999_6 param1 1)
			temp2 = (proc999_6 param1 2)
			temp3 = (proc999_6 param1 3)
			temp4 = (proc999_6 param1 4)
		#endif
		if (raving and raveName):
			(self showRave: temp0 temp1 temp2 temp3 temp4)
		else:
			(self show:)
			if mouth:
				if (ResCheck 147 temp0 temp1 temp2 temp3 temp4):
					(mouth setCycle: MouthSync temp0 temp1 temp2 temp3 temp4)
					(super startAudio: param1)
				else:
					temp18 = (super startAudio: param1)
					(mouth setCycle: RandCycle (temp18 * 4) 0 1)
				#endif
			else:
				(super startAudio: param1)
			#endif
			if (eyes and (not (eyes cycler:))):
				(eyes setCycle: Blink blinkSpeed)
			#endif
		#endif
	#end:method

	@classmethod
	def cycle(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 and (param1 cycler:)):
			temp0 = (param1 cel:)
			((param1 cycler:) doit:)
			if (temp0 != (param1 cel:)):
				(DrawCel
					(param1 view:)
					(param1 loop:)
					(param1 cel:)
					((param1 nsLeft:) + nsLeft)
					((param1 nsTop:) + nsTop)
					-1
				)
				(param1
					nsRight:
						(+
							(param1 nsLeft:)
							(CelWide
								(param1 view:)
								(param1 loop:)
								(param1 cel:)
							)
						)
				)
				(param1
					nsBottom:
						(+
							(param1 nsTop:)
							(CelHigh
								(param1 view:)
								(param1 loop:)
								(param1 cel:)
							)
						)
				)
				(Graph
					12
					((param1 nsTop:) + nsTop)
					((param1 nsLeft:) + nsLeft)
					((param1 nsBottom:) + nsTop)
					((param1 nsRight:) + nsLeft)
					1
				)
			#endif
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((super doit:) and mouth):
			(self cycle: mouth)
		#endif
		if eyes:
			(self cycle: eyes)
		#endif
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Graph 8 underBits)
		underBits = 0
		(Graph 13 nsTop nsLeft nsBottom nsRight)
		if global69:
			(global69 enable:)
		#endif
	#end:method

	@classmethod
	def dispose(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (mouth and underBits):
			(mouth cel: 0)
			(DrawCel
				(mouth view:)
				(mouth loop:)
				0
				((mouth nsLeft:) + nsLeft)
				((mouth nsTop:) + nsTop)
				-1
			)
		#endif
		if (mouth and (mouth cycler:)):
			if ((mouth cycler:) respondsTo: #cue):
				((mouth cycler:) cue:)
			#endif
			(mouth setCycle: 0)
		#endif
		if ((not argc) or (param1 == 1)):
			if raving:
				(Graph 8 underBits)
				(Graph
					13
					(y - 10)
					(x - 10)
					(+ 10 (y - 10) (((CelHigh 5 0 0) * 5) / 11))
					(+ 10 (x - 10) ((CelWide 5 0 0) / 2))
				)
				raving = underBits = 0
			#endif
			if (eyes and underBits):
				(eyes setCycle: 0 cel: 0)
				(DrawCel
					(eyes view:)
					(eyes loop:)
					0
					((eyes nsLeft:) + nsLeft)
					((eyes nsTop:) + nsTop)
					-1
				)
			#endif
			if saveX:
				x = saveX
				y = saveY
			#endif
			saveY = saveX = 0
			(self hide:)
		#endif
		(super dispose: param1)
	#end:method

#end:class or instance

