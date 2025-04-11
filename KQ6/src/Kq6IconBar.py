#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 98
import sci_sh
import kernel
import Main
import IconBar
import Tutorial
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


class Kq6IconBar(IconBar):
	#property vars (may be empty)
	activateHeight = 10
	hiRes = 0
	
	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (state & 0x0020):
			(global8 pause: 0)
			(state &= 0xffdf)
			temp0 = kernel.FirstNode(elements)
			while temp0: # inline for
				temp1 = kernel.NextNode(temp0)
				if (not kernel.IsObject(temp2 = kernel.NodeValue(temp0))):
					return
				#endif
				(temp2 = kernel.NodeValue(temp0)
					signal: ((temp2 signal:) & 0xffdf)
					view: local0
					maskView: local0
					hiRes: 0
				)
				# for:reinit
				temp0 = temp1
			#end:loop
			if 
				(and
					(not (state & 0x0800))
					helpIconItem
					((helpIconItem signal:) & 0x0010)
				)
				(helpIconItem signal: ((helpIconItem signal:) & 0xffef))
			#endif
			kernel.Graph(8, underBits)
			kernel.Graph(12, y, 0, (y + height), 320, 1)
			kernel.Graph(13, y, 0, (y + height), 320)
			kernel.SetPort(port)
			hiRes = 0
			height = activateHeight
		#endif
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global8 pause:)
		(state |= 0x0020)
		(global1 setCursor: 999 1)
		temp0 = (self at: 0)
		local0 = (temp0 view:)
		(= hiRes
			if (global169 and (not kernel.Platform(5))):
				kernel.Platform(6)
			#endif
		)
		if hiRes:
			(temp0 view: (temp0 hrView:))
		else:
			(temp0 view: (temp0 view:))
		#endif
		height = kernel.CelHigh((temp0 view:), (temp0 loop:), (temp0 cel:))
		port = kernel.GetPort()
		kernel.SetPort(-1)
		if hiRes:
			(height /= 2)
			underBits = kernel.Graph(15, y, 0, (y + height), 319)
		else:
			underBits = kernel.Graph(7, y, 0, (y + height), 320, 1)
		#endif
		temp1 = kernel.PicNotValid()
		kernel.PicNotValid(1)
		temp3 = 0
		temp4 = y
		temp5 = kernel.FirstNode(elements)
		while temp5: # inline for
			temp6 = kernel.NextNode(temp5)
			if (not kernel.IsObject(temp7 = kernel.NodeValue(temp5))):
				return
			#endif
			if hiRes:
				(temp7
					maskView: (temp0 hrView:)
					view: (temp0 hrView:)
					nsRight: 0
				)
			else:
				(temp7
					maskView: (temp0 maskView:)
					view: (temp0 view:)
					nsRight: 0
				)
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
		(self updateInvIcon:)
		kernel.PicNotValid(temp1)
		kernel.Graph(12, y, 0, (height * (2 if hiRes else 1)), 639, 1, if hiRes:
			underBits
		else:
			0
		#endif)
		(self highlight: curIcon)
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
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue((self first:))
			#endif
			(breakif (not ((temp0 signal:) & 0x0004)))
			# for:reinit
			temp1.post('++')
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
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue((self last:))
			#endif
			(breakif (not ((temp0 signal:) & 0x0004)))
			# for:reinit
			temp1.post('++')
		#end:loop
		(self highlight: temp0 (state & 0x0020))
	#end:method

	@classmethod
	def updateInvIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (curInvIcon and (not ((useIconItem state:) & 0x0004))):
			(curInvIcon view: (973 if hiRes else 970))
			if (global0 has: (global9 indexOf: curInvIcon)):
				(= temp0
					(+
						(/
							(-
								((useIconItem nsRight:) - (useIconItem nsLeft:))
								kernel.CelWide((curInvIcon view:), (curInvIcon
									loop:
								), (curInvIcon cel:))
							)
							2
						)
						(useIconItem nsLeft:)
					)
				)
				(= temp1
					(+
						y
						(/
							(-
								((useIconItem nsBottom:) - (useIconItem nsTop:))
								kernel.CelHigh((curInvIcon view:), (curInvIcon
									loop:
								), (curInvIcon cel:))
							)
							2
						)
						(useIconItem nsTop:)
					)
				)
				kernel.DrawCel((curInvIcon view:), (curInvIcon loop:), (curInvIcon
					cel:
				), temp0, temp1, -1, 0, (underBits if hiRes else 0))
				if ((useIconItem signal:) & 0x0004):
					(useIconItem mask:)
				#endif
			else:
				curInvIcon = 0
			#endif
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
								(/
									((curIcon nsRight:) - (curIcon nsLeft:))
									(4 if hiRes else 2)
								)
							)
							if (not hiRes):
								((curIcon nsBottom:) - 3)
							else:
								(-
									(+
										(curIcon nsTop:)
										kernel.CelHigh((curIcon view:), (curIcon
											loop:
										), (curIcon cel:))
									)
									3
								)
							#endif
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
					(global1 setCursor: temp3 1)
				#endif
				(self hide:)
			#end:case
			case (temp1 & 0x0004):
				match (param1 message:)
					case 13:
						(cond
							case (not kernel.IsObject(curIcon)):#end:case
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
					case kernel.IsObject(curIcon):
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

#end:class or instance

class Kq6IconItem(IconI):
	#property vars (may be empty)
	hiRes = 0
	hrView = 981
	
	@classmethod
	def highlight(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (or (not (signal & 0x0020)) (highlightColor == -1) hiRes):
			return
		#endif
		if (argc and param1):
			temp4 = highlightColor
			temp0 = (nsTop + 1)
			temp1 = (nsLeft + 1)
			temp2 = (nsBottom - 3)
			temp3 = (nsRight - 3)
			kernel.Graph(4, temp0, temp1, temp0, temp3, temp4, -1, -1)
			kernel.Graph(4, temp0, temp3, temp2, temp3, temp4, -1, -1)
			kernel.Graph(4, temp2, temp3, temp2, temp1, temp4, -1, -1)
			kernel.Graph(4, temp2, temp1, temp0, temp1, temp4, -1, -1)
		else:
			(self show:)
			if (Kq6IconBar curInvIcon:):
				(Kq6IconBar updateInvIcon:)
			#endif
		#endif
		kernel.Graph(12, (nsTop - 2), (nsLeft - 2), nsBottom, (nsRight + 3), 1)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				(>=
					(param1 x:)
					if hiRes:
						(nsLeft / 2)
					else:
						nsLeft
					#endif
				)
				(>=
					(param1 y:)
					if hiRes:
						(nsTop / 2)
					else:
						nsTop
					#endif
				)
				(<=
					(param1 x:)
					if hiRes:
						(nsRight / 2)
					else:
						nsRight
					#endif
				)
				(<=
					(param1 y:)
					if hiRes:
						(nsBottom / 2)
					else:
						nsBottom
					#endif
				)
			)
		)
	#end:method

	@classmethod
	def select(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if hiRes:
			temp3 = (global69 underBits:)
		else:
			temp3 = 0
		#endif
		(return
			(cond
				case (signal & 0x0004): 0#end:case
				case (and argc param1 (signal & 0x0001)):
					kernel.DrawCel(view, loop, temp1 = 1, nsLeft, nsTop, -1, 0, temp3)
					kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
					while ((temp0 = (Event new:) type:) != 2):

						(temp0 localize:)
						(cond
							case (self onMe: temp0):
								if (not temp1):
									kernel.DrawCel(view, loop, temp1 = 1, nsLeft, nsTop, -1, 0, temp3)
									kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
								#endif
							#end:case
							case temp1:
								kernel.DrawCel(view, loop, temp1 = 0, nsLeft, nsTop, -1, 0, temp3)
								kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
							#end:case
						)
						(temp0 dispose:)
					#end:loop
					(temp0 dispose:)
					if (temp1 == 1):
						kernel.DrawCel(view, loop, 0, nsLeft, nsTop, -1, 0, temp3)
						kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
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

	@classmethod
	def mask():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.DrawCel(maskView, maskLoop, maskCel, (+
			nsLeft
			(/
				(kernel.CelWide(view, loop, cel) - kernel.CelWide(maskView, maskLoop, maskCel))
				2
			)
		), (+
			nsTop
			(/
				(kernel.CelHigh(view, loop, cel) - kernel.CelHigh(maskView, maskLoop, maskCel))
				2
			)
		), -1, 0, if hiRes:
			(global69 underBits:)
		else:
			0
		#endif)
	#end:method

	@classmethod
	def show(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= hiRes
			if (global169 and (not kernel.Platform(5))):
				kernel.Platform(6)
			#endif
		)
		(signal |= 0x0020)
		if argc:
			nsRight = (nsLeft = param1 + kernel.CelWide(view, loop, cel))
			nsBottom = (nsTop = param2 + kernel.CelHigh(view, loop, cel))
		else:
			nsRight = (nsLeft + kernel.CelWide(view, loop, cel))
			nsBottom = (nsTop + kernel.CelHigh(view, loop, cel))
		#endif
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1, 0, if hiRes:
			(global69 underBits:)
		else:
			0
		#endif)
		if (signal & 0x0004):
			(self mask:)
		#endif
		if (global77 and (global77 respondsTo: #stop)):
			(global77 stop:)
		#endif
	#end:method

#end:class or instance

