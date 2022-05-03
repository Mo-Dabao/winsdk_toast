# -*- coding: utf-8 -*-
"""
minimal example

@Author: modabao
@Time: 2022/5/3 10:33
"""

from winsdk_toast import Notifier, Toast


notifier = Notifier('程序名 applicationId')

# %% minimal example
toast = Toast()
toast.add_text('第一行 1st line')
notifier.show(toast)

# %% which is equivalent to
xml = """
<toast activationType="background">
    <visual>
        <binding template="ToastGeneric">
            <text>第一行 1st line</text>
        </binding>
    </visual>
</toast>
"""
toast = Toast(xml)
notifier.show(toast)
