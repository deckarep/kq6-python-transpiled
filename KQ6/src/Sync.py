#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 929
import sci_sh
import kernel
import Main
import Timer
import Motion
import System

class Sync(Obj):
	#property vars (may be empty)
	syncTime = -1
	syncCue = -1
	prevCue = -1
	syncNum = -1
	
	@classmethod
	def syncStart(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		kernel.DoSync(0, self, param1, param2, param3, param4, param5)
		if (syncCue != -1):
			prevCue = syncCue
			syncTime = 0
		#endif
	#end:method

	@classmethod
	def syncCheck():
		if 
			(and
				(syncCue != -1)
				((u<= syncTime global81) or (syncTime <= kernel.DoAudio(6)))
			)
			if ((0xfff0 & syncCue) == 0):
				prevCue = (| (prevCue & 0xfff0) syncCue)
			else:
				prevCue = syncCue
			#endif
			kernel.DoSync(1, self)
		#endif
	#end:method

	@classmethod
	def syncStop():
		prevCue = -1
		kernel.DoSync(2)
	#end:method

#end:class or instance

class ScriptSync(Obj):
	#property vars (may be empty)
	prevSignal = -1
	playing = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		if global82:
			self._send('cue:')
		#endif
		global82 = Sync._send('new:')._send(
			'init:',
			'syncStart:', param1, param2, param3, param4, param5
		)
		if (global82._send('prevCue:') != -1):
			playing = 1
			global6._send('add:', self)
		#endif
		Timer._send('setTicks:', self, kernel.DoAudio(1, param1, param2, param3, param4, param5))
	#end:method

	@classmethod
	def doit():
		if (global82._send('prevCue:') != -1):
			while True: #repeat
				if (global82._send('prevCue:') == -1):
					(break)
				#endif
				temp0 = global82._send('syncTime:')
				global82._send('syncCheck:')
				if (temp0 == global82._send('syncTime:')):
					(break)
				#endif
			#end:loop
			prevSignal = global82._send('prevCue:')
		#endif
	#end:method

	@classmethod
	def cue():
		kernel.Animate(global5._send('elements:'), 0)
		playing = 0
		prevSignal = 32767
		global6._send('delete:', self)
		if global82:
			global82._send('syncStop:', 'dispose:')
			global82 = 0
		#endif
	#end:method

#end:class or instance

class MouthSync(Cycle):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, *rest):
		super._send('init:', param1)
		if kernel.IsObject(global82):
			global82._send('syncStop:', 'dispose:')
		#endif
		global82 = Sync._send('new:')._send('syncStart:', param2, param3, param4, param5, param6)
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		if (global82._send('prevCue:') != -1):
			temp2 = global82._send('syncTime:')
			temp3 = 0
			while True: #repeat
				temp1 = global82._send('syncTime:')
				global82._send('syncCheck:')
				if (temp1 == global82._send('syncTime:')):
					(break)
				#endif
			#end:loop
			if 
				(and
					(temp2 != global82._send('syncTime:'))
					(client._send('cel:') != temp0 = (0x000f & global82._send('prevCue:')))
				)
				client._send('cel:', temp0)
			#endif
		else:
			completed = 1
			self._send('cycleDone:')
		#endif
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		if global82:
			global82._send('dispose:')
			global82 = 0
		#endif
	#end:method

	@classmethod
	def cue():
		if global82:
			global82._send('syncStop:', 'dispose:')
			global82 = 0
			if caller:
				caller._send('cue:')
				caller = 0
			#endif
		#endif
	#end:method

#end:class or instance

