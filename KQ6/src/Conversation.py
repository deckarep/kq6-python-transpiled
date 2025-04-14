#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 925
import sci_sh
import kernel
import Main
import Print
import System

class MessageObj(Obj):
	#property vars (may be empty)
	modNum = -1
	noun = 0
	verb = 0
	case = 0
	sequence = 0
	whoSays = 0
	client = 0
	caller = 0
	font = 0
	x = 0
	y = 0
	
	@classmethod
	def showSelf():
		(= whoSays
			global91._send(
				'findTalker:', kernel.Message(0, modNum, noun, verb, case, if 
						sequence
						sequence
					else:
						1
					#endif)
			)
		)
		if (whoSays != -1):
			if (not kernel.IsObject(whoSays)):
				Print._send(
					'addTextF:', r"""<MessageObj> Message not found: %d - %d, %d, %d, %d""", modNum, noun, verb, case, sequence,
					'init:'
				)
				global4 = 1
			else:
				if font:
					whoSays._send('font:', font)
				#endif
				if (x or y):
					whoSays._send('x:', x, 'y:', y)
				#endif
				global91._send('say:', noun, verb, case, sequence, caller, modNum)
			#endif
		else:
			caller._send('cue:')
		#endif
	#end:method

#end:class or instance

class Conversation(List):
	#property vars (may be empty)
	script = 0
	curItem = -1
	caller = 0
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		curItem = -1
		if (argc and kernel.IsObject(param1)):
			caller = param1
		#endif
		global78._send('add:', self)
		self._send('cue:')
	#end:method

	@classmethod
	def dispose():
		self._send('eachElementDo:', #perform, cleanCode)
		global78._send('delete:', self)
		if global25:
			global25._send('dispose:')
		#endif
		if script:
			script = 0
		#endif
		temp0 = caller
		super._send('dispose:')
		if temp0:
			caller = 0
			temp0._send('cue:')
		#endif
	#end:method

	@classmethod
	def doit():
		if script:
			script._send('doit:')
		#endif
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((argc and param1) or (curItem.post('++') == size)):
			self._send('dispose:')
		else:
			temp0 = self._send('at:', curItem)
			(cond
				case temp0._send('isKindOf:', MessageObj):
					temp0._send('caller:', self, 'showSelf:')
				#end:case
				case temp0._send('isKindOf:', Script):
					self._send('setScript:', temp0, self)
				#end:case
				case kernel.IsObject(temp0):
					temp0._send('doit:', self)
				#end:case
				else:
					self._send('cue:')
				#end:else
			)
		#endif
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		if kernel.IsObject(script):
			script._send('dispose:')
		#endif
		if param1:
			param1._send('init:', self, &rest)
		#endif
	#end:method

	@classmethod
	def load(param1 = None, *rest):
		temp0 = proc999_6(param1, 0)
		temp1 = proc999_6(param1, 1)
		temp2 = proc999_6(param1, 2)
		temp3 = proc999_6(param1, 3)
		temp4 = proc999_6(param1, 4)
		temp5 = proc999_6(param1, 5)
		temp6 = proc999_6(param1, 6)
		temp7 = proc999_6(param1, 7)
		temp8 = 7
		while temp0:

			if (temp0 == -1):
				temp0 = global11
			#endif
			self._send('add:', temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7)
			temp0 = proc999_6(param1, temp8.post('++'))
			temp1 = proc999_6(param1, temp8.post('++'))
			temp2 = proc999_6(param1, temp8.post('++'))
			temp3 = proc999_6(param1, temp8.post('++'))
			temp4 = proc999_6(param1, temp8.post('++'))
			temp5 = proc999_6(param1, temp8.post('++'))
			temp6 = proc999_6(param1, temp8.post('++'))
			temp7 = proc999_6(param1, temp8.post('++'))
		#end:loop
	#end:method

	@classmethod
	def add(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = temp1 = temp2 = temp3 = temp4 = 0
		temp5 = temp6 = temp7 = 0
		if (argc and (not kernel.IsObject(param1[0]))):
			if (temp0 = param1[0] == -1):
				temp0 = global11
			#endif
			if (argc > 1):
				temp1 = param1[1]
				if (argc > 2):
					temp2 = param1[2]
					if (argc > 3):
						temp3 = param1[3]
						if (argc > 4):
							temp4 = param1[4]
							if (argc > 5):
								temp5 = param1[5]
								if (argc > 6):
									temp6 = param1[6]
									if (argc > 7):
										temp7 = param1[7]
									#endif
								#endif
							#endif
						#endif
					#endif
				#endif
			#endif
			if (not kernel.IsObject(param1[0])):
				super._send(
					'add:', MessageObj._send('new:')._send(
							'modNum:', temp0,
							'noun:', temp1,
							'verb:', temp2,
							'case:', temp3,
							'sequence:', temp4,
							'x:', temp5,
							'y:', temp6,
							'font:', temp7,
							'yourself:'
						)
				)
			#endif
		else:
			super._send('add:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class cleanCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		if param1._send('isKindOf:', Script):
			param1._send('caller:', 0)
		#endif
		if 
			(and
				param1._send('isKindOf:', MessageObj)
				kernel.IsObject(temp0 = param1._send('whoSays:'))
				temp0._send('underBits:')
			)
			temp0._send('dispose:', 1)
		#endif
	#end:method

#end:class or instance

