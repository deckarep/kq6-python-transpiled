#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 605
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import Polygon

# Public Export Declarations
SCI.public_exports(
	rm605 = 0,
)

@SCI.instance
class rm605(KQ6Room):
	#property vars (may be empty)
	picture = 605
	north = 630
	autoLoad = 0
	
	@classmethod
	def init():
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 3,
					'init:', 295, 93, 305, 116, 246, 146, 261, 129, 241, 114, 137, 114, 106, 120, 140, 138, 99, 150, 42, 150, 31, 163, 54, 167, 319, 167, 319, 43, 255, 43, 255, 79,
					'yourself:'
				)
		)
		global0._send('init:', 'reset:', 4, 'setScale:')
		if (global12 == 630):
			global0._send('posn:', 302, 80)
		else:
			global0._send('posn:', 95, 167)
		#endif
		super._send('init:', &rest)
		if 
			KQ6Print._send(
				'addText:', r"""Would you like a ticket?""", 0, 0,
				'addButton:', 1, r"""YES""", 0, 10,
				'addButton:', 0, r"""NO""", 0, 25,
				'init:'
			)
			global0._send('get:', 28)
		#endif
		if 
			KQ6Print._send(
				'addText:', r"""How about a (deadman's) coin?""", 0, 0,
				'addButton:', 1, r"""YES""", 0, 10,
				'addButton:', 0, r"""NO""", 0, 25,
				'init:'
			)
			global0._send('get:', 7)
		#endif
		if 
			KQ6Print._send(
				'addText:', r"""Maybe a mirror? They're great for defeating spirits!""", 0, 0,
				'addButton:', 1, r"""YES""", 0, 22,
				'addButton:', 0, r"""NO""", 0, 37,
				'init:'
			)
			global0._send('get:', 24)
		#endif
		global1._send('handsOn:')
	#end:method

#end:class or instance

