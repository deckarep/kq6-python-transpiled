#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 916
import sci_sh
import Main
import User
import Actor
import System

class GatePanel(View):
	#property vars (may be empty)
	offsetX = 20
	offsetY = 14
	maxCol = 6
	maxRow = 4
	cursorSpace = 4
	numButtons = 0
	strPointer = 0
	strLen = 0
	maxLen = 0
	row = 0
	column = 0
	charCount = 0
	failed = 0
	value = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		strPointer = param1
		strLen = param2
		maxLen = param3
		(global69 curIcon: (global69 at: 1))
		(global1 setCursor: ((global69 curIcon:) cursor:))
		(global69 disable:)
		(SetPort 0)
		(super init:)
		(global72 addToFront: self)
		(global73 addToFront: self)
		(global74 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		failed = charCount = strPointer = 0
		(super dispose:)
		(global72 delete: self)
		(global73 delete: self)
		(global74 delete: self)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (User canInput:):
			(param1 claimed: 1)
			(cond
				case ((param1 type:) & 0x0001):
					(cond
						case 
							(or
								(temp0 = (param1 modifiers:) & 0x0003)
								(temp0 & 0x0004)
								(temp0 & 0x0008)
							):
							0
						#end:case
						case (self onMe: param1):
							(self calcValue: param1)
						#end:case
						else:
							(global2 notify: 0)
							(self dispose:)
						#end:else
					)
				#end:case
				case ((param1 type:) & 0x0044):
					(cond
						case (proc999_5 (param1 message:) 2 4 6 8 9): 0#end:case
						case (proc999_5 (param1 message:) 1 5 3 7 0):
							(self moveCursorPosn: param1)
						#end:case
						case ((param1 message:) == 13):
							if (self onMe: param1):
								(self calcValue: param1)
							else:
								(global2 notify: 0)
								(self dispose:)
							#endif
						#end:case
						case 27:
							(global2 notify: 0)
							(self dispose:)
						#end:case
						else:
							(param1 claimed: 0)
						#end:else
					)
				#end:case
				else:
					(param1 claimed: 0)
				#end:else
			)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def calcPosn(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= column
			(proc999_3 1 (proc999_2 ((((param1 x:) - x) / offsetX) + 1) maxCol))
		)
		row = (proc999_3 0 (proc999_2 (((param1 y:) - y) / offsetY) maxRow))
	#end:method

	@classmethod
	def calcValue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		value = 0
		if strPointer:
			temp0 = (proc999_6 strPointer charCount)
		#endif
		(self calcPosn: param1)
		if 
			(and
				(value = (column + (row * maxCol)) <= numButtons)
				(self buttonSetup:)
			)
			(self failCheck: temp0)
			if ((charCount++ == strLen) and (not failed)):
				(global2 notify: (not failed))
				(self dispose:)
			#endif
			if (charCount == maxLen):
				(global2 notify: (not failed))
				(self dispose:)
			#endif
		#endif
	#end:method

	@classmethod
	def moveCursorPosn(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self calcPosn: param1)
		temp0 = ((x + (column * offsetX)) - (offsetX / 2))
		temp1 = ((y + ((row + 1) * offsetY)) - cursorSpace)
		match (param1 message:)
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
		(SetCursor temp0 temp1)
	#end:method

	@classmethod
	def buttonSetup():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc999_5 value 26 27 29 30):
			return 0
		#endif
		temp0 = (((value - 1) / 16) + 1)
		temp1 = (mod (value - 1) 16)
		temp2 = (x + ((column - 1) * offsetX))
		temp3 = (y + (row * offsetY))
		return (self drawButton: temp0 temp1 temp2 temp3)
	#end:method

	@classmethod
	def failCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 and (param1 != value)):
			failed = 1
		#endif
	#end:method

	@classmethod
	def drawButton(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(DrawCel view param1 param2 param3 param4 15)
		return 1
	#end:method

#end:class or instance

