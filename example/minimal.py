# -*- coding: utf-8 -*-
"""
minimal example

@Author: modabao
@Time: 2022/5/3 10:33
"""

from winsdk_toast import Notifier, Toast


# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
toast = Toast()
toast.add_text('第一行 1st line')

# Step3. Show the Toast
notifier.show(toast)

# %% which is equivalent to
# xml = """
# <toast activationType="background">
#     <visual>
#         <binding template="ToastGeneric">
#             <text>第一行 1st line</text>
#         </binding>
#     </visual>
# </toast>
# """
# toast = Toast(xml)
# notifier.show(toast)
