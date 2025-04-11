#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 947
import sci_sh
import Main
import Interface
import Print
import PolyEdit
import Window
import File
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2
local42
local62 = [r"""DIALOG""", 0, 0, r"""About""", 0, 0, r"""Item""", 0, 0, r"""Edit""", 0, 0, r"""Look""", 0, 0, r"""Del""", 0, 0, r"""Win""", 0, 0, r"""Help""", 0, 0, r"""eXit""", 120, 0, 0]
local90 = [r"""EDITING""", 0, 0, r"""Text""", 0, 0, r"""Font""", 0, 0, r"""Value""", 0, 0, r"""Position""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]
local112 = [r"""EDITING""", 0, 0, r"""Text""", 0, 0, r"""Font""", 0, 0, r"""Just""", 0, 0, r"""Width""", 0, 0, r"""Position""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]
local137 = [r"""EDITING""", 0, 0, r"""Font""", 0, 0, r"""Length""", 0, 0, r"""Position""", 0, 0, r"""Text""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]
local159 = [r"""EDITING""", 0, 0, r"""View""", 0, 0, r"""Loop""", 0, 0, r"""Cel""", 0, 0, r"""Position""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]
local181 = [r"""EDITING""", 0, 0, r"""Width""", 0, 0, r"""Length""", 0, 0, r"""Position""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]
local200 = [r"""WINDOW""", 0, 0, r"""Create""", 0, 0, r"""Position""", 0, 0, r"""Delete""", 0, 0, r"""Title""", 0, 0, r"""Help""", 0, 0, r"""Menu""", 0, 0, 0]


@SCI.procedure
def localproc_0(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if ((StrLen param1) > param2):
		(StrAt param1 param2 0)
		(StrAt param1 param2-- 46)
		(StrAt param1 param2-- 46)
		(StrAt param1 param2-- 46)
	#endif
	return param1
#end:procedure

@SCI.procedure
def localproc_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = (param1 noun:)
	temp1 = (param1 verb:)
	temp2 = (param1 case:)
	temp3 = (param1 seq:)
	temp4 = (param1 modNum:)
	(Format @temp5 r"""%d""" temp0)
	(Format @temp15 r"""%d""" temp1)
	(Format @temp25 r"""%d""" temp2)
	(Format @temp35 r"""%d""" temp3)
	(Format @temp45 r"""%d""" temp4)
	if 
		(Print
			addTitle: @local42
			font: 0
			addText: r"""Enter new message parameters:"""
			addText: r"""Noun""" 5 25
			addText: r"""Verb""" 85 25
			addText: r"""Case""" 5 39
			addText: r"""Seq""" 85 39
			addText: r"""Module""" 47 53
			addEdit: @temp5 4 45 25 @temp5
			addEdit: @temp15 4 125 25 @temp15
			addEdit: @temp25 4 45 39 @temp25
			addEdit: @temp35 4 125 39 @temp35
			addEdit: @temp45 5 101 53 @temp45
			addButton: 1 r"""___OK___""" 18 67
			addButton: 0 r"""Cancel""" 91 67
			init:
		)
		temp0 = (ReadNumber @temp5)
		temp1 = (ReadNumber @temp15)
		temp2 = (ReadNumber @temp25)
		temp3 = (ReadNumber @temp35)
		temp4 = (ReadNumber @temp45)
		(cond
			case (not (Message 0 temp4 temp0 temp1 temp2 temp3)):
				(proc921_0 r"""Can't find message!""")
				return 0
			#end:case
			case (not (Message 2 temp4 temp0 temp1 temp2 temp3)):
				(proc921_0 r"""Message contains no text!""")
				return 0
			#end:case
			else:
				(param1
					noun: temp0
					verb: temp1
					case: temp2
					seq: temp3
					modNum: temp4
				)
				return 1
			#end:else
		)
	else:
		return 0
	#endif
#end:procedure

@SCI.procedure
def localproc_2(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(Print
		addTitle: @local42
		font: 0
		width: 50
		addText: r"""What kind of text?"""
		addButton: 1 r""" Literal """ 60 0
		addButton: 2 r"""MSG file""" 60 14
		addButton: 0 r"""__Cancel__""" 60 28
		first: (2 if (param1 seq:) else 1)
		init:
	)
#end:procedure

@SCI.instance
class mainMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local62)
	#end:method

#end:class or instance

@SCI.instance
class editBMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local90)
	#end:method

#end:class or instance

@SCI.instance
class editTMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local112)
	#end:method

#end:class or instance

@SCI.instance
class editEMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local137)
	#end:method

#end:class or instance

@SCI.instance
class editIMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local159)
	#end:method

#end:class or instance

@SCI.instance
class editSMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local181)
	#end:method

#end:class or instance

@SCI.instance
class editWMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local200)
	#end:method

#end:class or instance

