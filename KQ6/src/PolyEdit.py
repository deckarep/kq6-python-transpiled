#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 943
import sci_sh
import kernel
import Main
import Print
import Polygon
import Window
import File
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2
local42 = None
local43 = None
local44 = None
local45 = None
local46 = [r"""EDITING""", 0, 0, r"""About""", 0, 0, r"""Map""", 0, 0, r"""Create""", 0, 0, r"""Type""", 0, 0, r"""Undo""", 0, 0, r"""Help""", 0, 0, r"""eXit""", 120, 0, 0]
local71 = [r"""CREATING""", 0, 0, r"""About""", 0, 0, r"""Map""", 0, 0, r"""Done""", 0, 0, r"""Undo""", 0, 0, r"""Help""", 0, 0, r"""eXit""", 120, 0, 0]


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	local45 = local44 = 0
	local43 = local42 = 32767
	temp0 = 0
	while (temp0 < argc): # inline for
		temp1 = param1[temp0]
		if (temp2 = param1[(temp0 + 1)] < local42):
			local42 = temp2
		#endif
		if (temp2 > local44):
			local44 = temp2
		#endif
		if (temp1 < local43):
			local43 = temp1
		#endif
		if (temp1 > local45):
			local45 = temp1
		#endif
		# for:reinit
		(temp0 += 2)
	#end:loop
	(local43 -= 2)
	(local42 -= 2)
	(local45 += 2)
	(local44 += 2)
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
	(return
		(+
			(((param1 / 2) + 1) * ((param3 / 2) + 1))
			(((param2 / 2) + 1) * ((param4 / 2) + 1))
		)
	)
#end:procedure

@SCI.procedure
def localproc_2(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, *rest):
	if 
		(and
			(<=
				0
				localproc_1((param3 - param1), (param4 - param2), (-
					param5
					param1
				), (param6 - param2))
			)
			(<=
				0
				localproc_1((param1 - param3), (param2 - param4), (-
					param5
					param3
				), (param6 - param4))
			)
		)
		(return
			if temp0 = kernel.GetDistance(param1, param2, param3, param4):
				(/
					kernel.Abs(localproc_1((param4 - param2), (param1 - param3), (-
						param5
						param1
					), (param6 - param2)))
					temp0
				)
			else:
				0
			#endif
		)
	else:
		(return
			proc999_2(kernel.GetDistance(param5, param6, param1, param2), kernel.GetDistance(param5, param6, param3, param4))
		)
	#endif
#end:procedure

@SCI.procedure
def localproc_3(param1 = None, param2 = None, *rest):
	Print._send(
		'width:', 240,
		'font:', 999,
		'mode:', param2,
		'addText:', param1,
		'addTitle:', r"""Polygon Editor 1.11""",
		'init:'
	)
#end:procedure

class ClickMenu(Obj):
	#property vars (may be empty)
	text = 0
	array = 0
	
	@classmethod
	def init(param1 = None, *rest):
		text = kernel.Memory(2, 81)
		kernel.Memory(6, text, 0)
		temp1 = array = param1
		temp48 = 0
		temp0 = 0
		while temp2 = kernel.Memory(5, temp1):

			kernel.StrCpy(@temp8, temp2)
			if (not temp0):
				kernel.StrCat(@temp8, r""": """)
			#endif
			kernel.StrCat(@temp8, r""" """)
			kernel.StrCat(text, @temp8)
			kernel.TextSize(@temp4, @temp8, 0, 0)
			(temp48 += temp4[3])
			kernel.Memory(6, (temp1 + 4), temp48)
			if (not kernel.Memory(5, (temp1 + 2))):
				temp49 = kernel.StrAt(temp2, 0)
				if (<= 65 temp49 90):
					(temp49 += 32)
				#endif
				kernel.Memory(6, (temp1 + 2), temp49)
			#endif
			temp0.post('++')
			(temp1 += 6)
		#end:loop
		kernel.DrawStatus(text)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if (param1._send('type:') != 1):
			return 0
		#endif
		if (param1._send('y:') >= 10):
			return 0
		#endif
		temp0 = array
		temp1 = 0
		while kernel.Memory(5, temp0):

			if ((param1._send('x:') < kernel.Memory(5, (temp0 + 4))) and temp1):
				param1._send('type:', 4, 'message:', kernel.Memory(5, (temp0 + 2)))
				return 0
			#endif
			temp1.post('++')
			(temp0 += 6)
		#end:loop
		param1._send('claimed:', 1)
	#end:method

	@classmethod
	def dispose():
		kernel.Memory(3, text)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class editMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local46)
	#end:method

