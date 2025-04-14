#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 917
import sci_sh
import kernel
import Main
import User
import Actor
import System

class PanelInset(View):
	#property vars (may be empty)
	depressOk = 1
	offsetX = 20
	offsetY = 14
	maxCol = 6
	maxRow = 4
	cursorSpace = 4
	numButtons = 0
	strPointer = 0
	strLen = 0
	row = 0
	column = 0
	charCount = 0
	saveIcon = 0
	failed = 0
	value = 0
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		strPointer = param1
		strLen = param2
		saveIcon = global69._send('curIcon:')._send('cursor:')
		global1._send('setCursor:', global21)
		super._send('init:', &rest)
		global1._send('setCursor:', global20)
		self._send('setPri:', 15, 'ignoreActors:', 'stopUpd:')
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		global74._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		failed = charCount = 0
		super._send('dispose:')
		global72._send('delete:', self)
		global73._send('delete:', self)
		global74._send('delete:', self)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if User._send('canInput:'):
			param1._send('claimed:', 1)
			(cond
				case (param1._send('type:') & 0x0001):
					if self._send('onMe:', param1):
						self._send('calcValue:', param1)
					else:
						self._send('dispose:')
					#endif
				#end:case
				case (param1._send('type:') & 0x0044):
					(cond
						case proc999_5(param1._send('message:'), 2, 4, 6, 8, 9): 0#end:case
						case proc999_5(param1._send('message:'), 1, 5, 3, 7, 0):
							self._send('moveCursorPosn:', param1)
						#end:case
						case (param1._send('message:') == 13):
							if self._send('onMe:', param1):
								self._send('calcValue:', param1)
							else:
								self._send('dispose:')
							#endif
						#end:case
						case 27:
							self._send('dispose:')
						#end:case
						else:
							param1._send('claimed:', 0)
						#end:else
					)
				#end:case
				else:
					param1._send('claimed:', 0)
				#end:else
			)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def calcPosn(param1 = None, *rest):
		(= column
			proc999_3(1, proc999_2((((param1._send('x:') - x) / offsetX) + 1), maxCol))
		)
		row = proc999_3(0, proc999_2(((param1._send('y:') - y) / offsetY), maxRow))
	#end:method

	@classmethod
	def calcValue(param1 = None, *rest):
		temp0 = 0
		value = 0
		if strPointer:
			temp0 = proc999_6(strPointer, charCount)
		#endif
		self._send('calcPosn:', param1)
		if 
			(and
				(value = (column + (row * maxCol)) <= numButtons)
				self._send('buttonSetup:')
			)
			self._send('failCheck:', temp0)
			if (charCount.post('++') == strLen):
				global1._send('setCursor:', saveIcon)
				saveIcon = 0
				global2._send('notify:', (not failed))
				self._send('dispose:')
			#endif
		#endif
	#end:method

	@classmethod
	def moveCursorPosn(param1 = None, *rest):
		self._send('calcPosn:', param1)
		temp0 = ((x + (column * offsetX)) - (offsetX / 2))
		temp1 = ((y + ((row + 1) * offsetY)) - cursorSpace)
		match param1._send('message:')
			case 1:
				if (row > 0):
					(temp1 -= offsetY)
				#endif
			#end:case
			case 5:
				if (row < maxRow):
					(temp1 += offsetY)
				#endif
			#end:case
			case 3:
				if (column < maxCol):
					(temp0 += offsetX)
				#endif
			#end:case
			case 7:
				if (column > 1):
					(temp0 -= offsetX)
				#endif
			#end:case
		#end:match
		kernel.SetCursor(temp0, temp1)
	#end:method

	@classmethod
	def buttonSetup():
		temp0 = (((value - 1) / 16) + 1)
		temp1 = (mod (value - 1) 16)
		temp2 = (x + ((column - 1) * offsetX))
		temp3 = (y + (row * offsetY))
		self._send('drawButton:', temp0, temp1, temp2, temp3)
	#end:method

	@classmethod
	def failCheck(param1 = None, *rest):
		if (param1 and (param1 != value)):
			failed = 1
		#endif
	#end:method

	@classmethod
	def drawButton(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		kernel.DrawCel(view, param1, param2, param3, param4, 15)
		return 1
	#end:method

	@classmethod
	def solveIt():
		if strPointer:
			charCount = 0
			while (charCount < strLen): # inline for
				value = proc999_6(strPointer, charCount)
				row = ((value - 1) / maxCol)
				column = (value - (row * maxCol))
				self._send('buttonSetup:')
				# for:reinit
				charCount.post('++')
			#end:loop
		#endif
	#end:method

#end:class or instance

