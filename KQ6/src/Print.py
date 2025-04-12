#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 921
import sci_sh
import kernel
import Main
import Interface
import Dialog
import System

# Public Export Declarations
SCI.public_exports(
	proc921_0 = 0,
	proc921_1 = 1,
	proc921_2 = 2,
	proc921_3 = 3,
)

@SCI.procedure
def proc921_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = (Print new:)
	(temp0 addText: &rest init:)
#end:procedure

@SCI.procedure
def proc921_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = (Print new:)
	(temp0 addTextF: &rest init:)
#end:procedure

@SCI.procedure
def proc921_2(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if 
		((Print new:)
			font: (param4 if (argc > 3) else global22)
			addText: (param3 if ((argc > 2) and param3) else r"""""")
			addEdit: param1 param2 0 12 param1
			init:
		)
		kernel.StrLen(param1)
	#endif
#end:procedure

@SCI.procedure
def proc921_3(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = temp1 = kernel.StrLen(param1)
	temp2 = 0
	temp3 = 0
	while (temp3 < temp1): # inline for
		if (kernel.StrAt(param1, temp3) == 37):
			match kernel.StrAt(param1, temp3.post('++'))
				case 100:
					(temp0 += 5)
				#end:case
				case 120:
					(temp0 += 4)
				#end:case
				case 115:
					(temp0 += kernel.StrLen(param2[temp2]))
				#end:case
			#end:match
			temp2.post('++')
		#endif
		# for:reinit
		temp3.post('++')
	#end:loop
	temp0.post('++')
#end:procedure

class Print(Obj):
	#property vars (may be empty)
	dialog = 0
	window = 0
	title = 0
	mode = 0
	font = -1
	width = 0
	x = -1
	y = -1
	ticks = 0
	caller = 0
	retValue = 0
	modeless = 0
	first = 0
	saveCursor = 0
	
	@classmethod
	def addButton(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not dialog):
			dialog = (Dialog new:)
		#endif
		if (font == -1):
			font = global22
		#endif
		if (argc > 4):
			temp0 = param2[0]
			temp1 = param2[1]
			temp2 = param2[2]
			temp3 = (param2[3] if param2[3] else 1)
			temp4 = 0
			temp5 = 0
			temp6 = global11
			if (argc > 5):
				temp4 = param2[4]
				if (argc > 6):
					temp5 = param2[5]
					if (argc > 7):
						temp6 = param2[6]
					#endif
				#endif
			#endif
			if temp8 = kernel.Message(2, temp6, temp0, temp1, temp2, temp3):
				temp7 = kernel.Memory(1, temp8)
				if (not kernel.Message(0, temp6, temp0, temp1, temp2, temp3, temp7)):
					temp7 = 0
				#endif
			#endif
		else:
			temp4 = 0
			temp5 = 0
			if (argc > 2):
				temp4 = param2[1]
				if (argc > 3):
					temp5 = param2[2]
				#endif
			#endif
			temp7 = kernel.Memory(1, (kernel.StrLen(param2[0]) + 1))
			kernel.StrCpy(temp7, param2[0])
		#endif
		if temp7:
			(dialog
				add:
					((DButton new:)
						value: param1
						font: font
						text: temp7
						setSize:
						moveTo: (4 + temp4) (4 + temp5)
						yourself:
					)
				setSize:
			)
		#endif
	#end:method

	@classmethod
	def addEdit(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not dialog):
			dialog = (Dialog new:)
		#endif
		kernel.StrCpy(param1, (param5 if (argc > 4) else r""""""))
		if (argc > 2):
			temp0 = param3
			if (argc > 3):
				temp1 = param4
			#endif
		#endif
		(dialog
			add:
				((DEdit new:)
					text: param1
					max: param2
					setSize:
					moveTo: (temp0 + 4) (temp1 + 4)
					yourself:
				)
			setSize:
		)
	#end:method

	@classmethod
	def addIcon(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not dialog):
			dialog = (Dialog new:)
		#endif
		if (argc > 3):
			temp0 = param4
			temp1 = param5
		else:
			temp0 = temp1 = 0
		#endif
		if kernel.IsObject(param1):
			(dialog
				add: (param1 setSize: moveTo: (temp0 + 4) (temp1 + 4) yourself:)
				setSize:
			)
		else:
			(dialog
				add:
					((DIcon new:)
						view: param1
						loop: param2
						cel: param3
						setSize:
						moveTo: (temp0 + 4) (temp1 + 4)
						yourself:
					)
				setSize:
			)
		#endif
	#end:method

	@classmethod
	def addText(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not dialog):
			dialog = (Dialog new:)
		#endif
		if (font == -1):
			font = global22
		#endif
		if (argc > 3):
			temp0 = param1[0]
			temp1 = param1[1]
			temp2 = param1[2]
			temp3 = (param1[3] if param1[3] else 1)
			temp4 = 0
			temp5 = 0
			temp6 = global11
			if (argc >= 5):
				temp4 = param1[4]
				if (argc >= 6):
					temp5 = param1[5]
					if (argc >= 7):
						temp6 = param1[6]
					#endif
				#endif
			#endif
			if temp8 = kernel.Message(2, temp6, temp0, temp1, temp2, temp3):
				temp7 = kernel.Memory(1, temp8)
				if kernel.Message(0, temp6, temp0, temp1, temp2, temp3, temp7):
					(dialog
						add:
							((DText new:)
								text: temp7
								font: font
								mode: mode
								setSize: width
								moveTo: (4 + temp4) (4 + temp5)
								yourself:
							)
						setSize:
					)
				#endif
			#endif
		else:
			temp4 = 0
			temp5 = 0
			if (argc >= 2):
				temp4 = param1[1]
				if (argc >= 3):
					temp5 = param1[2]
				#endif
			#endif
			temp7 = kernel.Memory(1, (kernel.StrLen(param1[0]) + 1))
			kernel.StrCpy(temp7, param1[0])
			(dialog
				add:
					((DText new:)
						text: temp7
						font: font
						mode: mode
						setSize: width
						moveTo: (4 + temp4) (4 + temp5)
						yourself:
					)
				setSize:
			)
		#endif
	#end:method

	@classmethod
	def addTextF():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = proc921_3(&rest)
		temp1 = kernel.Memory(1, temp0)
		kernel.Format(temp1, &rest)
		(self addText: temp1)
		kernel.Memory(3, temp1)
	#end:method

	@classmethod
	def addTitle(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc > 1):
			temp0 = param1[0]
			temp1 = param1[1]
			temp2 = param1[2]
			temp3 = param1[3]
			temp4 = param1[4]
			if temp5 = kernel.Message(2, temp4, temp0, temp1, temp2, temp3):
				title = kernel.Memory(1, temp5)
				kernel.Message(0, temp4, temp0, temp1, temp2, temp3, title)
			#endif
		else:
			title = kernel.Memory(1, (kernel.StrLen(param1[0]) + 1))
			kernel.StrCpy(title, param1[0])
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global92 and (global92 contains: self)):
			(global92 delete: self)
			if (global92 isEmpty:):
				(global92 dispose:)
				global92 = 0
			#endif
		#endif
		if title:
			kernel.Memory(3, title)
		#endif
		width = mode = title = first = saveCursor = window = 0
		x = y = -1
		modeless = 0
		(global8 pause: 0)
		(super dispose:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = caller
		dialog = 0
		if window:
			(window dispose:)
		#endif
		(self dispose:)
		if temp0:
			(temp0 cue:)
		#endif
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = param1
		y = param2
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		caller = 0
		if argc:
			caller = param1
		#endif
		if (argc > 1):
			(self addText: &rest)
		#endif
		if (not modeless):
			if (not kernel.IsObject(global92)):
				global92 = ((EventHandler new:) name: r"""prints""")
			#endif
			(global92 add: self)
		#endif
		(self showSelf:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(dialog eachElementDo: #doit)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (dialog handleEvent: param1):
			(dialog dispose:)
		#endif
	#end:method

	@classmethod
	def showSelf():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if saveCursor:
			(global1 setCursor: 999)
		#endif
		if (not dialog):
			dialog = (Dialog new:)
		#endif
		(dialog
			window: (window if window else global38)
			name: r"""PODialog"""
			caller: self
		)
		(dialog text: title time: ticks setSize:)
		(dialog center:)
		(= temp3
			if (x == -1):
				(dialog nsLeft:)
			else:
				x
			#endif
		)
		(= temp4
			if (y == -1):
				(dialog nsTop:)
			else:
				y
			#endif
		)
		(dialog moveTo: temp3 temp4)
		temp1 = kernel.GetPort()
		(dialog open: (4 if title else 0) 15)
		if modeless:
			global41 = kernel.GetPort()
			kernel.SetPort(temp1)
			global25 = dialog
		else:
			(global8 pause: 1)
			(cond
				case (not temp0 = first):
					if 
						(and
							temp0 = (dialog firstTrue: #checkState 1)
							(not (dialog firstTrue: #checkState 2))
						)
						(temp0 state: (| (temp0 state:) 0x0002))
					#endif
				#end:case
				case (not kernel.IsObject(temp0)):
					temp0 = (dialog at: temp0)
				#end:case
			)
			retValue = (dialog doit: temp0)
			kernel.SetPort(temp1)
			(cond
				case (retValue == -1):
					retValue = 0
				#end:case
				case (kernel.IsObject(retValue) and (retValue isKindOf: DButton)):
					retValue = (retValue value:)
				#end:case
				case (not (dialog theItem:)):
					retValue = 1
				#end:case
			)
			if saveCursor:
				(global1 setCursor: ((global69 curIcon:) cursor:))
			#endif
			(dialog dispose:)
			return retValue
		#endif
	#end:method

#end:class or instance