#end:class or instance

@SCI.instance
class addMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', @local71)
	#end:method

#end:class or instance

class Class_943_1
	#property vars (may be empty)
	x = 0
	y = 0
	underBits = 0
	
	@classmethod
	def new():
		kernel.Clone(self)
	#end:method

	@classmethod
	def yourself():
		return self
	#end:method

	@classmethod
	def draw(param1 = None, param2 = None, *rest):
		if (local0 == 4):
			temp0 = -1
			temp1 = (3 if (param2 == 1) else 4)
		else:
			temp0 = 0
			temp1 = -1
		#endif
		kernel.Graph(4, y, x, param1._send('y:'), param1._send('x:'), temp0, -1, temp1)
	#end:method

	@classmethod
	def save(param1 = None, *rest):
		localproc_0(x, y, param1._send('x:'), param1._send('y:'))
		if underBits:
			kernel.UnLoad(133, underBits)
		#endif
		underBits = kernel.Graph(7, local42, local43, local44, local45, local0)
	#end:method

	@classmethod
	def restore():
		if underBits:
			kernel.Graph(8, underBits)
			underBits = 0
		#endif
	#end:method

	@classmethod
	def dispose():
		if underBits:
			kernel.UnLoad(133, underBits)
			underBits = 0
		#endif
		kernel.DisposeClone(self)
	#end:method

#end:class or instance

