#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 987
import sci_sh
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
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		window = SysWindow
		(self update: param1)
		(local2 = (DButton new:) text: lower moveTo: 4 4 setSize:)
		(self add: local2 setSize:)
		(local3 = (DText new:)
			text: @local7
			moveTo: ((local2 nsRight:) + 4) 4
			font: 0
			setSize:
		)
		(self add: local3 setSize:)
		(local1 = (DButton new:)
			text: higher
			moveTo: ((local3 nsRight:) + 4) 4
			setSize:
		)
		(self add: local1 setSize:)
		(nsBottom += 8)
		(local4 = (DButton new:) text: r"""OK""" setSize: moveTo: 4 nsBottom)
		(local5 = (DButton new:)
			text: r"""Normal"""
			setSize:
			moveTo: ((local4 nsRight:) + 4) nsBottom
		)
		(local6 = (DButton new:)
			text: r"""Cancel"""
			setSize:
			moveTo: ((local5 nsRight:) + 4) nsBottom
		)
		(self add: local4 local5 local6 setSize:)
		temp0 = ((nsRight - (local6 nsRight:)) - 4)
		(local0 = (DText new:)
			text: description
			font: global23
			setSize: (nsRight - 8)
			moveTo: 4 4
		)
		temp1 = ((local0 nsBottom:) + 4)
		(self add: local0)
		(local1 move: 0 temp1)
		(local2 move: 0 temp1)
		(local3 move: 0 temp1)
		(local4 move: temp0 temp1)
		(local5 move: temp0 temp1)
		(local6 move: temp0 temp1)
		(self setSize: center: open: 4 15)
	#end:method

	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self init: param1)
		temp1 = param1
		while True: #repeat
			(self update: temp1)
			(local3 draw:)
			(cond
				case (temp0 = (super doit: local4) == local1):
					if (temp1 < maximum):
						temp1++
					#endif
				#end:case
				case (temp0 == local2):
					if (temp1 > minimum):
						temp1--
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
		(self dispose:)
		return temp1
	#end:method

	@classmethod
	def update(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (maximum - minimum)
		temp0 = 0
		while (temp0 < temp1): # inline for
			(StrAt @local7 temp0 (6 if (temp0 < param1) else 7))
			# for:reinit
			temp0++
		#end:loop
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (param1 type:)
			case 4:
				match (param1 message:)
					case 19200:
						(param1 claimed: 1)
						return local2
					#end:case
					case 19712:
						(param1 claimed: 1)
						return local1
					#end:case
				#end:match
			#end:case
			case 64:
				match (param1 message:)
					case 7:
						(param1 claimed: 1)
						return local2
					#end:case
					case 3:
						(param1 claimed: 1)
						return local1
					#end:case
				#end:match
			#end:case
		#end:match
		(super handleEvent: param1)
	#end:method

#end:class or instance

