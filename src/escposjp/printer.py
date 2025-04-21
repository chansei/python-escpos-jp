from escpos.printer import Network, Usb, Serial, Dummy, File
from escpos.exceptions import CharCodeError, TextError
import inspect
import sys

CHARCODE_JIS = '\x1b\x74\x01'


def charcode(self, code):
    """ Set Character Code Table """
    if code.upper() == "JIS":
        self._raw(CHARCODE_JIS)
    else:
        raise CharCodeError()


def text(self, txt):
    """ Print alpha-numeric text """
    if txt:
        self._raw(txt)
    else:
        raise TextError()


def jpInit(self):
    self.charcode("JIS")
    self._raw(b'\x1c\x43\x01')


def jpText(self, txt, dw=False, dh=False):
    self._raw(b'\x1c\x26')    # Kanji mode ON
    n = 0x00
    if (dw):
        n += 0x04
    if (dh):
        n += 0x08
    if (n != 0x00):
        # Char size ON
        self._raw(b'\x1c\x21' + n.to_bytes(1, byteorder='big'))
    self._raw(txt.encode('shift-jis', 'ignore'))
    if (n != 0x00):
        self._raw(b'\x1c\x21\x00')  # Char size OFF
    self._raw(b'\x1c\x2e')    # Kanji mode OFF


def addfunc(_class, func):
    setattr(_class, func.__name__, func)


for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    addfunc(obj, charcode)
    addfunc(obj, text)
    addfunc(obj, jpInit)
    addfunc(obj, jpText)
