# -*- coding: utf-8 -*-
"""
Handle or create XmlDocument toast.

@Author: modabao
@Time: 2022/5/1 11:09
"""

from winsdk.windows.data.xml.dom import XmlDocument
from winsdk.windows.ui.notifications import ToastNotification


def set_attributes(element, attributes: dict):
    for name, value in attributes.items():
        if value is None:
            continue
        element.set_attribute(name, value)


class Toast(object):
    def __init__(self, xml=None):
        self.xml_document = XmlDocument()
        if xml is not None:
            self.xml_document.load_xml(xml)
        self.input_ids = []

    def suit_up(self):
        """Suit up to face notifier

        Returns:
            toast_notification
        """
        return ToastNotification(self.xml_document)

    def set_toast(
            self, launch=None, duration=None, displayTimeStamp=None, scenario=None, useButtonStyle=None,
            activationType='background'
    ):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-toast
        Args:
            launch: <str>
            duration: 'long' | 'short'
            displayTimeStamp: <str>
            scenario: 'default' | 'reminder' | 'alarm' | 'incomingCall' | 'urgent'
            useButtonStyle: 'false' | 'true'
            activationType: 'background' | 'protocol'

        Returns:
            element_toast
        """
        xml_document = self.xml_document
        element_toast = xml_document.create_element('toast')
        xml_document.append_child(element_toast)
        attributes = {
            'launch': launch,
            'duration': duration,
            'displayTimeStamp': displayTimeStamp,
            'scenario': scenario,
            'useButtonStyle': useButtonStyle,
            'activationType': activationType
        }
        set_attributes(element_toast, attributes)
        return element_toast

    def set_visual(self, version=None, lang=None, baseUri=None, branding=None, addImageQuery=None):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-visual
        Args:
            version: '1'
            lang: <str>
            baseUri: 'ms-appx:///'
            branding: Not used. 'none' | 'logo' | 'name'
            addImageQuery: 'false' | 'true'

        Returns:
            None
        """
        xml_document = self.xml_document
        element_toast = xml_document.select_single_node('/toast') or self.set_toast()
        element_visual = xml_document.create_element('visual')
        element_toast.append_child(element_visual)
        attributes = {
            'version': version,
            'lang': lang,
            'baseUri': baseUri,
            'branding': branding,
            'addImageQuery': addImageQuery
        }
        set_attributes(element_visual, attributes)
        return element_visual

    def set_binding(
            self, template='ToastGeneric', fallback=None, lang=None, addImageQuery=None, baseUri=None, branding=None
    ):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-binding
        Args:
            template: 'ToastGeneric'
            fallback:
            lang: <str>
            addImageQuery: 'false' | 'true'
            baseUri: <str> 'ms-appx:///'
            branding: Not used. 'none' | 'logo' | 'name'

        Returns:
            element_binding
        """
        xml_document = self.xml_document
        element_visual = xml_document.select_single_node('//visual') or self.set_visual()
        element_binding = xml_document.create_element('binding')
        element_visual.append_child(element_binding)
        attributes = {
            'template': template,
            'fallback': fallback,
            'lang': lang,
            'addImageQuery': addImageQuery,
            'baseUri': baseUri,
            'branding': branding
        }
        set_attributes(element_binding, attributes)
        return element_binding

    def add_text(
            self, text, id_=None, lang=None, placement=None, hint_maxLines=None, hint_style=None, hint_align=None,
            hint_wrap=None, element_parent=None
    ):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-text
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-tiles-schema
        Args:
            text: <str>
            id_: <str>
            lang: <str>
            placement: 'attribution' ...
            hint_maxLines: '1'-'4'
            hint_style: 'base' | 'captionSubtle' ...
            hint_align: 'left' | 'center' | 'right'
            hint_wrap: 'false' | 'true'
            element_parent:

        Returns:
            element_text
        """
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//binding') or self.set_binding()
        element_text = xml_document.create_element('text')
        element_parent.append_child(element_text)
        element_text.inner_text = text
        attributes = {
            'id': id_,
            'lang': lang,
            'placement': placement,
            'hint-maxLines': hint_maxLines,
            'hint-style': hint_style,
            'hint-align': hint_align,
            'hint-wrap': hint_wrap
        }
        set_attributes(element_text, attributes)
        return element_text

    def add_image(
            self, src, id_=None, alt=None, addImageQuery=None, placement=None, hint_crop=None, element_parent=None
    ):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-image
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        Args:
            src: (<3MB)
            id_: <str>
            alt: <str>
            addImageQuery: 'false' | 'true'
            placement: 'appLogoOverride' | 'hero'
            hint_crop: 'circle' | ''
            element_parent:

        Returns:
            None
        """
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//binding') or self.set_binding()
        element_image = xml_document.create_element('image')
        element_parent.append_child(element_image)
        attributes = {
            'src': src,
            'id': id_,
            'alt': alt,
            'addImageQuery': addImageQuery,
            'placement': placement,
            'hint-crop': hint_crop
        }
        set_attributes(element_image, attributes)
        return element_image

    def add_progress(self, title=None, status='Progress', value='0.5', valueStringOverride=None, element_parent=None):
        """
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/toast-progress-bar
        Args:
            title:
            status:
            value: '0.0' - '1.0'
            valueStringOverride:
            element_parent:

        Returns:

        """
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//binding') or self.set_binding()
        element_progress = xml_document.create_element('progress')
        element_parent.append_child(element_progress)
        attributes = {
            'title': title,
            'status': status,
            'value': value,
            'valueStringOverride': valueStringOverride
        }
        set_attributes(element_parent, attributes)
        return element_progress

    def add_group(self):
        """
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        Returns:
            element_group
        """
        xml_document = self.xml_document
        element_binding = xml_document.select_single_node('//binding') or self.set_binding()
        element_group = xml_document.create_element('group')
        element_binding.append_child(element_group)
        return element_group

    def add_subgroup(self, element_parent=None):
        """
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        Returns:
            element_group
        """
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//group') or self.add_group()
        element_subgroup = xml_document.create_element('subgroup')
        element_parent.append_child(element_subgroup)
        return element_subgroup

    def set_actions(self):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-actions
        Returns:
            None
        """
        xml_document = self.xml_document
        element_toast = xml_document.select_single_node('/toast') or self.set_toast()
        element_actions = xml_document.create_element('actions')
        element_toast.append_child(element_actions)
        return element_actions

    def add_action(
            self, content, arguments='dismiss', activationType='system', placement=None, imageUri=None,
            hint_inputId=None, hint_buttonStyle=None, hint_toolTip=None
    ):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-action
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        type?
        Args:
            content: <str>
            arguments: ('dismiss' | 'snooze') for activationType='system'
            activationType: 'system' | 'foreground' | 'background' | 'protocol'
            placement: 'contextMenu' | ''
            imageUri:
            hint_inputId:
            hint_buttonStyle: 'success' | 'citical'
            hint_toolTip:

        Returns:

        """
        xml_document = self.xml_document
        element_actions = xml_document.select_single_node('//actions') or self.set_actions()
        element_action = xml_document.create_element('action')
        element_actions.append_child(element_action)
        attributes = {
            'content': content,
            'arguments': arguments,
            'activationType': activationType,
            'placement': placement,
            'imageUri': imageUri,
            'hint-inputId': hint_inputId,
            'hint-buttonStyle': hint_buttonStyle,
            'hint-toolTip': hint_toolTip
        }
        set_attributes(element_action, attributes)
        return element_action

    def add_input(self, type_, id_=None, placeHolderContent=None, element_parent=None):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-input
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        Args:
            id_:
            type_: 'text' | 'selection'
            placeHolderContent:

        Returns:

        """
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//actions') or self.set_actions()
        element_input = xml_document.create_element('input')
        element_parent.append_child(element_input)
        attributes = {
            'type': type_,
            'id': id_,
            'placeHolderContent': placeHolderContent
        }
        set_attributes(element_input, attributes)
        self.input_ids.append(id_)
        return element_input

    def add_selection(self, id_=None, content=None, element_parent=None):
        """
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts
        Args:
            id_:
            content:
            element_parent:

        Returns:
            element_selection
        """
        pass
        xml_document = self.xml_document
        element_parent = element_parent or xml_document.select_single_node('//input') or self.add_input()
        element_selection = xml_document.create_element('selection')
        element_parent.append_child(element_selection)
        attributes = {
            'id': id_,
            'content': content
        }
        set_attributes(element_selection, attributes)
        return element_selection

    def set_audio(self, src=None, loop='false', silent='false'):
        """
        https://docs.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-audio
        https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/custom-audio-on-toasts
        Args:
            src:
            loop:
            silent:

        Returns:

        """
        xml_document = self.xml_document
        element_toast = xml_document.select_single_node('/toast') or self.set_toast()
        element_audio = xml_document.create_element('audio')
        element_toast.append_child(element_audio)
        attributes = {
            'src': src,
            'loop': loop,
            'silent': silent
        }
        set_attributes(element_audio, attributes)
        return element_audio
