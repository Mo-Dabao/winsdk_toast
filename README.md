# winsdk_toast

[![Documentation Status](https://readthedocs.org/projects/winsdk-toast/badge/?version=latest)](https://winsdk-toast.readthedocs.io/en/latest/?badge=latest)

A simple package for displaying Windows Toast Notification based on [winsdk].

Sometimes, after starting my data processing python script, I may surf the Internet.
It chokes my happiness that to frequently check whether the script stops,
or suddenly realize the script has stopped for a long while.

It'll be reassuring that the script can stop with a friendly gesture.

## Features

winsdk_toast can pop up Windows Toast Notifications that contain

- [x] Text
- [x] Image
- [x] Input
  - [x] Text
  - [x] Selection
- [x] Audio
  - [x] Buit-in
  - [ ] Custom
- [x] Progress
  - [x] Still
  - [ ] Live
- [x] Group
- [x] Event

## Minimal Example

```python
from winsdk_toast import Notifier, Toast


notifier = Notifier('程序名 applicationId')
toast = Toast()
toast.add_text('第一行 1st line')
notifier.show(toast)
```

![minimal_example.gif](docs/source/Examples/pics/minimal.gif)

[More examples and documents](https://winsdk-toast.readthedocs.io/en/latest/?badge=latest) are on the way.


[winsdk]: https://pypi.org/project/winsdk
