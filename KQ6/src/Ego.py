#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 988
import sci_sh
import kernel
import Main
import PolyPath
import Motion
import Actor

class Ego(Actor):
	#property vars (may be empty)
	signal = 8192
	edgeHit = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:')
		if (not cycler):
			self._send('setCycle:', Walk)
		#endif
	#end:method

	@classmethod
	def facingMe():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 1
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doit:')
		(= edgeHit
			(cond
				case (x <= 0): 4#end:case
				case (x >= 319): 2#end:case
				case (y >= 189): 3#end:case
				case (y <= global2._send('horizon:')): 1#end:case
				else: 0#end:else
			)
		)
	#end:method

	@classmethod
	def get(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < argc): # inline for
			global9._send('at:', param1[temp0])._send('moveTo:', self)
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def put(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if self._send('has:', param1):
			temp0 = global9._send('at:', param1)._send(
				'moveTo:', (-1 if (argc == 1) else param2)
			)
			if (global69 and (global69._send('curInvIcon:') == temp0)):
				global69._send(
					'curInvIcon:', 0,
					'disable:', global69._send('useIconItem:')._send('cursor:', 999, 'yourself:')
				)
			#endif
		#endif
	#end:method

	@classmethod
	def has(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = global9._send('at:', param1):
			temp0._send('ownedBy:', self)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = param1._send('type:')
		temp2 = param1._send('message:')
		(cond
			case (script and script._send('handleEvent:', param1)): 1#end:case
			case (temp1 & 0x0040):
				if ((temp0 = temp2 == 0) and (temp1 & 0x0004)):
					param1._send('claimed:')
					return
				#endif
				if 
					(and
						(temp1 & 0x0004)
						(temp0 == global80._send('prevDir:'))
						kernel.IsObject(mover)
					)
					temp0 = 0
				#endif
				global80._send('prevDir:', temp0)
				self._send('setDirection:', temp0)
				param1._send('claimed:', 1)
			#end:case
			case (temp1 & 0x4000):
				if (temp1 & 0x1000):
					match global67
						case 0:
							self._send(
								'setMotion:', MoveTo, param1._send('x:'), (param1._send('y:') + z)
							)
						#end:case
						case 1:
							self._send(
								'setMotion:', PolyPath, param1._send('x:'), (+
										param1._send('y:')
										z
									)
							)
						#end:case
						case 2:
							self._send(
								'setMotion:', PolyPath, param1._send('x:'), (+
										param1._send('y:')
										z
									), 0, 0
							)
						#end:case
					#end:match
					global80._send('prevDir:', 0)
					param1._send('claimed:', 1)
				else:
					super._send('handleEvent:', param1)
				#endif
			#end:case
			else:
				super._send('handleEvent:', param1)
			#end:else
		)
		param1._send('claimed:')
	#end:method

#end:class or instance

