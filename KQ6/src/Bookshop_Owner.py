#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1034
import sci_sh
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Bookshop_Owner = 33,
)

@SCI.instance
class Bookshop_Owner(Kq6Talker):
	#property vars (may be empty)
	name = r"""Bookshop Owner"""
	x = 5
	y = 5
	view = 897
	talkWidth = 213
	textX = 76
	textY = 8
	raveName = r"""BOOKSH"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: tBust tEyes tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 897
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 31
	nsLeft = 28
	view = 897
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 42
	nsLeft = 31
	view = 897
	loop = 1
	
#end:class or instance

