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
import Windows.Devices.Spi
import Windows.Devices.Spi.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISpiBusInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9929444a-54f2-48c6-b9-52-9c-32-fc-02-c6-69')
    @winrt_commethod(6)
    def get_ChipSelectLineCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_MinClockFrequency(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxClockFrequency(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SupportedDataBitLengths(self) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    ChipSelectLineCount = property(get_ChipSelectLineCount, None)
    MinClockFrequency = property(get_MinClockFrequency, None)
    MaxClockFrequency = property(get_MaxClockFrequency, None)
    SupportedDataBitLengths = property(get_SupportedDataBitLengths, None)
class ISpiConnectionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5283a37f-f935-4b9f-a7-a7-3a-78-90-af-a5-ce')
    @winrt_commethod(6)
    def get_ChipSelectLine(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ChipSelectLine(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Devices.Spi.SpiMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.Devices.Spi.SpiMode) -> Void: ...
    @winrt_commethod(10)
    def get_DataBitLength(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DataBitLength(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_ClockFrequency(self) -> Int32: ...
    @winrt_commethod(13)
    def put_ClockFrequency(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_SharingMode(self) -> Windows.Devices.Spi.SpiSharingMode: ...
    @winrt_commethod(15)
    def put_SharingMode(self, value: Windows.Devices.Spi.SpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    Mode = property(get_Mode, put_Mode)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    SharingMode = property(get_SharingMode, put_SharingMode)
class ISpiConnectionSettingsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ff99081e-10c4-44b7-9f-ea-a7-48-b5-a4-6f-31')
    @winrt_commethod(6)
    def Create(self, chipSelectLine: Int32) -> Windows.Devices.Spi.SpiConnectionSettings: ...
class ISpiController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a8d3c829-9895-4159-a9-34-87-41-f1-ee-6d-27')
    @winrt_commethod(6)
    def GetDevice(self, settings: Windows.Devices.Spi.SpiConnectionSettings) -> Windows.Devices.Spi.SpiDevice: ...
class ISpiControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0d5229e2-138b-4e48-b9-64-4f-2f-79-b9-c5-a2')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Spi.SpiController]: ...
    @winrt_commethod(7)
    def GetControllersAsync(self, provider: Windows.Devices.Spi.Provider.ISpiProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Spi.SpiController]]: ...
class ISpiDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05d5356d-11b6-4d39-84-d5-95-df-b4-c9-f2-ce')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> Windows.Devices.Spi.SpiConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def Read(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def TransferSequential(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(11)
    def TransferFullDuplex(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
class ISpiDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a278e559-5720-4d3f-bd-93-56-f5-ff-5a-58-79')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetBusInfo(self, busId: WinRT_String) -> Windows.Devices.Spi.SpiBusInfo: ...
    @winrt_commethod(9)
    def FromIdAsync(self, busId: WinRT_String, settings: Windows.Devices.Spi.SpiConnectionSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Spi.SpiDevice]: ...
class SpiBusInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Spi.SpiBusInfo'
    @winrt_mixinmethod
    def get_ChipSelectLineCount(self: Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_MinClockFrequency(self: Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxClockFrequency(self: Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_SupportedDataBitLengths(self: Windows.Devices.Spi.ISpiBusInfo) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    ChipSelectLineCount = property(get_ChipSelectLineCount, None)
    MinClockFrequency = property(get_MinClockFrequency, None)
    MaxClockFrequency = property(get_MaxClockFrequency, None)
    SupportedDataBitLengths = property(get_SupportedDataBitLengths, None)
class SpiConnectionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Spi.SpiConnectionSettings'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Spi.ISpiConnectionSettingsFactory, chipSelectLine: Int32) -> Windows.Devices.Spi.SpiConnectionSettings: ...
    @winrt_mixinmethod
    def get_ChipSelectLine(self: Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ChipSelectLine(self: Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Devices.Spi.ISpiConnectionSettings) -> Windows.Devices.Spi.SpiMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Devices.Spi.ISpiConnectionSettings, value: Windows.Devices.Spi.SpiMode) -> Void: ...
    @winrt_mixinmethod
    def get_DataBitLength(self: Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_DataBitLength(self: Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ClockFrequency(self: Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ClockFrequency(self: Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.Spi.ISpiConnectionSettings) -> Windows.Devices.Spi.SpiSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: Windows.Devices.Spi.ISpiConnectionSettings, value: Windows.Devices.Spi.SpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    Mode = property(get_Mode, put_Mode)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    SharingMode = property(get_SharingMode, put_SharingMode)
class SpiController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Spi.SpiController'
    @winrt_mixinmethod
    def GetDevice(self: Windows.Devices.Spi.ISpiController, settings: Windows.Devices.Spi.SpiConnectionSettings) -> Windows.Devices.Spi.SpiDevice: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Spi.ISpiControllerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Spi.SpiController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: Windows.Devices.Spi.ISpiControllerStatics, provider: Windows.Devices.Spi.Provider.ISpiProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Spi.SpiController]]: ...
class SpiDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Spi.SpiDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Spi.ISpiDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionSettings(self: Windows.Devices.Spi.ISpiDevice) -> Windows.Devices.Spi.SpiConnectionSettings: ...
    @winrt_mixinmethod
    def Write(self: Windows.Devices.Spi.ISpiDevice, buffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def Read(self: Windows.Devices.Spi.ISpiDevice, buffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def TransferSequential(self: Windows.Devices.Spi.ISpiDevice, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def TransferFullDuplex(self: Windows.Devices.Spi.ISpiDevice, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Spi.ISpiDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: Windows.Devices.Spi.ISpiDeviceStatics, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetBusInfo(cls: Windows.Devices.Spi.ISpiDeviceStatics, busId: WinRT_String) -> Windows.Devices.Spi.SpiBusInfo: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Spi.ISpiDeviceStatics, busId: WinRT_String, settings: Windows.Devices.Spi.SpiConnectionSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Spi.SpiDevice]: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
SpiMode = Int32
SpiMode_Mode0: SpiMode = 0
SpiMode_Mode1: SpiMode = 1
SpiMode_Mode2: SpiMode = 2
SpiMode_Mode3: SpiMode = 3
SpiSharingMode = Int32
SpiSharingMode_Exclusive: SpiSharingMode = 0
SpiSharingMode_Shared: SpiSharingMode = 1
make_head(_module, 'ISpiBusInfo')
make_head(_module, 'ISpiConnectionSettings')
make_head(_module, 'ISpiConnectionSettingsFactory')
make_head(_module, 'ISpiController')
make_head(_module, 'ISpiControllerStatics')
make_head(_module, 'ISpiDevice')
make_head(_module, 'ISpiDeviceStatics')
make_head(_module, 'SpiBusInfo')
make_head(_module, 'SpiConnectionSettings')
make_head(_module, 'SpiController')
make_head(_module, 'SpiDevice')
