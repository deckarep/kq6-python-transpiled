#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 947
import sci_sh
import kernel
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
def localproc_0(param1 = None, param2 = None, *rest):
	if (kernel.StrLen(param1) > param2):
		kernel.StrAt(param1, param2, 0)
		kernel.StrAt(param1, param2.post('--'), 46)
		kernel.StrAt(param1, param2.post('--'), 46)
		kernel.StrAt(param1, param2.post('--'), 46)
	#endif
	return param1
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	temp0 = param1._send('noun:')
	temp1 = param1._send('verb:')
	temp2 = param1._send('case:')
	temp3 = param1._send('seq:')
	temp4 = param1._send('modNum:')
	kernel.Format(@temp5, r"""%d""", temp0)
	kernel.Format(@temp15, r"""%d""", temp1)
	kernel.Format(@temp25, r"""%d""", temp2)
	kernel.Format(@temp35, r"""%d""", temp3)
	kernel.Format(@temp45, r"""%d""", temp4)
	if 
		Print._send(
			'addTitle:', @local42,
			'font:', 0,
			'addText:', r"""Enter new message parameters:""",
			'addText:', r"""Noun""", 5, 25,
			'addText:', r"""Verb""", 85, 25,
			'addText:', r"""Case""", 5, 39,
			'addText:', r"""Seq""", 85, 39,
			'addText:', r"""Module""", 47, 53,
			'addEdit:', @temp5, 4, 45, 25, @temp5,
			'addEdit:', @temp15, 4, 125, 25, @temp15,
			'addEdit:', @temp25, 4, 45, 39, @temp25,
			'addEdit:', @temp35, 4, 125, 39, @temp35,
			'addEdit:', @temp45, 5, 101, 53, @temp45,
			'addButton:', 1, r"""___OK___""", 18, 67,
			'addButton:', 0, r"""Cancel""", 91, 67,
			'init:'
		)
		temp0 = kernel.ReadNumber(@temp5)
		temp1 = kernel.ReadNumber(@temp15)
		temp2 = kernel.ReadNumber(@temp25)
		temp3 = kernel.ReadNumber(@temp35)
		temp4 = kernel.ReadNumber(@temp45)
		(cond
			case (not kernel.Message(0, temp4, temp0, temp1, temp2, temp3)):
				proc921_0(r"""Can't find message!""")
				return 0
			#end:case
			case (not kernel.Message(2, temp4, temp0, temp1, temp2, temp3)):
				proc921_0(r"""Message contains no text!""")
				return 0
			#end:case
			else:
				param1._send(
					'noun:', temp0,
					'verb:', temp1,
					'case:', temp2,
					'seq:', temp3,
					'modNum:', temp4
				)
				return 1
			#end:else
		)
	else:
		return 0
	#endif
#end:procedure

@SCI.procedure
def localproc_2(param1 = None, *rest):
	Print._send(
		'addTitle:', @local42,
		'font:', 0,
		'width:', 50,
		'addText:', r"""What kind of text?""",
		'addButton:', 1, r""" Literal """, 60, 0,
		'addButton:', 2, r"""MSG file""", 60, 14,
		'addButton:', 0, r"""__Cancel__""", 60, 28,
		'first:', (2 if param1._send('seq:') else 1),
		'init:'
	)
#end:procedure

@SCI.instance
class mainMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local62)
	#end:method

#end:class or instance

@SCI.instance
class editBMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local90)
	#end:method

#end:class or instance

@SCI.instance
class editTMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local112)
	#end:method

#end:class or instance

@SCI.instance
class editEMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local137)
	#end:method

#end:class or instance

@SCI.instance
class editIMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local159)
	#end:method

#end:class or instance

@SCI.instance
class editSMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local181)
	#end:method

#end:class or instance

