# -*- coding: utf-8 -*-
"""
simple example

@Author: modabao
@Time: 2022/5/3 10:33
"""

from winsdk_toast import Notifier, Toast
from winsdk_toast.event import EventArgsActivated, EventArgsDismissed, EventArgsFailed


def handle_activated(event_args_activated: EventArgsActivated):
    print('activated')
    print('inputs:', event_args_activated.inputs)
    print('argument:', event_args_activated.argument)


def handle_dismissed(event_args_dismissed: EventArgsDismissed):
    print('dismissed')
    print('reason:', event_args_dismissed.reason)


def handle_failed(event_args_failed: EventArgsFailed):
    print('failed')
    print('error_code:', event_args_failed.error_code)


# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
toast = Toast()
toast.add_text('第一行 1st line', hint_align='center', hint_style='caption')
toast.add_input(type_='text', id_='input_name')
toast.add_action('关闭 Close')
toast.set_audio(silent='true')  # Mute

# Step3. Show the Toast
notifier.show(
    toast, handle_activated=handle_activated, handle_dismissed=handle_dismissed, handle_failed=handle_failed
)
