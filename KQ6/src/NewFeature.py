#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 83
import sci_sh
import kernel
import Main
import PolyPath
import Feature

class NewFeature(Feature):
	#property vars (may be empty)
	normal = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 addToFront: self)
		(global73 addToFront: self)
		(super init: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 delete: self)
		(global73 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(not normal)
				((param1 type:) & 0x4000)
				(self onMe: param1)
				(_approachVerbs & (global66 doit: (param1 message:)))
			)
			(CueObj state: 0 cycles: 0 client: self theVerb: (param1 message:))
			(self doSpecial: (CueObj theVerb:))
			(param1 claimed: 1)
			return
		else:
			(super handleEvent: param1)
		#endif
	#end:method

	@classmethod
	def doSpecial():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self cue:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setMotion: PolyPath approachX approachY CueObj)
	#end:method

#end:class or instance

