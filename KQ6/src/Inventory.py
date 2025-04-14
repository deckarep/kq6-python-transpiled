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
	def onMe(param1 = None, *rest):
		return (super._send('onMe:', param1) and (not (signal & 0x0004)))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if (modNum == -1):
			modNum = global11
		#endif
		if (global90 and kernel.Message(0, modNum, noun, param1, 0, 1)):
			global91._send('say:', noun, param1, 0, 0, 0, modNum)
		#endif
		if (temp0 = global1._send('script:') and temp0._send('isKindOf:', Tutorial)):
			(cond
				case (temp0._send('nextItem:') != self):
					temp0._send('report:', self)
				#end:case
				case (temp0._send('nextAction:') != param1):
					temp0._send('report:', param1)
				#end:case
				else:
					temp0._send('cue:')
				#end:else
			)
		#endif
	#end:method

	@classmethod
	def highlight(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1)
	#end:method

	@classmethod
	def ownedBy(param1 = None, *rest):
		return (owner == param1)
	#end:method

	@classmethod
	def moveTo(param1 = None, *rest):
		owner = param1
		if (value and (param1 == global0)):
			global1._send('changeScore:', value)
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
	def drawInvWindow(param1 = None, param2 = None, *rest):
		global170 = 0
		temp0 = temp1 = temp2 = temp3 = temp4 = temp5 = 0
		temp8 = self._send('first:')
		while temp8: # inline for
			if temp9 = kernel.NodeValue(temp8)._send('isKindOf:', InvI):
				if temp9._send('ownedBy:', param1):
					temp9._send('signal:', (temp9._send('signal:') & 0xfffb))
					temp0.post('++')
					if 
						(>
							(= temp6
								kernel.CelWide(temp9._send('view:'), temp9._send(
									'loop:'
								), temp9._send('cel:'))
							)
							temp2
						)
						temp2 = temp6
					#endif
					if 
						(>
							(= temp7
								kernel.CelHigh(temp9._send('view:'), temp9._send(
									'loop:'
								), temp9._send('cel:'))
							)
							temp1
						)
						temp1 = temp7
					#endif
				else:
					temp9._send('signal:', (| temp9._send('signal:') 0x0004))
				#endif
			else:
				temp3.post('++')
				(temp5 += kernel.CelWide(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:')))
				if 
					(>
						(= temp7
							kernel.CelHigh(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:'))
						)
						temp4
					)
					temp4 = temp7
				#endif
			#endif
			# for:reinit
			temp8 = self._send('next:', temp8)
		#end:loop
		if (not temp0):
			Print._send('addTextF:', r"""%s %s""", normalHeading, empty, 'init:')
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
		if temp21 = self._send('window:'):
			temp21._send('top:', temp12, 'left:', temp13, 'right:', temp15, 'bottom:', temp14, 'open:')
		#endif
		temp20 = local0
		if temp0:
			(= temp18
				(+
					2
					if temp21._send('respondsTo:', #yOffset):
						temp21._send('yOffset:')
					#endif
				)
			)
			(= temp19
				(= temp17
					(+
						4
						if temp21._send('respondsTo:', #xOffset):
							temp21._send('xOffset:')
						#endif
					)
				)
			)
			temp8 = self._send('first:')
			while temp8: # inline for
				if 
					(and
						(not (temp9 = kernel.NodeValue(temp8)._send('signal:') & 0x0004))
						temp9._send('isKindOf:', InvI)
					)
					if (not (temp9._send('signal:') & 0x0080)):
						temp9._send(
							'nsLeft:', (+
									temp17
									(/
										(-
											temp2
											(= temp6
												kernel.CelWide(temp9._send('view:'), temp9._send(
													'loop:'
												), temp9._send('cel:'))
											)
										)
										2
									)
								),
							'nsTop:', (+
									temp18
									(/
										(-
											temp1
											(= temp7
												kernel.CelHigh(temp9._send('view:'), temp9._send(
													'loop:'
												), temp9._send('cel:'))
											)
										)
										2
									)
								)
						)
						temp9._send(
							'nsRight:', (temp9._send('nsLeft:') + temp6),
							'nsBottom:', (temp9._send('nsTop:') + temp7)
						)
						if temp20.post('--'):
							(temp17 += temp2)
						else:
							temp20 = local0
							(temp18 += temp1)
							temp17 = temp19
						#endif
					else:
						temp17 = temp9._send('nsLeft:')
						temp18 = temp9._send('nsTop:')
					#endif
					temp9._send('show:')
					if (temp9 == param2):
						temp9._send('highlight:')
					#endif
				#endif
				# for:reinit
				temp8 = self._send('next:', temp8)
			#end:loop
		#endif
		temp17 = (((temp21._send('right:') - temp21._send('left:')) - temp5) / 2)
		temp11 = (temp21._send('bottom:') - temp21._send('top:'))
		temp18 = 32767
		temp8 = self._send('first:')
		while temp8: # inline for
			if (not temp9 = kernel.NodeValue(temp8)._send('isKindOf:', InvI)):
				temp9._send('nsTop:', 0)
				temp6 = kernel.CelWide(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:'))
				temp7 = kernel.CelHigh(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:'))
				if (not (temp9._send('signal:') & 0x0080)):
					if (temp18 == 32767):
						temp18 = (temp11 - temp7)
					#endif
					temp9._send(
						'nsLeft:', temp17,
						'nsTop:', temp18,
						'nsBottom:', temp11,
						'nsRight:', (temp17 + temp6)
					)
				#endif
				temp17 = (temp9._send('nsLeft:') + temp6)
				temp18 = temp9._send('nsTop:')
				temp9._send('signal:', (temp9._send('signal:') & 0xfffb), 'show:')
			#endif
			# for:reinit
			temp8 = self._send('next:', temp8)
		#end:loop
		return 1
	#end:method

	@classmethod
	def init():
		heading = normalHeading
	#end:method

	@classmethod
	def ownedBy(param1 = None, *rest):
		self._send('firstTrue:', #ownedBy, param1)
	#end:method

	@classmethod
	def showSelf(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global8._send('pause:')
		if (global77 and global77._send('respondsTo:', #stop)):
			global77._send('stop:')
		#endif
		if global69._send('height:'):
			global69._send('hide:')
		#endif
		if (not window):
			window = SysWindow._send('new:')
		#endif
		if window._send('window:'):
			window._send('dispose:')
			window = 0
		#endif
		if (not okButton):
			okButton = kernel.NodeValue(self._send('first:'))
		#endif
		curIcon = 0
		if self._send('show:', (param1 if argc else global0)):
			self._send('doit:')
		#endif
	#end:method

	@classmethod
	def show(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global1._send(
			'setCursor:', if curIcon:
					curIcon._send('cursor:')
				else:
					selectIcon._send('cursor:')
				#endif
		)
		temp0 = kernel.PicNotValid()
		kernel.PicNotValid(0)
		(state |= 0x0020)
		if 
			(not
				(= temp1
					self._send(
						'drawInvWindow:', (param1 if argc else global0), global69._send(
								'curIcon:'
							)
					)
				)
			)
			(state &= 0xffdf)
		#endif
		kernel.PicNotValid(temp0)
		return temp1
	#end:method

	@classmethod
	def advance(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = (param1 if argc else 1)
		temp2 = self._send('indexOf:', highlightedIcon)
		temp3 = (temp1 + temp2)
		while True: #repeat
			(= temp0
				self._send(
					'at:', if (temp3 <= size):
							temp3
						else:
							(mod temp3 (size - 1))
						#endif
				)
			)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue(self._send('first:'))
			#endif
			if (not (temp0._send('signal:') & 0x0004)):
				(break)
			else:
				temp3.post('++')
			#endif
		#end:loop
		self._send('highlight:', temp0, 1)
	#end:method

	@classmethod
	def retreat(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = (param1 if argc else 1)
		temp3 = (temp2 = self._send('indexOf:', highlightedIcon) - temp1)
		while True: #repeat
			temp0 = self._send('at:', temp3)
			if (not kernel.IsObject(temp0)):
				temp0 = kernel.NodeValue(self._send('last:'))
			#endif
			if (not (temp0._send('signal:') & 0x0004)):
				(break)
			else:
				temp3.post('--')
			#endif
		#end:loop
		self._send('highlight:', temp0, 1)
	#end:method

	(procedure (localproc_0param1 = None, param2 = None, param3 = None, *rest):
		(= temp2
			(((param1._send('nsRight:') - param1._send('nsLeft:')) / 2) + param1._send('nsLeft:'))
		)
		temp1 = param2
		while (kernel.Abs((temp1 - param3)) >= 4):

			if 
				(= temp0
					self._send(
						'firstTrue:', #onMe, global80._send('curEvent:')._send('new:')._send(
								'x:', temp2,
								'y:', temp1,
								'yourself:'
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
		while temp1 = global80._send('curEvent:')._send('new:')._send('type:'):

		#end:loop
		while (state & 0x0020):

			temp1 = global80._send('curEvent:')._send('new:')
			global70 = temp1._send('x:')
			global71 = temp1._send('y:')
			temp2 = temp1._send('type:')
			temp3 = temp1._send('message:')
			temp4 = temp1._send('modifiers:')
			temp9 = 0
			temp1._send('localize:')
			if 
				(and
					curIcon
					(not temp4)
					(curIcon != selectIcon)
					(or
						(temp2 == 1)
						((temp2 == 4) and (temp3 == 13) and temp9 = 1)
						((temp2 == 256) and temp9 = 1)
					)
					(or
						(curIcon != helpIconItem)
						(helpIconItem._send('signal:') & 0x0010)
					)
				)
				temp1._send('type:', 16384, 'message:', curIcon._send('message:'))
			#endif
			kernel.MapKeyToDir(temp1)
			temp2 = temp1._send('type:')
			temp3 = temp1._send('message:')
			if global170:
				temp1._send('claimed:', 1)
				global170 = 0
				(break)
			#endif
			if global18:
				global18._send('eachElementDo:', #doit)
			#endif
			if (temp60 = global1._send('script:') and temp60._send('isKindOf:', Tutorial)):
				temp60._send('doit:')
			#endif
			if global84:
				global84._send('eachElementDo:', #doit)
				global88 = (global86 + kernel.GetTime())
				if global84:
					global84._send('handleEvent:', temp1)
				#endif
			else:
				if ((temp2 == 1) and temp4):
					self._send('advanceCurIcon:')
					temp1._send('claimed:', 1)
					(continue)
				#endif
				if 
					(and
						(temp2 == 0)
						temp0 = self._send('firstTrue:', #onMe, temp1)
						(temp0 != highlightedIcon)
					)
					self._send('highlight:', temp0)
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
								self._send('select:', highlightedIcon, (temp2 == 1))
							)
							if (highlightedIcon == okButton):
								temp1._send('claimed:', 1)
								(break)
							#endif
							if (highlightedIcon == helpIconItem):
								if (highlightedIcon._send('cursor:') != -1):
									global1._send('setCursor:', helpIconItem._send('cursor:'))
								#endif
								if (state & 0x0800):
									self._send('noClickHelp:')
									(continue)
								#endif
								if helpIconItem:
									helpIconItem._send(
										'signal:', (| helpIconItem._send('signal:') 0x0010)
									)
								#endif
								(continue)
							#endif
							curIcon = highlightedIcon
							global1._send('setCursor:', curIcon._send('cursor:'))
						#endif
					#end:case
					case (temp2 & 0x0040):
						match temp3
							case 3:
								self._send('advance:')
							#end:case
							case 7:
								self._send('retreat:')
							#end:case
							case 1:
								if 
									(and
										highlightedIcon
										(= temp0
											localproc_0(highlightedIcon, (-
												highlightedIcon._send('nsTop:')
												1
											), 0)
										)
									)
									self._send('highlight:', temp0, 1)
								else:
									self._send('retreat:')
								#endif
							#end:case
							case 5:
								if 
									(and
										highlightedIcon
										(= temp0
											localproc_0(highlightedIcon, (+
												highlightedIcon._send('nsBottom:')
												1
											), window._send('bottom:'))
										)
									)
									self._send('highlight:', temp0, 1)
								else:
									self._send('advance:')
								#endif
							#end:case
							case 0:
								if (temp2 & 0x0004):
									self._send('advanceCurIcon:')
								#endif
							#end:case
						#end:match
					#end:case
					case (temp2 == 4):
						match temp3
							case 9:
								self._send('advance:')
							#end:case
							case 3840:
								self._send('retreat:')
							#end:case
							case 27:
								(break)
							#end:case
						#end:match
					#end:case
					case 
						(and
							(temp2 & 0x4000)
							temp0 = self._send('firstTrue:', #onMe, temp1)
						):
						if (temp2 & 0x2000):
							if 
								(and
									temp0
									temp0._send('noun:')
									kernel.Message(0, temp0._send('modNum:'), temp0._send(
										'noun:'
									), temp0._send('helpVerb:'), 0, 1, @temp10)
								)
								if global38._send('respondsTo:', #eraseOnly):
									temp7 = global38._send('eraseOnly:')
									global38._send('eraseOnly:', 1)
									proc921_0(@temp10)
									global38._send('eraseOnly:', temp7)
								else:
									proc921_0(@temp10)
								#endif
							#endif
							helpIconItem._send(
								'signal:', (helpIconItem._send('signal:') & 0xffef)
							)
							global1._send('setCursor:', 999)
							(continue)
						#endif
						if (temp0 == okButton):
							temp1._send('claimed:', 1)
							(break)
						#endif
						if (not temp0._send('isKindOf:', InvI)):
							if self._send('select:', temp0, (not temp9)):
								curIcon = temp0
								global1._send('setCursor:', curIcon._send('cursor:'))
								if (temp0 == helpIconItem):
									if (state & 0x0800):
										self._send('noClickHelp:')
										(continue)
									#endif
									helpIconItem._send(
										'signal:', (| helpIconItem._send('signal:') 0x0010)
									)
								#endif
							#endif
							(continue)
						#endif
						if curIcon:
							temp1._send('claimed:', 1)
							if global38._send('respondsTo:', #eraseOnly):
								temp7 = global38._send('eraseOnly:')
								global38._send('eraseOnly:', 1)
							#endif
							if curIcon._send('isKindOf:', InvI):
								temp0._send('doVerb:', curIcon._send('message:'))
							else:
								temp0._send('doVerb:', temp1._send('message:'))
							#endif
							if global38._send('respondsTo:', #eraseOnly):
								global38._send('eraseOnly:', temp7)
							#endif
						#endif
					#end:case
				)
			#endif
		#end:loop
		self._send('hide:')
	#end:method

	@classmethod
	def hide():
		if (state & 0x0020):
			global8._send('pause:', 0)
			(state &= 0xffdf)
		#endif
		if window:
			window._send('dispose:')
		#endif
		if (kernel.IsObject(curIcon) and curIcon._send('isKindOf:', InvI)):
			if (not global69._send('curInvIcon:')):
				global69._send('enable:', global69._send('useIconItem:'))
			#endif
			global69._send(
				'curIcon:', global69._send('useIconItem:')._send(
						'cursor:', curIcon._send('cursor:'),
						'yourself:'
					),
				'curInvIcon:', curIcon
			)
			if temp0 = global69._send('curIcon:')._send('cursor:'):
				global1._send('setCursor:', temp0)
			#endif
		#endif
	#end:method

#end:class or instance