class DlgWindow(SysWindow):
	#property vars (may be empty)
	noun = 0
	verb = 0
	case = 0
	seq = 0
	modNum = 0
	
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		type = (4 if title else 0)
		temp0 = (GetPort)
		(super open: &rest)
		(SetPort temp0)
		local1 = 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		local1 = 0
	#end:method

	@classmethod
	def create():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 190
		temp1 = 320
		temp2 = 0
		temp3 = 0
		temp4 = 0
		while (temp4 < (DialogEditor size:)): # inline for
			temp5 = (DialogEditor at: temp4)
			temp0 = (proc999_2 (temp5 nsTop:) temp0)
			temp1 = (proc999_2 (temp5 nsLeft:) temp1)
			temp2 = (proc999_3 (temp5 nsBottom:) temp2)
			temp3 = (proc999_3 (temp5 nsRight:) temp3)
			# for:reinit
			temp4++
		#end:loop
		(DialogEditor eachElementDo: #hide)
		(self dispose:)
		top = (temp0 - 4)
		bottom = (temp2 + 4)
		left = (temp1 - 4)
		right = (temp3 + 4)
		(self open:)
		(DialogEditor eachElementDo: #draw)
	#end:method

	@classmethod
	def moveTo(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < (DialogEditor size:)): # inline for
			temp1 = (DialogEditor at: temp0)
			temp2 = ((temp1 nsLeft:) - left)
			temp3 = ((temp1 nsTop:) - top)
			(temp1 hide: moveTo: (param1 + temp2) (param2 + temp3))
			# for:reinit
			temp0++
		#end:loop
		left = param1
		top = param2
		(self create:)
	#end:method

	@classmethod
	def editMsg():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (localproc_1 self):
			if title:
				(Memory 3 title)
			#endif
			title = (Memory 1 (Message 2 modNum noun verb case seq))
			(Message 0 modNum noun verb case seq title)
		#endif
		(self create:)
	#end:method

	@classmethod
	def editPosn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if local1:
			(proc921_0
				r"""Click to where the top left of the window should be"""
			)
			while ((temp0 = (Event new:) type:) != 1):

				(temp0 dispose:)
			#end:loop
			temp1 = (temp0 x:)
			temp2 = ((temp0 y:) - 10)
			(temp0 dispose:)
			temp3 = (bottom - top)
			temp4 = (right - left)
			temp1 = (proc999_3 0 (proc999_2 temp1 (320 - temp4)))
			temp2 = (proc999_3 0 (proc999_2 temp2 (190 - temp3)))
			(self moveTo: temp1 temp2)
		else:
			(proc921_0 r"""No window to position!""")
		#endif
	#end:method

	@classmethod
	def editTitle():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (localproc_2 self)
			case 0:
				return
			#end:case
			case 2:
				(self editMsg:)
				return
			#end:case
		#end:match
		if seq:
			(Memory 3 title)
			noun = verb = case = seq = modNum = title = 0
		#endif
		if (not title):
			title = (Memory 1 50)
			(StrCpy title r"""title""")
		#endif
		(Print
			addTitle: @local42
			addText: r"""Enter new title:"""
			addEdit: title 50 0 12 title
			init:
		)
		(self create:)
	#end:method

#end:class or instance

class _DItem(Class_255_0):
	#property vars (may be empty)
	underBits = 0
	
	@classmethod
	def select(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self hide:)
		if param1:
			(state |= 0x0008)
		else:
			(state &= 0xfff7)
		#endif
		(self draw:)
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if underBits:
			(Graph 8 underBits)
			temp0 = (nsTop - 1)
			temp1 = (nsLeft - 1)
			temp2 = (nsBottom + 1)
			temp3 = (nsRight + 1)
			underBits = 0
			(Graph 13 temp0 temp1 temp2 temp3)
		#endif
	#end:method

	@classmethod
	def draw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (nsTop - 1)
		temp1 = (nsLeft - 1)
		temp2 = (nsBottom + 1)
		temp3 = (nsRight + 1)
		if underBits:
			(UnLoad 133 underBits)
			underBits = 0
		#endif
		underBits = (Graph 7 temp0 temp1 temp2 temp3 1)
		(DrawControl self)
	#end:method

	@classmethod
	def editPosn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" nsLeft)
		(Format @temp25 r"""%d""" nsTop)
		if 
			(= temp30
				(Print
					addTitle: @local42
					addText: r"""Enter new position:"""
					addText: r"""x = """ 0 12
					addText: r"""y = """ 65 12
					addEdit: @temp0 5 25 12 @temp0
					addEdit: @temp25 6 90 12 @temp25
					font: 0
					addButton: 0 r""" Cancel """ 35 26
					init:
				)
			)
			temp31 = (proc999_3 4 (ReadNumber @temp0))
			temp32 = (proc999_3 4 (ReadNumber @temp25))
			(self hide: moveTo: temp31 temp32 draw:)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		(param1 claimed: 1)
		temp0 = (self track: param1)
	#end:method

	@classmethod
	def track(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 type:) == 1):
			(self hide:)
			while True: #repeat
				param1 = (Event new: -32768)
				(param1 localize:)
				temp0 = (param1 x:)
				temp1 = (param1 y:)
				(DrawStatus (Format @temp2 r"""DRAGGING: %d, %d""" temp0 temp1))
				(self moveTo: temp0 temp1)
				(param1 dispose:)
				(breakif (not (proc255_0)))
			#end:loop
			(DrawStatus r""" """ 0 0)
			(DrawStatus 0)
			if (DialogEditor curMenu:):
				((DialogEditor curMenu:) init:)
			#endif
			(DrawPic (global2 picture:) 100)
			if local1:
				(DlgWindow create:)
			else:
				(DialogEditor eachElementDo: #draw)
			#endif
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self hide:)
		(super dispose: &rest)
	#end:method

#end:class or instance

class _DText(_DItem):
	#property vars (may be empty)
	type = 2
	text = 0
	font = 0
	mode = 0
	width = 0
	noun = 0
	verb = 0
	case = 0
	seq = 0
	modNum = 0
	
	@classmethod
	def setSize(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] text font (param1 if argc else width))
		nsLeft--
		nsTop--
		nsBottom = (+ nsTop temp0[2] 1)
		nsRight = (+ nsLeft temp0[3] 1)
	#end:method

	@classmethod
	def editFont():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp25
			(Print
				addTitle: @local42
				font: 0
				width: 90
				addText: r"""Enter new font number:"""
				addEdit: @temp0 6 0 24
				addButton: 0 r""" System """ 100 0
				addButton: global22 r"""__User__""" 100 14
				addButton: global23 r"""__Small__""" 100 28
				addButton: global26 r"""___Big___""" 100 42
				addButton: -1 r""" Cancel """ 100 56
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if (temp25 != -1):
			(self hide: font: temp25 setSize: draw:)
		#endif
	#end:method

	@classmethod
	def editJust():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		(= temp25
			(Print
				addTitle: @local42
				font: 0
				width: 100
				addText: r"""Enter justification mode:"""
				addButton: 1 r"""___Left___""" 100 0
				addButton: 2 r""" Center """ 100 14
				addButton: 3 r"""__Right__""" 100 28
				addButton: 0 r""" Cancel """ 100 42
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			(self
				hide:
				mode:
					match temp25
						case 1: 0#end:case
						case 2: 1#end:case
						case 3: -1#end:case
					#end:match
				setSize:
				draw:
			)
		#endif
	#end:method

	@classmethod
	def editMsg():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (localproc_1 self):
			(Memory 3 text)
			text = (Memory 1 (Message 2 modNum noun verb case seq))
			(Message 0 modNum noun verb case seq text)
		#endif
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editText():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (localproc_2 self)
			case 0:
				return
			#end:case
			case 2:
				(self editMsg:)
				return
			#end:case
		#end:match
		if seq:
			(Memory 3 text)
			text = (Memory 1 100)
			(StrCpy text r"""text""")
			noun = verb = case = seq = modNum = 0
		#endif
		(Print
			addTitle: @local42
			addText: r"""Enter new text:"""
			addEdit: text 50 0 12 text
			init:
		)
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editWidth():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" width)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new width:"""
				addEdit: @temp0 6 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			(self hide: width: temp25 setSize: draw:)
		#endif
	#end:method

	@classmethod
	def showHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			font: global22
			width: 250
			addText:
				r"""Text Menu:\n\n__Text - Change the text\n__Font - Change the font of the text\n__Just - Change justification mode\n__Position - Change the position of the text\n__Menu - Return to the Main Menu\n"""
			init:
		)
	#end:method

#end:class or instance

class _DIcon(_DItem):
	#property vars (may be empty)
	type = 4
	view = 0
	loop = 0
	cel = 0
	
	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		nsRight = (nsLeft + (CelWide view loop cel))
		nsBottom = (nsTop + (CelHigh view loop cel))
	#end:method

	@classmethod
	def editView():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" view)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new view number:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			view = temp25
		#endif
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editLoop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" loop)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new loop number:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			loop = temp25
		#endif
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" cel)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new cel number:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			cel = temp25
		#endif
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def showHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			font: global22
			width: 250
			addText:
				r"""Icon Menu:\n\n__View - Change the view of the icon\n__Loop - Change the loop of the icon\n__Cel - Change the cel of the icon\n__Position - Change the position of the icon\n__Menu - Return to the Main Menu\n"""
			init:
		)
	#end:method

#end:class or instance

class _DButton(_DItem):
	#property vars (may be empty)
	type = 1
	state = 1
	text = 0
	font = 0
	noun = 0
	verb = 0
	case = 0
	seq = 0
	modNum = 0
	
	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] text font 0 0)
		(temp0[2] += 2)
		(temp0[3] += 2)
		nsBottom = (nsTop + temp0[2])
		temp0[3] = (((temp0[3] + 15) / 16) * 16)
		nsRight = (temp0[3] + nsLeft)
	#end:method

	@classmethod
	def editFont():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp25
			(Print
				addTitle: @local42
				font: 0
				width: 90
				addText: r"""Enter new font number:"""
				addEdit: @temp0 6 0 24
				addButton: 0 r""" System """ 100 0
				addButton: global22 r"""__User__""" 100 14
				addButton: global23 r"""__Small__""" 100 28
				addButton: global26 r"""___Big___""" 100 42
				addButton: -1 r""" Cancel """ 100 56
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if (temp25 != -1):
			(self hide: font: temp25 setSize: draw:)
		#endif
	#end:method

	@classmethod
	def editMsg():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (localproc_1 self):
			(Memory 3 text)
			text = (Memory 1 (Message 2 modNum noun verb case seq))
			(Message 0 modNum noun verb case seq text)
		#endif
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editText():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (localproc_2 self)
			case 0:
				return
			#end:case
			case 2:
				(self editMsg:)
				return
			#end:case
		#end:match
		if seq:
			(Memory 3 text)
			text = (Memory 1 50)
			(StrCpy text r"""button""")
			noun = verb = case = seq = modNum = 0
		#endif
		(Print
			addTitle: @local42
			addText: r"""Enter new text:"""
			addEdit: text 50 0 12 text
			init:
		)
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def editValue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" value)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new value:"""
				addEdit: @temp0 6 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			value = temp25
		#endif
	#end:method

	@classmethod
	def showHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			font: global22
			width: 250
			addText:
				r"""Button Menu:\n\n__Text - Change the button text\n__Font - Change the font of the button text\n__Value - Change the return value of the button\n__Position - Change the position of the button\n__Menu - Return to the Main Menu\n"""
			init:
		)
	#end:method

