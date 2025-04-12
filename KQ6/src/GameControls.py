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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global8 pause:)
		if (global77 and (global77 respondsTo: #stop)):
			(global77 stop:)
		#endif
		(state |= 0x0020)
		if kernel.IsObject(window):
			(window open:)
		else:
			(= window
				((global38 new:)
					top: 46
					left: 24
					bottom: 155
					right: 296
					priority: 15
					open:
					yourself:
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
			if ((not ((temp4 signal:) & 0x0080)) and ((temp4 nsRight:) <= 0)):
				(temp4 show: temp0 temp1)
				temp0 = (20 + (temp4 nsRight:))
			else:
				(temp4 show:)
			#endif
			# for:reinit
			temp2 = temp3
		#end:loop
		if (not okButton):
			okButton = kernel.NodeValue((self first:))
		#endif
		if curIcon:
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
		(self doit: hide:)
	#end:method

	@classmethod
	def dispatchEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp53 = (param1 type:)
		temp54 = (param1 message:)
		(cond
			case (temp53 == 8192):
				if 
					(and
						temp1 = (self firstTrue: #onMe param1)
						(temp1 helpVerb:)
					)
					temp2 = kernel.GetPort()
					if (global38 respondsTo: #eraseOnly):
						temp0 = (global38 eraseOnly:)
						(global38 eraseOnly: 1)
						(Print
							font: global22
							width: 250
							addText:
								(temp1 noun:)
								(temp1 helpVerb:)
								0
								1
								0
								0
								(temp1 modNum:)
							init:
						)
						(global38 eraseOnly: temp0)
					else:
						(Print
							font: global22
							width: 250
							addText:
								(temp1 noun:)
								(temp1 helpVerb:)
								0
								1
								0
								0
								(temp1 modNum:)
							init:
						)
					#endif
					kernel.SetPort(temp2)
				#endif
				if helpIconItem:
					(helpIconItem signal: ((helpIconItem signal:) & 0xffef))
				#endif
				(global1 setCursor: 999)
				return 0
			#end:case
			case (temp53 & 0x0040):
				match temp54
					case 5:
						(cond
							case 
								(and
									kernel.IsObject(highlightedIcon)
									(highlightedIcon respondsTo: #retreat)
								):
								(highlightedIcon retreat:)
								return 0
							#end:case
							case 
								(or
									(not kernel.IsObject(highlightedIcon))
									((highlightedIcon signal:) & 0x0100)
								):
								(self advance:)
								return 0
							#end:case
						)
					#end:case
					case 1:
						(cond
							case 
								(and
									kernel.IsObject(highlightedIcon)
									(highlightedIcon respondsTo: #advance)
								):
								(highlightedIcon advance:)
								return 0
							#end:case
							case 
								(or
									(not kernel.IsObject(highlightedIcon))
									((highlightedIcon signal:) & 0x0100)
								):
								(self retreat:)
								return 0
							#end:case
						)
					#end:case
					else:
						(super dispatchEvent: param1)
					#end:else
				#end:match
			#end:case
			else:
				(super dispatchEvent: param1)
			#end:else
		)
	#end:method

	@classmethod
	def select(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(param1 select: ((argc >= 2) and param2))
	#end:method

	@classmethod
	def advanceCurIcon():#end:method

	@classmethod
	def swapCurIcon():#end:method

	@classmethod
	def hide():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if window:
			(window dispose:)
			window = 0
		#endif
		if (state & 0x0020):
			(global8 pause: 0)
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if theObj:
			if (signal & 0x0040):
				((global63 if global63 else GameControls) hide:)
			#endif
			(global1 panelObj: theObj panelSelector: selector)
		#endif
	#end:method

#end:class or instance

