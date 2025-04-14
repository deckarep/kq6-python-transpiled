#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 987
import sci_sh
import kernel
import Main
import Interface
import Dialog
import Window

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7


class Gauge(Dialog):
	#property vars (may be empty)
	description = 0
	higher = r"""up"""
	lower = r"""down"""
	normal = 7
	minimum = 0
	maximum = 15
	
	@classmethod
	def init(param1 = None, *rest):
		window = SysWindow
		self._send('update:', param1)
		local2 = DButton._send('new:')._send('text:', lower, 'moveTo:', 4, 4, 'setSize:')
		self._send('add:', local2, 'setSize:')
		local3 = DText._send('new:')._send(
			'text:', @local7,
			'moveTo:', (local2._send('nsRight:') + 4), 4,
			'font:', 0,
			'setSize:'
		)
		self._send('add:', local3, 'setSize:')
		local1 = DButton._send('new:')._send(
			'text:', higher,
			'moveTo:', (local3._send('nsRight:') + 4), 4,
			'setSize:'
		)
		self._send('add:', local1, 'setSize:')
		(nsBottom += 8)
		local4 = DButton._send('new:')._send('text:', r"""OK""", 'setSize:', 'moveTo:', 4, nsBottom)
		local5 = DButton._send('new:')._send(
			'text:', r"""Normal""",
			'setSize:',
			'moveTo:', (local4._send('nsRight:') + 4), nsBottom
		)
		local6 = DButton._send('new:')._send(
			'text:', r"""Cancel""",
			'setSize:',
			'moveTo:', (local5._send('nsRight:') + 4), nsBottom
		)
		self._send('add:', local4, local5, local6, 'setSize:')
		temp0 = ((nsRight - local6._send('nsRight:')) - 4)
		local0 = DText._send('new:')._send(
			'text:', description,
			'font:', global23,
			'setSize:', (nsRight - 8),
			'moveTo:', 4, 4
		)
		temp1 = (local0._send('nsBottom:') + 4)
		self._send('add:', local0)
		local1._send('move:', 0, temp1)
		local2._send('move:', 0, temp1)
		local3._send('move:', 0, temp1)
		local4._send('move:', temp0, temp1)
		local5._send('move:', temp0, temp1)
		local6._send('move:', temp0, temp1)
		self._send('setSize:', 'center:', 'open:', 4, 15)
	#end:method

	@classmethod
	def doit(param1 = None, *rest):
		self._send('init:', param1)
		temp1 = param1
		while True: #repeat
			self._send('update:', temp1)
			local3._send('draw:')
			(cond
				case (temp0 = super._send('doit:', local4) == local1):
					if (temp1 < maximum):
						temp1.post('++')
					#endif
				#end:case
				case (temp0 == local2):
					if (temp1 > minimum):
						temp1.post('--')
					#endif
				#end:case
				case (temp0 == local4):
					(break)
				#end:case
				case (temp0 == local5):
					temp1 = normal
				#end:case
				case ((temp0 == 0) or (temp0 == local6)):
					temp1 = param1
					(break)
				#end:case
			)
		#end:loop
		self._send('dispose:')
		return temp1
	#end:method

	@classmethod
	def update(param1 = None, *rest):
		temp1 = (maximum - minimum)
		temp0 = 0
		while (temp0 < temp1): # inline for
			kernel.StrAt(@local7, temp0, (6 if (temp0 < param1) else 7))
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		match param1._send('type:')
			case 4:
				match param1._send('message:')
					case 19200:
						param1._send('claimed:', 1)
						return local2
					#end:case
					case 19712:
						param1._send('claimed:', 1)
						return local1
					#end:case
				#end:match
			#end:case
			case 64:
				match param1._send('message:')
					case 7:
						param1._send('claimed:', 1)
						return local2
					#end:case
					case 3:
						param1._send('claimed:', 1)
						return local1
					#end:case
				#end:match
			#end:case
		#end:match
		super._send('handleEvent:', param1)
	#end:method

#end:class or instance

