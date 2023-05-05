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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics
import Windows.Graphics.DirectX
import Windows.Graphics.Effects
import Windows.System
import Windows.UI
import Windows.UI.Composition
import Windows.UI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AmbientLight(ComPtr):
    extends: Windows.UI.Composition.CompositionLight
    default_interface: Windows.UI.Composition.IAmbientLight
    _classid_ = 'Windows.UI.Composition.AmbientLight'
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.IAmbientLight) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.IAmbientLight, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: Windows.UI.Composition.IAmbientLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: Windows.UI.Composition.IAmbientLight2, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Intensity = property(get_Intensity, put_Intensity)
class AnimationController(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IAnimationController
    _classid_ = 'Windows.UI.Composition.AnimationController'
    @winrt_mixinmethod
    def get_PlaybackRate(self: Windows.UI.Composition.IAnimationController) -> Single: ...
    @winrt_mixinmethod
    def put_PlaybackRate(self: Windows.UI.Composition.IAnimationController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.UI.Composition.IAnimationController) -> Single: ...
    @winrt_mixinmethod
    def put_Progress(self: Windows.UI.Composition.IAnimationController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressBehavior(self: Windows.UI.Composition.IAnimationController) -> Windows.UI.Composition.AnimationControllerProgressBehavior: ...
    @winrt_mixinmethod
    def put_ProgressBehavior(self: Windows.UI.Composition.IAnimationController, value: Windows.UI.Composition.AnimationControllerProgressBehavior) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: Windows.UI.Composition.IAnimationController) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: Windows.UI.Composition.IAnimationController) -> Void: ...
    @winrt_classmethod
    def get_MaxPlaybackRate(cls: Windows.UI.Composition.IAnimationControllerStatics) -> Single: ...
    @winrt_classmethod
    def get_MinPlaybackRate(cls: Windows.UI.Composition.IAnimationControllerStatics) -> Single: ...
    PlaybackRate = property(get_PlaybackRate, put_PlaybackRate)
    Progress = property(get_Progress, put_Progress)
    ProgressBehavior = property(get_ProgressBehavior, put_ProgressBehavior)
    MaxPlaybackRate = property(get_MaxPlaybackRate, None)
    MinPlaybackRate = property(get_MinPlaybackRate, None)
AnimationControllerProgressBehavior = Int32
AnimationControllerProgressBehavior_Default: AnimationControllerProgressBehavior = 0
AnimationControllerProgressBehavior_IncludesDelayTime: AnimationControllerProgressBehavior = 1
AnimationDelayBehavior = Int32
AnimationDelayBehavior_SetInitialValueAfterDelay: AnimationDelayBehavior = 0
AnimationDelayBehavior_SetInitialValueBeforeDelay: AnimationDelayBehavior = 1
AnimationDirection = Int32
AnimationDirection_Normal: AnimationDirection = 0
AnimationDirection_Reverse: AnimationDirection = 1
AnimationDirection_Alternate: AnimationDirection = 2
AnimationDirection_AlternateReverse: AnimationDirection = 3
AnimationIterationBehavior = Int32
AnimationIterationBehavior_Count: AnimationIterationBehavior = 0
AnimationIterationBehavior_Forever: AnimationIterationBehavior = 1
AnimationPropertyAccessMode = Int32
AnimationPropertyAccessMode_None: AnimationPropertyAccessMode = 0
AnimationPropertyAccessMode_ReadOnly: AnimationPropertyAccessMode = 1
AnimationPropertyAccessMode_WriteOnly: AnimationPropertyAccessMode = 2
AnimationPropertyAccessMode_ReadWrite: AnimationPropertyAccessMode = 3
class AnimationPropertyInfo(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IAnimationPropertyInfo
    _classid_ = 'Windows.UI.Composition.AnimationPropertyInfo'
    @winrt_mixinmethod
    def get_AccessMode(self: Windows.UI.Composition.IAnimationPropertyInfo) -> Windows.UI.Composition.AnimationPropertyAccessMode: ...
    @winrt_mixinmethod
    def put_AccessMode(self: Windows.UI.Composition.IAnimationPropertyInfo, value: Windows.UI.Composition.AnimationPropertyAccessMode) -> Void: ...
    @winrt_mixinmethod
    def GetResolvedCompositionObject(self: Windows.UI.Composition.IAnimationPropertyInfo2) -> Windows.UI.Composition.CompositionObject: ...
    @winrt_mixinmethod
    def GetResolvedCompositionObjectProperty(self: Windows.UI.Composition.IAnimationPropertyInfo2) -> WinRT_String: ...
    AccessMode = property(get_AccessMode, put_AccessMode)
AnimationStopBehavior = Int32
AnimationStopBehavior_LeaveCurrentValue: AnimationStopBehavior = 0
AnimationStopBehavior_SetToInitialValue: AnimationStopBehavior = 1
AnimationStopBehavior_SetToFinalValue: AnimationStopBehavior = 2
class BackEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IBackEasingFunction
    _classid_ = 'Windows.UI.Composition.BackEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.IBackEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Amplitude(self: Windows.UI.Composition.IBackEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Amplitude = property(get_Amplitude, None)
class BooleanKeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IBooleanKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.BooleanKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IBooleanKeyFrameAnimation, normalizedProgressKey: Single, value: Boolean) -> Void: ...
class BounceEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IBounceEasingFunction
    _classid_ = 'Windows.UI.Composition.BounceEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.IBounceEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Bounces(self: Windows.UI.Composition.IBounceEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def get_Bounciness(self: Windows.UI.Composition.IBounceEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Bounces = property(get_Bounces, None)
    Bounciness = property(get_Bounciness, None)
class BounceScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.ScalarNaturalMotionAnimation
    default_interface: Windows.UI.Composition.IBounceScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: Windows.UI.Composition.IBounceScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: Windows.UI.Composition.IBounceScalarNaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: Windows.UI.Composition.IBounceScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: Windows.UI.Composition.IBounceScalarNaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class BounceVector2NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.Vector2NaturalMotionAnimation
    default_interface: Windows.UI.Composition.IBounceVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceVector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: Windows.UI.Composition.IBounceVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: Windows.UI.Composition.IBounceVector2NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: Windows.UI.Composition.IBounceVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: Windows.UI.Composition.IBounceVector2NaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class BounceVector3NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.Vector3NaturalMotionAnimation
    default_interface: Windows.UI.Composition.IBounceVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceVector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: Windows.UI.Composition.IBounceVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: Windows.UI.Composition.IBounceVector3NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: Windows.UI.Composition.IBounceVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: Windows.UI.Composition.IBounceVector3NaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class CircleEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.ICircleEasingFunction
    _classid_ = 'Windows.UI.Composition.CircleEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.ICircleEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class ColorKeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IColorKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.ColorKeyFrameAnimation'
    @winrt_mixinmethod
    def get_InterpolationColorSpace(self: Windows.UI.Composition.IColorKeyFrameAnimation) -> Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_mixinmethod
    def put_InterpolationColorSpace(self: Windows.UI.Composition.IColorKeyFrameAnimation, value: Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IColorKeyFrameAnimation, normalizedProgressKey: Single, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IColorKeyFrameAnimation, normalizedProgressKey: Single, value: Windows.UI.Color, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    InterpolationColorSpace = property(get_InterpolationColorSpace, put_InterpolationColorSpace)
class CompositionAnimation(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionAnimation
    _classid_ = 'Windows.UI.Composition.CompositionAnimation'
    @winrt_mixinmethod
    def ClearAllParameters(self: Windows.UI.Composition.ICompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def ClearParameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetColorParameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetMatrix3x2Parameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def SetMatrix4x4Parameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def SetQuaternionParameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def SetReferenceParameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, compositionObject: Windows.UI.Composition.CompositionObject) -> Void: ...
    @winrt_mixinmethod
    def SetScalarParameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Single) -> Void: ...
    @winrt_mixinmethod
    def SetVector2Parameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def SetVector3Parameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetVector4Parameter(self: Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def SetBooleanParameter(self: Windows.UI.Composition.ICompositionAnimation2, key: WinRT_String, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: Windows.UI.Composition.ICompositionAnimation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Target(self: Windows.UI.Composition.ICompositionAnimation2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValueExpressions(self: Windows.UI.Composition.ICompositionAnimation3) -> Windows.UI.Composition.InitialValueExpressionCollection: ...
    @winrt_mixinmethod
    def SetExpressionReferenceParameter(self: Windows.UI.Composition.ICompositionAnimation4, parameterName: WinRT_String, source: Windows.UI.Composition.IAnimationObject) -> Void: ...
    Target = property(get_Target, put_Target)
    InitialValueExpressions = property(get_InitialValueExpressions, None)
class CompositionAnimationGroup(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionAnimationGroup
    _classid_ = 'Windows.UI.Composition.CompositionAnimationGroup'
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.ICompositionAnimationGroup) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: Windows.UI.Composition.ICompositionAnimationGroup, value: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.ICompositionAnimationGroup, value: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.ICompositionAnimationGroup) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.CompositionAnimation]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.CompositionAnimation]: ...
    Count = property(get_Count, None)
class CompositionBackdropBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionBackdropBrush
    _classid_ = 'Windows.UI.Composition.CompositionBackdropBrush'
CompositionBackfaceVisibility = Int32
CompositionBackfaceVisibility_Inherit: CompositionBackfaceVisibility = 0
CompositionBackfaceVisibility_Visible: CompositionBackfaceVisibility = 1
CompositionBackfaceVisibility_Hidden: CompositionBackfaceVisibility = 2
class CompositionBatchCompletedEventArgs(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionBatchCompletedEventArgs
    _classid_ = 'Windows.UI.Composition.CompositionBatchCompletedEventArgs'
CompositionBatchTypes = UInt32
CompositionBatchTypes_None: CompositionBatchTypes = 0
CompositionBatchTypes_Animation: CompositionBatchTypes = 1
CompositionBatchTypes_Effect: CompositionBatchTypes = 2
CompositionBatchTypes_InfiniteAnimation: CompositionBatchTypes = 4
CompositionBatchTypes_AllAnimations: CompositionBatchTypes = 5
CompositionBitmapInterpolationMode = Int32
CompositionBitmapInterpolationMode_NearestNeighbor: CompositionBitmapInterpolationMode = 0
CompositionBitmapInterpolationMode_Linear: CompositionBitmapInterpolationMode = 1
CompositionBitmapInterpolationMode_MagLinearMinLinearMipLinear: CompositionBitmapInterpolationMode = 2
CompositionBitmapInterpolationMode_MagLinearMinLinearMipNearest: CompositionBitmapInterpolationMode = 3
CompositionBitmapInterpolationMode_MagLinearMinNearestMipLinear: CompositionBitmapInterpolationMode = 4
CompositionBitmapInterpolationMode_MagLinearMinNearestMipNearest: CompositionBitmapInterpolationMode = 5
CompositionBitmapInterpolationMode_MagNearestMinLinearMipLinear: CompositionBitmapInterpolationMode = 6
CompositionBitmapInterpolationMode_MagNearestMinLinearMipNearest: CompositionBitmapInterpolationMode = 7
CompositionBitmapInterpolationMode_MagNearestMinNearestMipLinear: CompositionBitmapInterpolationMode = 8
CompositionBitmapInterpolationMode_MagNearestMinNearestMipNearest: CompositionBitmapInterpolationMode = 9
CompositionBorderMode = Int32
CompositionBorderMode_Inherit: CompositionBorderMode = 0
CompositionBorderMode_Soft: CompositionBorderMode = 1
CompositionBorderMode_Hard: CompositionBorderMode = 2
class CompositionBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionBrush
    _classid_ = 'Windows.UI.Composition.CompositionBrush'
class CompositionCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositionCapabilities
    _classid_ = 'Windows.UI.Composition.CompositionCapabilities'
    @winrt_mixinmethod
    def AreEffectsSupported(self: Windows.UI.Composition.ICompositionCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def AreEffectsFast(self: Windows.UI.Composition.ICompositionCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.UI.Composition.ICompositionCapabilities, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.CompositionCapabilities, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.UI.Composition.ICompositionCapabilities, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Composition.ICompositionCapabilitiesStatics) -> Windows.UI.Composition.CompositionCapabilities: ...
class CompositionClip(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionClip
    _classid_ = 'Windows.UI.Composition.CompositionClip'
    @winrt_mixinmethod
    def get_AnchorPoint(self: Windows.UI.Composition.ICompositionClip2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: Windows.UI.Composition.ICompositionClip2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Composition.ICompositionClip2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Composition.ICompositionClip2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionClip2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionClip2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.ICompositionClip2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.ICompositionClip2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionClip2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionClip2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.ICompositionClip2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.ICompositionClip2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Composition.ICompositionClip2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Composition.ICompositionClip2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class CompositionColorBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionColorBrush
    _classid_ = 'Windows.UI.Composition.CompositionColorBrush'
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.ICompositionColorBrush) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.ICompositionColorBrush, value: Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class CompositionColorGradientStop(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionColorGradientStop
    _classid_ = 'Windows.UI.Composition.CompositionColorGradientStop'
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.ICompositionColorGradientStop) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.ICompositionColorGradientStop, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionColorGradientStop) -> Single: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionColorGradientStop, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class CompositionColorGradientStopCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositionColorGradientStopCollection
    _classid_ = 'Windows.UI.Composition.CompositionColorGradientStopCollection'
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.CompositionColorGradientStop]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.CompositionColorGradientStop]: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], index: UInt32) -> Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Composition.CompositionColorGradientStop]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], value: Windows.UI.Composition.CompositionColorGradientStop, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], index: UInt32, value: Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], index: UInt32, value: Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], value: Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], startIndex: UInt32, items: POINTER(Windows.UI.Composition.CompositionColorGradientStop)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionColorGradientStop], items: POINTER(Windows.UI.Composition.CompositionColorGradientStop)) -> Void: ...
    Size = property(get_Size, None)
CompositionColorSpace = Int32
CompositionColorSpace_Auto: CompositionColorSpace = 0
CompositionColorSpace_Hsl: CompositionColorSpace = 1
CompositionColorSpace_Rgb: CompositionColorSpace = 2
CompositionColorSpace_HslLinear: CompositionColorSpace = 3
CompositionColorSpace_RgbLinear: CompositionColorSpace = 4
class CompositionCommitBatch(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionCommitBatch
    _classid_ = 'Windows.UI.Composition.CompositionCommitBatch'
    @winrt_mixinmethod
    def get_IsActive(self: Windows.UI.Composition.ICompositionCommitBatch) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEnded(self: Windows.UI.Composition.ICompositionCommitBatch) -> Boolean: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.UI.Composition.ICompositionCommitBatch, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.UI.Composition.ICompositionCommitBatch, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
CompositionCompositeMode = Int32
CompositionCompositeMode_Inherit: CompositionCompositeMode = 0
CompositionCompositeMode_SourceOver: CompositionCompositeMode = 1
CompositionCompositeMode_DestinationInvert: CompositionCompositeMode = 2
CompositionCompositeMode_MinBlend: CompositionCompositeMode = 3
class CompositionContainerShape(ComPtr):
    extends: Windows.UI.Composition.CompositionShape
    default_interface: Windows.UI.Composition.ICompositionContainerShape
    _classid_ = 'Windows.UI.Composition.CompositionContainerShape'
    @winrt_mixinmethod
    def get_Shapes(self: Windows.UI.Composition.ICompositionContainerShape) -> Windows.UI.Composition.CompositionShapeCollection: ...
    Shapes = property(get_Shapes, None)
class CompositionDrawingSurface(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionDrawingSurface
    _classid_ = 'Windows.UI.Composition.CompositionDrawingSurface'
    @winrt_mixinmethod
    def get_AlphaMode(self: Windows.UI.Composition.ICompositionDrawingSurface) -> Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: Windows.UI.Composition.ICompositionDrawingSurface) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.ICompositionDrawingSurface) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SizeInt32(self: Windows.UI.Composition.ICompositionDrawingSurface2) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def Resize(self: Windows.UI.Composition.ICompositionDrawingSurface2, sizePixels: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def Scroll(self: Windows.UI.Composition.ICompositionDrawingSurface2, offset: Windows.Graphics.PointInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollRect(self: Windows.UI.Composition.ICompositionDrawingSurface2, offset: Windows.Graphics.PointInt32, scrollRect: Windows.Graphics.RectInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollWithClip(self: Windows.UI.Composition.ICompositionDrawingSurface2, offset: Windows.Graphics.PointInt32, clipRect: Windows.Graphics.RectInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollRectWithClip(self: Windows.UI.Composition.ICompositionDrawingSurface2, offset: Windows.Graphics.PointInt32, clipRect: Windows.Graphics.RectInt32, scrollRect: Windows.Graphics.RectInt32) -> Void: ...
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
    SizeInt32 = property(get_SizeInt32, None)
CompositionDropShadowSourcePolicy = Int32
CompositionDropShadowSourcePolicy_Default: CompositionDropShadowSourcePolicy = 0
CompositionDropShadowSourcePolicy_InheritFromVisualContent: CompositionDropShadowSourcePolicy = 1
class CompositionEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionEasingFunction
    _classid_ = 'Windows.UI.Composition.CompositionEasingFunction'
    @winrt_classmethod
    def CreateCubicBezierEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, controlPoint1: Windows.Foundation.Numerics.Vector2, controlPoint2: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_classmethod
    def CreateLinearEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_classmethod
    def CreateStepEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_classmethod
    def CreateStepEasingFunctionWithStepCount(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, stepCount: Int32) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_classmethod
    def CreateBackEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, amplitude: Single) -> Windows.UI.Composition.BackEasingFunction: ...
    @winrt_classmethod
    def CreateBounceEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, bounces: Int32, bounciness: Single) -> Windows.UI.Composition.BounceEasingFunction: ...
    @winrt_classmethod
    def CreateCircleEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode) -> Windows.UI.Composition.CircleEasingFunction: ...
    @winrt_classmethod
    def CreateElasticEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, oscillations: Int32, springiness: Single) -> Windows.UI.Composition.ElasticEasingFunction: ...
    @winrt_classmethod
    def CreateExponentialEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, exponent: Single) -> Windows.UI.Composition.ExponentialEasingFunction: ...
    @winrt_classmethod
    def CreatePowerEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, power: Single) -> Windows.UI.Composition.PowerEasingFunction: ...
    @winrt_classmethod
    def CreateSineEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode) -> Windows.UI.Composition.SineEasingFunction: ...
CompositionEasingFunctionMode = Int32
CompositionEasingFunctionMode_In: CompositionEasingFunctionMode = 0
CompositionEasingFunctionMode_Out: CompositionEasingFunctionMode = 1
CompositionEasingFunctionMode_InOut: CompositionEasingFunctionMode = 2
class CompositionEffectBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionEffectBrush
    _classid_ = 'Windows.UI.Composition.CompositionEffectBrush'
    @winrt_mixinmethod
    def GetSourceParameter(self: Windows.UI.Composition.ICompositionEffectBrush, name: WinRT_String) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def SetSourceParameter(self: Windows.UI.Composition.ICompositionEffectBrush, name: WinRT_String, source: Windows.UI.Composition.CompositionBrush) -> Void: ...
class CompositionEffectFactory(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionEffectFactory
    _classid_ = 'Windows.UI.Composition.CompositionEffectFactory'
    @winrt_mixinmethod
    def CreateBrush(self: Windows.UI.Composition.ICompositionEffectFactory) -> Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.UI.Composition.ICompositionEffectFactory) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_LoadStatus(self: Windows.UI.Composition.ICompositionEffectFactory) -> Windows.UI.Composition.CompositionEffectFactoryLoadStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LoadStatus = property(get_LoadStatus, None)
CompositionEffectFactoryLoadStatus = Int32
CompositionEffectFactoryLoadStatus_Success: CompositionEffectFactoryLoadStatus = 0
CompositionEffectFactoryLoadStatus_EffectTooComplex: CompositionEffectFactoryLoadStatus = 1
CompositionEffectFactoryLoadStatus_Pending: CompositionEffectFactoryLoadStatus = 2
CompositionEffectFactoryLoadStatus_Other: CompositionEffectFactoryLoadStatus = -1
class CompositionEffectSourceParameter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositionEffectSourceParameter
    _classid_ = 'Windows.UI.Composition.CompositionEffectSourceParameter'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Composition.ICompositionEffectSourceParameterFactory, name: WinRT_String) -> Windows.UI.Composition.CompositionEffectSourceParameter: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.UI.Composition.ICompositionEffectSourceParameter) -> WinRT_String: ...
    Name = property(get_Name, None)
class CompositionEllipseGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionGeometry
    default_interface: Windows.UI.Composition.ICompositionEllipseGeometry
    _classid_ = 'Windows.UI.Composition.CompositionEllipseGeometry'
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Composition.ICompositionEllipseGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Center(self: Windows.UI.Composition.ICompositionEllipseGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: Windows.UI.Composition.ICompositionEllipseGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Radius(self: Windows.UI.Composition.ICompositionEllipseGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class CompositionGeometricClip(ComPtr):
    extends: Windows.UI.Composition.CompositionClip
    default_interface: Windows.UI.Composition.ICompositionGeometricClip
    _classid_ = 'Windows.UI.Composition.CompositionGeometricClip'
    @winrt_mixinmethod
    def get_Geometry(self: Windows.UI.Composition.ICompositionGeometricClip) -> Windows.UI.Composition.CompositionGeometry: ...
    @winrt_mixinmethod
    def put_Geometry(self: Windows.UI.Composition.ICompositionGeometricClip, value: Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_ViewBox(self: Windows.UI.Composition.ICompositionGeometricClip) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def put_ViewBox(self: Windows.UI.Composition.ICompositionGeometricClip, value: Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Geometry = property(get_Geometry, put_Geometry)
    ViewBox = property(get_ViewBox, put_ViewBox)
class CompositionGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionGeometry
    _classid_ = 'Windows.UI.Composition.CompositionGeometry'
    @winrt_mixinmethod
    def get_TrimEnd(self: Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimEnd(self: Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TrimOffset(self: Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimOffset(self: Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TrimStart(self: Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimStart(self: Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    TrimEnd = property(get_TrimEnd, put_TrimEnd)
    TrimOffset = property(get_TrimOffset, put_TrimOffset)
    TrimStart = property(get_TrimStart, put_TrimStart)
CompositionGetValueStatus = Int32
CompositionGetValueStatus_Succeeded: CompositionGetValueStatus = 0
CompositionGetValueStatus_TypeMismatch: CompositionGetValueStatus = 1
CompositionGetValueStatus_NotFound: CompositionGetValueStatus = 2
class CompositionGradientBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionGradientBrush'
    @winrt_mixinmethod
    def get_AnchorPoint(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_ColorStops(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.UI.Composition.CompositionColorGradientStopCollection: ...
    @winrt_mixinmethod
    def get_ExtendMode(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.UI.Composition.CompositionGradientExtendMode: ...
    @winrt_mixinmethod
    def put_ExtendMode(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.UI.Composition.CompositionGradientExtendMode) -> Void: ...
    @winrt_mixinmethod
    def get_InterpolationSpace(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_mixinmethod
    def put_InterpolationSpace(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.ICompositionGradientBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.ICompositionGradientBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionGradientBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionGradientBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Composition.ICompositionGradientBrush) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Composition.ICompositionGradientBrush, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_MappingMode(self: Windows.UI.Composition.ICompositionGradientBrush2) -> Windows.UI.Composition.CompositionMappingMode: ...
    @winrt_mixinmethod
    def put_MappingMode(self: Windows.UI.Composition.ICompositionGradientBrush2, value: Windows.UI.Composition.CompositionMappingMode) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    ColorStops = property(get_ColorStops, None)
    ExtendMode = property(get_ExtendMode, put_ExtendMode)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    MappingMode = property(get_MappingMode, put_MappingMode)
CompositionGradientExtendMode = Int32
CompositionGradientExtendMode_Clamp: CompositionGradientExtendMode = 0
CompositionGradientExtendMode_Wrap: CompositionGradientExtendMode = 1
CompositionGradientExtendMode_Mirror: CompositionGradientExtendMode = 2
class CompositionGraphicsDevice(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionGraphicsDevice
    _classid_ = 'Windows.UI.Composition.CompositionGraphicsDevice'
    @winrt_mixinmethod
    def CreateDrawingSurface(self: Windows.UI.Composition.ICompositionGraphicsDevice, sizePixels: Windows.Foundation.Size, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_mixinmethod
    def add_RenderingDeviceReplaced(self: Windows.UI.Composition.ICompositionGraphicsDevice, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.CompositionGraphicsDevice, Windows.UI.Composition.RenderingDeviceReplacedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RenderingDeviceReplaced(self: Windows.UI.Composition.ICompositionGraphicsDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateDrawingSurface2(self: Windows.UI.Composition.ICompositionGraphicsDevice2, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_mixinmethod
    def CreateVirtualDrawingSurface(self: Windows.UI.Composition.ICompositionGraphicsDevice2, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionVirtualDrawingSurface: ...
    @winrt_mixinmethod
    def CreateMipmapSurface(self: Windows.UI.Composition.ICompositionGraphicsDevice3, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionMipmapSurface: ...
    @winrt_mixinmethod
    def Trim(self: Windows.UI.Composition.ICompositionGraphicsDevice3) -> Void: ...
    @winrt_mixinmethod
    def CaptureAsync(self: Windows.UI.Composition.ICompositionGraphicsDevice4, captureVisual: Windows.UI.Composition.Visual, size: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode, sdrBoost: Single) -> Windows.Foundation.IAsyncOperation[Windows.UI.Composition.ICompositionSurface]: ...
class CompositionLight(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionLight
    _classid_ = 'Windows.UI.Composition.CompositionLight'
    @winrt_mixinmethod
    def get_Targets(self: Windows.UI.Composition.ICompositionLight) -> Windows.UI.Composition.VisualUnorderedCollection: ...
    @winrt_mixinmethod
    def get_ExclusionsFromTargets(self: Windows.UI.Composition.ICompositionLight2) -> Windows.UI.Composition.VisualUnorderedCollection: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.UI.Composition.ICompositionLight3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.UI.Composition.ICompositionLight3, value: Boolean) -> Void: ...
    Targets = property(get_Targets, None)
    ExclusionsFromTargets = property(get_ExclusionsFromTargets, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class CompositionLineGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionGeometry
    default_interface: Windows.UI.Composition.ICompositionLineGeometry
    _classid_ = 'Windows.UI.Composition.CompositionLineGeometry'
    @winrt_mixinmethod
    def get_Start(self: Windows.UI.Composition.ICompositionLineGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Start(self: Windows.UI.Composition.ICompositionLineGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_End(self: Windows.UI.Composition.ICompositionLineGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_End(self: Windows.UI.Composition.ICompositionLineGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Start = property(get_Start, put_Start)
    End = property(get_End, put_End)
class CompositionLinearGradientBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionGradientBrush
    default_interface: Windows.UI.Composition.ICompositionLinearGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionLinearGradientBrush'
    @winrt_mixinmethod
    def get_EndPoint(self: Windows.UI.Composition.ICompositionLinearGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EndPoint(self: Windows.UI.Composition.ICompositionLinearGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_StartPoint(self: Windows.UI.Composition.ICompositionLinearGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_StartPoint(self: Windows.UI.Composition.ICompositionLinearGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
CompositionMappingMode = Int32
CompositionMappingMode_Absolute: CompositionMappingMode = 0
CompositionMappingMode_Relative: CompositionMappingMode = 1
class CompositionMaskBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionMaskBrush
    _classid_ = 'Windows.UI.Composition.CompositionMaskBrush'
    @winrt_mixinmethod
    def get_Mask(self: Windows.UI.Composition.ICompositionMaskBrush) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Mask(self: Windows.UI.Composition.ICompositionMaskBrush, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Composition.ICompositionMaskBrush) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Composition.ICompositionMaskBrush, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    Mask = property(get_Mask, put_Mask)
    Source = property(get_Source, put_Source)
class CompositionMipmapSurface(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionMipmapSurface
    _classid_ = 'Windows.UI.Composition.CompositionMipmapSurface'
    @winrt_mixinmethod
    def get_LevelCount(self: Windows.UI.Composition.ICompositionMipmapSurface) -> UInt32: ...
    @winrt_mixinmethod
    def get_AlphaMode(self: Windows.UI.Composition.ICompositionMipmapSurface) -> Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: Windows.UI.Composition.ICompositionMipmapSurface) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_SizeInt32(self: Windows.UI.Composition.ICompositionMipmapSurface) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def GetDrawingSurfaceForLevel(self: Windows.UI.Composition.ICompositionMipmapSurface, level: UInt32) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    LevelCount = property(get_LevelCount, None)
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    SizeInt32 = property(get_SizeInt32, None)
class CompositionNineGridBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionNineGridBrush
    _classid_ = 'Windows.UI.Composition.CompositionNineGridBrush'
    @winrt_mixinmethod
    def get_BottomInset(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInset(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_IsCenterHollow(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCenterHollow(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInset(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInset(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInset(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RightInset(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RightInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_TopInset(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_TopInset(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_TopInsetScale(self: Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsets(self: Windows.UI.Composition.ICompositionNineGridBrush, inset: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetsWithValues(self: Windows.UI.Composition.ICompositionNineGridBrush, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetScales(self: Windows.UI.Composition.ICompositionNineGridBrush, scale: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetScalesWithValues(self: Windows.UI.Composition.ICompositionNineGridBrush, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    BottomInsetScale = property(get_BottomInsetScale, put_BottomInsetScale)
    IsCenterHollow = property(get_IsCenterHollow, put_IsCenterHollow)
    LeftInset = property(get_LeftInset, put_LeftInset)
    LeftInsetScale = property(get_LeftInsetScale, put_LeftInsetScale)
    RightInset = property(get_RightInset, put_RightInset)
    RightInsetScale = property(get_RightInsetScale, put_RightInsetScale)
    Source = property(get_Source, put_Source)
    TopInset = property(get_TopInset, put_TopInset)
    TopInsetScale = property(get_TopInsetScale, put_TopInsetScale)
class CompositionObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositionObject
    _classid_ = 'Windows.UI.Composition.CompositionObject'
    @winrt_mixinmethod
    def get_Compositor(self: Windows.UI.Composition.ICompositionObject) -> Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Composition.ICompositionObject) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.UI.Composition.ICompositionObject) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_mixinmethod
    def StartAnimation(self: Windows.UI.Composition.ICompositionObject, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def StopAnimation(self: Windows.UI.Composition.ICompositionObject, propertyName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Comment(self: Windows.UI.Composition.ICompositionObject2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Comment(self: Windows.UI.Composition.ICompositionObject2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ImplicitAnimations(self: Windows.UI.Composition.ICompositionObject2) -> Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_mixinmethod
    def put_ImplicitAnimations(self: Windows.UI.Composition.ICompositionObject2, value: Windows.UI.Composition.ImplicitAnimationCollection) -> Void: ...
    @winrt_mixinmethod
    def StartAnimationGroup(self: Windows.UI.Composition.ICompositionObject2, value: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def StopAnimationGroup(self: Windows.UI.Composition.ICompositionObject2, value: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Composition.ICompositionObject3) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def TryGetAnimationController(self: Windows.UI.Composition.ICompositionObject4, propertyName: WinRT_String) -> Windows.UI.Composition.AnimationController: ...
    @winrt_mixinmethod
    def StartAnimationWithController(self: Windows.UI.Composition.ICompositionObject5, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation, animationController: Windows.UI.Composition.AnimationController) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def StartAnimationWithIAnimationObject(cls: Windows.UI.Composition.ICompositionObjectStatics, target: Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_classmethod
    def StartAnimationGroupWithIAnimationObject(cls: Windows.UI.Composition.ICompositionObjectStatics, target: Windows.UI.Composition.IAnimationObject, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    Compositor = property(get_Compositor, None)
    Dispatcher = property(get_Dispatcher, None)
    Properties = property(get_Properties, None)
    Comment = property(get_Comment, put_Comment)
    ImplicitAnimations = property(get_ImplicitAnimations, put_ImplicitAnimations)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CompositionPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositionPath
    _classid_ = 'Windows.UI.Composition.CompositionPath'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Composition.ICompositionPathFactory, source: Windows.Graphics.IGeometrySource2D) -> Windows.UI.Composition.CompositionPath: ...
class CompositionPathGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionGeometry
    default_interface: Windows.UI.Composition.ICompositionPathGeometry
    _classid_ = 'Windows.UI.Composition.CompositionPathGeometry'
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Composition.ICompositionPathGeometry) -> Windows.UI.Composition.CompositionPath: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.UI.Composition.ICompositionPathGeometry, value: Windows.UI.Composition.CompositionPath) -> Void: ...
    Path = property(get_Path, put_Path)
class CompositionProjectedShadow(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionProjectedShadow
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadow'
    @winrt_mixinmethod
    def get_BlurRadiusMultiplier(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_BlurRadiusMultiplier(self: Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Casters(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Windows.UI.Composition.CompositionProjectedShadowCasterCollection: ...
    @winrt_mixinmethod
    def get_LightSource(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Windows.UI.Composition.CompositionLight: ...
    @winrt_mixinmethod
    def put_LightSource(self: Windows.UI.Composition.ICompositionProjectedShadow, value: Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBlurRadius(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_MaxBlurRadius(self: Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinBlurRadius(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_MinBlurRadius(self: Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Receivers(self: Windows.UI.Composition.ICompositionProjectedShadow) -> Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection: ...
    BlurRadiusMultiplier = property(get_BlurRadiusMultiplier, put_BlurRadiusMultiplier)
    Casters = property(get_Casters, None)
    LightSource = property(get_LightSource, put_LightSource)
    MaxBlurRadius = property(get_MaxBlurRadius, put_MaxBlurRadius)
    MinBlurRadius = property(get_MinBlurRadius, put_MinBlurRadius)
    Receivers = property(get_Receivers, None)
class CompositionProjectedShadowCaster(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionProjectedShadowCaster
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowCaster'
    @winrt_mixinmethod
    def get_Brush(self: Windows.UI.Composition.ICompositionProjectedShadowCaster) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Brush(self: Windows.UI.Composition.ICompositionProjectedShadowCaster, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_CastingVisual(self: Windows.UI.Composition.ICompositionProjectedShadowCaster) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CastingVisual(self: Windows.UI.Composition.ICompositionProjectedShadowCaster, value: Windows.UI.Composition.Visual) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    CastingVisual = property(get_CastingVisual, put_CastingVisual)
class CompositionProjectedShadowCasterCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowCasterCollection'
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection) -> Int32: ...
    @winrt_mixinmethod
    def InsertAbove(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster, reference: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertAtBottom(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertAtTop(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertBelow(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster, reference: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, caster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.ICompositionProjectedShadowCasterCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.CompositionProjectedShadowCaster]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.CompositionProjectedShadowCaster]: ...
    @winrt_classmethod
    def get_MaxRespectedCasters(cls: Windows.UI.Composition.ICompositionProjectedShadowCasterCollectionStatics) -> Int32: ...
    Count = property(get_Count, None)
    MaxRespectedCasters = property(get_MaxRespectedCasters, None)
class CompositionProjectedShadowReceiver(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionProjectedShadowReceiver
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowReceiver'
    @winrt_mixinmethod
    def get_ReceivingVisual(self: Windows.UI.Composition.ICompositionProjectedShadowReceiver) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_ReceivingVisual(self: Windows.UI.Composition.ICompositionProjectedShadowReceiver, value: Windows.UI.Composition.Visual) -> Void: ...
    ReceivingVisual = property(get_ReceivingVisual, put_ReceivingVisual)
class CompositionProjectedShadowReceiverUnorderedCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection'
    @winrt_mixinmethod
    def Add(self: Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection, value: Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection) -> Int32: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection, value: Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.CompositionProjectedShadowReceiver]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.CompositionProjectedShadowReceiver]: ...
    Count = property(get_Count, None)
class CompositionPropertySet(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionPropertySet
    _classid_ = 'Windows.UI.Composition.CompositionPropertySet'
    @winrt_mixinmethod
    def InsertColor(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def InsertMatrix3x2(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def InsertMatrix4x4(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def InsertQuaternion(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def InsertScalar(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertVector2(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def InsertVector3(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def InsertVector4(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def TryGetColor(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.UI.Color_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetMatrix3x2(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Matrix3x2_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetMatrix4x4(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetQuaternion(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Quaternion_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetScalar(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Single)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector2(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector2_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector3(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector4(self: Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector4_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def InsertBoolean(self: Windows.UI.Composition.ICompositionPropertySet2, propertyName: WinRT_String, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryGetBoolean(self: Windows.UI.Composition.ICompositionPropertySet2, propertyName: WinRT_String, value: POINTER(Boolean)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
class CompositionRadialGradientBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionGradientBrush
    default_interface: Windows.UI.Composition.ICompositionRadialGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionRadialGradientBrush'
    @winrt_mixinmethod
    def get_EllipseCenter(self: Windows.UI.Composition.ICompositionRadialGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EllipseCenter(self: Windows.UI.Composition.ICompositionRadialGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_EllipseRadius(self: Windows.UI.Composition.ICompositionRadialGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EllipseRadius(self: Windows.UI.Composition.ICompositionRadialGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_GradientOriginOffset(self: Windows.UI.Composition.ICompositionRadialGradientBrush) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_GradientOriginOffset(self: Windows.UI.Composition.ICompositionRadialGradientBrush, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    EllipseCenter = property(get_EllipseCenter, put_EllipseCenter)
    EllipseRadius = property(get_EllipseRadius, put_EllipseRadius)
    GradientOriginOffset = property(get_GradientOriginOffset, put_GradientOriginOffset)
class CompositionRectangleGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionGeometry
    default_interface: Windows.UI.Composition.ICompositionRectangleGeometry
    _classid_ = 'Windows.UI.Composition.CompositionRectangleGeometry'
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionRectangleGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionRectangleGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.ICompositionRectangleGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Composition.ICompositionRectangleGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class CompositionRoundedRectangleGeometry(ComPtr):
    extends: Windows.UI.Composition.CompositionGeometry
    default_interface: Windows.UI.Composition.ICompositionRoundedRectangleGeometry
    _classid_ = 'Windows.UI.Composition.CompositionRoundedRectangleGeometry'
    @winrt_mixinmethod
    def get_CornerRadius(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CornerRadius(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    CornerRadius = property(get_CornerRadius, put_CornerRadius)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class CompositionScopedBatch(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionScopedBatch
    _classid_ = 'Windows.UI.Composition.CompositionScopedBatch'
    @winrt_mixinmethod
    def get_IsActive(self: Windows.UI.Composition.ICompositionScopedBatch) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEnded(self: Windows.UI.Composition.ICompositionScopedBatch) -> Boolean: ...
    @winrt_mixinmethod
    def End(self: Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def Suspend(self: Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.UI.Composition.ICompositionScopedBatch, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.UI.Composition.ICompositionScopedBatch, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class CompositionShadow(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionShadow
    _classid_ = 'Windows.UI.Composition.CompositionShadow'
class CompositionShape(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionShape
    _classid_ = 'Windows.UI.Composition.CompositionShape'
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Composition.ICompositionShape) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Composition.ICompositionShape, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionShape) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionShape, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.ICompositionShape) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.ICompositionShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionShape) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.ICompositionShape) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.ICompositionShape, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Composition.ICompositionShape) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Composition.ICompositionShape, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class CompositionShapeCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape]
    _classid_ = 'Windows.UI.Composition.CompositionShapeCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], index: UInt32) -> Windows.UI.Composition.CompositionShape: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Composition.CompositionShape]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], value: Windows.UI.Composition.CompositionShape, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], index: UInt32, value: Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], index: UInt32, value: Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], value: Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], startIndex: UInt32, items: POINTER(Windows.UI.Composition.CompositionShape)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.CompositionShape], items: POINTER(Windows.UI.Composition.CompositionShape)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.CompositionShape]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.CompositionShape]: ...
    Size = property(get_Size, None)
class CompositionSpriteShape(ComPtr):
    extends: Windows.UI.Composition.CompositionShape
    default_interface: Windows.UI.Composition.ICompositionSpriteShape
    _classid_ = 'Windows.UI.Composition.CompositionSpriteShape'
    @winrt_mixinmethod
    def get_FillBrush(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_FillBrush(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Geometry(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionGeometry: ...
    @winrt_mixinmethod
    def put_Geometry(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_IsStrokeNonScaling(self: Windows.UI.Composition.ICompositionSpriteShape) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStrokeNonScaling(self: Windows.UI.Composition.ICompositionSpriteShape, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeBrush(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_StrokeBrush(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashArray(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionStrokeDashArray: ...
    @winrt_mixinmethod
    def get_StrokeDashCap(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeDashCap(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashOffset(self: Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeDashOffset(self: Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeEndCap(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeEndCap(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeLineJoin(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionStrokeLineJoin: ...
    @winrt_mixinmethod
    def put_StrokeLineJoin(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionStrokeLineJoin) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeMiterLimit(self: Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeMiterLimit(self: Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeStartCap(self: Windows.UI.Composition.ICompositionSpriteShape) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeStartCap(self: Windows.UI.Composition.ICompositionSpriteShape, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    FillBrush = property(get_FillBrush, put_FillBrush)
    Geometry = property(get_Geometry, put_Geometry)
    IsStrokeNonScaling = property(get_IsStrokeNonScaling, put_IsStrokeNonScaling)
    StrokeBrush = property(get_StrokeBrush, put_StrokeBrush)
    StrokeDashArray = property(get_StrokeDashArray, None)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndCap = property(get_StrokeEndCap, put_StrokeEndCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartCap = property(get_StrokeStartCap, put_StrokeStartCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
CompositionStretch = Int32
CompositionStretch_None: CompositionStretch = 0
CompositionStretch_Fill: CompositionStretch = 1
CompositionStretch_Uniform: CompositionStretch = 2
CompositionStretch_UniformToFill: CompositionStretch = 3
CompositionStrokeCap = Int32
CompositionStrokeCap_Flat: CompositionStrokeCap = 0
CompositionStrokeCap_Square: CompositionStrokeCap = 1
CompositionStrokeCap_Round: CompositionStrokeCap = 2
CompositionStrokeCap_Triangle: CompositionStrokeCap = 3
class CompositionStrokeDashArray(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.Foundation.Collections.IVector[Single]
    _classid_ = 'Windows.UI.Composition.CompositionStrokeDashArray'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Single], index: UInt32) -> Single: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Single]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Single]) -> Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Single], value: Single, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Single], index: UInt32, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Single], index: UInt32, value: Single) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Single], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Single], value: Single) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Single]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Single]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Single], startIndex: UInt32, items: POINTER(Single)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Single], items: POINTER(Single)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Single]) -> Windows.Foundation.Collections.IIterator[Single]: ...
    Size = property(get_Size, None)
CompositionStrokeLineJoin = Int32
CompositionStrokeLineJoin_Miter: CompositionStrokeLineJoin = 0
CompositionStrokeLineJoin_Bevel: CompositionStrokeLineJoin = 1
CompositionStrokeLineJoin_Round: CompositionStrokeLineJoin = 2
CompositionStrokeLineJoin_MiterOrBevel: CompositionStrokeLineJoin = 3
class CompositionSurfaceBrush(ComPtr):
    extends: Windows.UI.Composition.CompositionBrush
    default_interface: Windows.UI.Composition.ICompositionSurfaceBrush
    _classid_ = 'Windows.UI.Composition.CompositionSurfaceBrush'
    @winrt_mixinmethod
    def get_BitmapInterpolationMode(self: Windows.UI.Composition.ICompositionSurfaceBrush) -> Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_BitmapInterpolationMode(self: Windows.UI.Composition.ICompositionSurfaceBrush, value: Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: Windows.UI.Composition.ICompositionSurfaceBrush) -> Single: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: Windows.UI.Composition.ICompositionSurfaceBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: Windows.UI.Composition.ICompositionSurfaceBrush) -> Windows.UI.Composition.CompositionStretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: Windows.UI.Composition.ICompositionSurfaceBrush, value: Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_mixinmethod
    def get_Surface(self: Windows.UI.Composition.ICompositionSurfaceBrush) -> Windows.UI.Composition.ICompositionSurface: ...
    @winrt_mixinmethod
    def put_Surface(self: Windows.UI.Composition.ICompositionSurfaceBrush, value: Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: Windows.UI.Composition.ICompositionSurfaceBrush) -> Single: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: Windows.UI.Composition.ICompositionSurfaceBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AnchorPoint(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Composition.ICompositionSurfaceBrush2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Composition.ICompositionSurfaceBrush2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_SnapToPixels(self: Windows.UI.Composition.ICompositionSurfaceBrush3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SnapToPixels(self: Windows.UI.Composition.ICompositionSurfaceBrush3, value: Boolean) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Stretch = property(get_Stretch, put_Stretch)
    Surface = property(get_Surface, put_Surface)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    SnapToPixels = property(get_SnapToPixels, put_SnapToPixels)
class CompositionTarget(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionTarget
    _classid_ = 'Windows.UI.Composition.CompositionTarget'
    @winrt_mixinmethod
    def get_Root(self: Windows.UI.Composition.ICompositionTarget) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_Root(self: Windows.UI.Composition.ICompositionTarget, value: Windows.UI.Composition.Visual) -> Void: ...
    Root = property(get_Root, put_Root)
class CompositionTransform(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionTransform
    _classid_ = 'Windows.UI.Composition.CompositionTransform'
class CompositionViewBox(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionViewBox
    _classid_ = 'Windows.UI.Composition.CompositionViewBox'
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: Windows.UI.Composition.ICompositionViewBox) -> Single: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: Windows.UI.Composition.ICompositionViewBox, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ICompositionViewBox) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ICompositionViewBox, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.ICompositionViewBox) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Composition.ICompositionViewBox, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: Windows.UI.Composition.ICompositionViewBox) -> Windows.UI.Composition.CompositionStretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: Windows.UI.Composition.ICompositionViewBox, value: Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: Windows.UI.Composition.ICompositionViewBox) -> Single: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: Windows.UI.Composition.ICompositionViewBox, value: Single) -> Void: ...
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
    Stretch = property(get_Stretch, put_Stretch)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class CompositionVirtualDrawingSurface(ComPtr):
    extends: Windows.UI.Composition.CompositionDrawingSurface
    default_interface: Windows.UI.Composition.ICompositionVirtualDrawingSurface
    _classid_ = 'Windows.UI.Composition.CompositionVirtualDrawingSurface'
    @winrt_mixinmethod
    def Trim(self: Windows.UI.Composition.ICompositionVirtualDrawingSurface, rects: POINTER(Windows.Graphics.RectInt32_head)) -> Void: ...
class CompositionVisualSurface(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.ICompositionVisualSurface
    _classid_ = 'Windows.UI.Composition.CompositionVisualSurface'
    @winrt_mixinmethod
    def get_SourceVisual(self: Windows.UI.Composition.ICompositionVisualSurface) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_SourceVisual(self: Windows.UI.Composition.ICompositionVisualSurface, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_SourceOffset(self: Windows.UI.Composition.ICompositionVisualSurface) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_SourceOffset(self: Windows.UI.Composition.ICompositionVisualSurface, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_SourceSize(self: Windows.UI.Composition.ICompositionVisualSurface) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_SourceSize(self: Windows.UI.Composition.ICompositionVisualSurface, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    SourceVisual = property(get_SourceVisual, put_SourceVisual)
    SourceOffset = property(get_SourceOffset, put_SourceOffset)
    SourceSize = property(get_SourceSize, put_SourceSize)
class Compositor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.ICompositor
    _classid_ = 'Windows.UI.Composition.Compositor'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def CreateColorKeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.ColorKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateColorBrush(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_mixinmethod
    def CreateColorBrushWithColor(self: Windows.UI.Composition.ICompositor, color: Windows.UI.Color) -> Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_mixinmethod
    def CreateContainerVisual(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def CreateCubicBezierEasingFunction(self: Windows.UI.Composition.ICompositor, controlPoint1: Windows.Foundation.Numerics.Vector2, controlPoint2: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_mixinmethod
    def CreateEffectFactory(self: Windows.UI.Composition.ICompositor, graphicsEffect: Windows.Graphics.Effects.IGraphicsEffect) -> Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_mixinmethod
    def CreateEffectFactoryWithProperties(self: Windows.UI.Composition.ICompositor, graphicsEffect: Windows.Graphics.Effects.IGraphicsEffect, animatableProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_mixinmethod
    def CreateExpressionAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def CreateExpressionAnimationWithExpression(self: Windows.UI.Composition.ICompositor, expression: WinRT_String) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def CreateInsetClip(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.InsetClip: ...
    @winrt_mixinmethod
    def CreateInsetClipWithInsets(self: Windows.UI.Composition.ICompositor, leftInset: Single, topInset: Single, rightInset: Single, bottomInset: Single) -> Windows.UI.Composition.InsetClip: ...
    @winrt_mixinmethod
    def CreateLinearEasingFunction(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_mixinmethod
    def CreatePropertySet(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_mixinmethod
    def CreateQuaternionKeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.QuaternionKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateScalarKeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.ScalarKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateScopedBatch(self: Windows.UI.Composition.ICompositor, batchType: Windows.UI.Composition.CompositionBatchTypes) -> Windows.UI.Composition.CompositionScopedBatch: ...
    @winrt_mixinmethod
    def CreateSpriteVisual(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.SpriteVisual: ...
    @winrt_mixinmethod
    def CreateSurfaceBrush(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_mixinmethod
    def CreateSurfaceBrushWithSurface(self: Windows.UI.Composition.ICompositor, surface: Windows.UI.Composition.ICompositionSurface) -> Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_mixinmethod
    def CreateTargetForCurrentView(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.CompositionTarget: ...
    @winrt_mixinmethod
    def CreateVector2KeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.Vector2KeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateVector3KeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.Vector3KeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateVector4KeyFrameAnimation(self: Windows.UI.Composition.ICompositor) -> Windows.UI.Composition.Vector4KeyFrameAnimation: ...
    @winrt_mixinmethod
    def GetCommitBatch(self: Windows.UI.Composition.ICompositor, batchType: Windows.UI.Composition.CompositionBatchTypes) -> Windows.UI.Composition.CompositionCommitBatch: ...
    @winrt_mixinmethod
    def CreateAmbientLight(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.AmbientLight: ...
    @winrt_mixinmethod
    def CreateAnimationGroup(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.CompositionAnimationGroup: ...
    @winrt_mixinmethod
    def CreateBackdropBrush(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateDistantLight(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.DistantLight: ...
    @winrt_mixinmethod
    def CreateDropShadow(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.DropShadow: ...
    @winrt_mixinmethod
    def CreateImplicitAnimationCollection(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_mixinmethod
    def CreateLayerVisual(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.LayerVisual: ...
    @winrt_mixinmethod
    def CreateMaskBrush(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.CompositionMaskBrush: ...
    @winrt_mixinmethod
    def CreateNineGridBrush(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.CompositionNineGridBrush: ...
    @winrt_mixinmethod
    def CreatePointLight(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.PointLight: ...
    @winrt_mixinmethod
    def CreateSpotLight(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.SpotLight: ...
    @winrt_mixinmethod
    def CreateStepEasingFunction(self: Windows.UI.Composition.ICompositor2) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_mixinmethod
    def CreateStepEasingFunctionWithStepCount(self: Windows.UI.Composition.ICompositor2, stepCount: Int32) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_mixinmethod
    def CreateHostBackdropBrush(self: Windows.UI.Composition.ICompositor3) -> Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateColorGradientStop(self: Windows.UI.Composition.ICompositor4) -> Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def CreateColorGradientStopWithOffsetAndColor(self: Windows.UI.Composition.ICompositor4, offset: Single, color: Windows.UI.Color) -> Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def CreateLinearGradientBrush(self: Windows.UI.Composition.ICompositor4) -> Windows.UI.Composition.CompositionLinearGradientBrush: ...
    @winrt_mixinmethod
    def CreateSpringScalarAnimation(self: Windows.UI.Composition.ICompositor4) -> Windows.UI.Composition.SpringScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateSpringVector2Animation(self: Windows.UI.Composition.ICompositor4) -> Windows.UI.Composition.SpringVector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateSpringVector3Animation(self: Windows.UI.Composition.ICompositor4) -> Windows.UI.Composition.SpringVector3NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def get_Comment(self: Windows.UI.Composition.ICompositor5) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Comment(self: Windows.UI.Composition.ICompositor5, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalPlaybackRate(self: Windows.UI.Composition.ICompositor5) -> Single: ...
    @winrt_mixinmethod
    def put_GlobalPlaybackRate(self: Windows.UI.Composition.ICompositor5, value: Single) -> Void: ...
    @winrt_mixinmethod
    def CreateBounceScalarAnimation(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.BounceScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateBounceVector2Animation(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.BounceVector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateBounceVector3Animation(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.BounceVector3NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateContainerShape(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionContainerShape: ...
    @winrt_mixinmethod
    def CreateEllipseGeometry(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionEllipseGeometry: ...
    @winrt_mixinmethod
    def CreateLineGeometry(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionLineGeometry: ...
    @winrt_mixinmethod
    def CreatePathGeometry(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_mixinmethod
    def CreatePathGeometryWithPath(self: Windows.UI.Composition.ICompositor5, path: Windows.UI.Composition.CompositionPath) -> Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_mixinmethod
    def CreatePathKeyFrameAnimation(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.PathKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateRectangleGeometry(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionRectangleGeometry: ...
    @winrt_mixinmethod
    def CreateRoundedRectangleGeometry(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionRoundedRectangleGeometry: ...
    @winrt_mixinmethod
    def CreateShapeVisual(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.ShapeVisual: ...
    @winrt_mixinmethod
    def CreateSpriteShape(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_mixinmethod
    def CreateSpriteShapeWithGeometry(self: Windows.UI.Composition.ICompositor5, geometry: Windows.UI.Composition.CompositionGeometry) -> Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_mixinmethod
    def CreateViewBox(self: Windows.UI.Composition.ICompositor5) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def RequestCommitAsync(self: Windows.UI.Composition.ICompositor5) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateGeometricClip(self: Windows.UI.Composition.ICompositor6) -> Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_mixinmethod
    def CreateGeometricClipWithGeometry(self: Windows.UI.Composition.ICompositor6, geometry: Windows.UI.Composition.CompositionGeometry) -> Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_mixinmethod
    def CreateRedirectVisual(self: Windows.UI.Composition.ICompositor6) -> Windows.UI.Composition.RedirectVisual: ...
    @winrt_mixinmethod
    def CreateRedirectVisualWithSourceVisual(self: Windows.UI.Composition.ICompositor6, source: Windows.UI.Composition.Visual) -> Windows.UI.Composition.RedirectVisual: ...
    @winrt_mixinmethod
    def CreateBooleanKeyFrameAnimation(self: Windows.UI.Composition.ICompositor6) -> Windows.UI.Composition.BooleanKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateProjectedShadowCaster(self: Windows.UI.Composition.ICompositorWithProjectedShadow) -> Windows.UI.Composition.CompositionProjectedShadowCaster: ...
    @winrt_mixinmethod
    def CreateProjectedShadow(self: Windows.UI.Composition.ICompositorWithProjectedShadow) -> Windows.UI.Composition.CompositionProjectedShadow: ...
    @winrt_mixinmethod
    def CreateProjectedShadowReceiver(self: Windows.UI.Composition.ICompositorWithProjectedShadow) -> Windows.UI.Composition.CompositionProjectedShadowReceiver: ...
    @winrt_mixinmethod
    def CreateRadialGradientBrush(self: Windows.UI.Composition.ICompositorWithRadialGradient) -> Windows.UI.Composition.CompositionRadialGradientBrush: ...
    @winrt_mixinmethod
    def CreateVisualSurface(self: Windows.UI.Composition.ICompositorWithVisualSurface) -> Windows.UI.Composition.CompositionVisualSurface: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Composition.ICompositor7) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def CreateAnimationPropertyInfo(self: Windows.UI.Composition.ICompositor7) -> Windows.UI.Composition.AnimationPropertyInfo: ...
    @winrt_mixinmethod
    def CreateRectangleClip(self: Windows.UI.Composition.ICompositor7) -> Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def CreateRectangleClipWithSides(self: Windows.UI.Composition.ICompositor7, left: Single, top: Single, right: Single, bottom: Single) -> Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def CreateRectangleClipWithSidesAndRadius(self: Windows.UI.Composition.ICompositor7, left: Single, top: Single, right: Single, bottom: Single, topLeftRadius: Windows.Foundation.Numerics.Vector2, topRightRadius: Windows.Foundation.Numerics.Vector2, bottomRightRadius: Windows.Foundation.Numerics.Vector2, bottomLeftRadius: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def TryCreateBlurredWallpaperBackdropBrush(self: Windows.UI.Composition.ICompositorWithBlurredWallpaperBackdropBrush) -> Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateAnimationController(self: Windows.UI.Composition.ICompositor8) -> Windows.UI.Composition.AnimationController: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def get_MaxGlobalPlaybackRate(cls: Windows.UI.Composition.ICompositorStatics) -> Single: ...
    @winrt_classmethod
    def get_MinGlobalPlaybackRate(cls: Windows.UI.Composition.ICompositorStatics) -> Single: ...
    Comment = property(get_Comment, put_Comment)
    GlobalPlaybackRate = property(get_GlobalPlaybackRate, put_GlobalPlaybackRate)
    DispatcherQueue = property(get_DispatcherQueue, None)
    MaxGlobalPlaybackRate = property(get_MaxGlobalPlaybackRate, None)
    MinGlobalPlaybackRate = property(get_MinGlobalPlaybackRate, None)
class ContainerVisual(ComPtr):
    extends: Windows.UI.Composition.Visual
    default_interface: Windows.UI.Composition.IContainerVisual
    _classid_ = 'Windows.UI.Composition.ContainerVisual'
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Composition.IContainerVisual) -> Windows.UI.Composition.VisualCollection: ...
    Children = property(get_Children, None)
class CubicBezierEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.ICubicBezierEasingFunction
    _classid_ = 'Windows.UI.Composition.CubicBezierEasingFunction'
    @winrt_mixinmethod
    def get_ControlPoint1(self: Windows.UI.Composition.ICubicBezierEasingFunction) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_ControlPoint2(self: Windows.UI.Composition.ICubicBezierEasingFunction) -> Windows.Foundation.Numerics.Vector2: ...
    ControlPoint1 = property(get_ControlPoint1, None)
    ControlPoint2 = property(get_ControlPoint2, None)
class DelegatedInkTrailVisual(ComPtr):
    extends: Windows.UI.Composition.Visual
    default_interface: Windows.UI.Composition.IDelegatedInkTrailVisual
    _classid_ = 'Windows.UI.Composition.DelegatedInkTrailVisual'
    @winrt_mixinmethod
    def AddTrailPoints(self: Windows.UI.Composition.IDelegatedInkTrailVisual, inkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head)) -> UInt32: ...
    @winrt_mixinmethod
    def AddTrailPointsWithPrediction(self: Windows.UI.Composition.IDelegatedInkTrailVisual, inkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head), predictedInkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head)) -> UInt32: ...
    @winrt_mixinmethod
    def RemoveTrailPoints(self: Windows.UI.Composition.IDelegatedInkTrailVisual, generationId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def StartNewTrail(self: Windows.UI.Composition.IDelegatedInkTrailVisual, color: Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.IDelegatedInkTrailVisualStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.DelegatedInkTrailVisual: ...
    @winrt_classmethod
    def CreateForSwapChain(cls: Windows.UI.Composition.IDelegatedInkTrailVisualStatics, compositor: Windows.UI.Composition.Compositor, swapChain: Windows.UI.Composition.ICompositionSurface) -> Windows.UI.Composition.DelegatedInkTrailVisual: ...
class DistantLight(ComPtr):
    extends: Windows.UI.Composition.CompositionLight
    default_interface: Windows.UI.Composition.IDistantLight
    _classid_ = 'Windows.UI.Composition.DistantLight'
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.IDistantLight) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.IDistantLight, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: Windows.UI.Composition.IDistantLight) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: Windows.UI.Composition.IDistantLight, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Composition.IDistantLight) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Direction(self: Windows.UI.Composition.IDistantLight, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: Windows.UI.Composition.IDistantLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: Windows.UI.Composition.IDistantLight2, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    Intensity = property(get_Intensity, put_Intensity)
class DropShadow(ComPtr):
    extends: Windows.UI.Composition.CompositionShadow
    default_interface: Windows.UI.Composition.IDropShadow
    _classid_ = 'Windows.UI.Composition.DropShadow'
    @winrt_mixinmethod
    def get_BlurRadius(self: Windows.UI.Composition.IDropShadow) -> Single: ...
    @winrt_mixinmethod
    def put_BlurRadius(self: Windows.UI.Composition.IDropShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.IDropShadow) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.IDropShadow, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Mask(self: Windows.UI.Composition.IDropShadow) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Mask(self: Windows.UI.Composition.IDropShadow, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.IDropShadow) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.IDropShadow, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: Windows.UI.Composition.IDropShadow) -> Single: ...
    @winrt_mixinmethod
    def put_Opacity(self: Windows.UI.Composition.IDropShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePolicy(self: Windows.UI.Composition.IDropShadow2) -> Windows.UI.Composition.CompositionDropShadowSourcePolicy: ...
    @winrt_mixinmethod
    def put_SourcePolicy(self: Windows.UI.Composition.IDropShadow2, value: Windows.UI.Composition.CompositionDropShadowSourcePolicy) -> Void: ...
    BlurRadius = property(get_BlurRadius, put_BlurRadius)
    Color = property(get_Color, put_Color)
    Mask = property(get_Mask, put_Mask)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    SourcePolicy = property(get_SourcePolicy, put_SourcePolicy)
class ElasticEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IElasticEasingFunction
    _classid_ = 'Windows.UI.Composition.ElasticEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.IElasticEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Oscillations(self: Windows.UI.Composition.IElasticEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def get_Springiness(self: Windows.UI.Composition.IElasticEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Oscillations = property(get_Oscillations, None)
    Springiness = property(get_Springiness, None)
class ExponentialEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IExponentialEasingFunction
    _classid_ = 'Windows.UI.Composition.ExponentialEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.IExponentialEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Exponent(self: Windows.UI.Composition.IExponentialEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Exponent = property(get_Exponent, None)
class ExpressionAnimation(ComPtr):
    extends: Windows.UI.Composition.CompositionAnimation
    default_interface: Windows.UI.Composition.IExpressionAnimation
    _classid_ = 'Windows.UI.Composition.ExpressionAnimation'
    @winrt_mixinmethod
    def get_Expression(self: Windows.UI.Composition.IExpressionAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Expression(self: Windows.UI.Composition.IExpressionAnimation, value: WinRT_String) -> Void: ...
    Expression = property(get_Expression, put_Expression)
class IAmbientLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAmbientLight'
    _iid_ = Guid('{a48130a1-b7c4-46f7-b9bf-daf43a44e6ee}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class IAmbientLight2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAmbientLight2'
    _iid_ = Guid('{3b64a6bf-5f97-4c94-86e5-042dd386b27d}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IAnimationController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationController'
    _iid_ = Guid('{c934efd2-0722-4f5f-a4e2-9510f3d43bf7}')
    @winrt_commethod(6)
    def get_PlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def put_PlaybackRate(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Single: ...
    @winrt_commethod(9)
    def put_Progress(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_ProgressBehavior(self) -> Windows.UI.Composition.AnimationControllerProgressBehavior: ...
    @winrt_commethod(11)
    def put_ProgressBehavior(self, value: Windows.UI.Composition.AnimationControllerProgressBehavior) -> Void: ...
    @winrt_commethod(12)
    def Pause(self) -> Void: ...
    @winrt_commethod(13)
    def Resume(self) -> Void: ...
    PlaybackRate = property(get_PlaybackRate, put_PlaybackRate)
    Progress = property(get_Progress, put_Progress)
    ProgressBehavior = property(get_ProgressBehavior, put_ProgressBehavior)
class IAnimationControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationControllerStatics'
    _iid_ = Guid('{e71164df-651b-4800-b9e5-6a3bcfed3365}')
    @winrt_commethod(6)
    def get_MaxPlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def get_MinPlaybackRate(self) -> Single: ...
    MaxPlaybackRate = property(get_MaxPlaybackRate, None)
    MinPlaybackRate = property(get_MinPlaybackRate, None)
class IAnimationObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationObject'
    _iid_ = Guid('{e7141e0a-04b8-4fc5-a4dc-195392e57807}')
    @winrt_commethod(6)
    def PopulatePropertyInfo(self, propertyName: WinRT_String, propertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IAnimationPropertyInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationPropertyInfo'
    _iid_ = Guid('{f4716f05-ed77-4e3c-b328-5c3985b3738f}')
    @winrt_commethod(6)
    def get_AccessMode(self) -> Windows.UI.Composition.AnimationPropertyAccessMode: ...
    @winrt_commethod(7)
    def put_AccessMode(self, value: Windows.UI.Composition.AnimationPropertyAccessMode) -> Void: ...
    AccessMode = property(get_AccessMode, put_AccessMode)
class IAnimationPropertyInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationPropertyInfo2'
    _iid_ = Guid('{591720b4-7472-5218-8b39-dffe615ae6da}')
    @winrt_commethod(6)
    def GetResolvedCompositionObject(self) -> Windows.UI.Composition.CompositionObject: ...
    @winrt_commethod(7)
    def GetResolvedCompositionObjectProperty(self) -> WinRT_String: ...
class IBackEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBackEasingFunction'
    _iid_ = Guid('{b8560da4-5e3c-545d-b263-7987a2bd27cb}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Amplitude(self) -> Single: ...
    Mode = property(get_Mode, None)
    Amplitude = property(get_Amplitude, None)
class IBooleanKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBooleanKeyFrameAnimation'
    _iid_ = Guid('{95e23a08-d1f4-4972-9770-3efe68d82e14}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Boolean) -> Void: ...
class IBounceEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceEasingFunction'
    _iid_ = Guid('{e7fdb44b-aad5-5174-9421-eef8b75a6a43}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Bounces(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Bounciness(self) -> Single: ...
    Mode = property(get_Mode, None)
    Bounces = property(get_Bounces, None)
    Bounciness = property(get_Bounciness, None)
class IBounceScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceScalarNaturalMotionAnimation'
    _iid_ = Guid('{baa30dcc-a633-4618-9b06-7f7c72c87cff}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class IBounceVector2NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceVector2NaturalMotionAnimation'
    _iid_ = Guid('{da344196-2154-4b3c-88aa-47361204eccd}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class IBounceVector3NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceVector3NaturalMotionAnimation'
    _iid_ = Guid('{47dabc31-10d3-4518-86f1-09caf742d113}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class ICircleEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICircleEasingFunction'
    _iid_ = Guid('{1e07222a-6f82-5a28-8748-2e92fc46ee2b}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class IColorKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IColorKeyFrameAnimation'
    _iid_ = Guid('{93adb5e9-8e05-4593-84a3-dca152781e56}')
    @winrt_commethod(6)
    def get_InterpolationColorSpace(self) -> Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_commethod(7)
    def put_InterpolationColorSpace(self, value: Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_commethod(8)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Windows.UI.Color, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    InterpolationColorSpace = property(get_InterpolationColorSpace, put_InterpolationColorSpace)
class ICompositionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation'
    _iid_ = Guid('{464c4c2c-1caa-4061-9b40-e13fde1503ca}')
    @winrt_commethod(6)
    def ClearAllParameters(self) -> Void: ...
    @winrt_commethod(7)
    def ClearParameter(self, key: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def SetColorParameter(self, key: WinRT_String, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def SetMatrix3x2Parameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(10)
    def SetMatrix4x4Parameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(11)
    def SetQuaternionParameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(12)
    def SetReferenceParameter(self, key: WinRT_String, compositionObject: Windows.UI.Composition.CompositionObject) -> Void: ...
    @winrt_commethod(13)
    def SetScalarParameter(self, key: WinRT_String, value: Single) -> Void: ...
    @winrt_commethod(14)
    def SetVector2Parameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(15)
    def SetVector3Parameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def SetVector4Parameter(self, key: WinRT_String, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
class ICompositionAnimation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation2'
    _iid_ = Guid('{369b603e-a80f-4948-93e3-ed23fb38c6cb}')
    @winrt_commethod(6)
    def SetBooleanParameter(self, key: WinRT_String, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Target(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Target(self, value: WinRT_String) -> Void: ...
    Target = property(get_Target, put_Target)
class ICompositionAnimation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation3'
    _iid_ = Guid('{d51e030d-7da4-4bd7-bc2d-f4517529f43a}')
    @winrt_commethod(6)
    def get_InitialValueExpressions(self) -> Windows.UI.Composition.InitialValueExpressionCollection: ...
    InitialValueExpressions = property(get_InitialValueExpressions, None)
class ICompositionAnimation4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation4'
    _iid_ = Guid('{770137be-76bc-4e23-bfed-fe9cc20f6ec9}')
    @winrt_commethod(6)
    def SetExpressionReferenceParameter(self, parameterName: WinRT_String, source: Windows.UI.Composition.IAnimationObject) -> Void: ...
class ICompositionAnimationBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationBase'
    _iid_ = Guid('{1c2c2999-e818-48d3-a6dd-d78c82f8ace9}')
class ICompositionAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationFactory'
    _iid_ = Guid('{10f6c4fb-6e51-4c25-bbd3-586a9bec3ef4}')
class ICompositionAnimationGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationGroup'
    _iid_ = Guid('{5e7cc90c-cd14-4e07-8a55-c72527aabdac}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, value: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, value: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionBackdropBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBackdropBrush'
    _iid_ = Guid('{c5acae58-3898-499e-8d7f-224e91286a5d}')
class ICompositionBatchCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBatchCompletedEventArgs'
    _iid_ = Guid('{0d00dad0-9464-450a-a562-2e2698b0a812}')
class ICompositionBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBrush'
    _iid_ = Guid('{ab0d7608-30c0-40e9-b568-b60a6bd1fb46}')
class ICompositionBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBrushFactory'
    _iid_ = Guid('{da53fb4c-4650-47c4-ad76-765379607ed6}')
class ICompositionCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCapabilities'
    _iid_ = Guid('{8253353e-b517-48bc-b1e8-4b3561a2e181}')
    @winrt_commethod(6)
    def AreEffectsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def AreEffectsFast(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.CompositionCapabilities, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICompositionCapabilitiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCapabilitiesStatics'
    _iid_ = Guid('{f7b7a86e-6416-49e5-8ddf-afe949e20562}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Composition.CompositionCapabilities: ...
class ICompositionClip(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClip'
    _iid_ = Guid('{1ccd2a52-cfc7-4ace-9983-146bb8eb6a3c}')
class ICompositionClip2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClip2'
    _iid_ = Guid('{5893e069-3516-40e1-89e0-5ba924927235}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(17)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(18)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(19)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionClipFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClipFactory'
    _iid_ = Guid('{b9484caf-20c7-4aed-ac4a-9c78ba1302cf}')
class ICompositionColorBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorBrush'
    _iid_ = Guid('{2b264c5e-bf35-4831-8642-cf70c20fff2f}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class ICompositionColorGradientStop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorGradientStop'
    _iid_ = Guid('{6f00ca92-c801-4e41-9a8f-a53e20f57778}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Single: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class ICompositionColorGradientStopCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorGradientStopCollection'
    _iid_ = Guid('{9f1d20ec-7b04-4b1d-90bc-9fa32c0cfd26}')
class ICompositionCommitBatch(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCommitBatch'
    _iid_ = Guid('{0d00dad0-ca07-4400-8c8e-cb5db08559cc}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnded(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class ICompositionContainerShape(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionContainerShape'
    _iid_ = Guid('{4f5e859b-2e5b-44a8-982c-aa0f69c16059}')
    @winrt_commethod(6)
    def get_Shapes(self) -> Windows.UI.Composition.CompositionShapeCollection: ...
    Shapes = property(get_Shapes, None)
class ICompositionDrawingSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurface'
    _iid_ = Guid('{a166c300-fad0-4d11-9e67-e433162ff49e}')
    @winrt_commethod(6)
    def get_AlphaMode(self) -> Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_commethod(7)
    def get_PixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(8)
    def get_Size(self) -> Windows.Foundation.Size: ...
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class ICompositionDrawingSurface2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurface2'
    _iid_ = Guid('{fad0e88b-e354-44e8-8e3d-c4880d5a213f}')
    @winrt_commethod(6)
    def get_SizeInt32(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(7)
    def Resize(self, sizePixels: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(8)
    def Scroll(self, offset: Windows.Graphics.PointInt32) -> Void: ...
    @winrt_commethod(9)
    def ScrollRect(self, offset: Windows.Graphics.PointInt32, scrollRect: Windows.Graphics.RectInt32) -> Void: ...
    @winrt_commethod(10)
    def ScrollWithClip(self, offset: Windows.Graphics.PointInt32, clipRect: Windows.Graphics.RectInt32) -> Void: ...
    @winrt_commethod(11)
    def ScrollRectWithClip(self, offset: Windows.Graphics.PointInt32, clipRect: Windows.Graphics.RectInt32, scrollRect: Windows.Graphics.RectInt32) -> Void: ...
    SizeInt32 = property(get_SizeInt32, None)
class ICompositionDrawingSurfaceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurfaceFactory'
    _iid_ = Guid('{9497b00a-312d-46b9-9db3-412fd79464c8}')
class ICompositionEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunction'
    _iid_ = Guid('{5145e356-bf79-4ea8-8cc2-6b5b472e6c9a}')
class ICompositionEasingFunctionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunctionFactory'
    _iid_ = Guid('{60840774-3da0-4949-8200-7206c00190a0}')
class ICompositionEasingFunctionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunctionStatics'
    _iid_ = Guid('{17a766b6-2936-53ea-b5af-c642f4a61083}')
    @winrt_commethod(6)
    def CreateCubicBezierEasingFunction(self, owner: Windows.UI.Composition.Compositor, controlPoint1: Windows.Foundation.Numerics.Vector2, controlPoint2: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_commethod(7)
    def CreateLinearEasingFunction(self, owner: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_commethod(8)
    def CreateStepEasingFunction(self, owner: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(9)
    def CreateStepEasingFunctionWithStepCount(self, owner: Windows.UI.Composition.Compositor, stepCount: Int32) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(10)
    def CreateBackEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, amplitude: Single) -> Windows.UI.Composition.BackEasingFunction: ...
    @winrt_commethod(11)
    def CreateBounceEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, bounces: Int32, bounciness: Single) -> Windows.UI.Composition.BounceEasingFunction: ...
    @winrt_commethod(12)
    def CreateCircleEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode) -> Windows.UI.Composition.CircleEasingFunction: ...
    @winrt_commethod(13)
    def CreateElasticEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, oscillations: Int32, springiness: Single) -> Windows.UI.Composition.ElasticEasingFunction: ...
    @winrt_commethod(14)
    def CreateExponentialEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, exponent: Single) -> Windows.UI.Composition.ExponentialEasingFunction: ...
    @winrt_commethod(15)
    def CreatePowerEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode, power: Single) -> Windows.UI.Composition.PowerEasingFunction: ...
    @winrt_commethod(16)
    def CreateSineEasingFunction(self, owner: Windows.UI.Composition.Compositor, mode: Windows.UI.Composition.CompositionEasingFunctionMode) -> Windows.UI.Composition.SineEasingFunction: ...
class ICompositionEffectBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectBrush'
    _iid_ = Guid('{bf7f795e-83cc-44bf-a447-3e3c071789ec}')
    @winrt_commethod(6)
    def GetSourceParameter(self, name: WinRT_String) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def SetSourceParameter(self, name: WinRT_String, source: Windows.UI.Composition.CompositionBrush) -> Void: ...
class ICompositionEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectFactory'
    _iid_ = Guid('{be5624af-ba7e-4510-9850-41c0b4ff74df}')
    @winrt_commethod(6)
    def CreateBrush(self) -> Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_LoadStatus(self) -> Windows.UI.Composition.CompositionEffectFactoryLoadStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LoadStatus = property(get_LoadStatus, None)
class ICompositionEffectSourceParameter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectSourceParameter'
    _iid_ = Guid('{858ab13a-3292-4e4e-b3bb-2b6c6544a6ee}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class ICompositionEffectSourceParameterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectSourceParameterFactory'
    _iid_ = Guid('{b3d9f276-aba3-4724-acf3-d0397464db1c}')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String) -> Windows.UI.Composition.CompositionEffectSourceParameter: ...
class ICompositionEllipseGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEllipseGeometry'
    _iid_ = Guid('{4801f884-f6ad-4b93-afa9-897b64e57b1f}')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Center(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Radius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Radius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class ICompositionGeometricClip(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometricClip'
    _iid_ = Guid('{c840b581-81c9-4444-a2c1-ccaece3a50e5}')
    @winrt_commethod(6)
    def get_Geometry(self) -> Windows.UI.Composition.CompositionGeometry: ...
    @winrt_commethod(7)
    def put_Geometry(self, value: Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_commethod(8)
    def get_ViewBox(self) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(9)
    def put_ViewBox(self, value: Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Geometry = property(get_Geometry, put_Geometry)
    ViewBox = property(get_ViewBox, put_ViewBox)
class ICompositionGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometry'
    _iid_ = Guid('{e985217c-6a17-4207-abd8-5fd3dd612a9d}')
    @winrt_commethod(6)
    def get_TrimEnd(self) -> Single: ...
    @winrt_commethod(7)
    def put_TrimEnd(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_TrimOffset(self) -> Single: ...
    @winrt_commethod(9)
    def put_TrimOffset(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TrimStart(self) -> Single: ...
    @winrt_commethod(11)
    def put_TrimStart(self, value: Single) -> Void: ...
    TrimEnd = property(get_TrimEnd, put_TrimEnd)
    TrimOffset = property(get_TrimOffset, put_TrimOffset)
    TrimStart = property(get_TrimStart, put_TrimStart)
class ICompositionGeometryFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometryFactory'
    _iid_ = Guid('{bffebfe1-8c25-480b-9f56-fed6b288055d}')
class ICompositionGradientBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrush'
    _iid_ = Guid('{1d9709e0-ffc6-4c0e-a9ab-34144d4c9098}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_ColorStops(self) -> Windows.UI.Composition.CompositionColorGradientStopCollection: ...
    @winrt_commethod(11)
    def get_ExtendMode(self) -> Windows.UI.Composition.CompositionGradientExtendMode: ...
    @winrt_commethod(12)
    def put_ExtendMode(self, value: Windows.UI.Composition.CompositionGradientExtendMode) -> Void: ...
    @winrt_commethod(13)
    def get_InterpolationSpace(self) -> Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_commethod(14)
    def put_InterpolationSpace(self, value: Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_commethod(15)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(16)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(17)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(18)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(19)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(20)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(21)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(22)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(23)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(24)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    ColorStops = property(get_ColorStops, None)
    ExtendMode = property(get_ExtendMode, put_ExtendMode)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionGradientBrush2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrush2'
    _iid_ = Guid('{899dd5a1-b4c7-4b33-a1b6-264addc26d10}')
    @winrt_commethod(6)
    def get_MappingMode(self) -> Windows.UI.Composition.CompositionMappingMode: ...
    @winrt_commethod(7)
    def put_MappingMode(self, value: Windows.UI.Composition.CompositionMappingMode) -> Void: ...
    MappingMode = property(get_MappingMode, put_MappingMode)
class ICompositionGradientBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrushFactory'
    _iid_ = Guid('{56d765d7-f189-48c9-9c8d-94daf1bec010}')
class ICompositionGraphicsDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice'
    _iid_ = Guid('{fb22c6e1-80a2-4667-9936-dbeaf6eefe95}')
    @winrt_commethod(6)
    def CreateDrawingSurface(self, sizePixels: Windows.Foundation.Size, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_commethod(7)
    def add_RenderingDeviceReplaced(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.CompositionGraphicsDevice, Windows.UI.Composition.RenderingDeviceReplacedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_RenderingDeviceReplaced(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICompositionGraphicsDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice2'
    _iid_ = Guid('{0fb8bdf6-c0f0-4bcc-9fb8-084982490d7d}')
    @winrt_commethod(6)
    def CreateDrawingSurface2(self, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_commethod(7)
    def CreateVirtualDrawingSurface(self, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionVirtualDrawingSurface: ...
class ICompositionGraphicsDevice3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice3'
    _iid_ = Guid('{37f67514-d3ef-49d1-b69d-0d8eabeb3626}')
    @winrt_commethod(6)
    def CreateMipmapSurface(self, sizePixels: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode) -> Windows.UI.Composition.CompositionMipmapSurface: ...
    @winrt_commethod(7)
    def Trim(self) -> Void: ...
class ICompositionGraphicsDevice4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice4'
    _iid_ = Guid('{5a73bff9-a97f-4cf5-ba46-98ef358e71b1}')
    @winrt_commethod(6)
    def CaptureAsync(self, captureVisual: Windows.UI.Composition.Visual, size: Windows.Graphics.SizeInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: Windows.Graphics.DirectX.DirectXAlphaMode, sdrBoost: Single) -> Windows.Foundation.IAsyncOperation[Windows.UI.Composition.ICompositionSurface]: ...
class ICompositionLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight'
    _iid_ = Guid('{41a6d7c2-2e5d-4bc1-b09e-8f0a03e3d8d3}')
    @winrt_commethod(6)
    def get_Targets(self) -> Windows.UI.Composition.VisualUnorderedCollection: ...
    Targets = property(get_Targets, None)
class ICompositionLight2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight2'
    _iid_ = Guid('{a7bcda72-f35d-425d-9b98-23f4205f6669}')
    @winrt_commethod(6)
    def get_ExclusionsFromTargets(self) -> Windows.UI.Composition.VisualUnorderedCollection: ...
    ExclusionsFromTargets = property(get_ExclusionsFromTargets, None)
class ICompositionLight3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight3'
    _iid_ = Guid('{4b0b00e4-df07-4959-b7a4-4f7e4233f838}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class ICompositionLightFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLightFactory'
    _iid_ = Guid('{069cf306-da3c-4b44-838a-5e03d51ace55}')
class ICompositionLineGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLineGeometry'
    _iid_ = Guid('{dd7615a4-0c9a-4b67-8dce-440a5bf9cdec}')
    @winrt_commethod(6)
    def get_Start(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Start(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_End(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_End(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Start = property(get_Start, put_Start)
    End = property(get_End, put_End)
class ICompositionLinearGradientBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLinearGradientBrush'
    _iid_ = Guid('{983bc519-a9db-413c-a2d8-2a9056fc525e}')
    @winrt_commethod(6)
    def get_EndPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_EndPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_StartPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_StartPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
class ICompositionMaskBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionMaskBrush'
    _iid_ = Guid('{522cf09e-be6b-4f41-be49-f9226d471b4a}')
    @winrt_commethod(6)
    def get_Mask(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Mask(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(9)
    def put_Source(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    Mask = property(get_Mask, put_Mask)
    Source = property(get_Source, put_Source)
class ICompositionMipmapSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionMipmapSurface'
    _iid_ = Guid('{4863675c-cf4a-4b1c-9ece-c5ec0c2b2fe6}')
    @winrt_commethod(6)
    def get_LevelCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_AlphaMode(self) -> Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_commethod(8)
    def get_PixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def get_SizeInt32(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(10)
    def GetDrawingSurfaceForLevel(self, level: UInt32) -> Windows.UI.Composition.CompositionDrawingSurface: ...
    LevelCount = property(get_LevelCount, None)
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    SizeInt32 = property(get_SizeInt32, None)
class ICompositionNineGridBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionNineGridBrush'
    _iid_ = Guid('{f25154e4-bc8c-4be7-b80f-8685b83c0186}')
    @winrt_commethod(6)
    def get_BottomInset(self) -> Single: ...
    @winrt_commethod(7)
    def put_BottomInset(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_BottomInsetScale(self) -> Single: ...
    @winrt_commethod(9)
    def put_BottomInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_IsCenterHollow(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCenterHollow(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_LeftInset(self) -> Single: ...
    @winrt_commethod(13)
    def put_LeftInset(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_LeftInsetScale(self) -> Single: ...
    @winrt_commethod(15)
    def put_LeftInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_RightInset(self) -> Single: ...
    @winrt_commethod(17)
    def put_RightInset(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_RightInsetScale(self) -> Single: ...
    @winrt_commethod(19)
    def put_RightInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_Source(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(21)
    def put_Source(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(22)
    def get_TopInset(self) -> Single: ...
    @winrt_commethod(23)
    def put_TopInset(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_TopInsetScale(self) -> Single: ...
    @winrt_commethod(25)
    def put_TopInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def SetInsets(self, inset: Single) -> Void: ...
    @winrt_commethod(27)
    def SetInsetsWithValues(self, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    @winrt_commethod(28)
    def SetInsetScales(self, scale: Single) -> Void: ...
    @winrt_commethod(29)
    def SetInsetScalesWithValues(self, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    BottomInsetScale = property(get_BottomInsetScale, put_BottomInsetScale)
    IsCenterHollow = property(get_IsCenterHollow, put_IsCenterHollow)
    LeftInset = property(get_LeftInset, put_LeftInset)
    LeftInsetScale = property(get_LeftInsetScale, put_LeftInsetScale)
    RightInset = property(get_RightInset, put_RightInset)
    RightInsetScale = property(get_RightInsetScale, put_RightInsetScale)
    Source = property(get_Source, put_Source)
    TopInset = property(get_TopInset, put_TopInset)
    TopInsetScale = property(get_TopInsetScale, put_TopInsetScale)
class ICompositionObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject'
    _iid_ = Guid('{bcb4ad45-7609-4550-934f-16002a68fded}')
    @winrt_commethod(6)
    def get_Compositor(self) -> Windows.UI.Composition.Compositor: ...
    @winrt_commethod(7)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(9)
    def StartAnimation(self, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(10)
    def StopAnimation(self, propertyName: WinRT_String) -> Void: ...
    Compositor = property(get_Compositor, None)
    Dispatcher = property(get_Dispatcher, None)
    Properties = property(get_Properties, None)
class ICompositionObject2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject2'
    _iid_ = Guid('{ef874ea1-5cff-4b68-9e30-a1519d08ba03}')
    @winrt_commethod(6)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Comment(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ImplicitAnimations(self) -> Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_commethod(9)
    def put_ImplicitAnimations(self, value: Windows.UI.Composition.ImplicitAnimationCollection) -> Void: ...
    @winrt_commethod(10)
    def StartAnimationGroup(self, value: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(11)
    def StopAnimationGroup(self, value: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    Comment = property(get_Comment, put_Comment)
    ImplicitAnimations = property(get_ImplicitAnimations, put_ImplicitAnimations)
class ICompositionObject3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject3'
    _iid_ = Guid('{4bc27925-dacd-4cf2-98b1-986b76e7ebe6}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICompositionObject4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject4'
    _iid_ = Guid('{0bb3784c-346b-4a7c-966b-7310966553d5}')
    @winrt_commethod(6)
    def TryGetAnimationController(self, propertyName: WinRT_String) -> Windows.UI.Composition.AnimationController: ...
class ICompositionObject5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject5'
    _iid_ = Guid('{1d7f391b-a130-5265-a62b-60b8e668965a}')
    @winrt_commethod(6)
    def StartAnimationWithController(self, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation, animationController: Windows.UI.Composition.AnimationController) -> Void: ...
class ICompositionObjectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObjectFactory'
    _iid_ = Guid('{51205c5e-558a-4f2a-8d39-37bfe1e20ddd}')
class ICompositionObjectStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObjectStatics'
    _iid_ = Guid('{c1ed052f-1ba2-44ba-a904-6a882a0a5adb}')
    @winrt_commethod(6)
    def StartAnimationWithIAnimationObject(self, target: Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, animation: Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(7)
    def StartAnimationGroupWithIAnimationObject(self, target: Windows.UI.Composition.IAnimationObject, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
class ICompositionPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPath'
    _iid_ = Guid('{66da1d5f-2e10-4f22-8a06-0a8151919e60}')
class ICompositionPathFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPathFactory'
    _iid_ = Guid('{9c1e8c6a-0f33-4751-9437-eb3fb9d3ab07}')
    @winrt_commethod(6)
    def Create(self, source: Windows.Graphics.IGeometrySource2D) -> Windows.UI.Composition.CompositionPath: ...
class ICompositionPathGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPathGeometry'
    _iid_ = Guid('{0b6a417e-2c77-4c23-af5e-6304c147bb61}')
    @winrt_commethod(6)
    def get_Path(self) -> Windows.UI.Composition.CompositionPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: Windows.UI.Composition.CompositionPath) -> Void: ...
    Path = property(get_Path, put_Path)
class ICompositionProjectedShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadow'
    _iid_ = Guid('{285b8e72-4328-523f-bcf2-5557c52c3b25}')
    @winrt_commethod(6)
    def get_BlurRadiusMultiplier(self) -> Single: ...
    @winrt_commethod(7)
    def put_BlurRadiusMultiplier(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Casters(self) -> Windows.UI.Composition.CompositionProjectedShadowCasterCollection: ...
    @winrt_commethod(9)
    def get_LightSource(self) -> Windows.UI.Composition.CompositionLight: ...
    @winrt_commethod(10)
    def put_LightSource(self, value: Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_commethod(11)
    def get_MaxBlurRadius(self) -> Single: ...
    @winrt_commethod(12)
    def put_MaxBlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(13)
    def get_MinBlurRadius(self) -> Single: ...
    @winrt_commethod(14)
    def put_MinBlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(15)
    def get_Receivers(self) -> Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection: ...
    BlurRadiusMultiplier = property(get_BlurRadiusMultiplier, put_BlurRadiusMultiplier)
    Casters = property(get_Casters, None)
    LightSource = property(get_LightSource, put_LightSource)
    MaxBlurRadius = property(get_MaxBlurRadius, put_MaxBlurRadius)
    MinBlurRadius = property(get_MinBlurRadius, put_MinBlurRadius)
    Receivers = property(get_Receivers, None)
class ICompositionProjectedShadowCaster(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCaster'
    _iid_ = Guid('{b1d7d426-1e36-5a62-be56-a16112fdd148}')
    @winrt_commethod(6)
    def get_Brush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Brush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_CastingVisual(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CastingVisual(self, value: Windows.UI.Composition.Visual) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    CastingVisual = property(get_CastingVisual, put_CastingVisual)
class ICompositionProjectedShadowCasterCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCasterCollection'
    _iid_ = Guid('{d2525c0c-e07f-58a3-ac91-37f73ee91740}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def InsertAbove(self, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster, reference: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(8)
    def InsertAtBottom(self, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(9)
    def InsertAtTop(self, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(10)
    def InsertBelow(self, newCaster: Windows.UI.Composition.CompositionProjectedShadowCaster, reference: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(11)
    def Remove(self, caster: Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(12)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionProjectedShadowCasterCollectionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCasterCollectionStatics'
    _iid_ = Guid('{56fbb136-e94f-5299-ab5b-6e15e38bd899}')
    @winrt_commethod(6)
    def get_MaxRespectedCasters(self) -> Int32: ...
    MaxRespectedCasters = property(get_MaxRespectedCasters, None)
class ICompositionProjectedShadowReceiver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowReceiver'
    _iid_ = Guid('{1377985a-6a49-536a-9be4-a96a8e5298a9}')
    @winrt_commethod(6)
    def get_ReceivingVisual(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_ReceivingVisual(self, value: Windows.UI.Composition.Visual) -> Void: ...
    ReceivingVisual = property(get_ReceivingVisual, put_ReceivingVisual)
class ICompositionProjectedShadowReceiverUnorderedCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection'
    _iid_ = Guid('{02b3e3b7-27d2-599f-ac4b-ab787cdde6fd}')
    @winrt_commethod(6)
    def Add(self, value: Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_commethod(7)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(8)
    def Remove(self, value: Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionPropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPropertySet'
    _iid_ = Guid('{c9d6d202-5f67-4453-9117-9eadd430d3c2}')
    @winrt_commethod(6)
    def InsertColor(self, propertyName: WinRT_String, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(7)
    def InsertMatrix3x2(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def InsertMatrix4x4(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(9)
    def InsertQuaternion(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(10)
    def InsertScalar(self, propertyName: WinRT_String, value: Single) -> Void: ...
    @winrt_commethod(11)
    def InsertVector2(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def InsertVector3(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(13)
    def InsertVector4(self, propertyName: WinRT_String, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(14)
    def TryGetColor(self, propertyName: WinRT_String, value: POINTER(Windows.UI.Color_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(15)
    def TryGetMatrix3x2(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Matrix3x2_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(16)
    def TryGetMatrix4x4(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(17)
    def TryGetQuaternion(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Quaternion_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(18)
    def TryGetScalar(self, propertyName: WinRT_String, value: POINTER(Single)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(19)
    def TryGetVector2(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector2_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(20)
    def TryGetVector3(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(21)
    def TryGetVector4(self, propertyName: WinRT_String, value: POINTER(Windows.Foundation.Numerics.Vector4_head)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
class ICompositionPropertySet2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPropertySet2'
    _iid_ = Guid('{de80731e-a211-4455-8880-7d0f3f6a44fd}')
    @winrt_commethod(6)
    def InsertBoolean(self, propertyName: WinRT_String, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def TryGetBoolean(self, propertyName: WinRT_String, value: POINTER(Boolean)) -> Windows.UI.Composition.CompositionGetValueStatus: ...
class ICompositionRadialGradientBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRadialGradientBrush'
    _iid_ = Guid('{3d3b50c5-e3fa-4ce2-b9fc-3ee12561788f}')
    @winrt_commethod(6)
    def get_EllipseCenter(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_EllipseCenter(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_EllipseRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_EllipseRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_GradientOriginOffset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_GradientOriginOffset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    EllipseCenter = property(get_EllipseCenter, put_EllipseCenter)
    EllipseRadius = property(get_EllipseRadius, put_EllipseRadius)
    GradientOriginOffset = property(get_GradientOriginOffset, put_GradientOriginOffset)
class ICompositionRectangleGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRectangleGeometry'
    _iid_ = Guid('{0cd51428-5356-4246-aecf-7a0b76975400}')
    @winrt_commethod(6)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Size(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Size(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class ICompositionRoundedRectangleGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRoundedRectangleGeometry'
    _iid_ = Guid('{8770c822-1d50-4b8b-b013-7c9a0e46935f}')
    @winrt_commethod(6)
    def get_CornerRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_CornerRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Size(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    CornerRadius = property(get_CornerRadius, put_CornerRadius)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class ICompositionScopedBatch(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionScopedBatch'
    _iid_ = Guid('{0d00dad0-fb07-46fd-8c72-6280d1a3d1dd}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnded(self) -> Boolean: ...
    @winrt_commethod(8)
    def End(self) -> Void: ...
    @winrt_commethod(9)
    def Resume(self) -> Void: ...
    @winrt_commethod(10)
    def Suspend(self) -> Void: ...
    @winrt_commethod(11)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class ICompositionShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShadow'
    _iid_ = Guid('{329e52e2-4335-49cc-b14a-37782d10f0c4}')
class ICompositionShadowFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShadowFactory'
    _iid_ = Guid('{221f492f-dcba-4b91-999e-1dc217a01530}')
class ICompositionShape(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShape'
    _iid_ = Guid('{b47ce2f7-9a88-42c4-9e87-2e500ca8688c}')
    @winrt_commethod(6)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(11)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(15)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(16)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(17)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionShapeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShapeFactory'
    _iid_ = Guid('{1dfc36d0-b05a-44ef-82b0-12118bcd4cd0}')
class ICompositionSpriteShape(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSpriteShape'
    _iid_ = Guid('{401b61bb-0007-4363-b1f3-6bcc003fb83e}')
    @winrt_commethod(6)
    def get_FillBrush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_FillBrush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_Geometry(self) -> Windows.UI.Composition.CompositionGeometry: ...
    @winrt_commethod(9)
    def put_Geometry(self, value: Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_commethod(10)
    def get_IsStrokeNonScaling(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsStrokeNonScaling(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeBrush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(13)
    def put_StrokeBrush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(14)
    def get_StrokeDashArray(self) -> Windows.UI.Composition.CompositionStrokeDashArray: ...
    @winrt_commethod(15)
    def get_StrokeDashCap(self) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(16)
    def put_StrokeDashCap(self, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(17)
    def get_StrokeDashOffset(self) -> Single: ...
    @winrt_commethod(18)
    def put_StrokeDashOffset(self, value: Single) -> Void: ...
    @winrt_commethod(19)
    def get_StrokeEndCap(self) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(20)
    def put_StrokeEndCap(self, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(21)
    def get_StrokeLineJoin(self) -> Windows.UI.Composition.CompositionStrokeLineJoin: ...
    @winrt_commethod(22)
    def put_StrokeLineJoin(self, value: Windows.UI.Composition.CompositionStrokeLineJoin) -> Void: ...
    @winrt_commethod(23)
    def get_StrokeMiterLimit(self) -> Single: ...
    @winrt_commethod(24)
    def put_StrokeMiterLimit(self, value: Single) -> Void: ...
    @winrt_commethod(25)
    def get_StrokeStartCap(self) -> Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(26)
    def put_StrokeStartCap(self, value: Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(27)
    def get_StrokeThickness(self) -> Single: ...
    @winrt_commethod(28)
    def put_StrokeThickness(self, value: Single) -> Void: ...
    FillBrush = property(get_FillBrush, put_FillBrush)
    Geometry = property(get_Geometry, put_Geometry)
    IsStrokeNonScaling = property(get_IsStrokeNonScaling, put_IsStrokeNonScaling)
    StrokeBrush = property(get_StrokeBrush, put_StrokeBrush)
    StrokeDashArray = property(get_StrokeDashArray, None)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndCap = property(get_StrokeEndCap, put_StrokeEndCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartCap = property(get_StrokeStartCap, put_StrokeStartCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
class ICompositionSupportsSystemBackdrop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSupportsSystemBackdrop'
    _iid_ = Guid('{397dafe4-b6c2-5bb9-951d-f5707de8b7bc}')
    @winrt_commethod(6)
    def get_SystemBackdrop(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_SystemBackdrop(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
class ICompositionSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurface'
    _iid_ = Guid('{1527540d-42c7-47a6-a408-668f79a90dfb}')
class ICompositionSurfaceBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush'
    _iid_ = Guid('{ad016d79-1e4c-4c0d-9c29-83338c87c162}')
    @winrt_commethod(6)
    def get_BitmapInterpolationMode(self) -> Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_commethod(7)
    def put_BitmapInterpolationMode(self, value: Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_commethod(8)
    def get_HorizontalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(9)
    def put_HorizontalAlignmentRatio(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_Stretch(self) -> Windows.UI.Composition.CompositionStretch: ...
    @winrt_commethod(11)
    def put_Stretch(self, value: Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_commethod(12)
    def get_Surface(self) -> Windows.UI.Composition.ICompositionSurface: ...
    @winrt_commethod(13)
    def put_Surface(self, value: Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_commethod(14)
    def get_VerticalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(15)
    def put_VerticalAlignmentRatio(self, value: Single) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Stretch = property(get_Stretch, put_Stretch)
    Surface = property(get_Surface, put_Surface)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class ICompositionSurfaceBrush2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush2'
    _iid_ = Guid('{d27174d5-64f5-4692-9dc7-71b61d7e5880}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(17)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(18)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(19)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionSurfaceBrush3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush3'
    _iid_ = Guid('{550bb289-1fe0-42e5-8195-1eefa87ff08e}')
    @winrt_commethod(6)
    def get_SnapToPixels(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SnapToPixels(self, value: Boolean) -> Void: ...
    SnapToPixels = property(get_SnapToPixels, put_SnapToPixels)
class ICompositionSurfaceFacade(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceFacade'
    _iid_ = Guid('{e01622c8-2332-55c7-8868-a7312c5c229d}')
    @winrt_commethod(6)
    def GetRealSurface(self) -> Windows.UI.Composition.ICompositionSurface: ...
class ICompositionTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTarget'
    _iid_ = Guid('{a1bea8ba-d726-4663-8129-6b5e7927ffa6}')
    @winrt_commethod(6)
    def get_Root(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_Root(self, value: Windows.UI.Composition.Visual) -> Void: ...
    Root = property(get_Root, put_Root)
class ICompositionTargetFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTargetFactory'
    _iid_ = Guid('{93cd9d2b-8516-4b14-a8ce-f49e2119ec42}')
class ICompositionTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTransform'
    _iid_ = Guid('{7cd54529-fbed-4112-abc5-185906dd927c}')
class ICompositionTransformFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTransformFactory'
    _iid_ = Guid('{aaaeca26-c149-517a-8f72-6bff7a65ce08}')
class ICompositionViewBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionViewBox'
    _iid_ = Guid('{b440bf07-068f-4537-84c6-4ecbe019e1f4}')
    @winrt_commethod(6)
    def get_HorizontalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_HorizontalAlignmentRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Size(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_Stretch(self) -> Windows.UI.Composition.CompositionStretch: ...
    @winrt_commethod(13)
    def put_Stretch(self, value: Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_commethod(14)
    def get_VerticalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(15)
    def put_VerticalAlignmentRatio(self, value: Single) -> Void: ...
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
    Stretch = property(get_Stretch, put_Stretch)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class ICompositionVirtualDrawingSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVirtualDrawingSurface'
    _iid_ = Guid('{a9c384db-8740-4f94-8b9d-b68521e7863d}')
    @winrt_commethod(6)
    def Trim(self, rects: POINTER(Windows.Graphics.RectInt32_head)) -> Void: ...
class ICompositionVirtualDrawingSurfaceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVirtualDrawingSurfaceFactory'
    _iid_ = Guid('{6766106c-d56b-4a49-b1df-5076a0620768}')
class ICompositionVisualSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVisualSurface'
    _iid_ = Guid('{b224d803-4f6e-4a3f-8cae-3dc1cda74fc6}')
    @winrt_commethod(6)
    def get_SourceVisual(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_SourceVisual(self, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def get_SourceOffset(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_SourceOffset(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_SourceSize(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_SourceSize(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    SourceVisual = property(get_SourceVisual, put_SourceVisual)
    SourceOffset = property(get_SourceOffset, put_SourceOffset)
    SourceSize = property(get_SourceSize, put_SourceSize)
class ICompositor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor'
    _iid_ = Guid('{b403ca50-7f8c-4e83-985f-cc45060036d8}')
    @winrt_commethod(6)
    def CreateColorKeyFrameAnimation(self) -> Windows.UI.Composition.ColorKeyFrameAnimation: ...
    @winrt_commethod(7)
    def CreateColorBrush(self) -> Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_commethod(8)
    def CreateColorBrushWithColor(self, color: Windows.UI.Color) -> Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_commethod(9)
    def CreateContainerVisual(self) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(10)
    def CreateCubicBezierEasingFunction(self, controlPoint1: Windows.Foundation.Numerics.Vector2, controlPoint2: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_commethod(11)
    def CreateEffectFactory(self, graphicsEffect: Windows.Graphics.Effects.IGraphicsEffect) -> Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_commethod(12)
    def CreateEffectFactoryWithProperties(self, graphicsEffect: Windows.Graphics.Effects.IGraphicsEffect, animatableProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_commethod(13)
    def CreateExpressionAnimation(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(14)
    def CreateExpressionAnimationWithExpression(self, expression: WinRT_String) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(15)
    def CreateInsetClip(self) -> Windows.UI.Composition.InsetClip: ...
    @winrt_commethod(16)
    def CreateInsetClipWithInsets(self, leftInset: Single, topInset: Single, rightInset: Single, bottomInset: Single) -> Windows.UI.Composition.InsetClip: ...
    @winrt_commethod(17)
    def CreateLinearEasingFunction(self) -> Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_commethod(18)
    def CreatePropertySet(self) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(19)
    def CreateQuaternionKeyFrameAnimation(self) -> Windows.UI.Composition.QuaternionKeyFrameAnimation: ...
    @winrt_commethod(20)
    def CreateScalarKeyFrameAnimation(self) -> Windows.UI.Composition.ScalarKeyFrameAnimation: ...
    @winrt_commethod(21)
    def CreateScopedBatch(self, batchType: Windows.UI.Composition.CompositionBatchTypes) -> Windows.UI.Composition.CompositionScopedBatch: ...
    @winrt_commethod(22)
    def CreateSpriteVisual(self) -> Windows.UI.Composition.SpriteVisual: ...
    @winrt_commethod(23)
    def CreateSurfaceBrush(self) -> Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_commethod(24)
    def CreateSurfaceBrushWithSurface(self, surface: Windows.UI.Composition.ICompositionSurface) -> Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_commethod(25)
    def CreateTargetForCurrentView(self) -> Windows.UI.Composition.CompositionTarget: ...
    @winrt_commethod(26)
    def CreateVector2KeyFrameAnimation(self) -> Windows.UI.Composition.Vector2KeyFrameAnimation: ...
    @winrt_commethod(27)
    def CreateVector3KeyFrameAnimation(self) -> Windows.UI.Composition.Vector3KeyFrameAnimation: ...
    @winrt_commethod(28)
    def CreateVector4KeyFrameAnimation(self) -> Windows.UI.Composition.Vector4KeyFrameAnimation: ...
    @winrt_commethod(29)
    def GetCommitBatch(self, batchType: Windows.UI.Composition.CompositionBatchTypes) -> Windows.UI.Composition.CompositionCommitBatch: ...
class ICompositor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor2'
    _iid_ = Guid('{735081dc-5e24-45da-a38f-e32cc349a9a0}')
    @winrt_commethod(6)
    def CreateAmbientLight(self) -> Windows.UI.Composition.AmbientLight: ...
    @winrt_commethod(7)
    def CreateAnimationGroup(self) -> Windows.UI.Composition.CompositionAnimationGroup: ...
    @winrt_commethod(8)
    def CreateBackdropBrush(self) -> Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_commethod(9)
    def CreateDistantLight(self) -> Windows.UI.Composition.DistantLight: ...
    @winrt_commethod(10)
    def CreateDropShadow(self) -> Windows.UI.Composition.DropShadow: ...
    @winrt_commethod(11)
    def CreateImplicitAnimationCollection(self) -> Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_commethod(12)
    def CreateLayerVisual(self) -> Windows.UI.Composition.LayerVisual: ...
    @winrt_commethod(13)
    def CreateMaskBrush(self) -> Windows.UI.Composition.CompositionMaskBrush: ...
    @winrt_commethod(14)
    def CreateNineGridBrush(self) -> Windows.UI.Composition.CompositionNineGridBrush: ...
    @winrt_commethod(15)
    def CreatePointLight(self) -> Windows.UI.Composition.PointLight: ...
    @winrt_commethod(16)
    def CreateSpotLight(self) -> Windows.UI.Composition.SpotLight: ...
    @winrt_commethod(17)
    def CreateStepEasingFunction(self) -> Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(18)
    def CreateStepEasingFunctionWithStepCount(self, stepCount: Int32) -> Windows.UI.Composition.StepEasingFunction: ...
class ICompositor3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor3'
    _iid_ = Guid('{c9dd8ef0-6eb1-4e3c-a658-675d9c64d4ab}')
    @winrt_commethod(6)
    def CreateHostBackdropBrush(self) -> Windows.UI.Composition.CompositionBackdropBrush: ...
class ICompositor4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor4'
    _iid_ = Guid('{ae47e78a-7910-4425-a482-a05b758adce9}')
    @winrt_commethod(6)
    def CreateColorGradientStop(self) -> Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_commethod(7)
    def CreateColorGradientStopWithOffsetAndColor(self, offset: Single, color: Windows.UI.Color) -> Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_commethod(8)
    def CreateLinearGradientBrush(self) -> Windows.UI.Composition.CompositionLinearGradientBrush: ...
    @winrt_commethod(9)
    def CreateSpringScalarAnimation(self) -> Windows.UI.Composition.SpringScalarNaturalMotionAnimation: ...
    @winrt_commethod(10)
    def CreateSpringVector2Animation(self) -> Windows.UI.Composition.SpringVector2NaturalMotionAnimation: ...
    @winrt_commethod(11)
    def CreateSpringVector3Animation(self) -> Windows.UI.Composition.SpringVector3NaturalMotionAnimation: ...
class ICompositor5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor5'
    _iid_ = Guid('{48ea31ad-7fcd-4076-a79c-90cc4b852c9b}')
    @winrt_commethod(6)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Comment(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_GlobalPlaybackRate(self) -> Single: ...
    @winrt_commethod(9)
    def put_GlobalPlaybackRate(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def CreateBounceScalarAnimation(self) -> Windows.UI.Composition.BounceScalarNaturalMotionAnimation: ...
    @winrt_commethod(11)
    def CreateBounceVector2Animation(self) -> Windows.UI.Composition.BounceVector2NaturalMotionAnimation: ...
    @winrt_commethod(12)
    def CreateBounceVector3Animation(self) -> Windows.UI.Composition.BounceVector3NaturalMotionAnimation: ...
    @winrt_commethod(13)
    def CreateContainerShape(self) -> Windows.UI.Composition.CompositionContainerShape: ...
    @winrt_commethod(14)
    def CreateEllipseGeometry(self) -> Windows.UI.Composition.CompositionEllipseGeometry: ...
    @winrt_commethod(15)
    def CreateLineGeometry(self) -> Windows.UI.Composition.CompositionLineGeometry: ...
    @winrt_commethod(16)
    def CreatePathGeometry(self) -> Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_commethod(17)
    def CreatePathGeometryWithPath(self, path: Windows.UI.Composition.CompositionPath) -> Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_commethod(18)
    def CreatePathKeyFrameAnimation(self) -> Windows.UI.Composition.PathKeyFrameAnimation: ...
    @winrt_commethod(19)
    def CreateRectangleGeometry(self) -> Windows.UI.Composition.CompositionRectangleGeometry: ...
    @winrt_commethod(20)
    def CreateRoundedRectangleGeometry(self) -> Windows.UI.Composition.CompositionRoundedRectangleGeometry: ...
    @winrt_commethod(21)
    def CreateShapeVisual(self) -> Windows.UI.Composition.ShapeVisual: ...
    @winrt_commethod(22)
    def CreateSpriteShape(self) -> Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_commethod(23)
    def CreateSpriteShapeWithGeometry(self, geometry: Windows.UI.Composition.CompositionGeometry) -> Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_commethod(24)
    def CreateViewBox(self) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(25)
    def RequestCommitAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, put_Comment)
    GlobalPlaybackRate = property(get_GlobalPlaybackRate, put_GlobalPlaybackRate)
class ICompositor6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor6'
    _iid_ = Guid('{7a38b2bd-cec8-4eeb-830f-d8d07aedebc3}')
    @winrt_commethod(6)
    def CreateGeometricClip(self) -> Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_commethod(7)
    def CreateGeometricClipWithGeometry(self, geometry: Windows.UI.Composition.CompositionGeometry) -> Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_commethod(8)
    def CreateRedirectVisual(self) -> Windows.UI.Composition.RedirectVisual: ...
    @winrt_commethod(9)
    def CreateRedirectVisualWithSourceVisual(self, source: Windows.UI.Composition.Visual) -> Windows.UI.Composition.RedirectVisual: ...
    @winrt_commethod(10)
    def CreateBooleanKeyFrameAnimation(self) -> Windows.UI.Composition.BooleanKeyFrameAnimation: ...
class ICompositor7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor7'
    _iid_ = Guid('{d3483fad-9a12-53ba-bfc8-88b7ff7977c6}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    @winrt_commethod(7)
    def CreateAnimationPropertyInfo(self) -> Windows.UI.Composition.AnimationPropertyInfo: ...
    @winrt_commethod(8)
    def CreateRectangleClip(self) -> Windows.UI.Composition.RectangleClip: ...
    @winrt_commethod(9)
    def CreateRectangleClipWithSides(self, left: Single, top: Single, right: Single, bottom: Single) -> Windows.UI.Composition.RectangleClip: ...
    @winrt_commethod(10)
    def CreateRectangleClipWithSidesAndRadius(self, left: Single, top: Single, right: Single, bottom: Single, topLeftRadius: Windows.Foundation.Numerics.Vector2, topRightRadius: Windows.Foundation.Numerics.Vector2, bottomRightRadius: Windows.Foundation.Numerics.Vector2, bottomLeftRadius: Windows.Foundation.Numerics.Vector2) -> Windows.UI.Composition.RectangleClip: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICompositor8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor8'
    _iid_ = Guid('{9a0bdee2-fe7b-5f62-a366-9cf8effe2112}')
    @winrt_commethod(6)
    def CreateAnimationController(self) -> Windows.UI.Composition.AnimationController: ...
class ICompositorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorStatics'
    _iid_ = Guid('{080db93e-121e-4d97-8b74-1dfcf91987ea}')
    @winrt_commethod(6)
    def get_MaxGlobalPlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def get_MinGlobalPlaybackRate(self) -> Single: ...
    MaxGlobalPlaybackRate = property(get_MaxGlobalPlaybackRate, None)
    MinGlobalPlaybackRate = property(get_MinGlobalPlaybackRate, None)
class ICompositorWithBlurredWallpaperBackdropBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithBlurredWallpaperBackdropBrush'
    _iid_ = Guid('{0d8fb190-f122-5b8d-9fdd-543b0d8eb7f3}')
    @winrt_commethod(6)
    def TryCreateBlurredWallpaperBackdropBrush(self) -> Windows.UI.Composition.CompositionBackdropBrush: ...
class ICompositorWithProjectedShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithProjectedShadow'
    _iid_ = Guid('{a2e6330e-8a60-5a38-bb85-b44ea901677c}')
    @winrt_commethod(6)
    def CreateProjectedShadowCaster(self) -> Windows.UI.Composition.CompositionProjectedShadowCaster: ...
    @winrt_commethod(7)
    def CreateProjectedShadow(self) -> Windows.UI.Composition.CompositionProjectedShadow: ...
    @winrt_commethod(8)
    def CreateProjectedShadowReceiver(self) -> Windows.UI.Composition.CompositionProjectedShadowReceiver: ...
class ICompositorWithRadialGradient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithRadialGradient'
    _iid_ = Guid('{98b9c1a7-8e71-4b53-b4a8-69ba5d19dc5b}')
    @winrt_commethod(6)
    def CreateRadialGradientBrush(self) -> Windows.UI.Composition.CompositionRadialGradientBrush: ...
class ICompositorWithVisualSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithVisualSurface'
    _iid_ = Guid('{cfa1658b-0123-4551-8891-89bdcc40322b}')
    @winrt_commethod(6)
    def CreateVisualSurface(self) -> Windows.UI.Composition.CompositionVisualSurface: ...
class IContainerVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IContainerVisual'
    _iid_ = Guid('{02f6bc74-ed20-4773-afe6-d49b4a93db32}')
    @winrt_commethod(6)
    def get_Children(self) -> Windows.UI.Composition.VisualCollection: ...
    Children = property(get_Children, None)
class IContainerVisualFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IContainerVisualFactory'
    _iid_ = Guid('{0363a65b-c7da-4d9a-95f4-69b5c8df670b}')
class ICubicBezierEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICubicBezierEasingFunction'
    _iid_ = Guid('{32350666-c1e8-44f9-96b8-c98acf0ae698}')
    @winrt_commethod(6)
    def get_ControlPoint1(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def get_ControlPoint2(self) -> Windows.Foundation.Numerics.Vector2: ...
    ControlPoint1 = property(get_ControlPoint1, None)
    ControlPoint2 = property(get_ControlPoint2, None)
class IDelegatedInkTrailVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDelegatedInkTrailVisual'
    _iid_ = Guid('{856e60b1-e1ab-5b23-8e3d-d513f221c998}')
    @winrt_commethod(6)
    def AddTrailPoints(self, inkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head)) -> UInt32: ...
    @winrt_commethod(7)
    def AddTrailPointsWithPrediction(self, inkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head), predictedInkPoints: POINTER(Windows.UI.Composition.InkTrailPoint_head)) -> UInt32: ...
    @winrt_commethod(8)
    def RemoveTrailPoints(self, generationId: UInt32) -> Void: ...
    @winrt_commethod(9)
    def StartNewTrail(self, color: Windows.UI.Color) -> Void: ...
class IDelegatedInkTrailVisualStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDelegatedInkTrailVisualStatics'
    _iid_ = Guid('{0daf6bd5-42c6-555c-9267-e0ac663af836}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.DelegatedInkTrailVisual: ...
    @winrt_commethod(7)
    def CreateForSwapChain(self, compositor: Windows.UI.Composition.Compositor, swapChain: Windows.UI.Composition.ICompositionSurface) -> Windows.UI.Composition.DelegatedInkTrailVisual: ...
class IDistantLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDistantLight'
    _iid_ = Guid('{318cfafc-5ce3-4b55-ab5d-07a00353ac99}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_CoordinateSpace(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CoordinateSpace(self, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Direction(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    Color = property(get_Color, put_Color)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
class IDistantLight2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDistantLight2'
    _iid_ = Guid('{dbcdaa1c-294b-48d7-b60e-76df64aa392b}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IDropShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDropShadow'
    _iid_ = Guid('{cb977c07-a154-4851-85e7-a8924c84fad8}')
    @winrt_commethod(6)
    def get_BlurRadius(self) -> Single: ...
    @winrt_commethod(7)
    def put_BlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Mask(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(11)
    def put_Mask(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(12)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Opacity(self) -> Single: ...
    @winrt_commethod(15)
    def put_Opacity(self, value: Single) -> Void: ...
    BlurRadius = property(get_BlurRadius, put_BlurRadius)
    Color = property(get_Color, put_Color)
    Mask = property(get_Mask, put_Mask)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
class IDropShadow2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDropShadow2'
    _iid_ = Guid('{6c4218bc-15b9-4c2d-8d4a-0767df11977a}')
    @winrt_commethod(6)
    def get_SourcePolicy(self) -> Windows.UI.Composition.CompositionDropShadowSourcePolicy: ...
    @winrt_commethod(7)
    def put_SourcePolicy(self, value: Windows.UI.Composition.CompositionDropShadowSourcePolicy) -> Void: ...
    SourcePolicy = property(get_SourcePolicy, put_SourcePolicy)
class IElasticEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IElasticEasingFunction'
    _iid_ = Guid('{66de6285-054e-5594-8475-c22cb51f1bd5}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Oscillations(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Springiness(self) -> Single: ...
    Mode = property(get_Mode, None)
    Oscillations = property(get_Oscillations, None)
    Springiness = property(get_Springiness, None)
class IExponentialEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IExponentialEasingFunction'
    _iid_ = Guid('{6f7d1a51-98d2-5638-a34a-00486554c750}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Exponent(self) -> Single: ...
    Mode = property(get_Mode, None)
    Exponent = property(get_Exponent, None)
class IExpressionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IExpressionAnimation'
    _iid_ = Guid('{6acc5431-7d3d-4bf3-abb6-f44bdc4888c1}')
    @winrt_commethod(6)
    def get_Expression(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Expression(self, value: WinRT_String) -> Void: ...
    Expression = property(get_Expression, put_Expression)
class IImplicitAnimationCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IImplicitAnimationCollection'
    _iid_ = Guid('{0598a3ff-0a92-4c9d-a427-b25519250dbf}')
class IInsetClip(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IInsetClip'
    _iid_ = Guid('{1e73e647-84c7-477a-b474-5880e0442e15}')
    @winrt_commethod(6)
    def get_BottomInset(self) -> Single: ...
    @winrt_commethod(7)
    def put_BottomInset(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_LeftInset(self) -> Single: ...
    @winrt_commethod(9)
    def put_LeftInset(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_RightInset(self) -> Single: ...
    @winrt_commethod(11)
    def put_RightInset(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_TopInset(self) -> Single: ...
    @winrt_commethod(13)
    def put_TopInset(self, value: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    LeftInset = property(get_LeftInset, put_LeftInset)
    RightInset = property(get_RightInset, put_RightInset)
    TopInset = property(get_TopInset, put_TopInset)
class IKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation'
    _iid_ = Guid('{126e7f22-3ae9-4540-9a8a-deae8a4a4a84}')
    @winrt_commethod(6)
    def get_DelayTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DelayTime(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_IterationBehavior(self) -> Windows.UI.Composition.AnimationIterationBehavior: ...
    @winrt_commethod(11)
    def put_IterationBehavior(self, value: Windows.UI.Composition.AnimationIterationBehavior) -> Void: ...
    @winrt_commethod(12)
    def get_IterationCount(self) -> Int32: ...
    @winrt_commethod(13)
    def put_IterationCount(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_KeyFrameCount(self) -> Int32: ...
    @winrt_commethod(15)
    def get_StopBehavior(self) -> Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_commethod(16)
    def put_StopBehavior(self, value: Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    @winrt_commethod(17)
    def InsertExpressionKeyFrame(self, normalizedProgressKey: Single, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def InsertExpressionKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: WinRT_String, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    DelayTime = property(get_DelayTime, put_DelayTime)
    Duration = property(get_Duration, put_Duration)
    IterationBehavior = property(get_IterationBehavior, put_IterationBehavior)
    IterationCount = property(get_IterationCount, put_IterationCount)
    KeyFrameCount = property(get_KeyFrameCount, None)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class IKeyFrameAnimation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation2'
    _iid_ = Guid('{f4b488bb-2940-4ec0-a41a-eb6d801a2f18}')
    @winrt_commethod(6)
    def get_Direction(self) -> Windows.UI.Composition.AnimationDirection: ...
    @winrt_commethod(7)
    def put_Direction(self, value: Windows.UI.Composition.AnimationDirection) -> Void: ...
    Direction = property(get_Direction, put_Direction)
class IKeyFrameAnimation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation3'
    _iid_ = Guid('{845bf0b4-d8de-462f-8753-c80d43c6ff5a}')
    @winrt_commethod(6)
    def get_DelayBehavior(self) -> Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_commethod(7)
    def put_DelayBehavior(self, value: Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
class IKeyFrameAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimationFactory'
    _iid_ = Guid('{bf0803f8-712a-4fc1-8c87-970859ed8d2e}')
class ILayerVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILayerVisual'
    _iid_ = Guid('{af843985-0444-4887-8e83-b40b253f822c}')
    @winrt_commethod(6)
    def get_Effect(self) -> Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_commethod(7)
    def put_Effect(self, value: Windows.UI.Composition.CompositionEffectBrush) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ILayerVisual2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILayerVisual2'
    _iid_ = Guid('{98f9aeeb-6f23-49f1-90b1-1f59a14fbce3}')
    @winrt_commethod(6)
    def get_Shadow(self) -> Windows.UI.Composition.CompositionShadow: ...
    @winrt_commethod(7)
    def put_Shadow(self, value: Windows.UI.Composition.CompositionShadow) -> Void: ...
    Shadow = property(get_Shadow, put_Shadow)
class ILinearEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILinearEasingFunction'
    _iid_ = Guid('{9400975a-c7a6-46b3-acf7-1a268a0a117d}')
class INaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.INaturalMotionAnimation'
    _iid_ = Guid('{438de12d-769b-4821-a949-284a6547e873}')
    @winrt_commethod(6)
    def get_DelayBehavior(self) -> Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_commethod(7)
    def put_DelayBehavior(self, value: Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    @winrt_commethod(8)
    def get_DelayTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_DelayTime(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StopBehavior(self) -> Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_commethod(11)
    def put_StopBehavior(self, value: Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
    DelayTime = property(get_DelayTime, put_DelayTime)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class INaturalMotionAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.INaturalMotionAnimationFactory'
    _iid_ = Guid('{f53acb06-cf6a-4387-a3fe-5221f3e7e0e0}')
class IPathKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPathKeyFrameAnimation'
    _iid_ = Guid('{9d0d18c9-1576-4b3f-be60-1d5031f5e71b}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, path: Windows.UI.Composition.CompositionPath) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, path: Windows.UI.Composition.CompositionPath, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IPointLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight'
    _iid_ = Guid('{b18545b3-0c5a-4ab0-bedc-4f3546948272}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_ConstantAttenuation(self) -> Single: ...
    @winrt_commethod(9)
    def put_ConstantAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_CoordinateSpace(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(11)
    def put_CoordinateSpace(self, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(12)
    def get_LinearAttenuation(self) -> Single: ...
    @winrt_commethod(13)
    def put_LinearAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(15)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def get_QuadraticAttenuation(self) -> Single: ...
    @winrt_commethod(17)
    def put_QuadraticAttenuation(self, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
class IPointLight2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight2'
    _iid_ = Guid('{efe98f2c-0678-4f69-b164-a810d995bcb7}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IPointLight3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight3'
    _iid_ = Guid('{4c0a8367-d4e9-468a-87ae-7ba43ab29485}')
    @winrt_commethod(6)
    def get_MinAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_MinAttenuationCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_MaxAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(9)
    def put_MaxAttenuationCutoff(self, value: Single) -> Void: ...
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class IPowerEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPowerEasingFunction'
    _iid_ = Guid('{c3ff53d6-138b-5815-891a-b7f615ccc563}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Power(self) -> Single: ...
    Mode = property(get_Mode, None)
    Power = property(get_Power, None)
class IQuaternionKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IQuaternionKeyFrameAnimation'
    _iid_ = Guid('{404e5835-ecf6-4240-8520-671279cf36bc}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Quaternion, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IRectangleClip(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRectangleClip'
    _iid_ = Guid('{b3e7549e-00b4-5b53-8be8-353f6c433101}')
    @winrt_commethod(6)
    def get_Bottom(self) -> Single: ...
    @winrt_commethod(7)
    def put_Bottom(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_BottomLeftRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_BottomLeftRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_BottomRightRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_BottomRightRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_Left(self) -> Single: ...
    @winrt_commethod(13)
    def put_Left(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Right(self) -> Single: ...
    @winrt_commethod(15)
    def put_Right(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Top(self) -> Single: ...
    @winrt_commethod(17)
    def put_Top(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_TopLeftRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(19)
    def put_TopLeftRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(20)
    def get_TopRightRadius(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(21)
    def put_TopRightRadius(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Bottom = property(get_Bottom, put_Bottom)
    BottomLeftRadius = property(get_BottomLeftRadius, put_BottomLeftRadius)
    BottomRightRadius = property(get_BottomRightRadius, put_BottomRightRadius)
    Left = property(get_Left, put_Left)
    Right = property(get_Right, put_Right)
    Top = property(get_Top, put_Top)
    TopLeftRadius = property(get_TopLeftRadius, put_TopLeftRadius)
    TopRightRadius = property(get_TopRightRadius, put_TopRightRadius)
class IRedirectVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRedirectVisual'
    _iid_ = Guid('{8cc6e340-8b75-5422-b06f-09ffe9f8617e}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_Source(self, value: Windows.UI.Composition.Visual) -> Void: ...
    Source = property(get_Source, put_Source)
class IRenderingDeviceReplacedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRenderingDeviceReplacedEventArgs'
    _iid_ = Guid('{3a31ac7d-28bf-4e7a-8524-71679d480f38}')
    @winrt_commethod(6)
    def get_GraphicsDevice(self) -> Windows.UI.Composition.CompositionGraphicsDevice: ...
    GraphicsDevice = property(get_GraphicsDevice, None)
class IScalarKeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarKeyFrameAnimation'
    _iid_ = Guid('{ae288fa9-252c-4b95-a725-bf85e38000a1}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Single) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Single, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarNaturalMotionAnimation'
    _iid_ = Guid('{94a94581-bf92-495b-b5bd-d2c659430737}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> Single: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: Single) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IScalarNaturalMotionAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarNaturalMotionAnimationFactory'
    _iid_ = Guid('{835aa4fc-671c-41dd-af48-ae8def8b1529}')
class IShapeVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IShapeVisual'
    _iid_ = Guid('{f2bd13c3-ba7e-4b0f-9126-ffb7536b8176}')
    @winrt_commethod(6)
    def get_Shapes(self) -> Windows.UI.Composition.CompositionShapeCollection: ...
    @winrt_commethod(7)
    def get_ViewBox(self) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(8)
    def put_ViewBox(self, value: Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Shapes = property(get_Shapes, None)
    ViewBox = property(get_ViewBox, put_ViewBox)
class ISineEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISineEasingFunction'
    _iid_ = Guid('{f1b518bf-9563-5474-bd13-44b2df4b1d58}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class ISpotLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight'
    _iid_ = Guid('{5a9fe273-44a1-4f95-a422-8fa5116bdb44}')
    @winrt_commethod(6)
    def get_ConstantAttenuation(self) -> Single: ...
    @winrt_commethod(7)
    def put_ConstantAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_CoordinateSpace(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CoordinateSpace(self, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Direction(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(12)
    def get_InnerConeAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_InnerConeAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_InnerConeAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_InnerConeAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_InnerConeColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_InnerConeColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_LinearAttenuation(self) -> Single: ...
    @winrt_commethod(19)
    def put_LinearAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(21)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(22)
    def get_OuterConeAngle(self) -> Single: ...
    @winrt_commethod(23)
    def put_OuterConeAngle(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_OuterConeAngleInDegrees(self) -> Single: ...
    @winrt_commethod(25)
    def put_OuterConeAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_OuterConeColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(27)
    def put_OuterConeColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(28)
    def get_QuadraticAttenuation(self) -> Single: ...
    @winrt_commethod(29)
    def put_QuadraticAttenuation(self, value: Single) -> Void: ...
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    InnerConeAngle = property(get_InnerConeAngle, put_InnerConeAngle)
    InnerConeAngleInDegrees = property(get_InnerConeAngleInDegrees, put_InnerConeAngleInDegrees)
    InnerConeColor = property(get_InnerConeColor, put_InnerConeColor)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    OuterConeAngle = property(get_OuterConeAngle, put_OuterConeAngle)
    OuterConeAngleInDegrees = property(get_OuterConeAngleInDegrees, put_OuterConeAngleInDegrees)
    OuterConeColor = property(get_OuterConeColor, put_OuterConeColor)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
class ISpotLight2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight2'
    _iid_ = Guid('{64ee615e-0686-4dea-a9e8-bc3a8c701459}')
    @winrt_commethod(6)
    def get_InnerConeIntensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_InnerConeIntensity(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_OuterConeIntensity(self) -> Single: ...
    @winrt_commethod(9)
    def put_OuterConeIntensity(self, value: Single) -> Void: ...
    InnerConeIntensity = property(get_InnerConeIntensity, put_InnerConeIntensity)
    OuterConeIntensity = property(get_OuterConeIntensity, put_OuterConeIntensity)
class ISpotLight3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight3'
    _iid_ = Guid('{e4d03eea-131f-480e-859e-b82705b74360}')
    @winrt_commethod(6)
    def get_MinAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_MinAttenuationCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_MaxAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(9)
    def put_MaxAttenuationCutoff(self, value: Single) -> Void: ...
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class ISpringScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringScalarNaturalMotionAnimation'
    _iid_ = Guid('{0572a95f-37f9-4fbe-b87b-5cd03a89501c}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpringVector2NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringVector2NaturalMotionAnimation'
    _iid_ = Guid('{23f494b5-ee73-4f0f-a423-402b946df4b3}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpringVector3NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringVector3NaturalMotionAnimation'
    _iid_ = Guid('{6c8749df-d57b-4794-8e2d-cecb11e194e5}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpriteVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpriteVisual'
    _iid_ = Guid('{08e05581-1ad1-4f97-9757-402d76e4233b}')
    @winrt_commethod(6)
    def get_Brush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Brush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    Brush = property(get_Brush, put_Brush)
class ISpriteVisual2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpriteVisual2'
    _iid_ = Guid('{588c9664-997a-4850-91fe-53cb58f81ce9}')
    @winrt_commethod(6)
    def get_Shadow(self) -> Windows.UI.Composition.CompositionShadow: ...
    @winrt_commethod(7)
    def put_Shadow(self, value: Windows.UI.Composition.CompositionShadow) -> Void: ...
    Shadow = property(get_Shadow, put_Shadow)
class IStepEasingFunction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IStepEasingFunction'
    _iid_ = Guid('{d0caa74b-560c-4a0b-a5f6-206ca8c3ecd6}')
    @winrt_commethod(6)
    def get_FinalStep(self) -> Int32: ...
    @winrt_commethod(7)
    def put_FinalStep(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_InitialStep(self) -> Int32: ...
    @winrt_commethod(9)
    def put_InitialStep(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_IsFinalStepSingleFrame(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsFinalStepSingleFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsInitialStepSingleFrame(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsInitialStepSingleFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_StepCount(self) -> Int32: ...
    @winrt_commethod(15)
    def put_StepCount(self, value: Int32) -> Void: ...
    FinalStep = property(get_FinalStep, put_FinalStep)
    InitialStep = property(get_InitialStep, put_InitialStep)
    IsFinalStepSingleFrame = property(get_IsFinalStepSingleFrame, put_IsFinalStepSingleFrame)
    IsInitialStepSingleFrame = property(get_IsInitialStepSingleFrame, put_IsInitialStepSingleFrame)
    StepCount = property(get_StepCount, put_StepCount)
class IVector2KeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2KeyFrameAnimation'
    _iid_ = Guid('{df414515-4e29-4f11-b55e-bf2a6eb36294}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector2, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVector2NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2NaturalMotionAnimation'
    _iid_ = Guid('{0f3e0b7d-e512-479d-a00c-77c93a30a395}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IVector2NaturalMotionAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2NaturalMotionAnimationFactory'
    _iid_ = Guid('{8c74ff61-0761-48a2-bddb-6afcc52b89d8}')
class IVector3KeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3KeyFrameAnimation'
    _iid_ = Guid('{c8039daa-a281-43c2-a73d-b68e3c533c40}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector3, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVector3NaturalMotionAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3NaturalMotionAnimation'
    _iid_ = Guid('{9c17042c-e2ca-45ad-969e-4e78b7b9ad41}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IVector3NaturalMotionAnimationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3NaturalMotionAnimationFactory'
    _iid_ = Guid('{21a81d2f-0880-457b-ac87-b609018c876d}')
class IVector4KeyFrameAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector4KeyFrameAnimation'
    _iid_ = Guid('{2457945b-addd-4385-9606-b6a3d5e4e1b9}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector4, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVisual(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual'
    _iid_ = Guid('{117e202d-a859-4c89-873b-c2aa566788e3}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_BackfaceVisibility(self) -> Windows.UI.Composition.CompositionBackfaceVisibility: ...
    @winrt_commethod(9)
    def put_BackfaceVisibility(self, value: Windows.UI.Composition.CompositionBackfaceVisibility) -> Void: ...
    @winrt_commethod(10)
    def get_BorderMode(self) -> Windows.UI.Composition.CompositionBorderMode: ...
    @winrt_commethod(11)
    def put_BorderMode(self, value: Windows.UI.Composition.CompositionBorderMode) -> Void: ...
    @winrt_commethod(12)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Clip(self) -> Windows.UI.Composition.CompositionClip: ...
    @winrt_commethod(15)
    def put_Clip(self, value: Windows.UI.Composition.CompositionClip) -> Void: ...
    @winrt_commethod(16)
    def get_CompositeMode(self) -> Windows.UI.Composition.CompositionCompositeMode: ...
    @winrt_commethod(17)
    def put_CompositeMode(self, value: Windows.UI.Composition.CompositionCompositeMode) -> Void: ...
    @winrt_commethod(18)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_Offset(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(21)
    def put_Offset(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(22)
    def get_Opacity(self) -> Single: ...
    @winrt_commethod(23)
    def put_Opacity(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_Orientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(25)
    def put_Orientation(self, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(26)
    def get_Parent(self) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(27)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(28)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(29)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(30)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(31)
    def get_RotationAxis(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(32)
    def put_RotationAxis(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(33)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(34)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(35)
    def get_Size(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(36)
    def put_Size(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(37)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(38)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    BackfaceVisibility = property(get_BackfaceVisibility, put_BackfaceVisibility)
    BorderMode = property(get_BorderMode, put_BorderMode)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Clip = property(get_Clip, put_Clip)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    Orientation = property(get_Orientation, put_Orientation)
    Parent = property(get_Parent, None)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Size = property(get_Size, put_Size)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class IVisual2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual2'
    _iid_ = Guid('{3052b611-56c3-4c3e-8bf3-f6e1ad473f06}')
    @winrt_commethod(6)
    def get_ParentForTransform(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_ParentForTransform(self, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def get_RelativeOffsetAdjustment(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def put_RelativeOffsetAdjustment(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(10)
    def get_RelativeSizeAdjustment(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_RelativeSizeAdjustment(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    ParentForTransform = property(get_ParentForTransform, put_ParentForTransform)
    RelativeOffsetAdjustment = property(get_RelativeOffsetAdjustment, put_RelativeOffsetAdjustment)
    RelativeSizeAdjustment = property(get_RelativeSizeAdjustment, put_RelativeSizeAdjustment)
class IVisual3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual3'
    _iid_ = Guid('{30be580d-f4b6-4ab7-80dd-3738cbac9f2c}')
    @winrt_commethod(6)
    def get_IsHitTestVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsHitTestVisible(self, value: Boolean) -> Void: ...
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
class IVisual4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual4'
    _iid_ = Guid('{9476bf11-e24b-5bf9-9ebe-6274109b2711}')
    @winrt_commethod(6)
    def get_IsPixelSnappingEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPixelSnappingEnabled(self, value: Boolean) -> Void: ...
    IsPixelSnappingEnabled = property(get_IsPixelSnappingEnabled, put_IsPixelSnappingEnabled)
class IVisualCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualCollection'
    _iid_ = Guid('{8b745505-fd3e-4a98-84a8-e949468c6bcb}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def InsertAbove(self, newChild: Windows.UI.Composition.Visual, sibling: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def InsertAtBottom(self, newChild: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def InsertAtTop(self, newChild: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def InsertBelow(self, newChild: Windows.UI.Composition.Visual, sibling: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(11)
    def Remove(self, child: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(12)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class IVisualElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualElement'
    _iid_ = Guid('{01e64612-1d82-42f4-8e3f-a722ded33fc7}')
class IVisualElement2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualElement2'
    _iid_ = Guid('{993ae8a0-6057-5e40-918c-e06e0b7e7c64}')
    @winrt_commethod(6)
    def GetVisualInternal(self) -> Windows.UI.Composition.Visual: ...
class IVisualFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualFactory'
    _iid_ = Guid('{ad0ff93e-b502-4eb5-87b4-9a38a71d0137}')
class IVisualUnorderedCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualUnorderedCollection'
    _iid_ = Guid('{338faa70-54c8-40a7-8029-c9ceeb0aa250}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, newVisual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ImplicitAnimationCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IImplicitAnimationCollection
    _classid_ = 'Windows.UI.Composition.ImplicitAnimationCollection'
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]]: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> Windows.UI.Composition.ICompositionAnimationBase: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String, value: Windows.UI.Composition.ICompositionAnimationBase) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.ICompositionAnimationBase]) -> Void: ...
    Size = property(get_Size, None)
class InitialValueExpressionCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.UI.Composition.InitialValueExpressionCollection'
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
class InkTrailPoint(EasyCastStructure):
    Point: Windows.Foundation.Point
    Radius: Single
class InsetClip(ComPtr):
    extends: Windows.UI.Composition.CompositionClip
    default_interface: Windows.UI.Composition.IInsetClip
    _classid_ = 'Windows.UI.Composition.InsetClip'
    @winrt_mixinmethod
    def get_BottomInset(self: Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInset(self: Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInset(self: Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInset(self: Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInset(self: Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_RightInset(self: Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopInset(self: Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_TopInset(self: Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    LeftInset = property(get_LeftInset, put_LeftInset)
    RightInset = property(get_RightInset, put_RightInset)
    TopInset = property(get_TopInset, put_TopInset)
class KeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.CompositionAnimation
    default_interface: Windows.UI.Composition.IKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.KeyFrameAnimation'
    @winrt_mixinmethod
    def get_DelayTime(self: Windows.UI.Composition.IKeyFrameAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DelayTime(self: Windows.UI.Composition.IKeyFrameAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.UI.Composition.IKeyFrameAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.UI.Composition.IKeyFrameAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IterationBehavior(self: Windows.UI.Composition.IKeyFrameAnimation) -> Windows.UI.Composition.AnimationIterationBehavior: ...
    @winrt_mixinmethod
    def put_IterationBehavior(self: Windows.UI.Composition.IKeyFrameAnimation, value: Windows.UI.Composition.AnimationIterationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_IterationCount(self: Windows.UI.Composition.IKeyFrameAnimation) -> Int32: ...
    @winrt_mixinmethod
    def put_IterationCount(self: Windows.UI.Composition.IKeyFrameAnimation, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_KeyFrameCount(self: Windows.UI.Composition.IKeyFrameAnimation) -> Int32: ...
    @winrt_mixinmethod
    def get_StopBehavior(self: Windows.UI.Composition.IKeyFrameAnimation) -> Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_mixinmethod
    def put_StopBehavior(self: Windows.UI.Composition.IKeyFrameAnimation, value: Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    @winrt_mixinmethod
    def InsertExpressionKeyFrame(self: Windows.UI.Composition.IKeyFrameAnimation, normalizedProgressKey: Single, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def InsertExpressionKeyFrameWithEasingFunction(self: Windows.UI.Composition.IKeyFrameAnimation, normalizedProgressKey: Single, value: WinRT_String, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Composition.IKeyFrameAnimation2) -> Windows.UI.Composition.AnimationDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: Windows.UI.Composition.IKeyFrameAnimation2, value: Windows.UI.Composition.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_DelayBehavior(self: Windows.UI.Composition.IKeyFrameAnimation3) -> Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_mixinmethod
    def put_DelayBehavior(self: Windows.UI.Composition.IKeyFrameAnimation3, value: Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    DelayTime = property(get_DelayTime, put_DelayTime)
    Duration = property(get_Duration, put_Duration)
    IterationBehavior = property(get_IterationBehavior, put_IterationBehavior)
    IterationCount = property(get_IterationCount, put_IterationCount)
    KeyFrameCount = property(get_KeyFrameCount, None)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
    Direction = property(get_Direction, put_Direction)
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
class LayerVisual(ComPtr):
    extends: Windows.UI.Composition.ContainerVisual
    default_interface: Windows.UI.Composition.ILayerVisual
    _classid_ = 'Windows.UI.Composition.LayerVisual'
    @winrt_mixinmethod
    def get_Effect(self: Windows.UI.Composition.ILayerVisual) -> Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_mixinmethod
    def put_Effect(self: Windows.UI.Composition.ILayerVisual, value: Windows.UI.Composition.CompositionEffectBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Shadow(self: Windows.UI.Composition.ILayerVisual2) -> Windows.UI.Composition.CompositionShadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: Windows.UI.Composition.ILayerVisual2, value: Windows.UI.Composition.CompositionShadow) -> Void: ...
    Effect = property(get_Effect, put_Effect)
    Shadow = property(get_Shadow, put_Shadow)
class LinearEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.ILinearEasingFunction
    _classid_ = 'Windows.UI.Composition.LinearEasingFunction'
class NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.CompositionAnimation
    default_interface: Windows.UI.Composition.INaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DelayBehavior(self: Windows.UI.Composition.INaturalMotionAnimation) -> Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_mixinmethod
    def put_DelayBehavior(self: Windows.UI.Composition.INaturalMotionAnimation, value: Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_DelayTime(self: Windows.UI.Composition.INaturalMotionAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DelayTime(self: Windows.UI.Composition.INaturalMotionAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StopBehavior(self: Windows.UI.Composition.INaturalMotionAnimation) -> Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_mixinmethod
    def put_StopBehavior(self: Windows.UI.Composition.INaturalMotionAnimation, value: Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
    DelayTime = property(get_DelayTime, put_DelayTime)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class PathKeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IPathKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.PathKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IPathKeyFrameAnimation, normalizedProgressKey: Single, path: Windows.UI.Composition.CompositionPath) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IPathKeyFrameAnimation, normalizedProgressKey: Single, path: Windows.UI.Composition.CompositionPath, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class PointLight(ComPtr):
    extends: Windows.UI.Composition.CompositionLight
    default_interface: Windows.UI.Composition.IPointLight
    _classid_ = 'Windows.UI.Composition.PointLight'
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Composition.IPointLight) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Composition.IPointLight, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ConstantAttenuation(self: Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_ConstantAttenuation(self: Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: Windows.UI.Composition.IPointLight) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: Windows.UI.Composition.IPointLight, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_LinearAttenuation(self: Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_LinearAttenuation(self: Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.IPointLight) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.IPointLight, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_QuadraticAttenuation(self: Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_QuadraticAttenuation(self: Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: Windows.UI.Composition.IPointLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: Windows.UI.Composition.IPointLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinAttenuationCutoff(self: Windows.UI.Composition.IPointLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MinAttenuationCutoff(self: Windows.UI.Composition.IPointLight3, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAttenuationCutoff(self: Windows.UI.Composition.IPointLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MaxAttenuationCutoff(self: Windows.UI.Composition.IPointLight3, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
    Intensity = property(get_Intensity, put_Intensity)
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class PowerEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IPowerEasingFunction
    _classid_ = 'Windows.UI.Composition.PowerEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.IPowerEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Power(self: Windows.UI.Composition.IPowerEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Power = property(get_Power, None)
class QuaternionKeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IQuaternionKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.QuaternionKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IQuaternionKeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IQuaternionKeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Quaternion, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class RectangleClip(ComPtr):
    extends: Windows.UI.Composition.CompositionClip
    default_interface: Windows.UI.Composition.IRectangleClip
    _classid_ = 'Windows.UI.Composition.RectangleClip'
    @winrt_mixinmethod
    def get_Bottom(self: Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Bottom(self: Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomLeftRadius(self: Windows.UI.Composition.IRectangleClip) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_BottomLeftRadius(self: Windows.UI.Composition.IRectangleClip, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_BottomRightRadius(self: Windows.UI.Composition.IRectangleClip) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_BottomRightRadius(self: Windows.UI.Composition.IRectangleClip, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Left(self: Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Left(self: Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Right(self: Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Right(self: Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Top(self: Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Top(self: Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopLeftRadius(self: Windows.UI.Composition.IRectangleClip) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_TopLeftRadius(self: Windows.UI.Composition.IRectangleClip, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TopRightRadius(self: Windows.UI.Composition.IRectangleClip) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_TopRightRadius(self: Windows.UI.Composition.IRectangleClip, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    Bottom = property(get_Bottom, put_Bottom)
    BottomLeftRadius = property(get_BottomLeftRadius, put_BottomLeftRadius)
    BottomRightRadius = property(get_BottomRightRadius, put_BottomRightRadius)
    Left = property(get_Left, put_Left)
    Right = property(get_Right, put_Right)
    Top = property(get_Top, put_Top)
    TopLeftRadius = property(get_TopLeftRadius, put_TopLeftRadius)
    TopRightRadius = property(get_TopRightRadius, put_TopRightRadius)
class RedirectVisual(ComPtr):
    extends: Windows.UI.Composition.ContainerVisual
    default_interface: Windows.UI.Composition.IRedirectVisual
    _classid_ = 'Windows.UI.Composition.RedirectVisual'
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Composition.IRedirectVisual) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Composition.IRedirectVisual, value: Windows.UI.Composition.Visual) -> Void: ...
    Source = property(get_Source, put_Source)
class RenderingDeviceReplacedEventArgs(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IRenderingDeviceReplacedEventArgs
    _classid_ = 'Windows.UI.Composition.RenderingDeviceReplacedEventArgs'
    @winrt_mixinmethod
    def get_GraphicsDevice(self: Windows.UI.Composition.IRenderingDeviceReplacedEventArgs) -> Windows.UI.Composition.CompositionGraphicsDevice: ...
    GraphicsDevice = property(get_GraphicsDevice, None)
class ScalarKeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IScalarKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.ScalarKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IScalarKeyFrameAnimation, normalizedProgressKey: Single, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IScalarKeyFrameAnimation, normalizedProgressKey: Single, value: Single, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class ScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.NaturalMotionAnimation
    default_interface: Windows.UI.Composition.IScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.ScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: Windows.UI.Composition.IScalarNaturalMotionAnimation) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: Windows.UI.Composition.IScalarNaturalMotionAnimation, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: Windows.UI.Composition.IScalarNaturalMotionAnimation) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: Windows.UI.Composition.IScalarNaturalMotionAnimation, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: Windows.UI.Composition.IScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: Windows.UI.Composition.IScalarNaturalMotionAnimation, value: Single) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class ShapeVisual(ComPtr):
    extends: Windows.UI.Composition.ContainerVisual
    default_interface: Windows.UI.Composition.IShapeVisual
    _classid_ = 'Windows.UI.Composition.ShapeVisual'
    @winrt_mixinmethod
    def get_Shapes(self: Windows.UI.Composition.IShapeVisual) -> Windows.UI.Composition.CompositionShapeCollection: ...
    @winrt_mixinmethod
    def get_ViewBox(self: Windows.UI.Composition.IShapeVisual) -> Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def put_ViewBox(self: Windows.UI.Composition.IShapeVisual, value: Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Shapes = property(get_Shapes, None)
    ViewBox = property(get_ViewBox, put_ViewBox)
class SineEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.ISineEasingFunction
    _classid_ = 'Windows.UI.Composition.SineEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Composition.ISineEasingFunction) -> Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class SpotLight(ComPtr):
    extends: Windows.UI.Composition.CompositionLight
    default_interface: Windows.UI.Composition.ISpotLight
    _classid_ = 'Windows.UI.Composition.SpotLight'
    @winrt_mixinmethod
    def get_ConstantAttenuation(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_ConstantAttenuation(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: Windows.UI.Composition.ISpotLight) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: Windows.UI.Composition.ISpotLight, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Composition.ISpotLight) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Direction(self: Windows.UI.Composition.ISpotLight, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeAngle(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeAngle(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeAngleInDegrees(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeAngleInDegrees(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeColor(self: Windows.UI.Composition.ISpotLight) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_InnerConeColor(self: Windows.UI.Composition.ISpotLight, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_LinearAttenuation(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_LinearAttenuation(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.ISpotLight) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.ISpotLight, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeAngle(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeAngle(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeAngleInDegrees(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeAngleInDegrees(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeColor(self: Windows.UI.Composition.ISpotLight) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_OuterConeColor(self: Windows.UI.Composition.ISpotLight, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_QuadraticAttenuation(self: Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_QuadraticAttenuation(self: Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeIntensity(self: Windows.UI.Composition.ISpotLight2) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeIntensity(self: Windows.UI.Composition.ISpotLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeIntensity(self: Windows.UI.Composition.ISpotLight2) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeIntensity(self: Windows.UI.Composition.ISpotLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinAttenuationCutoff(self: Windows.UI.Composition.ISpotLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MinAttenuationCutoff(self: Windows.UI.Composition.ISpotLight3, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAttenuationCutoff(self: Windows.UI.Composition.ISpotLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MaxAttenuationCutoff(self: Windows.UI.Composition.ISpotLight3, value: Single) -> Void: ...
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    InnerConeAngle = property(get_InnerConeAngle, put_InnerConeAngle)
    InnerConeAngleInDegrees = property(get_InnerConeAngleInDegrees, put_InnerConeAngleInDegrees)
    InnerConeColor = property(get_InnerConeColor, put_InnerConeColor)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    OuterConeAngle = property(get_OuterConeAngle, put_OuterConeAngle)
    OuterConeAngleInDegrees = property(get_OuterConeAngleInDegrees, put_OuterConeAngleInDegrees)
    OuterConeColor = property(get_OuterConeColor, put_OuterConeColor)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
    InnerConeIntensity = property(get_InnerConeIntensity, put_InnerConeIntensity)
    OuterConeIntensity = property(get_OuterConeIntensity, put_OuterConeIntensity)
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class SpringScalarNaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.ScalarNaturalMotionAnimation
    default_interface: Windows.UI.Composition.ISpringScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: Windows.UI.Composition.ISpringScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: Windows.UI.Composition.ISpringScalarNaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: Windows.UI.Composition.ISpringScalarNaturalMotionAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: Windows.UI.Composition.ISpringScalarNaturalMotionAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpringVector2NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.Vector2NaturalMotionAnimation
    default_interface: Windows.UI.Composition.ISpringVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringVector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: Windows.UI.Composition.ISpringVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: Windows.UI.Composition.ISpringVector2NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: Windows.UI.Composition.ISpringVector2NaturalMotionAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: Windows.UI.Composition.ISpringVector2NaturalMotionAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpringVector3NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.Vector3NaturalMotionAnimation
    default_interface: Windows.UI.Composition.ISpringVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringVector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: Windows.UI.Composition.ISpringVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: Windows.UI.Composition.ISpringVector3NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: Windows.UI.Composition.ISpringVector3NaturalMotionAnimation) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: Windows.UI.Composition.ISpringVector3NaturalMotionAnimation, value: Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpriteVisual(ComPtr):
    extends: Windows.UI.Composition.ContainerVisual
    default_interface: Windows.UI.Composition.ISpriteVisual
    _classid_ = 'Windows.UI.Composition.SpriteVisual'
    @winrt_mixinmethod
    def get_Brush(self: Windows.UI.Composition.ISpriteVisual) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Brush(self: Windows.UI.Composition.ISpriteVisual, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Shadow(self: Windows.UI.Composition.ISpriteVisual2) -> Windows.UI.Composition.CompositionShadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: Windows.UI.Composition.ISpriteVisual2, value: Windows.UI.Composition.CompositionShadow) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    Shadow = property(get_Shadow, put_Shadow)
class StepEasingFunction(ComPtr):
    extends: Windows.UI.Composition.CompositionEasingFunction
    default_interface: Windows.UI.Composition.IStepEasingFunction
    _classid_ = 'Windows.UI.Composition.StepEasingFunction'
    @winrt_mixinmethod
    def get_FinalStep(self: Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_FinalStep(self: Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_InitialStep(self: Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_InitialStep(self: Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsFinalStepSingleFrame(self: Windows.UI.Composition.IStepEasingFunction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFinalStepSingleFrame(self: Windows.UI.Composition.IStepEasingFunction, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsInitialStepSingleFrame(self: Windows.UI.Composition.IStepEasingFunction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInitialStepSingleFrame(self: Windows.UI.Composition.IStepEasingFunction, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StepCount(self: Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_StepCount(self: Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    FinalStep = property(get_FinalStep, put_FinalStep)
    InitialStep = property(get_InitialStep, put_InitialStep)
    IsFinalStepSingleFrame = property(get_IsFinalStepSingleFrame, put_IsFinalStepSingleFrame)
    IsInitialStepSingleFrame = property(get_IsInitialStepSingleFrame, put_IsInitialStepSingleFrame)
    StepCount = property(get_StepCount, put_StepCount)
class Vector2KeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IVector2KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector2KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IVector2KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IVector2KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector2, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Vector2NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.NaturalMotionAnimation
    default_interface: Windows.UI.Composition.IVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.Vector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: Windows.UI.Composition.IVector2NaturalMotionAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: Windows.UI.Composition.IVector2NaturalMotionAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: Windows.UI.Composition.IVector2NaturalMotionAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: Windows.UI.Composition.IVector2NaturalMotionAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: Windows.UI.Composition.IVector2NaturalMotionAnimation) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: Windows.UI.Composition.IVector2NaturalMotionAnimation, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class Vector3KeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IVector3KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector3KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IVector3KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IVector3KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector3, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Vector3NaturalMotionAnimation(ComPtr):
    extends: Windows.UI.Composition.NaturalMotionAnimation
    default_interface: Windows.UI.Composition.IVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.Vector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: Windows.UI.Composition.IVector3NaturalMotionAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: Windows.UI.Composition.IVector3NaturalMotionAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: Windows.UI.Composition.IVector3NaturalMotionAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: Windows.UI.Composition.IVector3NaturalMotionAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: Windows.UI.Composition.IVector3NaturalMotionAnimation) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: Windows.UI.Composition.IVector3NaturalMotionAnimation, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class Vector4KeyFrameAnimation(ComPtr):
    extends: Windows.UI.Composition.KeyFrameAnimation
    default_interface: Windows.UI.Composition.IVector4KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector4KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: Windows.UI.Composition.IVector4KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: Windows.UI.Composition.IVector4KeyFrameAnimation, normalizedProgressKey: Single, value: Windows.Foundation.Numerics.Vector4, easingFunction: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Visual(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IVisual
    _classid_ = 'Windows.UI.Composition.Visual'
    @winrt_mixinmethod
    def get_AnchorPoint(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_BackfaceVisibility(self: Windows.UI.Composition.IVisual) -> Windows.UI.Composition.CompositionBackfaceVisibility: ...
    @winrt_mixinmethod
    def put_BackfaceVisibility(self: Windows.UI.Composition.IVisual, value: Windows.UI.Composition.CompositionBackfaceVisibility) -> Void: ...
    @winrt_mixinmethod
    def get_BorderMode(self: Windows.UI.Composition.IVisual) -> Windows.UI.Composition.CompositionBorderMode: ...
    @winrt_mixinmethod
    def put_BorderMode(self: Windows.UI.Composition.IVisual, value: Windows.UI.Composition.CompositionBorderMode) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Clip(self: Windows.UI.Composition.IVisual) -> Windows.UI.Composition.CompositionClip: ...
    @winrt_mixinmethod
    def put_Clip(self: Windows.UI.Composition.IVisual, value: Windows.UI.Composition.CompositionClip) -> Void: ...
    @winrt_mixinmethod
    def get_CompositeMode(self: Windows.UI.Composition.IVisual) -> Windows.UI.Composition.CompositionCompositeMode: ...
    @winrt_mixinmethod
    def put_CompositeMode(self: Windows.UI.Composition.IVisual, value: Windows.UI.Composition.CompositionCompositeMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.Composition.IVisual) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: Windows.UI.Composition.IVisual, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_Opacity(self: Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_Orientation(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Composition.IVisual) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Composition.IVisual) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Composition.IVisual, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def get_ParentForTransform(self: Windows.UI.Composition.IVisual2) -> Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_ParentForTransform(self: Windows.UI.Composition.IVisual2, value: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeOffsetAdjustment(self: Windows.UI.Composition.IVisual2) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RelativeOffsetAdjustment(self: Windows.UI.Composition.IVisual2, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeSizeAdjustment(self: Windows.UI.Composition.IVisual2) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_RelativeSizeAdjustment(self: Windows.UI.Composition.IVisual2, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_IsHitTestVisible(self: Windows.UI.Composition.IVisual3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHitTestVisible(self: Windows.UI.Composition.IVisual3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPixelSnappingEnabled(self: Windows.UI.Composition.IVisual4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPixelSnappingEnabled(self: Windows.UI.Composition.IVisual4, value: Boolean) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    BackfaceVisibility = property(get_BackfaceVisibility, put_BackfaceVisibility)
    BorderMode = property(get_BorderMode, put_BorderMode)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Clip = property(get_Clip, put_Clip)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    Orientation = property(get_Orientation, put_Orientation)
    Parent = property(get_Parent, None)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Size = property(get_Size, put_Size)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    ParentForTransform = property(get_ParentForTransform, put_ParentForTransform)
    RelativeOffsetAdjustment = property(get_RelativeOffsetAdjustment, put_RelativeOffsetAdjustment)
    RelativeSizeAdjustment = property(get_RelativeSizeAdjustment, put_RelativeSizeAdjustment)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    IsPixelSnappingEnabled = property(get_IsPixelSnappingEnabled, put_IsPixelSnappingEnabled)
class VisualCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IVisualCollection
    _classid_ = 'Windows.UI.Composition.VisualCollection'
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.IVisualCollection) -> Int32: ...
    @winrt_mixinmethod
    def InsertAbove(self: Windows.UI.Composition.IVisualCollection, newChild: Windows.UI.Composition.Visual, sibling: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertAtBottom(self: Windows.UI.Composition.IVisualCollection, newChild: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertAtTop(self: Windows.UI.Composition.IVisualCollection, newChild: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertBelow(self: Windows.UI.Composition.IVisualCollection, newChild: Windows.UI.Composition.Visual, sibling: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.IVisualCollection, child: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.IVisualCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Visual]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.Visual]: ...
    Count = property(get_Count, None)
class VisualUnorderedCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    default_interface: Windows.UI.Composition.IVisualUnorderedCollection
    _classid_ = 'Windows.UI.Composition.VisualUnorderedCollection'
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.IVisualUnorderedCollection) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: Windows.UI.Composition.IVisualUnorderedCollection, newVisual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.IVisualUnorderedCollection, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.IVisualUnorderedCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Visual]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.Visual]: ...
    Count = property(get_Count, None)
make_head(_module, 'AmbientLight')
make_head(_module, 'AnimationController')
make_head(_module, 'AnimationPropertyInfo')
make_head(_module, 'BackEasingFunction')
make_head(_module, 'BooleanKeyFrameAnimation')
make_head(_module, 'BounceEasingFunction')
make_head(_module, 'BounceScalarNaturalMotionAnimation')
make_head(_module, 'BounceVector2NaturalMotionAnimation')
make_head(_module, 'BounceVector3NaturalMotionAnimation')
make_head(_module, 'CircleEasingFunction')
make_head(_module, 'ColorKeyFrameAnimation')
make_head(_module, 'CompositionAnimation')
make_head(_module, 'CompositionAnimationGroup')
make_head(_module, 'CompositionBackdropBrush')
make_head(_module, 'CompositionBatchCompletedEventArgs')
make_head(_module, 'CompositionBrush')
make_head(_module, 'CompositionCapabilities')
make_head(_module, 'CompositionClip')
make_head(_module, 'CompositionColorBrush')
make_head(_module, 'CompositionColorGradientStop')
make_head(_module, 'CompositionColorGradientStopCollection')
make_head(_module, 'CompositionCommitBatch')
make_head(_module, 'CompositionContainerShape')
make_head(_module, 'CompositionDrawingSurface')
make_head(_module, 'CompositionEasingFunction')
make_head(_module, 'CompositionEffectBrush')
make_head(_module, 'CompositionEffectFactory')
make_head(_module, 'CompositionEffectSourceParameter')
make_head(_module, 'CompositionEllipseGeometry')
make_head(_module, 'CompositionGeometricClip')
make_head(_module, 'CompositionGeometry')
make_head(_module, 'CompositionGradientBrush')
make_head(_module, 'CompositionGraphicsDevice')
make_head(_module, 'CompositionLight')
make_head(_module, 'CompositionLineGeometry')
make_head(_module, 'CompositionLinearGradientBrush')
make_head(_module, 'CompositionMaskBrush')
make_head(_module, 'CompositionMipmapSurface')
make_head(_module, 'CompositionNineGridBrush')
make_head(_module, 'CompositionObject')
make_head(_module, 'CompositionPath')
make_head(_module, 'CompositionPathGeometry')
make_head(_module, 'CompositionProjectedShadow')
make_head(_module, 'CompositionProjectedShadowCaster')
make_head(_module, 'CompositionProjectedShadowCasterCollection')
make_head(_module, 'CompositionProjectedShadowReceiver')
make_head(_module, 'CompositionProjectedShadowReceiverUnorderedCollection')
make_head(_module, 'CompositionPropertySet')
make_head(_module, 'CompositionRadialGradientBrush')
make_head(_module, 'CompositionRectangleGeometry')
make_head(_module, 'CompositionRoundedRectangleGeometry')
make_head(_module, 'CompositionScopedBatch')
make_head(_module, 'CompositionShadow')
make_head(_module, 'CompositionShape')
make_head(_module, 'CompositionShapeCollection')
make_head(_module, 'CompositionSpriteShape')
make_head(_module, 'CompositionStrokeDashArray')
make_head(_module, 'CompositionSurfaceBrush')
make_head(_module, 'CompositionTarget')
make_head(_module, 'CompositionTransform')
make_head(_module, 'CompositionViewBox')
make_head(_module, 'CompositionVirtualDrawingSurface')
make_head(_module, 'CompositionVisualSurface')
make_head(_module, 'Compositor')
make_head(_module, 'ContainerVisual')
make_head(_module, 'CubicBezierEasingFunction')
make_head(_module, 'DelegatedInkTrailVisual')
make_head(_module, 'DistantLight')
make_head(_module, 'DropShadow')
make_head(_module, 'ElasticEasingFunction')
make_head(_module, 'ExponentialEasingFunction')
make_head(_module, 'ExpressionAnimation')
make_head(_module, 'IAmbientLight')
make_head(_module, 'IAmbientLight2')
make_head(_module, 'IAnimationController')
make_head(_module, 'IAnimationControllerStatics')
make_head(_module, 'IAnimationObject')
make_head(_module, 'IAnimationPropertyInfo')
make_head(_module, 'IAnimationPropertyInfo2')
make_head(_module, 'IBackEasingFunction')
make_head(_module, 'IBooleanKeyFrameAnimation')
make_head(_module, 'IBounceEasingFunction')
make_head(_module, 'IBounceScalarNaturalMotionAnimation')
make_head(_module, 'IBounceVector2NaturalMotionAnimation')
make_head(_module, 'IBounceVector3NaturalMotionAnimation')
make_head(_module, 'ICircleEasingFunction')
make_head(_module, 'IColorKeyFrameAnimation')
make_head(_module, 'ICompositionAnimation')
make_head(_module, 'ICompositionAnimation2')
make_head(_module, 'ICompositionAnimation3')
make_head(_module, 'ICompositionAnimation4')
make_head(_module, 'ICompositionAnimationBase')
make_head(_module, 'ICompositionAnimationFactory')
make_head(_module, 'ICompositionAnimationGroup')
make_head(_module, 'ICompositionBackdropBrush')
make_head(_module, 'ICompositionBatchCompletedEventArgs')
make_head(_module, 'ICompositionBrush')
make_head(_module, 'ICompositionBrushFactory')
make_head(_module, 'ICompositionCapabilities')
make_head(_module, 'ICompositionCapabilitiesStatics')
make_head(_module, 'ICompositionClip')
make_head(_module, 'ICompositionClip2')
make_head(_module, 'ICompositionClipFactory')
make_head(_module, 'ICompositionColorBrush')
make_head(_module, 'ICompositionColorGradientStop')
make_head(_module, 'ICompositionColorGradientStopCollection')
make_head(_module, 'ICompositionCommitBatch')
make_head(_module, 'ICompositionContainerShape')
make_head(_module, 'ICompositionDrawingSurface')
make_head(_module, 'ICompositionDrawingSurface2')
make_head(_module, 'ICompositionDrawingSurfaceFactory')
make_head(_module, 'ICompositionEasingFunction')
make_head(_module, 'ICompositionEasingFunctionFactory')
make_head(_module, 'ICompositionEasingFunctionStatics')
make_head(_module, 'ICompositionEffectBrush')
make_head(_module, 'ICompositionEffectFactory')
make_head(_module, 'ICompositionEffectSourceParameter')
make_head(_module, 'ICompositionEffectSourceParameterFactory')
make_head(_module, 'ICompositionEllipseGeometry')
make_head(_module, 'ICompositionGeometricClip')
make_head(_module, 'ICompositionGeometry')
make_head(_module, 'ICompositionGeometryFactory')
make_head(_module, 'ICompositionGradientBrush')
make_head(_module, 'ICompositionGradientBrush2')
make_head(_module, 'ICompositionGradientBrushFactory')
make_head(_module, 'ICompositionGraphicsDevice')
make_head(_module, 'ICompositionGraphicsDevice2')
make_head(_module, 'ICompositionGraphicsDevice3')
make_head(_module, 'ICompositionGraphicsDevice4')
make_head(_module, 'ICompositionLight')
make_head(_module, 'ICompositionLight2')
make_head(_module, 'ICompositionLight3')
make_head(_module, 'ICompositionLightFactory')
make_head(_module, 'ICompositionLineGeometry')
make_head(_module, 'ICompositionLinearGradientBrush')
make_head(_module, 'ICompositionMaskBrush')
make_head(_module, 'ICompositionMipmapSurface')
make_head(_module, 'ICompositionNineGridBrush')
make_head(_module, 'ICompositionObject')
make_head(_module, 'ICompositionObject2')
make_head(_module, 'ICompositionObject3')
make_head(_module, 'ICompositionObject4')
make_head(_module, 'ICompositionObject5')
make_head(_module, 'ICompositionObjectFactory')
make_head(_module, 'ICompositionObjectStatics')
make_head(_module, 'ICompositionPath')
make_head(_module, 'ICompositionPathFactory')
make_head(_module, 'ICompositionPathGeometry')
make_head(_module, 'ICompositionProjectedShadow')
make_head(_module, 'ICompositionProjectedShadowCaster')
make_head(_module, 'ICompositionProjectedShadowCasterCollection')
make_head(_module, 'ICompositionProjectedShadowCasterCollectionStatics')
make_head(_module, 'ICompositionProjectedShadowReceiver')
make_head(_module, 'ICompositionProjectedShadowReceiverUnorderedCollection')
make_head(_module, 'ICompositionPropertySet')
make_head(_module, 'ICompositionPropertySet2')
make_head(_module, 'ICompositionRadialGradientBrush')
make_head(_module, 'ICompositionRectangleGeometry')
make_head(_module, 'ICompositionRoundedRectangleGeometry')
make_head(_module, 'ICompositionScopedBatch')
make_head(_module, 'ICompositionShadow')
make_head(_module, 'ICompositionShadowFactory')
make_head(_module, 'ICompositionShape')
make_head(_module, 'ICompositionShapeFactory')
make_head(_module, 'ICompositionSpriteShape')
make_head(_module, 'ICompositionSupportsSystemBackdrop')
make_head(_module, 'ICompositionSurface')
make_head(_module, 'ICompositionSurfaceBrush')
make_head(_module, 'ICompositionSurfaceBrush2')
make_head(_module, 'ICompositionSurfaceBrush3')
make_head(_module, 'ICompositionSurfaceFacade')
make_head(_module, 'ICompositionTarget')
make_head(_module, 'ICompositionTargetFactory')
make_head(_module, 'ICompositionTransform')
make_head(_module, 'ICompositionTransformFactory')
make_head(_module, 'ICompositionViewBox')
make_head(_module, 'ICompositionVirtualDrawingSurface')
make_head(_module, 'ICompositionVirtualDrawingSurfaceFactory')
make_head(_module, 'ICompositionVisualSurface')
make_head(_module, 'ICompositor')
make_head(_module, 'ICompositor2')
make_head(_module, 'ICompositor3')
make_head(_module, 'ICompositor4')
make_head(_module, 'ICompositor5')
make_head(_module, 'ICompositor6')
make_head(_module, 'ICompositor7')
make_head(_module, 'ICompositor8')
make_head(_module, 'ICompositorStatics')
make_head(_module, 'ICompositorWithBlurredWallpaperBackdropBrush')
make_head(_module, 'ICompositorWithProjectedShadow')
make_head(_module, 'ICompositorWithRadialGradient')
make_head(_module, 'ICompositorWithVisualSurface')
make_head(_module, 'IContainerVisual')
make_head(_module, 'IContainerVisualFactory')
make_head(_module, 'ICubicBezierEasingFunction')
make_head(_module, 'IDelegatedInkTrailVisual')
make_head(_module, 'IDelegatedInkTrailVisualStatics')
make_head(_module, 'IDistantLight')
make_head(_module, 'IDistantLight2')
make_head(_module, 'IDropShadow')
make_head(_module, 'IDropShadow2')
make_head(_module, 'IElasticEasingFunction')
make_head(_module, 'IExponentialEasingFunction')
make_head(_module, 'IExpressionAnimation')
make_head(_module, 'IImplicitAnimationCollection')
make_head(_module, 'IInsetClip')
make_head(_module, 'IKeyFrameAnimation')
make_head(_module, 'IKeyFrameAnimation2')
make_head(_module, 'IKeyFrameAnimation3')
make_head(_module, 'IKeyFrameAnimationFactory')
make_head(_module, 'ILayerVisual')
make_head(_module, 'ILayerVisual2')
make_head(_module, 'ILinearEasingFunction')
make_head(_module, 'INaturalMotionAnimation')
make_head(_module, 'INaturalMotionAnimationFactory')
make_head(_module, 'IPathKeyFrameAnimation')
make_head(_module, 'IPointLight')
make_head(_module, 'IPointLight2')
make_head(_module, 'IPointLight3')
make_head(_module, 'IPowerEasingFunction')
make_head(_module, 'IQuaternionKeyFrameAnimation')
make_head(_module, 'IRectangleClip')
make_head(_module, 'IRedirectVisual')
make_head(_module, 'IRenderingDeviceReplacedEventArgs')
make_head(_module, 'IScalarKeyFrameAnimation')
make_head(_module, 'IScalarNaturalMotionAnimation')
make_head(_module, 'IScalarNaturalMotionAnimationFactory')
make_head(_module, 'IShapeVisual')
make_head(_module, 'ISineEasingFunction')
make_head(_module, 'ISpotLight')
make_head(_module, 'ISpotLight2')
make_head(_module, 'ISpotLight3')
make_head(_module, 'ISpringScalarNaturalMotionAnimation')
make_head(_module, 'ISpringVector2NaturalMotionAnimation')
make_head(_module, 'ISpringVector3NaturalMotionAnimation')
make_head(_module, 'ISpriteVisual')
make_head(_module, 'ISpriteVisual2')
make_head(_module, 'IStepEasingFunction')
make_head(_module, 'IVector2KeyFrameAnimation')
make_head(_module, 'IVector2NaturalMotionAnimation')
make_head(_module, 'IVector2NaturalMotionAnimationFactory')
make_head(_module, 'IVector3KeyFrameAnimation')
make_head(_module, 'IVector3NaturalMotionAnimation')
make_head(_module, 'IVector3NaturalMotionAnimationFactory')
make_head(_module, 'IVector4KeyFrameAnimation')
make_head(_module, 'IVisual')
make_head(_module, 'IVisual2')
make_head(_module, 'IVisual3')
make_head(_module, 'IVisual4')
make_head(_module, 'IVisualCollection')
make_head(_module, 'IVisualElement')
make_head(_module, 'IVisualElement2')
make_head(_module, 'IVisualFactory')
make_head(_module, 'IVisualUnorderedCollection')
make_head(_module, 'ImplicitAnimationCollection')
make_head(_module, 'InitialValueExpressionCollection')
make_head(_module, 'InkTrailPoint')
make_head(_module, 'InsetClip')
make_head(_module, 'KeyFrameAnimation')
make_head(_module, 'LayerVisual')
make_head(_module, 'LinearEasingFunction')
make_head(_module, 'NaturalMotionAnimation')
make_head(_module, 'PathKeyFrameAnimation')
make_head(_module, 'PointLight')
make_head(_module, 'PowerEasingFunction')
make_head(_module, 'QuaternionKeyFrameAnimation')
make_head(_module, 'RectangleClip')
make_head(_module, 'RedirectVisual')
make_head(_module, 'RenderingDeviceReplacedEventArgs')
make_head(_module, 'ScalarKeyFrameAnimation')
make_head(_module, 'ScalarNaturalMotionAnimation')
make_head(_module, 'ShapeVisual')
make_head(_module, 'SineEasingFunction')
make_head(_module, 'SpotLight')
make_head(_module, 'SpringScalarNaturalMotionAnimation')
make_head(_module, 'SpringVector2NaturalMotionAnimation')
make_head(_module, 'SpringVector3NaturalMotionAnimation')
make_head(_module, 'SpriteVisual')
make_head(_module, 'StepEasingFunction')
make_head(_module, 'Vector2KeyFrameAnimation')
make_head(_module, 'Vector2NaturalMotionAnimation')
make_head(_module, 'Vector3KeyFrameAnimation')
make_head(_module, 'Vector3NaturalMotionAnimation')
make_head(_module, 'Vector4KeyFrameAnimation')
make_head(_module, 'Visual')
make_head(_module, 'VisualCollection')
make_head(_module, 'VisualUnorderedCollection')
