from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.LockScreen
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILockApplicationHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('38ee31ad-d94f-4e7c-81-fa-4f-44-36-50-62-81')
    @winrt_commethod(6)
    def RequestUnlock(self) -> Void: ...
    @winrt_commethod(7)
    def add_Unlocking(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockApplicationHost, Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Unlocking(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ILockApplicationHostStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f48fab8e-23d7-4e63-96-a1-66-6f-f5-2d-3b-2c')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.LockScreen.LockApplicationHost: ...
class ILockScreenBadge(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e95105d9-2bff-4db0-9b-4f-38-24-77-8b-9c-9a')
    @winrt_commethod(6)
    def get_Logo(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(7)
    def get_Glyph(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def get_Number(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_AutomationName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def LaunchApp(self) -> Void: ...
    Logo = property(get_Logo, None)
    Glyph = property(get_Glyph, None)
    Number = property(get_Number, None)
    AutomationName = property(get_AutomationName, None)
class ILockScreenInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f59aa65c-9711-4dc9-a6-30-95-b6-cb-8c-da-d0')
    @winrt_commethod(6)
    def add_LockScreenImageChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LockScreenImageChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_LockScreenImage(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(9)
    def add_BadgesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_BadgesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_Badges(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.LockScreen.LockScreenBadge]: ...
    @winrt_commethod(12)
    def add_DetailTextChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DetailTextChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_DetailText(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(15)
    def add_AlarmIconChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AlarmIconChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def get_AlarmIcon(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    LockScreenImage = property(get_LockScreenImage, None)
    Badges = property(get_Badges, None)
    DetailText = property(get_DetailText, None)
    AlarmIcon = property(get_AlarmIcon, None)
class ILockScreenUnlockingDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e7d1ad6-5203-43e7-9b-d6-7c-39-47-d1-e3-fe')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ILockScreenUnlockingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('44e6c007-75fb-4abb-9f-8b-82-47-48-90-0c-71')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class LockApplicationHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LockScreen.LockApplicationHost'
    @winrt_mixinmethod
    def RequestUnlock(self: Windows.ApplicationModel.LockScreen.ILockApplicationHost) -> Void: ...
    @winrt_mixinmethod
    def add_Unlocking(self: Windows.ApplicationModel.LockScreen.ILockApplicationHost, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockApplicationHost, Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unlocking(self: Windows.ApplicationModel.LockScreen.ILockApplicationHost, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.LockScreen.ILockApplicationHostStatics) -> Windows.ApplicationModel.LockScreen.LockApplicationHost: ...
class LockScreenBadge(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LockScreen.LockScreenBadge'
    @winrt_mixinmethod
    def get_Logo(self: Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_Glyph(self: Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_Number(self: Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_AutomationName(self: Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> WinRT_String: ...
    @winrt_mixinmethod
    def LaunchApp(self: Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> Void: ...
    Logo = property(get_Logo, None)
    Glyph = property(get_Glyph, None)
    Number = property(get_Number, None)
    AutomationName = property(get_AutomationName, None)
class LockScreenInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LockScreen.LockScreenInfo'
    @winrt_mixinmethod
    def add_LockScreenImageChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LockScreenImageChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_LockScreenImage(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def add_BadgesChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BadgesChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Badges(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.LockScreen.LockScreenBadge]: ...
    @winrt_mixinmethod
    def add_DetailTextChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DetailTextChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DetailText(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def add_AlarmIconChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.LockScreen.LockScreenInfo, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AlarmIconChanged(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AlarmIcon(self: Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> Windows.Storage.Streams.IRandomAccessStream: ...
    LockScreenImage = property(get_LockScreenImage, None)
    Badges = property(get_Badges, None)
    DetailText = property(get_DetailText, None)
    AlarmIcon = property(get_AlarmIcon, None)
class LockScreenUnlockingDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.LockScreen.ILockScreenUnlockingDeferral) -> Void: ...
class LockScreenUnlockingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs) -> Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
make_head(_module, 'ILockApplicationHost')
make_head(_module, 'ILockApplicationHostStatics')
make_head(_module, 'ILockScreenBadge')
make_head(_module, 'ILockScreenInfo')
make_head(_module, 'ILockScreenUnlockingDeferral')
make_head(_module, 'ILockScreenUnlockingEventArgs')
make_head(_module, 'LockApplicationHost')
make_head(_module, 'LockScreenBadge')
make_head(_module, 'LockScreenInfo')
make_head(_module, 'LockScreenUnlockingDeferral')
make_head(_module, 'LockScreenUnlockingEventArgs')
