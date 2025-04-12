#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 223
import sci_sh
import kernel
import Main
import Scaler
import Rev
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	slaveWomenScr = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local4 = None


@SCI.instance
class slave1(Actor):
	#property vars (may be empty)
	x = 137
	y = 124
	noun = 7
	view = 225
	signal = 18432
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self dispose:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self setCycle: Walk)
	#end:method

#end:class or instance

@SCI.instance
class slave2(Actor):
	#property vars (may be empty)
	x = 152
	y = 132
	noun = 7
	view = 225
	loop = 1
	signal = 18432
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self dispose:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self setCycle: Walk)
	#end:method

#end:class or instance

@SCI.instance
class slave3(Actor):
	#property vars (may be empty)
	x = 165
	y = 143
	noun = 7
	view = 225
	loop = 3
	signal = 18432
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self dispose:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self setCycle: Walk)
	#end:method

#end:class or instance

@SCI.instance
class slave4(Actor):
	#property vars (may be empty)
	x = 179
	y = 151
	noun = 7
	view = 225
	loop = 2
	signal = 18432
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self setCycle: Walk)
	#end:method

#end:class or instance

@SCI.instance
class slaveWomenScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local4 = (3 if (global153 == 3) else 4)
				local0[0] = (slave1 init: yourself:)
				local0[1] = (slave2 init: yourself:)
				local0[2] = (slave3 init: yourself:)
				local0[3] = (slave4 init: yourself:)
				cycles = 3
			#end:case
			case 1:
				(global91 say: 1 0 local4 1 self)
			#end:case
			case 2:
				temp0 = 0
				while (temp0 < 4): # inline for
					(local0[temp0]
						setMotion:
							MoveTo
							((local0[temp0] x:) - 19)
							((local0[temp0] y:) - 11)
							(self if (temp0 == 3) else 0)
					)
					# for:reinit
					temp0.post('++')
				#end:loop
			#end:case
			case 3:
				if (global153 == 5):
					(global91 say: 1 0 local4 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				if (global153 == 3):
					(kernel.ScriptID(220, 4)
						view: 725
						setLoop: 1
						setCycle: Rev
						setMotion:
							MoveTo
							((kernel.ScriptID(220, 4) x:) + 10)
							(kernel.ScriptID(220, 4) y:)
							self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 5:
				if (global153 == 3):
					(kernel.ScriptID(220, 4) setCycle: 0 setLoop: -1)
					(self setScript: kernel.ScriptID(220, 1) self 1)
				else:
					(self setScript: kernel.ScriptID(220, 7) self)
				#endif
			#end:case
			case 6:
				(kernel.ScriptID(220, 3) setPri: 7)
				(kernel.ScriptID(220, 4) setPri: 4)
				temp0 = 0
				while (temp0 < 4): # inline for
					(local0[temp0] setPri: 5)
					# for:reinit
					temp0.post('++')
				#end:loop
				(global91 say: 1 0 local4 (2 if (global153 == 3) else 3) self)
			#end:case
			case 7:
				(global91 say: 1 0 local4 (3 if (global153 == 3) else 4) self)
			#end:case
			case 8:
				(kernel.ScriptID(220, 4) stopUpd:)
				(local0[0] setMotion: MoveTo 104 94 self)
				(local0[1]
					setMotion: MoveTo (local0[0] x:) (local0[0] y:) self
				)
				(local0[2]
					setMotion: MoveTo (local0[1] x:) (local0[1] y:) self
				)
				(local0[3]
					setMotion: MoveTo (local0[2] x:) (local0[2] y:) self
				)
			#end:case
			case 9: 0#end:case
			case 10: 0#end:case
			case 11: 0#end:case
			case 12:
				(local0[0]
					setPri: 2
					setScale: Scaler 64 94 103 95
					setMotion: MoveTo 75 100 local0[0]
				)
				(local0[1] setMotion: MoveTo 104 94 self)
				(local0[2]
					setMotion: MoveTo (local0[1] x:) (local0[1] y:) self
				)
				(local0[3]
					setMotion: MoveTo (local0[2] x:) (local0[2] y:) self
				)
			#end:case
			case 13: 0#end:case
			case 14: 0#end:case
			case 15:
				(local0[1]
					setPri: 2
					setScale: Scaler 64 94 103 95
					setMotion: MoveTo 75 100 local0[1]
				)
				(local0[2] setMotion: MoveTo 104 94 self)
				(local0[3]
					setMotion: MoveTo (local0[2] x:) (local0[2] y:) self
				)
			#end:case
			case 16: 0#end:case
			case 17:
				(local0[2]
					setPri: 2
					setScale: Scaler 64 94 103 95
					setMotion: MoveTo 75 100 local0[2]
				)
				(local0[3] setMotion: MoveTo 104 94 self)
			#end:case
			case 18:
				(local0[3]
					setPri: 2
					setScale: Scaler 64 94 103 95
					setMotion: MoveTo 75 100 self
				)
			#end:case
			case 19:
				(local0[3] dispose:)
				cycles = 2
			#end:case
			case 20:
				if (global153 == 3):
					(kernel.ScriptID(220, 4)
						setCycle: Walk
						setMotion:
							MoveTo
							((kernel.ScriptID(220, 4) x:) - 10)
							(kernel.ScriptID(220, 4) y:)
					)
				#endif
				(kernel.ScriptID(220, 3) setPri: -1)
				(kernel.ScriptID(220, 4) setPri: -1)
				(script cue:)
			#end:case
			case 21:
				if (global153 == 3):
					(kernel.ScriptID(220, 4)
						view: 224
						setLoop: -1
						loop: 1
						cel: 0
						posn: 139 109
					)
					cycles = 2
				else:
					(self cue:)
				#endif
			#end:case
			case 22:
				if (global153 == 3):
					(global91 say: 1 0 local4 4 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 23:
				(global91 say: 1 0 local4 5 self)
			#end:case
			case 24:
				(kernel.ScriptID(220, 3) stopUpd:)
				(kernel.ScriptID(220, 4) stopUpd:)
				(kernel.ScriptID(220, 5) stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(223)
	#end:method

#end:class or instance

