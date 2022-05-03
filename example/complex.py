# -*- coding: utf-8 -*-
"""
example for control freak

@Author: modabao
@Time: 2022/5/3 10:33
"""

from os.path import abspath

from winsdk_toast import Notifier, Toast

path_pic = abspath('./resource/python.ico')

notifier = Notifier('程序名 applicationId')


# %% example for control freak
toast = Toast()
element_toast = toast.set_toast(
    launch='blah', duration='long', displayTimeStamp='2022-04-01T12:00:00Z', scenario='default',
    useButtonStyle='false', activationType='background'
)
element_visual = toast.set_visual(
    version='1', lang='zh-CN', baseUri='ms-appx:///', branding='none', addImageQuery='false'
)
element_binding = toast.set_binding(
    template='ToastGeneric', fallback='2ndtemplate', lang='zh-CN', addImageQuery='false',
    baseUri='ms-appx:///', branding='none'
)
element_text = toast.add_text(
    text='第一行 1st line for control freak', id_='1', lang='zh-CN', placement=None,
    hint_maxLines='1', hint_style='title', hint_align='center', hint_wrap='false',
    element_parent=element_binding
)
element_group = toast.add_group()
element_subgroup_left = toast.add_subgroup(element_parent=element_group)
element_text = toast.add_text(
    text='第二行 2nd line for control freak', id_='2', lang='zh-CN', placement=None,
    hint_maxLines='1', hint_style='captionSubtle ', hint_align='left', hint_wrap='false',
    element_parent=element_subgroup_left
)
element_subgroup_right = toast.add_subgroup(element_parent=element_group)
element_text = toast.add_text(
    text='第三行 3rd line for control freak', id_='3', lang='zh-CN', placement='attribution',
    hint_maxLines='1', hint_style='captionSubtle', hint_align='left', hint_wrap='false',
    element_parent=element_subgroup_right
)
toast.add_image(
    path_pic, id_=None, alt='', addImageQuery='false',
    placement='appLogoOverride', hint_crop='circle'
)
toast.set_actions()
toast.add_action(
    '关闭 Close', arguments='dismiss', activationType='system', placement=None,
    imageUri=None, hint_inputId=None, hint_buttonStyle=None, hint_toolTip='tip close'
)
notifier.show(toast)

# %% which is equivalent to
xml = f"""
<toast launch="blah" duration="long" displayTimeStamp="2022-04-01T12:00:00Z" scenario="default" useButtonStyle="false" activationType="background">
    <visual version="1" lang="zh-CN" baseUri="ms-appx:///" branding="none" addImageQuery="false">
        <binding template="ToastGeneric" fallback="2ndtemplate" lang="zh-CN" addImageQuery="false" baseUri="ms-appx:///" branding="none">
            <text id="1" lang="zh-CN" hint-maxLines="1" hint-style="title" hint-align="center" hint-wrap="false">第一行 1st line for control freak</text>
            <group>
                <subgroup>
                    <text id="2" lang="zh-CN" hint-maxLines="1" hint-style="captionSubtle " hint-align="left" hint-wrap="false">第二行 2nd line for control freak</text>
                </subgroup>
                <subgroup>
                    <text id="3" lang="zh-CN" placement="attribution" hint-maxLines="1" hint-style="captionSubtle" hint-align="left" hint-wrap="false">第三行 3rd line for control freak</text>
                </subgroup>
            </group>
            <image src="{path_pic}" alt="" addImageQuery="false" placement="appLogoOverride" hint-crop="circle"/>
        </binding>
    </visual>
    <actions>
        <action content="关闭 Close" arguments="dismiss" activationType="system" hint-toolTip="tip close"/>
    </actions>
</toast>
"""
toast = Toast(xml)
notifier.show(toast)
