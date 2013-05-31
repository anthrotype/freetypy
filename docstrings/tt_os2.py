# -*- coding: utf-8 -*-

# Copyright (c) 2013, Michael Droettboom All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and
# documentation are those of the authors and should not be interpreted
# as representing official policies, either expressed or implied, of
# the FreeBSD Project.

from __future__ import print_function, unicode_literals, absolute_import

TT_OS2__init__ = """
Information about the TrueType font, used on OS/2 and Microsoft
Windows.

Note that we now support old Mac fonts which do not include an OS/2
table.  In this case, the `version` field is always set to 0xFFFF.
"""

TT_OS2_version = """
The version of the `TT_OS2` table.

If this table was synthesized from a font that has no OS/2 table, the
version is set to 0xFFFF.
"""

TT_OS2_x_avg_char_width = """
Specifies the arithmetic average of the advance width of all of the 26
lowercase letters of the Latin alphabet and the space character. If
any of the 26 lowercase letters are not present, this parameter should
equal zero.

This parameter is a descriptive attribute of the font that specifies
the spacing of characters used for comparing one font to another for
selection or substitution. For proportionally spaced fonts, this value
is useful in estimating the length for lines of text.
"""

TT_OS2_weight_class = """
Indicates the visual weight (degree of blackness or thickness of
strokes) of the characters in the font.
"""

TT_WEIGHT_CLASS = """
|freetypy| Weight values for the `TT_OS2.usWeightClass` property.

- `ULTRA_LIGHT`

- `EXTRA_LIGHT`

- `LIGHT`

- `SEMI_LIGHT`

- `MEDIUM` (aliased to `NORMAL`)

- `SEMI_BOLD`

- `BOLD`

- `EXTRA_BOLD`

- `ULTRA_BOLD`
"""

TT_OS2_width_class = """
Indicates a relative change from the normal aspect ratio (width to
height ratio) as specified by a font designer for the glyphs in a
font.

Although every character in a font may have a different numeric aspect
ratio, each character in a font of normal width has a relative aspect
ratio of one. When a new type style is created of a different width
class (either by a font designer or by some automated means) the
relative aspect ratio of the characters in the new font is some
percentage greater or less than those same characters in the normal
font it is this difference that this parameter specifies.
"""

TT_WIDTH_CLASS = """
|freetypy| Width values for the `TT_OS2.usWidthClass` property.

- `ULTRA_CONDENSED`: 50% of normal

- `EXTRA_CONDENSED`: 62.5% of normal

- `CONDENSED`: 75% of normal

- `SEMI_CONDENSED`: 87.5% of normal

- `MEDIUM`: 100% of normal (aliased to `NORMAL`)

- `SEMI_EXPANDED`: 112.5% of normal

- `EXPANDED`: 125% of normal

- `EXTRA_EXPANDED`: 150% of normal

- `ULTRA_EXPANDED`: 200% of normal
"""

TT_OS2_type = """
`FSTYPE` bitflags indicating the licensing restrictions on a font.
"""

TT_OS2_y_subscript_x_size = """
Maps to the em square size of the font being used for a subscript.  If
a font has two recommended sizes for subscripts, e.g., numerics and
other, the numeric sizes should be stressed.  The horizontal font size
specifies a font designer's recommended horizontal font size for
subscript characters associated with this font. If a font does not
include all of the required subscript characters for an application,
and the application can substitute characters by scaling the character
of a font or by substituting characters from another font, this
parameter specifies the recommended em square for those subscript
characters.  For example, if the em square for a font is 2048 and
`y_subscript_x_size` is set to 205, then the horizontal size for a
simulated subscript character would be 1/10th the size of the normal
character.
"""

TT_OS2_y_subscript_y_size = """
Maps to the emHeight of the font being used for a subscript.  If a
font has two recommended sizes for subscripts, e.g. numerics and
other, the numeric sizes should be stressed. The horizontal font size
specifies a font designer's recommendation for horizontal font size of
subscript characters associated with this font. If a font does not
include all of the required subscript characters for an application,
and the application can substitute characters by scaling the
characters in a font or by substituting characters from another font,
this parameter specifies the recommended horizontal EmInc for those
subscript characters.  For example, if the em square for a font is
2048 and `y_subScript_y_size` is set to 205, then the vertical size
for a simulated subscript character would be 1/10th the size of the
normal character.
"""

TT_OS2_y_subscript_x_offset = """
Specifies a font designer's recommended horizontal offset for
subscript characters. It is from the character origin of the font to
the character origin of the subscript's character. If a font does not
include all of the required subscript characters for an application,
and the application can substitute characters, this parameter
specifies the recommended horizontal position from the character
escapement point of the last character before the first subscript
character. For upright characters, this value is usually zero;
however, if the characters of a font have an incline (italic
characters) the reference point for subscript characters is usually
adjusted to compensate for the angle of incline.
"""

TT_OS2_y_subscript_y_offset = """
Specifies a font designer's recommended vertical offset from the
character baseline to the character baseline for subscript characters
associated with this font. Values are expressed as a positive offset
below the character baseline. If a font does not include all of the
required subscript for an application, this parameter specifies the
recommended vertical distance below the character baseline for those
subscript characters.
"""

TT_OS2_y_superscript_x_size = """
Maps to the em square size of the font being used for a subscript.  If
a font has two recommended sizes for subscripts, e.g., numerics and
other, the numeric sizes should be stressed.  The horizontal font size
specifies a font designer's recommended horizontal font size for
superscript characters associated with this font. If a font does not
include all of the required superscript characters for an application,
and the application can substitute characters by scaling the character
of a font or by substituting characters from another font, this
parameter specifies the recommended em square for those superscript
characters.  For example, if the em square for a font is 2048 and
`ySuperScriptXSize` is set to 205, then the horizontal size for a
simulated superscript character would be 1/10th the size of the normal
character.
"""

