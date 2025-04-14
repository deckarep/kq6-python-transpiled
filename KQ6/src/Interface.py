#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 255
import sci_sh
import kernel
import Main
import Print
import System

# Public Export Declarations
SCI.public_exports(
	proc255_0 = 0,
	proc255_1 = 1,
	proc255_2 = 2,
)

@SCI.procedure
def proc255_0():
	temp0 = Event._send('new:')
	temp1 = (temp0._send('type:') != 2)
	temp0._send('dispose:')
	return temp1
#end:procedure

@SCI.procedure
def proc255_1(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = 0
	if (argc > 1):
		kernel.Format(@temp0, r"""%d""", param2)
	#endif
	(return
		if proc921_2(@temp0, 5, param1):
			kernel.ReadNumber(@temp0)
		else:
			-1
		#endif
	)
#end:procedure

@SCI.procedure
def proc255_2(param1 = None, param2 = None, *rest):
	(return
		(and
			(< param1._send('nsLeft:') param2._send('x:') param1._send('nsRight:'))
			(< param1._send('nsTop:') param2._send('y:') param1._send('nsBottom:'))
		)
	)
#end:procedure

class Class_255_0(Obj):
	#property vars (may be empty)
	type = 0
	state = 0
	nsTop = 0
	nsLeft = 0
	nsBottom = 0
	nsRight = 0
	key = 0
	said = 0
	value = 0
	
	@classmethod
	def enable(param1 = None, *rest):
		if param1:
			(state |= 0x0001)
		else:
			(state &= 0xfffe)
		#endif
	#end:method

	@classmethod
	def select(param1 = None, *rest):
		if param1:
			(state |= 0x0008)
		else:
			(state &= 0xfff7)
		#endif
		self._send('draw:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if param1._send('claimed:'):
			return 0
		#endif
		temp0 = 0
		if 
			(and
				(state & 0x0001)
				(or
					(and
						(temp1 = param1._send('type:') == 4)
						(param1._send('message:') == key)
					)
					((temp1 == 1) and self._send('check:', param1))
				)
			)
			param1._send('claimed:', 1)
			temp0 = self._send('track:', param1)
		#endif
		return temp0
	#end:method

	@classmethod
	def check(param1 = None, *rest):
		(return
			(and
				(param1._send('x:') >= nsLeft)
				(param1._send('y:') >= nsTop)
				(param1._send('x:') < nsRight)
				(param1._send('y:') < nsBottom)
			)
		)
	#end:method

	@classmethod
	def track(param1 = None, *rest):
		if (1 == param1._send('type:')):
			temp1 = 0
			while True: #repeat
				param1 = Event._send('new:', -32768)
				param1._send('localize:')
				if (temp0 = self._send('check:', param1) != temp1):
					kernel.HiliteControl(self)
					temp1 = temp0
				#endif
				param1._send('dispose:')
				(breakif (not proc255_0()))
			#end:loop
			if temp0:
				kernel.HiliteControl(self)
			#endif
			return temp0
		else:
			return self
		#endif
	#end:method

	@classmethod
	def isType(param1 = None, *rest):
		return (type == param1)
	#end:method

	@classmethod
	def checkState(param1 = None, *rest):
		return (state & param1)
	#end:method

	@classmethod
	def doit():
		return value
	#end:method

	@classmethod
	def setSize():#end:method

	@classmethod
	def move(param1 = None, param2 = None, *rest):
		(nsRight += param1)
		(nsLeft += param1)
		(nsTop += param2)
		(nsBottom += param2)
	#end:method

	@classmethod
	def moveTo(param1 = None, param2 = None, *rest):
		self._send('move:', (param1 - nsLeft), (param2 - nsTop))
	#end:method

	@classmethod
	def draw():
		kernel.DrawControl(self)
	#end:method

	@classmethod
	def cycle():#end:method

#end:class or instance

class DText(Class_255_0):
	#property vars (may be empty)
	type = 2
	text = 0
	font = 1
	mode = 0
	rects = 0
	
	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (text and ((not argc) or (not param1))):
			kernel.Memory(3, self._send('text:'))
		#endif
		if rects:
			kernel.Memory(3, self._send('rects:'))
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def new():
		super._send('new:')._send('font:', global22, 'yourself:')
	#end:method

	@classmethod
	def setSize(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.TextSize(@temp0[0], text, font, (param1 if argc else 0))
		nsBottom = (nsTop + temp0[2])
		nsRight = (nsLeft + temp0[3])
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				global17
				rects
				(or
					proc999_5(param1._send('type:'), 1, 256)
					((param1._send('type:') == 4) and (param1._send('message:') == 13))
				)
			)
			temp0 = -1
			param1._send('globalize:', 'claimed:', 1)
			while (proc999_6(rects, (temp0 + 1)) != 30583):

				temp2 = proc999_6(rects, temp0.post('++'))
				temp1 = proc999_6(rects, temp0.post('++'))
				temp4 = proc999_6(rects, temp0.post('++'))
				temp3 = proc999_6(rects, temp0.post('++'))
				if 
					(and
						(<= temp2 param1._send('x:') temp4)
						(<= temp1 param1._send('y:') temp3)
					)
					global17._send('doit:', (temp0 / 4))
					param1._send('type:', 0, 'claimed:', 0)
					(break)
				#endif
			#end:loop
		#endif
		super._send('handleEvent:', param1)
	#end:method

	@classmethod
	def draw():
		rects = kernel.DrawControl(self)
	#end:method

#end:class or instance

class Dialog(List):
	#property vars (may be empty)
	text = 0
	font = 0
	window = 0
	theItem = 0
	nsTop = 0
	nsLeft = 0
	nsBottom = 0
	nsRight = 0
	time = 0
	caller = 0
	seconds = 0
	lastSeconds = 0
	eatTheMice = 0
	lastTicks = 0
	
	@classmethod
	def open(param1 = None, param2 = None, *rest):
		if (kernel.PicNotValid() and global5):
			kernel.Animate(global5._send('elements:'), 0)
		#endif
		window = window._send('new:')
		window._send(
			'top:', nsTop,
			'left:', nsLeft,
			'bottom:', nsBottom,
			'right:', nsRight,
			'title:', text,
			'type:', param1,
			'priority:', param2,
			'open:'
		)
		seconds = time
		self._send('draw:')
	#end:method

	@classmethod
	def draw():
		self._send('eachElementDo:', #draw)
	#end:method

	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global88 = (global86 + kernel.GetTime())
		temp2 = 0
		self._send('eachElementDo:', #init)
		if theItem:
			theItem._send('select:', 0)
		#endif
		(= theItem
			if (argc and param1):
				param1
			else:
				self._send('firstTrue:', #checkState, 1)
			#endif
		)
		if theItem:
			theItem._send('select:', 1)
		#endif
		if (not theItem):
			eatTheMice = global79
			lastTicks = kernel.GetTime()
		else:
			eatTheMice = 0
		#endif
		temp1 = 0
		while (not temp1):

			global88 = (global86 + kernel.GetTime())
			self._send('eachElementDo:', #cycle)
			temp0 = Event._send('new:')._send('localize:')
			if eatTheMice:
				eatTheMice.post('--')
				if (temp0._send('type:') == 1):
					temp0._send('type:', 0)
				#endif
				while (lastTicks == kernel.GetTime()):

				#end:loop
				lastTicks = kernel.GetTime()
			#endif
			self._send('eachElementDo:', #perform, checkHiliteCode, self, temp0)
			temp1 = self._send('handleEvent:', temp0)
			temp0._send('dispose:')
			if self._send('check:'):
				(break)
			#endif
			if (temp1 == -2):
				temp1 = 0
				kernel.EditControl(theItem, 0)
				(break)
			#endif
			kernel.Wait(1)
		#end:loop
		return temp1
	#end:method

	@classmethod
	def check():
		if seconds:
			temp0 = kernel.GetTime(1)
			if (lastSeconds != temp0):
				lastSeconds = temp0
				return (not seconds.post('--'))
			#endif
		#endif
	#end:method

	@classmethod
	def dispose():
		self._send('eachElementDo:', #dispose, 'release:')
		if (self == global25):
			kernel.SetPort(global41)
			global25 = 0
			global41 = 0
		#endif
		if window:
			window._send('dispose:')
			window = 0
		#endif
		theItem = 0
		temp0 = caller
		super._send('dispose:')
		if temp0:
			temp0._send('cue:')
		#endif
	#end:method

	@classmethod
	def advance():
		if theItem:
			theItem._send('select:', 0)
			temp1 = self._send('contains:', theItem)
			while True: #repeat
				if (not temp1 = self._send('next:', temp1)):
					temp1 = self._send('first:')
				#endif
				theItem = kernel.NodeValue(temp1)
				if (theItem._send('state:') & 0x0001):
					(break)
				#endif
			#end:loop
			theItem._send('select:', 1)
			global1._send(
				'setCursor:', global19, 1, (+
						theItem._send('nsLeft:')
						((theItem._send('nsRight:') - theItem._send('nsLeft:')) / 2)
					), (theItem._send('nsBottom:') - 3)
			)
		#endif
	#end:method

	@classmethod
	def retreat():
		if theItem:
			theItem._send('select:', 0)
			temp1 = self._send('contains:', theItem)
			while True: #repeat
				if (not temp1 = self._send('prev:', temp1)):
					temp1 = self._send('last:')
				#endif
				theItem = kernel.NodeValue(temp1)
				if (theItem._send('state:') & 0x0001):
					(break)
				#endif
			#end:loop
			theItem._send('select:', 1)
			global1._send(
				'setCursor:', global19, 1, (+
						theItem._send('nsLeft:')
						((theItem._send('nsRight:') - theItem._send('nsLeft:')) / 2)
					), (theItem._send('nsBottom:') - 3)
			)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if (param1._send('type:') & 0x0040):
			match param1._send('message:')
				case 5:
					param1._send('type:', 4, 'message:', 20480)
				#end:case
				case 1:
					param1._send('type:', 4, 'message:', 18432)
				#end:case
				case 7:
					param1._send('type:', 4, 'message:', 19200)
				#end:case
				case 3:
					param1._send('type:', 4, 'message:', 19712)
				#end:case
			#end:match
		#endif
		temp1 = param1._send('type:')
		temp2 = param1._send('message:')
		if temp0 = self._send('firstTrue:', #handleEvent, param1):
			kernel.EditControl(theItem, 0)
			if (not temp0._send('checkState:', 2)):
				if theItem:
					theItem._send('select:', 0)
				#endif
				theItem = temp0._send('select:', 1)
				temp0._send('doit:')
				temp0 = 0
			else:
				return temp0
			#endif
		else:
			temp1 = param1._send('type:')
			temp2 = param1._send('message:')
			temp0 = 0
			(cond
				case 
					(and
						((temp1 == 256) or ((temp1 == 4) and (temp2 == 13)))
						theItem
						theItem._send('checkState:', 1)
					):
					temp0 = theItem
					kernel.EditControl(theItem, 0)
					param1._send('claimed:', 1)
				#end:case
				case ((temp1 == 4) and (temp2 == 27)):
					param1._send('claimed:', 1)
					temp0 = -1
				#end:case
				case 
					(and
						(not self._send('firstTrue:', #checkState, 1))
						(or
							((temp1 == 4) and (temp2 == 13))
							proc999_5(temp1, 1, 256)
						)
					):
					param1._send('claimed:', 1)
					temp0 = -2
				#end:case
				case 
					(and
						kernel.IsObject(theItem)
						theItem._send('isType:', 3)
						(temp1 == 4)
						(temp2 == 19712)
					):
					if (theItem._send('cursor:') >= kernel.StrLen(theItem._send('text:'))):
						self._send('advance:')
					else:
						kernel.EditControl(theItem, param1)
					#endif
				#end:case
				case 
					(and
						kernel.IsObject(theItem)
						theItem._send('isType:', 3)
						(temp1 == 4)
						(temp2 == 19200)
					):
					if (theItem._send('cursor:') <= 0):
						self._send('retreat:')
					else:
						kernel.EditControl(theItem, param1)
					#endif
				#end:case
				case ((temp1 == 4) and proc999_5(temp2, 9, 19712, 20480)):
					param1._send('claimed:', 1)
					self._send('advance:')
				#end:case
				case ((temp1 == 4) and proc999_5(temp2, 3840, 19200, 18432)):
					param1._send('claimed:', 1)
					self._send('retreat:')
				#end:case
				else:
					kernel.EditControl(theItem, param1)
				#end:else
			)
		#endif
		return temp0
	#end:method

	@classmethod
	def move(param1 = None, param2 = None, *rest):
		(nsRight += param1)
		(nsLeft += param1)
		(nsTop += param2)
		(nsBottom += param2)
	#end:method

	@classmethod
	def moveTo(param1 = None, param2 = None, *rest):
		self._send('move:', (param1 - nsLeft), (param2 - nsTop))
	#end:method

	@classmethod
	def center():
		self._send(
			'moveTo:', (+
					window._send('brLeft:')
					(/
						(-
							(window._send('brRight:') - window._send('brLeft:'))
							(nsRight - nsLeft)
						)
						2
					)
				), (+
					window._send('brTop:')
					(/
						(-
							(window._send('brBottom:') - window._send('brTop:'))
							(nsBottom - nsTop)
						)
						2
					)
				)
		)
	#end:method

	@classmethod
	def setSize():
		if text:
			kernel.TextSize(@temp2[0], text, font, -1, 0)
			nsTop = temp2[0]
			nsLeft = temp2[1]
			nsBottom = temp2[2]
			nsRight = temp2[3]
		else:
			nsRight = nsBottom = nsLeft = nsTop = 0
		#endif
		temp0 = self._send('first:')
		while temp0: # inline for
			temp1 = kernel.NodeValue(temp0)
			if (temp1._send('nsLeft:') < nsLeft):
				nsLeft = temp1._send('nsLeft:')
			#endif
			if (temp1._send('nsTop:') < nsTop):
				nsTop = temp1._send('nsTop:')
			#endif
			if (temp1._send('nsRight:') > nsRight):
				nsRight = temp1._send('nsRight:')
			#endif
			if (temp1._send('nsBottom:') > nsBottom):
				nsBottom = temp1._send('nsBottom:')
			#endif
			# for:reinit
			temp0 = self._send('next:', temp0)
		#end:loop
		(nsRight += 4)
		(nsBottom += 4)
		self._send('moveTo:', 0, 0)
	#end:method

#end:class or instance

@SCI.instance
class checkHiliteCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, param3 = None, *rest):
		if 
			(and
				(param1._send('state:') & 0x0001)
				param1._send('check:', param3)
				(not (param1._send('state:') & 0x0008))
			)
			param2._send('theItem:')._send('select:', 0)
			param2._send('theItem:', param1)
			param1._send('select:', 1)
		#endif
	#end:method

#end:class or instance

