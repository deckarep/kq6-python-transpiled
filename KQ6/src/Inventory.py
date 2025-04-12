#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 995
import sci_sh
import kernel
import Main
import Print
import IconBar
import Tutorial
import Window
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


class InvI(IconI):
	#property vars (may be empty)
	view = 0
	loop = 0
	cel = 0
	nsTop = 0
	cursor = 999
	message = 0
	signal = 0
	modNum = -1
	owner = 0
	script = 0
	value = 0
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return ((super onMe: param1) and (not (signal & 0x0004)))
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (modNum == -1):
			modNum = global11
		#endif
		if (global90 and kernel.Message(0, modNum, noun, param1, 0, 1)):
			(global91 say: noun param1 0 0 0 modNum)
		#endif
		if (temp0 = (global1 script:) and (temp0 isKindOf: Tutorial)):
			(cond
				case ((temp0 nextItem:) != self):
					(temp0 report: self)
				#end:case
				case ((temp0 nextAction:) != param1):
					(temp0 report: param1)
				#end:case
				else:
					(temp0 cue:)
				#end:else
			)
		#endif
	#end:method

	@classmethod
	def highlight(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (highlightColor == -1):
			return
		#endif
		temp4 = (highlightColor if (argc and param1) else lowlightColor)
		temp0 = (nsTop - 2)
		temp1 = (nsLeft - 2)
		temp2 = (nsBottom + 1)
		temp3 = (nsRight + 1)
		kernel.Graph(4, temp0, temp1, temp0, temp3, temp4, -1, -1)
		kernel.Graph(4, temp0, temp3, temp2, temp3, temp4, -1, -1)
		kernel.Graph(4, temp2, temp3, temp2, temp1, temp4, -1, -1)
		kernel.Graph(4, temp2, temp1, temp0, temp1, temp4, -1, -1)
		kernel.Graph(12, (nsTop - 2), (nsLeft - 2), (nsBottom + 2), (nsRight + 2), 1)
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1)
	#end:method

	@classmethod
	def ownedBy(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return (owner == param1)
	#end:method

	@classmethod
	def moveTo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		owner = param1
		if (value and (param1 == global0)):
			(global1 changeScore: value)
			value = 0
		#endif
		return self
	#end:method

#end:class or instance

class Inv(IconBar):
	#property vars (may be empty)
	normalHeading = r"""You are carrying:"""
	heading = 0
	empty = r"""nothing!"""
	iconBarInvItem = 0
	okButton = 0
	selectIcon = 0
	
	@classmethod
	def drawInvWindow(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		global170 = 0
		temp0 = temp1 = temp2 = temp3 = temp4 = temp5 = 0
		temp8 = (self first:)
		while temp8: # inline for
			if (temp9 = kernel.NodeValue(temp8) isKindOf: InvI):
				if (temp9 ownedBy: param1):
					(temp9 signal: ((temp9 signal:) & 0xfffb))
					temp0.post('++')
					if 
						(>
							(= temp6
								kernel.CelWide((temp9 view:), (temp9 loop:), (temp9
									cel:
								))
							)
							temp2
						)
						temp2 = temp6
					#endif
					if 
						(>
							(= temp7
								kernel.CelHigh((temp9 view:), (temp9 loop:), (temp9
									cel:
								))
							)
							temp1
						)
						temp1 = temp7
					#endif
				else:
					(temp9 signal: (| (temp9 signal:) 0x0004))
				#endif
			else:
				temp3.post('++')
				(temp5 += kernel.CelWide((temp9 view:), (temp9 loop:), (temp9 cel:)))
				if 
					(>
						(= temp7
							kernel.CelHigh((temp9 view:), (temp9 loop:), (temp9 cel:))
						)
						temp4
					)
					temp4 = temp7
				#endif
			#endif
			# for:reinit
			temp8 = (self next: temp8)
		#end:loop
		if (not temp0):
			(Print addTextF: r"""%s %s""" normalHeading empty init:)
			return 0
		#endif
		if ((temp16 = kernel.Sqrt(temp0) * temp16) > temp0):
			temp16.post('--')
		#endif
		if (temp16 > 3):
			temp16 = 3
		#endif
		local0 = (temp0 / temp16)
		if ((temp16 * local0) < temp0):
			local0.post('++')
		#endif
		temp10 = proc999_3((4 + temp5), (local0 * (4 + temp2)))
		temp11 = (temp16 * (4 + temp1))
		temp12 = ((190 - temp11) / 2)
		temp13 = ((320 - temp10) / 2)
		temp14 = (temp12 + temp11)
		temp15 = (temp13 + temp10)
		if temp21 = (self window:):
			(temp21 top: temp12 left: temp13 right: temp15 bottom: temp14 open:)
		#endif
		temp20 = local0
		if temp0:
			(= temp18
				(+
					2
					if (temp21 respondsTo: #yOffset):
						(temp21 yOffset:)
					#endif
				)
			)
			(= temp19
				(= temp17
					(+
						4
						if (temp21 respondsTo: #xOffset):
							(temp21 xOffset:)
						#endif
					)
				)
			)
			temp8 = (self first:)
			while temp8: # inline for
				if 
					(and
						(not ((temp9 = kernel.NodeValue(temp8) signal:) & 0x0004))
						(temp9 isKindOf: InvI)
					)
					if (not ((temp9 signal:) & 0x0080)):
						(temp9
							nsLeft:
								(+
									temp17
									(/
										(-
											temp2
											(= temp6
												kernel.CelWide((temp9 view:), (temp9
													loop:
												), (temp9 cel:))
											)
										)
										2
									)
								)
							nsTop:
								(+
									temp18
									(/
										(-
											temp1
											(= temp7
												kernel.CelHigh((temp9 view:), (temp9
													loop:
												), (temp9 cel:))
											)
										)
										2
									)
								)
						)
						(temp9
							nsRight: ((temp9 nsLeft:) + temp6)
							nsBottom: ((temp9 nsTop:) + temp7)
						)
						if temp20.post('--'):
							(temp17 += temp2)
						else:
							temp20 = local0
							(temp18 += temp1)
							temp17 = temp19
						#endif
					else:
						temp17 = (temp9 nsLeft:)
						temp18 = (temp9 nsTop:)
					#endif
					(temp9 show:)
					if (temp9 == param2):
						(temp9 highlight:)
					#endif
				#endif
				# for:reinit
				temp8 = (self next: temp8)
			#end:loop
		#endif
		temp17 = ((((temp21 right:) - (temp21 left:)) - temp5) / 2)
		temp11 = ((temp21 bottom:) - (temp21 top:))
		temp18 = 32767
		temp8 = (self first:)
		while temp8: # inline for
			if (not (temp9 = kernel.NodeValue(temp8) isKindOf: InvI)):
				(temp9 nsTop: 0)
				temp6 = kernel.CelWide((temp9 view:), (temp9 loop:), (temp9 cel:))
				temp7 = kernel.CelHigh((temp9 view:), (temp9 loop:), (temp9 cel:))
				if (not ((temp9 signal:) & 0x0080)):
					if (temp18 == 32767):
						temp18 = (temp11 - temp7)
					#endif
					(temp9
						nsLeft: temp17
						nsTop: temp18
						nsBottom: temp11
						nsRight: (temp17 + temp6)
					)
				#endif
				temp17 = ((temp9 nsLeft:) + temp6)
				temp18 = (temp9 nsTop:)
				(temp9 signal: ((temp9 signal:) & 0xfffb) show:)
			#endif
			# for:reinit
			temp8 = (self next: temp8)
		#end:loop
		return 1
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		heading = normalHeading
	#end:method

	@classmethod
	def ownedBy(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self firstTrue: #ownedBy param1)
	#end:method

	@classmethod
	def showSelf(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global8 pause:)
		if (global77 and (global77 respondsTo: #stop)):
			(global77 stop:)
		#endif
		if (global69 height:):
			(global69 hide:)
		#endif
		if (not window):
			window = (SysWindow new:)
		#endif
		if (window window:):
			(window dispose:)
			window = 0
		#endif
		if (not okButton):
			okButton = kernel.NodeValue((self first:))
		#endif
		curIcon = 0
		if (self show: (param1 if argc else global0)):
			(self doit:)
		#endif
	#end:method

	@classmethod
	def show(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1
			setCursor:
				if curIcon:
					(curIcon cursor:)
				else:
					(selectIcon cursor:)
				#endif
		)
		temp0 = kernel.PicNotValid()
		kernel.PicNotValid(0)
		(state |= 0x0020)
		if 
			(not
				(= temp1
					(self
						drawInvWindow:
							(param1 if argc else global0)
							(global69 curIcon:)
					)
				)
			)
			(state &= 0xffdf)
		#endif
		kernel.PicNotValid(temp0)
		return temp1
	#end:method

	@classmethod
	def advance(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (param1 if argc else 1)
		temp2 = (self indexOf: highlightedIcon)
		temp3 = (temp1 + temp2)
		while True: #repeat
			(= temp0
				(self
					at:
						if (temp3 <= size):
							temp3
						else:
							(mod temp3 (size - 1))
						#endif
				)
			)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue((self first:))
			#endif
			if (not ((temp0 signal:) & 0x0004)):
				(break)
			else:
				temp3.post('++')
			#endif
		#end:loop
		(self highlight: temp0 1)
	#end:method

	@classmethod
	def retreat(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (param1 if argc else 1)
		temp3 = (temp2 = (self indexOf: highlightedIcon) - temp1)
		while True: #repeat
			temp0 = (self at: temp3)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue((self last:))
			#endif
			if (not ((temp0 signal:) & 0x0004)):
				(break)
			else:
				temp3.post('--')
			#endif
		#end:loop
		(self highlight: temp0 1)
	#end:method

	(procedure (localproc_0param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp2
			((((param1 nsRight:) - (param1 nsLeft:)) / 2) + (param1 nsLeft:))
		)
		temp1 = param2
		while (kernel.Abs((temp1 - param3)) >= 4):

			if 
				(= temp0
					(self
						firstTrue:
							#onMe
							(((global80 curEvent:) new:)
								x: temp2
								y: temp1
								yourself:
							)
					)
				)
				return
			#endif
			if (param2 < param3):
				(temp1 += 4)
			else:
				(temp1 -= 4)
			#endif
		#end:loop
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		while (temp1 = ((global80 curEvent:) new:) type:):

		#end:loop
		while (state & 0x0020):

			temp1 = ((global80 curEvent:) new:)
			global70 = (temp1 x:)
			global71 = (temp1 y:)
			temp2 = (temp1 type:)
			temp3 = (temp1 message:)
			temp4 = (temp1 modifiers:)
			temp9 = 0
			(temp1 localize:)
			if 
				(and
					curIcon
					(not temp4)
					(curIcon != selectIcon)
					(or
						(temp2 == 1)
						(and (temp2 == 4) (temp3 == 13) temp9 = 1)
						((temp2 == 256) and temp9 = 1)
					)
					(or
						(curIcon != helpIconItem)
						((helpIconItem signal:) & 0x0010)
					)
				)
				(temp1 type: 16384 message: (curIcon message:))
			#endif
			kernel.MapKeyToDir(temp1)
			temp2 = (temp1 type:)
			temp3 = (temp1 message:)
			if global170:
				(temp1 claimed: 1)
				global170 = 0
				(break)
			#endif
			if global18:
				(global18 eachElementDo: #doit)
			#endif
			if (temp60 = (global1 script:) and (temp60 isKindOf: Tutorial)):
				(temp60 doit:)
			#endif
			if global84:
				(global84 eachElementDo: #doit)
				global88 = (global86 + kernel.GetTime())
				if global84:
					(global84 handleEvent: temp1)
				#endif
			else:
				if ((temp2 == 1) and temp4):
					(self advanceCurIcon:)
					(temp1 claimed: 1)
					(continue)
				#endif
				if 
					(and
						(temp2 == 0)
						temp0 = (self firstTrue: #onMe temp1)
						(temp0 != highlightedIcon)
					)
					(self highlight: temp0)
					(continue)
				#endif
				(cond
					case 
						(or
							(temp2 == 1)
							((temp2 == 4) and (temp3 == 13))
							(temp2 == 256)
						):
						if 
							(and
								kernel.IsObject(highlightedIcon)
								(self select: highlightedIcon (temp2 == 1))
							)
							if (highlightedIcon == okButton):
								(temp1 claimed: 1)
								(break)
							#endif
							if (highlightedIcon == helpIconItem):
								if ((highlightedIcon cursor:) != -1):
									(global1 setCursor: (helpIconItem cursor:))
								#endif
								if (state & 0x0800):
									(self noClickHelp:)
									(continue)
								#endif
								if helpIconItem:
									(helpIconItem
										signal: (| (helpIconItem signal:) 0x0010)
									)
								#endif
								(continue)
							#endif
							curIcon = highlightedIcon
							(global1 setCursor: (curIcon cursor:))
						#endif
					#end:case
					case (temp2 & 0x0040):
						match temp3
							case 3:
								(self advance:)
							#end:case
							case 7:
								(self retreat:)
							#end:case
							case 1:
								if 
									(and
										highlightedIcon
										(= temp0
											localproc_0(highlightedIcon, (-
												(highlightedIcon nsTop:)
												1
											), 0)
										)
									)
									(self highlight: temp0 1)
								else:
									(self retreat:)
								#endif
							#end:case
							case 5:
								if 
									(and
										highlightedIcon
										(= temp0
											localproc_0(highlightedIcon, (+
												(highlightedIcon nsBottom:)
												1
											), (window bottom:))
										)
									)
									(self highlight: temp0 1)
								else:
									(self advance:)
								#endif
							#end:case
							case 0:
								if (temp2 & 0x0004):
									(self advanceCurIcon:)
								#endif
							#end:case
						#end:match
					#end:case
					case (temp2 == 4):
						match temp3
							case 9:
								(self advance:)
							#end:case
							case 3840:
								(self retreat:)
							#end:case
							case 27:
								(break)
							#end:case
						#end:match
					#end:case
					case 
						(and
							(temp2 & 0x4000)
							temp0 = (self firstTrue: #onMe temp1)
						):
						if (temp2 & 0x2000):
							if 
								(and
									temp0
									(temp0 noun:)
									kernel.Message(0, (temp0 modNum:), (temp0
										noun:
									), (temp0 helpVerb:), 0, 1, @temp10)
								)
								if (global38 respondsTo: #eraseOnly):
									temp7 = (global38 eraseOnly:)
									(global38 eraseOnly: 1)
									proc921_0(@temp10)
									(global38 eraseOnly: temp7)
								else:
									proc921_0(@temp10)
								#endif
							#endif
							(helpIconItem
								signal: ((helpIconItem signal:) & 0xffef)
							)
							(global1 setCursor: 999)
							(continue)
						#endif
						if (temp0 == okButton):
							(temp1 claimed: 1)
							(break)
						#endif
						if (not (temp0 isKindOf: InvI)):
							if (self select: temp0 (not temp9)):
								curIcon = temp0
								(global1 setCursor: (curIcon cursor:))
								if (temp0 == helpIconItem):
									if (state & 0x0800):
										(self noClickHelp:)
										(continue)
									#endif
									(helpIconItem
										signal: (| (helpIconItem signal:) 0x0010)
									)
								#endif
							#endif
							(continue)
						#endif
						if curIcon:
							(temp1 claimed: 1)
							if (global38 respondsTo: #eraseOnly):
								temp7 = (global38 eraseOnly:)
								(global38 eraseOnly: 1)
							#endif
							if (curIcon isKindOf: InvI):
								(temp0 doVerb: (curIcon message:))
							else:
								(temp0 doVerb: (temp1 message:))
							#endif
							if (global38 respondsTo: #eraseOnly):
								(global38 eraseOnly: temp7)
							#endif
						#endif
					#end:case
				)
			#endif
		#end:loop
		(self hide:)
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (state & 0x0020):
			(global8 pause: 0)
			(state &= 0xffdf)
		#endif
		if window:
			(window dispose:)
		#endif
		if (kernel.IsObject(curIcon) and (curIcon isKindOf: InvI)):
			if (not (global69 curInvIcon:)):
				(global69 enable: (global69 useIconItem:))
			#endif
			(global69
				curIcon:
					((global69 useIconItem:)
						cursor: (curIcon cursor:)
						yourself:
					)
				curInvIcon: curIcon
			)
			if temp0 = ((global69 curIcon:) cursor:):
				(global1 setCursor: temp0)
			#endif
		#endif
	#end:method

#end:class or instance

