#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 909
import sci_sh
import Main
import Kq6Window
import Print
import Dialog
import Talker

# Public Export Declarations
SCI.public_exports(
	Kq6Talker = 0,
)

class Kq6Talker(Talker):
	#property vars (may be empty)
	disposeWhenDone = 2
	talkWidth = 270
	textX = 82
	winPosn = 1
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		if (and (global90 == 2) argc (IsObject param1) raveName):
			saveX = x
			saveY = y
			if (winPosn == 0):
				x = 59
				y = 15
			else:
				x = 177
				y = 15
			#endif
		#endif
		if (not (global11 == 450)):
			(= raving
				if 
					(and
						argc
						param1
						global169
						(global90 == 2)
						(not (Platform 5))
					)
					(Platform 6)
				#endif
			)
		else:
			(= raving
				if 
					(and
						(bust or param1)
						global169
						(global90 == 2)
						(not (Platform 5))
					)
					(Platform 6)
				#endif
			)
		#endif
		if argc:
			(super init: param1 &rest)
		else:
			(super init:)
		#endif
	#end:method

#end:class or instance

class Kq6Narrator(Narrator):
	#property vars (may be empty)
	y = 10
	keepWindow = 1
	strView = 945
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self font: global22 color: (Kq6Window color:) back: (Kq6Window back:))
		(super init: &rest)
	#end:method

	@classmethod
	def display(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((x + talkWidth) > 318):
			temp0 = (318 - x)
		else:
			temp0 = talkWidth
		#endif
		(temp1 = (global38 new:) color: color back: back)
		temp2 = (StrAt param1 0)
		if (>= 90 temp2 65):
			(StrAt param1 0 9)
			(temp3 = (DIcon new:)
				view: strView
				loop: (0 + ((temp2 - 65) / 13))
				cel: (mod (temp2 - 65) 13)
			)
			(Print
				window: temp1
				posn: x y
				font: font
				width: temp0
				addTitle: (name if showTitle else 0)
				addText: param1 0 7
				addIcon: temp3 0 0 0 0
				modeless: 1
				init:
			)
		else:
			(Print
				window: temp1
				posn: x y
				font: font
				width: temp0
				title: (name if showTitle else 0)
				addText: param1
				modeless: 1
				init:
			)
		#endif
	#end:method

#end:class or instance