#end:class or instance

class _DEdit(_DItem):
	#property vars (may be empty)
	type = 3
	state = 1
	text = 0
	font = 0
	max = 0
	cursor = 0
	
	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] r"""M""" font 0 0)
		nsBottom = (nsTop + temp0[2])
		nsRight = (nsLeft + ((* temp0[3] max 3) / 4))
		cursor = (StrLen text)
	#end:method

	@classmethod
	def editFont():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp25
			(Print
				addTitle: @local42
				font: 0
				width: 90
				addText: r"""Enter new font number:"""
				addEdit: @temp0 6 0 24
				addButton: 0 r""" System """ 100 0
				addButton: global22 r"""__User__""" 100 14
				addButton: global23 r"""__Small__""" 100 28
				addButton: global26 r"""___Big___""" 100 42
				addButton: -1 r""" Cancel """ 100 56
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if (temp25 != -1):
			(self hide: font: temp25 setSize: draw:)
		#endif
	#end:method

	@classmethod
	def editLength():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" max)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new maximum length:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			(self max: temp25 hide: setSize: draw:)
		#endif
	#end:method

	@classmethod
	def editText():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			addTitle: @local42
			addText: r"""Enter new default text:"""
			addEdit: text 25 0 12 text
			init:
		)
		(self hide: setSize: draw:)
	#end:method

	@classmethod
	def showHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			font: global22
			width: 250
			addText:
				r"""Edit Menu:\n\n__Font - Change the font of the edit text\n__Length - Change the maximum length of input\n__Position - Change the position of the edit\n__Text - Change the default edit text\n__Menu - Return to the Main Menu\n"""
			init:
		)
	#end:method

