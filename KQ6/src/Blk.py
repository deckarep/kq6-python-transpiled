#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 949
import sci_sh
import System

class Blk(Obj):
	#property vars (may be empty)
	top = 0
	left = 0
	bottom = 0
	right = 0
	
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				((param1 brBottom:) <= top)
				((param1 brTop:) > bottom)
				((param1 brRight:) < left)
				((param1 brLeft:) >= right)
			)
		)
	#end:method

#end:class or instance

class Cage(Blk):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				((param1 brTop:) >= top)
				((param1 brLeft:) >= left)
				((param1 brBottom:) <= bottom)
				((param1 brRight:) <= right)
			)
		)
	#end:method

#end:class or instance

