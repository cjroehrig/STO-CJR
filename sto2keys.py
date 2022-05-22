#!/usr/bin/python
"""sto2keys:  convert any STO binding hex keycodes to human-readable keys
"""

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser Public License for more details.
#
#   You should have received a copy of the GNU Lesser Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   Copyright (c) 2022 Chris Roehrig <chris@crispart.com>
#

#==============================================================================
# Imports and definitions
import sys
import argparse

def printf(fmt, *args):
    print(fmt % args, end='')

#==============================================================================
# KEYTABLE

# To deduce:  bind a key:   /bind SysRq "team SysRq", log out, log in and
#  bind_save_file CJR/ff.txt

KeyTable = [None] * 256

# ROW 2
KeyTable[    0x0    ] =   None
KeyTable[    0x1    ] =  'Esc'
KeyTable[    0x2    ] =  '1'
KeyTable[    0x3    ] =  '2'
KeyTable[    0x4    ] =  '3'
KeyTable[    0x5    ] =  '4'
KeyTable[    0x6    ] =  '5'
KeyTable[    0x7    ] =  '6'
KeyTable[    0x8    ] =  '7'
KeyTable[    0x9    ] =  '8'
KeyTable[    0xa    ] =  '9'
KeyTable[    0xb    ] =  '0'
KeyTable[    0xc    ] =  '-'
KeyTable[    0xd    ] =  '='
KeyTable[    0xe    ] =  'Backspace'

# ROW 3
KeyTable[    0xf    ] = 'Tab'
KeyTable[    0x10   ] = 'Q'
KeyTable[    0x11   ] = 'W'
KeyTable[    0x12   ] = 'E'
KeyTable[    0x13   ] = 'R'
KeyTable[    0x14   ] = 'T'
KeyTable[    0x15   ] = 'Y'
KeyTable[    0x16   ] = 'U'
KeyTable[    0x17   ] = 'I'
KeyTable[    0x18   ] = 'O'
KeyTable[    0x19   ] = 'P'
KeyTable[    0x1a   ] = '['
KeyTable[    0x1b   ] = ']'
KeyTable[    0x1c   ] = 'Enter'

# ROW 4
KeyTable[    0x1d   ] = 'LCtrl'
KeyTable[    0x1e   ] = 'A'
KeyTable[    0x1f   ] = 'S'
KeyTable[    0x20   ] = 'D'
KeyTable[    0x21   ] = 'F'
KeyTable[    0x22   ] = 'G'
KeyTable[    0x23   ] = 'H'
KeyTable[    0x24   ] = 'J'
KeyTable[    0x25   ] = 'K'
KeyTable[    0x26   ] = 'L'
KeyTable[    0x27   ] = 'SemiColon'
KeyTable[    0x28   ] = '\''
KeyTable[    0x29   ] = '`'

# ROW 5
KeyTable[    0x2a   ] = 'LShift'
KeyTable[    0x2b   ] = '\\'
KeyTable[    0x2c   ] = 'Z'
KeyTable[    0x2d   ] = 'X'
KeyTable[    0x2e   ] = 'C'
KeyTable[    0x2f   ] = 'V'
KeyTable[    0x30   ] = 'B'
KeyTable[    0x31   ] = 'N'
KeyTable[    0x32   ] = 'M'
KeyTable[    0x33   ] = ','
KeyTable[    0x34   ] = '.'
KeyTable[    0x35   ] = '/'
KeyTable[    0x36   ] = 'RShift'

