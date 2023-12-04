from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization.NumberFormatting
class CurrencyFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter
    _classid_ = 'Windows.Globalization.NumberFormatting.CurrencyFormatter'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter.CreateCurrencyFormatterCode(*args)
        elif len(args) == 3:
            instance = win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter.CreateCurrencyFormatterCodeContext(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateCurrencyFormatterCode(cls: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatterFactory, currencyCode: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter: ...
    @winrt_factorymethod
    def CreateCurrencyFormatterCodeContext(cls: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatterFactory, currencyCode: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter: ...
    @winrt_mixinmethod
    def get_Currency(self: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Currency(self: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter2, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def ParseInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def ParseUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def ParseDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter2) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatterMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter2, value: win32more.Windows.Globalization.NumberFormatting.CurrencyFormatterMode) -> Void: ...
    @winrt_mixinmethod
    def ApplyRoundingForCurrency(self: win32more.Windows.Globalization.NumberFormatting.ICurrencyFormatter2, roundingAlgorithm: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption) -> Int32: ...
    @winrt_mixinmethod
    def put_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption) -> win32more.Windows.Globalization.NumberFormatting.INumberRounder: ...
    @winrt_mixinmethod
    def put_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption, value: win32more.Windows.Globalization.NumberFormatting.INumberRounder) -> Void: ...
    @winrt_mixinmethod
    def get_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption, value: Boolean) -> Void: ...
    Currency = property(get_Currency, put_Currency)
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IntegerDigits = property(get_IntegerDigits, put_IntegerDigits)
    FractionDigits = property(get_FractionDigits, put_FractionDigits)
    IsGrouped = property(get_IsGrouped, put_IsGrouped)
    IsDecimalPointAlwaysDisplayed = property(get_IsDecimalPointAlwaysDisplayed, put_IsDecimalPointAlwaysDisplayed)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    Mode = property(get_Mode, put_Mode)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
    NumberRounder = property(get_NumberRounder, put_NumberRounder)
    IsZeroSigned = property(get_IsZeroSigned, put_IsZeroSigned)
CurrencyFormatterMode = Int32
CurrencyFormatterMode_UseSymbol: CurrencyFormatterMode = 0
CurrencyFormatterMode_UseCurrencyCode: CurrencyFormatterMode = 1
class DecimalFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumberFormatter
    _classid_ = 'Windows.Globalization.NumberFormatting.DecimalFormatter'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.DecimalFormatter.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Globalization.NumberFormatting.DecimalFormatter.CreateDecimalFormatter(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.DecimalFormatter: ...
    @winrt_factorymethod
    def CreateDecimalFormatter(cls: win32more.Windows.Globalization.NumberFormatting.IDecimalFormatterFactory, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.DecimalFormatter: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def ParseInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def ParseUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def ParseDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption) -> Int32: ...
    @winrt_mixinmethod
    def put_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption) -> win32more.Windows.Globalization.NumberFormatting.INumberRounder: ...
    @winrt_mixinmethod
    def put_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption, value: win32more.Windows.Globalization.NumberFormatting.INumberRounder) -> Void: ...
    @winrt_mixinmethod
    def get_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption, value: Boolean) -> Void: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IntegerDigits = property(get_IntegerDigits, put_IntegerDigits)
    FractionDigits = property(get_FractionDigits, put_FractionDigits)
    IsGrouped = property(get_IsGrouped, put_IsGrouped)
    IsDecimalPointAlwaysDisplayed = property(get_IsDecimalPointAlwaysDisplayed, put_IsDecimalPointAlwaysDisplayed)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
    NumberRounder = property(get_NumberRounder, put_NumberRounder)
    IsZeroSigned = property(get_IsZeroSigned, put_IsZeroSigned)
class ICurrencyFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ICurrencyFormatter'
    _iid_ = Guid('{11730ca5-4b00-41b2-b332-73b12a497d54}')
    @winrt_commethod(6)
    def get_Currency(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Currency(self, value: WinRT_String) -> Void: ...
    Currency = property(get_Currency, put_Currency)
class ICurrencyFormatter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ICurrencyFormatter2'
    _iid_ = Guid('{072c2f1d-e7ba-4197-920e-247c92f7dea6}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatterMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.Globalization.NumberFormatting.CurrencyFormatterMode) -> Void: ...
    @winrt_commethod(8)
    def ApplyRoundingForCurrency(self, roundingAlgorithm: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class ICurrencyFormatterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ICurrencyFormatterFactory'
    _iid_ = Guid('{86c7537e-b938-4aa2-84b0-2c33dc5b1450}')
    @winrt_commethod(6)
    def CreateCurrencyFormatterCode(self, currencyCode: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter: ...
    @winrt_commethod(7)
    def CreateCurrencyFormatterCodeContext(self, currencyCode: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.CurrencyFormatter: ...
class IDecimalFormatterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.IDecimalFormatterFactory'
    _iid_ = Guid('{0d018c9a-e393-46b8-b830-7a69c8f89fbb}')
    @winrt_commethod(6)
    def CreateDecimalFormatter(self, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.DecimalFormatter: ...
class IIncrementNumberRounder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.IIncrementNumberRounder'
    _iid_ = Guid('{70a64ff8-66ab-4155-9da1-739e46764543}')
    @winrt_commethod(6)
    def get_RoundingAlgorithm(self) -> win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm: ...
    @winrt_commethod(7)
    def put_RoundingAlgorithm(self, value: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    @winrt_commethod(8)
    def get_Increment(self) -> Double: ...
    @winrt_commethod(9)
    def put_Increment(self, value: Double) -> Void: ...
    RoundingAlgorithm = property(get_RoundingAlgorithm, put_RoundingAlgorithm)
    Increment = property(get_Increment, put_Increment)
class INumberFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberFormatter'
    _iid_ = Guid('{a5007c49-7676-4db7-8631-1b6ff265caa9}')
    @winrt_commethod(6)
    def FormatInt(self, value: Int64) -> WinRT_String: ...
    @winrt_commethod(7)
    def FormatUInt(self, value: UInt64) -> WinRT_String: ...
    @winrt_commethod(8)
    def FormatDouble(self, value: Double) -> WinRT_String: ...
class INumberFormatter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberFormatter2'
    _iid_ = Guid('{d4a8c1f0-80d0-4b0d-a89e-882c1e8f8310}')
    @winrt_commethod(6)
    def FormatInt(self, value: Int64) -> WinRT_String: ...
    @winrt_commethod(7)
    def FormatUInt(self, value: UInt64) -> WinRT_String: ...
    @winrt_commethod(8)
    def FormatDouble(self, value: Double) -> WinRT_String: ...
class INumberFormatterOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberFormatterOptions'
    _iid_ = Guid('{80332d21-aee1-4a39-baa2-07ed8c96daf6}')
    @winrt_commethod(6)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_GeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IntegerDigits(self) -> Int32: ...
    @winrt_commethod(9)
    def put_IntegerDigits(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_FractionDigits(self) -> Int32: ...
    @winrt_commethod(11)
    def put_FractionDigits(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_IsGrouped(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsGrouped(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsDecimalPointAlwaysDisplayed(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDecimalPointAlwaysDisplayed(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_NumeralSystem(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_NumeralSystem(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_ResolvedGeographicRegion(self) -> WinRT_String: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IntegerDigits = property(get_IntegerDigits, put_IntegerDigits)
    FractionDigits = property(get_FractionDigits, put_FractionDigits)
    IsGrouped = property(get_IsGrouped, put_IsGrouped)
    IsDecimalPointAlwaysDisplayed = property(get_IsDecimalPointAlwaysDisplayed, put_IsDecimalPointAlwaysDisplayed)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
class INumberParser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberParser'
    _iid_ = Guid('{e6659412-4a13-4a53-83a1-392fbe4cff9f}')
    @winrt_commethod(6)
    def ParseInt(self, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_commethod(7)
    def ParseUInt(self, text: WinRT_String) -> win32more.Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(8)
    def ParseDouble(self, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Double]: ...
class INumberRounder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberRounder'
    _iid_ = Guid('{5473c375-38ed-4631-b80c-ef34fc48b7f5}')
    @winrt_commethod(6)
    def RoundInt32(self, value: Int32) -> Int32: ...
    @winrt_commethod(7)
    def RoundUInt32(self, value: UInt32) -> UInt32: ...
    @winrt_commethod(8)
    def RoundInt64(self, value: Int64) -> Int64: ...
    @winrt_commethod(9)
    def RoundUInt64(self, value: UInt64) -> UInt64: ...
    @winrt_commethod(10)
    def RoundSingle(self, value: Single) -> Single: ...
    @winrt_commethod(11)
    def RoundDouble(self, value: Double) -> Double: ...
class INumberRounderOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumberRounderOption'
    _iid_ = Guid('{3b088433-646f-4efe-8d48-66eb2e49e736}')
    @winrt_commethod(6)
    def get_NumberRounder(self) -> win32more.Windows.Globalization.NumberFormatting.INumberRounder: ...
    @winrt_commethod(7)
    def put_NumberRounder(self, value: win32more.Windows.Globalization.NumberFormatting.INumberRounder) -> Void: ...
    NumberRounder = property(get_NumberRounder, put_NumberRounder)
class INumeralSystemTranslator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumeralSystemTranslator'
    _iid_ = Guid('{28f5bc2c-8c23-4234-ad2e-fa5a3a426e9b}')
    @winrt_commethod(6)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NumeralSystem(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_NumeralSystem(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TranslateNumerals(self, value: WinRT_String) -> WinRT_String: ...
    Languages = property(get_Languages, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
class INumeralSystemTranslatorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.INumeralSystemTranslatorFactory'
    _iid_ = Guid('{9630c8da-36ef-4d88-a85c-6f0d98d620a6}')
    @winrt_commethod(6)
    def Create(self, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.NumberFormatting.NumeralSystemTranslator: ...
class IPercentFormatterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.IPercentFormatterFactory'
    _iid_ = Guid('{b7828aef-fed4-4018-a6e2-e09961e03765}')
    @winrt_commethod(6)
    def CreatePercentFormatter(self, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.PercentFormatter: ...
class IPermilleFormatterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.IPermilleFormatterFactory'
    _iid_ = Guid('{2b37b4ac-e638-4ed5-a998-62f6b06a49ae}')
    @winrt_commethod(6)
    def CreatePermilleFormatter(self, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.PermilleFormatter: ...
class ISignedZeroOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ISignedZeroOption'
    _iid_ = Guid('{fd1cdd31-0a3c-49c4-a642-96a1564f4f30}')
    @winrt_commethod(6)
    def get_IsZeroSigned(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsZeroSigned(self, value: Boolean) -> Void: ...
    IsZeroSigned = property(get_IsZeroSigned, put_IsZeroSigned)
class ISignificantDigitsNumberRounder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ISignificantDigitsNumberRounder'
    _iid_ = Guid('{f5941bca-6646-4913-8c76-1b191ff94dfd}')
    @winrt_commethod(6)
    def get_RoundingAlgorithm(self) -> win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm: ...
    @winrt_commethod(7)
    def put_RoundingAlgorithm(self, value: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    @winrt_commethod(8)
    def get_SignificantDigits(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_SignificantDigits(self, value: UInt32) -> Void: ...
    RoundingAlgorithm = property(get_RoundingAlgorithm, put_RoundingAlgorithm)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
class ISignificantDigitsOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.NumberFormatting.ISignificantDigitsOption'
    _iid_ = Guid('{1d4dfcdd-2d43-4ee8-bbf1-c1b26a711a58}')
    @winrt_commethod(6)
    def get_SignificantDigits(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SignificantDigits(self, value: Int32) -> Void: ...
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
class IncrementNumberRounder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumberRounder
    _classid_ = 'Windows.Globalization.NumberFormatting.IncrementNumberRounder'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.IncrementNumberRounder.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.IncrementNumberRounder: ...
    @winrt_mixinmethod
    def RoundInt32(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Int32) -> Int32: ...
    @winrt_mixinmethod
    def RoundUInt32(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: UInt32) -> UInt32: ...
    @winrt_mixinmethod
    def RoundInt64(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Int64) -> Int64: ...
    @winrt_mixinmethod
    def RoundUInt64(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: UInt64) -> UInt64: ...
    @winrt_mixinmethod
    def RoundSingle(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Single) -> Single: ...
    @winrt_mixinmethod
    def RoundDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Double) -> Double: ...
    @winrt_mixinmethod
    def get_RoundingAlgorithm(self: win32more.Windows.Globalization.NumberFormatting.IIncrementNumberRounder) -> win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm: ...
    @winrt_mixinmethod
    def put_RoundingAlgorithm(self: win32more.Windows.Globalization.NumberFormatting.IIncrementNumberRounder, value: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_Increment(self: win32more.Windows.Globalization.NumberFormatting.IIncrementNumberRounder) -> Double: ...
    @winrt_mixinmethod
    def put_Increment(self: win32more.Windows.Globalization.NumberFormatting.IIncrementNumberRounder, value: Double) -> Void: ...
    RoundingAlgorithm = property(get_RoundingAlgorithm, put_RoundingAlgorithm)
    Increment = property(get_Increment, put_Increment)
class NumeralSystemTranslator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator
    _classid_ = 'Windows.Globalization.NumberFormatting.NumeralSystemTranslator'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.NumeralSystemTranslator.CreateInstance(*args)
        elif len(args) == 1:
            instance = win32more.Windows.Globalization.NumberFormatting.NumeralSystemTranslator.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.NumeralSystemTranslator: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslatorFactory, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.NumberFormatting.NumeralSystemTranslator: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TranslateNumerals(self: win32more.Windows.Globalization.NumberFormatting.INumeralSystemTranslator, value: WinRT_String) -> WinRT_String: ...
    Languages = property(get_Languages, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
class PercentFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumberFormatter
    _classid_ = 'Windows.Globalization.NumberFormatting.PercentFormatter'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.PercentFormatter.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Globalization.NumberFormatting.PercentFormatter.CreatePercentFormatter(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.PercentFormatter: ...
    @winrt_factorymethod
    def CreatePercentFormatter(cls: win32more.Windows.Globalization.NumberFormatting.IPercentFormatterFactory, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.PercentFormatter: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def ParseInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def ParseUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def ParseDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption) -> Int32: ...
    @winrt_mixinmethod
    def put_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption) -> win32more.Windows.Globalization.NumberFormatting.INumberRounder: ...
    @winrt_mixinmethod
    def put_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption, value: win32more.Windows.Globalization.NumberFormatting.INumberRounder) -> Void: ...
    @winrt_mixinmethod
    def get_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption, value: Boolean) -> Void: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IntegerDigits = property(get_IntegerDigits, put_IntegerDigits)
    FractionDigits = property(get_FractionDigits, put_FractionDigits)
    IsGrouped = property(get_IsGrouped, put_IsGrouped)
    IsDecimalPointAlwaysDisplayed = property(get_IsDecimalPointAlwaysDisplayed, put_IsDecimalPointAlwaysDisplayed)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
    NumberRounder = property(get_NumberRounder, put_NumberRounder)
    IsZeroSigned = property(get_IsZeroSigned, put_IsZeroSigned)
class PermilleFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumberFormatter
    _classid_ = 'Windows.Globalization.NumberFormatting.PermilleFormatter'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.PermilleFormatter.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Globalization.NumberFormatting.PermilleFormatter.CreatePermilleFormatter(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.PermilleFormatter: ...
    @winrt_factorymethod
    def CreatePermilleFormatter(cls: win32more.Windows.Globalization.NumberFormatting.IPermilleFormatterFactory, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String) -> win32more.Windows.Globalization.NumberFormatting.PermilleFormatter: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_IntegerDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_FractionDigits(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGrouped(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecimalPointAlwaysDisplayed(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatterOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Int64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: UInt64) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberFormatter, value: Double) -> WinRT_String: ...
    @winrt_mixinmethod
    def ParseInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def ParseUInt(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def ParseDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberParser, text: WinRT_String) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption) -> Int32: ...
    @winrt_mixinmethod
    def put_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsOption, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption) -> win32more.Windows.Globalization.NumberFormatting.INumberRounder: ...
    @winrt_mixinmethod
    def put_NumberRounder(self: win32more.Windows.Globalization.NumberFormatting.INumberRounderOption, value: win32more.Windows.Globalization.NumberFormatting.INumberRounder) -> Void: ...
    @winrt_mixinmethod
    def get_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsZeroSigned(self: win32more.Windows.Globalization.NumberFormatting.ISignedZeroOption, value: Boolean) -> Void: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IntegerDigits = property(get_IntegerDigits, put_IntegerDigits)
    FractionDigits = property(get_FractionDigits, put_FractionDigits)
    IsGrouped = property(get_IsGrouped, put_IsGrouped)
    IsDecimalPointAlwaysDisplayed = property(get_IsDecimalPointAlwaysDisplayed, put_IsDecimalPointAlwaysDisplayed)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
    NumberRounder = property(get_NumberRounder, put_NumberRounder)
    IsZeroSigned = property(get_IsZeroSigned, put_IsZeroSigned)
RoundingAlgorithm = Int32
RoundingAlgorithm_None: RoundingAlgorithm = 0
RoundingAlgorithm_RoundDown: RoundingAlgorithm = 1
RoundingAlgorithm_RoundUp: RoundingAlgorithm = 2
RoundingAlgorithm_RoundTowardsZero: RoundingAlgorithm = 3
RoundingAlgorithm_RoundAwayFromZero: RoundingAlgorithm = 4
RoundingAlgorithm_RoundHalfDown: RoundingAlgorithm = 5
RoundingAlgorithm_RoundHalfUp: RoundingAlgorithm = 6
RoundingAlgorithm_RoundHalfTowardsZero: RoundingAlgorithm = 7
RoundingAlgorithm_RoundHalfAwayFromZero: RoundingAlgorithm = 8
RoundingAlgorithm_RoundHalfToEven: RoundingAlgorithm = 9
RoundingAlgorithm_RoundHalfToOdd: RoundingAlgorithm = 10
class SignificantDigitsNumberRounder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.NumberFormatting.INumberRounder
    _classid_ = 'Windows.Globalization.NumberFormatting.SignificantDigitsNumberRounder'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Globalization.NumberFormatting.SignificantDigitsNumberRounder.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.NumberFormatting.SignificantDigitsNumberRounder: ...
    @winrt_mixinmethod
    def RoundInt32(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Int32) -> Int32: ...
    @winrt_mixinmethod
    def RoundUInt32(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: UInt32) -> UInt32: ...
    @winrt_mixinmethod
    def RoundInt64(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Int64) -> Int64: ...
    @winrt_mixinmethod
    def RoundUInt64(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: UInt64) -> UInt64: ...
    @winrt_mixinmethod
    def RoundSingle(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Single) -> Single: ...
    @winrt_mixinmethod
    def RoundDouble(self: win32more.Windows.Globalization.NumberFormatting.INumberRounder, value: Double) -> Double: ...
    @winrt_mixinmethod
    def get_RoundingAlgorithm(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsNumberRounder) -> win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm: ...
    @winrt_mixinmethod
    def put_RoundingAlgorithm(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsNumberRounder, value: win32more.Windows.Globalization.NumberFormatting.RoundingAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsNumberRounder) -> UInt32: ...
    @winrt_mixinmethod
    def put_SignificantDigits(self: win32more.Windows.Globalization.NumberFormatting.ISignificantDigitsNumberRounder, value: UInt32) -> Void: ...
    RoundingAlgorithm = property(get_RoundingAlgorithm, put_RoundingAlgorithm)
    SignificantDigits = property(get_SignificantDigits, put_SignificantDigits)
make_ready(__name__)
