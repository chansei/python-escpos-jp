[python-escpos japenese wrapper](https://github.com/iakyi/python-escpos-jp)よりfork

# CHANGELOG

- Wrapper元の[python-escpos](https://github.com/python-escpos/python-escpos)現行バージョンで動作させるために関数を追加
- [python-escpos for japanese](https://github.com/lrks/python-escpos)に合わせて関数名を修正

# HOW TO USE

```python
from escposjp import Usb

p = Usb(0x04B8, 0x0202, 0, timeout=1000)
p.jpInit()
p.jpText("テスト印刷\n")
p.qr("https://example.com")
p.cut()
```

- USB接続のTM-T88Vで動作確認(Windows環境)
- fork元にて`Network`クラスでも動作確認済み
