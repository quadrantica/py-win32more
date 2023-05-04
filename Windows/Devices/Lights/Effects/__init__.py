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
import Windows.Devices.Lights
import Windows.Devices.Lights.Effects
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Imaging
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILampArrayBitmapEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3238e065-d877-4627-89e5-2a88f7052fa6}')
    @winrt_commethod(6)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_StartDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_StartDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_UpdateInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_UpdateInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_SuggestedBitmapSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def add_BitmapRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Effects.LampArrayBitmapEffect, Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_BitmapRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    SuggestedBitmapSize = property(get_SuggestedBitmapSize, None)
class ILampArrayBitmapEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{13608090-e336-4c8f-9053-a92407ca7b1d}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayBitmapEffect: ...
class ILampArrayBitmapRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c8b4af9e-fe63-4d51-babd-619defb454ba}')
    @winrt_commethod(6)
    def get_SinceStarted(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def UpdateBitmap(self, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class ILampArrayBlinkEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ebbf35f6-2fc5-4bb3-b3c3-6221a7680d13}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_AttackDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_AttackDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_SustainDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_SustainDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_DecayDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def put_DecayDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_RepetitionDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_RepetitionDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def get_StartDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_StartDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(18)
    def get_Occurrences(self) -> Int32: ...
    @winrt_commethod(19)
    def put_Occurrences(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_RepetitionMode(self) -> Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_commethod(21)
    def put_RepetitionMode(self, value: Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    Color = property(get_Color, put_Color)
    AttackDuration = property(get_AttackDuration, put_AttackDuration)
    SustainDuration = property(get_SustainDuration, put_SustainDuration)
    DecayDuration = property(get_DecayDuration, put_DecayDuration)
    RepetitionDelay = property(get_RepetitionDelay, put_RepetitionDelay)
    StartDelay = property(get_StartDelay, put_StartDelay)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
class ILampArrayBlinkEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{879f1d97-9f50-49b2-a56f-013aa08d55e0}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayBlinkEffect: ...
class ILampArrayColorRampEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2b004437-40a7-432e-a0b9-0d570c2153ff}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_RampDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_RampDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_StartDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_CompletionBehavior(self) -> Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_commethod(13)
    def put_CompletionBehavior(self, value: Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    Color = property(get_Color, put_Color)
    RampDuration = property(get_RampDuration, put_RampDuration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
class ILampArrayColorRampEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{520bd133-0c74-4df5-bea7-4899e0266b0f}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayColorRampEffect: ...
class ILampArrayCustomEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ec579170-3c34-4876-818b-5765f78b0ee4}')
    @winrt_commethod(6)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_UpdateInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def add_UpdateRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Effects.LampArrayCustomEffect, Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UpdateRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
class ILampArrayCustomEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{68b4774d-63e5-4af0-a58b-3e535b94e8c9}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayCustomEffect: ...
class ILampArrayEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{11d45590-57fb-4546-b1ce-863107f740df}')
    @winrt_commethod(6)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ZIndex(self, value: Int32) -> Void: ...
    ZIndex = property(get_ZIndex, put_ZIndex)
class ILampArrayEffectPlaylist(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7de58bfe-6f61-4103-98c7-d6632f7b9169}')
    @winrt_commethod(6)
    def Append(self, effect: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Void: ...
    @winrt_commethod(7)
    def OverrideZIndex(self, zIndex: Int32) -> Void: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def get_EffectStartMode(self) -> Windows.Devices.Lights.Effects.LampArrayEffectStartMode: ...
    @winrt_commethod(12)
    def put_EffectStartMode(self, value: Windows.Devices.Lights.Effects.LampArrayEffectStartMode) -> Void: ...
    @winrt_commethod(13)
    def get_Occurrences(self) -> Int32: ...
    @winrt_commethod(14)
    def put_Occurrences(self, value: Int32) -> Void: ...
    @winrt_commethod(15)
    def get_RepetitionMode(self) -> Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_commethod(16)
    def put_RepetitionMode(self, value: Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    EffectStartMode = property(get_EffectStartMode, put_EffectStartMode)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
class ILampArrayEffectPlaylistStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fb15235c-ea35-4c7f-a016-f3bfc6a6c47d}')
    @winrt_commethod(6)
    def StartAll(self, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_commethod(7)
    def StopAll(self, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_commethod(8)
    def PauseAll(self, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
class ILampArraySolidEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{441f8213-43cc-4b33-80eb-c6ddde7dc8ed}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_StartDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_CompletionBehavior(self) -> Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_commethod(13)
    def put_CompletionBehavior(self, value: Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    Color = property(get_Color, put_Color)
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
class ILampArraySolidEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f862a32c-5576-4341-961b-aee1f13cf9dd}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArraySolidEffect: ...
class ILampArrayUpdateRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{73560d6a-576a-48af-8539-67ffa0ab3516}')
    @winrt_commethod(6)
    def get_SinceStarted(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def SetColor(self, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def SetColorForIndex(self, lampIndex: Int32, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def SetSingleColorForIndices(self, desiredColor: Windows.UI.Color, lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_commethod(10)
    def SetColorsForIndices(self, desiredColors: POINTER(Windows.UI.Color_head), lampIndexes: POINTER(Int32)) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class LampArrayBitmapEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBitmapEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Lights.Effects.ILampArrayBitmapEffectFactory, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayBitmapEffect: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateInterval(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_UpdateInterval(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedBitmapSize(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def add_BitmapRequested(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Effects.LampArrayBitmapEffect, Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BitmapRequested(self: Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    SuggestedBitmapSize = property(get_SuggestedBitmapSize, None)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayBitmapRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs'
    @winrt_mixinmethod
    def get_SinceStarted(self: Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def UpdateBitmap(self: Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class LampArrayBlinkEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBlinkEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Lights.Effects.ILampArrayBlinkEffectFactory, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayBlinkEffect: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_AttackDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AttackDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SustainDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SustainDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DecayDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DecayDuration(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionDelay(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RepetitionDelay(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_Occurrences(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionMode(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_mixinmethod
    def put_RepetitionMode(self: Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Color = property(get_Color, put_Color)
    AttackDuration = property(get_AttackDuration, put_AttackDuration)
    SustainDuration = property(get_SustainDuration, put_SustainDuration)
    DecayDuration = property(get_DecayDuration, put_DecayDuration)
    RepetitionDelay = property(get_RepetitionDelay, put_RepetitionDelay)
    StartDelay = property(get_StartDelay, put_StartDelay)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayColorRampEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayColorRampEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Lights.Effects.ILampArrayColorRampEffectFactory, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayColorRampEffect: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_RampDuration(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RampDuration(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionBehavior(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_mixinmethod
    def put_CompletionBehavior(self: Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Color = property(get_Color, put_Color)
    RampDuration = property(get_RampDuration, put_RampDuration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayCustomEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayCustomEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Lights.Effects.ILampArrayCustomEffectFactory, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArrayCustomEffect: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateInterval(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_UpdateInterval(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateRequested(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Effects.LampArrayCustomEffect, Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateRequested(self: Windows.Devices.Lights.Effects.ILampArrayCustomEffect, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    ZIndex = property(get_ZIndex, put_ZIndex)
LampArrayEffectCompletionBehavior = Int32
LampArrayEffectCompletionBehavior_ClearState: LampArrayEffectCompletionBehavior = 0
LampArrayEffectCompletionBehavior_KeepState: LampArrayEffectCompletionBehavior = 1
class LampArrayEffectPlaylist(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayEffectPlaylist'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Lights.Effects.LampArrayEffectPlaylist: ...
    @winrt_mixinmethod
    def Append(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, effect: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Void: ...
    @winrt_mixinmethod
    def OverrideZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, zIndex: Int32) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def get_EffectStartMode(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Windows.Devices.Lights.Effects.LampArrayEffectStartMode: ...
    @winrt_mixinmethod
    def put_EffectStartMode(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: Windows.Devices.Lights.Effects.LampArrayEffectStartMode) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Int32: ...
    @winrt_mixinmethod
    def put_Occurrences(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionMode(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_mixinmethod
    def put_RepetitionMode(self: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Lights.Effects.ILampArrayEffect], index: UInt32) -> Windows.Devices.Lights.Effects.ILampArrayEffect: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Lights.Effects.ILampArrayEffect]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Lights.Effects.ILampArrayEffect], value: Windows.Devices.Lights.Effects.ILampArrayEffect, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Lights.Effects.ILampArrayEffect], startIndex: UInt32, items: POINTER(Windows.Devices.Lights.Effects.ILampArrayEffect)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.ILampArrayEffect]) -> Windows.Foundation.Collections.IIterator[Windows.Devices.Lights.Effects.ILampArrayEffect]: ...
    @winrt_classmethod
    def StartAll(cls: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_classmethod
    def StopAll(cls: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_classmethod
    def PauseAll(cls: Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: Windows.Foundation.Collections.IIterable[Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    EffectStartMode = property(get_EffectStartMode, put_EffectStartMode)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
    Size = property(get_Size, None)
LampArrayEffectStartMode = Int32
LampArrayEffectStartMode_Sequential: LampArrayEffectStartMode = 0
LampArrayEffectStartMode_Simultaneous: LampArrayEffectStartMode = 1
LampArrayRepetitionMode = Int32
LampArrayRepetitionMode_Occurrences: LampArrayRepetitionMode = 0
LampArrayRepetitionMode_Forever: LampArrayRepetitionMode = 1
class LampArraySolidEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArraySolidEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Lights.Effects.ILampArraySolidEffectFactory, lampArray: Windows.Devices.Lights.LampArray, lampIndexes: POINTER(Int32)) -> Windows.Devices.Lights.Effects.LampArraySolidEffect: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionBehavior(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_mixinmethod
    def put_CompletionBehavior(self: Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Color = property(get_Color, put_Color)
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayUpdateRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs'
    @winrt_mixinmethod
    def get_SinceStarted(self: Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetColor(self: Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetColorForIndex(self: Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, lampIndex: Int32, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetSingleColorForIndices(self: Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColor: Windows.UI.Color, lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForIndices(self: Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColors: POINTER(Windows.UI.Color_head), lampIndexes: POINTER(Int32)) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
make_head(_module, 'ILampArrayBitmapEffect')
make_head(_module, 'ILampArrayBitmapEffectFactory')
make_head(_module, 'ILampArrayBitmapRequestedEventArgs')
make_head(_module, 'ILampArrayBlinkEffect')
make_head(_module, 'ILampArrayBlinkEffectFactory')
make_head(_module, 'ILampArrayColorRampEffect')
make_head(_module, 'ILampArrayColorRampEffectFactory')
make_head(_module, 'ILampArrayCustomEffect')
make_head(_module, 'ILampArrayCustomEffectFactory')
make_head(_module, 'ILampArrayEffect')
make_head(_module, 'ILampArrayEffectPlaylist')
make_head(_module, 'ILampArrayEffectPlaylistStatics')
make_head(_module, 'ILampArraySolidEffect')
make_head(_module, 'ILampArraySolidEffectFactory')
make_head(_module, 'ILampArrayUpdateRequestedEventArgs')
make_head(_module, 'LampArrayBitmapEffect')
make_head(_module, 'LampArrayBitmapRequestedEventArgs')
make_head(_module, 'LampArrayBlinkEffect')
make_head(_module, 'LampArrayColorRampEffect')
make_head(_module, 'LampArrayCustomEffect')
make_head(_module, 'LampArrayEffectPlaylist')
make_head(_module, 'LampArraySolidEffect')
make_head(_module, 'LampArrayUpdateRequestedEventArgs')
