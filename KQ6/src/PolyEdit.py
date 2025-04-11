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
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

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
def localproc_1(param1 = None, param2 = None, param3 = None, param4 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		(+
			(((param1 / 2) + 1) * ((param3 / 2) + 1))
			(((param2 / 2) + 1) * ((param4 / 2) + 1))
		)
	)
#end:procedure

@SCI.procedure
def localproc_2(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if 
		(and
			(<=
				0
				(localproc_1
					(param3 - param1)
					(param4 - param2)
					(param5 - param1)
					(param6 - param2)
				)
			)
			(<=
				0
				(localproc_1
					(param1 - param3)
					(param2 - param4)
					(param5 - param3)
					(param6 - param4)
				)
			)
		)
		(return
			if temp0 = kernel.GetDistance(param1, param2, param3, param4):
				(/
					kernel.Abs((localproc_1
						(param4 - param2)
						(param1 - param3)
						(param5 - param1)
						(param6 - param2)
					))
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
def localproc_3(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(Print
		width: 240
		font: 999
		mode: param2
		addText: param1
		addTitle: r"""Polygon Editor 1.11"""
		init:
	)
#end:procedure

class ClickMenu(Obj):
	#property vars (may be empty)
	text = 0
	array = 0
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 type:) != 1):
			return 0
		#endif
		if ((param1 y:) >= 10):
			return 0
		#endif
		temp0 = array
		temp1 = 0
		while kernel.Memory(5, temp0):

			if (((param1 x:) < kernel.Memory(5, (temp0 + 4))) and temp1):
				(param1 type: 4 message: kernel.Memory(5, (temp0 + 2)))
				return 0
			#endif
			temp1.post('++')
			(temp0 += 6)
		#end:loop
		(param1 claimed: 1)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Memory(3, text)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class editMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local46)
	#end:method

#end:class or instance

@SCI.instance
class addMenu(ClickMenu):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: @local71)
	#end:method

#end:class or instance

