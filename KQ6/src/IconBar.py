#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 937
import sci_sh
import kernel
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
	def show(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(signal |= 0x0020)
		if argc:
			nsRight = (nsLeft = param1 + kernel.CelWide(view, loop, cel))
			nsBottom = (nsTop = param2 + kernel.CelHigh(view, loop, cel))
		else:
			nsRight = (nsLeft + kernel.CelWide(view, loop, cel))
			nsBottom = (nsTop + kernel.CelHigh(view, loop, cel))
		#endif
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1)
		if (signal & 0x0004):
			self._send('mask:')
		#endif
		if (global77 and global77._send('respondsTo:', #stop)):
			global77._send('stop:')
		#endif
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
		), -1)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				(param1._send('x:') >= nsLeft)
				(param1._send('y:') >= nsTop)
				(param1._send('x:') <= nsRight)
				(param1._send('y:') <= nsBottom)
			)
		)
	#end:method

	@classmethod
	def highlight(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not (signal & 0x0020)) or (highlightColor == -1)):
			return
		#endif
		temp4 = (highlightColor if (argc and param1) else lowlightColor)
		temp0 = (nsTop + 2)
		temp1 = (nsLeft + 2)
		temp2 = (nsBottom - 3)
		temp3 = (nsRight - 4)
		kernel.Graph(4, temp0, temp1, temp0, temp3, temp4, -1, -1)
		kernel.Graph(4, temp0, temp3, temp2, temp3, temp4, -1, -1)
		kernel.Graph(4, temp2, temp3, temp2, temp1, temp4, -1, -1)
		kernel.Graph(4, temp2, temp1, temp0, temp1, temp4, -1, -1)
		kernel.Graph(12, (nsTop - 2), (nsLeft - 2), nsBottom, (nsRight + 3), 1)
	#end:method

	@classmethod
	def select(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(cond
				case (signal & 0x0004): 0#end:case
				case (argc and param1 and (signal & 0x0001)):
					kernel.DrawCel(view, loop, temp1 = 1, nsLeft, nsTop, -1)
					kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
					while (temp0 = Event._send('new:')._send('type:') != 2):

						temp0._send('localize:')
						(cond
							case self._send('onMe:', temp0):
								if (not temp1):
									kernel.DrawCel(view, loop, temp1 = 1, nsLeft, nsTop, -1)
									kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
								#endif
							#end:case
							case temp1:
								kernel.DrawCel(view, loop, temp1 = 0, nsLeft, nsTop, -1)
								kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
							#end:case
						)
						temp0._send('dispose:')
					#end:loop
					temp0._send('dispose:')
					if (temp1 == 1):
						kernel.DrawCel(view, loop, 0, nsLeft, nsTop, -1)
						kernel.Graph(12, nsTop, nsLeft, nsBottom, nsRight, 1)
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
	def findIcon(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < size): # inline for
			temp1 = self._send('at:', temp0)
			if (temp1._send('message:') == param1):
				return temp1
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		return 0
	#end:method

	@classmethod
	def noClickHelp():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = temp2 = 0
		temp3 = kernel.GetPort()
		temp4 = global38._send('eraseOnly:')
		global38._send('eraseOnly:', 1)
		while (not temp0 = global80._send('curEvent:')._send('new:')._send('type:')):

			if (not self._send('isMemberOf:', IconBar)):
				temp0._send('localize:')
			#endif
			(cond
				case temp2 = self._send('firstTrue:', #onMe, temp0):
					if ((temp2 != temp1) and temp2._send('helpVerb:')):
						temp1 = temp2
						if global25:
							global25._send('dispose:')
						#endif
						Print._send(
							'font:', global22,
							'width:', 250,
							'addText:', temp2._send('noun:'), temp2._send('helpVerb:'), 0, 1, 0, 0, temp2._send(
									'modNum:'
								),
							'modeless:', 1,
							'init:'
						)
						kernel.SetPort(temp3)
					#endif
				#end:case
				case global25:
					global25._send('dispose:')
				#end:case
				else:
					temp1 = 0
				#end:else
			)
			temp0._send('dispose:')
		#end:loop
		global38._send('eraseOnly:', temp4)
		global1._send('setCursor:', 999, 1)
		if global25:
			global25._send('dispose:')
		#endif
		kernel.SetPort(temp3)
		if (not helpIconItem._send('onMe:', temp0)):
			self._send('dispatchEvent:', temp0)
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
								((curIcon._send('nsRight:') - curIcon._send('nsLeft:')) / 2)
							), (curIcon._send('nsBottom:') - 3)
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
					global1._send(
						'setCursor:', temp3, 1, param1._send('new:')._send('x:'), proc999_3(param1._send(
								'y:'
							), (1 + height))
					)
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

	@classmethod
	def disable(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			temp0 = 0
			while (temp0 < argc): # inline for
				(= temp1
					if kernel.IsObject(param1[temp0]):
						param1[temp0]
					else:
						self._send('at:', param1[temp0])
					#endif
				)
				temp1._send('signal:', (| temp1._send('signal:') 0x0004))
				(cond
					case (temp1 == curIcon):
						self._send('advanceCurIcon:')
					#end:case
					case (temp1 == highlightedIcon):
						self._send('advance:')
					#end:case
				)
				# for:reinit
				temp0.post('++')
			#end:loop
		else:
			(state |= 0x0004)
		#endif
	#end:method

	@classmethod
	def enable(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			temp0 = 0
			while (temp0 < argc): # inline for
				(= temp1
					if kernel.IsObject(param1[temp0]):
						param1[temp0]
					else:
						self._send('at:', param1[temp0])
					#endif
				)
				temp1._send('signal:', (temp1._send('signal:') & 0xfffb))
				# for:reinit
				temp0.post('++')
			#end:loop
		else:
			(state &= 0xfffb)
		#endif
	#end:method

	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global8._send('pause:')
		(state |= 0x0020)
		global1._send('setCursor:', 999, 1)
		(= height
			kernel.CelHigh(temp0 = self._send('at:', 0)._send('view:'), temp0._send('loop:'), temp0._send('cel:'))
		)
		port = kernel.GetPort()
		kernel.SetPort(-1)
		underBits = kernel.Graph(7, y, 0, (y + height), 320, 1)
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
			if (temp7._send('nsRight:') <= 0):
				temp7._send('show:', temp3, temp4)
				temp3 = temp7._send('nsRight:')
			else:
				temp7._send('show:')
			#endif
			# for:reinit
			temp5 = temp6
		#end:loop
		if curInvIcon:
			if global0._send('has:', global9._send('indexOf:', curInvIcon)):
				(= temp3
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
				(= temp4
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
				), temp3, temp4, -1)
				if (useIconItem._send('signal:') & 0x0004):
					useIconItem._send('mask:')
				#endif
			else:
				curInvIcon = 0
			#endif
		#endif
		kernel.PicNotValid(temp1)
		kernel.Graph(12, y, 0, (y + height), 320, 1)
		self._send('highlight:', curIcon)
	#end:method

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
				temp2 = kernel.NodeValue(temp0)._send('signal:', (temp2._send('signal:') & 0xffdf))
				# for:reinit
				temp0 = temp1
			#end:loop
			if 
				(and
					(not (state & 0x0800))
					kernel.IsObject(helpIconItem)
					(helpIconItem._send('signal:') & 0x0010)
				)
				helpIconItem._send('signal:', (helpIconItem._send('signal:') & 0xffef))
			#endif
			kernel.Graph(8, underBits)
			kernel.Graph(12, y, 0, (y + height), 320, 1)
			kernel.Graph(13, y, 0, (y + height), 320)
			kernel.SetPort(port)
			height = activateHeight
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		while ((state & 0x0020) and temp0 = global80._send('curEvent:')._send('new:')):

			temp1 = temp0._send('type:')
			temp2 = temp0._send('message:')
			temp3 = temp0._send('modifiers:')
			kernel.Wait(1)
			global88 = (global86 + kernel.GetTime())
			if global18:
				global18._send('eachElementDo:', #doit)
			#endif
			if (temp4 = global1._send('script:') and temp4._send('isKindOf:', Tutorial)):
				temp4._send('doit:')
			#endif
			if (temp1 == 256):
				temp1 = 4
				temp2 = (27 if (temp3 & 0x0003) else 13)
				temp3 = 0
				temp0._send('type:', temp1, 'message:', temp2, 'modifiers:', 0)
			#endif
			temp0._send('localize:')
			if 
				(and
					((temp1 == 1) or ((temp1 == 4) and (temp2 == 13)))
					kernel.IsObject(helpIconItem)
					(helpIconItem._send('signal:') & 0x0010)
				)
				temp0._send('type:', 24576, 'message:', helpIconItem._send('message:'))
			#endif
			kernel.MapKeyToDir(temp0)
			(breakif self._send('dispatchEvent:', temp0))
		#end:loop
	#end:method

	@classmethod
	def dispatchEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = param1._send('x:')
		temp0 = param1._send('y:')
		temp2 = param1._send('type:')
		temp3 = param1._send('message:')
		temp5 = param1._send('claimed:')
		if temp4 = self._send('firstTrue:', #onMe, param1):
			temp57 = temp4._send('cursor:')
			temp58 = temp4._send('signal:')
			temp59 = (temp4 == helpIconItem)
		#endif
		if (temp2 & 0x0040):
			match temp3
				case 3:
					self._send('advance:')
				#end:case
				case 7:
					self._send('retreat:')
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
										(not kernel.IsObject(helpIconItem))
										(not (helpIconItem._send('signal:') & 0x0010))
									)
								)
								oldMouseY = 0
								temp5 = 1
							#endif
						#end:case
						case (temp4 and (temp4 != highlightedIcon)):
							oldMouseY = 0
							self._send('highlight:', temp4)
						#end:case
					)
				#end:case
				case 1:
					if (temp4 and self._send('select:', temp4, 1)):
						if temp59:
							if temp57:
								global1._send('setCursor:', temp57)
							#endif
							if (state & 0x0800):
								self._send('noClickHelp:')
							else:
								helpIconItem._send(
									'signal:', (| helpIconItem._send('signal:') 0x0010)
								)
							#endif
						else:
							temp5 = (temp58 & 0x0040)
						#endif
						temp4._send('doit:')
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
										global1._send('setCursor:', temp57)
									#endif
									if helpIconItem:
										helpIconItem._send(
											'signal:', (|
													helpIconItem._send('signal:')
													0x0010
												)
										)
									#endif
								#end:case
								case (kernel.IsObject(temp4) and self._send('select:', temp4)):
									temp4._send('doit:')
									temp5 = (temp58 & 0x0040)
								#end:case
							)
						#end:case
						case 3840:
							self._send('retreat:')
						#end:case
						case 9:
							self._send('advance:')
						#end:case
					#end:match
				#end:case
				case 24576:
					if (temp4 and temp4._send('helpVerb:')):
						if (not kernel.HaveMouse()):
							temp60 = global1._send('setCursor:', 996)
						#endif
						temp6 = kernel.GetPort()
						Print._send(
							'font:', global22,
							'width:', 250,
							'addText:', temp4._send('noun:'), temp4._send('helpVerb:'), 0, 1, 0, 0, temp4._send(
									'modNum:'
								),
							'init:'
						)
						kernel.SetPort(temp6)
						if (not kernel.HaveMouse()):
							global1._send('setCursor:', temp60)
						#endif
					#endif
					if helpIconItem:
						helpIconItem._send('signal:', (helpIconItem._send('signal:') & 0xffef))
					#endif
					global1._send('setCursor:', 999)
				#end:case
			#end:match
		#endif
		return temp5
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
			temp1 = (mod (temp1 + 1) size)
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
			temp1 = (mod (temp1 + 1) size)
		#end:loop
		self._send('highlight:', temp0, (state & 0x0020))
	#end:method

	@classmethod
	def select(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			if param1._send('select:', ((argc >= 2) and param2)):
				if (not (param1._send('signal:') & 0x0002)):
					curIcon = param1
				#endif
				1
			#endif
		)
	#end:method

	@classmethod
	def highlight(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (param1._send('signal:') & 0x0004)):
			if kernel.IsObject(highlightedIcon):
				highlightedIcon._send('highlight:', 0)
			#endif
			highlightedIcon = param1
			highlightedIcon._send('highlight:', 1)
		#endif
		if ((argc >= 2) and param2):
			global1._send(
				'setCursor:', global19, 1, (+
						param1._send('nsLeft:')
						((param1._send('nsRight:') - param1._send('nsLeft:')) / 2)
					), (param1._send('nsBottom:') - 3)
			)
		#endif
	#end:method

	@classmethod
	def advanceCurIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (state & 0x0004):
			return
		#endif
		temp0 = curIcon
		temp1 = 0
		while
			(&
				temp0 = self._send('at:', (mod (self._send('indexOf:', temp0) + 1) size))._send(
					'signal:'
				)
				0x0006
			):

			if (temp1 > (1 + size)):
				return
			else:
				temp1.post('++')
			#endif
		#end:loop
		curIcon = temp0
		global1._send('setCursor:', curIcon._send('cursor:'), 1)
	#end:method

	@classmethod
	def swapCurIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (state & 0x0004):
				return
			#end:case
			case 
				(and
					(curIcon != temp0 = kernel.NodeValue(self._send('first:')))
					(not (temp0._send('signal:') & 0x0004))
				):
				prevIcon = curIcon
				curIcon = kernel.NodeValue(self._send('first:'))
			#end:case
			case (prevIcon and (not (prevIcon._send('signal:') & 0x0004))):
				curIcon = prevIcon
			#end:case
		)
		global1._send('setCursor:', curIcon._send('cursor:'), 1)
	#end:method

#end:class or instance

