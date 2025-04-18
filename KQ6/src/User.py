#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 996
import sci_sh
import kernel
import Main
import System

@SCI.instance
class uEvt(Event):
	#property vars (may be empty)
	@classmethod
	def new():
		type = message = modifiers = y = x = claimed = port = 0
		kernel.GetEvent(32767, self)
		return self
	#end:method

#end:class or instance

class User(Obj):
	#property vars (may be empty)
	alterEgo = 0
	input = 0
	controls = 0
	prevDir = 0
	x = -1
	y = -1
	mapKeyToDir = 1
	curEvent = 0
	
	@classmethod
	def init():
		curEvent = uEvt
	#end:method

	@classmethod
	def canInput(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			input = param1
		#endif
		return input
	#end:method

	@classmethod
	def doit():
		curEvent._send('new:')
		self._send('handleEvent:', curEvent)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		global70 = param1._send('x:')
		global71 = param1._send('y:')
		temp0 = param1._send('type:')
		temp2 = param1._send('modifiers:')
		if temp0:
			global24 = param1
			if mapKeyToDir:
				kernel.MapKeyToDir(param1)
			#endif
			if (temp0 == 256):
				temp0 = 4
				temp1 = (27 if (temp2 & 0x0003) else 13)
				temp2 = 0
				param1._send('type:', temp0, 'message:', temp1, 'modifiers:', 0)
			#endif
			if (global75 and global75._send('handleEvent:', param1)):
				return 1
			#endif
			if (global92 and global92._send('handleEvent:', param1)):
				return 1
			#endif
			param1._send('localize:')
			temp0 = param1._send('type:')
			temp1 = param1._send('message:')
			(cond
				case (temp0 & 0x0080):
					(cond
						case 
							(and
								(temp1 == 1)
								(or
									(= temp4
										global5._send('firstTrue:', #perform, findNoun)
									)
									(= temp4
										global32._send('firstTrue:', #perform, findNoun)
									)
									(= temp4
										global10._send('firstTrue:', #perform, findNoun)
									)
								)
							):
							temp4._send('doVerb:', global69._send('curIcon:')._send('message:'))
						#end:case
						case temp4 = global69._send('findIcon:', temp1):
							global69._send('select:', temp4)
							global1._send('setCursor:', temp4._send('cursor:'))
						#end:case
					)
				#end:case
				case (temp0 & 0x0040):
					(cond
						case (global74 and global74._send('handleEvent:', param1)):
							return 1
						#end:case
						case 
							(and
								(or
									(and
										global69
										(==
											global69._send('curIcon:')
											global69._send('walkIconItem:')
										)
									)
									(not global69)
								)
								alterEgo
								controls
								global5._send('contains:', alterEgo)
								alterEgo._send('handleEvent:', param1)
							):
							return 1
						#end:case
						case 
							(and
								global77
								((not (temp0 & 0x0004)) or (temp1 != 0))
								global77._send('handleEvent:', param1)
							):
							return 1
						#end:case
					)
				#end:case
				case 
					(and
						(temp0 & 0x0004)
						global72
						global72._send('handleEvent:', param1)
					):
					return 1
				#end:case
				case 
					(and
						(temp0 & 0x0003)
						global73
						global73._send('handleEvent:', param1)
					):
					return 1
				#end:case
			)
		#endif
		if global69:
			global69._send('handleEvent:', param1)
		#endif
		temp0 = param1._send('type:')
		temp1 = param1._send('message:')
		if (input and (temp0 & 0x4000)):
			(cond
				case 
					(and
						(temp0 & 0x1000)
						global93
						global93._send('handleEvent:', param1)
					):
					return 1
				#end:case
				case 
					(and
						(temp0 & 0x1000)
						global5._send('contains:', alterEgo)
						controls
						alterEgo._send('handleEvent:', param1)
					):
					return 1
				#end:case
				case global34:
					OnMeAndLowY._send('init:')
					global5._send('eachElementDo:', #perform, OnMeAndLowY, param1)
					global32._send('eachElementDo:', #perform, OnMeAndLowY, param1)
					global10._send('eachElementDo:', #perform, OnMeAndLowY, param1)
					if 
						(and
							OnMeAndLowY._send('theObj:')
							OnMeAndLowY._send('theObj:')._send('handleEvent:', param1)
						)
						return 1
					#endif
				#end:case
				case global5._send('handleEvent:', param1):
					return 1
				#end:case
				case global32._send('handleEvent:', param1):
					return 1
				#end:case
				case global10._send('handleEvent:', param1):
					return 1
				#end:case
			)
			if ((not param1._send('claimed:')) and global6._send('handleEvent:', param1)):
				return 1
			#endif
		#endif
		if temp0:
			(cond
				case global1._send('handleEvent:', param1):
					return 1
				#end:case
				case (global92 and global92._send('handleEvent:', param1)):
					return 1
				#end:case
			)
		#endif
		return 0
	#end:method

	@classmethod
	def canControl(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			controls = param1
			prevDir = 0
		#endif
		return controls
	#end:method

#end:class or instance

class OnMeAndLowY(Code):
	#property vars (may be empty)
	theObj = 0
	lastY = -1
	
	@classmethod
	def init():
		theObj = 0
		lastY = -1
	#end:method

	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		if (param1._send('onMe:', param2) and (param1._send('y:') > lastY)):
			theObj = param1
			lastY = theObj._send('y:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class findNoun(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		return (param1._send('noun:') == param2)
	#end:method

#end:class or instance

