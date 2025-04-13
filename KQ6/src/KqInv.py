#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 907
import sci_sh
import kernel
import Main
import KQ6Print
import Kq6Window
import n913
import Print
import IconBar
import Tutorial
import Window
import Game
import Inventory
import User
import System

# Public Export Declarations
SCI.public_exports(
	KqInv = 0,
	pageCode = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


class Kq6InvItem(InvI):
	#property vars (may be empty)
	view = 970
	modNum = 907
	realOwner = 0
	cursorView = 0
	cursorLoop = 0
	cursorCel = 0
	hideInv = 0
	
	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1, 0, if 
			(global169 and kernel.Platform(6) and (not kernel.Platform(5)))
			global9._send('empty:')
		else:
			0
		#endif)
	#end:method

	@classmethod
	def select():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		genericCursor._send('view:', cursorView, 'loop:', cursorLoop, 'cel:', cursorCel)
		global1._send('setCursor:', genericCursor)
		super._send('select:', &rest)
	#end:method

	@classmethod
	def highlight():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not global169) or kernel.Platform(5)):
			super._send('highlight:', &rest)
		#endif
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (signal & 0x0004):
			return 0
		#endif
		(= temp0
			if (global169 and kernel.Platform(6)):
				(not kernel.Platform(5))
			else:
				0
			#endif
		)
		(return
			if 
				(>=
					param1._send('x:')
					if temp0:
						(nsLeft / 2)
					else:
						nsLeft
					#endif
				)
				if 
					(>=
						param1._send('y:')
						if temp0:
							(nsTop / 2)
						else:
							nsTop
						#endif
					)
					(and
						(<=
							param1._send('x:')
							if temp0:
								(nsRight / 2)
							else:
								nsRight
							#endif
						)
						(<=
							param1._send('y:')
							if temp0:
								(nsBottom / 2)
							else:
								nsBottom
							#endif
						)
					)
				#endif
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 28, 13, 12):
			global91._send('say:', 0, param1, 0, 0, 0, modNum)
		else:
			if hideInv:
				global9._send('hide:', 1)
			#endif
			if (not modNum):
				modNum = global11
			#endif
			(cond
				case 
					(and
						global90
						kernel.Message(0, modNum, noun, param1, 0, 1)
						(global91._send('findTalker:', kernel.Message(1, 0)) != -1)
					):
					if hideInv:
						global91._send('say:', noun, param1, 0, 0, self, modNum)
					else:
						global91._send('say:', noun, param1, 0, 0, 0, modNum)
					#endif
				#end:case
				case 
					(and
						global9._send('curIcon:')
						(global9._send('curIcon:') != self)
						global9._send('curIcon:')._send('isKindOf:', InvI)
						temp0 = kernel.Message(0, modNum, noun, param1, 0, 1)
						(global91._send('findTalker:', temp0) != -1)
					):
					global9._send('curIcon:')._send('doVerb:', message)
				#end:case
				else:
					match param1
						case 5:
							global91._send('say:', 64, 5, 0, 0, 0, modNum)
						#end:case
						case 2:
							global91._send('say:', 64, 2, 0, 0, 0, modNum)
						#end:case
						else:
							global91._send('say:', noun, 0, 0, 0, 0, modNum)
						#end:else
					#end:match
				#end:else
			)
		#endif
	#end:method

	@classmethod
	def checkPage():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = 0
		temp0 = 0
		while (temp0 < 52): # inline for
			if (global9._send('at:', temp0)._send('owner:') == local1):
				temp1 = 1
				temp0 = 53
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		global9._send('hide:')
		if temp1:
			if (temp0 > 52):
				global9._send('show:', local1, 'selectIcon:', invSelect)
			else:
				invPrevious._send('select:')
			#endif
		#endif
	#end:method

	@classmethod
	def setCursor(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		cursorView = param1
		cursorLoop = param2
		cursorCel = param3
		cursor = genericCursor
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc and param1):
			pageCode._send('init:', local1)
		else:
			if (not global18):
				global18 = Set._send('new:')
			#endif
			global18._send(
				'add:', Cue._send('new:')._send('cuee:', self, 'cuer:', self, 'register:', 1, 'yourself:')
			)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class pageCode(Code):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local1 = param1
		global9._send('selectIcon:', invSelect, 'window:', invWin)
		invSelect._send('loop:', 4, 'message:', -1)
		local0 = 0
		temp0 = 0
		while (temp0 < 52): # inline for
			if (temp1 = global9._send('at:', temp0)._send('owner:') == local1):
				temp1._send('realOwner:', temp1._send('owner:'), 'owner:', 0)
				if (local0.post('++') < 13):
					temp1._send('owner:', local1)
				#endif
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		if local0:
			global9._send('addAfter:', invTalk, invMore)
		#endif
		global9._send('delete:', invPrevious, 'showSelf:', local1)
	#end:method

#end:class or instance

