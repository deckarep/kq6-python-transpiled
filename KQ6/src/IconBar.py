#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 937
import sci_sh
import Main
import Print
import Tutorial
import System

class IconI(Obj):
	#property vars (may be empty)
	view = -1
	loop = -1
	cel = -1
	nsLeft = 0
	nsTop = -1
	nsRight = 0
	nsBottom = 0
	state = 0
	cursor = -1
	type = 16384
	message = -1
	modifiers = 0
	signal = 1
	maskView = 0
	maskLoop = 0
	maskCel = 0
	highlightColor = 0
	lowlightColor = 0
	noun = 0
	modNum = 0
	helpVerb = 0
	
	@classmethod
	def show(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(signal |= 0x0020)
		if argc:
			nsRight = (nsLeft = param1 + (CelWide view loop cel))
			nsBottom = (nsTop = param2 + (CelHigh view loop cel))
		else:
			nsRight = (nsLeft + (CelWide view loop cel))
			nsBottom = (nsTop + (CelHigh view loop cel))
		#endif
		(DrawCel view loop cel nsLeft nsTop -1)
		if (signal & 0x0004):
			(self mask:)
		#endif
		if (global77 and (global77 respondsTo: #stop)):
			(global77 stop:)
		#endif
	#end:method

	@classmethod
	def mask():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(DrawCel
			maskView
			maskLoop
			maskCel
			(+
				nsLeft
				(/
					(-
						(CelWide view loop cel)
						(CelWide maskView maskLoop maskCel)
					)
					2
				)
			)
			(+
				nsTop
				(/
					(-
						(CelHigh view loop cel)
						(CelHigh maskView maskLoop maskCel)
					)
					2
				)
			)
			-1
		)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				((param1 x:) >= nsLeft)
				((param1 y:) >= nsTop)
				((param1 x:) <= nsRight)
				((param1 y:) <= nsBottom)
			)
		)
	#end:method

	@classmethod
	def highlight(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((not (signal & 0x0020)) or (highlightColor == -1)):
			return
		#endif
		temp4 = (highlightColor if (argc and param1) else lowlightColor)
		temp0 = (nsTop + 2)
		temp1 = (nsLeft + 2)
		temp2 = (nsBottom - 3)
		temp3 = (nsRight - 4)
		(Graph 4 temp0 temp1 temp0 temp3 temp4 -1 -1)
		(Graph 4 temp0 temp3 temp2 temp3 temp4 -1 -1)
		(Graph 4 temp2 temp3 temp2 temp1 temp4 -1 -1)
		(Graph 4 temp2 temp1 temp0 temp1 temp4 -1 -1)
		(Graph 12 (nsTop - 2) (nsLeft - 2) nsBottom (nsRight + 3) 1)
	#end:method

	@classmethod
	def select(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(cond
				case (signal & 0x0004): 0#end:case
				case (and argc param1 (signal & 0x0001)):
					(DrawCel view loop temp1 = 1 nsLeft nsTop -1)
					(Graph 12 nsTop nsLeft nsBottom nsRight 1)
					while ((temp0 = (Event new:) type:) != 2):

						(temp0 localize:)
						(cond
							case (self onMe: temp0):
								if (not temp1):
									(DrawCel
										view
										loop
										temp1 = 1
										nsLeft
										nsTop
										-1
									)
									(Graph 12 nsTop nsLeft nsBottom nsRight 1)
								#endif
							#end:case
							case temp1:
								(DrawCel view loop temp1 = 0 nsLeft nsTop -1)
								(Graph 12 nsTop nsLeft nsBottom nsRight 1)
							#end:case
						)
						(temp0 dispose:)
					#end:loop
					(temp0 dispose:)
					if (temp1 == 1):
						(DrawCel view loop 0 nsLeft nsTop -1)
						(Graph 12 nsTop nsLeft nsBottom nsRight 1)
					#endif
					if 
						(and
							temp2 = (global1 script:)
							(temp2 isKindOf: Tutorial)
						)
						(cond
							case 
								(and
									((temp2 nextItem:) == self)
									(!=
										(temp2 nextAction:)
										((global69 helpIconItem:) message:)
									)
								):
								(temp2 cue:)
							#end:case
							case (not temp1):
								return 0
							#end:case
							else:
								(temp2 report:)
								return 0
							#end:else
						)
					#endif
					temp1
				#end:case
				else:
					if 
						(and
							temp2 = (global1 script:)
							(temp2 isKindOf: Tutorial)
						)
						if 
							(and
								((temp2 nextItem:) == self)
								(!=
									(temp2 nextAction:)
									((global69 helpIconItem:) message:)
								)
							)
							(temp2 cue:)
						else:
							(temp2 report:)
							return 0
						#endif
					#endif
					1
				#end:else
			)
		)
	#end:method

#end:class or instance

class IconBar(Set):
	#property vars (may be empty)
	height = 0
	underBits = 0
	oldMouseX = 0
	oldMouseY = 0
	curIcon = 0
	highlightedIcon = 0
	prevIcon = 0
	curInvIcon = 0
	useIconItem = 0
	helpIconItem = 0
	walkIconItem = 0
	port = 0
	window = 0
	state = 1024
	activateHeight = 0
	y = 0
	
	@classmethod
	def findIcon(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < size): # inline for
			temp1 = (self at: temp0)
			if ((temp1 message:) == param1):
				return temp1
			#endif
			# for:reinit
			temp0++
		#end:loop
		return 0
	#end:method

	@classmethod
	def noClickHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = temp2 = 0
		temp3 = (GetPort)
		temp4 = (global38 eraseOnly:)
		(global38 eraseOnly: 1)
		while (not (temp0 = ((global80 curEvent:) new:) type:)):

			if (not (self isMemberOf: IconBar)):
				(temp0 localize:)
			#endif
			(cond
				case temp2 = (self firstTrue: #onMe temp0):
					if ((temp2 != temp1) and (temp2 helpVerb:)):
						temp1 = temp2
						if global25:
							(global25 dispose:)
						#endif
						(Print
							font: global22
							width: 250
							addText:
								(temp2 noun:)
								(temp2 helpVerb:)
								0
								1
								0
								0
								(temp2 modNum:)
							modeless: 1
							init:
						)
						(SetPort temp3)
					#endif
				#end:case
				case global25:
					(global25 dispose:)
				#end:case
				else:
					temp1 = 0
				#end:else
			)
			(temp0 dispose:)
		#end:loop
		(global38 eraseOnly: temp4)
		(global1 setCursor: 999 1)
		if global25:
			(global25 dispose:)
		#endif
		(SetPort temp3)
		if (not (helpIconItem onMe: temp0)):
			(self dispatchEvent: temp0)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(param1 localize:)
		temp1 = (param1 type:)
		(cond
			case (state & 0x0004):#end:case
			case 
				(or
					(and
						(not temp1)
						(state & 0x0400)
						(<= -10 (param1 y:) height)
						(<= 0 (param1 x:) 320)
						(not temp0 = 0)
					)
					(and
						(temp1 == 4)
						(or
							((param1 message:) == 27)
							((param1 message:) == 21248)
						)
						temp0 = 1
					)
				):
				(param1 globalize:)
				oldMouseX = (param1 x:)
				oldMouseY = (param1 y:)
				temp4 = global19
				temp5 = curIcon
				temp6 = curInvIcon
				(self show:)
				(global1 setCursor: 999)
				if temp0:
					(global1
						setCursor:
							global19
							1
							(+
								(curIcon nsLeft:)
								(((curIcon nsRight:) - (curIcon nsLeft:)) / 2)
							)
							((curIcon nsBottom:) - 3)
					)
				#endif
				(self doit:)
				(= temp3
					if ((global80 canControl:) or (global80 canInput:)):
						(curIcon cursor:)
					else:
						global21
					#endif
				)
				if temp0:
					(global1 setCursor: temp3 1 oldMouseX oldMouseY)
				else:
					(global1
						setCursor:
							temp3
							1
							((param1 new:) x:)
							(proc999_3 (param1 y:) (1 + height))
					)
				#endif
				(self hide:)
			#end:case
			case (temp1 & 0x0004):
				match (param1 message:)
					case 13:
						(cond
							case (not (IsObject curIcon)):#end:case
							case ((curIcon != useIconItem) or curInvIcon):
								(param1
									type: (curIcon type:)
									message:
										if (curIcon == useIconItem):
											(curInvIcon message:)
										else:
											(curIcon message:)
										#endif
								)
							#end:case
							else:
								(param1 type: 0)
							#end:else
						)
					#end:case
					case 20992:
						if (global80 canControl:):
							(self swapCurIcon:)
						#endif
						(param1 claimed: 1)
					#end:case
					case 0:
						if ((param1 type:) & 0x0040):
							(self advanceCurIcon:)
							(param1 claimed: 1)
						#endif
					#end:case
				#end:match
			#end:case
			case (temp1 & 0x0001):
				(cond
					case ((param1 modifiers:) & 0x0003):
						(self advanceCurIcon:)
						(param1 claimed: 1)
					#end:case
					case ((param1 modifiers:) & 0x0004):
						if (global80 canControl:):
							(self swapCurIcon:)
						#endif
						(param1 claimed: 1)
					#end:case
					case (IsObject curIcon):
						(param1
							type: (curIcon type:)
							message:
								if (curIcon == useIconItem):
									(curInvIcon message:)
								else:
									(curIcon message:)
								#endif
						)
					#end:case
				)
			#end:case
		)
	#end:method

	@classmethod
	def disable(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			temp0 = 0
			while (temp0 < argc): # inline for
				(= temp1
					if (IsObject param1[temp0]):
						param1[temp0]
					else:
						(self at: param1[temp0])
					#endif
				)
				(temp1 signal: (| (temp1 signal:) 0x0004))
				(cond
					case (temp1 == curIcon):
						(self advanceCurIcon:)
					#end:case
					case (temp1 == highlightedIcon):
						(self advance:)
					#end:case
				)
				# for:reinit
				temp0++
			#end:loop
		else:
			(state |= 0x0004)
		#endif
	#end:method

	@classmethod
	def enable(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			temp0 = 0
			while (temp0 < argc): # inline for
				(= temp1
					if (IsObject param1[temp0]):
						param1[temp0]
					else:
						(self at: param1[temp0])
					#endif
				)
				(temp1 signal: ((temp1 signal:) & 0xfffb))
				# for:reinit
				temp0++
			#end:loop
		else:
			(state &= 0xfffb)
		#endif
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global8 pause:)
		(state |= 0x0020)
		(global1 setCursor: 999 1)
		(= height
			(CelHigh (temp0 = (self at: 0) view:) (temp0 loop:) (temp0 cel:))
		)
		port = (GetPort)
		(SetPort -1)
		underBits = (Graph 7 y 0 (y + height) 320 1)
		temp1 = (PicNotValid)
		(PicNotValid 1)
		temp3 = 0
		temp4 = y
		temp5 = (FirstNode elements)
		while temp5: # inline for
			temp6 = (NextNode temp5)
			if (not (IsObject temp7 = (NodeValue temp5))):
				return
			#endif
			if ((temp7 nsRight:) <= 0):
				(temp7 show: temp3 temp4)
				temp3 = (temp7 nsRight:)
			else:
				(temp7 show:)
			#endif
			# for:reinit
			temp5 = temp6
		#end:loop
		if curInvIcon:
			if (global0 has: (global9 indexOf: curInvIcon)):
				(= temp3
					(+
						(/
							(-
								((useIconItem nsRight:) - (useIconItem nsLeft:))
								(CelWide
									(curInvIcon view:)
									(curInvIcon loop:)
									(curInvIcon cel:)
								)
							)
							2
						)
						(useIconItem nsLeft:)
					)
				)
				(= temp4
					(+
						y
						(/
							(-
								((useIconItem nsBottom:) - (useIconItem nsTop:))
								(CelHigh
									(curInvIcon view:)
									(curInvIcon loop:)
									(curInvIcon cel:)
								)
							)
							2
						)
						(useIconItem nsTop:)
					)
				)
				(DrawCel
					(curInvIcon view:)
					(curInvIcon loop:)
					(curInvIcon cel:)
					temp3
					temp4
					-1
				)
				if ((useIconItem signal:) & 0x0004):
					(useIconItem mask:)
				#endif
			else:
				curInvIcon = 0
			#endif
		#endif
		(PicNotValid temp1)
		(Graph 12 y 0 (y + height) 320 1)
		(self highlight: curIcon)
	#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (state & 0x0020):
			(global8 pause: 0)
			(state &= 0xffdf)
			temp0 = (FirstNode elements)
			while temp0: # inline for
				temp1 = (NextNode temp0)
				if (not (IsObject temp2 = (NodeValue temp0))):
					return
				#endif
				(temp2 = (NodeValue temp0) signal: ((temp2 signal:) & 0xffdf))
				# for:reinit
				temp0 = temp1
			#end:loop
			if 
				(and
					(not (state & 0x0800))
					(IsObject helpIconItem)
					((helpIconItem signal:) & 0x0010)
				)
				(helpIconItem signal: ((helpIconItem signal:) & 0xffef))
			#endif
			(Graph 8 underBits)
			(Graph 12 y 0 (y + height) 320 1)
			(Graph 13 y 0 (y + height) 320)
			(SetPort port)
			height = activateHeight
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		while ((state & 0x0020) and temp0 = ((global80 curEvent:) new:)):

			temp1 = (temp0 type:)
			temp2 = (temp0 message:)
			temp3 = (temp0 modifiers:)
			(Wait 1)
			global88 = (global86 + (GetTime))
			if global18:
				(global18 eachElementDo: #doit)
			#endif
			if (temp4 = (global1 script:) and (temp4 isKindOf: Tutorial)):
				(temp4 doit:)
			#endif
			if (temp1 == 256):
				temp1 = 4
				temp2 = (27 if (temp3 & 0x0003) else 13)
				temp3 = 0
				(temp0 type: temp1 message: temp2 modifiers: 0)
			#endif
			(temp0 localize:)
			if 
				(and
					((temp1 == 1) or ((temp1 == 4) and (temp2 == 13)))
					(IsObject helpIconItem)
					((helpIconItem signal:) & 0x0010)
				)
				(temp0 type: 24576 message: (helpIconItem message:))
			#endif
			(MapKeyToDir temp0)
			(breakif (self dispatchEvent: temp0))
		#end:loop
	#end:method

	@classmethod
	def dispatchEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (param1 x:)
		temp0 = (param1 y:)
		temp2 = (param1 type:)
		temp3 = (param1 message:)
		temp5 = (param1 claimed:)
		if temp4 = (self firstTrue: #onMe param1):
			temp57 = (temp4 cursor:)
			temp58 = (temp4 signal:)
			temp59 = (temp4 == helpIconItem)
		#endif
		if (temp2 & 0x0040):
			match temp3
				case 3:
					(self advance:)
				#end:case
				case 7:
					(self retreat:)
				#end:case
			#end:match
		else:
			match temp2
				case 0:
					(cond
						case 
							(not
								((<= 0 temp0 (y + height)) and (<= 0 temp1 320))
							):
							if 
								(and
									(state & 0x0400)
									(or
										(not (IsObject helpIconItem))
										(not ((helpIconItem signal:) & 0x0010))
									)
								)
								oldMouseY = 0
								temp5 = 1
							#endif
						#end:case
						case (temp4 and (temp4 != highlightedIcon)):
							oldMouseY = 0
							(self highlight: temp4)
						#end:case
					)
				#end:case
				case 1:
					if (temp4 and (self select: temp4 1)):
						if temp59:
							if temp57:
								(global1 setCursor: temp57)
							#endif
							if (state & 0x0800):
								(self noClickHelp:)
							else:
								(helpIconItem
									signal: (| (helpIconItem signal:) 0x0010)
								)
							#endif
						else:
							temp5 = (temp58 & 0x0040)
						#endif
						(temp4 doit:)
					#endif
				#end:case
				case 4:
					match temp3
						case 27:
							temp5 = 1
						#end:case
						case 21248:
							temp5 = 1
						#end:case
						case 13:
							if (not temp4):
								temp4 = highlightedIcon
							#endif
							(cond
								case (temp4 and (temp4 == helpIconItem)):
									if (temp57 != -1):
										(global1 setCursor: temp57)
									#endif
									if helpIconItem:
										(helpIconItem
											signal:
												(| (helpIconItem signal:) 0x0010)
										)
									#endif
								#end:case
								case ((IsObject temp4) and (self select: temp4)):
									(temp4 doit:)
									temp5 = (temp58 & 0x0040)
								#end:case
							)
						#end:case
						case 3840:
							(self retreat:)
						#end:case
						case 9:
							(self advance:)
						#end:case
					#end:match
				#end:case
				case 24576:
					if (temp4 and (temp4 helpVerb:)):
						if (not (HaveMouse)):
							temp60 = (global1 setCursor: 996)
						#endif
						temp6 = (GetPort)
						(Print
							font: global22
							width: 250
							addText:
								(temp4 noun:)
								(temp4 helpVerb:)
								0
								1
								0
								0
								(temp4 modNum:)
							init:
						)
						(SetPort temp6)
						if (not (HaveMouse)):
							(global1 setCursor: temp60)
						#endif
					#endif
					if helpIconItem:
						(helpIconItem signal: ((helpIconItem signal:) & 0xffef))
					#endif
					(global1 setCursor: 999)
				#end:case
			#end:match
		#endif
		return temp5
	#end:method

	@classmethod
	def advance():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = 1
		while (temp1 <= size): # inline for
			(= temp0
				(self at: (mod (temp1 + (self indexOf: highlightedIcon)) size))
			)
			if (not (IsObject temp0)):
				temp0 = (NodeValue (self first:))
			#endif
			(breakif (not ((temp0 signal:) & 0x0004)))
			# for:reinit
			temp1 = (mod (temp1 + 1) size)
		#end:loop
		(self highlight: temp0 (state & 0x0020))
	#end:method

	@classmethod
	def retreat():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = 1
		while (temp1 <= size): # inline for
			(= temp0
				(self at: (mod ((self indexOf: highlightedIcon) - temp1) size))
			)
			if (not (IsObject temp0)):
				temp0 = (NodeValue (self last:))
			#endif
			(breakif (not ((temp0 signal:) & 0x0004)))
			# for:reinit
			temp1 = (mod (temp1 + 1) size)
		#end:loop
		(self highlight: temp0 (state & 0x0020))
	#end:method

	@classmethod
	def select(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			if (param1 select: ((argc >= 2) and param2)):
				if (not ((param1 signal:) & 0x0002)):
					curIcon = param1
				#endif
				1
			#endif
		)
	#end:method

	@classmethod
	def highlight(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not ((param1 signal:) & 0x0004)):
			if (IsObject highlightedIcon):
				(highlightedIcon highlight: 0)
			#endif
			highlightedIcon = param1
			(highlightedIcon highlight: 1)
		#endif
		if ((argc >= 2) and param2):
			(global1
				setCursor:
					global19
					1
					(+
						(param1 nsLeft:)
						(((param1 nsRight:) - (param1 nsLeft:)) / 2)
					)
					((param1 nsBottom:) - 3)
			)
		#endif
	#end:method

	@classmethod
	def advanceCurIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (state & 0x0004):
			return
		#endif
		temp0 = curIcon
		temp1 = 0
		while
			(&
				(temp0 = (self at: (mod ((self indexOf: temp0) + 1) size))
					signal:
				)
				0x0006
			):

			if (temp1 > (1 + size)):
				return
			else:
				temp1++
			#endif
		#end:loop
		curIcon = temp0
		(global1 setCursor: (curIcon cursor:) 1)
	#end:method

	@classmethod
	def swapCurIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (state & 0x0004):
				return
			#end:case
			case 
				(and
					(curIcon != temp0 = (NodeValue (self first:)))
					(not ((temp0 signal:) & 0x0004))
				):
				prevIcon = curIcon
				curIcon = (NodeValue (self first:))
			#end:case
			case (prevIcon and (not ((prevIcon signal:) & 0x0004))):
				curIcon = prevIcon
			#end:case
		)
		(global1 setCursor: (curIcon cursor:) 1)
	#end:method

#end:class or instance

