#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 903
import sci_sh
import kernel
import Main
import EgoGroop
import KQ6Print
import Kq6Window
import Print
import Slider
import IconBar
import GameControls
import System

# Public Export Declarations
SCI.public_exports(
	kq6Controls = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class kq6Controls(GameControls):
	#property vars (may be empty)
	@classmethod
	def init():
		kernel.Load(128, 947)
		global63 = self
		self._send(
			'window:', controlWin._send(
					'top:', (((200 - (kernel.CelHigh(947, 1, 1) + 0)) / 2) - 15),
					'left:', (((320 - (+ 157 kernel.CelWide(947, 0, 1) 0)) / 2) - 10),
					'bottom:', (-
							(+
								kernel.CelHigh(947, 1, 1)
								0
								((200 - (kernel.CelHigh(947, 1, 1) + 0)) / 2)
								10
							)
							5
						),
					'right:', (+
							157
							kernel.CelWide(947, 0, 1)
							0
							((320 - (+ 157 kernel.CelWide(947, 0, 1) 0)) / 2)
							10
						),
					'back:', 19,
					'yourself:'
				),
			'add:', iconOk, iconTextSwitch._send(
					'theObj:', iconTextSwitch,
					'selector:', #doit,
					'yourself:'
				), iconSave._send('init:', 'theObj:', global1, 'selector:', #save, 'yourself:'), iconRestore._send(
					'init:',
					'theObj:', global1,
					'selector:', #restore,
					'yourself:'
				), iconRestart._send(
					'init:',
					'theObj:', global1,
					'selector:', #restart,
					'yourself:'
				), iconQuit._send(
					'init:',
					'theObj:', global1,
					'selector:', #quitGame,
					'yourself:'
				), iconAbout._send('init:', 'selector:', #doit, 'yourself:'), detailSlider._send(
					'init:',
					'theObj:', global1,
					'selector:', #detailLevel,
					'topValue:', 3,
					'bottomValue:', 0,
					'yStep:', 2,
					'yourself:'
				), volumeSlider._send(
					'init:',
					'theObj:', global1,
					'selector:', #masterVolume,
					'topValue:', 15,
					'bottomValue:', 0,
					'yStep:', 2,
					'yourself:'
				), speedSlider._send('init:', 'theObj:', 0, 'selector:', #y, 'yStep:', 2, 'yourself:'),
			'eachElementDo:', #highlightColor, 0,
			'eachElementDo:', #lowlightColor, 19,
			'curIcon:', iconRestore
		)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(934)
		kernel.DisposeScript(903)
	#end:method

#end:class or instance

@SCI.instance
class controlWin(Kq6Window):
	#property vars (may be empty)
	@classmethod
	def open():
		super._send('open:', &rest)
		priority = -1
		local0 = kernel.PicNotValid()
		kernel.PicNotValid(1)
		if 
			(not
				(= temp54
					if (global169 and (not kernel.Platform(5))):
						kernel.Platform(6)
					#endif
				)
			)
			kernel.DrawCel(947, 0, 7, (-
				(+
					(/
						(-
							(-
								(+ 157 kernel.CelWide(947, 0, 1) 0)
								(4 + kernel.CelWide(947, 1, 1))
							)
							kernel.CelWide(947, 0, 5)
						)
						2
					)
					4
					kernel.CelWide(947, 1, 1)
				)
				35
			), 12, -1, 0)
			local1 = 0
		#endif
		kernel.DrawCel(947, 1, 1, 14, 11, -1, 0)
		kernel.DrawCel(947, 1, 0, 106, 56, -1, 0)
		kernel.DrawCel(947, 1, 0, 149, 56, -1, 0)
		kernel.DrawCel(947, 1, 2, 104, (+ 0 (103 if (global107 == 256) else 104) 7), -1, 0)
		kernel.DrawCel(947, 0, 4, 75, ((30 - (kernel.CelHigh(947, 0, 4) + 0)) + 24), -1, 0)
		kernel.DrawCel(947, 0, 3, 115, ((30 - (kernel.CelHigh(947, 0, 4) + 0)) + 24), -1, 0)
		kernel.DrawCel(947, 0, 2, 162, ((30 - (kernel.CelHigh(947, 0, 4) + 0)) + 24), -1, 0)
		kernel.PicNotValid(local0)
		temp0 = kernel.GetPort()
		kernel.SetPort(0)
		kernel.Graph(12, top, left, bottom, right, 1)
		if temp54:
			(= temp55
				(+
					left
					(-
						(+
							(/
								(-
									(-
										(+ 157 kernel.CelWide(947, 0, 1) 0)
										(4 + kernel.CelWide(947, 1, 1))
									)
									kernel.CelWide(947, 0, 5)
								)
								2
							)
							4
							kernel.CelWide(947, 1, 1)
						)
						35
					)
				)
			)
			temp56 = (top + 18)
			(= local1
				kernel.Graph(15, temp56, temp55, (+
					(kernel.CelHigh(948, 12, 0) / 2)
					temp56
				), ((kernel.CelWide(948, 12, 0) / 2) + temp55))
			)
			kernel.DrawCel(948, 12, 0, 0, 0, -1, 0, local1)
		#endif
		kernel.SetPort(temp0)
		temp53 = global15
		kernel.DrawCel(947, 10, 0, (+
			(((+ 157 kernel.CelWide(947, 0, 1) 0) - (+ 10 kernel.CelWide(947, 1, 1) 6)) / 2)
			37
		), (+ 39 kernel.CelHigh(947, 0, 1) 3 17), -1, 0)
		temp51 = 93
		temp52 = 0
		while (temp52 < 3): # inline for
			(temp51 -= 7)
			if ((temp52 == 2) and ((mod temp53 10) == 0) and (not (global15 == 0))):
				temp50 = 11
			else:
				temp50 = (mod temp53 10)
			#endif
			(temp53 /= 10)
			kernel.DrawCel(947, 11, temp50, (+
				(((+ 157 kernel.CelWide(947, 0, 1) 0) - (+ 10 kernel.CelWide(947, 1, 1) 6)) / 2)
				temp51
			), (+ 39 kernel.CelHigh(947, 0, 1) 3 17), -1, 0)
			# for:reinit
			temp52.post('++')
		#end:loop
		kernel.DrawCel(947, 11, 10, (+
			(((+ 157 kernel.CelWide(947, 0, 1) 0) - (+ 10 kernel.CelWide(947, 1, 1) 6)) / 2)
			93
		), (+ 39 kernel.CelHigh(947, 0, 1) 3 17), -1, 0)
		temp51 = 123
		temp53 = global16
		temp52 = 0
		while (temp52 < 3): # inline for
			(temp51 -= 7)
			temp50 = (mod temp53 10)
			(temp53 /= 10)
			kernel.DrawCel(947, 11, temp50, (+
				(((+ 157 kernel.CelWide(947, 0, 1) 0) - (+ 10 kernel.CelWide(947, 1, 1) 6)) / 2)
				temp51
			), (+ 39 kernel.CelHigh(947, 0, 1) 3 17), -1, 0)
			# for:reinit
			temp52.post('++')
		#end:loop
		global1._send('setCursor:', global20)
	#end:method

	@classmethod
	def dispose():
		if local1:
			kernel.Graph(8, local1)
		#endif
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class detailSlider(Slider):
	#property vars (may be empty)
	view = 947
	loop = 0
	cel = 1
	signal = 128
	sliderView = 947
	topValue = 3
	
	@classmethod
	def show():
		nsLeft = 79
		nsTop = 55
		sRight = 0
		super._send('show:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class volumeSlider(Slider):
	#property vars (may be empty)
	view = 947
	loop = 0
	cel = 1
	signal = 128
	sliderView = 947
	topValue = 15
	
	@classmethod
	def show():
		view = 947
		nsLeft = 121
		sliderView = 947
		nsTop = 55
		sRight = 0
		super._send('show:', &rest)
	#end:method

	@classmethod
	def doit(param1 = None, *rest):
		if theObj:
			if (proc999_7(theObj, selector) != param1):
				proc999_7(theObj, selector, param1, &rest)
			else:
				proc999_7(theObj, selector)
			#endif
		#endif
	#end:method

#end:class or instance

@SCI.instance
class speedSlider(Slider):
	#property vars (may be empty)
	view = 947
	loop = 0
	cel = 1
	signal = 128
	sliderView = 947
	bottomValue = 15
	
	@classmethod
	def show():
		if (global0._send('looper:') and (global0._send('looper:') == EgoGroop)):
			topValue = global0._send('looper:')._send('speedState:')
			bottomValue = (topValue + 15)
		else:
			topValue = 0
			bottomValue = 15
		#endif
		nsLeft = 163
		nsTop = 55
		sRight = 0
		super._send('show:', &rest)
	#end:method

	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			global0._send('currentSpeed:', param1)
			global0._send('setSpeed:', global0._send('currentSpeed:'))
		#endif
		global0._send('currentSpeed:')
	#end:method

#end:class or instance

@SCI.instance
class iconSave(ControlIcon):
	#property vars (may be empty)
	view = 947
	loop = 2
	cel = 0
	message = 0
	signal = 451
	
	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (3 if (global107 == 256) else 4) 10)
		super._send('show:', &rest)
	#end:method

	@classmethod
	def init():
		nsLeft = 18
		nsTop = (+ 0 (3 if (global107 == 256) else 4) 10)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class iconRestore(ControlIcon):
	#property vars (may be empty)
	view = 947
	loop = 3
	cel = 0
	message = 0
	signal = 451
	
	@classmethod
	def init():
		nsLeft = 18
		nsTop = (+ 0 (23 if (global107 == 256) else 24) 10)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (23 if (global107 == 256) else 24) 10)
		super._send('show:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class iconRestart(ControlIcon):
	#property vars (may be empty)
	view = 947
	loop = 4
	cel = 0
	message = 0
	signal = 451
	
	@classmethod
	def init():
		nsLeft = 18
		nsTop = (+ 0 (43 if (global107 == 256) else 44) 10)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (43 if (global107 == 256) else 44) 10)
		super._send('show:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class iconTextSwitch(ControlIcon):
	#property vars (may be empty)
	view = 947
	cel = 0
	signal = 387
	
	@classmethod
	def show():
		if (global90 == 2):
			loop = 8
		else:
			loop = 9
		#endif
		nsLeft = 108
		nsTop = (+ 0 (103 if (global107 == 256) else 104) 10)
		super._send('show:', &rest)
	#end:method

	@classmethod
	def doit():
		(cond
			case (not kernel.FileIO(10, r"""KQ6CD""")):
				Print._send(
					'font:', global22,
					'addText:', r"""This button is reserved for the CD version of King's Quest VI""",
					'init:'
				)
			#end:case
			case (not kernel.DoAudio(9)):
				Print._send(
					'font:', global22,
					'addText:', r"""Sorry, but a sound card capable of playing samples is required to hear speech""",
					'init:'
				)
			#end:case
			else:
				match global90
					case 1:
						global90 = 2
					#end:case
					case 2:
						global90 = 1
					#end:case
				#end:match
				loop = (8 if (loop == 9) else 9)
			#end:else
		)
		self._send('show:')
	#end:method

#end:class or instance

@SCI.instance
class iconQuit(ControlIcon):
	#property vars (may be empty)
	view = 947
	loop = 5
	cel = 0
	message = 0
	signal = 451
	
	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (63 if (global107 == 256) else 64) 10)
		super._send('show:', &rest)
	#end:method

	@classmethod
	def init():
		nsLeft = 18
		nsTop = (+ 0 (63 if (global107 == 256) else 64) 10)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class iconAbout(ControlIcon):
	#property vars (may be empty)
	view = 947
	loop = 6
	cel = 0
	message = 0
	signal = 449
	
	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (83 if (global107 == 256) else 84) 10)
		super._send('show:', &rest)
	#end:method

	@classmethod
	def init():
		nsLeft = 18
		nsTop = (+ 0 (83 if (global107 == 256) else 84) 10)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def select():
		super._send('select:', &rest)
		global63._send('hide:')
		if global2._send('script:'):
			KQ6Print._send('font:', global22, 'say:', 0, 7, 0, 16, 0, 1, 0, 0, 0, 'init:')
		else:
			global2._send('setScript:', 905)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class iconOk(IconI):
	#property vars (may be empty)
	view = 947
	loop = 7
	cel = 0
	message = 0
	signal = 451
	
	@classmethod
	def show():
		nsLeft = 18
		nsTop = (+ 0 (103 if (global107 == 256) else 104) 10)
		super._send('show:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class helpCursor(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 4
	
#end:class or instance

