#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 999
import sci_sh
import kernel
import Main
import Print

# Public Export Declarations
SCI.public_exports(
	proc999_0 = 0,
	proc999_1 = 1,
	proc999_2 = 2,
	proc999_3 = 3,
	proc999_4 = 4,
	proc999_5 = 5,
	proc999_6 = 6,
	proc999_7 = 7,
)

@SCI.procedure
def proc999_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		if (param1 < 0):
			-1
		else:
			(param1 > 0)
		#endif
	)
#end:procedure

@SCI.procedure
def proc999_1(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if ((param1 -= (param2 * (param1 / param2))) < 0):
		(param1 += param2)
	#endif
	return param1
#end:procedure

@SCI.procedure
def proc999_2(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		if ((argc == 1) or (param1 < temp0 = (proc999_2 &rest))):
			param1
		else:
			temp0
		#endif
	)
#end:procedure

@SCI.procedure
def proc999_3(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		if ((argc == 1) or (param1 > temp0 = (proc999_3 &rest))):
			param1
		else:
			temp0
		#endif
	)
#end:procedure

@SCI.procedure
def proc999_4(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		(and
			(<=
				param1
				if (argc < 6):
					(param5 x:)
				else:
					param5
				#endif
				param3
			)
			(<=
				param2
				if (argc < 6):
					(param5 y:)
				else:
					param6
				#endif
				param4
			)
		)
	)
#end:procedure

@SCI.procedure
def proc999_5(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < (argc - 1)): # inline for
		if (param1 == param2[temp0]):
			return (param1 or 1)
		#endif
		# for:reinit
		temp0.post('++')
	#end:loop
	return 0
#end:procedure

@SCI.procedure
def proc999_6(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	kernel.Memory(5, (param1 + (2 * param2)))
#end:procedure

@SCI.procedure
def proc999_7(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(param1 param2: &rest)
#end:procedure

class Obj
	#property vars (may be empty)
	@classmethod
	def new():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Clone(self)
	#end:method

	@classmethod
	def init():#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return self
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.DisposeClone(self)
	#end:method

	@classmethod
	def showStr(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.StrCpy(param1, name)
	#end:method

	@classmethod
	def showSelf():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc921_0((self showStr: @temp0))
	#end:method

	@classmethod
	def perform(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(param1 doit: self &rest)
	#end:method

	@classmethod
	def respondsTo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.RespondsTo(self, param1)
	#end:method

	@classmethod
	def isMemberOf(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				(param1 == self)
				(and
					((param1 -info-:) & 0x8000)
					(not (-info- & 0x8000))
					(-propDict- == (param1 -propDict-:))
				)
			)
		)
	#end:method

	@classmethod
	def isKindOf(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				(and
					(-propDict- == (param1 -propDict-:))
					(-classScript- == (param1 -classScript-:))
				)
				(and
					temp0 = (self -super-:)
					kernel.IsObject(temp0)
					(temp0 isKindOf: param1)
				)
			)
		)
	#end:method

	@classmethod
	def yourself():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return self
	#end:method

#end:class or instance

class Code(Obj):
	#property vars (may be empty)
	@classmethod
	def doit():#end:method

#end:class or instance

class Collect(Obj):
	#property vars (may be empty)
	elements = 0
	size = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #doit &rest)
	#end:method

	@classmethod
	def showStr(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Format(param1, 999, 0, name, size)
	#end:method

	@classmethod
	def showSelf():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc921_0((self showStr: @temp0))
		(self eachElementDo: #showSelf)
	#end:method

	@classmethod
	def add(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not elements):
			elements = kernel.NewList()
		#endif
		temp1 = 0
		while (temp1 < argc): # inline for
			if (not (self isDuplicate: param1[temp1])):
				kernel.AddToEnd(elements, kernel.NewNode(param1[temp1], param1[temp1]))
				size.post('++')
			#endif
			# for:reinit
			temp1.post('++')
		#end:loop
		return self
	#end:method

	@classmethod
	def delete(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < argc): # inline for
			if kernel.DeleteKey(elements, param1[temp0]):
				size.post('--')
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		return self
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if elements:
			(self eachElementDo: #dispose)
			kernel.DisposeList(elements)
		#endif
		size = elements = 0
		(super dispose:)
	#end:method

	@classmethod
	def first():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.FirstNode(elements)
	#end:method

	@classmethod
	def next(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.NextNode(param1)
	#end:method

	@classmethod
	def isEmpty():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return ((elements == 0) or kernel.EmptyList(elements))
	#end:method

	@classmethod
	def contains(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.FindKey(elements, param1)
	#end:method

	@classmethod
	def eachElementDo(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.FirstNode(elements)
		while temp0: # inline for
			temp1 = kernel.NextNode(temp0)
			if (not kernel.IsObject(temp2 = kernel.NodeValue(temp0))):
				return
			#endif
			(temp2 param1: &rest)
			# for:reinit
			temp0 = temp1
		#end:loop
	#end:method

	@classmethod
	def firstTrue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.FirstNode(elements)
		while temp0: # inline for
			temp1 = kernel.NextNode(temp0)
			temp2 = kernel.NodeValue(temp0)
			if (temp2 param1: &rest):
				return temp2
			#endif
			# for:reinit
			temp0 = temp1
		#end:loop
		return 0
	#end:method

	@classmethod
	def allTrue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.FirstNode(elements)
		while temp0: # inline for
			temp1 = kernel.NextNode(temp0)
			temp2 = kernel.NodeValue(temp0)
			if (not (temp2 param1: &rest)):
				return 0
			#endif
			# for:reinit
			temp0 = temp1
		#end:loop
		return 1
	#end:method

	@classmethod
	def release():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.FirstNode(elements)
		while temp0: # inline for
			temp1 = kernel.NextNode(temp0)
			(self delete: kernel.NodeValue(temp0))
			# for:reinit
			temp0 = temp1
		#end:loop
	#end:method

	@classmethod
	def isDuplicate():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 0
	#end:method

#end:class or instance

class List(Collect):
	#property vars (may be empty)
	@classmethod
	def showStr(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Format(param1, 999, 1, name, size)
	#end:method

	@classmethod
	def at(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		
			(temp0 = kernel.FirstNode(elements))
			(param1 and temp0)
			(temp0 = kernel.NextNode(temp0))
			
			param1.post('--')
			# for:reinit
			temp0 = kernel.NextNode(temp0)
		#end:loop
		(return
			if temp0:
				kernel.NodeValue(temp0)
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def last():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.LastNode(elements)
	#end:method

	@classmethod
	def prev(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.PrevNode(param1)
	#end:method

	@classmethod
	def addToFront(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not elements):
			elements = kernel.NewList()
		#endif
		temp0 = (argc - 1)
		while (0 <= temp0): # inline for
			if (not (self isDuplicate: param1[temp0])):
				kernel.AddToFront(elements, kernel.NewNode(param1[temp0], param1[temp0]))
				size.post('++')
			#endif
			# for:reinit
			temp0.post('--')
		#end:loop
		return self
	#end:method

	@classmethod
	def addToEnd(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not elements):
			elements = kernel.NewList()
		#endif
		temp0 = 0
		while (temp0 < argc): # inline for
			if (not (self isDuplicate: param1[temp0])):
				kernel.AddToEnd(elements, kernel.NewNode(param1[temp0], param1[temp0]))
				size.post('++')
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		return self
	#end:method

	@classmethod
	def addAfter(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp2 = kernel.FindKey(elements, param1):
			argc.post('--')
			temp0 = 0
			while (temp0 < argc): # inline for
				if (not (self isDuplicate: param2[temp0])):
					(= temp2
						kernel.AddAfter(elements, temp2, kernel.NewNode([param2
							temp0
						], param2[temp0]))
					)
					size.post('++')
				#endif
				# for:reinit
				temp0.post('++')
			#end:loop
		#endif
		return self
	#end:method

	@classmethod
	def indexOf(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		temp1 = kernel.FirstNode(elements)
		while temp1: # inline for
			if (param1 == kernel.NodeValue(temp1)):
				return temp0
			#endif
			temp0.post('++')
			# for:reinit
			temp1 = kernel.NextNode(temp1)
		#end:loop
		return -1
	#end:method

#end:class or instance

class Set(List):
	#property vars (may be empty)
	@classmethod
	def showStr(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Format(param1, 999, 2, name, size)
	#end:method

	@classmethod
	def isDuplicate(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self contains: param1)
	#end:method

#end:class or instance

class EventHandler(Set):
	#property vars (may be empty)
	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp3 = kernel.Clone(param1)
		
			(temp0 = kernel.FirstNode(elements))
			(temp0 and (not (temp3 claimed:)))
			(temp0 = temp1)
			
			temp1 = kernel.NextNode(temp0)
			(breakif (not kernel.IsObject(temp2 = kernel.NodeValue(temp0))))
			(temp2 handleEvent: temp3)
			# for:reinit
			temp0 = temp1
		#end:loop
		temp4 = (temp3 claimed:)
		(temp3 dispose:)
		return temp4
	#end:method

#end:class or instance

class Script(Obj):
	#property vars (may be empty)
	client = 0
	state = -1
	start = 0
	timer = 0
	cycles = 0
	seconds = 0
	lastSeconds = 0
	ticks = 0
	lastTicks = 0
	register = 0
	script = 0
	caller = 0
	next = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script doit:)
		#endif
		(cond
			case cycles:
				if (not cycles.post('--')):
					(self cue:)
				#endif
			#end:case
			case seconds:
				temp0 = kernel.GetTime(1)
				if (lastSeconds != temp0):
					lastSeconds = temp0
					if (not seconds.post('--')):
						(self cue:)
					#endif
				#endif
			#end:case
			case (ticks and ((ticks -= kernel.Abs((global88 - lastTicks))) <= 0)):
				ticks = 0
				(self cue:)
			#end:case
		)
		lastTicks = global88
	#end:method

	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		lastTicks = global88
		if (argc >= 1):
			(client = param1 script: self)
			if (argc >= 2):
				caller = param2
				if (argc >= 3):
					register = param3
				#endif
			#endif
		#endif
		state = (start - 1)
		(self cue:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(script):
			(script dispose:)
		#endif
		if kernel.IsObject(timer):
			(timer dispose:)
		#endif
		if kernel.IsObject(client):
			(client
				script:
					(= temp0
						(cond
							case kernel.IsObject(next): next#end:case
							case next:
								kernel.ScriptID(next)
							#end:case
						)
					)
			)
			(cond
				case (not temp0): 0#end:case
				case (global13 == global11):
					(temp0 init: client)
				#end:case
				else:
					(temp0 dispose:)
				#end:else
			)
		#endif
		if (kernel.IsObject(caller) and (global13 == global11)):
			(caller cue: register)
		#endif
		script = timer = client = next = caller = 0
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		state = param1
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if client:
			(self changeState: (state + 1) &rest)
		#endif
	#end:method

	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(script):
			(script dispose:)
		#endif
		if param1:
			(param1 init: self &rest)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script handleEvent: param1)
		#endif
		(param1 claimed:)
	#end:method

#end:class or instance

class Event(Obj):
	#property vars (may be empty)
	type = 0
	message = 0
	modifiers = 0
	y = 0
	x = 0
	claimed = 0
	port = 0
	
	@classmethod
	def new(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (super new:)
		kernel.GetEvent((param1 if argc else 32767), temp0)
		return temp0
	#end:method

	@classmethod
	def localize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (type & 0x4000)):
			temp0 = kernel.GetPort()
			(cond
				case (not port):
					kernel.GlobalToLocal(self)
				#end:case
				case (port != temp0):
					kernel.SetPort(port)
					kernel.LocalToGlobal(self)
					kernel.SetPort(temp0)
					kernel.GlobalToLocal(self)
				#end:case
			)
			port = temp0
		#endif
		return self
	#end:method

	@classmethod
	def globalize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (type & 0x4000)):
			temp0 = kernel.GetPort()
			(cond
				case (port == temp0):
					kernel.LocalToGlobal(self)
				#end:case
				case port:
					kernel.SetPort(port)
					kernel.LocalToGlobal(self)
					kernel.SetPort(temp0)
				#end:case
			)
			port = 0
		#endif
		return self
	#end:method

#end:class or instance

class Cursor(Obj):
	#property vars (may be empty)
	view = 0
	loop = 0
	cel = 0
	x = 0
	y = 0
	hotSpotX = 0
	hotSpotY = 0
	hidden = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (hotSpotX or hotSpotY):
			kernel.SetCursor(view, loop, cel, hotSpotX, hotSpotY)
		else:
			kernel.SetCursor(view, loop, cel)
		#endif
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.SetCursor(param1, param2)
	#end:method

	@classmethod
	def posnHotSpot(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		hotSpotX = param1
		hotSpotY = param2
		(self init:)
	#end:method

	@classmethod
	def setLoop(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		loop = param1
		(self init:)
	#end:method

	@classmethod
	def setCel(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		cel = param1
		(self init:)
	#end:method

	@classmethod
	def showCursor(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			hidden = param1
			kernel.SetCursor(hidden)
		#endif
	#end:method

#end:class or instance

