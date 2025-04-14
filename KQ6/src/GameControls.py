#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 978
import sci_sh
import kernel
import Main
import Print
import IconBar

class GameControls(IconBar):
	#property vars (may be empty)
	height = 200
	state = 0
	okButton = 0
	
	@classmethod
	def show():
		global8._send('pause:')
		if (global77 and global77._send('respondsTo:', #stop)):
			global77._send('stop:')
		#endif
		(state |= 0x0020)
		if kernel.IsObject(window):
			window._send('open:')
		else:
			(= window
				global38._send('new:')._send(
					'top:', 46,
					'left:', 24,
					'bottom:', 155,
					'right:', 296,
					'priority:', 15,
					'open:',
					'yourself:'
				)
			)
		#endif
		temp0 = 30
		temp1 = 30
		temp2 = kernel.FirstNode(elements)
		while temp2: # inline for
			temp3 = kernel.NextNode(temp2)
			if (not kernel.IsObject(temp4 = kernel.NodeValue(temp2))):
				return
			#endif
			if ((not (temp4._send('signal:') & 0x0080)) and (temp4._send('nsRight:') <= 0)):
				temp4._send('show:', temp0, temp1)
				temp0 = (20 + temp4._send('nsRight:'))
			else:
				temp4._send('show:')
			#endif
			# for:reinit
			temp2 = temp3
		#end:loop
		if (not okButton):
			okButton = kernel.NodeValue(self._send('first:'))
		#endif
		if curIcon:
			global1._send(
				'setCursor:', global19, 1, (+
						curIcon._send('nsLeft:')
						((curIcon._send('nsRight:') - curIcon._send('nsLeft:')) / 2)
					), (curIcon._send('nsBottom:') - 3)
			)
		#endif
		self._send('doit:', 'hide:')
	#end:method

	@classmethod
	def dispatchEvent(param1 = None, *rest):
		temp53 = param1._send('type:')
		temp54 = param1._send('message:')
		(cond
			case (temp53 == 8192):
				if 
					(and
						temp1 = self._send('firstTrue:', #onMe, param1)
						temp1._send('helpVerb:')
					)
					temp2 = kernel.GetPort()
					if global38._send('respondsTo:', #eraseOnly):
						temp0 = global38._send('eraseOnly:')
						global38._send('eraseOnly:', 1)
						Print._send(
							'font:', global22,
							'width:', 250,
							'addText:', temp1._send('noun:'), temp1._send('helpVerb:'), 0, 1, 0, 0, temp1._send(
									'modNum:'
								),
							'init:'
						)
						global38._send('eraseOnly:', temp0)
					else:
						Print._send(
							'font:', global22,
							'width:', 250,
							'addText:', temp1._send('noun:'), temp1._send('helpVerb:'), 0, 1, 0, 0, temp1._send(
									'modNum:'
								),
							'init:'
						)
					#endif
					kernel.SetPort(temp2)
				#endif
				if helpIconItem:
					helpIconItem._send('signal:', (helpIconItem._send('signal:') & 0xffef))
				#endif
				global1._send('setCursor:', 999)
				return 0
			#end:case
			case (temp53 & 0x0040):
				match temp54
					case 5:
						(cond
							case 
								(and
									kernel.IsObject(highlightedIcon)
									highlightedIcon._send('respondsTo:', #retreat)
								):
								highlightedIcon._send('retreat:')
								return 0
							#end:case
							case 
								(or
									(not kernel.IsObject(highlightedIcon))
									(highlightedIcon._send('signal:') & 0x0100)
								):
								self._send('advance:')
								return 0
							#end:case
						)
					#end:case
					case 1:
						(cond
							case 
								(and
									kernel.IsObject(highlightedIcon)
									highlightedIcon._send('respondsTo:', #advance)
								):
								highlightedIcon._send('advance:')
								return 0
							#end:case
							case 
								(or
									(not kernel.IsObject(highlightedIcon))
									(highlightedIcon._send('signal:') & 0x0100)
								):
								self._send('retreat:')
								return 0
							#end:case
						)
					#end:case
					else:
						super._send('dispatchEvent:', param1)
					#end:else
				#end:match
			#end:case
			else:
				super._send('dispatchEvent:', param1)
			#end:else
		)
	#end:method

	@classmethod
	def select(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		param1._send('select:', ((argc >= 2) and param2))
	#end:method

	@classmethod
	def advanceCurIcon():#end:method

	@classmethod
	def swapCurIcon():#end:method

	@classmethod
	def hide():
		if window:
			window._send('dispose:')
			window = 0
		#endif
		if (state & 0x0020):
			global8._send('pause:', 0)
			(state &= 0xffdf)
		#endif
	#end:method

#end:class or instance

class ControlIcon(IconI):
	#property vars (may be empty)
	theObj = 0
	selector = 0
	
	@classmethod
	def doit():
		if theObj:
			if (signal & 0x0040):
				(global63 if global63 else GameControls)._send('hide:')
			#endif
			global1._send('panelObj:', theObj, 'panelSelector:', selector)
		#endif
	#end:method

#end:class or instance

