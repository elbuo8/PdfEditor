## PdfEditor for Python ##

This is a minimalistic module for editing previously created PDFs.

### Example

```python
from PdfEditor import PdfEditor

editor = PdfEditor('test.pdf', 'letter')
editor.drawString(3, 3, 'HELLO!')
editor.save('test-gen.pdf')
```

### License

MIT

### Enjoy

Feel free to submit pull requests. More methods and features will be added.
