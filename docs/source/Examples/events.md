# Events

A Toast Notification ends up with an event among `Activated`, `Dissmissed` and `Failed`.

By default, `Notifier` handles `Activated` by printing the argument of the Action(button) and the inputs of Inputs, handes `Dissmissed` by printing the reason of `Dissmissed`, handles `Failed` by raising error_code.

```python
from winsdk_toast import Notifier, Toast


# Step1. Create Notifier with applicationId
notifier = Notifier('程序名 applicationId')

# Step2. Create Toast which contains the message to be shown
toast = Toast()
toast.add_text('第一行 1st line', hint_align='center', hint_style='caption')
toast.add_input(type_='text', id_='input_name')
toast.add_action('关闭 Close')
toast.set_audio(silent='true')  # Mute

# Step3. Show the Toast
notifier.show(toast)
```

If click the `X` at the top-right, `Dissmissed` event happens and prints

```
Dismissed reason: UserCanceled
```

If wait till it disappears, `Dissmissed` event happens and prints

```
Dismissed reason: TimeOut
```

If click the `关闭 Close` button, `Activated` event happens and prints

```
Activated with
	argument: dismiss
	inputs: {'input_name': ''}
```

If type `test input` in the input box and click on `关闭 Close` button, `Activated` event happens and prints

```
Activated with
	argument: dismiss
	inputs: {'input_name': 'test input'}
```

I haven't figured out how the `activationType` and `arguments` of `action` work, so just leave them to dismiss the Toast Notification.

## Custom `handle`

Just define the functions that handle the `EventArgsActivated`, `EventArgsDismissed`, `EventArgsFailed` respectively, and pass them to `notifier.show`.

```python
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
```