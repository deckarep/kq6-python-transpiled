#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 990
import sci_sh
import kernel
import Main
import Interface
import Print
import Dialog
import File

# Public Export Declarations
SCI.public_exports(
	proc990_0 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5
local20
local35
local50
local65


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		(cond
			case (self == Restore): 0#end:case
			case (localproc_1): 1#end:case
			case local2: 2#end:case
			else: 3#end:else
		)
	)
#end:procedure

@SCI.procedure
def proc990_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	while True: #repeat
		if 
			(not
				(= temp0
					(Print
						font: 0
						addText: 1 0 0 1 0 0 990
						addEdit: kernel.StrCpy(@temp1, param1) 29 0 20 param1
						addButton: 1 27 0 0 1 0 34 990
						addButton: 0 38 0 0 1 50 34 990
						init:
					)
				)
			)
			return 0
		#endif
		if (not kernel.StrLen(@temp1)):
			kernel.GetCWD(@temp1)
		#endif
		if kernel.ValidPath(@temp1):
			kernel.StrCpy(param1, @temp1)
			return 1
		else:
			kernel.Message(0, 990, 29, 0, 0, 1, @temp134)
			kernel.Format(@temp34, @temp134, @temp1)
			(Print font: 0 addText: @temp34 init:)
		#endif
	#end:loop
#end:procedure

@SCI.procedure
def localproc_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (local2 < 20):
		kernel.CheckFreeSpace(global29)
	#endif
#end:procedure

@SCI.procedure
def localproc_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(Print font: 0 addText: 3 0 0 1 0 0 990 init:)
#end:procedure

