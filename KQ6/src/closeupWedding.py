#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 745
import sci_sh
import kernel
import Main
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	closeupWedding = 0,
)

@SCI.instance
class closeupWedding(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		proc913_1(99)
		(global2 noun: 3)
		(kernel.ScriptID(80, 0) setFlag: 710 2048)
		(global93 addToFront: self)
		(global74 addToFront: self)
	#end:method

	@classmethod
	def setScript():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		seconds = 0
		(super setScript: &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				((global69 at: 0) == (global69 curIcon:))
				((param1 type:) & 0x1040)
			)
			(param1 claimed: 1)
			next = kernel.ScriptID(744, 1)
			(self cue:)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable:)
		(global93 delete: self)
		(global74 delete: self)
		(genieHead dispose: delete:)
		(vizierHead dispose: delete:)
		(saladinArm dispose: delete:)
		(alexHead dispose: delete:)
		(priestHead dispose: delete:)
		(saladinHead dispose: delete:)
		(glint1 dispose: delete:)
		(glint2 dispose: delete:)
		(global2 drawPic: 740)
		proc913_2(99)
		(global2 noun: 3)
		(global5 eachElementDo: #show eachElementDo: #stopUpd)
		(super dispose:)
		(global0 startUpd:)
		if proc913_0(156):
			(global0 posn: 149 144)
		#endif
		kernel.UnLoad(128, 160)
		kernel.UnLoad(128, 161)
		kernel.UnLoad(128, 902)
		kernel.UnLoad(129, 160)
		kernel.UnLoad(143, 160)
		kernel.DisposeScript(1005)
		kernel.DisposeScript(745)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global5 eachElementDo: #startUpd)
				(global69 disable:)
				cycles = 1
			#end:case
			case 1:
				(global5 eachElementDo: #hide)
				(global2 drawPic: 160)
				(global102 number: 740 loop: -1 play:)
				(vizierHead addToPic:)
				(saladinArm init: stopUpd:)
				(saladinHead init:)
				(alexHead init:)
				(priestHead init:)
				seconds = cycles = 2
			#end:case
			case 2:
				(global69 enable:)
			#end:case
			case 3:
				(kernel.ScriptID(740, 7)
					add: 160 1 0 1 1
					add: 160 1 0 1 2
					add: 160 1 0 1 3
					add: 160 1 0 1 4
					add: 160 1 0 1 5
					add: 160 1 0 1 6
					init: self
				)
			#end:case
			case 4:
				(glint1 init: setCycle: End self)
				(glint2 init: setCycle: End)
			#end:case
			case 5:
				(global102 number: 746 loop: -1 play:)
				(glint1 setCycle: Beg self)
				(glint2 setCycle: Beg)
			#end:case
			case 6:
				(kernel.ScriptID(740, 7) add: 160 1 0 1 7 add: 160 1 0 1 8 init: self)
			#end:case
			case 7:
				(glint1 dispose:)
				(glint2 dispose:)
				(genieHead init: cel: 0)
				cycles = 10
			#end:case
			case 8:
				kernel.DisposeScript(939)
				(saladinArm cel: 2 startUpd:)
				if (not register = (kernel.ScriptID(80, 0) tstFlag: 709 128)):
					(saladinArm setCycle: Beg self)
				else:
					(saladinArm setScript: drawSword self)
					cycles = 1
				#endif
			#end:case
			case 9:
				if (not register):
					next = 0
					(global91 say: 1 0 2 0 self 160)
				else:
					(global1 handsOn:)
					state.post('++')
				#endif
			#end:case
			case 10:
				(saladinArm setScript: 0 setCycle: End self)
			#end:case
			case 11:
				cycles = 3
			#end:case
			case 12:
				(global1 handsOff:)
				(global69 disable:)
				if (not next):
					if (not register):
						kernel.UnLoad(128, 738)
						(kernel.ScriptID(740, 5) view: 7424 loop: 0 cel: 0 setCycle: 0)
						next = kernel.ScriptID(742, 3)
					else:
						(kernel.ScriptID(744, 1) register: 29)
						next = kernel.ScriptID(744, 1)
					#endif
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showMirror(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(saladinHead dispose: delete:)
		(priestHead dispose: delete:)
		(alexHead dispose: delete:)
		(mirror dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(drawSword caller: 0)
				(saladinArm setScript: 0)
				if (saladinArm cel:):
					(saladinArm setCycle: Beg self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				(global91 say: 4 13 0 1 self 160)
			#end:case
			case 2:
				(genieHead init: cel: 1 setCycle: End)
				(mirror init: cel: 0 cycleSpeed: 15 setCycle: End self)
			#end:case
			case 3:
				(global1 givePoints: 3)
				(saladinArm addToPic:)
				(priestHead cel: 1 addToPic:)
				(saladinHead cel: 1 addToPic:)
				(alexHead cel: 1 addToPic:)
				(genieHead addToPic:)
				(mirror addToPic:)
				cycles = 18
			#end:case
			case 4:
				(global91 say: 4 13 0 2 self 160)
			#end:case
			case 5:
				(client seconds: 0 next: kernel.ScriptID(744, 0))
				(kernel.ScriptID(740, 5) view: 7424 loop: 0 cel: 0 setCycle: 0)
				(global69 disable:)
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showReplicaLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 7 56 0 0 self 160)
			#end:case
			case 1:
				(closeupWedding next: kernel.ScriptID(744, 1) changeState: 12)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class drawSword(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 4
			#end:case
			case 1:
				if ((saladinArm cel:) > 0):
					(saladinArm cel: ((saladinArm cel:) - 1) startUpd:)
					cycles = 2
				else:
					(self dispose:)
				#endif
			#end:case
			case 2:
				(saladinArm stopUpd:)
				state = -1
				cycles = 1
			#end:case
		#end:match
	#end:method

#end:class or instance

class CloseupProp(Prop):
	#property vars (may be empty)
	controlColor = 0
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				(super onMe: param1)
				(controlColor & kernel.OnControl(4, (param1 x:), (param1 y:)))
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class genieHead(CloseupProp):
	#property vars (may be empty)
	x = 147
	y = 58
	noun = 4
	modNum = 160
	view = 160
	loop = 1
	cel = 1
	priority = 9
	signal = 16
	controlColor = 2
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 33, 18):
				(global91 say: noun 18 0 0 0 modNum)
			#end:case
			case proc999_5(param1, 57, 58, 59, 60, 43):
				(kernel.ScriptID(740, 7) add: modNum noun 43 0 1)
				if (param1 != 43):
					(kernel.ScriptID(740, 7) add: modNum noun 57 0 1)
				else:
					(kernel.ScriptID(740, 7) add: modNum noun 43 0 2)
				#endif
				(kernel.ScriptID(740, 7) init:)
			#end:case
			case proc999_5(param1, 56, 2):
				(global1 handsOff:)
				(closeupWedding seconds: 0 next: kernel.ScriptID(744, 1))
				(global91 say: noun param1 0 0 closeupWedding modNum)
			#end:case
			case proc999_5(param1, 67, 63):
				(global1 handsOff:)
				proc913_1(156)
				(closeupWedding seconds: 0 next: kernel.ScriptID(744, 1))
				(global91 say: 4 67 0 0 closeupWedding 160)
			#end:case
			else:
				match param1
					case 13:
						(closeupWedding setScript: showMirror)
					#end:case
					else:
						(super doVerb: param1)
					#end:else
				#end:match
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class vizierHead(CloseupProp):
	#property vars (may be empty)
	x = 120
	y = 53
	noun = 7
	modNum = 160
	view = 160
	loop = 3
	controlColor = 4
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 33, 18):
				param1 = 65
				(super doVerb: 65)
			#end:case
			case proc999_5(param1, 57, 58, 59, 60, 43):
				param1 = 43
				(super doVerb: 43)
			#end:case
			case (param1 == 56):
				(closeupWedding setScript: showReplicaLamp)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class alexHead(CloseupProp):
	#property vars (may be empty)
	x = 51
	y = 50
	view = 160
	loop = 2
	controlColor = 8
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class priestHead(CloseupProp):
	#property vars (may be empty)
	x = 270
	y = 56
	noun = 8
	modNum = 160
	view = 160
	loop = 4
	controlColor = 32
	
#end:class or instance

@SCI.instance
class saladinArm(CloseupProp):
	#property vars (may be empty)
	x = 5
	y = 79
	noun = 5
	modNum = 160
	view = 160
	loop = 7
	cel = 3
	controlColor = 16
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 33, 18):
			(global91 say: noun 33 0 0 0 modNum)
		else:
			(super doVerb: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class saladinHead(View):
	#property vars (may be empty)
	x = 10
	y = 24
	view = 160
	loop = 5
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(saladinArm doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class mirror(Prop):
	#property vars (may be empty)
	x = 35
	y = 102
	view = 160
	cel = 2
	
#end:class or instance

@SCI.instance
class glint1(Prop):
	#property vars (may be empty)
	x = 179
	y = 47
	view = 902
	priority = 15
	signal = 24576
	cycleSpeed = 4
	
#end:class or instance

@SCI.instance
class glint2(Prop):
	#property vars (may be empty)
	x = 169
	y = 47
	view = 902
	priority = 15
	signal = 24576
	cycleSpeed = 4
	
#end:class or instance