#end:class or instance

class _DSelector(_DItem):
	#property vars (may be empty)
	type = 6
	font = 0
	x = 20
	y = 6
	
	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] r"""M""" font 0 0)
		nsBottom = (+ nsTop 20 (temp0[2] * y))
		nsRight = (nsLeft + ((* temp0[3] x 3) / 4))
	#end:method

	@classmethod
	def editLength():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" y)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new length:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			(self y: temp25 hide: setSize: draw:)
		#endif
	#end:method

	@classmethod
	def editWidth():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format @temp0 r"""%d""" x)
		(= temp25
			(Print
				addTitle: @local42
				addText: r"""Enter new width:"""
				addEdit: @temp0 5 0 12 @temp0
				font: 0
				addButton: 0 r""" Cancel """ 0 26
				init:
			)
		)
		if temp0:
			temp25 = (ReadNumber @temp0)
		#endif
		if temp25:
			(self x: temp25 hide: setSize: draw:)
		#endif
	#end:method

	@classmethod
	def showHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			font: global22
			width: 250
			addText:
				r"""Selector Menu:\n\n__Width - Change the selector width (in chars)\n__Length - Change number of selector lines\n__Position - Change the position of the selector\n__Menu - Return to the Main Menu\n"""
			init:
		)
	#end:method

