# Minimal

```python
from winsdk_toast import Notifier, Toast


# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
toast = Toast()
toast.add_text('第一行 1st line')

# Step3. Show the Toast
notifier.show(toast)
```

![minimal.gif](pics/minimal.gif)

Which can also be achieved by

```python
from winsdk_toast import Notifier, Toast


# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
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

# Step3. Show the Toast
notifier.show(toast)
```
