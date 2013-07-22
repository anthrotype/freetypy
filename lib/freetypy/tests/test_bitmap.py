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

import freetypy as ft
from .util import *


A = [
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x71,0xff,0xff,0xff,0xff,0xff,0x78,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xd2,0xff,0xff,0xff,0xff,0xff,0xd9,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x35,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x3b,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x97,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x9d,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0xef,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xf3,0x0b,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5a,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xbc,0xff,0xff,0xff,0xff,0xfc,0xff,0xff,0xff,0xff,0xc1,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1f,0xfe,0xff,0xff,0xff,0xff,0x77,0xff,0xff,0xff,0xff,0xfe,0x23,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7f,0xff,0xff,0xff,0xff,0xdc,0x01,0xd6,0xff,0xff,0xff,0xff,0x85,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0xdf,0xff,0xff,0xff,0xff,0x7b,0x00,0x75,0xff,0xff,0xff,0xff,0xe3,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x43,0xff,0xff,0xff,0xff,0xfd,0x1c,0x00,0x17,0xfb,0xff,0xff,0xff,0xff,0x48,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xa5,0xff,0xff,0xff,0xff,0xb8,0x00,0x00,0x00,0xb2,0xff,0xff,0xff,0xff,0xa9,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0f,0xf6,0xff,0xff,0xff,0xff,0x56,0x00,0x00,0x00,0x50,0xff,0xff,0xff,0xff,0xf8,0x12,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x68,0xff,0xff,0xff,0xff,0xed,0x07,0x00,0x00,0x00,0x05,0xe9,0xff,0xff,0xff,0xff,0x6c,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xca,0xff,0xff,0xff,0xff,0x92,0x00,0x00,0x00,0x00,0x00,0x8d,0xff,0xff,0xff,0xff,0xce,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x2b,0xff,0xff,0xff,0xff,0xff,0x31,0x00,0x00,0x00,0x00,0x00,0x2c,0xff,0xff,0xff,0xff,0xff,0x2f,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x8e,0xff,0xff,0xff,0xff,0xcf,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xca,0xff,0xff,0xff,0xff,0x91,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x05,0xea,0xff,0xff,0xff,0xff,0x6d,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x69,0xff,0xff,0xff,0xff,0xec,0x06,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0x51,0xff,0xff,0xff,0xff,0xf8,0x12,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x10,0xf7,0xff,0xff,0xff,0xff,0x54,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x00,0xb3,0xff,0xff,0xff,0xff,0xaa,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xa6,0xff,0xff,0xff,0xff,0xb6,0x00,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x18,0xfb,0xff,0xff,0xff,0xff,0x48,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x44,0xff,0xff,0xff,0xff,0xfc,0x1a,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0x77,0xff,0xff,0xff,0xff,0xe3,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x02,0xe1,0xff,0xff,0xff,0xff,0x79,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x00,0xd7,0xff,0xff,0xff,0xff,0x84,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x81,0xff,0xff,0xff,0xff,0xd9,0x00,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x3a,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x3c,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x00,0x9c,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x9d,0x00,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x0b,0xf2,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xf3,0x0b,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0x5f,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x61,0x00,0x00,0x00,  ],
  [0x00,0x00,0x00,0xc1,0xff,0xff,0xff,0xff,0x9b,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x97,0xff,0xff,0xff,0xff,0xc2,0x00,0x00,0x00,  ],
  [0x00,0x00,0x23,0xfe,0xff,0xff,0xff,0xff,0x39,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x36,0xff,0xff,0xff,0xff,0xff,0x24,0x00,0x00,  ],
  [0x00,0x00,0x85,0xff,0xff,0xff,0xff,0xd6,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xd4,0xff,0xff,0xff,0xff,0x85,0x00,0x00,  ],
  [0x00,0x02,0xe3,0xff,0xff,0xff,0xff,0x75,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x72,0xff,0xff,0xff,0xff,0xe3,0x02,0x00,  ],
  [0x00,0x48,0xff,0xff,0xff,0xff,0xfb,0x17,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x15,0xfa,0xff,0xff,0xff,0xff,0x48,0x00,  ],
  [0x00,0xaa,0xff,0xff,0xff,0xff,0xb2,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xaf,0xff,0xff,0xff,0xff,0xaa,0x00,  ],
  [0x12,0xf8,0xff,0xff,0xff,0xff,0x50,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x4d,0xff,0xff,0xff,0xff,0xf8,0x12,  ],
  [0x6e,0xff,0xff,0xff,0xff,0xe9,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x04,0xe7,0xff,0xff,0xff,0xff,0x6d,  ],
  [0xcf,0xff,0xff,0xff,0xff,0x8c,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x89,0xff,0xff,0xff,0xff,0xcf,  ],
]


def test_bitmap():
    face = ft.Face(vera_path())
    face.set_charmap(0)
    face.set_char_size(12, 12, 300, 300)
    glyph = face.load_char(65, ft.LOAD.RENDER)

    x = glyph.bitmap.to_list()
    assert x == A

    glyph = face.load_char(65, ft.LOAD.RENDER|ft.LOAD.TARGET_LCD)

    x = glyph.bitmap.to_list()
    assert len(x[0][0]) == 3



def test_instantiate_Bitmap():
    try:
        x = ft.Bitmap()
    except RuntimeError:
        pass
    else:
        assert False, "Shouldn't be able to directly instantiate a Bitmap"