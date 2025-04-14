#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 948
import sci_sh
import kernel
import Main
import Interface
import Print
import Dialog
import Feature
import Window
import File
import Actor
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local50
local80
local180
local280
local380 = r""" WALK____________"""
local381 = [r""" LOOK____________""", r""" DO______________""", r""" TALK____________""", r""" ASK_____________""", r""" HELP____________""", r""""""]
local387 = None
local388 = 1
local389 = None
local390 = None
local391 = None
local392 = None
local393 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	param1._send('sightAngle:', proc255_1(r"""sight angle?""", 40))
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	proc921_0(r"""Click left mouse button on top left corner""")
	while (temp0 = Event._send('new:')._send('type:') != 1):

		temp0._send('dispose:')
	#end:loop
	kernel.GlobalToLocal(temp0)
	temp3 = temp0._send('y:')
	temp4 = temp0._send('x:')
	temp0._send('dispose:')
	proc921_0(r"""Click left mouse button on bottom right corner""")
	while (temp0 = Event._send('new:')._send('type:') != 1):

		temp0._send('dispose:')
	#end:loop
	kernel.GlobalToLocal(temp0)
	temp5 = temp0._send('y:')
	temp6 = temp0._send('x:')
	temp0._send('dispose:')
	temp1 = (((temp6 - temp4) / 2) + temp4)
	temp2 = (((temp5 - temp3) / 2) + temp3)
	param1._send(
		'x:', temp1,
		'y:', temp2,
		'nsLeft:', temp4,
		'nsTop:', temp3,
		'nsBottom:', temp5,
		'nsRight:', temp6
	)
	if local388:
		kernel.Graph(4, temp3, temp4, temp3, temp6, 1, 0)
		kernel.Graph(4, temp5, temp4, temp5, temp6, 1, 0)
		kernel.Graph(4, temp3, temp4, temp5, temp4, 1, 0)
		kernel.Graph(4, temp3, temp6, temp5, temp6, 1, 0)
		kernel.Graph(12, temp3, temp4, (temp5 + 1), (temp6 + 1), 1)
	#endif
#end:procedure

