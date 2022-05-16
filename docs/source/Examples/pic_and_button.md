# pic and button

```python
from os.path import abspath

from winsdk_toast import Notifier, Toast


# absolute path of the picture to be shown
path_pic = abspath('./resource/python.ico')

# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
toast = Toast()
toast.add_text('第一行 1st line', hint_align='center', hint_style='caption')
toast.add_text('第二行 2nd line')
toast.add_text('第三行 3rd line', placement='attribution')
toast.add_image(path_pic, placement='appLogoOverride')
toast.add_action('关闭 Close')
toast.set_audio(silent='true')  # Mute

# Step3. Show the Toast
notifier.show(toast)
```

![simple.gif](pics/simple.gif)

Which can also be achieved by

```python
from os.path import abspath

from winsdk_toast import Notifier, Toast


# absolute path of the picture to be shown
path_pic = abspath('./resource/python.ico')

# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
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

# Step3. Show the Toast
notifier.show(toast)
```


