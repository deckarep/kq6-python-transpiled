#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 290
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm290 = 0,
)

@SCI.instance
class rm290(KQ6Room):
	#property vars (may be empty)
	noun = 5
	picture = 290
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						142
						120
						98
						120
						79
						133
						27
						133
						7
						159
						106
						159
						119
						172
						119
						184
						184
						184
						183
						161
						309
						161
						248
						128
						224
						128
						208
						118
						157
						118
						157
						1
						319
						1
						319
						189
						0
						189
						0
						1
						142
						1
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 164 138 182 132 203 141 184 146
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 120 127 137 136 118 145 102 137
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 142 150 142 140 161 140 161 150
					yourself:
				)
		)
		(super init: &rest)
		kernel.Load(128, 291)
		(global0 init: reset: 2 posn: 151 119 setScale: 0)
		(global93 addToFront: self)
		(ferryman init:)
		(door init: cel: 5 setCycle: Beg door)
		(genericFeatures init:)
		(table init:)
		if (((global9 at: 34) owner:) == global11):
			(rabbitsFoot init:)
		#endif
		(global2 setScript: enterScr)
		(global102 number: 290 loop: -1 play:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 3:
				(global2 setScript: leaveScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 fade:)
		(super dispose: &rest)
		proc913_1(17)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global91 say: 0 0 34 0 0 899)
		return 0
	#end:method

#end:class or instance

@SCI.instance
class enterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (not proc913_0(17)):
					(global1 givePoints: 2)
				#endif
				(ferryman setMotion: PolyPath 138 137 self)
			#end:case
			case 1:
				(ferryman
					posn: 128 147
					view: 294
					loop: 2
					cel: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(ferryman stopUpd:)
				(global0 setSpeed: 6 setMotion: MoveTo 160 140 self)
			#end:case
			case 3:
				(global0
					view: 291
					setLoop: 0
					posn: 176 144
					normal: 0
					cel: 0
					setCycle: End self
				)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(global0 stopUpd:)
				(global91 say: 1 0 (9 if proc913_0(17) else 8) 0 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class leaveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global93 delete: global2)
				(ferryman hide:)
				(global0
					view: 291
					loop: 3
					posn: 178 144
					cel: 0
					normal: 0
					setCycle: CT 8 1 self
				)
			#end:case
			case 1:
				(global91 say: 6 5 (13 if proc913_0(17) else 12) 0 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0 setCycle: End self)
			#end:case
			case 4:
				(ferryman view: 291 loop: 4 cel: 0 posn: 134 145 show:)
				(global0 reset: 7 posn: 167 142 ignoreActors: setScale: 0)
				cycles = 2
			#end:case
			case 5:
				(global0 setMotion: PolyPath 148 116 self)
			#end:case
			case 6:
				(global0 setHeading: 0 self)
			#end:case
			case 7:
				(ferryman setCycle: End self)
				(door setCycle: End self)
				(global105 number: 901 loop: 1 play:)
			#end:case
			case 8: 0#end:case
			case 9:
				(global2 newRoom: 260)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 136
	y = 78
	noun = 6
	sightAngle = 180
	view = 290
	loop = 3
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self stopUpd:)
		(global105 number: 902 loop: 1 play:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: leaveScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ferrymanTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (global158 < 5):
					global158.post('++')
				#endif
				match global158
					case 0: 0#end:case
					case 1:
						register = 2
						proc913_2(30)
						proc913_1(29)
					#end:case
					case 2:
						register = 3
					#end:case
					case 3:
						register = 4
					#end:case
					case 4:
						register = 5
					#end:case
					case 5:
						if (global166.post('++') > 5):
							global166 = 1
						#endif
						(= register
							match global166
								case 0: 0#end:case
								case 1: 6#end:case
								case 2: 14#end:case
								case 3: 15#end:case
								case 4: 16#end:case
								case 5: 18#end:case
								case 6: 19#end:case
							#end:match
						)
					#end:case
				#end:match
				cycles = 1
			#end:case
			case 1:
				if (global158 == 5):
					(global91 say: 3 2 17 1 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				(global91 say: 3 2 register 0 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ferryman(Actor):
	#property vars (may be empty)
	x = 150
	y = 121
	noun = 3
	sightAngle = 180
	view = 292
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			setStep: (global0 xStep:) (global0 yStep:)
			setCycle: Walk
			signal: (| signal 0x1000)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(global2 setScript: ferrymanTalkScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getRabbitsFoot(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 get: 34)
				(global91 say: 4 5 0 0 self)
			#end:case
			case 1:
				(global0 loop: 2 cel: 0 setPri: 11 setCycle: CT 3 1 self)
			#end:case
			case 2:
				(rabbitsFoot dispose:)
				cycles = 2
			#end:case
			case 3:
				(global0 setCycle: End self)
			#end:case
			case 4:
				(global0 cel: 0)
				cycles = 1
			#end:case
			case 5:
				(global1 givePoints: 1)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rabbitsFoot(View):
	#property vars (may be empty)
	x = 154
	y = 174
	z = 42
	noun = 4
	sightAngle = 180
	view = 290
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getRabbitsFoot)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setPri: 11 stopUpd: ignoreActors:)
	#end:method

#end:class or instance

@SCI.instance
class table(Feature):
	#property vars (may be empty)
	noun = 18
	onMeCheck = 256
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 5, 1):
			(global91
				say: noun param1 (21 if (global5 contains: rabbitsFoot) else 11)
			)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(= noun
				match temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
					case 2: 15#end:case
					case 8: 7#end:case
					case 16: 8#end:case
					case 32: 10#end:case
					case 64: 16#end:case
					case 128: 9#end:case
					case 512: 14#end:case
					case 1024: 11#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

