# -*- coding: utf-8 -*-
"""
simple example

@Author: modabao
@Time: 2022/5/3 10:33
"""

from os.path import abspath

from winsdk_toast import Notifier, Toast

path_pic = abspath('./resource/python.ico')

notifier = Notifier('程序名 applicationId')

# %% simple example
toast = Toast()
toast.add_text('第一行 1st line', hint_align='center', hint_style='caption')
toast.add_text('第二行 2nd line')
toast.add_text('第三行 3rd line', placement='attribution')
toast.add_image(path_pic, placement='appLogoOverride')
toast.add_action('关闭 Close')
toast.set_audio(silent='true')
notifier.show(toast)

# %% which is equivalent to
xml = f"""
<toast activationType="background">
    <visual>
        <binding template="ToastGeneric">
            <text hint-style="caption" hint-align="center">第一行 1st line</text>
            <text>第二行 2nd line</text>
            <text placement="attribution">第三行 3rd line</text>
            <image src="{path_pic}" placement="appLogoOverride" />
        </binding>
    </visual>
    <actions>
        <action content="关闭 Close" arguments="dismiss" activationType="system" />
    </actions><audio loop="false" silent="true" />
</toast>
"""
toast = Toast(xml)
notifier.show(toast)
