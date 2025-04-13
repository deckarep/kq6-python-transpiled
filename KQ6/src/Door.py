#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 954
import sci_sh
import kernel
import Main
import PolyPath
import Polygon
import Sound
import Motion
import Actor

class Door(Prop):
	#property vars (may be empty)
	entranceTo = 0
	locked = 0
	lockedCase = 0
	openSnd = 0
	closeSnd = 0
	openVerb = 0
	listenVerb = 0
	doubleDoor = 0
	forceOpen = 0
	forceClose = 1
	caller = 0
	moveToX = 0
	moveToY = 0
	enterType = 2
	exitType = 2
	closeScript = 0
	openScript = 0
	doorPoly = 0
	polyAdjust = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('approachVerbs:', openVerb, listenVerb)
		if (forceOpen or (global12 and (global12 == entranceTo))):
			state = 2
		#endif
		super._send('init:')
		self._send('createPoly:')
		self._send('ignoreActors:', 1)
		if (state == 0):
			cel = 0
			if doubleDoor:
				doubleDoor._send('setCel:', 0)
			#endif
		else:
			global95._send('delete:', doorPoly)
			cel = (kernel.NumCels(self) - 1)
			if doubleDoor:
				doubleDoor._send('setCel:', (kernel.NumCels(doubleDoor) - 1))
			#endif
		#endif
		if (state == 2):
			if closeScript:
				self._send('setScript:', closeScript)
			else:
				match enterType
					case 0:
						global0._send(
							'posn:', moveToX, moveToY,
							'setMotion:', PolyPath, approachX, approachY, self
						)
					#end:case
					case 1:
						global0._send(
							'edgeHit:', 0,
							'posn:', approachX, approachY,
							'setHeading:', heading
						)
						if forceClose:
							self._send('close:')
						#endif
					#end:case
					case 2:
						if forceClose:
							self._send('close:')
						#endif
					#end:case
				#end:match
			#endif
		else:
			self._send('stopUpd:')
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case openVerb:
				if (state == 2):
					self._send('close:')
				else:
					self._send('open:')
				#endif
			#end:case
			case listenVerb:
				self._send('listen:')
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if locked:
			if (modNum == -1):
				modNum = global11
			#endif
			global91._send('say:', noun, 0, lockedCase, 0, 0, modNum)
		else:
			if global80._send('controls:'):
				global1._send('handsOff:')
			#endif
			state = 1
			self._send('setCycle:', End, self)
			if openSnd:
				doorSound._send('number:', openSnd, 'play:')
			#endif
			if doubleDoor:
				doubleDoor._send('setCycle:', End)
			#endif
		#endif
	#end:method

	@classmethod
	def close():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		state = 3
		self._send('setCycle:', Beg, self)
		if closeSnd:
			doorSound._send('number:', closeSnd, 'play:')
		#endif
		if doubleDoor:
			doubleDoor._send('setCycle:', Beg)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state
			case 3:
				state = 0
				self._send('stopUpd:')
				global95._send('add:', doorPoly)
				if caller:
					caller._send('cue:')
				#endif
				if (not global80._send('controls:')):
					global1._send('handsOn:', 1)
				#endif
			#end:case
			case 1:
				state = 2
				self._send('stopUpd:')
				global95._send('delete:', doorPoly)
				if caller:
					caller._send('cue:')
				#endif
				if openScript:
					self._send('setScript:', openScript)
				else:
					match exitType
						case 0:
							if (moveToX or moveToY):
								global0._send(
									'illegalBits:', 0,
									'setMotion:', PolyPath, moveToX, moveToY, self
								)
							#endif
						#end:case
						case 1:
							if (moveToX or moveToY):
								global0._send(
									'setMotion:', PolyPath, moveToX, moveToY, self
								)
							#endif
						#end:case
						case 2:
							if (not global80._send('controls:')):
								global1._send('handsOn:', 1)
							#endif
						#end:case
					#end:match
				#endif
			#end:case
			else:
				(cond
					case 
						(and
							(global0._send('x:') == moveToX)
							(global0._send('y:') == moveToY)
						):
						(cond
							case entranceTo:
								match entranceTo
									case global2._send('north:'):
										global0._send('edgeHit:', 1)
									#end:case
									case global2._send('south:'):
										global0._send('edgeHit:', 3)
									#end:case
									case global2._send('west:'):
										global0._send('edgeHit:', 4)
									#end:case
									case global2._send('east:'):
										global0._send('edgeHit:', 2)
									#end:case
								#end:match
								global2._send('newRoom:', entranceTo)
							#end:case
							case forceClose:
								self._send('close:')
							#end:case
							case caller:
								caller._send('cue:')
							#end:case
						)
					#end:case
					case 
						(and
							(global0._send('x:') == approachX)
							(global0._send('y:') == approachY)
						):
						(cond
							case forceClose:
								self._send('close:')
							#end:case
							case caller:
								caller._send('cue:')
							#end:case
						)
					#end:case
				)
			#end:else
		#end:match
	#end:method

	@classmethod
	def listen():#end:method

	@classmethod
	def createPoly():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		doorPoly = Polygon._send('new:')._send('type:', 2, 'yourself:')
		if argc:
			doorPoly._send('init:', &rest)
		else:
			doorPoly._send(
				'init:', (brLeft - polyAdjust), (brBottom + polyAdjust), (-
						brLeft
						polyAdjust
					), (brTop - polyAdjust), (brRight + polyAdjust), (-
						brTop
						polyAdjust
					), (brRight + polyAdjust), (brBottom + polyAdjust)
			)
		#endif
		global95._send('add:', doorPoly)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global95._send('delete:', doorPoly)
		doorPoly._send('dispose:')
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class doorSound(Sound):
	#property vars (may be empty)
	flags = 1
	
#end:class or instance