TT_OS2_y_superscript_y_size = """
Maps to the emHeight of the font being used for a subscript. If a font
has two recommended sizes for subscripts, e.g., numerics and other,
the numeric sizes should be stressed. The vertical font size specifies
a font designer's recommended vertical font size for superscript
characters associated with this font. If a font does not include all
of the required superscript characters for an application, and the
application can substitute characters by scaling the character of a
font or by substituting characters from another font, this parameter
specifies the recommended EmHeight for those superscript characters.
For example, if the em square for a font is 2048 and `ySuperScriptYSize`
is set to 205, then the vertical size for a simulated superscript
character would be 1/10th the size of the normal character.
"""

TT_OS2_y_superscript_x_offset = """
Specifies a font designer's recommended horizontal offset for the
superscript characters associated with this font.  It is from the
character origin to the superscript character's origin. If a font does
not include all of the required superscript characters for an
application, this parameter specifies the recommended horizontal
position from the escapement point of the character before the first
superscript character. For upright characters, this value is usually
zero; however, if the characters of a font have an incline (italic
characters) the reference point for superscript characters is usually
adjusted to compensate for the angle of incline.
"""

TT_OS2_y_superscript_y_offset = """
Specifies a font designer's recommended vertical offset for
superscript characeters.  It is from the character baseline to the
superscript character's baseline associated with this font. Values for
this parameter are expressed as a positive offset above the character
baseline. If a font does not include all of the required superscript
characters for an application, this parameter specifies the
recommended vertical distance above the character baseline for those
superscript characters.
"""

TT_OS2_y_strikeout_size = """
The size of the strikeout line.  This field should normally be the
width of the em-dash for the current font. If the size is one, the
strikeout line will be the line represented by the strikeout position
field. If the value is two, the strikeout line will be the line
represented by the strikeout position and the line immediately above
the strikeout position.
"""

TT_OS2_y_strikeout_position = """
The width of the strikeout line.  Positive values represent distances
above the baseline, while negative values represent distances below
the baseline. A value of zero falls directly on the baseline, while a
value of one falls one pixel above the baseline. The value of
strikeout position should not interfere with the recognition of
standard characters, and therefore should not line up with crossbars
in the font.
"""

TT_OS2_family_class = """
Classifies a font design as to its appearance.  It does not identify
the specific font family, typeface variation, designer, supplier,
size, or metric table differences.  This is the high byte of the
`sFamilyClass` field.

|freetypy| The use of this is limited, so the values are not provided
as enumerations.  See `the TrueType specification
<https://developer.apple.com/fonts/TTRefMan/RM06/Chap6OS2.html>`_ for
more information.
"""

TT_OS2_family_subclass = """
Classifies a font design as to its appearance.  It does not identify
the specific font family, typeface variation, designer, supplier,
size, or metric table differences.  This is the low byte of the
`sFamilyClass` field.

|freetypy| The use of this is limited, so the values are not provided
as enumerations.  See `the TrueType specification
<https://developer.apple.com/fonts/TTRefMan/RM06/Chap6OS2.html>`_ for
more information.
"""

TT_OS2_panose = """
The PANOSE classification number.

|freetypy| The use of this is limited, so the values are not provided
as enumerations.  See `the TrueType specification
<https://developer.apple.com/fonts/TTRefMan/RM06/Chap6OS2.html>`_ for
more information.  A more Pythonic interface may be provided in the
future if needed.

It is a 10-byte string where each byte is as follows:

- 0: Family type
- 1: Serif style
- 2: Weight
- 3: Proportion
- 4: Contrast
- 5: Stroke Variation
- 6: Arm Style
- 7: Letterform
- 8: Midline
- 9: x height
"""

TT_OS2_vend_id = """
Indentifies the font vendor.

It is not the royalty owner of the original artwork but the company
responsible for the marketing and distribution of the typeface that is
being classified. It is reasonable to assume that there will be 6
vendors of ITC Zapf Dingbats for use on desktop platforms in the near
future (if not already). It is also likely that the vendors will have
other inherent benefits in their fonts (more kern pairs, unregularized
data, hand hinted, etc.). This identifier will allow for the correct
vendors type to be used over another, possibly inferior, font
file. These id's are assigned by Microsoft.
"""

TT_OS2_selection = """
A `TT_FS_SELECTION` bitflag.
"""

TT_FS_SELECTION = """
Bitflag concerning the nature of the font patterns.

- `ITALIC`

- `UNDERSCORE`

- `NEGATIVE`

- `OUTLINED`

- `STRIKEOUT`

- `BOLD`
"""

TT_OS2_first_char_index = """
The minimum Unicode index in this font.
"""

TT_OS2_last_char_index = """
The maximum Unicode index in this font.
"""

TT_OS2_typo_ascender = """
TODO
"""

TT_OS2_typo_descender = """
TODO
"""

TT_OS2_typo_line_gap = """
TODO
"""

TT_OS2_win_ascent = """
TODO
"""

TT_OS2_win_descent = """
TODO
"""

TT_OS2_x_height = """
TODO
"""

TT_OS2_cap_height = """
TODO
"""

TT_OS2_default_char = """
TODO
"""

TT_OS2_break_char = """
TODO
"""

TT_OS2_max_context = """
TODO
"""
