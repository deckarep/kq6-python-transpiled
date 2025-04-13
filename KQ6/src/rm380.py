#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 380
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm380 = 0,
)

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm380(KQ6Room):
	#property vars (may be empty)
	picture = 380
	style = 7
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global69._send(
			'enable:',
			'disable:', 0, 1, 2, 3, 4, 5, 6,
			'height:', -100,
			'activateHeight:', -100
		)
		Cursor._send('showCursor:', 0)
		global102._send('number:', 380, 'setLoop:', -1, 'play:')
		oracArm._send('init:', 'stopUpd:')
		egoBod._send('addToPic:')
		egoButt._send('addToPic:')
		global0._send(
			'view:', 3812,
			'normal:', 0,
			'posn:', 230, 152,
			'cycleSpeed:', 18,
			'setPri:', 14,
			'init:',
			'stopUpd:',
			'setScript:', goodNews
		)
		global1._send('givePoints:', 5)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('height:', 0, 'activateHeight:', 0)
		Cursor._send('showCursor:', 1)
		global0._send('setScale:', 0)
		global69._send('enable:', 6)
		global1._send('setCursor:', global21)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class oracArm(Prop):
	#property vars (may be empty)
	x = 94
	y = 87
	view = 3832
	signal = 16384
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class cassFace(Prop):
	#property vars (may be empty)
	x = 182
	y = 158
	view = 384
	signal = 16384
	
#end:class or instance

@SCI.instance
class deadHead(Prop):
	#property vars (may be empty)
	x = 164
	y = 125
	view = 3841
	signal = 16384
	cycleSpeed = 10
	
#end:class or instance

@SCI.instance
class flyer(Actor):
	#property vars (may be empty)
	view = 353
	signal = 24576
	
#end:class or instance

