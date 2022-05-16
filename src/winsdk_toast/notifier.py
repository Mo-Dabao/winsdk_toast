# -*- coding: utf-8 -*-
"""

@Author: modabao
@Time: 2022/5/1 11:52
"""

import asyncio

from winsdk.windows.ui.notifications import ToastNotificationManager

from winsdk_toast.toast import Toast
from winsdk_toast.event import (
    EventArgsActivated, EventArgsDismissed, EventArgsFailed,
    handle_activated, handle_dismissed, handle_failed
)


async def show(
        toast_notifier, toast: Toast,
        handle_activated=handle_activated, handle_dismissed=handle_dismissed, handle_failed=handle_failed
):
    toast_notification = toast.suit_up()
    event_loop = asyncio.get_running_loop()
    aws = []
    tokens = {}

    future_activated = event_loop.create_future()
    token_activated = toast_notification.add_activated(
        lambda sender, event_args: event_loop.call_soon_threadsafe(
            future_activated.set_result, handle_activated(EventArgsActivated(sender, event_args, toast.input_ids))
        )
    )
    aws.append(future_activated)
    tokens['activated'] = token_activated

    future_dismissed = event_loop.create_future()
    token_dismissed = toast_notification.add_dismissed(
        lambda sender, event_args: event_loop.call_soon_threadsafe(
            future_dismissed.set_result, handle_dismissed(EventArgsDismissed(sender, event_args)))
    )
    aws.append(future_dismissed)
    tokens['dismissed'] = token_dismissed

    future_failed = event_loop.create_future()
    token_failed = toast_notification.add_failed(
        lambda sender, event_args: event_loop.call_soon_threadsafe(
            future_failed.set_result, handle_failed(EventArgsFailed(sender, event_args)))
    )
    aws.append(future_failed)
    tokens['failed'] = token_failed

    toast_notifier.show(toast_notification)
    try:
        [done], pending = await asyncio.wait(aws, return_when=asyncio.FIRST_COMPLETED)
        for p in pending:
            p.cancel()
    finally:
        if (token_activated := tokens['activated']) is not None:
            toast_notification.remove_activated(token_activated)
        if (token_dismissed := tokens['dismissed']) is not None:
            toast_notification.remove_dismissed(token_dismissed)
        if (token_failed := tokens['failed']) is not None:
            toast_notification.remove_failed(token_failed)


class Notifier(object):
    def __init__(self, applicationId):
        """
        https://docs.microsoft.com/en-us/uwp/api/windows.ui.notifications.toastnotificationmanager.createtoastnotifier
        Args:
            applicationId:
        """
        self.toast_notifier = ToastNotificationManager.create_toast_notifier(applicationId)

    def show(self, toast: Toast,
             handle_activated=handle_activated, handle_dismissed=handle_dismissed, handle_failed=handle_failed):
        asyncio.run(show(self.toast_notifier, toast, handle_activated, handle_dismissed, handle_failed))

