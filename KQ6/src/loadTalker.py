#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 109
import sci_sh
import kernel
import System

# Public Export Declarations
SCI.public_exports(
	loadTalker = 0,
)

@SCI.instance
class loadTalker(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Load(128, 5)
		match param1
			case 260:
				kernel.Portrait(0, r"""FERRYM""")
			#end:case
			case 680:
				kernel.Portrait(0, r"""ALLARIA""")
			#end:case
			case 340:
				kernel.Portrait(0, r"""WINGG""")
				kernel.Portrait(0, r"""CELESTE""")
			#end:case
			case 240:
				kernel.Portrait(0, r"""LAMPSELL""")
			#end:case
			case 250:
				kernel.Portrait(0, r"""BEAUTPEA""")
			#end:case
			case 460:
				kernel.Portrait(0, r"""BOOKWORM""")
			#end:case
			case 780:
				kernel.Portrait(0, r"""JOLLO""")
			#end:case
			case 350:
				kernel.Portrait(0, r"""WINGG""")
			#end:case
			case 810:
				kernel.Portrait(0, r"""VIZIER""")
			#end:case
			case 280:
				kernel.Portrait(0, r"""PAWNSHOP""")
			#end:case
			case 140:
				kernel.Portrait(0, r"""CASSIMA""")
			#end:case
			case 220:
				kernel.Portrait(0, r"""SALADIN""")
				kernel.Portrait(0, r"""JOLLO""")
			#end:case
			case 870:
				kernel.Portrait(0, r"""CASSIMA""")
			#end:case
			case 820:
				kernel.Portrait(0, r"""JOLLO""")
			#end:case
			case 105:
				kernel.Portrait(0, r"""CASSIMA""")
				kernel.Portrait(0, r"""VALANICE""")
			#end:case
			case 160:
				kernel.Portrait(0, r"""SALADIN""")
			#end:case
			case 550:
				kernel.Portrait(0, r"""HEADDRU""")
			#end:case
			case 580:
				kernel.Portrait(0, r"""HEADDRU""")
			#end:case
			case 800:
				kernel.Portrait(0, r"""CASSIMA""")
				kernel.Portrait(0, r"""SALADIN""")
			#end:case
			case 600:
				kernel.Portrait(0, r"""ALLARIA""")
				kernel.Portrait(0, r"""CALIPHIM""")
			#end:case
			case 740:
				kernel.Portrait(0, r"""SALADIN""")
				kernel.Portrait(0, r"""ALLARIA""")
				kernel.Portrait(0, r"""CALIPHIM""")
				kernel.Portrait(0, r"""CASSIMA""")
				kernel.Portrait(0, r"""VIZIER""")
				kernel.Portrait(0, r"""GRAHAM""")
				kernel.Portrait(0, r"""CALIPHIM""")
				kernel.Portrait(0, r"""ROSELLA""")
				kernel.Portrait(0, r"""JOLLO""")
				kernel.Portrait(0, r"""VALANICE""")
			#end:case
			case 145:
				kernel.Portrait(0, r"""VIZIER""")
			#end:case
			case 710:
				kernel.Portrait(0, r"""JOLLO""")
			#end:case
			case 165:
				kernel.Portrait(0, r"""SALADIN""")
				kernel.Portrait(0, r"""CASSIMA""")
			#end:case
			case 450:
				kernel.Portrait(0, r"""SIGHT""")
				kernel.Portrait(0, r"""GNOMES""")
				kernel.Portrait(0, r"""SMELL""")
				kernel.Portrait(0, r"""SIGHT""")
				kernel.Portrait(0, r"""TOUCH""")
				kernel.Portrait(0, r"""TASTE""")
				kernel.Portrait(0, r"""SOUND""")
			#end:case
			case 150:
				kernel.Portrait(0, r"""SALADIN""")
				kernel.Portrait(0, r"""VIZIER""")
			#end:case
			case 540:
				kernel.Portrait(0, r"""BEAST""")
				kernel.Portrait(0, r"""PRINCE""")
				kernel.Portrait(0, r"""BEAUTESS""")
				kernel.Portrait(0, r"""BEAUTPEA""")
			#end:case
			case 290:
				kernel.Portrait(0, r"""FERRYM""")
			#end:case
			case 850:
				kernel.Portrait(0, r"""VIZIER""")
			#end:case
			case 380:
				kernel.Portrait(0, r"""WINGG""")
			#end:case
			case 270:
				kernel.Portrait(0, r"""BOOKSH""")
				kernel.Portrait(0, r"""JOLLO""")
			#end:case
			case 730:
				kernel.Portrait(0, r"""SALADIN""")
			#end:case
			case 180:
				kernel.Portrait(0, r"""CASSIMA""")
			#end:case
			case 440:
				kernel.Portrait(0, r"""CELESTE""")
			#end:case
			case 750:
				kernel.Portrait(0, r"""CASSIMA""")
				kernel.Portrait(0, r"""JOLLO""")
				kernel.Portrait(0, r"""VIZIER""")
			#end:case
		#end:match
		kernel.DisposeScript(109)
	#end:method

#end:class or instance