# Special Keys
KeyTable[    0x37   ] = 'Multiply'
KeyTable[    0x38   ] = 'LAlt'
KeyTable[    0x39   ] = 'Space'
KeyTable[    0x3a   ] = None
KeyTable[    0x3b   ] = 'F1'
KeyTable[    0x3c   ] = 'F2'
KeyTable[    0x3d   ] = 'F3'
KeyTable[    0x3e   ] = 'F4'
KeyTable[    0x3f   ] = 'F5'
KeyTable[    0x40   ] = 'F6'
KeyTable[    0x41   ] = 'F7'
KeyTable[    0x42   ] = 'F8'
KeyTable[    0x43   ] = 'F9'
KeyTable[    0x44   ] = 'F10'
KeyTable[    0x45   ] = 'Numlock'
KeyTable[    0x46   ] = 'Scroll'
KeyTable[    0x47   ] = 'numpad7'
KeyTable[    0x48   ] = 'numpad8'
KeyTable[    0x49   ] = 'numpad9'
KeyTable[    0x4a   ] = 'Subtract'
KeyTable[    0x4b   ] = 'numpad4'
KeyTable[    0x4c   ] = 'numpad5'
KeyTable[    0x4d   ] = 'numpad6'
KeyTable[    0x4e   ] = 'Add'
KeyTable[    0x4f   ] = 'numpad1'
KeyTable[    0x50   ] = 'numpad2'
KeyTable[    0x51   ] = 'numpad3'
KeyTable[    0x52   ] = 'numpad0'
KeyTable[    0x53   ] = 'Decimal'
KeyTable[    0x54   ] = None
KeyTable[    0x55   ] = None
KeyTable[    0x56   ] = None
KeyTable[    0x57   ] = 'F11'
KeyTable[    0x58   ] = 'F12'
KeyTable[    0x59   ] = None
KeyTable[    0x5a   ] = None
KeyTable[    0x5b   ] = None
KeyTable[    0x5c   ] = None
KeyTable[    0x5d   ] = None
KeyTable[    0x5e   ] = None
KeyTable[    0x5f   ] = None
KeyTable[    0x60   ] = None
KeyTable[    0x61   ] = None
KeyTable[    0x62   ] = None
KeyTable[    0x63   ] = None
KeyTable[    0x64   ] = 'F13'
KeyTable[    0x65   ] = 'F14'
KeyTable[    0x66   ] = 'F15'

KeyTable[    0x9c   ] = 'numpadEnter'
KeyTable[    0x9d   ] = 'RCtrl'
KeyTable[    0xb5   ] = 'Divide'
KeyTable[    0xb7   ] = 'SysRq'
KeyTable[    0xb8   ] = 'RAlt'

KeyTable[    0xc5   ] = 'Pause'
KeyTable[    0xc7   ] = 'Home'
KeyTable[    0xc8   ] = 'Up'
KeyTable[    0xc9   ] = 'PageUp'
KeyTable[    0xcb   ] = 'Left'
KeyTable[    0xcd   ] = 'Right'
KeyTable[    0xcf   ] = 'End'
KeyTable[    0xd0   ] = 'Down'
KeyTable[    0xd1   ] = 'PageDown'
KeyTable[    0xd2   ] = 'Insert'
KeyTable[    0xd3   ] = 'Delete'
KeyTable[    0xdb   ] = 'LWin'
KeyTable[    0xdc   ] = 'RWin'
KeyTable[    0xdd   ] = 'Apps'

# MOUSE
KeyTable[    0xee   ] = 'LButton'
KeyTable[    0xef   ] = 'MButton'
KeyTable[    0xf0   ] = 'RButton'
KeyTable[    0xf7   ] = 'MouseChord'
KeyTable[    0xf9   ] = 'MiddleClick'
KeyTable[    0xfe   ] = 'WheelPlus'
KeyTable[    0xff   ] = 'WheelMinus'



ModifierTable = [
        None,           # 0x0
        'Ctrl',         # 0x1
        'Shift',        # 0x2
        'Alt',          # 0x3
        None,           # 0x4
        None,           # 0x5
        None,           # 0x6
        None,           # 0x7
        None,           # 0x8
        None,           # 0x9
        None,           # 0xa
        None,           # 0xb
        None,           # 0xc
        None,           # 0xd
        None,           # 0xe
        None            # 0xf
]


#==============================================================================
def STOKeycode2Name(val):
    """Convert an STO hex key value to its string name"""
    str = None

    if val < len(KeyTable):
        str = KeyTable[val]

    elif val & 0x800:
        str = ModifierTable[val & 0xf]

    # No entry 
    if str == None:
        print( "WARNING: No KeyTable mapping found for 0x%x" % val,
                file=sys.stderr )
        str = "0x%x" % val

    return str

#==============================================================================
def dehex(line):
    binding, rest = line.split(None, 1)
    buttons = binding.split("+")
    newbinding = None
    for b in buttons:
        if b[:2] == '0x':
            val = int(b[2:], 16)
            b = STOKeycode2Name(val)
        if newbinding == None:
            newbinding = b
        else:
            newbinding = newbinding + '+' + b

    # Canonicalize case (for diffing)
    newbinding = newbinding[0].upper() + newbinding[1:].lower()

    line = newbinding + " " + rest
    return line


#==============================================================================
def main():
#    args = handle_args()

    with sys.stdin as f:
        while True:
            line = f.readline()     # NB: includes trailing newline
            if not line: break
            line = line.rstrip('\n')
            if line[0] == '#': continue
            line = dehex(line)
            print(line)




#==============================================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("caught interrupt")
