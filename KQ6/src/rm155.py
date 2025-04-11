#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 155
import sci_sh
import Main
import KQ6Room
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm155 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1551


@SCI.instance
class rm155(KQ6Room):
	#property vars (may be empty)
	picture = 98
	style = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global69 disable:)
		(self setScript: backgroundScr)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable:)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class backgroundScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (global12 > 500):
					(Palette 1 1551)
					local0 = 155
				else:
					(moonEnd init:)
				#endif
				(global2 drawPic: 136 100)
				(SetCursor 0)
				(mane1 init: setCycle: Fwd)
				(mane2 init: setCycle: Fwd)
				(mane3 init: setCycle: Fwd)
				(mane4 init: setCycle: Fwd)
				(mane5 init: setCycle: Fwd)
				(mane6 init: setCycle: Fwd)
				(water1 init: setCycle: Fwd)
				(water2 init: setCycle: Fwd)
				(isle1 init:)
				(isle2 init:)
				(isle1 moveSpeed: 15 setMotion: MoveTo 76 154 self)
				(isle2 moveSpeed: 15 setMotion: MoveTo 242 159 self)
				ticks = 60
			#end:case
			case 1:
				(water1
					moveSpeed: 30
					setStep: 1 1
					setMotion: MoveTo 27 176
					setPri: 12
				)
				(water2
					moveSpeed: 30
					setStep: 1 1
					setMotion: MoveTo 289 176
					setPri: 12
				)
				ticks = 120
			#end:case
			case 2:
				(PalVary 0 local0 4 64 1)
				ticks = 60
			#end:case
			case 3:
				if (global5 contains: moonEnd):
					(moonEnd moveSpeed: 4 setMotion: MoveTo 73 118)
				#endif
			#end:case
			case 4: 0#end:case
			case 5:
				(isle1 setPri: 13 cycleSpeed: 25)
				(isle2 setPri: 13 cycleSpeed: 25)
				ticks = 1
			#end:case
			case 6:
				(isle1 setCycle: End setMotion: MoveTo 62 172 self)
				(isle2 setCycle: End setMotion: MoveTo 256 177 self)
			#end:case
			case 7:
				(PalVary 3)
				if (global12 == 340):
					(global2 newRoom: 600)
				else:
					(global2 newRoom: 200)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class water1(Actor):
	#property vars (may be empty)
	x = 27
	y = 167
	view = 137
	signal = 2048
	
#end:class or instance

@SCI.instance
class water2(Actor):
	#property vars (may be empty)
	x = 289
	y = 167
	view = 137
	loop = 1
	cel = 1
	signal = 2048
	
#end:class or instance

@SCI.instance
class isle1(Actor):
	#property vars (may be empty)
	x = 76
	y = 185
	loop = 2
	priority = 2
	signal = 18448
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global12 == 340):
			(self view: 137)
		else:
			(self view: 139)
		#endif
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class isle2(Actor):
	#property vars (may be empty)
	x = 242
	y = 190
	loop = 3
	priority = 2
	signal = 18448
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global12 == 340):
			(self view: 137)
		else:
			(self view: 139)
		#endif
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class moonEnd(Actor):
	#property vars (may be empty)
	x = 71
	y = 160
	view = 137
	loop = 4
	priority = 1
	signal = 18448
	
#end:class or instance

@SCI.instance
class mane1(Prop):
	#property vars (may be empty)
	x = 171
	y = 46
	view = 138
	cel = 4
	priority = 15
	signal = 16
	cycleSpeed = 7
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class mane2(Prop):
	#property vars (may be empty)
	x = 177
	y = 124
	view = 138
	loop = 2
	priority = 16
	signal = 16
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class mane3(Prop):
	#property vars (may be empty)
	x = 163
	y = 159
	view = 138
	loop = 3
	priority = 14
	signal = 16
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class mane4(Prop):
	#property vars (may be empty)
	x = 190
	y = 137
	view = 138
	loop = 1
	cel = 3
	priority = 15
	signal = 16
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class mane5(Prop):
	#property vars (may be empty)
	x = 173
	y = 96
	view = 138
	loop = 2
	priority = 5
	signal = 16
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class mane6(Prop):
	#property vars (may be empty)
	x = 163
	y = 98
	view = 138
	loop = 3
	priority = 15
	signal = 16
	detailLevel = 2
	
#end:class or instance