@SCI.instance
class editWMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local200)
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
		type = (4 if title else 0)
		temp0 = kernel.GetPort()
		super._send('open:', &rest)
		kernel.SetPort(temp0)
		local1 = 1
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		local1 = 0
	#end:method

	@classmethod
	def create():
		temp0 = 190
		temp1 = 320
		temp2 = 0
		temp3 = 0
		temp4 = 0
		while (temp4 < DialogEditor._send('size:')): # inline for
			temp5 = DialogEditor._send('at:', temp4)
			temp0 = proc999_2(temp5._send('nsTop:'), temp0)
			temp1 = proc999_2(temp5._send('nsLeft:'), temp1)
			temp2 = proc999_3(temp5._send('nsBottom:'), temp2)
			temp3 = proc999_3(temp5._send('nsRight:'), temp3)
			# for:reinit
			temp4.post('++')
		#end:loop
		DialogEditor._send('eachElementDo:', #hide)
		self._send('dispose:')
		top = (temp0 - 4)
		bottom = (temp2 + 4)
		left = (temp1 - 4)
		right = (temp3 + 4)
		self._send('open:')
		DialogEditor._send('eachElementDo:', #draw)
	#end:method

	@classmethod
	def moveTo(param1 = None, param2 = None, *rest):
		temp0 = 0
		while (temp0 < DialogEditor._send('size:')): # inline for
			temp1 = DialogEditor._send('at:', temp0)
			temp2 = (temp1._send('nsLeft:') - left)
			temp3 = (temp1._send('nsTop:') - top)
			temp1._send('hide:', 'moveTo:', (param1 + temp2), (param2 + temp3))
			# for:reinit
			temp0.post('++')
		#end:loop
		left = param1
		top = param2
		self._send('create:')
	#end:method

	@classmethod
	def editMsg():
		if localproc_1(self):
			if title:
				kernel.Memory(3, title)
			#endif
			title = kernel.Memory(1, kernel.Message(2, modNum, noun, verb, case, seq))
			kernel.Message(0, modNum, noun, verb, case, seq, title)
		#endif
		self._send('create:')
	#end:method

	@classmethod
	def editPosn():
		if local1:
			proc921_0(r"""Click to where the top left of the window should be""")
			while (temp0 = Event._send('new:')._send('type:') != 1):

				temp0._send('dispose:')
			#end:loop
			temp1 = temp0._send('x:')
			temp2 = (temp0._send('y:') - 10)
			temp0._send('dispose:')
			temp3 = (bottom - top)
			temp4 = (right - left)
			temp1 = proc999_3(0, proc999_2(temp1, (320 - temp4)))
			temp2 = proc999_3(0, proc999_2(temp2, (190 - temp3)))
			self._send('moveTo:', temp1, temp2)
		else:
			proc921_0(r"""No window to position!""")
		#endif
	#end:method

	@classmethod
	def editTitle():
		match localproc_2(self)
			case 0:
				return
			#end:case
			case 2:
				self._send('editMsg:')
				return
			#end:case
		#end:match
		if seq:
			kernel.Memory(3, title)
			noun = verb = case = seq = modNum = title = 0
		#endif
		if (not title):
			title = kernel.Memory(1, 50)
			kernel.StrCpy(title, r"""title""")
		#endif
		Print._send(
			'addTitle:', @local42,
			'addText:', r"""Enter new title:""",
			'addEdit:', title, 50, 0, 12, title,
			'init:'
		)
		self._send('create:')
	#end:method

#end:class or instance

class _DItem(Class_255_0):
	#property vars (may be empty)
	underBits = 0
	
	@classmethod
	def select(param1 = None, *rest):
		self._send('hide:')
		if param1:
			(state |= 0x0008)
		else:
			(state &= 0xfff7)
		#endif
		self._send('draw:')
	#end:method

	@classmethod
	def hide():
		if underBits:
			kernel.Graph(8, underBits)
			temp0 = (nsTop - 1)
			temp1 = (nsLeft - 1)
			temp2 = (nsBottom + 1)
			temp3 = (nsRight + 1)
			underBits = 0
			kernel.Graph(13, temp0, temp1, temp2, temp3)
		#endif
	#end:method

	@classmethod
	def draw():
		temp0 = (nsTop - 1)
		temp1 = (nsLeft - 1)
		temp2 = (nsBottom + 1)
		temp3 = (nsRight + 1)
		if underBits:
			kernel.UnLoad(133, underBits)
			underBits = 0
		#endif
		underBits = kernel.Graph(7, temp0, temp1, temp2, temp3, 1)
		kernel.DrawControl(self)
	#end:method

	@classmethod
	def editPosn():
		kernel.Format(@temp0, r"""%d""", nsLeft)
		kernel.Format(@temp25, r"""%d""", nsTop)
		if 
			(= temp30
				Print._send(
					'addTitle:', @local42,
					'addText:', r"""Enter new position:""",
					'addText:', r"""x = """, 0, 12,
					'addText:', r"""y = """, 65, 12,
					'addEdit:', @temp0, 5, 25, 12, @temp0,
					'addEdit:', @temp25, 6, 90, 12, @temp25,
					'font:', 0,
					'addButton:', 0, r""" Cancel """, 35, 26,
					'init:'
				)
			)
			temp31 = proc999_3(4, kernel.ReadNumber(@temp0))
			temp32 = proc999_3(4, kernel.ReadNumber(@temp25))
			self._send('hide:', 'moveTo:', temp31, temp32, 'draw:')
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		temp0 = 0
		param1._send('claimed:', 1)
		temp0 = self._send('track:', param1)
	#end:method

	@classmethod
	def track(param1 = None, *rest):
		if (param1._send('type:') == 1):
			self._send('hide:')
			while True: #repeat
				param1 = Event._send('new:', -32768)
				param1._send('localize:')
				temp0 = param1._send('x:')
				temp1 = param1._send('y:')
				kernel.DrawStatus(kernel.Format(@temp2, r"""DRAGGING: %d, %d""", temp0, temp1))
				self._send('moveTo:', temp0, temp1)
				param1._send('dispose:')
				(breakif (not proc255_0()))
			#end:loop
			kernel.DrawStatus(r""" """, 0, 0)
			kernel.DrawStatus(0)
			if DialogEditor._send('curMenu:'):
				DialogEditor._send('curMenu:')._send('init:')
			#endif
			kernel.DrawPic(global2._send('picture:'), 100)
			if local1:
				DlgWindow._send('create:')
			else:
				DialogEditor._send('eachElementDo:', #draw)
			#endif
		#endif
	#end:method

	@classmethod
	def dispose():
		self._send('hide:')
		super._send('dispose:', &rest)
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
	def setSize(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.TextSize(@temp0[0], text, font, (param1 if argc else width))
		nsLeft.post('--')
		nsTop.post('--')
		nsBottom = (+ nsTop temp0[2] 1)
		nsRight = (+ nsLeft temp0[3] 1)
	#end:method

	@classmethod
	def editFont():
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'font:', 0,
				'width:', 90,
				'addText:', r"""Enter new font number:""",
				'addEdit:', @temp0, 6, 0, 24,
				'addButton:', 0, r""" System """, 100, 0,
				'addButton:', global22, r"""__User__""", 100, 14,
				'addButton:', global23, r"""__Small__""", 100, 28,
				'addButton:', global26, r"""___Big___""", 100, 42,
				'addButton:', -1, r""" Cancel """, 100, 56,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if (temp25 != -1):
			self._send('hide:', 'font:', temp25, 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def editJust():
		temp0 = 0
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'font:', 0,
				'width:', 100,
				'addText:', r"""Enter justification mode:""",
				'addButton:', 1, r"""___Left___""", 100, 0,
				'addButton:', 2, r""" Center """, 100, 14,
				'addButton:', 3, r"""__Right__""", 100, 28,
				'addButton:', 0, r""" Cancel """, 100, 42,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			self._send(
				'hide:',
				'mode:', match temp25
						case 1: 0#end:case
						case 2: 1#end:case
						case 3: -1#end:case
					#end:match,
				'setSize:',
				'draw:'
			)
		#endif
	#end:method

	@classmethod
	def editMsg():
		if localproc_1(self):
			kernel.Memory(3, text)
			text = kernel.Memory(1, kernel.Message(2, modNum, noun, verb, case, seq))
			kernel.Message(0, modNum, noun, verb, case, seq, text)
		#endif
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editText():
		match localproc_2(self)
			case 0:
				return
			#end:case
			case 2:
				self._send('editMsg:')
				return
			#end:case
		#end:match
		if seq:
			kernel.Memory(3, text)
			text = kernel.Memory(1, 100)
			kernel.StrCpy(text, r"""text""")
			noun = verb = case = seq = modNum = 0
		#endif
		Print._send(
			'addTitle:', @local42,
			'addText:', r"""Enter new text:""",
			'addEdit:', text, 50, 0, 12, text,
			'init:'
		)
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editWidth():
		kernel.Format(@temp0, r"""%d""", width)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new width:""",
				'addEdit:', @temp0, 6, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			self._send('hide:', 'width:', temp25, 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def showHelp():
		Print._send(
			'font:', global22,
			'width:', 250,
			'addText:', r"""Text Menu:\n\n__Text - Change the text\n__Font - Change the font of the text\n__Just - Change justification mode\n__Position - Change the position of the text\n__Menu - Return to the Main Menu\n""",
			'init:'
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
		nsRight = (nsLeft + kernel.CelWide(view, loop, cel))
		nsBottom = (nsTop + kernel.CelHigh(view, loop, cel))
	#end:method

	@classmethod
	def editView():
		kernel.Format(@temp0, r"""%d""", view)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new view number:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			view = temp25
		#endif
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editLoop():
		kernel.Format(@temp0, r"""%d""", loop)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new loop number:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			loop = temp25
		#endif
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editCel():
		kernel.Format(@temp0, r"""%d""", cel)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new cel number:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			cel = temp25
		#endif
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def showHelp():
		Print._send(
			'font:', global22,
			'width:', 250,
			'addText:', r"""Icon Menu:\n\n__View - Change the view of the icon\n__Loop - Change the loop of the icon\n__Cel - Change the cel of the icon\n__Position - Change the position of the icon\n__Menu - Return to the Main Menu\n""",
			'init:'
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
		kernel.TextSize(@temp0[0], text, font, 0, 0)
		(temp0[2] += 2)
		(temp0[3] += 2)
		nsBottom = (nsTop + temp0[2])
		temp0[3] = (((temp0[3] + 15) / 16) * 16)
		nsRight = (temp0[3] + nsLeft)
	#end:method

	@classmethod
	def editFont():
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'font:', 0,
				'width:', 90,
				'addText:', r"""Enter new font number:""",
				'addEdit:', @temp0, 6, 0, 24,
				'addButton:', 0, r""" System """, 100, 0,
				'addButton:', global22, r"""__User__""", 100, 14,
				'addButton:', global23, r"""__Small__""", 100, 28,
				'addButton:', global26, r"""___Big___""", 100, 42,
				'addButton:', -1, r""" Cancel """, 100, 56,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if (temp25 != -1):
			self._send('hide:', 'font:', temp25, 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def editMsg():
		if localproc_1(self):
			kernel.Memory(3, text)
			text = kernel.Memory(1, kernel.Message(2, modNum, noun, verb, case, seq))
			kernel.Message(0, modNum, noun, verb, case, seq, text)
		#endif
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editText():
		match localproc_2(self)
			case 0:
				return
			#end:case
			case 2:
				self._send('editMsg:')
				return
			#end:case
		#end:match
		if seq:
			kernel.Memory(3, text)
			text = kernel.Memory(1, 50)
			kernel.StrCpy(text, r"""button""")
			noun = verb = case = seq = modNum = 0
		#endif
		Print._send(
			'addTitle:', @local42,
			'addText:', r"""Enter new text:""",
			'addEdit:', text, 50, 0, 12, text,
			'init:'
		)
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def editValue():
		kernel.Format(@temp0, r"""%d""", value)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new value:""",
				'addEdit:', @temp0, 6, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			value = temp25
		#endif
	#end:method

	@classmethod
	def showHelp():
		Print._send(
			'font:', global22,
			'width:', 250,
			'addText:', r"""Button Menu:\n\n__Text - Change the button text\n__Font - Change the font of the button text\n__Value - Change the return value of the button\n__Position - Change the position of the button\n__Menu - Return to the Main Menu\n""",
			'init:'
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
		kernel.TextSize(@temp0[0], r"""M""", font, 0, 0)
		nsBottom = (nsTop + temp0[2])
		nsRight = (nsLeft + ((* temp0[3] max 3) / 4))
		cursor = kernel.StrLen(text)
	#end:method

	@classmethod
	def editFont():
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'font:', 0,
				'width:', 90,
				'addText:', r"""Enter new font number:""",
				'addEdit:', @temp0, 6, 0, 24,
				'addButton:', 0, r""" System """, 100, 0,
				'addButton:', global22, r"""__User__""", 100, 14,
				'addButton:', global23, r"""__Small__""", 100, 28,
				'addButton:', global26, r"""___Big___""", 100, 42,
				'addButton:', -1, r""" Cancel """, 100, 56,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if (temp25 != -1):
			self._send('hide:', 'font:', temp25, 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def editLength():
		kernel.Format(@temp0, r"""%d""", max)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new maximum length:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			self._send('max:', temp25, 'hide:', 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def editText():
		Print._send(
			'addTitle:', @local42,
			'addText:', r"""Enter new default text:""",
			'addEdit:', text, 25, 0, 12, text,
			'init:'
		)
		self._send('hide:', 'setSize:', 'draw:')
	#end:method

	@classmethod
	def showHelp():
		Print._send(
			'font:', global22,
			'width:', 250,
			'addText:', r"""Edit Menu:\n\n__Font - Change the font of the edit text\n__Length - Change the maximum length of input\n__Position - Change the position of the edit\n__Text - Change the default edit text\n__Menu - Return to the Main Menu\n""",
			'init:'
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
		kernel.TextSize(@temp0[0], r"""M""", font, 0, 0)
		nsBottom = (+ nsTop 20 (temp0[2] * y))
		nsRight = (nsLeft + ((* temp0[3] x 3) / 4))
	#end:method

	@classmethod
	def editLength():
		kernel.Format(@temp0, r"""%d""", y)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new length:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			self._send('y:', temp25, 'hide:', 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def editWidth():
		kernel.Format(@temp0, r"""%d""", x)
		(= temp25
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""Enter new width:""",
				'addEdit:', @temp0, 5, 0, 12, @temp0,
				'font:', 0,
				'addButton:', 0, r""" Cancel """, 0, 26,
				'init:'
			)
		)
		if temp0:
			temp25 = kernel.ReadNumber(@temp0)
		#endif
		if temp25:
			self._send('x:', temp25, 'hide:', 'setSize:', 'draw:')
		#endif
	#end:method

	@classmethod
	def showHelp():
		Print._send(
			'font:', global22,
			'width:', 250,
			'addText:', r"""Selector Menu:\n\n__Width - Change the selector width (in chars)\n__Length - Change number of selector lines\n__Position - Change the position of the selector\n__Menu - Return to the Main Menu\n""",
			'init:'
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
		local0 = global38
		kernel.StrCpy(@local42, r"""DialogEditor__v1.1""")
		global38 = SysWindow._send('color:', 0, 'back:', 255)
		global1._send('setCursor:', 999)
		self._send('changeState:', 0)
	#end:method

	@classmethod
	def dispose():
		mainMenu._send('dispose:')
		DlgWindow._send('dispose:')
		global38 = local0
		global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
		kernel.DrawStatus(r""" """, 0, 0)
		kernel.DrawStatus(0)
		super._send('dispose:')
		kernel.DrawPic(global2._send('picture:'), 100)
		kernel.DisposeScript(111)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		if curMenu:
			curMenu._send('dispose:')
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
			curMenu._send('init:')
		#endif
	#end:method

	@classmethod
	def delItem():
		if size:
			if 
				Print._send(
					'addText:', r"""Delete current item?""",
					'font:', 0,
					'addButton:', 1, r"""Yes""", 0, 12,
					'addButton:', 0, r"""No""", 40, 12,
					'init:'
				)
				self._send('delete:', curItem)
				curItem._send('dispose:')
				curItem = 0
				if size:
					curItem = self._send('at:', 0)
				#endif
			#endif
		else:
			proc921_0(r"""Nothing to delete!""")
		#endif
	#end:method

	@classmethod
	def exit():
		if (not local1):
			DlgWindow._send('create:')
		#endif
		if (not local2):
			kernel.Format(@local2, r"""%d.dlg""", global11)
		#endif
		if 
			(not
				(= temp100
					Print._send(
						'addTitle:', @local42,
						'addText:', r"""Save to: """,
						'addEdit:', @local2, 25, 60, 0, @local2,
						'font:', 0,
						'addButton:', 1, r"""__Save__""", 10, 12,
						'addButton:', 2, r""" Abandon """, 80, 12,
						'addButton:', 0, r""" Cancel """, 151, 12,
						'init:'
					)
				)
			)
			return 0
		#endif
		if (temp100 == 2):
			return 1
		#endif
		if kernel.FileIO(10, @local2):
			kernel.Format(@temp0, r"""The file '%s' already exists.__Now what?""", @local2)
			if 
				(not
					(= temp100
						Print._send(
							'addTitle:', @local42,
							'addText:', @temp0,
							'font:', 0,
							'addButton:', 1, r""" Replace """, 0, 24,
							'addButton:', 2, r""" Append """, 70, 24,
							'addButton:', 0, r""" Cancel """, 125, 24,
							'init:'
						)
					)
				)
				return 0
			#endif
		#endif
		temp102 = (2 if (temp100 == 1) else 0)
		if (not temp101 = File._send('new:')._send('name:', @local2, 'open:', temp102)):
			proc921_1(r"""Error opening '%s'""", temp101._send('name:'))
			temp101._send('dispose:')
			return 0
		#endif
		temp101._send(
			'writeString:', r"""\t\t; DialogEditor v1.0\0d\n""",
			'writeString:', r"""\t\t; by Brian K. Hughes\0d\n""",
			'writeString:', r"""\t\t(Print\0d\n"""
		)
		if local1:
			kernel.Format(@temp0, r"""\t\t\tposn:\t\t\t%d %d,\0d\n""", DlgWindow._send(
				'left:'
			), DlgWindow._send('top:'))
			temp101._send('writeString:', @temp0)
			if DlgWindow._send('title:'):
				if DlgWindow._send('seq:'):
					kernel.Format(@temp0, r"""\t\t\taddTitle:\t%d %d %d %d %d,\0d\n""", DlgWindow._send(
						'noun:'
					), DlgWindow._send('verb:'), DlgWindow._send('case:'), DlgWindow._send(
						'seq:'
					), DlgWindow._send('modNum:'))
				else:
					kernel.Format(@temp0, r"""\t\t\taddTitle:\t{%s\},\0d\n""", DlgWindow._send(
						'title:'
					))
				#endif
				temp101._send('writeString:', @temp0)
			#endif
		#endif
		self._send('writeFile:', temp101)
		if 
			Print._send(
				'addTitle:', @local42,
				'addText:', r"""This dialog should be...""",
				'font:', 0,
				'addButton:', 0, r"""___Modal___""", 0, 24,
				'addButton:', 1, r""" Modeless """, 0, 38,
				'init:'
			)
			temp101._send('writeString:', r"""\t\t\tmodeless:\tTRUE,\0d\n""")
		#endif
		temp101._send(
			'writeString:', r"""\t\t\tinit:\0d\n""",
			'writeString:', r"""\t\t)\0d\n"""
		)
		temp101._send('dispose:')
		return 1
	#end:method

	@classmethod
	def doit():
		self._send('init:')
		while True: #repeat
			temp0 = Event._send('new:')
			if (not curMenu._send('handleEvent:', temp0)):
				kernel.GlobalToLocal(temp0)
				(breakif self._send('handleEvent:', temp0))
			#endif
			temp0._send('dispose:')
		#end:loop
		temp0._send('dispose:')
		self._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		match param1._send('type:')
			case 0:#end:case
			case 1:
				if temp1 = self._send('firstTrue:', #check, param1):
					param1._send('claimed:', 1)
					if (param1._send('modifiers:') == 3):
						temp1._send('handleEvent:', param1)
					else:
						if curItem:
							curItem._send('select:', 0)
						#endif
						curItem = temp1._send('select:', 1)
						self._send('changeState:', 0)
					#endif
				#endif
			#end:case
			case 2:#end:case
			case 4:
				match param1._send('message:')
					case 63:
						param1._send('message:', 104)
					#end:case
					case 19:
						param1._send('message:', 120)
					#end:case
				#end:match
				match param1._send('message:')
					case 9:
						curItem._send('select:', 0)
						temp0 = DialogEditor._send('indexOf:', curItem)
						if (temp0.post('++') == DialogEditor._send('size:')):
							curItem = DialogEditor._send('at:', 0)
						else:
							curItem = DialogEditor._send('at:', temp0)
						#endif
						curItem._send('select:', 1)
						DialogEditor._send('changeState:', 0)
					#end:case
					case 3840:
						curItem._send('select:', 0)
						if (temp0 = DialogEditor._send('indexOf:', curItem) == 0):
							(= curItem
								DialogEditor._send('at:', (DialogEditor._send('size:') - 1))
							)
						else:
							curItem = DialogEditor._send('at:', temp0.post('--'))
						#endif
					#end:case
					case 32:#end:case
					case 8:#end:case
					case 97:
						Print._send(
							'addTitle:', @local42,
							'mode:', 1,
							'width:', 140,
							'addText:', r"""by Brian K. Hughes\n17 July, 1992""",
							'init:'
						)
					#end:case
					case 99:
						match state
							case 4:
								curItem._send('editCel:')
							#end:case
							case 6:
								if size:
									DlgWindow._send('create:')
								else:
									proc921_0(r"""Can't create window: no items!""")
								#endif
							#end:case
						#end:match
					#end:case
					case 100:
						match state
							case 0:
								self._send('delItem:')
							#end:case
							case 6:
								if local1:
									DlgWindow._send('dispose:')
									self._send('eachElementDo:', #draw)
								else:
									proc921_0(r"""No window to delete!""")
								#endif
							#end:case
						#end:match
					#end:case
					case 101:
						if size:
							self._send(
								'changeState:', match curItem._send('-super-:')
										case _DButton: 1#end:case
										case _DText: 2#end:case
										case _DEdit: 3#end:case
										case _DIcon: 4#end:case
										case _DSelector: 5#end:case
									#end:match
							)
						else:
							proc921_0(r"""No items to edit!""")
						#endif
					#end:case
					case 102:
						if proc999_5(state, 2, 1, 3):
							curItem._send('editFont:')
						#endif
					#end:case
					case 104:
						match state
							case 0:
								Print._send(
									'font:', global22,
									'width:', 250,
									'addText:', r"""Main Menu:\n\n__About - About the DialogEditor\n__Item - Create a new item\n__Edit - Edit properties of the current item\n__Look - View properties of the current item\n__Del - Delete the current item\n__Win - Create a window background\n__Help - You're here!\n__eXit - Exit the DialogEditor (& maybe save)\n""",
									'init:'
								)
							#end:case
							case 6:
								Print._send(
									'font:', global22,
									'width:', 250,
									'addText:', r"""Window Menu:\n\n__Create - Draw the window to the correct size\n__Position - Move the window and all items\n__Delete - Remove the window\n__Menu - Return to the Main Menu""",
									'init:'
								)
							#end:case
							else:
								curItem._send('showHelp:')
							#end:else
						#end:match
					#end:case
					case 105:
						temp1 = 0
						match
							Print._send(
								'addTitle:', @local42,
								'width:', 65,
								'addText:', r"""Select the kind of item you want to add to the dialog:""",
								'font:', 0,
								'addButton:', 1, r"""__Button__""", 80, 0,
								'addButton:', 2, r"""___Text___""", 80, 14,
								'addButton:', 3, r"""___Edit___""", 80, 28,
								'addButton:', 4, r"""___Icon___""", 80, 42,
								'addButton:', 6, r""" Selector """, 80, 56,
								'addButton:', 0, r"""__Cancel__""", 80, 70,
								'init:'
							)
							case 1:
								temp0 = kernel.Memory(1, 50)
								kernel.StrCpy(temp0, r"""button""")
								(= temp1
									_DButton._send('new:')._send('text:', temp0, 'yourself:')
								)
							#end:case
							case 2:
								temp0 = kernel.Memory(1, 100)
								kernel.StrCpy(temp0, r"""text""")
								temp1 = _DText._send('new:')._send('text:', temp0, 'yourself:')
							#end:case
							case 3:
								temp0 = kernel.Memory(1, 50)
								kernel.StrCpy(temp0, r"""""")
								(= temp1
									_DEdit._send('new:')._send('text:', temp0, 'max:', 5, 'yourself:')
								)
							#end:case
							case 4:
								(= temp1
									_DIcon._send('new:')._send(
										'view:', 0,
										'loop:', 0,
										'cel:', 0,
										'yourself:'
									)
								)
							#end:case
							case 6:
								(= temp1
									_DSelector._send('new:')._send('x:', 10, 'y:', 1, 'yourself:')
								)
							#end:case
						#end:match
						if temp1:
							if curItem:
								curItem._send('select:', 0)
							#endif
							curItem = temp1
							if local1:
								DlgWindow._send('dispose:')
							#endif
							self._send(
								'addToEnd:', curItem._send(
										'setSize:',
										'moveTo:', 4, 4,
										'yourself:'
									),
								'eachElementDo:', #draw
							)
							curItem._send('select:', 1)
						#endif
					#end:case
					case 106:
						if (state == 2):
							curItem._send('editJust:')
						#endif
					#end:case
					case 108:
						match state
							case 0:
								if curItem:
									kernel.Format(@temp508, r"""__x:_______%d""", curItem._send(
										'nsLeft:'
									))
									kernel.Format(@temp538, r"""__y:_______%d""", curItem._send(
										'nsTop:'
									))
									match curItem._send('-super-:')
										case _DText:
											kernel.StrCpy(@temp788, r"""Text Item""")
											kernel.StrCpy(@temp2, curItem._send('text:'))
											kernel.Format(@temp568, r"""__text:___%s""", localproc_0(@temp2, 15))
											kernel.Format(@temp598, r"""__font:___%d""", curItem._send(
												'font:'
											))
											kernel.Format(@temp628, r"""__width:__%d""", curItem._send(
												'width:'
											))
											kernel.Format(@temp658, r"""__noun:___%d""", curItem._send(
												'noun:'
											))
											kernel.Format(@temp678, r"""__verb:___%d""", curItem._send(
												'verb:'
											))
											kernel.Format(@temp708, r"""__case:___%d""", curItem._send(
												'case:'
											))
											kernel.Format(@temp738, r"""__seq:____%d""", curItem._send(
												'seq:'
											))
											kernel.Format(@temp758, r"""__modNum: %d""", curItem._send(
												'modNum:'
											))
										#end:case
										case _DButton:
											kernel.StrCpy(@temp788, r"""Button Item""")
											kernel.StrCpy(@temp2, curItem._send('text:'))
											kernel.Format(@temp568, r"""__text:___%s""", localproc_0(@temp2, 15))
											kernel.Format(@temp598, r"""__font:___%d""", curItem._send(
												'font:'
											))
											kernel.Format(@temp628, r"""__value:__%d""", curItem._send(
												'value:'
											))
											kernel.Format(@temp658, r"""__noun:___%d""", curItem._send(
												'noun:'
											))
											kernel.Format(@temp678, r"""__verb:___%d""", curItem._send(
												'verb:'
											))
											kernel.Format(@temp708, r"""__case:___%d""", curItem._send(
												'case:'
											))
											kernel.Format(@temp738, r"""__seq:____%d""", curItem._send(
												'seq:'
											))
											kernel.Format(@temp758, r"""__modNum: %d""", curItem._send(
												'modNum:'
											))
										#end:case
										case _DIcon:
											kernel.StrCpy(@temp788, r"""Icon Item""")
											kernel.Format(@temp568, r"""__view:___%d""", curItem._send(
												'view:'
											))
											kernel.Format(@temp598, r"""__loop:___%d""", curItem._send(
												'loop:'
											))
											kernel.Format(@temp628, r"""__cel:____%d""", curItem._send(
												'cel:'
											))
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
											kernel.StrCpy(@temp788, r"""Edit Item""")
											kernel.StrCpy(@temp2, curItem._send('text:'))
											kernel.Format(@temp568, r"""__text:___%s""", localproc_0(@temp2, 15))
											kernel.Format(@temp598, r"""__font:___%d""", curItem._send(
												'font:'
											))
											kernel.Format(@temp628, r"""__max:____%d""", curItem._send(
												'max:'
											))
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
											kernel.StrCpy(@temp788, r"""Selector Item""")
											kernel.Format(@temp568, r"""__width:__%d""", curItem._send(
												'x:'
											))
											kernel.Format(@temp598, r"""__length: %d""", curItem._send(
												'y:'
											))
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
									Print._send(
										'addTitle:', @temp788,
										'addText:', @temp508,
										'addText:', @temp538, 0, 12,
										'addText:', @temp568, 0, 24,
										'addText:', @temp598, 0, 36,
										'addText:', @temp628, 0, 48,
										'addText:', @temp658, 0, 60,
										'addText:', @temp678, 0, 72,
										'addText:', @temp708, 0, 84,
										'addText:', @temp738, 0, 96,
										'addText:', @temp758, 0, 108,
										'init:'
									)
									if local1:
										DlgWindow._send('create:')
									#endif
								else:
									proc921_0(r"""No item to look at!""")
								#endif
							#end:case
							case 4:
								curItem._send('editLoop:')
							#end:case
							case 3:
								curItem._send('editLength:')
							#end:case
							case 5:
								curItem._send('editLength:')
							#end:case
						#end:match
					#end:case
					case 109:
						self._send('changeState:', 0)
					#end:case
					case 112:
						match state
							case 6:
								DlgWindow._send('editPosn:')
							#end:case
							else:
								curItem._send('editPosn:')
							#end:else
						#end:match
					#end:case
					case 116:
						match state
							case 6:
								DlgWindow._send('editTitle:')
							#end:case
							else:
								curItem._send('editText:')
							#end:else
						#end:match
					#end:case
					case 118:
						match state
							case 4:
								curItem._send('editView:')
							#end:case
							case 1:
								curItem._send('editValue:')
							#end:case
						#end:match
					#end:case
					case 119:
						match state
							case 0:
								self._send('changeState:', 6)
							#end:case
							case 5:
								curItem._send('editWidth:')
							#end:case
							case 2:
								curItem._send('editWidth:')
							#end:case
						#end:match
					#end:case
					case 120:
						self._send('exit:')
						return
					#end:case
				#end:match
			#end:case
		#end:match
		return 0
	#end:method

	@classmethod
	def writeFile(param1 = None, *rest):
		temp102 = -1
		temp103 = 0
		temp104 = 0
		temp0 = 0
		while (temp0 < size): # inline for
			temp1 = self._send('at:', temp0)
			match temp1._send('-super-:')
				case _DButton:
					if (temp1._send('font:') != temp102):
						temp102 = temp1._send('font:')
						kernel.Format(@temp2, r"""\t\t\tfont:\t\t\t%d,\0d\n""", temp102)
						param1._send('writeString:', @temp2)
					#endif
					if temp1._send('seq:'):
						kernel.Format(@temp2, r"""\t\t\taddButton:\t%d %d %d %d %d %d %d %d, \0d\n""", temp1._send(
							'value:'
						), temp1._send('noun:'), temp1._send('verb:'), temp1._send(
							'case:'
						), temp1._send('seq:'), (-
							(temp1._send('nsLeft:') - DlgWindow._send('left:'))
							4
						), ((temp1._send('nsTop:') - DlgWindow._send('top:')) - 4), temp1._send(
							'modNum:'
						))
					else:
						kernel.Format(@temp2, r"""\t\t\taddButton:\t%d {%s\} %d %d,\0d\n""", temp1._send(
							'value:'
						), temp1._send('text:'), (-
							(temp1._send('nsLeft:') - DlgWindow._send('left:'))
							4
						), ((temp1._send('nsTop:') - DlgWindow._send('top:')) - 4))
					#endif
					param1._send('writeString:', @temp2)
				#end:case
				case _DText:
					if (temp1._send('font:') != temp102):
						temp102 = temp1._send('font:')
						kernel.Format(@temp2, r"""\t\t\tfont:\t\t\t%d,\0d\n""", temp102)
						param1._send('writeString:', @temp2)
					#endif
					if (temp1._send('mode:') != temp103):
						temp103 = temp1._send('mode:')
						kernel.Format(@temp2, r"""\t\t\tmode:\t\t\t%s,\0d\n""", match
							temp1._send('mode:')
							case 0: r"""teJustLeft"""#end:case
							case -1: r"""teJustRight"""#end:case
							case 1: r"""teJustCenter"""#end:case
						#end:match)
						param1._send('writeString:', @temp2)
					#endif
					if (temp1._send('width:') != temp104):
						temp104 = temp1._send('width:')
						kernel.Format(@temp2, r"""\t\t\twidth:\t\t%d, \0d\n""", temp104)
						param1._send('writeString:', @temp2)
					#endif
					if temp1._send('seq:'):
						kernel.Format(@temp2, r"""\t\t\taddText:\t\t%d %d %d %d %d %d %d, \0d\n""", temp1._send(
							'noun:'
						), temp1._send('verb:'), temp1._send('case:'), temp1._send(
							'seq:'
						), ((temp1._send('nsLeft:') - DlgWindow._send('left:')) - 4), (-
							(temp1._send('nsTop:') - DlgWindow._send('top:'))
							4
						), temp1._send('modNum:'))
					else:
						kernel.Format(@temp2, r"""\t\t\taddText:\t\t{%s\} %d %d,\0d\n""", temp1._send(
							'text:'
						), ((temp1._send('nsLeft:') - DlgWindow._send('left:')) - 4), (-
							(temp1._send('nsTop:') - DlgWindow._send('top:'))
							4
						))
					#endif
					param1._send('writeString:', @temp2)
				#end:case
				case _DEdit:
					if (temp1._send('font:') != temp102):
						temp102 = temp1._send('font:')
						kernel.Format(@temp2, r"""\t\t\tfont:\t\t\t%d,\0d\n""", temp102)
						param1._send('writeString:', @temp2)
					#endif
					kernel.Format(@temp2, r"""\t\t\taddEdit:\t\t@str %d %d %d {%s\},\0d\n""", temp1._send(
						'max:'
					), ((temp1._send('nsLeft:') - DlgWindow._send('left:')) - 4), (-
						(temp1._send('nsTop:') - DlgWindow._send('top:'))
						4
					), temp1._send('text:'))
					param1._send('writeString:', @temp2)
				#end:case
				case _DIcon:
					kernel.Format(@temp2, r"""\t\t\taddIcon:\t\t%d %d %d %d %d,\0d\n""", temp1._send(
						'view:'
					), temp1._send('loop:'), temp1._send('cel:'), (-
						(temp1._send('nsLeft:') - DlgWindow._send('left:'))
						4
					), ((temp1._send('nsTop:') - DlgWindow._send('top:')) - 4))
					param1._send('writeString:', @temp2)
				#end:case
				case _DSelector:#end:case
			#end:match
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

#end:class or instance

