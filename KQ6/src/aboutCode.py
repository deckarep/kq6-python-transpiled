#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 905
import sci_sh
import kernel
import Main
import Print
import LoadMany
import Sound
import System

# Public Export Declarations
SCI.public_exports(
	aboutCode = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.instance
class aboutCode(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if global25:
					(global25 dispose:)
				#endif
				if (global90 == 2):
					local2 = 1
					global90 = 1
				#endif
				kernel.Format(@temp1, 905, 0)
				if kernel.FileIO(10, @temp1):
					local0 = 1
				#endif
				match
					(= temp0
						if local0:
							(Print
								posn: 75 60
								font: 4
								addButton: 1 0 0 1 0 24 0 908
								addButton: 2 0 0 2 0 24 18 908
								addButton: 3 0 0 4 0 0 36 908
								addButton: 4 0 0 3 0 32 54 908
								addButton: 5 0 0 19 0 0 72 908
								init:
							)
						else:
							(Print
								posn: 75 75
								font: 4
								addButton: 1 0 0 1 0 24 0 908
								addButton: 2 0 0 2 0 24 18 908
								addButton: 3 0 0 4 0 0 36 908
								addButton: 4 0 0 3 0 32 54 908
								init:
							)
						#endif
					)
					case 1:
						(global2 setScript: oneThroughFive)
					#end:case
					case 2:
						(global2 setScript: sixScript)
					#end:case
					case 3:
						(global2 setScript: tips)
					#end:case
					case 4:
						(global2 setScript: walkThrough)
					#end:case
					case 5:
						(global2 setScript: damnedAd)
					#end:case
					else:
						(self dispose:)
					#end:else
				#end:match
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oneThroughFive(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 0 0 5 0 self 908)
			#end:case
			case 1:
				(global91 say: 0 0 11 0 self 908)
			#end:case
			case 2:
				(global91 say: 0 0 12 0 self 908)
			#end:case
			case 3:
				(global91 say: 0 0 13 0 self 908)
			#end:case
			case 4:
				(global91 say: 0 0 14 0 self 908)
			#end:case
			case 5:
				(self dispose:)
				if local2:
					global90 = 2
				#endif
				proc958_0(0, 905)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sixScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				proc921_1(r"""King's Quest VI\nVersion: 1.000.00G\nThis entire work is Copyright 1992-93\nSierra On-Line, Inc. All rights reserved.""")
				cycles = 1
			#end:case
			case 1:
				(global91 say: 0 0 15 0 self 908)
			#end:case
			case 2:
				(self dispose:)
				if local2:
					global90 = 2
				#endif
				proc958_0(0, 905)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tips(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 0 0 16 0 self 908)
			#end:case
			case 1:
				(self dispose:)
				if local2:
					global90 = 2
				#endif
				proc958_0(0, 905)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkThrough(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 0 0 18 0 self 908)
			#end:case
			case 1:
				(self dispose:)
				if local2:
					global90 = 2
				#endif
				proc958_0(0, 905)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class damnedAd(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global1 isHandsOn:):
					local1 = 1
				#endif
				(global1 handsOff: killSound: 1)
				if kernel.DoSound(4):
					cycles = 1
				else:
					(global91 say: 0 0 21 1 self 908)
				#endif
			#end:case
			case 1:
				if kernel.DoSound(4):
					(localMusic number: 11 init: play: self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if kernel.DoSound(4):
					(global91 say: 0 0 20 1 self 908)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if local1:
					(global1 handsOn: killSound: 0)
				#endif
				(localMusic dispose:)
				(self dispose:)
				if local2:
					global90 = 2
				#endif
				proc958_0(0, 905)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic(Sound):
	#property vars (may be empty)
#end:class or instance