#end:class or instance

class DialogEditor(List):
	#property vars (may be empty)
	state = 0
	curItem = 0
	curMenu = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = global38
		(StrCpy @local42 r"""DialogEditor__v1.1""")
		(global38 = SysWindow color: 0 back: 255)
		(global1 setCursor: 999)
		(self changeState: 0)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(mainMenu dispose:)
		(DlgWindow dispose:)
		global38 = local0
		(global1 setCursor: ((global69 curIcon:) cursor:))
		(DrawStatus r""" """ 0 0)
		(DrawStatus 0)
		(super dispose:)
		(DrawPic (global2 picture:) 100)
		(DisposeScript 111)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if curMenu:
			(curMenu dispose:)
		#endif
		(= curMenu
			match state = param1
				case 0: mainMenu#end:case
				case 1: editBMenu#end:case
				case 2: editTMenu#end:case
				case 3: editEMenu#end:case
				case 4: editIMenu#end:case
				case 5: editSMenu#end:case
				case 6: editWMenu#end:case
				else: 0#end:else
			#end:match
		)
		if curMenu:
			(curMenu init:)
		#endif
	#end:method

	@classmethod
	def delItem():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if size:
			if 
				(Print
					addText: r"""Delete current item?"""
					font: 0
					addButton: 1 r"""Yes""" 0 12
					addButton: 0 r"""No""" 40 12
					init:
				)
				(self delete: curItem)
				(curItem dispose:)
				curItem = 0
				if size:
					curItem = (self at: 0)
				#endif
			#endif
		else:
			(proc921_0 r"""Nothing to delete!""")
		#endif
	#end:method

	@classmethod
	def exit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not local1):
			(DlgWindow create:)
		#endif
		if (not local2):
			(Format @local2 r"""%d.dlg""" global11)
		#endif
		if 
			(not
				(= temp100
					(Print
						addTitle: @local42
						addText: r"""Save to: """
						addEdit: @local2 25 60 0 @local2
						font: 0
						addButton: 1 r"""__Save__""" 10 12
						addButton: 2 r""" Abandon """ 80 12
						addButton: 0 r""" Cancel """ 151 12
						init:
					)
				)
			)
			return 0
		#endif
		if (temp100 == 2):
			return 1
		#endif
		if (FileIO 10 @local2):
			(Format
				@temp0
				r"""The file '%s' already exists.__Now what?"""
				@local2
			)
			if 
				(not
					(= temp100
						(Print
							addTitle: @local42
							addText: @temp0
							font: 0
							addButton: 1 r""" Replace """ 0 24
							addButton: 2 r""" Append """ 70 24
							addButton: 0 r""" Cancel """ 125 24
							init:
						)
					)
				)
				return 0
			#endif
		#endif
		temp102 = (2 if (temp100 == 1) else 0)
		if (not (temp101 = (File new:) name: @local2 open: temp102)):
			(proc921_1 r"""Error opening '%s'""" (temp101 name:))
			(temp101 dispose:)
			return 0
		#endif
		(temp101
			writeString: r"""\t\t; DialogEditor v1.0\0d\n"""
			writeString: r"""\t\t; by Brian K. Hughes\0d\n"""
			writeString: r"""\t\t(Print\0d\n"""
		)
		if local1:
			(Format
				@temp0
				r"""\t\t\tposn:\t\t\t%d %d,\0d\n"""
				(DlgWindow left:)
				(DlgWindow top:)
			)
			(temp101 writeString: @temp0)
			if (DlgWindow title:):
				if (DlgWindow seq:):
					(Format
						@temp0
						r"""\t\t\taddTitle:\t%d %d %d %d %d,\0d\n"""
						(DlgWindow noun:)
						(DlgWindow verb:)
						(DlgWindow case:)
						(DlgWindow seq:)
						(DlgWindow modNum:)
					)
				else:
					(Format
						@temp0
						r"""\t\t\taddTitle:\t{%s\},\0d\n"""
						(DlgWindow title:)
					)
				#endif
				(temp101 writeString: @temp0)
			#endif
		#endif
		(self writeFile: temp101)
		if 
			(Print
				addTitle: @local42
				addText: r"""This dialog should be..."""
				font: 0
				addButton: 0 r"""___Modal___""" 0 24
				addButton: 1 r""" Modeless """ 0 38
				init:
			)
			(temp101 writeString: r"""\t\t\tmodeless:\tTRUE,\0d\n""")
		#endif
		(temp101
			writeString: r"""\t\t\tinit:\0d\n"""
			writeString: r"""\t\t)\0d\n"""
		)
		(temp101 dispose:)
		return 1
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self init:)
		while True: #repeat
			temp0 = (Event new:)
			if (not (curMenu handleEvent: temp0)):
				(GlobalToLocal temp0)
				(breakif (self handleEvent: temp0))
			#endif
			(temp0 dispose:)
		#end:loop
		(temp0 dispose:)
		(self dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (param1 type:)
			case 0:#end:case
			case 1:
				if temp1 = (self firstTrue: #check param1):
					(param1 claimed: 1)
					if ((param1 modifiers:) == 3):
						(temp1 handleEvent: param1)
					else:
						if curItem:
							(curItem select: 0)
						#endif
						(curItem = temp1 select: 1)
						(self changeState: 0)
					#endif
				#endif
			#end:case
			case 2:#end:case
			case 4:
				match (param1 message:)
					case 63:
						(param1 message: 104)
					#end:case
					case 19:
						(param1 message: 120)
					#end:case
				#end:match
				match (param1 message:)
					case 9:
						(curItem select: 0)
						temp0 = (DialogEditor indexOf: curItem)
						if (temp0++ == (DialogEditor size:)):
							curItem = (DialogEditor at: 0)
						else:
							curItem = (DialogEditor at: temp0)
						#endif
						(curItem select: 1)
						(DialogEditor changeState: 0)
					#end:case
					case 3840:
						(curItem select: 0)
						if (temp0 = (DialogEditor indexOf: curItem) == 0):
							(= curItem
								(DialogEditor at: ((DialogEditor size:) - 1))
							)
						else:
							curItem = (DialogEditor at: temp0--)
						#endif
					#end:case
					case 32:#end:case
					case 8:#end:case
					case 97:
						(Print
							addTitle: @local42
							mode: 1
							width: 140
							addText: r"""by Brian K. Hughes\n17 July, 1992"""
							init:
						)
					#end:case
					case 99:
						match state
							case 4:
								(curItem editCel:)
							#end:case
							case 6:
								if size:
									(DlgWindow create:)
								else:
									(proc921_0
										r"""Can't create window: no items!"""
									)
								#endif
							#end:case
						#end:match
					#end:case
					case 100:
						match state
							case 0:
								(self delItem:)
							#end:case
							case 6:
								if local1:
									(DlgWindow dispose:)
									(self eachElementDo: #draw)
								else:
									(proc921_0 r"""No window to delete!""")
								#endif
							#end:case
						#end:match
					#end:case
					case 101:
						if size:
							(self
								changeState:
									match (curItem -super-:)
										case _DButton: 1#end:case
										case _DText: 2#end:case
										case _DEdit: 3#end:case
										case _DIcon: 4#end:case
										case _DSelector: 5#end:case
									#end:match
							)
						else:
							(proc921_0 r"""No items to edit!""")
						#endif
					#end:case
					case 102:
						if (proc999_5 state 2 1 3):
							(curItem editFont:)
						#endif
					#end:case
					case 104:
						match state
							case 0:
								(Print
									font: global22
									width: 250
									addText:
										r"""Main Menu:\n\n__About - About the DialogEditor\n__Item - Create a new item\n__Edit - Edit properties of the current item\n__Look - View properties of the current item\n__Del - Delete the current item\n__Win - Create a window background\n__Help - You're here!\n__eXit - Exit the DialogEditor (& maybe save)\n"""
									init:
								)
							#end:case
							case 6:
								(Print
									font: global22
									width: 250
									addText:
										r"""Window Menu:\n\n__Create - Draw the window to the correct size\n__Position - Move the window and all items\n__Delete - Remove the window\n__Menu - Return to the Main Menu"""
									init:
								)
							#end:case
							else:
								(curItem showHelp:)
							#end:else
						#end:match
					#end:case
					case 105:
						temp1 = 0
						match
							(Print
								addTitle: @local42
								width: 65
								addText:
									r"""Select the kind of item you want to add to the dialog:"""
								font: 0
								addButton: 1 r"""__Button__""" 80 0
								addButton: 2 r"""___Text___""" 80 14
								addButton: 3 r"""___Edit___""" 80 28
								addButton: 4 r"""___Icon___""" 80 42
								addButton: 6 r""" Selector """ 80 56
								addButton: 0 r"""__Cancel__""" 80 70
								init:
							)
							case 1:
								temp0 = (Memory 1 50)
								(StrCpy temp0 r"""button""")
								(= temp1
									((_DButton new:) text: temp0 yourself:)
								)
							#end:case
							case 2:
								temp0 = (Memory 1 100)
								(StrCpy temp0 r"""text""")
								temp1 = ((_DText new:) text: temp0 yourself:)
							#end:case
							case 3:
								temp0 = (Memory 1 50)
								(StrCpy temp0 r"""""")
								(= temp1
									((_DEdit new:) text: temp0 max: 5 yourself:)
								)
							#end:case
							case 4:
								(= temp1
									((_DIcon new:)
										view: 0
										loop: 0
										cel: 0
										yourself:
									)
								)
							#end:case
							case 6:
								(= temp1
									((_DSelector new:) x: 10 y: 1 yourself:)
								)
							#end:case
						#end:match
						if temp1:
							if curItem:
								(curItem select: 0)
							#endif
							curItem = temp1
							if local1:
								(DlgWindow dispose:)
							#endif
							(self
								addToEnd:
									(curItem setSize: moveTo: 4 4 yourself:)
								eachElementDo: #draw
							)
							(curItem select: 1)
						#endif
					#end:case
					case 106:
						if (state == 2):
							(curItem editJust:)
						#endif
					#end:case
					case 108:
						match state
							case 0:
								if curItem:
									(Format
										@temp508
										r"""__x:_______%d"""
										(curItem nsLeft:)
									)
									(Format
										@temp538
										r"""__y:_______%d"""
										(curItem nsTop:)
									)
									match (curItem -super-:)
										case _DText:
											(StrCpy @temp788 r"""Text Item""")
											(StrCpy @temp2 (curItem text:))
											(Format
												@temp568
												r"""__text:___%s"""
												(localproc_0 @temp2 15)
											)
											(Format
												@temp598
												r"""__font:___%d"""
												(curItem font:)
											)
											(Format
												@temp628
												r"""__width:__%d"""
												(curItem width:)
											)
											(Format
												@temp658
												r"""__noun:___%d"""
												(curItem noun:)
											)
											(Format
												@temp678
												r"""__verb:___%d"""
												(curItem verb:)
											)
											(Format
												@temp708
												r"""__case:___%d"""
												(curItem case:)
											)
											(Format
												@temp738
												r"""__seq:____%d"""
												(curItem seq:)
											)
											(Format
												@temp758
												r"""__modNum: %d"""
												(curItem modNum:)
											)
										#end:case
										case _DButton:
											(StrCpy @temp788 r"""Button Item""")
											(StrCpy @temp2 (curItem text:))
											(Format
												@temp568
												r"""__text:___%s"""
												(localproc_0 @temp2 15)
											)
											(Format
												@temp598
												r"""__font:___%d"""
												(curItem font:)
											)
											(Format
												@temp628
												r"""__value:__%d"""
												(curItem value:)
											)
											(Format
												@temp658
												r"""__noun:___%d"""
												(curItem noun:)
											)
											(Format
												@temp678
												r"""__verb:___%d"""
												(curItem verb:)
											)
											(Format
												@temp708
												r"""__case:___%d"""
												(curItem case:)
											)
											(Format
												@temp738
												r"""__seq:____%d"""
												(curItem seq:)
											)
											(Format
												@temp758
												r"""__modNum: %d"""
												(curItem modNum:)
											)
										#end:case
										case _DIcon:
											(StrCpy @temp788 r"""Icon Item""")
											(Format
												@temp568
												r"""__view:___%d"""
												(curItem view:)
											)
											(Format
												@temp598
												r"""__loop:___%d"""
												(curItem loop:)
											)
											(Format
												@temp628
												r"""__cel:____%d"""
												(curItem cel:)
											)
											(= temp658
												(= temp678
													(= temp708
														(= temp738
															temp758 = 0
														)
													)
												)
											)
										#end:case
										case _DEdit:
											(StrCpy @temp788 r"""Edit Item""")
											(StrCpy @temp2 (curItem text:))
											(Format
												@temp568
												r"""__text:___%s"""
												(localproc_0 @temp2 15)
											)
											(Format
												@temp598
												r"""__font:___%d"""
												(curItem font:)
											)
											(Format
												@temp628
												r"""__max:____%d"""
												(curItem max:)
											)
											(= temp658
												(= temp678
													(= temp708
														(= temp738
															temp758 = 0
														)
													)
												)
											)
										#end:case
										case _DSelector:
											(StrCpy
												@temp788
												r"""Selector Item"""
											)
											(Format
												@temp568
												r"""__width:__%d"""
												(curItem x:)
											)
											(Format
												@temp598
												r"""__length: %d"""
												(curItem y:)
											)
											(= temp628
												(= temp658
													(= temp678
														(= temp708
															(= temp738
																temp758 = 0
															)
														)
													)
												)
											)
										#end:case
									#end:match
									(Print
										addTitle: @temp788
										addText: @temp508
										addText: @temp538 0 12
										addText: @temp568 0 24
										addText: @temp598 0 36
										addText: @temp628 0 48
										addText: @temp658 0 60
										addText: @temp678 0 72
										addText: @temp708 0 84
										addText: @temp738 0 96
										addText: @temp758 0 108
										init:
									)
									if local1:
										(DlgWindow create:)
									#endif
								else:
									(proc921_0 r"""No item to look at!""")
								#endif
							#end:case
							case 4:
								(curItem editLoop:)
							#end:case
							case 3:
								(curItem editLength:)
							#end:case
							case 5:
								(curItem editLength:)
							#end:case
						#end:match
					#end:case
					case 109:
						(self changeState: 0)
					#end:case
					case 112:
						match state
							case 6:
								(DlgWindow editPosn:)
							#end:case
							else:
								(curItem editPosn:)
							#end:else
						#end:match
					#end:case
					case 116:
						match state
							case 6:
								(DlgWindow editTitle:)
							#end:case
							else:
								(curItem editText:)
							#end:else
						#end:match
					#end:case
					case 118:
						match state
							case 4:
								(curItem editView:)
							#end:case
							case 1:
								(curItem editValue:)
							#end:case
						#end:match
					#end:case
					case 119:
						match state
							case 0:
								(self changeState: 6)
							#end:case
							case 5:
								(curItem editWidth:)
							#end:case
							case 2:
								(curItem editWidth:)
							#end:case
						#end:match
					#end:case
					case 120:
						(self exit:)
						return
					#end:case
				#end:match
			#end:case
		#end:match
		return 0
	#end:method

	@classmethod
	def writeFile(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp102 = -1
		temp103 = 0
		temp104 = 0
		temp0 = 0
		while (temp0 < size): # inline for
			temp1 = (self at: temp0)
			match (temp1 -super-:)
				case _DButton:
					if ((temp1 font:) != temp102):
						temp102 = (temp1 font:)
						(Format @temp2 r"""\t\t\tfont:\t\t\t%d,\0d\n""" temp102)
						(param1 writeString: @temp2)
					#endif
					if (temp1 seq:):
						(Format
							@temp2
							r"""\t\t\taddButton:\t%d %d %d %d %d %d %d %d, \0d\n"""
							(temp1 value:)
							(temp1 noun:)
							(temp1 verb:)
							(temp1 case:)
							(temp1 seq:)
							(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
							(((temp1 nsTop:) - (DlgWindow top:)) - 4)
							(temp1 modNum:)
						)
					else:
						(Format
							@temp2
							r"""\t\t\taddButton:\t%d {%s\} %d %d,\0d\n"""
							(temp1 value:)
							(temp1 text:)
							(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
							(((temp1 nsTop:) - (DlgWindow top:)) - 4)
						)
					#endif
					(param1 writeString: @temp2)
				#end:case
				case _DText:
					if ((temp1 font:) != temp102):
						temp102 = (temp1 font:)
						(Format @temp2 r"""\t\t\tfont:\t\t\t%d,\0d\n""" temp102)
						(param1 writeString: @temp2)
					#endif
					if ((temp1 mode:) != temp103):
						temp103 = (temp1 mode:)
						(Format
							@temp2
							r"""\t\t\tmode:\t\t\t%s,\0d\n"""
							match (temp1 mode:)
								case 0: r"""teJustLeft"""#end:case
								case -1: r"""teJustRight"""#end:case
								case 1: r"""teJustCenter"""#end:case
							#end:match
						)
						(param1 writeString: @temp2)
					#endif
					if ((temp1 width:) != temp104):
						temp104 = (temp1 width:)
						(Format @temp2 r"""\t\t\twidth:\t\t%d, \0d\n""" temp104)
						(param1 writeString: @temp2)
					#endif
					if (temp1 seq:):
						(Format
							@temp2
							r"""\t\t\taddText:\t\t%d %d %d %d %d %d %d, \0d\n"""
							(temp1 noun:)
							(temp1 verb:)
							(temp1 case:)
							(temp1 seq:)
							(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
							(((temp1 nsTop:) - (DlgWindow top:)) - 4)
							(temp1 modNum:)
						)
					else:
						(Format
							@temp2
							r"""\t\t\taddText:\t\t{%s\} %d %d,\0d\n"""
							(temp1 text:)
							(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
							(((temp1 nsTop:) - (DlgWindow top:)) - 4)
						)
					#endif
					(param1 writeString: @temp2)
				#end:case
				case _DEdit:
					if ((temp1 font:) != temp102):
						temp102 = (temp1 font:)
						(Format @temp2 r"""\t\t\tfont:\t\t\t%d,\0d\n""" temp102)
						(param1 writeString: @temp2)
					#endif
					(Format
						@temp2
						r"""\t\t\taddEdit:\t\t@str %d %d %d {%s\},\0d\n"""
						(temp1 max:)
						(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
						(((temp1 nsTop:) - (DlgWindow top:)) - 4)
						(temp1 text:)
					)
					(param1 writeString: @temp2)
				#end:case
				case _DIcon:
					(Format
						@temp2
						r"""\t\t\taddIcon:\t\t%d %d %d %d %d,\0d\n"""
						(temp1 view:)
						(temp1 loop:)
						(temp1 cel:)
						(((temp1 nsLeft:) - (DlgWindow left:)) - 4)
						(((temp1 nsTop:) - (DlgWindow top:)) - 4)
					)
					(param1 writeString: @temp2)
				#end:case
				case _DSelector:#end:case
			#end:match
			# for:reinit
			temp0++
		#end:loop
	#end:method

#end:class or instance

