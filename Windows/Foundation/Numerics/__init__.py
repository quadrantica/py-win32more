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
import Windows.Foundation.Numerics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Matrix3x2(EasyCastStructure):
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
class Matrix4x4(EasyCastStructure):
    M11: Single
    M12: Single
    M13: Single
    M14: Single
    M21: Single
    M22: Single
    M23: Single
    M24: Single
    M31: Single
    M32: Single
    M33: Single
    M34: Single
    M41: Single
    M42: Single
    M43: Single
    M44: Single
class Plane(EasyCastStructure):
    Normal: Windows.Foundation.Numerics.Vector3
    D: Single
class Quaternion(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class Rational(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
class Vector2(EasyCastStructure):
    X: Single
    Y: Single
class Vector3(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
class Vector4(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
    W: Single
make_head(_module, 'Matrix3x2')
make_head(_module, 'Matrix4x4')
make_head(_module, 'Plane')
make_head(_module, 'Quaternion')
make_head(_module, 'Rational')
make_head(_module, 'Vector2')
make_head(_module, 'Vector3')
make_head(_module, 'Vector4')
