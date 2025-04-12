#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 952
import sci_sh
import kernel
import Main
import Print
import PolyPath
import System

# Public Export Declarations
SCI.public_exports(
	sysLogger = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	kernel.Format(@temp0, 952, 0, param2)
	kernel.FileIO(6, local0, @temp0)
	temp0 = 0
	match param1
		case 1:
			kernel.StrCpy(@temp0, (param3 if param3 else r""""""))
		#end:case
		case 2:
			kernel.Format(@temp0, 952, 1, param3)
		#end:case
		case 3:
			kernel.Format(@temp0, 952, 2, param3)
		#end:case
		case 4:
			kernel.Format(@temp0, 952, 3, param3)
		#end:case
		case 5:
			if param3:
				proc921_2(@temp0, 66, param3, 999)
			#endif
			temp41 = kernel.StrLen(@temp0)
		#end:case
		case 6:
			temp40 = kernel.GetTime(2)
			kernel.Format(@temp0, 952, 4, (temp40 >> 0x000b), (&
				(temp40 >> 0x0005)
				0x003f
			), ((temp40 & 0x001f) * 2))
		#end:case
		case 7:
			temp40 = kernel.GetTime(3)
			kernel.Format(@temp0, 952, 5, ((temp40 >> 0x0005) & 0x000f), (&
				temp40
				0x001f
			), (80 + (temp40 >> 0x0009)))
		#end:case
	#end:match
	kernel.StrCat(@temp0, r"""\0d\n""")
	kernel.FileIO(6, local0, @temp0)
	return temp41
#end:procedure

@SCI.instance
class sysLogger(Code):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp7 = global85
		global85 = 999
		(= temp8
			(= temp78
				(= temp108
					(= temp158
						(= temp198
							temp238 = temp278 = temp318 = temp358 = 0
						)
					)
				)
			)
		)
		if temp4 = (0 == kernel.StrLen(@global42)):
			while (not (< 0 kernel.StrLen(@temp78) 19)):

				(Print
					font: 999
					addText:
						r"""Enter drive letter, path, and your name\n(no extension, max 40 characters)"""
					addEdit: @temp78 40 0 20
					init:
				)
			#end:loop
			kernel.StrCpy(@global42, @temp78, 40)
		#endif
		kernel.Format(@temp78, 952, 6, @global42)
		if (-1 != local0 = kernel.FileIO(0, @temp78, 1)):
			kernel.FileIO(5, @temp138, 80, local0)
			kernel.FileIO(5, @temp48, 80, local0)
			kernel.FileIO(1, local0)
		else:
			temp138 = 0
			kernel.StrCpy(@temp48, r"""resource.cfg""")
		#endif
		if temp4:
			(Print
				font: 999
				addText: r"""Enter your login name\n(max 8 characters):"""
				addEdit: @temp138 12 0 20
				init:
			)
			kernel.StrAt(@temp138, 8, 0)
		#endif
		while
			(and
				(or
					(not temp4)
					(Print
						font: 999
						addText:
							r"""Enter configuration file name\n(or hit return to skip):"""
						addEdit: @temp48 30 0 20
						init:
					)
				)
				(-1 == local0 = kernel.FileIO(0, @temp48, 1))
				kernel.StrAt(@temp48, 0)
			):

			kernel.StrAt(@temp48, 0, 0)
		#end:loop
		if (-1 != local0):
			while kernel.FileIO(5, @temp8, 80, local0):

				
					(temp0 = 0)
					(temp3 = kernel.StrAt(@temp8, temp0) and proc999_5(temp3, 9, 32))
					(temp0.post('++'))
				#end:loop
				
					(temp1 = 0)
					(and
						temp3 = kernel.StrAt(@temp8, temp0)
						(not proc999_5(temp3, 61, 58, 9, 32))
					)
					(temp1.post('++'))
					
					kernel.StrAt(@temp108, temp1, temp3)
					temp0.post('++')
					# for:reinit
					temp1.post('++')
				#end:loop
				kernel.StrAt(@temp108, temp1, 0)
				if 
					(= temp5
						(cond
							case (0 == kernel.StrCmp(@temp108, r"""kbdDrv""")): @temp158#end:case
							case (0 == kernel.StrCmp(@temp108, r"""joyDrv""")): @temp198#end:case
							case (0 == kernel.StrCmp(@temp108, r"""videoDrv""")): @temp238#end:case
							case (0 == kernel.StrCmp(@temp108, r"""soundDrv""")): @temp278#end:case
							case (0 == kernel.StrCmp(@temp108, r"""mouseDrv""")): @temp318#end:case
							case (0 == kernel.StrCmp(@temp108, r"""audioDrv""")): @temp358#end:case
						)
					)
					while
						(and
							temp3 = kernel.StrAt(@temp8, temp0)
							proc999_5(temp3, 61, 58, 9, 32)
						):

						temp0.post('++')
					#end:loop
					temp1 = temp0
					temp2 = 0
					while temp3 = kernel.StrAt(@temp8, temp1):

						if proc999_5(temp3, 58, 92, 47):
							temp0 = (temp1 + 1)
						#endif
						if (temp3 == 46):
							temp2 = (temp1 - temp0)
						#endif
						temp1.post('++')
					#end:loop
					if (temp2 == 0):
						temp2 = (temp1 - temp0)
					#endif
					kernel.StrCpy(temp5, (@temp8 + temp0), temp2)
				#endif
			#end:loop
			kernel.FileIO(1, local0)
		#endif
		kernel.Format(@temp78, 952, 7, @global42)
		if 
			(and
				temp4
				(or
					(-1 == local0 = kernel.FileIO(0, @temp78, 1))
					(kernel.Format(@temp8, 952, 8, @temp78) and 0)
					(Print
						font: 999
						addText: @temp8
						addButton: 0 r"""Append to it""" 0 12
						addButton: 1 r"""Overwrite it""" 75 12
						saveCursor: 1
						init:
					)
				)
			)
			kernel.FileIO(1, local0)
			local0 = kernel.FileIO(0, @temp78, 2)
		else:
			local0 = kernel.FileIO(0, @temp78, 0)
		#endif
		if (-1 == local0):
			(Print
				font: 999
				addTextF: r"""Error: Couldn't open %s""" @temp78
				init:
			)
		else:
			localproc_0(1, r"""GAME""", (global1 name:))
			localproc_0(1, r"""VERSION""", global27)
			localproc_0(7, r"""QA-DATE""")
			localproc_0(1, r"""ANALYST""", @temp138)
			localproc_0(1, r"""SEVERITY""", (Print
				font: 999
				addText: r"""Severity of bug..."""
				addButton: r"""F""" r"""FATAL""" 0 12
				addButton: r"""N""" r"""NON-FATAL""" 40 12
				addButton: r"""S""" r"""SUGGESTION""" 110 12
				saveCursor: 1
				init:
			))
			temp0 = 1
			temp6 = 1
			while (temp0 <= 10):

				kernel.Format(@temp108, 952, 9, temp0)
				kernel.Format(@temp8, 952, 10, temp0, 10)
				if temp6:
					temp6 = localproc_0(5, @temp108, @temp8)
				else:
					localproc_0(1, @temp108, 0)
				#endif
				temp0.post('++')
			#end:loop
			localproc_0(1, r"""DEPARTMENT""", (Print
				font: 999
				addText: r"""Who can fix bug..."""
				addButton: r"""P""" r"""PROG""" 0 12
				addButton: r"""A""" r"""ART""" 40 12
				addButton: r"""D""" r"""DESIGN""" 80 12
				saveCursor: 1
				init:
			))
			localproc_0(2, r"""ROOM""", global11)
			temp0 = (global2 script:)
			localproc_0(1, r"""ROOM-SCRIPT""", (temp0 and (temp0 name:)))
			localproc_0(2, r"""ROOM-STATE""", (temp0 and (temp0 state:)))
			localproc_0(2, r"""EGO-X""", (global0 x:))
			localproc_0(2, r"""EGO-Y""", (global0 y:))
			localproc_0(2, r"""EGO-Z""", (global0 z:))
			temp0 = (global0 script:)
			localproc_0(1, r"""EGO-SCRIPT""", (temp0 and (temp0 name:)))
			localproc_0(2, r"""EGO-STATE""", (temp0 and (temp0 state:)))
			localproc_0(2, r"""EGO-VIEW""", (global0 view:))
			localproc_0(2, r"""EGO-LOOP""", (global0 loop:))
			localproc_0(2, r"""EGO-CEL""", (global0 cel:))
			localproc_0(2, r"""EGO-PRIORITY""", (global0 priority:))
			localproc_0(2, r"""EGO-HEADING""", (global0 heading:))
			localproc_0(1, r"""CYCLER""", (and
				(global0 cycler:)
				((global0 cycler:) name:)
			))
			temp0 = (global0 mover:)
			localproc_0(1, r"""EGO-MOVER""", (temp0 and (temp0 name:)))
			localproc_0(2, r"""MOVER-X""", (cond
				case (not temp0): 0#end:case
				case (temp0 isMemberOf: PolyPath):
					(temp0 finalX:)
				#end:case
				else:
					(temp0 x:)
				#end:else
			))
			localproc_0(2, r"""MOVER-Y""", (cond
				case (not temp0): 0#end:case
				case (temp0 isMemberOf: PolyPath):
					(temp0 finalY:)
				#end:case
				else:
					(temp0 y:)
				#end:else
			))
			localproc_0(2, r"""EGO-MOVESPD""", (global0 moveSpeed:))
			localproc_0(4, r"""SIGNAL-BITS""", (global0 signal:))
			localproc_0(4, r"""ILLEGAL-BITS""", (global0 illegalBits:))
			localproc_0(2, r"""HOWFAST""", global87)
			localproc_0(1, r"""ICONBAR""", (global69 and (global69 name:)))
			localproc_0(1, r"""CUR-ICON""", (and
				global69
				(global69 curIcon:)
				((global69 curIcon:) name:)
			))
			localproc_0(2, r"""DETAIL-LEVEL""", (global1 detailLevel:))
			localproc_0(2, r"""CD-AUDIO""", (global90 & 0x0002))
			localproc_0(1, r"""VIDEO-DRV""", @temp238)
			localproc_0(1, r"""SOUND-DRV""", @temp278)
			localproc_0(1, r"""AUDIO-DRV""", @temp358)
			localproc_0(1, r"""KEYBOARD-DRV""", @temp158)
			localproc_0(1, r"""JOY-DRV""", @temp198)
			localproc_0(1, r"""MOUSE""", @temp318)
			localproc_0(3, r"""LARGEST-HEAP""", kernel.MemoryInfo(0))
			localproc_0(3, r"""FREE-HEAP""", kernel.MemoryInfo(1))
			localproc_0(3, r"""TOTAL-HUNK""", (kernel.MemoryInfo(4) >> 0x0006))
			localproc_0(3, r"""LARGEST-HUNK""", kernel.MemoryInfo(2))
			localproc_0(3, r"""FREE-HUNK""", (kernel.MemoryInfo(3) >> 0x0006))
			kernel.FileIO(6, local0, r"""**********************************\0d\n""")
			kernel.FileIO(1, local0)
		#endif
		kernel.Format(@temp78, 952, 6, @global42)
		if 
			(and
				(-1 == local0 = kernel.FileIO(0, @temp78, 2))
				(-1 == local0 = kernel.FileIO(0, @temp78, 0))
			)
			(Print
				font: 999
				addTextF: r"""Error: Couldn't open memory file %s!""" @temp78
				init:
			)
		else:
			kernel.FileIO(6, local0, @temp138)
			kernel.FileIO(6, local0, r"""\n""")
			kernel.FileIO(6, local0, @temp48)
			kernel.FileIO(6, local0, r"""\n""")
			kernel.FileIO(1, local0)
		#endif
		global85 = temp7
		kernel.DisposeScript(952)
	#end:method

#end:class or instance