class SRDialog(Dialog):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
	#end:method

	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		window = global38
		nsBottom = 0
		if (local2 = kernel.GetSaveFiles((global1 name:), param2, param3) == -1):
			return 0
		#endif
		if (local4 = (localproc_0) == 1):
			(editI
				text: kernel.StrCpy(param1, param2)
				font: global23
				setSize:
				moveTo: 4 4
			)
			(self add: editI setSize:)
		#endif
		(selectorI
			text: param2
			font: global23
			setSize:
			moveTo: 4 (nsBottom + 4)
			state: 2
		)
		match local4
			case 0:
				kernel.Message(0, 990, 26, 0, 0, 1, @local5)
			#end:case
			case 1:
				kernel.Message(0, 990, 28, 0, 0, 1, @local5)
			#end:case
			else:
				kernel.Message(0, 990, 25, 0, 0, 1, @local5)
			#end:else
		#end:match
		local1 = ((selectorI nsRight:) + 4)
		(okI
			text: @local5
			setSize:
			moveTo: local1 (selectorI nsTop:)
			state:
				if (((local4 == 0) and (not local2)) or (local4 == 3)):
					0
				else:
					3
				#endif
		)
		kernel.Message(0, 990, 24, 0, 0, 1, @local20)
		(deleteI
			text: @local20
			setSize:
			moveTo: local1 ((okI nsBottom:) + 4)
			state: (0 if (not local2) else 3)
		)
		kernel.Message(0, 990, 23, 0, 0, 1, @local35)
		(changeDirI
			text: @local35
			setSize:
			moveTo: local1 ((deleteI nsBottom:) + 4)
			state: ((changeDirI state:) & 0xfff7)
		)
		kernel.Message(0, 990, 22, 0, 0, 1, @local50)
		(cancelI
			text: @local50
			setSize:
			moveTo: local1 ((changeDirI nsBottom:) + 4)
			state: ((cancelI state:) & 0xfff7)
		)
		(self add: selectorI okI deleteI changeDirI cancelI setSize:)
		match local4
			case 0:
				kernel.Message(0, 990, 10, 0, 0, 1, @temp0)
			#end:case
			case 1:
				kernel.Message(0, 990, 11, 0, 0, 1, @temp0)
			#end:case
			else:
				kernel.Message(0, 990, 30, 0, 0, 1, @temp0)
			#end:else
		#end:match
		(textI text: @temp0 setSize: ((nsRight - nsLeft) - 8) moveTo: 4 4)
		local1 = ((textI nsBottom:) + 4)
		(self eachElementDo: #move 0 local1)
		(self add: textI setSize: center: open: 4 -1)
		return 1
	#end:method

	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (and (self == Restore) argc param1):
			if 
				(==
					(= temp0
						kernel.FileIO(0, kernel.Format(@temp385, r"""%ssg.dir""", (global1
							name:
						)))
					)
					-1
				)
				return
			#endif
			kernel.FileIO(1, temp0)
		#endif
		if (not (self init: param1 @temp3 @temp364)):
			return -1
		#endif
		while True: #repeat
			(= local0
				match local4
					case 0:
						(okI if local2 else changeDirI)
					#end:case
					case 1: editI#end:case
					case 2: okI#end:case
					else: changeDirI#end:else
				#end:match
			)
			local1 = (super doit: local0)
			temp2 = (local3 = (selectorI indexOf: (selectorI cursor:)) * 18)
			if (local1 == changeDirI):
				(self dispose:)
				if 
					(and
						(proc990_0 global29)
						(==
							(= local2
								kernel.GetSaveFiles((global1 name:), @temp3, @temp364)
							)
							-1
						)
					)
					temp1 = -1
					(break)
				#endif
				(self init: param1 @temp3 @temp364)
			else:
				if ((local4 == 2) and (local1 == okI)):
					(self dispose:)
					if (GetReplaceName doit: kernel.StrCpy(param1, @temp3[temp2])):
						temp1 = temp364[local3]
						(break)
					#endif
					(self init: param1 @temp3 @temp364)
					(continue)
				#endif
				if ((local4 == 1) and ((local1 == okI) or (local1 == editI))):
					if (kernel.StrLen(param1) == 0):
						(self dispose:)
						(localproc_2)
						(self init: param1 @temp3 @temp364)
						(continue)
					#endif
					temp1 = -1
					local1 = 0
					while (local1 < local2): # inline for
						(breakif
							(not
								temp1 = kernel.StrCmp(param1, @temp3[(local1 * 18)])
							)
						)
						# for:reinit
						local1.post('++')
					#end:loop
					if (not temp1):
						temp1 = temp364[local1]
						(break)
					#endif
					if (local2 == 20):
						temp1 = temp364[local3]
						(break)
					#endif
					temp1 = 0
					while 1: # inline for
						local1 = 0
						while (local1 < local2): # inline for
							(breakif (temp1 == temp364[local1]))
							# for:reinit
							local1.post('++')
						#end:loop
						if (local1 == local2):
							(break)
						#endif
						# for:reinit
						temp1.post('++')
					#end:loop
					(break)
				#endif
				(cond
					case (local1 == deleteI):
						(self dispose:)
						if 
							(not
								(Print
									addText: 12 0 0 1 0 0 990
									addButton: 0 31 0 0 1 0 35 990
									addButton: 1 32 0 0 1 50 35 990
									init:
								)
							)
							(self init: param1 @temp3 @temp364)
						else:
							(temp0 = (File new:)
								name: kernel.DeviceInfo(7, @temp385, (global1 name:))
								open: 2
							)
							temp1 = 2570
							local1 = 0
							while (local1 < local2): # inline for
								if (local1 != local3):
									(temp0 write: @temp364[local1] 2)
									(temp0 writeString: @temp3[(local1 * 18)])
									(temp0 write: @temp1 1)
								#endif
								# for:reinit
								local1.post('++')
							#end:loop
							temp1 = -1
							(temp0 write: @temp1 2 close: dispose:)
							kernel.DeviceInfo(8, @temp385, (global1 name:), [temp364
								local3
							])
							kernel.FileIO(4, @temp385)
							(self init: param1 @temp3 @temp364)
						#endif
					#end:case
					case (local1 == okI):
						temp1 = temp364[local3]
						(break)
					#end:case
					case ((local1 == -1) or (local1 == cancelI)):
						temp1 = -1
						(break)
					#end:case
					case (local4 == 1):
						(editI
							cursor: kernel.StrLen(kernel.StrCpy(param1, @temp3[temp2]))
							draw:
						)
					#end:case
				)
			#endif
		#end:loop
		kernel.DisposeScript(993)
		(self dispose:)
		kernel.DisposeScript(990)
		return temp1
	#end:method

#end:class or instance

class Restore(SRDialog):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Message(0, 990, 20, 0, 0, 1, @local65)
		text = @local65
		(super init: &rest)
	#end:method

#end:class or instance

class Save(SRDialog):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Message(0, 990, 21, 0, 0, 1, @local65)
		text = @local65
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class GetReplaceName(Dialog):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		window = global38
		kernel.Message(0, 990, 33, 0, 0, 1, @temp1)
		(text1 text: @temp1 setSize: moveTo: 4 4)
		(self add: text1 setSize:)
		(oldName text: param1 font: global23 setSize: moveTo: 4 nsBottom)
		(self add: oldName setSize:)
		kernel.Message(0, 990, 34, 0, 0, 1, @temp16)
		(text2 text: @temp16 setSize: moveTo: 4 nsBottom)
		(self add: text2 setSize:)
		(newName text: param1 font: global23 setSize: moveTo: 4 nsBottom)
		(self add: newName setSize:)
		kernel.Message(0, 990, 33, 0, 0, 1, @temp31)
		(button1 text: @temp31 nsLeft: 0 nsTop: 0 setSize:)
		kernel.Message(0, 990, 38, 0, 0, 1, @temp46)
		(button2 text: @temp46 nsLeft: 0 nsTop: 0 setSize:)
		(button2 moveTo: (nsRight - ((button2 nsRight:) + 4)) nsBottom)
		(button1
			moveTo: ((button2 nsLeft:) - ((button1 nsRight:) + 4)) nsBottom
		)
		(self add: button1 button2 setSize: center: open: 0 -1)
		temp0 = (super doit: newName)
		(self dispose:)
		if (not kernel.StrLen(param1)):
			(localproc_2)
			temp0 = 0
		#endif
		return ((temp0 == newName) or (temp0 == button1))
	#end:method

#end:class or instance

@SCI.instance
class selectorI(DSelector):
	#property vars (may be empty)
	x = 36
	y = 8
	
#end:class or instance

@SCI.instance
class editI(DEdit):
	#property vars (may be empty)
	max = 35
	
#end:class or instance

@SCI.instance
class okI(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class cancelI(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class changeDirI(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class deleteI(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class textI(DText):
	#property vars (may be empty)
	font = 0
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class text1(DText):
	#property vars (may be empty)
	font = 0
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class text2(DText):
	#property vars (may be empty)
	font = 0
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class oldName(DText):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class newName(DEdit):
	#property vars (may be empty)
	max = 35
	
#end:class or instance

@SCI.instance
class button1(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

@SCI.instance
class button2(DButton):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: 1)
	#end:method

#end:class or instance

