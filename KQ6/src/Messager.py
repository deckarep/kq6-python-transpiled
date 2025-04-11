#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 924
import sci_sh
import Main
import Print
import Game
import System

class Messager(Obj):
	#property vars (may be empty)
	caller = 0
	disposeWhenDone = 1
	oneOnly = 0
	killed = 0
	oldIconBarState = 0
	curSequence = 0
	lastSequence = 0
	talker = 0
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(talkerSet dispose:)
		if global69:
			(global69 state: oldIconBarState)
			oldIconBarState = 0
		#endif
		if caller:
			if (not global18):
				global18 = (Set new:)
			#endif
			(global18
				add:
					((Cue new:)
						cuee: caller
						cuer: self
						register: killed
						yourself:
					)
			)
		#endif
		talker = 0
		(super dispose:)
	#end:method

	@classmethod
	def cue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc and param1):
			killed = 1
		#endif
		if (oneOnly or killed):
			if global84:
				(global84 release: dispose:)
				global84 = 0
			#endif
			(self dispose:)
		else:
			(self sayNext:)
		#endif
	#end:method

	@classmethod
	def say(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = temp1 = temp2 = curSequence = 0
		caller = oneOnly = killed = 0
		if (global69 and (not oldIconBarState)):
			oldIconBarState = (global69 state:)
		#endif
		if (temp0 = param1[0] == -1):
			if ((argc > 1) and (IsObject param1[1])):
				caller = param1[1]
			#endif
			(self sayNext:)
		else:
			if ((argc > 1) and param1[1]):
				temp1 = param1[1]
			#endif
			if ((argc > 2) and param1[2]):
				temp2 = param1[2]
			#endif
			if ((argc > 3) and param1[3]):
				oneOnly = 1
				curSequence = param1[3]
			else:
				curSequence = 1
			#endif
			temp24 = 4
			if 
				(and
					(argc > 4)
					param1[temp24]
					(not (IsObject param1[temp24]))
				)
				lastSequence = param1[temp24]
				temp24++
				oneOnly = 0
			else:
				lastSequence = 0
			#endif
			if ((argc > temp24) and param1[temp24]):
				caller = param1[temp24]
			else:
				caller = 0
			#endif
			temp3 = (param1[temp24] if (argc > temp24++) else global11)
			if (global90 and (Message 0 temp3 temp0 temp1 temp2 curSequence)):
				(self sayNext: temp3 temp0 temp1 temp2 curSequence)
			else:
				(Print
					addTextF:
						r"""<Messager>\n\tmsgType set to 0 or\n\t%d: %d, %d, %d, %d not found"""
						temp3
						temp0
						temp1
						temp2
						curSequence
					init:
				)
				(self dispose:)
			#endif
		#endif
	#end:method

	@classmethod
	def sayFormat(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global69 and (not oldIconBarState)):
			oldIconBarState = (global69 state:)
		#endif
		temp2 = (self findTalker: param1)
		temp0 = (proc921_3 param2 param3 &rest)
		if (IsObject param3[(argc - 2)]):
			caller = param3[(argc - 2)]
		#endif
		oneOnly = 1
		temp1 = (Memory 1 temp0)
		(Format temp1 param2 param3 &rest)
		(temp2 say: temp1 self)
		(Memory 3 temp1)
	#end:method

	@classmethod
	def sayNext(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			temp0 = (Message 0 param1 param2 param3 param4 param5 @temp1)
		else:
			temp0 = (Message 1 @temp1)
		#endif
		if (global90 & 0x0002):
			temp201 = (Memory 1 12)
			(Message 8 temp201)
		#endif
		if 
			(and
				temp0
				(or
					(not lastSequence)
					(lastSequence and (curSequence <= lastSequence))
				)
			)
			temp0 = (self findTalker: temp0)
			if (and talker (temp0 != talker) ((talker disposeWhenDone:) == 2)):
				(talker caller: 0 dispose: 1)
			#endif
			if (talker = temp0 != -1):
				(talkerSet add: temp0)
				if (global90 & 0x0002):
					(temp0 modNum: param1 say: temp201 self)
				else:
					(temp0
						modNum: param1
						say: @temp1 self param1 param2 param3 param4 param5
					)
				#endif
				curSequence++
			else:
				if global84:
					(global84 release: dispose:)
					global84 = 0
				#endif
				(self dispose:)
			#endif
		else:
			if global84:
				(global84 release: dispose:)
				global84 = 0
			#endif
			(self dispose:)
		#endif
		if (global90 & 0x0002):
			(Memory 3 temp201)
		#endif
	#end:method

	@classmethod
	def findTalker():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Print
			width: 200
			addText:
				r"""<Messager findTalker:>\n\tCan't find talker or\n\tfindTalker method not over-ridden"""
			init:
		)
		return global89
	#end:method

#end:class or instance

@SCI.instance
class talkerSet(Set):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			eachElementDo: #caller 0
			eachElementDo: #dispose (global91 disposeWhenDone:)
			release:
		)
		(super dispose:)
	#end:method

#end:class or instance

