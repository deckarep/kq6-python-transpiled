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
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: openVerb listenVerb)
		if (forceOpen or (global12 and (global12 == entranceTo))):
			state = 2
		#endif
		(super init:)
		(self createPoly:)
		(self ignoreActors: 1)
		if (state == 0):
			cel = 0
			if doubleDoor:
				(doubleDoor setCel: 0)
			#endif
		else:
			(global95 delete: doorPoly)
			cel = (kernel.NumCels(self) - 1)
			if doubleDoor:
				(doubleDoor setCel: (kernel.NumCels(doubleDoor) - 1))
			#endif
		#endif
		if (state == 2):
			if closeScript:
				(self setScript: closeScript)
			else:
				match enterType
					case 0:
						(global0
							posn: moveToX moveToY
							setMotion: PolyPath approachX approachY self
						)
					#end:case
					case 1:
						(global0
							edgeHit: 0
							posn: approachX approachY
							setHeading: heading
						)
						if forceClose:
							(self close:)
						#endif
					#end:case
					case 2:
						if forceClose:
							(self close:)
						#endif
					#end:case
				#end:match
			#endif
		else:
			(self stopUpd:)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case openVerb:
				if (state == 2):
					(self close:)
				else:
					(self open:)
				#endif
			#end:case
			case listenVerb:
				(self listen:)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if locked:
			if (modNum == -1):
				modNum = global11
			#endif
			(global91 say: noun 0 lockedCase 0 0 modNum)
		else:
			if (global80 controls:):
				(global1 handsOff:)
			#endif
			state = 1
			(self setCycle: End self)
			if openSnd:
				(doorSound number: openSnd play:)
			#endif
			if doubleDoor:
				(doubleDoor setCycle: End)
			#endif
		#endif
	#end:method

	@classmethod
	def close():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		state = 3
		(self setCycle: Beg self)
		if closeSnd:
			(doorSound number: closeSnd play:)
		#endif
		if doubleDoor:
			(doubleDoor setCycle: Beg)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state
			case 3:
				state = 0
				(self stopUpd:)
				(global95 add: doorPoly)
				if caller:
					(caller cue:)
				#endif
				if (not (global80 controls:)):
					(global1 handsOn: 1)
				#endif
			#end:case
			case 1:
				state = 2
				(self stopUpd:)
				(global95 delete: doorPoly)
				if caller:
					(caller cue:)
				#endif
				if openScript:
					(self setScript: openScript)
				else:
					match exitType
						case 0:
							if (moveToX or moveToY):
								(global0
									illegalBits: 0
									setMotion: PolyPath moveToX moveToY self
								)
							#endif
						#end:case
						case 1:
							if (moveToX or moveToY):
								(global0
									setMotion: PolyPath moveToX moveToY self
								)
							#endif
						#end:case
						case 2:
							if (not (global80 controls:)):
								(global1 handsOn: 1)
							#endif
						#end:case
					#end:match
				#endif
			#end:case
			else:
				(cond
					case 
						(and
							((global0 x:) == moveToX)
							((global0 y:) == moveToY)
						):
						(cond
							case entranceTo:
								match entranceTo
									case (global2 north:):
										(global0 edgeHit: 1)
									#end:case
									case (global2 south:):
										(global0 edgeHit: 3)
									#end:case
									case (global2 west:):
										(global0 edgeHit: 4)
									#end:case
									case (global2 east:):
										(global0 edgeHit: 2)
									#end:case
								#end:match
								(global2 newRoom: entranceTo)
							#end:case
							case forceClose:
								(self close:)
							#end:case
							case caller:
								(caller cue:)
							#end:case
						)
					#end:case
					case 
						(and
							((global0 x:) == approachX)
							((global0 y:) == approachY)
						):
						(cond
							case forceClose:
								(self close:)
							#end:case
							case caller:
								(caller cue:)
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
		argc = sum(v is not None for v in locals().values())

		doorPoly = ((Polygon new:) type: 2 yourself:)
		if argc:
			(doorPoly init: &rest)
		else:
			(doorPoly
				init:
					(brLeft - polyAdjust)
					(brBottom + polyAdjust)
					(brLeft - polyAdjust)
					(brTop - polyAdjust)
					(brRight + polyAdjust)
					(brTop - polyAdjust)
					(brRight + polyAdjust)
					(brBottom + polyAdjust)
			)
		#endif
		(global95 add: doorPoly)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global95 delete: doorPoly)
		(doorPoly dispose:)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class doorSound(Sound):
	#property vars (may be empty)
	flags = 1
	
#end:class or instance

