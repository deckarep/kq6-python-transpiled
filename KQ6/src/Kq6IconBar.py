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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (state & 0x0020):
			global8._send('pause:', 0)
			(state &= 0xffdf)
			temp0 = kernel.FirstNode(elements)
			while temp0: # inline for
				temp1 = kernel.NextNode(temp0)
				if (not kernel.IsObject(temp2 = kernel.NodeValue(temp0))):
					return
				#endif
				temp2 = kernel.NodeValue(temp0)._send(
					'signal:', (temp2._send('signal:') & 0xffdf),
					'view:', local0,
					'maskView:', local0,
					'hiRes:', 0
				)
				# for:reinit
				temp0 = temp1
			#end:loop
			if 
				(and
					(not (state & 0x0800))
					helpIconItem
					(helpIconItem._send('signal:') & 0x0010)
				)
				helpIconItem._send('signal:', (helpIconItem._send('signal:') & 0xffef))
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global8._send('pause:')
		(state |= 0x0020)
		global1._send('setCursor:', 999, 1)
		temp0 = self._send('at:', 0)
		local0 = temp0._send('view:')
		(= hiRes
			if (global169 and (not kernel.Platform(5))):
				kernel.Platform(6)
			#endif
		)
		if hiRes:
			temp0._send('view:', temp0._send('hrView:'))
		else:
			temp0._send('view:', temp0._send('view:'))
		#endif
		height = kernel.CelHigh(temp0._send('view:'), temp0._send('loop:'), temp0._send('cel:'))
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
				temp7._send(
					'maskView:', temp0._send('hrView:'),
					'view:', temp0._send('hrView:'),
					'nsRight:', 0
				)
			else:
				temp7._send(
					'maskView:', temp0._send('maskView:'),
					'view:', temp0._send('view:'),
					'nsRight:', 0
				)
			#endif
			if (temp7._send('nsRight:') <= 0):
				temp7._send('show:', temp3, temp4)
				temp3 = temp7._send('nsRight:')
			else:
				temp7._send('show:')
			#endif
			# for:reinit
			temp5 = temp6
		#end:loop
		self._send('updateInvIcon:')
		kernel.PicNotValid(temp1)
		kernel.Graph(12, y, 0, (height * (2 if hiRes else 1)), 639, 1, if hiRes:
			underBits
		else:
			0
		#endif)
		self._send('highlight:', curIcon)
	#end:method

	@classmethod
	def advance():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = 1
		while (temp1 <= size): # inline for
			(= temp0
				self._send('at:', (mod (temp1 + self._send('indexOf:', highlightedIcon)) size))
			)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue(self._send('first:'))
			#endif
			(breakif (not (temp0._send('signal:') & 0x0004)))
			# for:reinit
			temp1.post('++')
		#end:loop
		self._send('highlight:', temp0, (state & 0x0020))
	#end:method

	@classmethod
	def retreat():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = 1
		while (temp1 <= size): # inline for
			(= temp0
				self._send('at:', (mod (self._send('indexOf:', highlightedIcon) - temp1) size))
			)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue(self._send('last:'))
			#endif
			(breakif (not (temp0._send('signal:') & 0x0004)))
			# for:reinit
			temp1.post('++')
		#end:loop
		self._send('highlight:', temp0, (state & 0x0020))
	#end:method

	@classmethod
	def updateInvIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (curInvIcon and (not (useIconItem._send('state:') & 0x0004))):
			curInvIcon._send('view:', (973 if hiRes else 970))
			if global0._send('has:', global9._send('indexOf:', curInvIcon)):
				(= temp0
					(+
						(/
							(-
								(useIconItem._send('nsRight:') - useIconItem._send('nsLeft:'))
								kernel.CelWide(curInvIcon._send('view:'), curInvIcon._send(
									'loop:'
								), curInvIcon._send('cel:'))
							)
							2
						)
						useIconItem._send('nsLeft:')
					)
				)
				(= temp1
					(+
						y
						(/
							(-
								(useIconItem._send('nsBottom:') - useIconItem._send('nsTop:'))
								kernel.CelHigh(curInvIcon._send('view:'), curInvIcon._send(
									'loop:'
								), curInvIcon._send('cel:'))
							)
							2
						)
						useIconItem._send('nsTop:')
					)
				)
				kernel.DrawCel(curInvIcon._send('view:'), curInvIcon._send('loop:'), curInvIcon._send(
					'cel:'
				), temp0, temp1, -1, 0, (underBits if hiRes else 0))
				if (useIconItem._send('signal:') & 0x0004):
					useIconItem._send('mask:')
				#endif
			else:
				curInvIcon = 0
			#endif
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		param1._send('localize:')
		temp1 = param1._send('type:')
		(cond
			case (state & 0x0004):#end:case
			case 
				(or
					(and
						(not temp1)
						(state & 0x0400)
						(<= -10 param1._send('y:') height)
						(<= 0 param1._send('x:') 320)
						(not temp0 = 0)
					)
					(and
						(temp1 == 4)
						(or
							(param1._send('message:') == 27)
							(param1._send('message:') == 21248)
						)
						temp0 = 1
					)
				):
				param1._send('globalize:')
				oldMouseX = param1._send('x:')
				oldMouseY = param1._send('y:')
				temp4 = global19
				temp5 = curIcon
				temp6 = curInvIcon
				self._send('show:')
				global1._send('setCursor:', 999)
				if temp0:
					global1._send(
						'setCursor:', global19, 1, (+
								curIcon._send('nsLeft:')
								(/
									(curIcon._send('nsRight:') - curIcon._send('nsLeft:'))
									(4 if hiRes else 2)
								)
							), if (not hiRes):
								(curIcon._send('nsBottom:') - 3)
							else:
								(-
									(+
										curIcon._send('nsTop:')
										kernel.CelHigh(curIcon._send('view:'), curIcon._send(
											'loop:'
										), curIcon._send('cel:'))
									)
									3
								)
							#endif
					)
				#endif
				self._send('doit:')
				(= temp3
					if (global80._send('canControl:') or global80._send('canInput:')):
						curIcon._send('cursor:')
					else:
						global21
					#endif
				)
				if temp0:
					global1._send('setCursor:', temp3, 1, oldMouseX, oldMouseY)
				else:
					global1._send('setCursor:', temp3, 1)
				#endif
				self._send('hide:')
			#end:case
			case (temp1 & 0x0004):
				match param1._send('message:')
					case 13:
						(cond
							case (not kernel.IsObject(curIcon)):#end:case
							case ((curIcon != useIconItem) or curInvIcon):
								param1._send(
									'type:', curIcon._send('type:'),
									'message:', if (curIcon == useIconItem):
											curInvIcon._send('message:')
										else:
											curIcon._send('message:')
										#endif
								)
							#end:case
							else:
								param1._send('type:', 0)
							#end:else
						)
					#end:case
					case 20992:
						if global80._send('canControl:'):
							self._send('swapCurIcon:')
						#endif
						param1._send('claimed:', 1)
					#end:case
					case 0:
						if (param1._send('type:') & 0x0040):
							self._send('advanceCurIcon:')
							param1._send('claimed:', 1)
						#endif
					#end:case
				#end:match
			#end:case
			case (temp1 & 0x0001):
				(cond
					case (param1._send('modifiers:') & 0x0003):
						self._send('advanceCurIcon:')
						param1._send('claimed:', 1)
					#end:case
					case (param1._send('modifiers:') & 0x0004):
						if global80._send('canControl:'):
							self._send('swapCurIcon:')
						#endif
						param1._send('claimed:', 1)
					#end:case
					case kernel.IsObject(curIcon):
						param1._send(
							'type:', curIcon._send('type:'),
							'message:', if (curIcon == useIconItem):
									curInvIcon._send('message:')
								else:
									curIcon._send('message:')
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
	def highlight(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not (signal & 0x0020)) or (highlightColor == -1) or hiRes):
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
			self._send('show:')
			if Kq6IconBar._send('curInvIcon:'):
				Kq6IconBar._send('updateInvIcon:')
			#endif
		#endif
		kernel.Graph(12, (nsTop - 2), (nsLeft - 2), nsBottom, (nsRight + 3), 1)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				(>=
					param1._send('x:')
					if hiRes:
						(nsLeft / 2)
					else:
						nsLeft
					#endif
				)
				(>=
					param1._send('y:')
					if hiRes:
						(nsTop / 2)
					else:
						nsTop
					#endif
				)
				(<=
					param1._send('x:')
					if hiRes:
						(nsRight / 2)
					else:
						nsRight
					#endif
				)
				(<=
					param1._send('y:')
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
	def select(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if hiRes:
			temp3 = global69._send('underBits:')
		else:
			temp3 = 0
		#endif
		(return
			(cond
				case (signal & 0x0004): 0#end:case
				case (argc and param1 and (signal & 0x0001)):
					kernel.DrawCel(view, loop, temp1 = 1, nsLeft, nsTop, -1, 0, temp3)
					kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
					while (temp0 = Event._send('new:')._send('type:') != 2):

						temp0._send('localize:')
						(cond
							case self._send('onMe:', temp0):
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
						temp0._send('dispose:')
					#end:loop
					temp0._send('dispose:')
					if (temp1 == 1):
						kernel.DrawCel(view, loop, 0, nsLeft, nsTop, -1, 0, temp3)
						kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1, temp3)
					#endif
					if 
						(and
							temp2 = global1._send('script:')
							temp2._send('isKindOf:', Tutorial)
						)
						(cond
							case 
								(and
									(temp2._send('nextItem:') == self)
									(!=
										temp2._send('nextAction:')
										global69._send('helpIconItem:')._send('message:')
									)
								):
								temp2._send('cue:')
							#end:case
							case (not temp1):
								return 0
							#end:case
							else:
								temp2._send('report:')
								return 0
							#end:else
						)
					#endif
					temp1
				#end:case
				else:
					if 
						(and
							temp2 = global1._send('script:')
							temp2._send('isKindOf:', Tutorial)
						)
						if 
							(and
								(temp2._send('nextItem:') == self)
								(!=
									temp2._send('nextAction:')
									global69._send('helpIconItem:')._send('message:')
								)
							)
							temp2._send('cue:')
						else:
							temp2._send('report:')
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
			global69._send('underBits:')
		else:
			0
		#endif)
	#end:method

	@classmethod
	def show(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
			global69._send('underBits:')
		else:
			0
		#endif)
		if (signal & 0x0004):
			self._send('mask:')
		#endif
		if (global77 and global77._send('respondsTo:', #stop)):
			global77._send('stop:')
		#endif
	#end:method

#end:class or instance