@SCI.instance
class KqInv(Inv):
	#property vars (may be empty)
	normalHeading = r"""Alexander is carrying"""
	empty = r"""nothing."""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global9 = self
		self._send(
			'add:', map._send('setCursor:', 990, 1, 7, 'yourself:'), boringBook._send(
					'setCursor:', 990, 0, 0,
					'yourself:'
				), brick._send('setCursor:', 990, 0, 1, 'yourself:'), brush._send(
					'setCursor:', 990, 0, 2,
					'yourself:'
				), hair._send('setCursor:', 990, 0, 15, 'yourself:'), clothes._send(
					'setCursor:', 990, 0, 4,
					'yourself:'
				), coal._send('setCursor:', 990, 0, 5, 'yourself:'), deadMansCoin._send(
					'setCursor:', 990, 0, 6,
					'yourself:'
				), dagger._send('setCursor:', 990, 0, 7, 'yourself:'), coin._send(
					'setCursor:', 990, 0, 8,
					'yourself:'
				), egg._send('setCursor:', 990, 0, 10, 'yourself:'), skull._send(
					'setCursor:', 990, 3, 4,
					'yourself:'
				), feather._send('setCursor:', 990, 0, 11, 'yourself:'), flower._send(
					'setCursor:', 990, 0, 12,
					'yourself:'
				), flute._send('setCursor:', 990, 0, 13, 'yourself:'), gauntlet._send(
					'setCursor:', 990, 0, 14,
					'yourself:'
				), cassimaHair._send('setCursor:', 990, 0, 3, 'yourself:'), handkerchief._send(
					'setCursor:', 990, 1, 0,
					'yourself:'
				), holeInTheWall._send('setCursor:', 990, 1, 1, 'yourself:'), huntersLamp._send(
					'setCursor:', 990, 1, 2,
					'yourself:'
				), letter._send('setCursor:', 990, 1, 3, 'yourself:'), lettuce._send(
					'setCursor:', 990, 1, 4,
					'yourself:'
				), milk._send('setCursor:', 990, 1, 8, 'yourself:'), mint._send(
					'setCursor:', 990, 1, 9,
					'yourself:'
				), mirror._send('setCursor:', 990, 1, 10, 'yourself:'), newLamp._send(
					'setCursor:', 990, 1, 11,
					'yourself:'
				), nail._send('setCursor:', 990, 2, 0, 'yourself:'), nightingale._send(
					'setCursor:', 990, 2, 1,
					'yourself:'
				), ticket._send('setCursor:', 990, 3, 7, 'yourself:'), participle._send(
					'setCursor:', 990, 2, 3,
					'yourself:'
				), pearl._send('setCursor:', 990, 2, 4, 'yourself:'), peppermint._send(
					'setCursor:', 990, 2, 5,
					'yourself:'
				), note._send('setCursor:', 990, 2, 6, 'yourself:'), potion._send(
					'setCursor:', 990, 2, 7,
					'yourself:'
				), rabbitFoot._send('setCursor:', 990, 2, 8, 'yourself:'), ribbon._send(
					'setCursor:', 990, 2, 10,
					'yourself:'
				), riddleBook._send('setCursor:', 990, 2, 11, 'yourself:'), ring._send(
					'setCursor:', 990, 2, 12,
					'yourself:'
				), rose._send('setCursor:', 990, 2, 13, 'yourself:'), royalRing._send(
					'setCursor:', 990, 2, 14,
					'yourself:'
				), sacredWater._send('setCursor:', 990, 2, 15, 'yourself:'), scarf._send(
					'setCursor:', 990, 3, 0,
					'yourself:'
				), scythe._send('setCursor:', 990, 3, 1, 'yourself:'), shield._send(
					'setCursor:', 990, 3, 2,
					'yourself:'
				), skeletonKey._send('setCursor:', 990, 3, 3, 'yourself:'), spellBook._send(
					'setCursor:', 990, 3, 5,
					'yourself:'
				), teaCup._send('setCursor:', 990, 3, 6, 'yourself:'), poem._send(
					'setCursor:', 990, 2, 2,
					'yourself:'
				), tinderBox._send('setCursor:', 990, 3, 8, 'yourself:'), tomato._send(
					'setCursor:', 990, 3, 9,
					'yourself:'
				), sentence._send('setCursor:', 990, 3, 10, 'yourself:'), ink._send(
					'setCursor:', 990, 3, 12,
					'yourself:'
				), invLook._send('cursor:', cInvLook, 'yourself:'), invHand._send(
					'cursor:', cInvHand,
					'yourself:'
				), invSelect._send('cursor:', global20, 'yourself:'), invTalk._send(
					'cursor:', cInvTalk,
					'yourself:'
				), ok,
			'eachElementDo:', #highlightColor, 0,
			'eachElementDo:', #lowlightColor, invWin._send('back:'),
			'eachElementDo:', #init,
			'window:', invWin,
			'selectIcon:', invSelect,
			'okButton:', ok
		)
		super._send('init:', &rest)
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
		if (not (state & 0x2000)):
			curIcon = 0
		#endif
		(state &= 0xdfff)
		if self._send('show:', (param1 if argc else global0)):
			self._send('doit:')
		else:
			global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
		#endif
	#end:method

	@classmethod
	def hide(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (state & 0x0020):
			global8._send('pause:', 0)
			(state &= 0xffdf)
		#endif
		if (global169 and kernel.Platform(6) and (not kernel.Platform(5)) and empty):
			kernel.Graph(8, empty)
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
			if 
				(and
					global1._send('isHandsOn:')
					temp2 = global69._send('curIcon:')._send('cursor:')
				)
				global1._send('setCursor:', temp2)
			#endif
		else:
			if kernel.IsObject(temp3 = global69._send('curInvIcon:')):
				genericCursor._send(
					'view:', temp3._send('cursorView:'),
					'loop:', temp3._send('cursorLoop:'),
					'cel:', temp3._send('cursorCel:')
				)
			#endif
			if 
				(and
					global1._send('isHandsOn:')
					temp2 = global69._send('curIcon:')._send('cursor:')
				)
				global1._send('setCursor:', temp2)
			#endif
		#endif
		if ((not argc) or (not param1)):
			temp0 = 0
			while (temp0 < 52): # inline for
				if temp1 = self._send('at:', temp0)._send('realOwner:'):
					temp1._send('owner:', temp1._send('realOwner:'))
					temp1._send('realOwner:', 0)
				#endif
				# for:reinit
				temp0.post('++')
			#end:loop
			self._send('delete:', invMore, invPrevious)
		#endif
	#end:method

	@classmethod
	def highlight(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (param1._send('signal:') & 0x0004)):
			if kernel.IsObject(highlightedIcon):
				highlightedIcon._send('highlight:', 0)
			#endif
			highlightedIcon = param1._send('highlight:', 1)
		#endif
		(= temp1
			if (global169 and kernel.Platform(6)):
				(not kernel.Platform(5))
			else:
				0
			#endif
		)
		if ((argc >= 2) and param2):
			global1._send(
				'setCursor:', global19, 1, if temp1:
						(+
							(param1._send('nsLeft:') / 2)
							((param1._send('nsRight:') - param1._send('nsLeft:')) / 4)
						)
					else:
						(+
							param1._send('nsLeft:')
							((param1._send('nsRight:') - param1._send('nsLeft:')) / 2)
						)
					#endif, if temp1:
						((0 + (param1._send('nsBottom:') / 2)) - 8)
					else:
						(param1._send('nsBottom:') - 3)
					#endif
			)
		#endif
	#end:method

	@classmethod
	def advanceCurIcon():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = curIcon
		while 1:

			while
				temp0 = self._send('at:', (mod (self._send('indexOf:', temp0) + 1) size))._send(
					'isKindOf:', InvI
				):

			#end:loop
			if (temp0._send('cursor:') != -1):
				(break)
			#endif
		#end:loop
		curIcon = temp0
		if (curIcon == helpIconItem):
			curIcon._send('signal:', (| curIcon._send('signal:') 0x0010))
		else:
			curIcon._send('signal:', (curIcon._send('signal:') & 0xffef))
		#endif
		global1._send('setCursor:', curIcon._send('cursor:'))
	#end:method

	@classmethod
	def drawInvWindow(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = temp1 = temp2 = temp3 = temp4 = temp5 = 0
		(= temp72
			if (global169 and kernel.Platform(6)):
				(not kernel.Platform(5))
			else:
				0
			#endif
		)
		temp8 = self._send('first:')
		while temp8: # inline for
			if temp9 = kernel.NodeValue(temp8)._send('isKindOf:', InvI):
				if temp9._send('ownedBy:', param1):
					if temp72:
						temp9._send('view:', 972)
					else:
						temp9._send('view:', 970)
					#endif
					temp9._send('signal:', (temp9._send('signal:') & 0xfffb))
					temp0.post('++')
					temp6 = kernel.CelWide(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:'))
					temp7 = kernel.CelHigh(temp9._send('view:'), temp9._send('loop:'), temp9._send('cel:'))
					if (temp6 > temp2):
						temp2 = temp6
					#endif
					if (temp7 > temp1):
						temp1 = temp7
					#endif
				else:
					temp9._send('signal:', (| temp9._send('signal:') 0x0004))
				#endif
			else:
				if temp72:
					temp9._send('view:', 912)
				else:
					temp9._send('view:', 901)
				#endif
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
			if (global90 & 0x0002):
				global102._send('number:', 12, 'loop:', 1, 'play:')
			else:
				Print._send('addTextF:', r"""%s %s""", normalHeading, empty, 'init:')
			#endif
			return 0
		#endif
		if temp72:
			if ((local2 = (temp5 / temp2) * temp2) > temp5):
				local2.post('--')
			#endif
			(cond
				case (temp0 <= local2):
					temp16 = 1
					local2 = temp0
				#end:case
				case ((local2 * temp16 = (temp0 / local2)) < temp0):
					temp16.post('++')
				#end:case
			)
			(temp2 /= 2)
			(temp1 /= 2)
			temp10 = (4 + (temp5 /= 2))
		else:
			if ((temp16 = kernel.Sqrt(temp0) * temp16) > temp0):
				temp16.post('--')
			#endif
			if (temp16 > 3):
				temp16 = 3
			#endif
			if ((temp16 * local2 = (temp0 / temp16)) < temp0):
				local2.post('++')
			#endif
			temp10 = proc999_3((4 + temp5), (local2 * (4 + temp2)))
		#endif
		temp12 = ((190 - temp11 = ((temp16 * temp1) + 4)) / 2)
		temp13 = ((320 - temp10) / 2)
		temp14 = (temp12 + temp11)
		temp15 = (temp13 + temp10)
		if temp21 = self._send('window:'):
			temp21._send('top:', temp12, 'left:', temp13, 'right:', temp15, 'bottom:', temp14, 'open:')
			if temp72:
				(= empty
					kernel.Graph(15, (temp21._send('top:') + 10), temp21._send('left:'), (+
						temp21._send('bottom:')
						10
					), temp21._send('right:'))
				)
			else:
				empty = 0
			#endif
		#endif
		if temp72:
			(temp2 *= 2)
			(temp1 *= 2)
			(temp5 *= 2)
		#endif
		temp20 = local2
		if temp0:
			(= temp18
				(+
					2
					if temp21._send('respondsTo:', #yOffset):
						temp21._send('yOffset:')
					else:
						0
					#endif
				)
			)
			(= temp19
				(= temp17
					(+
						4
						if temp21._send('respondsTo:', #xOffset):
							temp21._send('xOffset:')
						else:
							0
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
							temp20 = local2
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
		if temp72:
			temp17 = ((((temp21._send('right:') - temp21._send('left:')) * 2) - temp5) / 2)
			temp11 = ((temp21._send('bottom:') - temp21._send('top:')) * 2)
		else:
			temp17 = (((temp21._send('right:') - temp21._send('left:')) - temp5) / 2)
			temp11 = (temp21._send('bottom:') - temp21._send('top:'))
		#endif
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
						if temp72:
							(temp18 += 10)
						#endif
					#endif
					temp9._send(
						'nsLeft:', temp17,
						'nsTop:', temp18,
						'nsBottom:', (temp18 + temp7),
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

#end:class or instance

@SCI.instance
class invWin(Kq6Window):
	#property vars (may be empty)
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(top -= temp0 = (kernel.CelHigh(901, 3, 0) / 2))
		(bottom += temp0)
		super._send('open:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class boringBook(Kq6InvItem):
	#property vars (may be empty)
	message = 42
	noun = 1
	owner = 270
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global9._send('hide:')
				global2._send('setScript:', 88)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class brick(Kq6InvItem):
	#property vars (may be empty)
	cel = 1
	message = 39
	noun = 4
	owner = 510
	
#end:class or instance

@SCI.instance
class brush(Kq6InvItem):
	#property vars (may be empty)
	cel = 2
	message = 29
	noun = 5
	owner = 280
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if state:
					global91._send('say:', noun, param1, 2, 0, 0, modNum)
				else:
					global91._send('say:', noun, param1, 1, 0, 0, modNum)
				#endif
			#end:case
			case 5:
				if state:
					global91._send('say:', noun, param1, 2, 0, 0, modNum)
				else:
					global91._send('say:', noun, param1, 1, 0, 0, modNum)
				#endif
			#end:case
			case 28:
				if state:
					global91._send('say:', noun, param1, 2, 0, 0, modNum)
				else:
					global91._send('say:', noun, param1, 1, 0, 0, modNum)
				#endif
			#end:case
			case 29:
				global91._send('say:', noun, param1, 0, 0, 0, modNum)
			#end:case
			case 44:
				teaCup._send('doVerb:', message)
			#end:case
			else:
				if state:
					global91._send('say:', noun, 0, 2, 0, 0, modNum)
				else:
					global91._send('say:', noun, 0, 1, 0, 0, modNum)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		loop = 3
		cel = 13
		state.post('++')
	#end:method

#end:class or instance

@SCI.instance
class hair(Kq6InvItem):
	#property vars (may be empty)
	cel = 15
	message = 15
	noun = 60
	owner = 530
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 51:
				skull._send('doVerb:', message)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clothes(Kq6InvItem):
	#property vars (may be empty)
	cel = 4
	message = 45
	noun = 6
	owner = 540
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if ((not global0._send('has:', 4)) and (not proc913_0(93))):
					KQ6Print._send(
						'font:', global22,
						'say:', 0, noun, param1, 0, 0, 0, 0, modNum,
						'posn:', -1, 10,
						'init:'
					)
					KQ6Print._send(
						'font:', global22,
						'say:', 0, noun, param1, 36, 0, 0, 0, modNum,
						'posn:', -1, 10,
						'init:'
					)
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			case 5:
				if 
					(or
						proc913_0(143)
						global0._send('has:', 4)
						global0._send('has:', 16)
						proc913_0(93)
					)
					global91._send('say:', noun, param1, 34, 0, 0, modNum)
				else:
					global9._send('hide:')
					proc913_1(143)
					global0._send('get:', 4)
					global1._send('givePoints:', 1)
					KQ6Print._send(
						'font:', global22,
						'say:', 0, noun, param1, 36, 0, 0, 0, modNum,
						'posn:', -1, 10,
						'init:'
					)
					pageCode._send('init:', local1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coal(Kq6InvItem):
	#property vars (may be empty)
	cel = 5
	message = 46
	noun = 7
	owner = 560
	
#end:class or instance

@SCI.instance
class deadMansCoin(Kq6InvItem):
	#property vars (may be empty)
	cel = 6
	message = 7
	noun = 9
	owner = 430
	
#end:class or instance

@SCI.instance
class dagger(Kq6InvItem):
	#property vars (may be empty)
	cel = 7
	message = 8
	noun = 10
	owner = 440
	
#end:class or instance

@SCI.instance
class coin(Kq6InvItem):
	#property vars (may be empty)
	cel = 8
	message = 40
	noun = 8
	owner = 200
	
#end:class or instance

@SCI.instance
class egg(Kq6InvItem):
	#property vars (may be empty)
	cel = 9
	message = 19
	noun = 52
	owner = 490
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 51:
				skull._send('doVerb:', message)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class skull(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 4
	message = 51
	noun = 63
	owner = 415
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 18):
			param1 = 15
		#endif
		match param1
			case 20:
				if (state & 0x0004):
					if (state & 0x0008):
						global91._send('say:', noun, 0, 0, 0, 0, modNum)
					else:
						global91._send('say:', noun, param1, 37, 0, 0, modNum)
					#endif
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			case 28:
				(cond
					case (not state):
						global91._send('say:', noun, param1, 38, 0, 0, modNum)
					#end:case
					case ((state & 0x0004) and (state & 0x0001) and (state & 0x0002)):
						if 
							(and
								(not global2._send('script:'))
								(global0._send('view:') == 900)
							)
							global9._send('hide:')
							global2._send('setScript:', 190)
						else:
							global91._send('say:', 7, 0, 16, 0, 0, 0)
						#endif
					#end:case
					case ((state & 0x0004) and (state & 0xfffe)):
						global91._send('say:', noun, param1, 39, 0, 0, modNum)
					#end:case
					case 
						(or
							((state & 0x0004) and (state & 0x0001))
							((state & 0x0004) and (state & 0x0002))
						):
						global91._send('say:', noun, param1, 41, 0, 0, modNum)
					#end:case
				)
			#end:case
			case 15:
				(cond
					case (not state):
						global91._send('say:', noun, 15, 38, 0, 0, modNum)
					#end:case
					case (state & 0x0004):
						global9._send('hide:')
						if global0._send('has:', 4):
							global0._send('put:', 4)
						else:
							global0._send('put:', 16)
						#endif
						global1._send('givePoints:', 1)
						if (state & 0x0001):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 41, 0, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 0, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
						(state |= 0x0002)
						pageCode._send('init:', local1)
					#end:case
				)
			#end:case
			case 19:
				(cond
					case (not state):
						global91._send('say:', noun, param1, 38, 0, 0, modNum)
					#end:case
					case ((state & 0x0004) and (state & 0x0002)):
						global9._send('hide:')
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 40, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
						global0._send('put:', 10)
						global1._send('givePoints:', 1)
						(state |= 0x0001)
						pageCode._send('init:', local1)
					#end:case
					case (state & 0x0004):
						global9._send('hide:')
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 39, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
						global0._send('put:', 10)
						global1._send('givePoints:', 1)
						(state |= 0x0001)
						pageCode._send('init:', local1)
					#end:case
				)
			#end:case
			case 1:
				(cond
					case (not state):
						global91._send('say:', noun, param1, 38, 0, 0, modNum)
					#end:case
					case ((state & 0x0004) and (state & 0x0001) and (state & 0x0002)):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 42, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 41, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 41, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
					#end:case
					case ((state & 0x0004) and (state & 0x0002)):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 40, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
					#end:case
					case ((state & 0x0004) and (state & 0x0001)):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 41, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 41, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 41, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
					#end:case
					case (state & 0x0004):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 39, 1, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						if (state & 0x0008):
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 3, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						else:
							KQ6Print._send(
								'font:', global22,
								'say:', 0, noun, param1, 39, 2, 0, 0, modNum,
								'posn:', -1, 10,
								'init:'
							)
						#endif
					#end:case
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('loop:', 3, 'cel:', 4, 'setCursor:', 990, 3, 4, 'state:', (self._send('state:') & 0xfff7))
		if 
			(and
				(global69._send('curIcon:') == global69._send('useIconItem:'))
				(global69._send('curInvIcon:') == self)
			)
			cursor._send('loop:', 3, 'cel:', 4)
			global1._send('setCursor:', cursor)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class feather(Kq6InvItem):
	#property vars (may be empty)
	cel = 11
	message = 30
	noun = 13
	owner = 300
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 44:
				teaCup._send('doVerb:', message)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flower(Kq6InvItem):
	#property vars (may be empty)
	cel = 12
	message = 47
	noun = 14
	owner = 300
	
#end:class or instance

@SCI.instance
class flute(Kq6InvItem):
	#property vars (may be empty)
	cel = 13
	message = 31
	noun = 15
	owner = 280
	
#end:class or instance

@SCI.instance
class gauntlet(Kq6InvItem):
	#property vars (may be empty)
	cel = 14
	message = 48
	noun = 16
	owner = 650
	
#end:class or instance

@SCI.instance
class cassimaHair(Kq6InvItem):
	#property vars (may be empty)
	cel = 3
	message = 18
	noun = 59
	owner = 210
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 51:
				skull._send('doVerb:', hair._send('message:'))
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class handkerchief(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	message = 50
	noun = 18
	owner = 680
	
#end:class or instance

@SCI.instance
class holeInTheWall(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 1
	message = 25
	noun = 19
	owner = 480
	
#end:class or instance

@SCI.instance
class huntersLamp(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 2
	message = 43
	noun = 23
	owner = 520
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, noun, param1, 0, 0, 0, 0, modNum,
					'init:'
				)
				(cond
					case (global161 == 0):
						global91._send('say:', noun, param1, 4, 0, 0, modNum)
					#end:case
					case (global161 == 1):
						global91._send('say:', noun, param1, 7, 0, 0, modNum)
					#end:case
					case (global161 == 4):
						global91._send('say:', noun, param1, 6, 0, 0, modNum)
					#end:case
					case (global161 == 6):
						global91._send('say:', noun, param1, 8, 0, 0, modNum)
					#end:case
					case (global161 == 5):
						global91._send('say:', noun, param1, 12, 0, 0, modNum)
					#end:case
					case (global161 == 15):
						global91._send('say:', noun, param1, 10, 0, 0, modNum)
					#end:case
					case (global161 == 7):
						global91._send('say:', noun, param1, 9, 0, 0, modNum)
					#end:case
					case (global161 == 2):
						global91._send('say:', noun, param1, 5, 0, 0, modNum)
					#end:case
					case (global161 == 3):
						global91._send('say:', noun, param1, 11, 0, 0, modNum)
					#end:case
				)
			#end:case
			case 28:
				(cond
					case (not proc913_0(77)):
						global91._send('say:', noun, param1, 15, 0, 0, modNum)
					#end:case
					case (global161 == 15):
						global91._send('say:', noun, param1, 10, 0, 0, modNum)
					#end:case
					case (global161 == 0):
						global91._send('say:', noun, param1, 4, 0, 0, modNum)
					#end:case
					case (global161 == 7):
						if 
							(and
								(not global2._send('script:'))
								(global0._send('view:') == 900)
							)
							global9._send('hide:')
							global2._send('setScript:', 190)
						else:
							global91._send('say:', 7, 0, 16, 0, 0, 0)
						#endif
					#end:case
					case 
						(or
							(global161 == (| global161 0x0001))
							(global161 == (| global161 0x0004))
							(global161 == (| global161 0x0002))
						):
						global91._send('say:', noun, param1, 14, 0, 0, modNum)
					#end:case
				)
			#end:case
			case 24:
				(cond
					case (not proc913_0(77)):
						global91._send('say:', noun, param1, 15, 0, 0, modNum)
					#end:case
					case (proc913_0(77) and (global161 == 1)):
						global91._send('say:', noun, param1, 18, 0, 0, modNum)
					#end:case
					case (proc913_0(77) and (global161 == 5)):
						global91._send('say:', noun, param1, 19, 0, 0, modNum)
					#end:case
					case (proc913_0(77) and (global161 == 0)):
						global9._send('hide:')
						global0._send('put:', 40)
						global1._send('givePoints:', 1)
						(global161 |= 0x0002)
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 16, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						global9._send('curIcon:', global9._send('selectIcon:'))
						global69._send('disable:', 4)
						pageCode._send('init:', local1)
					#end:case
					case (proc913_0(77) and (global161 == 4)):
						global9._send('hide:')
						global0._send('put:', 40)
						global1._send('givePoints:', 1)
						(global161 |= 0x0002)
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 17, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
						pageCode._send('init:', local1)
					#end:case
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class letter(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 3
	message = 61
	noun = 29
	owner = 780
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global9._send('hide:')
				global2._send('setScript:', 101, self)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lettuce(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 4
	message = 52
	noun = 20
	owner = 480
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state
			case 0:
				noun = 21
				message = 53
				self._send('setCursor:', 990, 1, cel = 5)
				if 
					(and
						(global69._send('curIcon:') == global69._send('useIconItem:'))
						(global69._send('curInvIcon:') == self)
					)
					genericCursor._send('view:', 990, 'loop:', cursorLoop, 'cel:', cursorCel)
					global1._send('setCursor:', genericCursor)
				#endif
				kernel.ScriptID(0, 7)._send('setReal:', global9._send('at:', 21), 30, 2)
				state.post('++')
			#end:case
			case 1:
				noun = 22
				message = 54
				self._send('setCursor:', 990, 1, cel = 6)
				if 
					(and
						(global69._send('curIcon:') == global69._send('useIconItem:'))
						(global69._send('curInvIcon:') == self)
					)
					genericCursor._send('view:', 990, 'loop:', cursorLoop, 'cel:', cursorCel)
					global1._send('setCursor:', genericCursor)
				#endif
				kernel.ScriptID(0, 7)._send('setReal:', global9._send('at:', 21), 30, 2)
				state.post('++')
			#end:case
			case 2:
				kernel.ScriptID(0, 7)._send('dispose:')
				noun = 20
				message = 52
				self._send('setCursor:', 990, 1, cel = 4)
				state = 0
				global0._send('put:', 21, 480)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class map(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 9
	message = 12
	noun = 31
	owner = 280
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			if proc999_5(global11, 200, 300, 260, 500, 550, 450):
				global9._send('hide:')
				self._send('cue:')
			else:
				global9._send('hide:')
				self._send('cue:')
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global11 == 450):
			global2._send('notify:', 1)
		else:
			if global0._send('looper:'):
				global0._send('looper:')._send('dispose:')
			#endif
			global2._send('setScript:', 130)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class milk(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 8
	message = 62
	noun = 32
	owner = 470
	
#end:class or instance

@SCI.instance
class mint(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 9
	message = 63
	noun = 33
	owner = 280
	
#end:class or instance

@SCI.instance
class mirror(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 10
	message = 13
	noun = 34
	owner = 540
	
#end:class or instance

@SCI.instance
class newLamp(Kq6InvItem):
	#property vars (may be empty)
	loop = 1
	cel = 11
	message = 57
	noun = 25
	owner = 240
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				if (not (noun == 66)):
					self._send('hideInv:', 1)
				#endif
				super._send('doVerb:', param1, &rest)
			#end:case
			case 24:
				self._send('hideInv:', 0)
				if proc913_0(77):
					global91._send('say:', noun, param1, 21, 0, 0, modNum)
				else:
					global91._send('say:', 57, param1, 15, 0, 0, modNum)
				#endif
			#end:case
			else:
				self._send('hideInv:', 0)
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class nail(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	message = 64
	noun = 35
	
#end:class or instance

@SCI.instance
class nightingale(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 1
	message = 37
	noun = 55
	owner = 280
	
#end:class or instance

@SCI.instance
class ticket(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 7
	message = 49
	noun = 17
	owner = 600
	
#end:class or instance

@SCI.instance
class participle(Kq6InvItem):
	#property vars (may be empty)
	loop = 6
	cel = 1
	message = 94
	noun = 57
	owner = 500
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doVerb:', param1, &rest)
		temp2 = (view == 972)
		if (not proc999_5(param1, 1, 94, 28, 13, 12)):
			if (global90 == 1):
				temp0 = 0
				while (temp0 < 20): # inline for
					temp1 = 0
					while (temp1 < 7000): # inline for
					#end:loop
					kernel.DrawCel(view, 5, kernel.Random(0, (-
						(14 if (not temp2) else 9)
						1
					)), nsLeft, nsTop, 15, 0, if temp2:
						global9._send('empty:')
					else:
						0
					#endif)
					# for:reinit
					temp0.post('++')
				#end:loop
			else:
				temp0 = 0
				while (temp0 < 500): # inline for
					temp1 = 0
					while (temp1 < 7000): # inline for
					#end:loop
					kernel.DrawCel(view, 5, kernel.Random(0, (-
						(14 if (not temp2) else 9)
						1
					)), nsLeft, nsTop, 15, 0, if temp2:
						global9._send('empty:')
					else:
						0
					#endif)
					if (kernel.DoAudio(6) == -1):
						(break)
					#endif
					# for:reinit
					temp0.post('++')
				#end:loop
			#endif
		#endif
		kernel.DrawCel(view, 5, 0, nsLeft, nsTop, 15, 0, if temp2:
			global9._send('empty:')
		else:
			0
		#endif)
	#end:method

#end:class or instance

@SCI.instance
class pearl(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 4
	message = 66
	noun = 37
	owner = 450
	
#end:class or instance

@SCI.instance
class peppermint(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 5
	message = 67
	noun = 38
	owner = 390
	
#end:class or instance

@SCI.instance
class note(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 6
	message = 65
	noun = 36
	owner = 210
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global9._send('hide:')
				global2._send('setScript:', 96, self)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class potion(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 7
	message = 14
	noun = 12
	owner = 480
	
#end:class or instance

@SCI.instance
class rabbitFoot(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 8
	message = 68
	noun = 39
	owner = 290
	
#end:class or instance

@SCI.instance
class ribbon(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 10
	message = 33
	noun = 40
	owner = 210
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if (global0._send('has:', 4) or global0._send('has:', 16) or proc913_0(112)):
					global91._send('say:', noun, param1, 0, 0, 0, modNum)
				else:
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'say:', 0, noun, param1, 0, 0, 0, 0, 907,
						'init:'
					)
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'say:', 0, noun, param1, 33, 0, 0, 0, 907,
						'init:'
					)
				#endif
			#end:case
			case 5:
				if 
					(or
						proc913_0(143)
						global0._send('has:', 4)
						global0._send('has:', 16)
						proc913_0(112)
					)
					global91._send('say:', noun, param1, 34, 0, 0, modNum)
				else:
					global9._send('hide:')
					proc913_1(143)
					global0._send('get:', 16)
					global1._send('givePoints:', 1)
					KQ6Print._send(
						'font:', global22,
						'say:', 0, noun, param1, 33, 0, 0, 0, modNum,
						'posn:', -1, 10,
						'init:'
					)
					pageCode._send('init:', local1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riddleBook(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 11
	message = 27
	noun = 2
	owner = 460
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			global9._send('hide:')
			global2._send('setScript:', 90)
		else:
			self._send('hideInv:', 0)
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class ring(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 12
	message = 69
	noun = 41
	owner = 540
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(global0._send('view:') == 900)
				User._send('canControl:')
				(not proc999_5(global11, 580, 390, 320, 300, 270, 490))
				(not global2._send('script:'))
			)
			global2._send('setScript:', kernel.ScriptID(84, 0))
		else:
			kernel.ScriptID(0, 5)._send('setReal:', self, 10, 0, 0)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class rose(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 13
	message = 71
	noun = 43
	owner = 530
	
#end:class or instance

@SCI.instance
class royalRing(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 14
	message = 70
	noun = 42
	owner = 200
	
#end:class or instance

@SCI.instance
class sacredWater(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 15
	message = 24
	noun = 56
	owner = 380
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (param1 == 43):
				huntersLamp._send('doVerb:', message)
			#end:case
			case proc999_5(57, 58, 59, 60, 96, 56):
				newLamp._send('doVerb:', message)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class scarf(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	message = 72
	noun = 45
	owner = 490
	
#end:class or instance

@SCI.instance
class scythe(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 1
	message = 16
	noun = 46
	owner = 560
	
#end:class or instance

@SCI.instance
class shield(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 2
	message = 17
	noun = 47
	owner = 408
	
#end:class or instance

@SCI.instance
class skeletonKey(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 3
	message = 35
	noun = 48
	owner = 670
	
#end:class or instance

@SCI.instance
class spellBook(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 5
	message = 28
	noun = 3
	owner = 270
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if ((global0._send('view:') == 900) and (not global2._send('script:'))):
					global9._send('hide:')
					global2._send('setScript:', 190)
				else:
					global91._send('say:', 7, 0, 16, 0, 0, 0)
				#endif
			#end:case
			case 43:
				huntersLamp._send('doVerb:', message)
			#end:case
			case 51:
				skull._send('doVerb:', message)
			#end:case
			case 44:
				teaCup._send('doVerb:', message)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class teaCup(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 6
	message = 44
	noun = 53
	owner = 480
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				KQ6Print._send(
					'font:', global22,
					'say:', 0, noun, param1, 0, 0, 0, 0, modNum,
					'posn:', -1, 10,
					'init:'
				)
				(cond
					case proc913_0(23):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 32, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
					case proc913_0(22):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 31, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
					case 
						(and
							(not proc913_0(68))
							(not proc913_0(58))
							(not proc913_0(22))
						):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 27, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
					case 
						(and
							proc913_0(68)
							(not proc913_0(58))
							(not proc913_0(22))
						):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 28, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
					case 
						(proc913_0(68) and proc913_0(58) and (not proc913_0(22))):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 30, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
					case 
						(and
							(not proc913_0(68))
							proc913_0(58)
							(not proc913_0(22))
						):
						KQ6Print._send(
							'font:', global22,
							'say:', 0, noun, param1, 29, 0, 0, 0, modNum,
							'posn:', -1, 10,
							'init:'
						)
					#end:case
				)
			#end:case
			case 28:
				(cond
					case proc913_0(23):
						global91._send('say:', noun, param1, 32, 0, 0, modNum)
					#end:case
					case proc913_0(22):
						global91._send('say:', noun, param1, 31, 0, 0, modNum)
					#end:case
					case 
						(or
							(and
								(not proc913_0(68))
								(not proc913_0(58))
								(not proc913_0(22))
							)
							(and
								proc913_0(68)
								(not proc913_0(58))
								(not proc913_0(22))
							)
							(and
								proc913_0(68)
								proc913_0(58)
								(not proc913_0(22))
							)
							(and
								(not proc913_0(68))
								proc913_0(58)
								(not proc913_0(22))
							)
						):
						global91._send('say:', noun, param1, 28, 0, 0, modNum)
					#end:case
				)
			#end:case
			case 29:
				(cond
					case proc913_0(23):
						global91._send('say:', noun, param1, 32, 0, 0, modNum)
					#end:case
					case proc913_0(22):
						global91._send('say:', noun, param1, 31, 0, 0, modNum)
					#end:case
					case 
						(and
							(not proc913_0(68))
							(not proc913_0(58))
							(not proc913_0(22))
						):
						global91._send('say:', noun, param1, 27, 0, 0, modNum)
					#end:case
					case 
						(or
							(and
								proc913_0(68)
								(not proc913_0(58))
								(not proc913_0(22))
							)
							(and
								proc913_0(68)
								proc913_0(58)
								(not proc913_0(22))
							)
							(and
								(not proc913_0(68))
								proc913_0(58)
								(not proc913_0(22))
							)
						):
						global91._send('say:', noun, param1, 28, 0, 0, modNum)
					#end:case
				)
			#end:case
			case 30:
				(cond
					case 
						(and
							(not proc913_0(68))
							(not proc913_0(58))
							(not proc913_0(22))
						):
						global91._send('say:', noun, param1, 27, 0, 0, modNum)
					#end:case
					case 
						(or
							(and
								proc913_0(68)
								(not proc913_0(58))
								(not proc913_0(22))
							)
							(and
								(not proc913_0(68))
								proc913_0(58)
								(not proc913_0(22))
							)
						):
						global91._send('say:', noun, param1, 28, 0, 0, modNum)
					#end:case
					case 
						(proc913_0(68) and proc913_0(58) and (not proc913_0(22))):
						if 
							(and
								(global0._send('view:') == 900)
								(not global2._send('script:'))
							)
							global2._send('setScript:', 915)
						else:
							global91._send('say:', 7, 0, 16, 0, 0, 0)
						#endif
					#end:case
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poem(Kq6InvItem):
	#property vars (may be empty)
	loop = 2
	cel = 2
	message = 32
	noun = 30
	owner = 270
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global9._send('hide:')
				global2._send('setScript:', 97, self)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tinderBox(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 8
	message = 20
	noun = 54
	owner = 280
	
#end:class or instance

@SCI.instance
class tomato(Kq6InvItem):
	#property vars (may be empty)
	loop = 6
	message = 34
	noun = 44
	owner = 480
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not proc999_5(param1, 1, 34)):
			temp2 = (view == 972)
			if (param1 == 2):
				global91._send('say:', noun, param1, kernel.Random(45, 48), 0, 0, 907)
			else:
				super._send('doVerb:', param1, &rest)
			#endif
			if (not proc999_5(param1, 28, 13, 12)):
				if (global90 == 1):
					temp0 = 0
					while (temp0 < 25): # inline for
						temp1 = 0
						while (temp1 < 7000): # inline for
						#end:loop
						kernel.DrawCel(view, 4, kernel.Random(0, (-
							(14 if (not temp2) else 9)
							1
						)), nsLeft, nsTop, 15, 0, if temp2:
							global9._send('empty:')
						else:
							0
						#endif)
						# for:reinit
						temp0.post('++')
					#end:loop
				else:
					temp0 = 0
					while (temp0 < 80): # inline for
						temp1 = 0
						while (temp1 < 7000): # inline for
						#end:loop
						kernel.DrawCel(view, 4, kernel.Random(0, (-
							(14 if (not temp2) else 9)
							1
						)), nsLeft, nsTop, 15, 0, if temp2:
							global9._send('empty:')
						else:
							0
						#endif)
						if (kernel.DoAudio(6) == -1):
							(break)
						#endif
						# for:reinit
						temp0.post('++')
					#end:loop
				#endif
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
		kernel.DrawCel(view, 4, 0, nsLeft, nsTop, 15, 0, if temp2:
			global9._send('empty:')
		else:
			0
		#endif)
	#end:method

#end:class or instance

@SCI.instance
class sentence(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 10
	message = 85
	noun = 11
	owner = 450
	
#end:class or instance

@SCI.instance
class ink(Kq6InvItem):
	#property vars (may be empty)
	loop = 3
	cel = 12
	message = 83
	noun = 68
	owner = 240
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 1, 5):
			if proc913_0(116):
				global91._send('say:', noun, param1, 50, 0, 0, 907)
			else:
				global91._send('say:', noun, param1, 0, 0, 0, 907)
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

class InvIconItem(IconI):
	#property vars (may be empty)
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
		kernel.DrawCel(view, loop, cel, nsLeft, nsTop, -1, 0, if 
			(global169 and kernel.Platform(6) and (not kernel.Platform(5)))
			global9._send('empty:')
		else:
			0
		#endif)
		if (global77 and global77._send('respondsTo:', #stop)):
			global77._send('stop:')
		#endif
	#end:method

	@classmethod
	def select(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global169 and kernel.Platform(6) and (not kernel.Platform(5)) and global9._send('empty:')):
			temp3 = global9._send('empty:')
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
	def highlight():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not global169) or kernel.Platform(5)):
			nsLeft.post('--')
			nsTop.post('--')
			(nsRight += 2)
			super._send('highlight:', &rest)
			(nsRight -= 2)
			nsTop.post('++')
			nsLeft.post('++')
		#endif
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= temp0
			if (global169 and kernel.Platform(6)):
				(not kernel.Platform(5))
			else:
				0
			#endif
		)
		(return
			if 
				(>=
					param1._send('x:')
					if temp0:
						(nsLeft / 2)
					else:
						nsLeft
					#endif
				)
				if 
					(>=
						param1._send('y:')
						if temp0:
							(nsTop / 2)
						else:
							nsTop
						#endif
					)
					(and
						(<=
							param1._send('x:')
							if temp0:
								(nsRight / 2)
							else:
								nsRight
							#endif
						)
						(<=
							param1._send('y:')
							if temp0:
								(nsBottom / 2)
							else:
								nsBottom
							#endif
						)
					)
				#endif
			else:
				0
			#endif
		)
	#end:method

#end:class or instance

@SCI.instance
class ok(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 3
	cel = 0
	nsLeft = 40
	signal = 67
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('highlightColor:', 0, 'lowlightColor:', 19)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class invLook(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 2
	cel = 0
	message = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('highlightColor:', 0, 'lowlightColor:', 19)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class invHand(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 0
	cel = 0
	message = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('highlightColor:', 0, 'lowlightColor:', 19)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class invSelect(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 4
	cel = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('highlightColor:', 0, 'lowlightColor:', 19)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class invTalk(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 5
	cel = 0
	message = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('highlightColor:', 0, 'lowlightColor:', 19)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class invMore(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 6
	cel = 0
	lowlightColor = 19
	
	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local0 < 13):
			loop = 8
		else:
			loop = 6
		#endif
		super._send('show:', &rest)
	#end:method

	@classmethod
	def select():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if super._send('select:', &rest):
			if (local0 >= 13):
				temp0 = 0
				while (temp0 < 52): # inline for
					if (temp1 = global9._send('at:', temp0)._send('realOwner:') == local1):
						if (temp1._send('owner:') == local1):
							temp1._send('owner:', 1)
						else:
							temp1._send('owner:', local1)
						#endif
					#endif
					# for:reinit
					temp0.post('++')
				#end:loop
				global9._send('state:', (| global9._send('state:') 0x2000))
				global9._send(
					'hide:', 1,
					'highlightedIcon:', ok,
					'addAfter:', invTalk, invPrevious,
					'delete:', invMore,
					'showSelf:', local1
				)
				return 0
			else:
				global91._send('say:', 67, 0, 49, 0, 0, 907)
				return 0
			#endif
		else:
			0
		#endif
	#end:method

#end:class or instance

@SCI.instance
class invPrevious(InvIconItem):
	#property vars (may be empty)
	view = 901
	loop = 7
	cel = 0
	lowlightColor = 19
	
	@classmethod
	def select():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if super._send('select:', &rest):
			temp0 = 0
			while (temp0 < 52): # inline for
				if (temp1 = global9._send('at:', temp0)._send('realOwner:') == local1):
					if (temp1._send('owner:') == 1):
						temp1._send('owner:', local1)
					else:
						temp1._send('owner:', 0)
					#endif
				#endif
				# for:reinit
				temp0.post('++')
			#end:loop
			global9._send('state:', (| global9._send('state:') 0x2000))
			global9._send(
				'hide:', 1,
				'highlightedIcon:', ok,
				'addAfter:', invTalk, invMore,
				'delete:', invPrevious,
				'showSelf:', local1
			)
			return 0
		else:
			0
		#endif
	#end:method

#end:class or instance

@SCI.instance
class cInvLook(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 1
	
#end:class or instance

@SCI.instance
class cInvHand(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 2
	
#end:class or instance

@SCI.instance
class cInvTalk(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 3
	
#end:class or instance

@SCI.instance
class genericCursor(Cursor):
	#property vars (may be empty)
#end:class or instance

