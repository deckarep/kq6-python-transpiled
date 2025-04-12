#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 460
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm460 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local9 = [300, 120, 207, 260, 70, 5, 140]
local16 = [11, 11, 41, 23, 23, 23, 23]
local23 = [0, 4, 2, 4, 2, 2, 0]


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 7): # inline for
		(local0[temp0] = (aBee new:)
			x: local9[temp0]
			y: local16[temp0]
			z: local23[temp0]
			init:
		)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class wormOut(Sound):
	#property vars (may be empty)
	number = 462
	
#end:class or instance

@SCI.instance
class wormIn(Sound):
	#property vars (may be empty)
	number = 463
	
#end:class or instance

@SCI.instance
class rm460(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 460
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 handsOn:)
		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						319
						189
						0
						189
						0
						141
						42
						187
						92
						187
						130
						176
						164
						183
						189
						177
						228
						185
						317
						150
						317
						123
						243
						123
						229
						129
						199
						113
						193
						119
						170
						117
						172
						108
						255
						111
						305
						109
						298
						104
						269
						103
						258
						106
						242
						106
						232
						100
						194
						98
						178
						94
						162
						95
						155
						106
						125
						106
						104
						113
						69
						112
						44
						114
						15
						106
						19
						103
						89
						103
						90
						100
						0
						97
						0
						0
						319
						0
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						181
						132
						181
						136
						175
						142
						144
						143
						115
						140
						108
						134
						117
						129
						174
						129
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						308
						138
						302
						142
						291
						139
						286
						139
						282
						152
						267
						152
						265
						144
						259
						139
						243
						138
						240
						135
						247
						126
						304
						126
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 256 149 246 157 204 157 197 151 201 143 249 143
					yourself:
				)
		)
		(super init: &rest)
		localproc_0()
		(widow init:)
		kernel.Lock(143, modNum, 0)
		if (global12 == 461):
			(global0 posn: 74 182 loop: 2 setScale: Scaler 100 40 135 0 init:)
			(cond
				case (kernel.ScriptID(40, 0) spiderBit:):
					(global0 posn: 65 187)
					(global2 setScript: widowKillsAlex 0 801)
				#end:case
				case (kernel.ScriptID(40, 0) parchmentBit:):
					(global0 posn: 65 187)
					(global2 setScript: widowKillsAlex 0 802)
				#end:case
				case (kernel.ScriptID(40, 0) gotParchment:):
					(global0 posn: 59 172)
					(kernel.ScriptID(40, 0) gotParchment: 0)
					(global2 setScript: lookAtParchment)
				#end:case
				else:
					(global0 posn: 68 176)
					(global103 fade: 0 10 10)
					(global102
						number: 460
						setLoop: -1
						setVol: 0
						play:
						fade: 127 10 10
					)
				#end:else
			)
		else:
			(global2 setScript: egoEnters)
			(global102 number: 460 setLoop: -1 play:)
		#endif
		if (not proc913_0(136)):
			(scrapOfPaper init: stopUpd:)
		#endif
		(global32
			add:
				bookWormBookPile
				otherBookPiles
				oxymoronBookPile
				dipthongBookPile
				cBrownBookPile
				cLGreyBookPile
				cLBlueBookPile
				web
			eachElementDo: #init
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (global2 script:):#end:case
			case (global0 inRect: 29 177 112 189):
				(global2 setScript: widowKillsAlex 0 3)
			#end:case
			case (global0 edgeHit:):
				(global102 fade: 0 10 10)
				(global2 setScript: egoExits)
			#end:case
		)
		(super doit:)
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					posn: 1 135
					setScale: Scaler 100 40 135 0
					init:
					setMotion: PolyPath 16 135 self
				)
			#end:case
			case 1:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoExits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion: MoveTo ((global0 x:) - 25) (global0 y:) self
				)
			#end:case
			case 1:
				(global1 handsOn:)
				(global2 newRoom: 450)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bookworm(Prop):
	#property vars (may be empty)
	x = 140
	y = 139
	z = 40
	noun = 4
	view = 463
	loop = 5
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 94:
				(self setScript: 0)
				(global1 handsOff:)
				(participle4U start: 5)
				(global2 setScript: participle4U)
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			case 5:
				(super doVerb: param1 &rest)
			#end:case
			else:
				(global1 handsOff:)
				(self setScript: inventOnWorm 0 param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

class ScriptFeature(Feature):
	#property vars (may be empty)
	script = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 1)
		(super init: &rest)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(cond
					case (bookworm script:):
						(global91 say: 5 5 19 1)
					#end:case
					case (((global9 at: 29) owner:) == global11):
						(global91 say: 5 5 6 1)
					#end:case
					else:
						(global2 setScript: rummage 0 self)
					#end:else
				)
			#end:case
			case 2:
				(cond
					case (bookworm script:):
						(global91 say: 5 5 19 1)
					#end:case
					case (((global9 at: 29) owner:) == global11):
						(global91 say: 5 5 6 1)
					#end:case
					case (not proc913_0(40)):
						(global91 say: 5 2 7 1)
					#end:case
					case proc913_0(7):
						(global2 setScript: callBooks 0 0)
					#end:case
					else:
						proc913_1(60)
						(global2 setScript: callBooks 0 1)
					#end:else
				)
			#end:case
			case 94:
				(global1 handsOff:)
				(global2 setScript: participle4U)
			#end:case
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			else:
				(self setScript: inventOnBooks 0 param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bookWormBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 138
	y = 135
	noun = 5
	onMeCheck = 8
	approachX = 115
	approachY = 146
	
#end:class or instance

@SCI.instance
class otherBookPiles(ScriptFeature):
	#property vars (may be empty)
	x = 298
	y = 115
	noun = 5
	onMeCheck = 4
	approachX = 268
	approachY = 131
	
#end:class or instance

@SCI.instance
class cBrownBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 188
	y = 116
	noun = 5
	onMeCheck = 64
	approachX = 186
	approachY = 123
	
#end:class or instance

@SCI.instance
class cLGreyBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 230
	y = 153
	noun = 5
	onMeCheck = 128
	approachX = 233
	approachY = 163
	
#end:class or instance

@SCI.instance
class cLBlueBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 275
	y = 147
	noun = 5
	onMeCheck = 512
	approachX = 249
	approachY = 141
	
#end:class or instance

@SCI.instance
class oxymoronBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 84
	y = 107
	noun = 5
	onMeCheck = 2
	approachX = 66
	approachY = 120
	
#end:class or instance

@SCI.instance
class dipthongBookPile(ScriptFeature):
	#property vars (may be empty)
	x = 223
	y = 114
	noun = 5
	onMeCheck = 32
	approachX = 208
	approachY = 127
	
#end:class or instance

@SCI.instance
class rummage(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(register approachX:)
						(register approachY:)
						self
				)
			#end:case
			case 1:
				if (register == bookWormBookPile):
					(global0
						view: 461
						normal: 0
						posn: ((register approachX:) + 2) (register approachY:)
						setLoop: 4
						cel: 0
						cycleSpeed: 6
						setCycle: End self
					)
				else:
					(global0
						view: 467
						setLoop: (1 if (register == cLBlueBookPile) else 0)
						cel: 0
						normal: 0
						posn:
							((register approachX:) - 2)
							((register approachY:) + 1)
						cycleSpeed: 6
						setCycle: End self
					)
				#endif
			#end:case
			case 2:
				(global0 setCycle: Beg self)
			#end:case
			case 3:
				(global0
					posn: ((global0 x:) - 2) (global0 y:)
					reset: (0 if (register == cLBlueBookPile) else 6)
				)
				cycles = 8
			#end:case
			case 4:
				(cond
					case (not proc913_0(7)):
						(global2 setScript: handsOffTheGoods 0 register)
					#end:case
					case (not proc913_0(61)):
						(global2 setScript: askForParti 0 register)
					#end:case
					case (((global9 at: 36) owner:) == global11):
						(global2 setScript: anythingYet 0 register)
					#end:case
					else:
						(global1 handsOn:)
						(self dispose:)
					#end:else
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class handsOffTheGoods(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				proc913_1(40)
				if (register == bookWormBookPile):
					(self cue:)
				else:
					(global0 setMotion: PolyPath 107 142 self)
				#endif
				(wormOut play:)
				(bookworm init: setCycle: End)
			#end:case
			case 1:
				if (register != bookWormBookPile):
					(global0 setHeading: 45)
				#endif
				cycles = 10
			#end:case
			case 2:
				(bookworm setLoop: 4 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(bookworm setLoop: 5 cel: 14)
				cycles = 8
			#end:case
			case 4:
				(myConv add: -1 5 5 3 1 add: -1 5 5 3 2 init: self)
			#end:case
			case 5:
				(wormIn play:)
				(bookworm setLoop: 5 cel: 14 setCycle: Beg self)
			#end:case
			case 6:
				(global1 handsOn:)
				(bookworm dispose:)
				proc958_0(0, 1044, 1046, 1045, 1007)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class askForParti(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				proc913_1(40)
				proc913_1(61)
				(cond
					case (register == callBooks):
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(self cue:)
					#end:case
					case (register == bookWormBookPile):
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(self cue:)
					#end:case
					else:
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(global0 setMotion: PolyPath 107 142 self)
					#end:else
				)
			#end:case
			case 1:#end:case
			case 2:
				if (register != bookWormBookPile):
					(global0 setHeading: 45)
				#endif
				cycles = 10
			#end:case
			case 3:
				(bookworm setLoop: 4 cel: 0 setCycle: End self)
			#end:case
			case 4:
				(myConv
					add: -1 5 5 4 1
					add: -1 5 5 4 2
					add: -1 5 5 4 3
					add: -1 5 5 4 4
					add: -1 5 5 4 5
					init: self
				)
			#end:case
			case 5:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 6:
				(bookworm cel: 0)
				cycles = 4
			#end:case
			case 7:
				(global91 say: 5 5 4 6 self)
			#end:case
			case 8:
				(oxymoron init:)
				(self setScript: oxyOut self)
			#end:case
			case 9:
				(global91 say: 5 5 4 7 self)
			#end:case
			case 10:
				(self setScript: oxyIn self)
			#end:case
			case 11:
				(dipthong init:)
				(self setScript: dipthOut self)
			#end:case
			case 12:
				(global91 say: 5 5 4 8 self)
			#end:case
			case 13:
				(self setScript: dipthIn self)
			#end:case
			case 14:
				(myConv add: -1 5 5 4 9 add: -1 5 5 4 10 init: self)
			#end:case
			case 15:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 16:
				(bookworm cel: 0)
				seconds = 3
			#end:case
			case 17:
				(myConv add: -1 5 5 4 11 add: -1 5 5 4 12 init: self)
			#end:case
			case 18:
				if (global0 has: 29):
					(global1 handsOff:)
					(participle4U start: 5)
					(global2 setScript: participle4U)
				else:
					(bookworm setLoop: 2 cel: 0 setCycle: End self)
				#endif
			#end:case
			case 19:
				(bookworm cel: 0)
				cycles = 4
			#end:case
			case 20:
				(myConv add: -1 5 5 4 13 add: -1 5 5 4 14 init: self)
			#end:case
			case 21:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 22:
				(bookworm cel: 0)
				cycles = 4
			#end:case
			case 23:
				(myConv add: -1 5 5 4 15 add: -1 5 5 4 16 init: self)
			#end:case
			case 24:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 25:
				(bookworm cel: 0)
				cycles = 4
			#end:case
			case 26:
				(myConv add: -1 5 5 4 17 add: -1 5 5 4 18 init: self)
			#end:case
			case 27:
				(wormIn play:)
				(bookworm setLoop: 5 cel: 14 setCycle: Beg self)
			#end:case
			case 28:
				(global1 handsOn:)
				(bookworm dispose:)
				proc958_0(0, 1044, 1046, 1045, 1007)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class anythingYet(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(cond
					case (register == callBooks):
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(self cue:)
					#end:case
					case (register == bookWormBookPile):
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(self cue:)
					#end:case
					else:
						(wormOut play:)
						(bookworm init: setCycle: End self)
						(global0 setMotion: PolyPath 107 142 self)
					#end:else
				)
			#end:case
			case 1:#end:case
			case 2:
				if (register != bookWormBookPile):
					(global0 setHeading: 45)
				#endif
				cycles = 10
			#end:case
			case 3:
				(global91 say: 5 5 5 1 self)
			#end:case
			case 4:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 5:
				(bookworm cel: 0)
				cycles = 4
			#end:case
			case 6:
				if proc913_0(120):
					temp0 = kernel.Random(1, 5)
					(global91 say: 5 5 18 temp0 self)
				else:
					proc913_1(120)
					(self setScript: stupidOxyScript self)
				#endif
			#end:case
			case 7:
				(bookworm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 8:
				(bookworm cel: 0)
				cycles = 3
			#end:case
			case 9:
				(global91 say: 5 5 5 4 self)
			#end:case
			case 10:
				(global1 handsOn:)
				(bookworm setScript: waitForAnswer)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stupidOxyScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(oxymoron init:)
				(self setScript: oxyOut self)
			#end:case
			case 1:
				(global91 say: 5 5 5 2 self)
			#end:case
			case 2:
				(self setScript: oxyIn self)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waitForAnswer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(bookworm stopUpd:)
				seconds = 10
			#end:case
			case 1:
				(global1 handsOff:)
				(global0
					normal: 0
					view: 461
					setLoop: 3
					cel: 0
					normal: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 reset: 6)
				cycles = 8
			#end:case
			case 3:
				(global91 say: 1 0 2 1 self)
			#end:case
			case 4:
				(wormIn play:)
				(bookworm setLoop: 5 cel: 14 setCycle: Beg self)
			#end:case
			case 5:
				(bookworm dispose:)
				proc958_0(0, 1044, 1046, 1045, 1007)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class callBooks(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 107 142 self)
			#end:case
			case 1:
				(global0 setHeading: 90)
				cycles = 10
			#end:case
			case 2:
				if proc913_0(61):
					(global91 say: 5 2 5 1 self)
				else:
					(global91 say: 5 2 8 1 self)
				#endif
			#end:case
			case 3:
				(cond
					case (register == 1):
						(global2 setScript: talkGoAway)
					#end:case
					case proc913_0(61):
						(global2 setScript: anythingYet 0 self)
					#end:case
					case proc913_0(7):
						(global2 setScript: askForParti 0 self)
					#end:case
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkGoAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(wormOut play:)
				(bookworm init: setCycle: End self)
			#end:case
			case 1:
				(global91 say: 5 2 8 2 self)
			#end:case
			case 2:
				(wormIn play:)
				(bookworm setCycle: Beg self)
			#end:case
			case 3:
				(global1 handsOn:)
				(bookworm dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inventOnBooks(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					setMotion:
						PolyPath
						(client approachX:)
						(client approachY:)
						self
				)
			#end:case
			case 1:
				(= temp0
					kernel.GetAngle((global0 x:), (global0 y:), (client x:), (client y:))
				)
				(global0 setHeading: temp0 self)
			#end:case
			case 2:
				(global91 say: 5 0 0 1 self)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inventOnWorm(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if proc999_5(register, 25, 12, 66, 85, 34):
					(global91 say: 4 register 0 0 self)
				else:
					(global91 say: 4 0 0 0 self)
				#endif
			#end:case
			case 1:
				(wormIn play:)
				(bookworm setLoop: 5 setCycle: Beg self)
			#end:case
			case 2:
				(global1 handsOn:)
				(bookworm dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class parti(Actor):
	#property vars (may be empty)
	x = 124
	y = 136
	view = 468
	priority = 11
	signal = 16400
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class participle4U(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 98 134 self)
			#end:case
			case 1:
				(global0 setHeading: 90 self)
			#end:case
			case 2:
				(global91 say: 5 94 0 1 self)
			#end:case
			case 3:
				(wormOut play:)
				(bookworm init: setCycle: End self)
			#end:case
			case 4:
				(global91 say: 5 94 0 2 self)
			#end:case
			case 5:
				(global1 handsOff:)
				(global91 say: 4 94 0 1 self)
			#end:case
			case 6:
				(global0
					normal: 0
					view: 468
					setLoop: 1
					cel: 0
					cycleSpeed: 8
					posn: 96 136
					setPri: 12
					setCycle: End self
				)
			#end:case
			case 7:
				(parti init:)
				(bookworm setLoop: 3 cel: 0 setCycle: End self)
			#end:case
			case 8:
				(global0 posn: 98 134 reset: 0)
				(bookworm setLoop: 5 cel: 14)
				cycles = 8
			#end:case
			case 9:
				(myConv
					add: -1 4 94 0 2
					add: -1 4 94 0 3
					add: -1 4 94 0 4
					init: self
				)
			#end:case
			case 10:
				(oxymoron init:)
				(self setScript: oxyOut self)
			#end:case
			case 11:
				(global91 say: 4 94 0 5 self)
			#end:case
			case 12:
				(self setScript: oxyIn self)
			#end:case
			case 13:
				(dipthong init:)
				(self setScript: dipthOut self)
			#end:case
			case 14:
				(global91 say: 4 94 0 6 self)
			#end:case
			case 15:
				(self setScript: dipthIn self)
			#end:case
			case 16:
				(parti setCycle: End self)
			#end:case
			case 17:
				(myConv
					add: -1 4 94 0 7
					add: -1 4 94 0 8
					add: -1 4 94 0 9
					init: self
				)
			#end:case
			case 18:
				(parti dispose:)
				(wormIn play:)
				(bookworm setLoop: 5 cel: 14 setCycle: Beg self)
			#end:case
			case 19:
				(wormOut play:)
				(bookworm init: setLoop: 1 cel: 0 setCycle: End self)
				(global0 posn: 98 134 reset: 6 setMotion: PolyPath 109 154 self)
			#end:case
			case 20:
				(global0 setHeading: 45)
				cycles = 6
			#end:case
			case 21:#end:case
			case 22:
				(global91 say: 4 94 0 10 self)
			#end:case
			case 23:
				(global0
					normal: 0
					view: 461
					setLoop: 4
					cel: 0
					cycleSpeed: 6
					setCycle: End self
				)
			#end:case
			case 24:
				(global1 givePoints: 2)
				(wormIn play:)
				(bookworm setLoop: 5 setCycle: Beg self)
				(global0 cycleSpeed: 1 setCycle: Beg)
			#end:case
			case 25:
				(bookworm dispose:)
				(global91 say: 4 94 0 11 self)
			#end:case
			case 26:
				(global1 handsOn:)
				(global0 posn: 109 154 get: 36 put: 29 global11 reset: 6)
				proc958_0(0, 1044, 1046, 1045, 1007)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class widow(Prop):
	#property vars (may be empty)
	x = 70
	y = 189
	z = 35
	noun = 11
	approachX = 68
	approachY = 176
	view = 460
	loop = 5
	priority = 15
	signal = 16400
	cycleSpeed = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 1 2)
		if (global12 == 461):
			(self cel: 12)
		else:
			(self cel: 0)
		#endif
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: widowKillsAlex 0 803)
			#end:case
			case 1:
				(global2 newRoom: 461)
			#end:case
			case 2:
				(global2 newRoom: 461)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class web(Feature):
	#property vars (may be empty)
	x = 69
	y = 189
	noun = 8
	onMeCheck = 16
	approachX = 68
	approachY = 176
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 1 2)
		(super init: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global2 newRoom: 461)
			#end:case
			case 5:
				(global2 setScript: widowKillsAlex 0 804)
			#end:case
			case 2:
				(global2 newRoom: 461)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class scrapOfPaper(View):
	#property vars (may be empty)
	x = 92
	y = 147
	noun = 8
	approachX = 68
	approachY = 176
	view = 460
	priority = 15
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 1 0)
		(super init: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global2 newRoom: 461)
			#end:case
			case 5:
				(global2 setScript: widowKillsAlex 0 804)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class loveInset(View):
	#property vars (may be empty)
	x = 65
	y = 189
	z = 94
	view = 462
	loop = 4
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class lookAtParchment(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 12 5 12 1 self)
			#end:case
			case 2:
				(global0
					view: 462
					setLoop: 7
					cel: 0
					normal: 0
					cycleSpeed: 8
					posn: 61 174
					setCycle: CT 1 1 self
				)
			#end:case
			case 3:
				(global105 number: 468 setLoop: 1 play:)
				(scrapOfPaper dispose:)
				(global0 setCycle: End self)
				proc913_1(136)
			#end:case
			case 4:
				(loveInset init:)
				seconds = 6
			#end:case
			case 5:
				(loveInset dispose:)
				(global1 givePoints: 2)
				(global103 fade: 0 10 10 self)
				(global102
					number: 460
					setLoop: -1
					setVol: 0
					play:
					fade: 127 10 10
				)
				(global0
					setLoop: 3
					cel: 0
					cycleSpeed: 6
					posn: 58 173
					setCycle: End self
				)
			#end:case
			case 6: 0#end:case
			case 7:
				(global91 say: 12 5 12 2 self)
			#end:case
			case 8:
				(global0 posn: 59 172 reset: 2)
				(global1 handsOn:)
				proc913_1(57)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class widowKillsAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				match register
					case 801:
						(state += 2)
						(self cue:)
					#end:case
					case 802:
						(state += 2)
						(self cue:)
					#end:case
					case 803:
						(global91 say: 11 5 0 1 self)
					#end:case
					case 804:
						(global91 say: 8 5 0 1 self)
					#end:case
					case 3:
						(self cue:)
					#end:case
				#end:match
			#end:case
			case 1:
				(global0 setMotion: PolyPath 68 176 self)
			#end:case
			case 2:
				(global0 setMotion: MoveTo 65 187 self)
			#end:case
			case 3:
				if (register == 3):
					(global0
						view: 462
						setLoop: 0
						cel: 0
						normal: 0
						cycleSpeed: 8
						posn: 70 189
						setCycle: CT 8 1 self
					)
				else:
					(global0
						view: 462
						setLoop: 5
						cel: 0
						normal: 0
						cycleSpeed: 8
						posn: 65 189
						setCycle: End self
					)
				#endif
				(widow setCycle: End self)
			#end:case
			case 4:#end:case
			case 5:
				(widow setLoop: 6 cel: 0 posn: 68 162 z: 0)
				cycles = 3
			#end:case
			case 6:
				match register
					case 801:
						(global91 say: 9 5 0 2 self)
					#end:case
					case 802:
						(global91 say: 12 5 11 2 self)
					#end:case
					case 803:
						(global91 say: 11 5 0 2 self)
					#end:case
					case 804:
						(global91 say: 8 5 0 2 self)
					#end:case
					case 3:
						(global91 say: 8 3 0 1 self)
					#end:case
				#end:match
			#end:case
			case 7:
				match register
					case 801:
						(global91 say: 9 5 0 3 self)
					#end:case
					case 802:
						(global91 say: 12 5 11 3 self)
					#end:case
					case 803:
						(global91 say: 11 5 0 3 self)
					#end:case
					case 804:
						(global91 say: 8 5 0 3 self)
					#end:case
					case 3:
						(global91 say: 8 5 0 3 self)
					#end:case
				#end:match
			#end:case
			case 8:
				if (register == 3):
					(global0 view: 462 setLoop: 1 cel: 0 setCycle: End self)
				else:
					(self cue:)
				#endif
			#end:case
			case 9:
				(global103 stop:)
				(global102 number: 466 setLoop: 1 play: self)
				if (register == 3):
					(global0 view: 462 setLoop: 2 cel: 0 setCycle: End self)
				else:
					(global0
						view: 462
						setLoop: 6
						cel: 0
						posn: 63 187
						setCycle: End self
					)
				#endif
				(widow setCycle: End self)
			#end:case
			case 10:#end:case
			case 11:#end:case
			case 12:
				match register
					case 801:
						(global91 say: 9 5 0 4 self)
					#end:case
					case 802:
						(global91 say: 12 5 11 4 self)
					#end:case
					case 803:
						(global91 say: 11 5 0 4 self)
					#end:case
					else:
						(self cue:)
					#end:else
				#end:match
			#end:case
			case 13:
				(global1 handsOn:)
				(kernel.ScriptID(40, 0) spiderBit: 0)
				(kernel.ScriptID(40, 0) parchmentBit: 0)
				if (register == 3):
					proc0_1(4)
				else:
					proc0_1(3)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class aBee(Actor):
	#property vars (may be empty)
	noun = 14
	view = 460
	loop = 11
	signal = 26624
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(beeLine start: z)
		(self setStep: 12 10 setPri: 14 setScript: (beeLine new:))
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class beeLine(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client
					setCycle: Fwd
					setMotion: MoveTo kernel.Random(5, 50) kernel.Random(5, 60) self
				)
			#end:case
			case 1:
				(client
					setLoop: 13
					cel: 0
					posn: ((client x:) + 6) (client y:)
					setCycle: End self
				)
			#end:case
			case 2:
				(client
					setLoop: 12
					setCycle: Fwd
					posn: ((client x:) - 9) ((client y:) + 14)
				)
				ticks = 2
			#end:case
			case 3:
				(client setMotion: MoveTo kernel.Random(260, 310) kernel.Random(5, 60) self)
			#end:case
			case 4:
				(client
					setLoop: 14
					cel: 0
					posn: ((client x:) - 6) (client y:)
					setCycle: End self
				)
			#end:case
			case 5:
				(client
					setLoop: 11
					posn: ((client x:) + 12) ((client y:) + 14)
					setCycle: Fwd
				)
				ticks = 2
			#end:case
			case 6:
				(client setMotion: MoveTo kernel.Random(5, 50) kernel.Random(5, 60) self)
			#end:case
			case 7:
				(state -= 6)
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dipthong(Prop):
	#property vars (may be empty)
	x = 234
	y = 45
	noun = 6
	view = 460
	loop = 8
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class oxymoron(Prop):
	#property vars (may be empty)
	x = 279
	y = 57
	noun = 7
	view = 460
	loop = 7
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class oxyOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(oxymoron init: setCycle: CT 4 1 self)
			#end:case
			case 1:
				(oxyBook init:)
				(oxymoron cel: 5 posn: 284 34)
				cycles = 3
			#end:case
			case 2:
				(oxymoron cel: 6 posn: 281 23)
				cycles = 3
			#end:case
			case 3:
				(oxymoron cel: 7 posn: 280 23)
				(global105 number: 464 setLoop: 1 play:)
				cycles = 3
			#end:case
			case 4:
				(oxymoron stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dipthOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(dipthong init: setCycle: CT 4 1 self)
			#end:case
			case 1:
				(dipBook init:)
				(dipthong cel: 5 posn: 238 20)
				cycles = 3
			#end:case
			case 2:
				(dipthong cel: 6 posn: 234 13)
				cycles = 3
			#end:case
			case 3:
				(dipthong cel: 7 posn: 235 14)
				cycles = 3
				(global105 number: 464 setLoop: 1 play: self)
			#end:case
			case 4:
				(dipthong stopUpd:)
			#end:case
			case 5:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oxyIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(oxymoron cel: 6 posn: 281 23)
				cycles = 3
			#end:case
			case 1:
				(oxymoron cel: 5 posn: 284 34)
				cycles = 3
			#end:case
			case 2:
				(oxyBook dispose:)
				(oxymoron posn: 279 57 setCycle: Beg self)
			#end:case
			case 3:
				(oxymoron dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dipthIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(dipthong cel: 6 posn: 234 13)
				cycles = 3
			#end:case
			case 1:
				(dipthong cel: 5 posn: 238 20)
				cycles = 3
			#end:case
			case 2:
				(dipBook dispose:)
				(dipthong posn: 234 45 setCycle: Beg self)
			#end:case
			case 3:
				(dipthong dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oxyBook(View):
	#property vars (may be empty)
	x = 285
	y = 71
	noun = 7
	view = 460
	loop = 9
	cel = 2
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self stopUpd:)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class dipBook(Prop):
	#property vars (may be empty)
	x = 240
	y = 52
	noun = 6
	view = 460
	loop = 10
	cel = 2
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self stopUpd:)
		(super init:)
	#end:method

#end:class or instance

