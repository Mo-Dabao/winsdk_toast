# -*- coding: utf-8 -*-
"""

@Author: modabao
@Time: 2022/5/1 11:52
"""

from winsdk.windows.ui.notifications import ToastNotificationManager

from winsdk_toast.toast import Toast


class Notifier(object):
    def __init__(self, applicationId):
        """
        https://docs.microsoft.com/en-us/uwp/api/windows.ui.notifications.toastnotificationmanager.createtoastnotifier
        Args:
            applicationId:
        """
        self.toast_notifier = ToastNotificationManager.create_toast_notifier(applicationId)

    def show(self, toast: Toast):
        self.toast_notifier.show(toast.suit_up())