@SCI.procedure
def localproc_2(param1 = None, *rest):
	param1._send(
		'view:', proc255_1(r"""View?""", global2._send('curPic:')),
		'loop:', proc255_1(r"""Loop?""", 0),
		'cel:', proc255_1(r"""Cel?""", 0),
		'signal:', 16400,
		'priority:', 15,
		'init:'
	)
	if param1._send('respondsTo:', #illegalBits):
		param1._send('illegalBits:', 0)
	#endif
	while (temp0 = Event._send('new:')._send('type:') != 1):

		kernel.GlobalToLocal(temp0)
		param1._send('posn:', temp0._send('x:'), temp0._send('y:'))
		kernel.Animate(global5._send('elements:'), 0)
		temp0._send('dispose:')
	#end:loop
	temp0._send('dispose:')
#end:procedure

@SCI.procedure
def localproc_3(param1 = None, *rest):
	if 
		Print._send(
			'addText:', r"""Where should the approach point be?""",
			'addButton:', 1, r"""Select with mouse""", 0, 20,
			'addButton:', 0, r"""Default to x, y""", 0, 34,
			'init:'
		)
		while (temp0 = Event._send('new:')._send('type:') != 1):

			temp0._send('dispose:')
		#end:loop
		kernel.GlobalToLocal(temp0)
		param1._send('approachX:', temp1 = temp0._send('x:'), 'approachY:', temp2 = temp0._send('y:'))
		temp0._send('dispose:')
		kernel.Graph(4, (temp2 - 1), (temp1 - 1), (temp2 - 1), (temp1 + 1), 7)
		kernel.Graph(4, temp2, (temp1 - 1), temp2, (temp1 + 1), 7)
		kernel.Graph(4, (temp2 + 1), (temp1 - 1), (temp2 + 1), (temp1 + 1), 7)
		kernel.Graph(4, temp2, temp1, temp2, temp1, 0)
		kernel.Graph(12, (temp2 - 1), (temp1 - 1), (temp2 + 2), (temp1 + 2), 1)
	else:
		param1._send('approachX:', param1._send('x:'), 'approachY:', param1._send('y:'))
	#endif
	temp3 = 0
	(= temp13
		Print._send(
			'addText:', r"""How far away must ego""", 0, 1,
			'addText:', r"""be before he tries to approach?""", 0, 12,
			'addEdit:', @temp3, 5, -50, 13,
			'addButton:', 1, r"""Select with mouse""", 0, 32,
			'addButton:', 0, r"""Always approach""", 0, 45,
			'init:'
		)
	)
	(cond
		case temp3:
			param1._send('approachDist:', kernel.ReadNumber(@temp3))
		#end:case
		case (not temp13):
			param1._send('approachDist:', 0)
		#end:case
		else:
			while (temp0 = Event._send('new:')._send('type:') != 1):

				temp0._send('dispose:')
			#end:loop
			kernel.GlobalToLocal(temp0)
			temp1 = temp0._send('x:')
			temp2 = temp0._send('y:')
			param1._send(
				'approachDist:', kernel.GetDistance(param1._send('x:'), param1._send('y:'), temp1, temp2)
			)
			temp0._send('dispose:')
			kernel.Graph(4, (temp2 - 1), (temp1 - 1), (temp2 - 1), (temp1 + 1), 28)
			kernel.Graph(4, temp2, (temp1 - 1), temp2, (temp1 + 1), 28)
			kernel.Graph(4, (temp2 + 1), (temp1 - 1), (temp2 + 1), (temp1 + 1), 28)
			kernel.Graph(4, temp2, temp1, temp2, temp1, 52)
			kernel.Graph(12, (temp2 - 1), (temp1 - 1), (temp2 + 2), (temp1 + 2), 1)
		#end:else
	)
#end:procedure

@SCI.procedure
def localproc_4():
	(= local391
		Print._send(
			'addText:', r"""doVerb method?""",
			'addButton:', 1, r"""YES""", 0, 12,
			'addButton:', 0, r"""NO""", 50, 12,
			'init:'
		)
	)
#end:procedure

@SCI.procedure
def localproc_5(param1 = None, *rest):
	local393._send('name:', @global42, 'writeString:', param1, 'close:')
#end:procedure

class Class_948_0
	#property vars (may be empty)
	@classmethod
	def doit():
		global1._send('setCursor:', 999)
		local392 = global38
		global38 = wfWin
		if (not local389):
			temp0 = 0
			kernel.Format(@temp0, r"""%d.fea""", global2._send('curPic:'))
			if (not proc921_2(@temp0, 30, r"""Enter path and filename""")):
				return
			else:
				kernel.Format(@global42, @temp0)
				(= local388
					Print._send(
						'addText:', r"""Outline Features?""",
						'addTitle:', r"""Feature Write V1.0""",
						'addButton:', 1, r"""YES""", 0, 12,
						'addButton:', 0, r"""NO""", 50, 12,
						'init:'
					)
				)
				(= local387
					Print._send(
						'addText:', r"""Display code to screen? (but not doVerb)""",
						'addTitle:', r"""Feature Write V1.0""",
						'addButton:', 0, r"""NO""", 0, 18,
						'addButton:', 1, r"""YES""", 50, 18,
						'init:'
					)
				)
				local389 = 1
			#endif
		#endif
		if 
			(not
				(= local390
					Print._send(
						'addText:', r"""Class?""",
						'addTitle:', r"""Feature Writer V1.0""",
						'addButton:', Feature, r"""Feature""", 0, 12,
						'addButton:', View, r"""View""", 73, 12,
						'addButton:', Prop, r"""Prop""", 113, 12,
						'addButton:', Actor, r"""Actor""", 153, 12,
						'init:'
					)
				)
			)
			return
		#endif
		temp15 = local390._send('new:')
		local0 = 0
		proc921_2(@local0, 30, r"""Name?""")
		local50 = 0
		proc921_2(@local50, 16, r"""Noun?""")
		localproc_0(temp15)
		if (local390 == Feature):
			localproc_1(temp15)
		else:
			localproc_2(temp15)
		#endif
		localproc_3(temp15)
		if 
			Print._send(
				'addText:', r"""Z property""",
				'addTitle:', r"""Feature Writer V1.0""",
				'addButton:', 0, r"""NO""", 0, 12,
				'addButton:', 1, r"""YES""", 50, 12,
				'init:'
			)
			Print._send(
				'addText:', r"""Click mouse on object's projection""",
				'addText:', r"""onto the ground""", 0, 12,
				'init:'
			)
			while (temp16 = Event._send('new:')._send('type:') != 1):

				temp16._send('dispose:')
			#end:loop
			kernel.GlobalToLocal(temp16)
			temp15._send('z:', (temp16._send('y:') - temp15._send('y:')))
			temp15._send('y:', temp16._send('y:'))
			temp16._send('dispose:')
		#endif
		localproc_4()
		Class_948_1._send('doit:', temp15)
		global38 = local392
	#end:method

#end:class or instance

class Class_948_1
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		if kernel.FileIO(10, @global42):
			kernel.Format(@temp492, r"""The file '%s' already exists""", @global42)
			if 
				(not
					(= temp491
						Print._send(
							'addText:', @temp492,
							'addButton:', 1, r"""Replace""", 0, 20,
							'addButton:', 2, r"""Append""", 73, 20,
							'addButton:', 0, r"""Cancel""", 133, 20,
							'init:'
						)
					)
				)
				return 0
			#endif
		#endif
		temp490 = (2 if (temp491 == 1) else 0)
		if (not local393 = File._send('new:')._send('name:', @global42, 'open:', temp490)):
			kernel.Format(@temp0, r"""Error opening '%s'""", @global42)
			proc921_0(@temp0)
			local393._send('dispose:')
			return 0
		#endif
		temp0 = 0
		if param1._send('isMemberOf:', Feature):
			kernel.Format(@temp400, r""" \t\tnsLeft\t\t\t%d\0d\n\t\tnsTop\t\t\t\t%d\0d\n\t\tnsBottom\t\t\t%d\0d\n\t\tnsRight\t\t\t%d\0d\n""", param1._send(
				'nsLeft:'
			), param1._send('nsTop:'), param1._send('nsBottom:'), param1._send(
				'nsRight:'
			))
			kernel.Format(@temp592, r"""..\\msg\\%d.shm""", global2._send('curPic:'))
			shmFile._send('name:', @temp592)
			if (not shmFile._send('open:', 1)):
				temp604 = 0
			else:
				temp605 = 0
				while (temp605 <= kernel.StrLen(@local50)): # inline for
					if (< 96 kernel.StrAt(@local50, temp605) 123):
						temp628 = (kernel.StrAt(@local50, temp605) - 32)
						kernel.StrAt(@local50, temp605, temp628)
					#endif
					# for:reinit
					temp605.post('++')
				#end:loop
				temp604 = 0
				while (kernel.FileIO(5, @temp552, 80, shmFile._send('handle:')) != -1):

					if (not kernel.StrCmp(@temp552, r"""(define""", 6)):
						temp605 = 0
						while (temp605 <= 40): # inline for
							temp552[temp605] = temp552[(temp605 + 4)]
							# for:reinit
							temp605.post('++')
						#end:loop
						if (not kernel.StrCmp(@temp552, @local50, kernel.StrLen(@local50))):
							temp606 = 0
							
								(temp605 = ((kernel.StrLen(@local50) / 2) + 1))
								(temp605 < 20)
								(temp605.post('++'))
								
								temp607[temp606] = temp552[temp605]
								temp606.post('++')
								# for:reinit
								temp605.post('++')
							#end:loop
							temp604 = kernel.ReadNumber(@temp607)
							(break)
						#endif
					#endif
					if (not kernel.StrCmp(@temp552, r"""; CASES""")):
						(break)
					#endif
				#end:loop
				shmFile._send('close:')
			#endif
			temp627 = Feature._send('new:')
			temp627._send(
				'init:',
				'setName:', @local0,
				'nsLeft:', param1._send('nsLeft:'),
				'nsTop:', param1._send('nsTop:'),
				'nsBottom:', param1._send('nsBottom:'),
				'nsRight:', param1._send('nsRight:'),
				'x:', param1._send('x:'),
				'y:', param1._send('y:'),
				'z:', param1._send('z:'),
				'heading:', param1._send('heading:'),
				'sightAngle:', param1._send('sightAngle:'),
				'approachX:', param1._send('approachX:'),
				'approachY:', param1._send('approachY:'),
				'noun:', temp604
			)
		else:
			kernel.Format(@temp400, r""" \t\tview\t\t\t%d\0d\n\t\tloop\t\t\t%d\0d\n\t\tcel\t\t\t%d\0d\n""", param1._send(
				'view:'
			), param1._send('loop:'), param1._send('cel:'))
		#endif
		kernel.Format(@temp440, r""" \t\tapproachX\t\t%d\0d\n\t\tapproachY\t\t%d\0d\n\t\tapproachDist\t%d\0d\n\t\t\_approachVerbs\t$%x\0d\n""", param1._send(
			'approachX:'
		), param1._send('approachY:'), param1._send('approachDist:'), param1._send(
			'_approachVerbs:'
		))
		kernel.Format(@temp0, r""" \0d\n(instance %s of %s\0d\n\t(properties\0d\n\t\tx\t\t\t\t\t%d\0d\n\t\ty\t\t\t\t\t%d\0d\n\t\tz\t\t\t\t\t%d\0d\n\t\theading\t\t\t%d\0d\n%s \t\tsightAngle\t\t%d\0d\n%s \t\tnoun\t\t\t\t%s\0d\n\t)\0d\n""", @local0, param1._send(
				'-super-:'
			)._send(
			'name:'
		), param1._send('x:'), param1._send('y:'), param1._send('z:'), param1._send(
			'heading:'
		), @temp400, param1._send('sightAngle:'), @temp440, @local50)
		if local387:
			Print._send(
				'font:', 999,
				'addText:', @temp0,
				'addTitle:', r"""Feature Writer V1.0""",
				'init:'
			)
		#endif
		localproc_5(@temp0)
		if local391:
			kernel.Format(@temp0, r""" \t(method (doVerb theVerb)\0d\n\t\t(switch theVerb\0d\n""")
			localproc_5(@temp0)
			if local180[0]:
				kernel.Format(@temp0, r""" \t\t\t(LOOK\0d\n\t\t\t)\0d\n""", @local180)
				localproc_5(@temp0)
			#endif
			if local80[0]:
				kernel.Format(@temp0, r""" \t\t\t(DO\0d\n\t\t\t)\0d\n""", @local80)
				localproc_5(@temp0)
			#endif
			if local280[0]:
				kernel.Format(@temp0, r""" \t\t\t(TALK\0d\n\t\t\t)\0d\n""", @local280)
				localproc_5(@temp0)
			#endif
			kernel.Format(@temp0, r""" \t\t\t(else\0d\n\t\t\t\t(super doVerb: theVerb)\0d\n\t\t\t)\0d\n\t\t)\0d\n\t)\0d\n""")
			localproc_5(@temp0)
		#endif
		kernel.StrCpy(@temp0, r""")\0d\n""")
		localproc_5(@temp0)
		if param1._send('isMemberOf:', Feature):
			param1._send('dispose:')
		else:
			param1._send('addToPic:')
		#endif
		local393._send('close:', 'dispose:')
		kernel.DisposeScript(993)
		return kernel.DisposeScript(948)
	#end:method

	@classmethod
	def writeList(param1 = None, *rest):
		param1._send('eachElementDo:', #perform, self)
		Class_948_0._send('doit:')
		kernel.DisposeScript(948)
	#end:method

#end:class or instance

@SCI.instance
class selectorI(DSelector):
	#property vars (may be empty)
	x = 18
	
	@classmethod
	def handleEvent(param1 = None, *rest):
		super._send('handleEvent:', param1)
		temp0 = param1._send('type:')
		temp1 = param1._send('message:')
		if 
			(or
				((temp0 == 1) and param1._send('claimed:'))
				((temp0 == 4) and (temp1 == 32))
			)
			if (kernel.StrAt(cursor, 0) == 62):
				kernel.StrAt(cursor, 0, 32)
			else:
				kernel.StrAt(cursor, 0, 62)
			#endif
			self._send('draw:')
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

#end:class or instance

@SCI.instance
class clearBut(DButton):
	#property vars (may be empty)
	state = 1
	text = r"""Clear"""
	
	@classmethod
	def doit():
		temp0 = 0
		while (temp0 < 6): # inline for
			kernel.StrAt(local380, (temp0 * 18), 32)
			# for:reinit
			temp0.post('++')
		#end:loop
		selectorI._send('draw:')
	#end:method

#end:class or instance

@SCI.instance
class allBut(DButton):
	#property vars (may be empty)
	state = 1
	value = 2
	text = r"""__All__"""
	
	@classmethod
	def doit():
		temp0 = 0
		while (temp0 < 6): # inline for
			kernel.StrAt(local380, (temp0 * 18), 62)
			# for:reinit
			temp0.post('++')
		#end:loop
		selectorI._send('draw:')
	#end:method

#end:class or instance

@SCI.instance
class doneBut(DButton):
	#property vars (may be empty)
	value = 1
	text = r""" Done """
	
#end:class or instance

@SCI.instance
class wfWin(Window):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class shmFile(File):
	#property vars (may be empty)
#end:class or instance