class _EditablePolygon(List):
	#property vars (may be empty)
	curNode = 0
	curPt = 0
	closed = 0
	type = 2
	srcList = 0
	closestPt = 0
	lsTop = 0
	lsLeft = 0
	lsBottom = 0
	lsRight = 0
	
	@classmethod
	def getAccessType():
		if 
			(= temp0
				Print._send(
					'addTitle:', r"""Polygon access type""",
					'addButton:', 1, r"""Total""", 0, 0,
					'addButton:', 2, r""" Near """, 60, 0,
					'addButton:', 3, r""" Barred """, 120, 0,
					'addButton:', 4, r""" Container """, 195, 0,
					'first:', type,
					'init:'
				)
			)
			type = (temp0 - 1)
		#endif
	#end:method

	@classmethod
	def writeFile(param1 = None, param2 = None, *rest):
		if (param2 == srcList):
			param1._send(
				'writeString:', r"""\t\t\t((Polygon new:)\0d\n""", r"""\t\t\t\ttype:\t\t""", match type
						case 0: r"""PTotalAccess"""#end:case
						case 1: r"""PNearestAccess"""#end:case
						case 2: r"""PBarredAccess"""#end:case
						case 3: r"""PContainedAccess"""#end:case
					#end:match, r""",\0d\n"""
			)
			param1._send('writeString:', r"""\t\t\t\tinit:\t\t""")
			temp14 = 1
			temp0 = 17
			temp3 = kernel.FirstNode(elements)
			while temp3: # inline for
				temp2 = kernel.NodeValue(temp3)
				kernel.Format(@temp4, 943, 0, temp2._send('x:'), temp2._send('y:'))
				if ((temp0 += temp1 = (kernel.StrLen(@temp4) + 1)) >= 80):
					param1._send('writeString:', r"""\0d\n\t\t\t\t\t\t""")
					temp14 = 1
					temp0 = (17 + temp1)
				#endif
				if (not temp14):
					param1._send('writeString:', r""" """)
				#endif
				param1._send('writeString:', @temp4)
				temp14 = 0
				# for:reinit
				temp3 = kernel.NextNode(temp3)
			#end:loop
			param1._send('writeString:', r""",\0d\n""")
			param1._send(
				'writeString:', r"""\t\t\t\tyourself:\0d\n""", r"""\t\t\t)\0d\n"""
			)
		#endif
	#end:method

	@classmethod
	def check():
		temp0 = self._send('first:')
		while temp0: # inline for
			temp2 = kernel.NodeValue(temp0)
			temp15 = kernel.NextNode(temp0)
			while temp15: # inline for
				temp16 = kernel.NodeValue(temp15)
				if 
					(and
						(temp2._send('x:') == temp16._send('x:'))
						(temp2._send('y:') == temp16._send('y:'))
					)
					temp15 = kernel.PrevNode(temp15)
					self._send('delete:', temp16)
					temp16._send('dispose:')
				#endif
				# for:reinit
				temp15 = kernel.NextNode(temp15)
			#end:loop
			# for:reinit
			temp0 = kernel.NextNode(temp0)
		#end:loop
		temp4 = 0
		temp9 = 0
		temp7 = 0
		temp8 = 1
		temp0 = temp6 = self._send('first:')
		while 1: # inline for
			temp2 = kernel.NodeValue(temp0)
			temp1 = self._send('next:', temp0)
			temp3 = kernel.NodeValue(temp1)
			temp4 = kernel.ATan(temp2._send('x:'), temp2._send('y:'), temp3._send('x:'), temp3._send('y:'))
			if (not temp8):
				(cond
					case (temp5 = (temp4 - temp9) > 180):
						(temp5 -= 360)
					#end:case
					case (temp5 < -180):
						(temp5 += 360)
					#end:case
				)
				(temp7 += temp5)
			#endif
			temp9 = temp4
			(breakif ((temp0 == temp6) and (not temp8)))
			temp8 = 0
			# for:reinit
			temp0 = temp1
		#end:loop
		if (type == 3):
			temp7 = -temp7
		#endif
		(cond
			case (temp7 == -360):
				temp0 = self._send('first:')
				
					(temp10 = self._send('last:'))
					((temp0 != temp10) and (temp0 != kernel.NextNode(temp10)))
					(temp10 = kernel.PrevNode(temp10))
					
					temp2 = kernel.NodeValue(temp0)
					temp11 = kernel.NodeValue(temp10)
					temp12 = temp2._send('x:')
					temp13 = temp2._send('y:')
					temp2._send('x:', temp11._send('x:'))
					temp2._send('y:', temp11._send('y:'))
					temp11._send('x:', temp12)
					temp11._send('y:', temp13)
					temp0 = kernel.NextNode(temp0)
					# for:reinit
					temp10 = kernel.PrevNode(temp10)
				#end:loop
			#end:case
			case (temp7 != 360):
				kernel.Format(@temp17, 943, 1, name, temp7)
				proc921_0(@temp17)
			#end:case
		)
	#end:method

	@classmethod
	def writeObstacle():
		temp1 = kernel.Memory(2, (size * 4))
		temp2 = kernel.FirstNode(elements)
		temp0 = temp1
		while temp2: # inline for
			temp3 = kernel.NodeValue(temp2)
			kernel.Memory(6, temp0, temp3._send('x:'))
			kernel.Memory(6, (temp0 + 2), temp3._send('y:'))
			temp2 = kernel.NextNode(temp2)
			# for:reinit
			(temp0 += 4)
		#end:loop
		if (srcList == 1):
			global95._send(
				'add:', Polygon._send('new:')._send(
						'type:', type,
						'points:', temp1,
						'size:', size,
						'dynamic:', 1,
						'yourself:'
					)
			)
		else:
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', type,
						'points:', temp1,
						'size:', size,
						'dynamic:', 1,
						'yourself:'
					)
			)
		#endif
	#end:method

	@classmethod
	def movePt(param1 = None, param2 = None, *rest):
		curPt._send('x:', param1, 'y:', param2)
	#end:method

	@classmethod
	def restore():
		self._send('eachLineDo:', #restore)
	#end:method

	@classmethod
	def save():
		self._send('eachLineDo:', #save)
	#end:method

	@classmethod
	def draw():
		self._send('eachLineDo:', #draw, srcList)
	#end:method

	@classmethod
	def add(param1 = None, param2 = None, param3 = None, *rest):
		super._send(
			'add:', curPt = Class_943_1._send('new:')._send('x:', param1, 'y:', param2, 'yourself:')
		)
		self._send('setCur:', kernel.FindKey(elements, curPt), param3)
	#end:method

	@classmethod
	def advance():
		self._send('setCur:', self._send('next:', curNode))
	#end:method

	@classmethod
	def retreat():
		self._send('setCur:', self._send('prev:', curNode))
	#end:method

	@classmethod
	def setCur(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if curNode = param1:
			curPt = kernel.NodeValue(curNode)
			if ((argc < 2) or param2):
				global1._send('setCursor:', 999, 1, curPt._send('x:'), curPt._send('y:'))
			#endif
		#endif
	#end:method

	@classmethod
	def setCurClosest(param1 = None, *rest):
		self._send('setCur:', kernel.FindKey(elements, closestPt), param1)
	#end:method

	@classmethod
	def startRedraw():
		if temp0 = self._send('next:', curNode):
			temp3 = kernel.NodeValue(temp0)
		else:
			temp3 = curPt
		#endif
		if temp1 = self._send('prev:', curNode):
			temp4 = kernel.NodeValue(temp1)
		else:
			temp4 = curPt
		#endif
		localproc_0(temp4._send('x:'), temp4._send('y:'), curPt._send('x:'), curPt._send(
			'y:'
		), temp3._send('x:'), temp3._send('y:'))
		lsTop = local42
		lsLeft = local43
		lsBottom = local44
		lsRight = local45
	#end:method

	@classmethod
	def endRedraw():
		localproc_0(curPt._send('x:'), curPt._send('y:'), lsLeft, lsTop, lsRight, lsBottom)
		kernel.Graph(12, local42, local43, local44, local45, local0)
	#end:method

	@classmethod
	def getDistToPt(param1 = None, param2 = None, *rest):
		temp4 = 32767
		temp1 = self._send('first:')
		temp0 = self._send('last:')
		while 1:

			temp2 = kernel.NodeValue(temp1)
			if 
				(<
					temp3 = kernel.GetDistance(param1, param2, temp2._send('x:'), temp2._send('y:'))
					temp4
				)
				temp4 = temp3
				closestPt = temp2
			#endif
			(breakif (temp1 == temp0))
			temp1 = self._send('next:', temp1)
		#end:loop
		return temp4
	#end:method

	@classmethod
	def getDistToLine(param1 = None, param2 = None, *rest):
		if (size < 2):
			return self._send('getDistToPt:', param1, param2, &rest)
		#endif
		temp4 = 32767
		temp1 = self._send('first:')
		temp0 = self._send('last:')
		while 1:

			temp2 = kernel.NodeValue(temp1)
			temp6 = self._send('next:', temp1)
			temp5 = kernel.NodeValue(temp6)
			if 
				(<
					(= temp3
						localproc_2(temp2._send('x:'), temp2._send('y:'), temp5._send(
							'x:'
						), temp5._send('y:'), param1, param2)
					)
					temp4
				)
				temp4 = temp3
				closestPt = temp2
			#endif
			(breakif (temp1 == temp0))
			temp1 = temp6
		#end:loop
		return temp4
	#end:method

	@classmethod
	def insertPt(param1 = None, param2 = None, *rest):
		temp0 = Class_943_1._send('new:')._send('x:', param1, 'y:', param2, 'yourself:')
		self._send('addAfter:', closestPt, temp0)
		self._send('setCur:', kernel.FindKey(elements, temp0))
	#end:method

	@classmethod
	def eachLineDo(param1 = None, *rest):
		temp0 = self._send('first:')
		temp4 = self._send('last:')
		while ((temp0 != temp4) or closed):

			temp1 = self._send('next:', temp0)
			temp2 = kernel.NodeValue(temp0)
			temp3 = kernel.NodeValue(temp1)
			temp2._send('param1:', temp3, &rest)
			(breakif (temp0 == temp4))
			temp0 = temp1
		#end:loop
	#end:method

	@classmethod
	def deletePt():
		if (curNode == temp0 = self._send('prev:', curNode)):
			temp0 = 0
		#endif
		self._send('delete:', curPt)
		curPt._send('dispose:')
		self._send('setCur:', temp0)
	#end:method

	@classmethod
	def next(param1 = None, *rest):
		temp0 = super._send('next:', param1)
		if (closed and (not temp0)):
			return super._send('first:')
		#endif
		return temp0
	#end:method

	@classmethod
	def prev(param1 = None, *rest):
		temp0 = super._send('prev:', param1)
		if (closed and (not temp0)):
			return super._send('last:')
		#endif
		return temp0
	#end:method

	@classmethod
	def saveForUndo():
		temp1 = temp0 = kernel.Memory(2, (2 * ((2 * size) + 3)))
		kernel.Memory(6, temp1, closed)
		(temp1 += 2)
		kernel.Memory(6, temp1, size)
		(temp1 += 2)
		kernel.Memory(6, temp1, self._send('indexOf:', curPt))
		(temp1 += 2)
		temp2 = self._send('first:')
		while temp2:

			temp3 = kernel.NodeValue(temp2)
			kernel.Memory(6, temp1, temp3._send('x:'))
			kernel.Memory(6, (temp1 += 2), temp3._send('y:'))
			temp2 = kernel.NextNode(temp2)
			(temp1 += 2)
		#end:loop
		return temp0
	#end:method

	@classmethod
	def undo(param1 = None, *rest):
		self._send('eachElementDo:', #dispose, 'release:')
		closed = kernel.Memory(5, param1)
		(param1 += 2)
		temp1 = kernel.Memory(5, param1)
		(param1 += 2)
		temp3 = kernel.Memory(5, param1)
		(param1 += 2)
		temp2 = 0
		while (temp2 < temp1):

			self._send('add:', kernel.Memory(5, param1), kernel.Memory(5, (param1 += 2)), 0)
			temp2.post('++')
			(param1 += 2)
		#end:loop
		self._send('setCur:', kernel.FindKey(elements, self._send('at:', temp3)), 0)
	#end:method

#end:class or instance

@SCI.instance
class readObstacle(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		temp2 = PolyEdit._send('add:')
		temp0 = 0
		temp1 = param1._send('points:')
		while (temp0 < param1._send('size:')): # inline for
			temp2._send(
				'add:', kernel.Memory(5, temp1), kernel.Memory(5, (temp1 + 2)), 0,
				'type:', param1._send('type:'),
				'srcList:', param2
			)
			temp0.post('++')
			# for:reinit
			(temp1 += 4)
		#end:loop
		temp2._send('closed:', 1)
	#end:method

#end:class or instance

class PolyEdit(List):
	#property vars (may be empty)
	curPolygon = 0
	x = 0
	y = 0
	state = 0
	isMouseDown = 0
	curMenu = 0
	undoPrvPoly = 0
	undoPoly = 0
	undoPolyBuf = 0
	undoX = 0
	undoY = 0
	undoState = 0
	
	@classmethod
	def handleEvent(param1 = None, *rest):
		temp1 = x
		temp2 = y
		x = param1._send('x:')
		y = param1._send('y:')
		match param1._send('type:')
			case 0:
				if curPolygon:
					if 
						(and
							isMouseDown
							(not proc999_5(state, 0, 2))
							((kernel.Abs((temp1 - x)) + kernel.Abs((temp2 - y))) > 1)
						)
						if (state != 3):
							self._send('saveForUndo:')
						#endif
						self._send('changeState:', 2)
					#endif
					if 
						(and
							proc999_5(state, 2, 0)
							((temp1 != x) or (temp2 != y))
						)
						self._send('movePt:', x, y)
					#endif
					if (state == 2):
						kernel.DrawStatus(kernel.Format(@temp3, 943, 2, x, y))
					#endif
				#endif
			#end:case
			case 1:
				temp0 = param1._send('modifiers:')
				isMouseDown = 1
				(cond
					case (temp0 & 0x0004):
						if (state == 0):
							self._send('finishAdding:')
							isMouseDown = 0
						else:
							self._send('insertPt:')
						#endif
					#end:case
					case (temp0 & 0x0003):
						if (state != 0):
							self._send('deletePt:')
						#endif
						isMouseDown = 0
					#end:case
					case (state == 0):
						self._send('addPt:')
					#end:case
					else:
						self._send('selectPt:')
					#end:else
				)
			#end:case
			case 2:
				isMouseDown = 0
				if proc999_5(state, 2, 3):
					self._send('changeState:', 1)
				#endif
			#end:case
			case 4:
				match param1._send('message:')
					case 63:
						param1._send('message:', 104)
					#end:case
					case 19:
						param1._send('message:', 120)
					#end:case
					case 15360:
						param1._send('message:', 12032)
					#end:case
					case 15872:
						param1._send('message:', 11776)
					#end:case
				#end:match
				match param1._send('message:')
					case 9:
						if ((state == 1) and curPolygon):
							self._send('advanceRetreat:', 65, 126)
						#endif
					#end:case
					case 3840:
						if ((state == 1) and curPolygon):
							self._send('advanceRetreat:', 130, 129)
						#endif
					#end:case
					case 32:
						if ((state == 1) and curPolygon):
							curPolygon._send('advance:')
						#endif
					#end:case
					case 8:
						if ((state == 1) and curPolygon):
							curPolygon._send('retreat:')
						#endif
					#end:case
					case 99:
						if (state == 1):
							self._send('changeState:', 0)
							curPolygon = 0
						#endif
					#end:case
					case 116:
						if (curPolygon and (state == 1)):
							curPolygon._send('getAccessType:')
						#endif
					#end:case
					case 100:
						(cond
							case (state == 1):
								if curPolygon:
									self._send('deletePt:')
								#endif
							#end:case
							case (state == 0):
								self._send('finishAdding:')
							#end:case
						)
					#end:case
					case 104:
						match state
							case 0:
								localproc_3(r"""___________CREATING POLYGON\0d\n\0d\nClick to create each corner of the polygon, then choose Done from the menu to finish.__You can also press Esc or Ctrl-click to finish.\0d\n\0d\nTo UNDO a corner, choose Undo.\0d\n\0d\nTo change MAP displayed (visual or control), choose Map.\0d\n\0d\nTo EXIT the Polygon Editor, choose eXit or press Ctrl-S.""", 0)
							#end:case
							case 1:
								localproc_3(r"""_____________EDITING POLYGON\0d\n\0d\nTo MOVE a corner, click on it and drag it to the new position.\0d\nTo INSERT a new corner, Ctrl-click to create it, then drag it to the correct position.\0d\nTo DELETE a corner, Shift-click on it.\0d\nTo UNDO an action, choose Undo from the menu.\0d\nTo CREATE a new polygon, choose Create.\0d\nTo change a polygon's TYPE (Total, Near or Barred), choose Type.\0d\nTo change MAP displayed (visual or control), choose Map.\0d\nTo EXIT the Polygon Editor, choose eXit or press Ctrl-S.\0d\n\0d\nIn addition to using the mouse, you can use Space and BackSpace to select corners and Tab and BackTab to select polygons. """, 0)
							#end:case
						#end:match
					#end:case
					case 117:
						self._send('undo:')
					#end:case
					case 109:
						self._send('showMap:', -1)
					#end:case
					case 12032:
						self._send('showMap:', 1)
					#end:case
					case 11776:
						self._send('showMap:', 4)
					#end:case
					case 97:
						localproc_3(r""" by\0d\n\0d\nMark Wilden\0d\n\0d\nOriginal program by Chad Bye """, 1)
					#end:case
					case 114:
						if (state == 1):
							self._send('draw:')
						#endif
					#end:case
					case 120:
						self._send('exit:')
						return
					#end:case
					case 27:
						if (state == 0):
							self._send('finishAdding:')
						#endif
					#end:case
				#end:match
			#end:case
		#end:match
		return 0
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		if curMenu:
			curMenu._send('dispose:')
		#endif
		(= curMenu
			match state = param1
				case 0: addMenu#end:case
				case 1: editMenu#end:case
				case 2: 0#end:case
				else: 0#end:else
			#end:match
		)
		if curMenu:
			curMenu._send('init:')
		#endif
	#end:method

	@classmethod
	def readObstacles():
		if global2._send('obstacles:'):
			global2._send('obstacles:')._send('eachElementDo:', #perform, readObstacle, 0)
		#endif
		if global95:
			global95._send('eachElementDo:', #perform, readObstacle, 1)
		#endif
	#end:method

	@classmethod
	def writeObstacles():
		if global2._send('obstacles:'):
			global2._send('obstacles:')._send('eachElementDo:', #dispose, 'release:')
		#endif
		self._send('eachElementDo:', #writeObstacle)
	#end:method

	@classmethod
	def add():
		super._send('add:', curPolygon = _EditablePolygon._send('new:'))
		return curPolygon
	#end:method

	@classmethod
	def draw():
		self._send('eachElementDo:', #restore)
		self._send('eachElementDo:', #save)
		self._send('eachElementDo:', #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def selectPt():
		self._send('select:', 486, 1)
		temp0 = Event._send('new:')
		kernel.GlobalToLocal(temp0)
		x = temp0._send('x:')
		y = temp0._send('y:')
		temp0._send('dispose:')
	#end:method

	@classmethod
	def addPt():
		self._send('saveForUndo:')
		if (not curPolygon):
			self._send('add:')
			curPolygon._send('add:', x, y, 0)
		#endif
		curPolygon._send('add:', x, y)
	#end:method

	@classmethod
	def finishAdding():
		(cond
			case curPolygon:
				curPolygon._send('closed:', 1)
				if (curPolygon._send('size:') > 1):
					curPolygon._send('deletePt:', curPolygon._send('last:'), 'advance:')
				#endif
				self._send('draw:')
				curPolygon._send('getAccessType:')
			#end:case
			case (not temp0 = self._send('first:')):
				curPolygon = 0
			#end:case
			else:
				curPolygon = kernel.NodeValue(temp0)
				self._send('draw:')
			#end:else
		)
		if curPolygon:
			self._send('changeState:', 1)
		#endif
	#end:method

	@classmethod
	def movePt(param1 = None, param2 = None, *rest):
		curPolygon._send('startRedraw:')
		self._send('eachElementDo:', #restore)
		curPolygon._send('movePt:', param1, param2)
		self._send('eachElementDo:', #save)
		self._send('eachElementDo:', #draw)
		curPolygon._send('endRedraw:')
	#end:method

	@classmethod
	def insertPt():
		self._send('eachElementDo:', #restore)
		self._send('select:', 485, 0)
		self._send('saveForUndo:')
		curPolygon._send('insertPt:', x, y)
		self._send('changeState:', 3)
		self._send('eachElementDo:', #save)
		self._send('eachElementDo:', #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def delete():
		temp0 = curPolygon
		self._send('advanceRetreat:', 130, 65)
		if (curPolygon == temp0):
			curPolygon = 0
		#endif
		super._send('delete:', temp0, &rest)
		temp0._send('dispose:')
	#end:method

	@classmethod
	def deletePt():
		self._send('eachElementDo:', #restore)
		self._send('select:', 486, 0)
		self._send('saveForUndo:')
		curPolygon._send('deletePt:')
		if (not curPolygon._send('size:')):
			self._send('delete:', curPolygon)
			if (not size):
				self._send('changeState:', 0)
			#endif
		#endif
		self._send('eachElementDo:', #save)
		self._send('eachElementDo:', #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def select(param1 = None, param2 = None, *rest):
		temp0 = 32767
		temp1 = 0
		temp4 = kernel.FirstNode(elements)
		while temp4: # inline for
			temp3 = kernel.NodeValue(temp4)
			if (temp2 = temp3._send('param1:', x, y) < temp0):
				temp0 = temp2
				temp1 = temp3
			#endif
			# for:reinit
			temp4 = kernel.NextNode(temp4)
		#end:loop
		curPolygon = temp1._send('setCurClosest:', param2)
	#end:method

	@classmethod
	def advanceRetreat(param1 = None, param2 = None, *rest):
		temp1 = kernel.FindKey(elements, curPolygon)
		if 
			(and
				(not temp0 = self._send('param1:', temp1))
				(not temp0 = self._send('param2:', temp1))
			)
			temp0 = temp1
		#endif
		curPolygon = kernel.NodeValue(temp0)
		curPolygon._send('setCur:', curPolygon._send('curNode:'))
	#end:method

	@classmethod
	def saveForUndo(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if undoPoly = curPolygon:
			undoPrvPoly = self._send('prev:', undoPoly)
			if (((not argc) or param1) and undoPolyBuf):
				kernel.Memory(3, undoPolyBuf)
			#endif
			undoPolyBuf = curPolygon._send('saveForUndo:')
		#endif
		undoX = x
		undoY = y
		undoState = state
	#end:method

	@classmethod
	def undo():
		if (not undoPoly):
			proc921_0(r"""Nothing to undo""")
			return
		#endif
		temp1 = undoPoly
		temp2 = undoPrvPoly
		temp3 = undoPolyBuf
		temp4 = undoX
		temp5 = undoY
		temp6 = undoState
		self._send('saveForUndo:', 0)
		self._send('eachElementDo:', #restore)
		if curPolygon = temp1:
			if (not self._send('contains:', curPolygon)):
				curPolygon = self._send('add:')
				if temp2:
					self._send('addAfter:', temp2, curPolygon)
				else:
					self._send('addToFront:', curPolygon)
				#endif
			#endif
			curPolygon._send('undo:', temp3)
		else:
			curPolygon = self._send('add:')
		#endif
		kernel.Memory(3, temp3)
		x = temp4
		y = temp5
		self._send('changeState:', temp6)
		self._send('eachElementDo:', #save)
		self._send('eachElementDo:', #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
		global1._send('setCursor:', 999, 1, x, y)
	#end:method

	@classmethod
	def showMap(param1 = None, *rest):
		if (param1 == -1):
			if (local0 == 1):
				param1 = 4
			else:
				param1 = 1
			#endif
		#endif
		if (local0 != param1):
			self._send('eachElementDo:', #restore)
			local0 = param1
			self._send('eachElementDo:', #save)
			self._send('eachElementDo:', #draw)
			kernel.Graph(12, 0, 0, 190, 320, local0)
		#endif
	#end:method

	@classmethod
	def init():
		kernel.DrawPic(global2._send('curPic:'), 100, 1)
		if (global36 != -1):
			kernel.DrawPic(global36, 100, 0)
		#endif
		global10._send('doit:')
		global5._send('eachElementDo:', #stopUpd)
		kernel.Animate(global5._send('elements:'), 0)
		local1 = global38
		global38 = SysWindow
		local0 = 1
		global1._send('setCursor:', 999, 1)
		self._send('readObstacles:')
		self._send('changeState:', (1 if size else 0))
		self._send('draw:')
	#end:method

	@classmethod
	def doit():
		self._send('init:')
		while True: #repeat
			temp0 = Event._send('new:')
			if (not (curMenu and curMenu._send('handleEvent:', temp0))):
				kernel.GlobalToLocal(temp0)
				(breakif self._send('handleEvent:', temp0))
			#endif
			temp0._send('dispose:')
		#end:loop
		temp0._send('dispose:')
		self._send('dispose:')
	#end:method

	@classmethod
	def exit():
		if (state == 0):
			self._send('finishAdding:')
		#endif
		self._send('showMap:', 1)
		if (not curPolygon):
			return 1
		#endif
		self._send('eachElementDo:', #check)
		if (not local2):
			kernel.Format(@local2, 943, 3, global2._send('curPic:'))
		#endif
		if 
			(not
				(= temp100
					Print._send(
						'addTitle:', r"""Save Polygons""",
						'addText:', r"""File:""",
						'addEdit:', @local2, 25, 50, 0, @local2,
						'addButton:', 1, r""" Save """, 5, 12,
						'addButton:', 2, r"""Abandon""", 70, 12,
						'addButton:', 0, r"""Cancel""", 150, 12,
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
			kernel.Format(@temp0, 943, 4, @local2)
			if 
				(not
					(= temp100
						Print._send(
							'width:', 210,
							'addText:', @temp0,
							'addButton:', 1, r"""Replace""", 5, 12,
							'addButton:', 2, r"""Append""", 85, 12,
							'addButton:', 0, r"""Cancel""", 150, 12,
							'init:'
						)
					)
				)
				return 0
			#endif
		#endif
		temp102 = (2 if (temp100 == 1) else 0)
		if (not temp101 = File._send('new:')._send('name:', @local2, 'open:', temp102)):
			kernel.Format(@temp0, 943, 5, temp101._send('name:'))
			proc921_0(@temp0)
			temp101._send('dispose:')
			return 0
		#endif
		temp101._send('writeString:', kernel.Format(@temp0, 943, 6, r"""Polygon Editor 1.11"""))
		temp101._send(
			'writeString:', kernel.Format(@temp0, 943, 7, r"""Dynamic Obstacles""", global2._send(
					'curPic:'
				))
		)
		temp101._send('writeString:', r"""\t\t(curRoom addObstacle:\0d\n""")
		self._send('eachElementDo:', #writeFile, temp101, 0)
		temp101._send('writeString:', r"""\t\t)\0d\n\0d\n""")
		temp101._send('writeString:', r"""\t\t(altPolyList add:\0d\n""")
		self._send('eachElementDo:', #writeFile, temp101, 1)
		temp101._send('writeString:', r"""\t\t)\0d\n""")
		temp101._send('dispose:')
		return 1
	#end:method

	@classmethod
	def dispose():
		self._send('writeObstacles:')
		if curMenu:
			curMenu._send('dispose:')
			curMenu = 0
		#endif
		if undoPolyBuf:
			kernel.Memory(3, undoPolyBuf)
			undoPolyBuf = 0
		#endif
		kernel.DrawStatus(r""" """, 0, 0)
		kernel.DrawStatus(0)
		global5._send('eachElementDo:', #startUpd)
		kernel.Animate(global5._send('elements:'), 0)
		self._send('eachElementDo:', #draw)
		if 
			Print._send(
				'addText:', r"""Erase polygon outlines?""",
				'addButton:', 1, r"""Yes """, 30, 12,
				'addButton:', 0, r""" No """, 85, 12,
				'init:'
			)
			kernel.DrawPic(global2._send('curPic:'), 100, 1)
			if (global36 != -1):
				kernel.DrawPic(global36, 100, 0)
			#endif
			global10._send('doit:')
		#endif
		global38 = local1
		kernel.DisposeScript(993)
		super._send('dispose:')
		kernel.DisposeScript(943)
	#end:method

#end:class or instance