class Class_943_1
	#property vars (may be empty)
	x = 0
	y = 0
	underBits = 0
	
	@classmethod
	def new():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Clone(self)
	#end:method

	@classmethod
	def yourself():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return self
	#end:method

	@classmethod
	def draw(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local0 == 4):
			temp0 = -1
			temp1 = (3 if (param2 == 1) else 4)
		else:
			temp0 = 0
			temp1 = -1
		#endif
		kernel.Graph(4, y, x, (param1 y:), (param1 x:), temp0, -1, temp1)
	#end:method

	@classmethod
	def save(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(localproc_0 x y (param1 x:) (param1 y:))
		if underBits:
			kernel.UnLoad(133, underBits)
		#endif
		underBits = kernel.Graph(7, local42, local43, local44, local45, local0)
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if underBits:
			kernel.Graph(8, underBits)
			underBits = 0
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(= temp0
				(Print
					addTitle: r"""Polygon access type"""
					addButton: 1 r"""Total""" 0 0
					addButton: 2 r""" Near """ 60 0
					addButton: 3 r""" Barred """ 120 0
					addButton: 4 r""" Container """ 195 0
					first: type
					init:
				)
			)
			type = (temp0 - 1)
		#endif
	#end:method

	@classmethod
	def writeFile(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param2 == srcList):
			(param1
				writeString:
					r"""\t\t\t((Polygon new:)\0d\n"""
					r"""\t\t\t\ttype:\t\t"""
					match type
						case 0: r"""PTotalAccess"""#end:case
						case 1: r"""PNearestAccess"""#end:case
						case 2: r"""PBarredAccess"""#end:case
						case 3: r"""PContainedAccess"""#end:case
					#end:match
					r""",\0d\n"""
			)
			(param1 writeString: r"""\t\t\t\tinit:\t\t""")
			temp14 = 1
			temp0 = 17
			temp3 = kernel.FirstNode(elements)
			while temp3: # inline for
				temp2 = kernel.NodeValue(temp3)
				kernel.Format(@temp4, 943, 0, (temp2 x:), (temp2 y:))
				if ((temp0 += temp1 = (kernel.StrLen(@temp4) + 1)) >= 80):
					(param1 writeString: r"""\0d\n\t\t\t\t\t\t""")
					temp14 = 1
					temp0 = (17 + temp1)
				#endif
				if (not temp14):
					(param1 writeString: r""" """)
				#endif
				(param1 writeString: @temp4)
				temp14 = 0
				# for:reinit
				temp3 = kernel.NextNode(temp3)
			#end:loop
			(param1 writeString: r""",\0d\n""")
			(param1
				writeString: r"""\t\t\t\tyourself:\0d\n""" r"""\t\t\t)\0d\n"""
			)
		#endif
	#end:method

	@classmethod
	def check():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (self first:)
		while temp0: # inline for
			temp2 = kernel.NodeValue(temp0)
			temp15 = kernel.NextNode(temp0)
			while temp15: # inline for
				temp16 = kernel.NodeValue(temp15)
				if 
					(and
						((temp2 x:) == (temp16 x:))
						((temp2 y:) == (temp16 y:))
					)
					temp15 = kernel.PrevNode(temp15)
					(self delete: temp16)
					(temp16 dispose:)
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
		temp0 = temp6 = (self first:)
		while 1: # inline for
			temp2 = kernel.NodeValue(temp0)
			temp1 = (self next: temp0)
			temp3 = kernel.NodeValue(temp1)
			temp4 = kernel.ATan((temp2 x:), (temp2 y:), (temp3 x:), (temp3 y:))
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
				temp0 = (self first:)
				
					(temp10 = (self last:))
					((temp0 != temp10) and (temp0 != kernel.NextNode(temp10)))
					(temp10 = kernel.PrevNode(temp10))
					
					temp2 = kernel.NodeValue(temp0)
					temp11 = kernel.NodeValue(temp10)
					temp12 = (temp2 x:)
					temp13 = (temp2 y:)
					(temp2 x: (temp11 x:))
					(temp2 y: (temp11 y:))
					(temp11 x: temp12)
					(temp11 y: temp13)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = kernel.Memory(2, (size * 4))
		temp2 = kernel.FirstNode(elements)
		temp0 = temp1
		while temp2: # inline for
			temp3 = kernel.NodeValue(temp2)
			kernel.Memory(6, temp0, (temp3 x:))
			kernel.Memory(6, (temp0 + 2), (temp3 y:))
			temp2 = kernel.NextNode(temp2)
			# for:reinit
			(temp0 += 4)
		#end:loop
		if (srcList == 1):
			(global95
				add:
					((Polygon new:)
						type: type
						points: temp1
						size: size
						dynamic: 1
						yourself:
					)
			)
		else:
			(global2
				addObstacle:
					((Polygon new:)
						type: type
						points: temp1
						size: size
						dynamic: 1
						yourself:
					)
			)
		#endif
	#end:method

	@classmethod
	def movePt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(curPt x: param1 y: param2)
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachLineDo: #restore)
	#end:method

	@classmethod
	def save():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachLineDo: #save)
	#end:method

	@classmethod
	def draw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachLineDo: #draw srcList)
	#end:method

	@classmethod
	def add(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super
			add: curPt = ((Class_943_1 new:) x: param1 y: param2 yourself:)
		)
		(self setCur: kernel.FindKey(elements, curPt) param3)
	#end:method

	@classmethod
	def advance():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setCur: (self next: curNode))
	#end:method

	@classmethod
	def retreat():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setCur: (self prev: curNode))
	#end:method

	@classmethod
	def setCur(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if curNode = param1:
			curPt = kernel.NodeValue(curNode)
			if ((argc < 2) or param2):
				(global1 setCursor: 999 1 (curPt x:) (curPt y:))
			#endif
		#endif
	#end:method

	@classmethod
	def setCurClosest(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setCur: kernel.FindKey(elements, closestPt) param1)
	#end:method

	@classmethod
	def startRedraw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (self next: curNode):
			temp3 = kernel.NodeValue(temp0)
		else:
			temp3 = curPt
		#endif
		if temp1 = (self prev: curNode):
			temp4 = kernel.NodeValue(temp1)
		else:
			temp4 = curPt
		#endif
		(localproc_0
			(temp4 x:)
			(temp4 y:)
			(curPt x:)
			(curPt y:)
			(temp3 x:)
			(temp3 y:)
		)
		lsTop = local42
		lsLeft = local43
		lsBottom = local44
		lsRight = local45
	#end:method

	@classmethod
	def endRedraw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(localproc_0 (curPt x:) (curPt y:) lsLeft lsTop lsRight lsBottom)
		kernel.Graph(12, local42, local43, local44, local45, local0)
	#end:method

	@classmethod
	def getDistToPt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp4 = 32767
		temp1 = (self first:)
		temp0 = (self last:)
		while 1:

			temp2 = kernel.NodeValue(temp1)
			if 
				(<
					temp3 = kernel.GetDistance(param1, param2, (temp2 x:), (temp2 y:))
					temp4
				)
				temp4 = temp3
				closestPt = temp2
			#endif
			(breakif (temp1 == temp0))
			temp1 = (self next: temp1)
		#end:loop
		return temp4
	#end:method

	@classmethod
	def getDistToLine(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (size < 2):
			return (self getDistToPt: param1 param2 &rest)
		#endif
		temp4 = 32767
		temp1 = (self first:)
		temp0 = (self last:)
		while 1:

			temp2 = kernel.NodeValue(temp1)
			temp6 = (self next: temp1)
			temp5 = kernel.NodeValue(temp6)
			if 
				(<
					(= temp3
						(localproc_2
							(temp2 x:)
							(temp2 y:)
							(temp5 x:)
							(temp5 y:)
							param1
							param2
						)
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
	def insertPt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = ((Class_943_1 new:) x: param1 y: param2 yourself:)
		(self addAfter: closestPt temp0)
		(self setCur: kernel.FindKey(elements, temp0))
	#end:method

	@classmethod
	def eachLineDo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (self first:)
		temp4 = (self last:)
		while ((temp0 != temp4) or closed):

			temp1 = (self next: temp0)
			temp2 = kernel.NodeValue(temp0)
			temp3 = kernel.NodeValue(temp1)
			(temp2 param1: temp3 &rest)
			(breakif (temp0 == temp4))
			temp0 = temp1
		#end:loop
	#end:method

	@classmethod
	def deletePt():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (curNode == temp0 = (self prev: curNode)):
			temp0 = 0
		#endif
		(self delete: curPt)
		(curPt dispose:)
		(self setCur: temp0)
	#end:method

	@classmethod
	def next(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (super next: param1)
		if (closed and (not temp0)):
			return (super first:)
		#endif
		return temp0
	#end:method

	@classmethod
	def prev(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (super prev: param1)
		if (closed and (not temp0)):
			return (super last:)
		#endif
		return temp0
	#end:method

	@classmethod
	def saveForUndo():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = temp0 = kernel.Memory(2, (2 * ((2 * size) + 3)))
		kernel.Memory(6, temp1, closed)
		(temp1 += 2)
		kernel.Memory(6, temp1, size)
		(temp1 += 2)
		kernel.Memory(6, temp1, (self indexOf: curPt))
		(temp1 += 2)
		temp2 = (self first:)
		while temp2:

			temp3 = kernel.NodeValue(temp2)
			kernel.Memory(6, temp1, (temp3 x:))
			kernel.Memory(6, (temp1 += 2), (temp3 y:))
			temp2 = kernel.NextNode(temp2)
			(temp1 += 2)
		#end:loop
		return temp0
	#end:method

	@classmethod
	def undo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #dispose release:)
		closed = kernel.Memory(5, param1)
		(param1 += 2)
		temp1 = kernel.Memory(5, param1)
		(param1 += 2)
		temp3 = kernel.Memory(5, param1)
		(param1 += 2)
		temp2 = 0
		while (temp2 < temp1):

			(self add: kernel.Memory(5, param1) kernel.Memory(5, (param1 += 2)) 0)
			temp2.post('++')
			(param1 += 2)
		#end:loop
		(self setCur: kernel.FindKey(elements, (self at: temp3)) 0)
	#end:method

#end:class or instance

@SCI.instance
class readObstacle(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp2 = (PolyEdit add:)
		temp0 = 0
		temp1 = (param1 points:)
		while (temp0 < (param1 size:)): # inline for
			(temp2
				add: kernel.Memory(5, temp1) kernel.Memory(5, (temp1 + 2)) 0
				type: (param1 type:)
				srcList: param2
			)
			temp0.post('++')
			# for:reinit
			(temp1 += 4)
		#end:loop
		(temp2 closed: 1)
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
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = x
		temp2 = y
		x = (param1 x:)
		y = (param1 y:)
		match (param1 type:)
			case 0:
				if curPolygon:
					if 
						(and
							isMouseDown
							(not proc999_5(state, 0, 2))
							((kernel.Abs((temp1 - x)) + kernel.Abs((temp2 - y))) > 1)
						)
						if (state != 3):
							(self saveForUndo:)
						#endif
						(self changeState: 2)
					#endif
					if 
						(and
							proc999_5(state, 2, 0)
							((temp1 != x) or (temp2 != y))
						)
						(self movePt: x y)
					#endif
					if (state == 2):
						kernel.DrawStatus(kernel.Format(@temp3, 943, 2, x, y))
					#endif
				#endif
			#end:case
			case 1:
				temp0 = (param1 modifiers:)
				isMouseDown = 1
				(cond
					case (temp0 & 0x0004):
						if (state == 0):
							(self finishAdding:)
							isMouseDown = 0
						else:
							(self insertPt:)
						#endif
					#end:case
					case (temp0 & 0x0003):
						if (state != 0):
							(self deletePt:)
						#endif
						isMouseDown = 0
					#end:case
					case (state == 0):
						(self addPt:)
					#end:case
					else:
						(self selectPt:)
					#end:else
				)
			#end:case
			case 2:
				isMouseDown = 0
				if proc999_5(state, 2, 3):
					(self changeState: 1)
				#endif
			#end:case
			case 4:
				match (param1 message:)
					case 63:
						(param1 message: 104)
					#end:case
					case 19:
						(param1 message: 120)
					#end:case
					case 15360:
						(param1 message: 12032)
					#end:case
					case 15872:
						(param1 message: 11776)
					#end:case
				#end:match
				match (param1 message:)
					case 9:
						if ((state == 1) and curPolygon):
							(self advanceRetreat: 65 126)
						#endif
					#end:case
					case 3840:
						if ((state == 1) and curPolygon):
							(self advanceRetreat: 130 129)
						#endif
					#end:case
					case 32:
						if ((state == 1) and curPolygon):
							(curPolygon advance:)
						#endif
					#end:case
					case 8:
						if ((state == 1) and curPolygon):
							(curPolygon retreat:)
						#endif
					#end:case
					case 99:
						if (state == 1):
							(self changeState: 0)
							curPolygon = 0
						#endif
					#end:case
					case 116:
						if (curPolygon and (state == 1)):
							(curPolygon getAccessType:)
						#endif
					#end:case
					case 100:
						(cond
							case (state == 1):
								if curPolygon:
									(self deletePt:)
								#endif
							#end:case
							case (state == 0):
								(self finishAdding:)
							#end:case
						)
					#end:case
					case 104:
						match state
							case 0:
								(localproc_3
									r"""___________CREATING POLYGON\0d\n\0d\nClick to create each corner of the polygon, then choose Done from the menu to finish.__You can also press Esc or Ctrl-click to finish.\0d\n\0d\nTo UNDO a corner, choose Undo.\0d\n\0d\nTo change MAP displayed (visual or control), choose Map.\0d\n\0d\nTo EXIT the Polygon Editor, choose eXit or press Ctrl-S."""
									0
								)
							#end:case
							case 1:
								(localproc_3
									r"""_____________EDITING POLYGON\0d\n\0d\nTo MOVE a corner, click on it and drag it to the new position.\0d\nTo INSERT a new corner, Ctrl-click to create it, then drag it to the correct position.\0d\nTo DELETE a corner, Shift-click on it.\0d\nTo UNDO an action, choose Undo from the menu.\0d\nTo CREATE a new polygon, choose Create.\0d\nTo change a polygon's TYPE (Total, Near or Barred), choose Type.\0d\nTo change MAP displayed (visual or control), choose Map.\0d\nTo EXIT the Polygon Editor, choose eXit or press Ctrl-S.\0d\n\0d\nIn addition to using the mouse, you can use Space and BackSpace to select corners and Tab and BackTab to select polygons. """
									0
								)
							#end:case
						#end:match
					#end:case
					case 117:
						(self undo:)
					#end:case
					case 109:
						(self showMap: -1)
					#end:case
					case 12032:
						(self showMap: 1)
					#end:case
					case 11776:
						(self showMap: 4)
					#end:case
					case 97:
						(localproc_3
							r""" by\0d\n\0d\nMark Wilden\0d\n\0d\nOriginal program by Chad Bye """
							1
						)
					#end:case
					case 114:
						if (state == 1):
							(self draw:)
						#endif
					#end:case
					case 120:
						(self exit:)
						return
					#end:case
					case 27:
						if (state == 0):
							(self finishAdding:)
						#endif
					#end:case
				#end:match
			#end:case
		#end:match
		return 0
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
				case 0: addMenu#end:case
				case 1: editMenu#end:case
				case 2: 0#end:case
				else: 0#end:else
			#end:match
		)
		if curMenu:
			(curMenu init:)
		#endif
	#end:method

	@classmethod
	def readObstacles():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global2 obstacles:):
			((global2 obstacles:) eachElementDo: #perform readObstacle 0)
		#endif
		if global95:
			(global95 eachElementDo: #perform readObstacle 1)
		#endif
	#end:method

	@classmethod
	def writeObstacles():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global2 obstacles:):
			((global2 obstacles:) eachElementDo: #dispose release:)
		#endif
		(self eachElementDo: #writeObstacle)
	#end:method

	@classmethod
	def add():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super add: curPolygon = (_EditablePolygon new:))
		return curPolygon
	#end:method

	@classmethod
	def draw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #restore)
		(self eachElementDo: #save)
		(self eachElementDo: #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def selectPt():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self select: 486 1)
		temp0 = (Event new:)
		kernel.GlobalToLocal(temp0)
		x = (temp0 x:)
		y = (temp0 y:)
		(temp0 dispose:)
	#end:method

	@classmethod
	def addPt():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self saveForUndo:)
		if (not curPolygon):
			(self add:)
			(curPolygon add: x y 0)
		#endif
		(curPolygon add: x y)
	#end:method

	@classmethod
	def finishAdding():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case curPolygon:
				(curPolygon closed: 1)
				if ((curPolygon size:) > 1):
					(curPolygon deletePt: (curPolygon last:) advance:)
				#endif
				(self draw:)
				(curPolygon getAccessType:)
			#end:case
			case (not temp0 = (self first:)):
				curPolygon = 0
			#end:case
			else:
				curPolygon = kernel.NodeValue(temp0)
				(self draw:)
			#end:else
		)
		if curPolygon:
			(self changeState: 1)
		#endif
	#end:method

	@classmethod
	def movePt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(curPolygon startRedraw:)
		(self eachElementDo: #restore)
		(curPolygon movePt: param1 param2)
		(self eachElementDo: #save)
		(self eachElementDo: #draw)
		(curPolygon endRedraw:)
	#end:method

	@classmethod
	def insertPt():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #restore)
		(self select: 485 0)
		(self saveForUndo:)
		(curPolygon insertPt: x y)
		(self changeState: 3)
		(self eachElementDo: #save)
		(self eachElementDo: #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = curPolygon
		(self advanceRetreat: 130 65)
		if (curPolygon == temp0):
			curPolygon = 0
		#endif
		(super delete: temp0 &rest)
		(temp0 dispose:)
	#end:method

	@classmethod
	def deletePt():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #restore)
		(self select: 486 0)
		(self saveForUndo:)
		(curPolygon deletePt:)
		if (not (curPolygon size:)):
			(self delete: curPolygon)
			if (not size):
				(self changeState: 0)
			#endif
		#endif
		(self eachElementDo: #save)
		(self eachElementDo: #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
	#end:method

	@classmethod
	def select(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 32767
		temp1 = 0
		temp4 = kernel.FirstNode(elements)
		while temp4: # inline for
			temp3 = kernel.NodeValue(temp4)
			if (temp2 = (temp3 param1: x y) < temp0):
				temp0 = temp2
				temp1 = temp3
			#endif
			# for:reinit
			temp4 = kernel.NextNode(temp4)
		#end:loop
		(curPolygon = temp1 setCurClosest: param2)
	#end:method

	@classmethod
	def advanceRetreat(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = kernel.FindKey(elements, curPolygon)
		if 
			(and
				(not temp0 = (self param1: temp1))
				(not temp0 = (self param2: temp1))
			)
			temp0 = temp1
		#endif
		curPolygon = kernel.NodeValue(temp0)
		(curPolygon setCur: (curPolygon curNode:))
	#end:method

	@classmethod
	def saveForUndo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if undoPoly = curPolygon:
			undoPrvPoly = (self prev: undoPoly)
			if (((not argc) or param1) and undoPolyBuf):
				kernel.Memory(3, undoPolyBuf)
			#endif
			undoPolyBuf = (curPolygon saveForUndo:)
		#endif
		undoX = x
		undoY = y
		undoState = state
	#end:method

	@classmethod
	def undo():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
		(self saveForUndo: 0)
		(self eachElementDo: #restore)
		if curPolygon = temp1:
			if (not (self contains: curPolygon)):
				curPolygon = (self add:)
				if temp2:
					(self addAfter: temp2 curPolygon)
				else:
					(self addToFront: curPolygon)
				#endif
			#endif
			(curPolygon undo: temp3)
		else:
			curPolygon = (self add:)
		#endif
		kernel.Memory(3, temp3)
		x = temp4
		y = temp5
		(self changeState: temp6)
		(self eachElementDo: #save)
		(self eachElementDo: #draw)
		kernel.Graph(12, 0, 0, 190, 320, local0)
		(global1 setCursor: 999 1 x y)
	#end:method

	@classmethod
	def showMap(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == -1):
			if (local0 == 1):
				param1 = 4
			else:
				param1 = 1
			#endif
		#endif
		if (local0 != param1):
			(self eachElementDo: #restore)
			local0 = param1
			(self eachElementDo: #save)
			(self eachElementDo: #draw)
			kernel.Graph(12, 0, 0, 190, 320, local0)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.DrawPic((global2 curPic:), 100, 1)
		if (global36 != -1):
			kernel.DrawPic(global36, 100, 0)
		#endif
		(global10 doit:)
		(global5 eachElementDo: #stopUpd)
		kernel.Animate((global5 elements:), 0)
		local1 = global38
		global38 = SysWindow
		local0 = 1
		(global1 setCursor: 999 1)
		(self readObstacles:)
		(self changeState: (1 if size else 0))
		(self draw:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self init:)
		while True: #repeat
			temp0 = (Event new:)
			if (not (curMenu and (curMenu handleEvent: temp0))):
				kernel.GlobalToLocal(temp0)
				(breakif (self handleEvent: temp0))
			#endif
			(temp0 dispose:)
		#end:loop
		(temp0 dispose:)
		(self dispose:)
	#end:method

	@classmethod
	def exit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (state == 0):
			(self finishAdding:)
		#endif
		(self showMap: 1)
		if (not curPolygon):
			return 1
		#endif
		(self eachElementDo: #check)
		if (not local2):
			kernel.Format(@local2, 943, 3, (global2 curPic:))
		#endif
		if 
			(not
				(= temp100
					(Print
						addTitle: r"""Save Polygons"""
						addText: r"""File:"""
						addEdit: @local2 25 50 0 @local2
						addButton: 1 r""" Save """ 5 12
						addButton: 2 r"""Abandon""" 70 12
						addButton: 0 r"""Cancel""" 150 12
						init:
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
						(Print
							width: 210
							addText: @temp0
							addButton: 1 r"""Replace""" 5 12
							addButton: 2 r"""Append""" 85 12
							addButton: 0 r"""Cancel""" 150 12
							init:
						)
					)
				)
				return 0
			#endif
		#endif
		temp102 = (2 if (temp100 == 1) else 0)
		if (not (temp101 = (File new:) name: @local2 open: temp102)):
			kernel.Format(@temp0, 943, 5, (temp101 name:))
			proc921_0(@temp0)
			(temp101 dispose:)
			return 0
		#endif
		(temp101 writeString: kernel.Format(@temp0, 943, 6, r"""Polygon Editor 1.11"""))
		(temp101
			writeString:
				kernel.Format(@temp0, 943, 7, r"""Dynamic Obstacles""", (global2 curPic:))
		)
		(temp101 writeString: r"""\t\t(curRoom addObstacle:\0d\n""")
		(self eachElementDo: #writeFile temp101 0)
		(temp101 writeString: r"""\t\t)\0d\n\0d\n""")
		(temp101 writeString: r"""\t\t(altPolyList add:\0d\n""")
		(self eachElementDo: #writeFile temp101 1)
		(temp101 writeString: r"""\t\t)\0d\n""")
		(temp101 dispose:)
		return 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self writeObstacles:)
		if curMenu:
			(curMenu dispose:)
			curMenu = 0
		#endif
		if undoPolyBuf:
			kernel.Memory(3, undoPolyBuf)
			undoPolyBuf = 0
		#endif
		kernel.DrawStatus(r""" """, 0, 0)
		kernel.DrawStatus(0)
		(global5 eachElementDo: #startUpd)
		kernel.Animate((global5 elements:), 0)
		(self eachElementDo: #draw)
		if 
			(Print
				addText: r"""Erase polygon outlines?"""
				addButton: 1 r"""Yes """ 30 12
				addButton: 0 r""" No """ 85 12
				init:
			)
			kernel.DrawPic((global2 curPic:), 100, 1)
			if (global36 != -1):
				kernel.DrawPic(global36, 100, 0)
			#endif
			(global10 doit:)
		#endif
		global38 = local1
		kernel.DisposeScript(993)
		(super dispose:)
		kernel.DisposeScript(943)
	#end:method

#end:class or instance