@SCI.instance
class egoBod(View):
	#property vars (may be empty)
	x = 230
	y = 152
	view = 381
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class egoButt(View):
	#property vars (may be empty)
	x = 232
	y = 191
	view = 381
	loop = 1
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class goodNews(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 4
			#end:case
			case 1:
				myConv._send(
					'add:', -1, 1, 0, 1, 2,
					'add:', -1, 1, 0, 1, 3,
					'add:', -1, 1, 0, 1, 4,
					'add:', -1, 1, 0, 1, 5,
					'add:', -1, 1, 0, 1, 6,
					'init:', self
				)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				oracArm._send('view:', 383, 'setCycle:', CT, 3, 1, self)
				kernel.UnLoad(128, 3832)
			#end:case
			case 4:
				global105._send('number:', 381, 'setLoop:', 1, 'play:')
				oracArm._send('setCycle:', End, self)
			#end:case
			case 5:
				oracArm._send('view:', 3832, 'cel:', 0, 'stopUpd:')
				kernel.UnLoad(128, 383)
				seconds = 1
			#end:case
			case 6:
				cassFace._send('init:', 'setCycle:', End, self)
				global105._send('number:', 382, 'setLoop:', 1, 'play:')
			#end:case
			case 7:
				cassFace._send('stopUpd:')
				ticks = 6
			#end:case
			case 8:
				seconds = 2
			#end:case
			case 9:
				myConv._send(
					'add:', -1, 1, 0, 1, 7,
					'add:', -1, 1, 0, 1, 8,
					'add:', -1, 1, 0, 1, 9,
					'init:', self
				)
			#end:case
			case 10:
				cassFace._send('startUpd:', 'setCycle:', Beg, self)
			#end:case
			case 11:
				myConv._send(
					'add:', -1, 1, 0, 1, 10,
					'add:', -1, 1, 0, 1, 11,
					'add:', -1, 1, 0, 1, 12,
					'add:', -1, 1, 0, 1, 13,
					'add:', -1, 1, 0, 1, 14,
					'add:', -1, 1, 0, 1, 15,
					'add:', -1, 1, 0, 1, 16,
					'add:', -1, 1, 0, 1, 17,
					'init:', self
				)
			#end:case
			case 12:
				seconds = 2
			#end:case
			case 13:
				cassFace._send('dispose:')
				oracArm._send('view:', 383, 'setCycle:', CT, 3, 1, self)
				kernel.UnLoad(128, 384)
				kernel.UnLoad(128, 3832)
			#end:case
			case 14:
				global105._send('number:', 381, 'setLoop:', 1, 'play:')
				oracArm._send('setCycle:', End, self)
			#end:case
			case 15:
				oracArm._send('view:', 3832, 'cel:', 0, 'stopUpd:')
				kernel.UnLoad(128, 383)
				seconds = 1
			#end:case
			case 16:
				deadHead._send('init:', 'setCycle:', End, self)
				global105._send('number:', 383, 'setLoop:', 1, 'play:')
			#end:case
			case 17:
				deadHead._send('dispose:')
				kernel.UnLoad(128, 3841)
				cycles = 6
			#end:case
			case 18:
				myConv._send(
					'add:', -1, 1, 0, 1, 18,
					'add:', -1, 1, 0, 1, 19,
					'add:', -1, 1, 0, 1, 20,
					'add:', -1, 1, 0, 1, 21,
					'init:', self
				)
			#end:case
			case 19:
				global105._send('stop:')
				ticks = 6
			#end:case
			case 20:
				global91._send('say:', 1, 0, 1, 22, self)
			#end:case
			case 21:
				oracArm._send('view:', 3831, 'posn:', 158, 82, 'setCycle:', CT, 5, 1, self)
				kernel.UnLoad(128, 383)
			#end:case
			case 22:
				global105._send('number:', 924, 'setLoop:', 1, 'play:')
				oracArm._send('view:', 3831, 'posn:', 158, 82, 'setCycle:', CT, 10, 1, self)
			#end:case
			case 23:
				global0._send(
					'view:', 3811,
					'setLoop:', 0,
					'cel:', 2,
					'posn:', (global0._send('x:') - 2), global0._send('y:')
				)
				cycles = 6
			#end:case
			case 24:
				global0._send('setCycle:', CT, 3, 1, self)
				oracArm._send('cel:', 11)
			#end:case
			case 25:
				global0._send('cel:', 4)
				cycles = 6
			#end:case
			case 26:
				oracArm._send('view:', 3832, 'posn:', 94, 87, 'cel:', 0, 'stopUpd:')
				kernel.UnLoad(128, 3831)
				global0._send(
					'view:', 3812,
					'cel:', 0,
					'posn:', (global0._send('x:') + 2), global0._send('y:'),
					'stopUpd:'
				)
				seconds = 1
			#end:case
			case 27:
				global91._send('say:', 1, 0, 1, 23, self)
			#end:case
			case 28:
				cycles = 6
			#end:case
			case 29:
				global91._send('say:', 1, 0, 1, 24, self)
			#end:case
			case 30:
				proc913_1(3)
				global0._send('get:', 40)
				oracArm._send('dispose:')
				global1._send('givePoints:', 1)
				global0._send('hide:')
				egoBod._send('dispose:')
				egoButt._send('dispose:')
				global2._send('setScript:', flyToBeach)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flyToBeach(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global2._send('drawPic:', 350, 10)
				flyer._send('setScale:', Scaler, 5, 4, 190, 0)
				ticks = 4
			#end:case
			case 1:
				flyer._send(
					'posn:', 174, 14,
					'setLoop:', 1,
					'setCycle:', Fwd,
					'setScale:', Scaler, 50, 5, 19, 14,
					'init:',
					'setMotion:', MoveTo, 174, 19, self
				)
			#end:case
			case 2:
				flyer._send(
					'setScale:', Scaler, 50, 49, 190, 0,
					'setMotion:', MoveTo, 180, -10, self
				)
			#end:case
			case 3:
				global2._send('newRoom:', 300)
			#end:case
		#end:match
	#end:method

#end:class or instance

