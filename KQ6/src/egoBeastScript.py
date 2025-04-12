#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 84
import sci_sh
import kernel
import Main
import Kq6Sound
import KQ6Print
import n913
import Print
import Window
import Motion
import Game
import System

# Public Export Declarations
SCI.public_exports(
	egoBeastScript = 0,
)

@SCI.instance
class egoBeastScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff: killSound: 1)
				(global69 disable: 5 6)
				(localMusic2 loop: -1 number: 972 play:)
				(global91 say: 3 0 7 1 self 0)
			#end:case
			case 1:
				(global91 say: 3 0 7 2 self 0)
			#end:case
			case 2:
				(localMusic number: 974 play:)
				(global0
					view: 910
					normal: 0
					cycleSpeed: 10
					setLoop: 0
					setCycle: End self
				)
			#end:case
			case 3:
				(localMusic number: 974 play:)
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(localMusic number: 974 play:)
				(global0 setCycle: End self)
			#end:case
			case 5:
				(global91 say: 3 0 7 3 self 0)
			#end:case
			case 6:
				(global91 say: 3 0 7 4 self 0)
			#end:case
			case 7:
				(localMusic2 number: 973 loop: 1 play:)
				(global0 setLoop: 1 setCel: 0 cycleSpeed: 10 setCycle: End self)
			#end:case
			case 8:
				proc913_1(59)
				(KQ6Print
					say: 0 3 0 7 5 0 0 0
					posn: 10 30
					width: 289
					modeless: 1
					init:
				)
				seconds = 4
			#end:case
			case 9:
				if global25:
					(global25 dispose:)
				#endif
				(localMusic2 stop:)
				cycles = 1
			#end:case
			case 10:
				(Sounds eachElementDo: #stop)
				(localMusic flags: 1 number: 970 loop: 1 play:)
				(global5 eachElementDo: #hide)
				(global2 drawPic: 98 10)
				kernel.Message(0, 916, 0, 0, 2, 1, @temp1)
				kernel.Display(@temp1, 100, 30, 11, 106, 260, 102, 16, 105, global22, 101, 1)
				kernel.Display(@temp1, 100, 29, 10, 106, 260, 102, 47, 105, global22, 101, 1)
				(global0
					view: 910
					loop: 1
					cel: (global0 lastCel:)
					normal: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 151 97
					setMotion: 0
					show:
				)
				cycles = 2
			#end:case
			case 11:
				if (global90 & 0x0002):
					kernel.DoAudio(2, 916, 0, 0, 2, 1)
				#endif
				(global1 setCursor: global20)
				while True: #repeat
					match
						(= temp0
							(Print
								window: deathWindow
								posn: 70 130
								addButton: 1 r"""Restore""" 0 15
								addButton: 2 r"""Restart""" 70 15
								addButton: 3 r"""Quit""" 140 15
								init:
							)
						)
						case 1:
							(global1 restore:)
						#end:case
						case 2:
							(global1 restart: 1)
						#end:case
						case 3:
							global4 = 1
							(break)
						#end:case
					#end:match
				#end:loop
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deathWindow(SysWindow):
	#property vars (may be empty)
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		color = 47
		back = 0
		(super open: &rest)
	#end:method

#end:class or instance

@SCI.instance
class localMusic(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class localMusic2(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

