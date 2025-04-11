#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 81
import sci_sh
import kernel
import Main
import rgCastle
import RegionPath
import System

# Public Export Declarations
SCI.public_exports(
	RgBasement = 0,
	guardPath1 = 1,
	guardPath2 = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [32767, 840, 16, 52, 79, 52, 100, 114, 131, 134, 178, 134, 192, 113, 152, 113, 32767, 720, 334, 166, 108, 142, 112, 134, 142, 135, -32768]
local27 = [32767, 720, 142, 135, 112, 134, 108, 142, -27, 158, 32767, 710, 164, 114, 126, 115, 125, 182, 343, 182, 32767, 840, -17, 182, 145, 182, 167, 134, 131, 134, 100, 114, 79, 52, 6, 52, -32768]


class RgBasement(rgCastle):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if (self tstFlag: 709 1):
			(kernel.ScriptID(80, 5)
				view: 725
				regPathID: guardPath1
				setMotion: guardPath1 kernel.ScriptID(80, 5) kernel.ScriptID(80, 5)
				init:
			)
		#endif
		if (self tstFlag: 709 2):
			(kernel.ScriptID(80, 6)
				view: 727
				regPathID: guardPath2
				setMotion: guardPath2 kernel.ScriptID(80, 6) kernel.ScriptID(80, 6)
				init:
			)
		#endif
		if 
			(and
				(or
					(not proc999_5(global12, 840, 710, 720, 770, 820, 780))
					((global102 number:) != 704)
				)
				(not (kernel.ScriptID(80, 0) tstFlag: 709 2))
				(not (kernel.ScriptID(80, 0) tstFlag: 709 8192))
			)
			(global102 fadeTo: 704 -1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(loiterTimer == -1)
				(not (global2 script:))
				(not (self tstFlag: 709 1))
				(not (self tstFlag: 709 2))
			)
			loiterTimer = 36
		#endif
		(super doit:)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		keep = proc999_5(param1, 840, 710, 720, 770, 820, 780)
		initialized = 0
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def doLoiter():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((not (rFlag1 & 0x0004)) and (not proc999_5(global11, 820, 780))):
			if ((not (rFlag1 & 0x0001)) and (not (rFlag1 & 0x0002))):
				match global11
					case 710:
						(rFlag1 |= 0x0002)
					#end:case
					else:
						(rFlag1 |= 0x0001)
					#end:else
				#end:match
				loiterTimer = 1
				(global2 doLoiter:)
			else:
				(self startGuard:)
			#endif
		#endif
	#end:method

	@classmethod
	def startGuard():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((rFlag1 & 0x0001) and (not (kernel.ScriptID(80, 5) mover:))):
			(kernel.ScriptID(80, 5)
				view: 725
				init:
				regPathID: guardPath1
				setMotion: guardPath1 kernel.ScriptID(80, 5) kernel.ScriptID(80, 5) 1
			)
		#endif
		if ((rFlag1 & 0x0002) and (not (kernel.ScriptID(80, 6) mover:))):
			(kernel.ScriptID(80, 6)
				view: 727
				init:
				regPathID: guardPath2
				setMotion: guardPath2 kernel.ScriptID(80, 6) kernel.ScriptID(80, 6) 1
			)
		#endif
		(self setupGuards:)
	#end:method

	@classmethod
	def resetGuard(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(rFlag1 &= (~ param2))
		if kernel.IsObject((param1 regPathID:)):
			((param1 regPathID:) value: 0)
		#endif
	#end:method

	@classmethod
	def setupGuards():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((global11 != 840) and (rFlag1 & 0x0001)):
			(kernel.ScriptID(80, 5)
				okToCheck: (>= 10 (((kernel.ScriptID(80, 5) regPathID:) value:) / 2) 4)
			)
		#endif
		if ((global11 != 840) and (rFlag1 & 0x0002)):
			(kernel.ScriptID(80, 6)
				okToCheck: (>= 13 (((kernel.ScriptID(80, 6) regPathID:) value:) / 2) 3)
			)
		#endif
		(super setupGuards:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(80, 5) z: 0 setMotion: 0)
		(kernel.ScriptID(80, 6) z: 0 setMotion: 0)
		(super dispose: &rest)
		kernel.DisposeScript(918)
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if ((argc > 3) and param4):
					(global91 say: param2 param3 param4)
				#endif
				(cond
					case ((kernel.ScriptID(80, 0) weddingMusicCount:) >= 3):
						(rFlag1 |= 0x0004)
						(self startGuard:)
					#end:case
					case (not (kernel.ScriptID(80, 0) weddingRemind:)):
						(kernel.ScriptID(80, 0) weddingRemind: 15)
					#end:case
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardPath1(RegionPath):
	#property vars (may be empty)
	endType = 0
	theRegion = 81
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (RgBasement tstFlag: 709 4):
			endType = 2
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def at(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return local0[param1]
	#end:method

	@classmethod
	def nextRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (currentRoom == global11)
		(super nextRoom: &rest)
		if (kernel.IsObject(global2) and (not temp0)):
			(cond
				case (value > 2):
					(global2 warnUser: 5 currentRoom)
				#end:case
				case (not (kernel.ScriptID(81, 0) tstFlag: 709 4)):
					(global2 warnUser: 6 7)
				#end:case
			)
			if (currentRoom == global11):
				(global105 number: 702 loop: 1 play:)
			#endif
		#endif
	#end:method

#end:class or instance

@SCI.instance
class guardPath2(RegionPath):
	#property vars (may be empty)
	endType = 0
	theRegion = 81
	
	@classmethod
	def at(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return local27[param1]
	#end:method

	@classmethod
	def nextRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (currentRoom == global11)
		if 
			(and
				(value < 2)
				(global11 == 840)
				(not (RgBasement tstFlag: 709 8))
			)
			(RgBasement setFlag: 709 8)
			value = 10
		#endif
		(super nextRoom: &rest)
		if (kernel.IsObject(global2) and (not temp0)):
			if (value > 2):
				(global2 warnUser: 5 currentRoom)
			else:
				(global2 warnUser: 6 8)
			#endif
			if (currentRoom == global11):
				(global105 number: 702 loop: 1 play:)
			#endif
		#endif
	#end:method

#end:class or instance

