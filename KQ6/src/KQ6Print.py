#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 104
import sci_sh
import kernel
import Main
import Interface
import Kq6Talker
import Print
import Dialog
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None


@SCI.instance
class myDialog(Dialog):
	#property vars (may be empty)
	@classmethod
	def check():
		if (super._send('check:') or (kernel.DoAudio(6) == -1)):
			return 1
		#endif
	#end:method

	@classmethod
	def handleEvent():
		if (kernel.DoAudio(6) == -1):
			return -2
		else:
			super._send('handleEvent:', &rest)
			return
		#endif
	#end:method

	@classmethod
	def dispose():
		if (not (kernel.DoAudio(6) == -1)):
			kernel.DoAudio(3)
		#endif
		super._send('dispose:', &rest)
	#end:method

#end:class or instance

class KQ6Print(Print):
	#property vars (may be empty)
	repressText = 0
	
	@classmethod
	def say(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global90 & 0x0002):
			local1 = param2[0]
			local2 = param2[1]
			local3 = param2[2]
			local4 = (param2[3] if param2[3] else 1)
			temp0 = 0
			temp1 = 0
			local0 = global11
			if (argc >= 5):
				temp0 = param2[4]
				if (argc >= 6):
					temp1 = param2[5]
					if (argc >= 7):
						local0 = param2[6]
					#endif
				#endif
			#endif
			if (param1 == 1):
				self._send('addText:', param2, &rest)
			else:
				repressText = 1
			#endif
		else:
			self._send('addText:', param2, &rest)
		#endif
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		caller = 0
		if argc:
			caller = param1
		#endif
		if (argc > 1):
			self._send('addText:', &rest)
		#endif
		if (not modeless):
			if (not kernel.IsObject(global92)):
				global92 = EventHandler._send('new:')._send('name:', r"""prints""")
			#endif
			global92._send('add:', self)
		#endif
		if (global90 & 0x0002):
			kernel.DoAudio(2, local0, local1, local2, local3, local4)
		#endif
		if modeless:
			global69._send('disable:', 6)
		#endif
		self._send('showSelf:')
	#end:method

	@classmethod
	def dispose():
		if modeless:
			global69._send('enable:', 6)
		#endif
		repressText = 0
		if (global90 & 0x0002):
			kernel.DoAudio(3)
		#endif
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def addText(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		repressText = 0
		if (not dialog):
			dialog = Dialog._send('new:')
		#endif
		if (font == -1):
			font = global22
		#endif
		if (argc > 3):
			temp0 = param1[0]
			temp1 = param1[1]
			temp2 = param1[2]
			temp3 = (param1[3] if param1[3] else 1)
			temp4 = 0
			temp5 = 0
			temp6 = global11
			if (argc >= 5):
				temp4 = param1[4]
				if (argc >= 6):
					temp5 = param1[5]
					if (argc >= 7):
						temp6 = param1[6]
					#endif
				#endif
			#endif
			if temp8 = kernel.Message(2, temp6, temp0, temp1, temp2, temp3):
				temp7 = kernel.Memory(1, temp8)
				if kernel.Message(0, temp6, temp0, temp1, temp2, temp3, temp7):
					temp9 = kernel.StrAt(temp7, 0)
					if (>= 90 temp9 65):
						kernel.StrAt(temp7, 0, 9)
						temp10 = (0 + ((temp9 - 65) / 13))
						temp11 = (mod (temp9 - 65) 13)
						dialog._send(
							'add:', DText._send('new:')._send(
									'text:', temp7,
									'font:', font,
									'mode:', mode,
									'setSize:', width,
									'moveTo:', (4 + temp4), (+ 4 temp5 7),
									'yourself:'
								),
							'add:', DIcon._send('new:')._send(
									'view:', Kq6Narrator._send('strView:'),
									'loop:', temp10,
									'cel:', temp11,
									'setSize:',
									'moveTo:', (temp4 + 4), (temp5 + 4),
									'yourself:'
								),
							'setSize:'
						)
					else:
						dialog._send(
							'add:', DText._send('new:')._send(
									'text:', temp7,
									'font:', font,
									'mode:', mode,
									'setSize:', width,
									'moveTo:', (4 + temp4), (4 + temp5),
									'yourself:'
								),
							'setSize:'
						)
					#endif
				#endif
			#endif
		else:
			temp4 = 0
			temp5 = 0
			if (argc >= 2):
				temp4 = param1[1]
				if (argc >= 3):
					temp5 = param1[2]
				#endif
			#endif
			temp7 = kernel.Memory(1, (kernel.StrLen(param1[0]) + 1))
			kernel.StrCpy(temp7, param1[0])
			dialog._send(
				'add:', DText._send('new:')._send(
						'text:', temp7,
						'font:', font,
						'mode:', mode,
						'setSize:', width,
						'moveTo:', (4 + temp4), (4 + temp5),
						'yourself:'
					),
				'setSize:'
			)
		#endif
	#end:method

	@classmethod
	def showSelf():
		if 
			(and
				(= temp6
					if repressText:
						(global90 & 0x0002)
					#endif
				)
				global1._send('isHandsOn:')
			)
			temp5 = global19
			global1._send('setCursor:', global21)
		else:
			temp5 = 0
		#endif
		if saveCursor:
			global1._send('setCursor:', 999)
		#endif
		if (not dialog):
			if temp6:
				dialog = myDialog
			else:
				dialog = Dialog._send('new:')
			#endif
		#endif
		dialog._send(
			'window:', (window if window else global38),
			'name:', r"""PODialog""",
			'caller:', self
		)
		dialog._send('text:', title, 'time:', ticks, 'setSize:')
		dialog._send('center:')
		(= temp3
			if (x == -1):
				dialog._send('nsLeft:')
			else:
				x
			#endif
		)
		(= temp4
			if (y == -1):
				dialog._send('nsTop:')
			else:
				y
			#endif
		)
		dialog._send('moveTo:', temp3, temp4)
		temp1 = kernel.GetPort()
		if (not repressText):
			dialog._send('open:', (4 if title else 0), 15)
		#endif
		if modeless:
			global41 = kernel.GetPort()
			kernel.SetPort(temp1)
			global25 = dialog
			if temp5:
				global1._send('handsOn:')
			#endif
		else:
			global8._send('pause:', 1)
			(cond
				case (not temp0 = first):
					if 
						(and
							temp0 = dialog._send('firstTrue:', #checkState, 1)
							(not dialog._send('firstTrue:', #checkState, 2))
						)
						temp0._send('state:', (| temp0._send('state:') 0x0002))
					#endif
				#end:case
				case (not kernel.IsObject(temp0)):
					temp0 = dialog._send('at:', temp0)
				#end:case
			)
			retValue = dialog._send('doit:', temp0)
			kernel.SetPort(temp1)
			(cond
				case (retValue == -1):
					retValue = 0
				#end:case
				case (kernel.IsObject(retValue) and retValue._send('isKindOf:', DButton)):
					retValue = retValue._send('value:')
				#end:case
				case (not dialog._send('theItem:')):
					retValue = 1
				#end:case
			)
			if saveCursor:
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
			#endif
			dialog._send('dispose:')
			if temp5:
				global1._send('setCursor:', temp5)
			#endif
			return retValue
		#endif
	#end:method

#end:class or instance

