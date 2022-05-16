# -*- coding: utf-8 -*-
"""

@Author: modabao
@Time: 2022/5/8 14:57
"""

from winsdk.windows.foundation import IPropertyValue
from winsdk.windows.ui.notifications import ToastActivatedEventArgs, ToastDismissedEventArgs, ToastFailedEventArgs


class EventArgsActivated(object):
    """
    https://docs.microsoft.com/en-us/uwp/api/windows.ui.notifications.toastactivatedeventargs?view=winrt-22000
    """
    def __init__(self, sender, event_args, input_ids):
        self.sender = sender
        event_args = ToastActivatedEventArgs._from(event_args)
        self.argument = event_args.arguments
        self.inputs = {
            input_id: IPropertyValue._from(event_args.user_input.lookup(input_id)).get_string()
            for input_id in input_ids
        }


class EventArgsDismissed(object):
    """
    https://docs.microsoft.com/en-us/uwp/api/windows.ui.notifications.toastdismissedeventargs?view=winrt-22000
    """
    def __init__(self, sender, event_args):
        self.sender = sender
        event_args = ToastDismissedEventArgs._from(event_args)
        self.reason = ['UserCanceled', 'ApplicationHidden', 'TimeOut'][event_args.reason]


class EventArgsFailed(object):
    """
    https://docs.microsoft.com/en-us/uwp/api/windows.ui.notifications.toastdismissedeventargs?view=winrt-22000
    """
    def __init__(self, sender, event_args):
        self.sender = sender
        event_args = ToastFailedEventArgs._from(event_args)
        self.error_code = event_args.error_code


def handle_activated(event_args_activated: EventArgsActivated):
    print(f'Activated with')
    print(f'\targument: {event_args_activated.argument}')
    print(f'\tinputs: {event_args_activated.inputs}')


def handle_dismissed(event_args_dismissed: EventArgsDismissed):
    print(f'Dismissed reason: {event_args_dismissed.reason}')


def handle_failed(event_args_failed: EventArgsFailed):
    raise RuntimeError(event_args_failed.error_code)
