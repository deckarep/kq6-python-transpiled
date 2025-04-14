#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 902
import sci_sh
import kernel
import Main
import n913
import System

# Public Export Declarations
SCI.public_exports(
	ColorInit = 0,
)

@SCI.instance
class ColorInit(Code):
	#property vars (may be empty)
	@classmethod
	def init():
		if (kernel.Graph(2) > 16):
			proc913_1(48)
			global111 = kernel.Palette(5, 31, 31, 31)
			global112 = kernel.Palette(5, 63, 63, 63)
			global113 = kernel.Palette(5, 95, 95, 95)
			global114 = kernel.Palette(5, 127, 127, 127)
			global115 = kernel.Palette(5, 159, 159, 159)
			global116 = kernel.Palette(5, 191, 191, 191)
			global117 = kernel.Palette(5, 223, 223, 223)
			global118 = kernel.Palette(5, 151, 27, 27)
			global119 = kernel.Palette(5, 231, 103, 103)
			global120 = kernel.Palette(5, 235, 135, 135)
			global121 = kernel.Palette(5, 187, 187, 35)
			global122 = kernel.Palette(5, 219, 219, 39)
			global123 = kernel.Palette(5, 223, 223, 71)
			global124 = kernel.Palette(5, 27, 151, 27)
			global125 = kernel.Palette(5, 71, 223, 71)
			global126 = kernel.Palette(5, 135, 235, 135)
			global127 = kernel.Palette(5, 23, 23, 119)
			global128 = kernel.Palette(5, 35, 35, 187)
			global129 = kernel.Palette(5, 71, 71, 223)
			global130 = kernel.Palette(5, 135, 135, 235)
			global131 = kernel.Palette(5, 219, 39, 219)
			global132 = kernel.Palette(5, 27, 151, 151)
		else:
			global111 = 0
			global128 = 1
			global124 = 2
			global132 = 3
			global118 = 4
			global131 = 5
			global122 = 6
			global112 = 7
			global113 = 8
			global129 = 9
			global125 = 10
			global133 = 11
			global119 = 12
			global134 = 13
			global123 = 14
			global117 = 15
		#endif
	#end:method

#end:class or instance

