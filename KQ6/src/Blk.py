#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 949
import sci_sh
import kernel
import System

class Blk(Obj):
	#property vars (may be empty)
	top = 0
	left = 0
	bottom = 0
	right = 0
	
	@classmethod
	def doit(param1 = None, *rest):
		(return
			(or
				(param1._send('brBottom:') <= top)
				(param1._send('brTop:') > bottom)
				(param1._send('brRight:') < left)
				(param1._send('brLeft:') >= right)
			)
		)
	#end:method

#end:class or instance

class Cage(Blk):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		(return
			(and
				(param1._send('brTop:') >= top)
				(param1._send('brLeft:') >= left)
				(param1._send('brBottom:') <= bottom)
				(param1._send('brRight:') <= right)
			)
		)
	#end:method

#end:class or instance

