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
import Windows.Devices.Sms
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
CellularClass = Int32
CellularClass_None: CellularClass = 0
CellularClass_Gsm: CellularClass = 1
CellularClass_Cdma: CellularClass = 2
class DeleteSmsMessageOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.DeleteSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncAction, handler: Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncAction) -> Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class DeleteSmsMessagesOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.DeleteSmsMessagesOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncAction, handler: Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncAction) -> Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class GetSmsDeviceOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]
    _classid_ = 'Windows.Devices.Sms.GetSmsDeviceOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice], handler: Windows.Foundation.AsyncOperationCompletedHandler[Windows.Devices.Sms.SmsDevice]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]) -> Windows.Foundation.AsyncOperationCompletedHandler[Windows.Devices.Sms.SmsDevice]: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]) -> Windows.Devices.Sms.SmsDevice: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class GetSmsMessageOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage]
    _classid_ = 'Windows.Devices.Sms.GetSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage], handler: Windows.Foundation.AsyncOperationCompletedHandler[Windows.Devices.Sms.ISmsMessage]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage]) -> Windows.Foundation.AsyncOperationCompletedHandler[Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage]) -> Windows.Devices.Sms.ISmsMessage: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class GetSmsMessagesOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]
    _classid_ = 'Windows.Devices.Sms.GetSmsMessagesOperation'
    @winrt_mixinmethod
    def put_Progress(self: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32], handler: Windows.Foundation.AsyncOperationProgressHandler[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]) -> Windows.Foundation.AsyncOperationProgressHandler[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32], handler: Windows.Foundation.AsyncOperationWithProgressCompletedHandler[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]) -> Windows.Foundation.AsyncOperationWithProgressCompletedHandler[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Progress = property(get_Progress, put_Progress)
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class ISmsAppMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e8bb8494-d3a0-4a0a-86d7-291033a8cf54}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_CallbackNumber(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CallbackNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IsDeliveryNotificationEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDeliveryNotificationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_RetryAttemptCount(self) -> Int32: ...
    @winrt_commethod(17)
    def put_RetryAttemptCount(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_Encoding(self) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(19)
    def put_Encoding(self, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(20)
    def get_PortNumber(self) -> Int32: ...
    @winrt_commethod(21)
    def put_PortNumber(self, value: Int32) -> Void: ...
    @winrt_commethod(22)
    def get_TeleserviceId(self) -> Int32: ...
    @winrt_commethod(23)
    def put_TeleserviceId(self, value: Int32) -> Void: ...
    @winrt_commethod(24)
    def get_ProtocolId(self) -> Int32: ...
    @winrt_commethod(25)
    def put_ProtocolId(self, value: Int32) -> Void: ...
    @winrt_commethod(26)
    def get_BinaryBody(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(27)
    def put_BinaryBody(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    Encoding = property(get_Encoding, put_Encoding)
    PortNumber = property(get_PortNumber, put_PortNumber)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
class ISmsBinaryMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5bf4e813-3b53-4c6e-b61a-d86a63755650}')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Devices.Sms.SmsDataFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: Windows.Devices.Sms.SmsDataFormat) -> Void: ...
    @winrt_commethod(8)
    def GetData(self) -> c_char_p_no: ...
    @winrt_commethod(9)
    def SetData(self, value: c_char_p_no) -> Void: ...
    Format = property(get_Format, put_Format)
class ISmsBroadcastMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{75aebbf1-e4b7-4874-a09c-2956e592f957}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Channel(self) -> Int32: ...
    @winrt_commethod(10)
    def get_GeographicalScope(self) -> Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_commethod(11)
    def get_MessageCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_UpdateNumber(self) -> Int32: ...
    @winrt_commethod(13)
    def get_BroadcastType(self) -> Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_commethod(14)
    def get_IsEmergencyAlert(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsUserPopupRequested(self) -> Boolean: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    Channel = property(get_Channel, None)
    GeographicalScope = property(get_GeographicalScope, None)
    MessageCode = property(get_MessageCode, None)
    UpdateNumber = property(get_UpdateNumber, None)
    BroadcastType = property(get_BroadcastType, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
class ISmsDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{091791ed-872b-4eec-9c72-ab11627b34ec}')
    @winrt_commethod(6)
    def SendMessageAsync(self, message: Windows.Devices.Sms.ISmsMessage) -> Windows.Devices.Sms.SendSmsMessageOperation: ...
    @winrt_commethod(7)
    def CalculateLength(self, message: Windows.Devices.Sms.SmsTextMessage) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_commethod(8)
    def get_AccountPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(10)
    def get_MessageStore(self) -> Windows.Devices.Sms.SmsDeviceMessageStore: ...
    @winrt_commethod(11)
    def get_DeviceStatus(self) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_commethod(12)
    def add_SmsMessageReceived(self, eventHandler: Windows.Devices.Sms.SmsMessageReceivedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SmsMessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SmsDeviceStatusChanged(self, eventHandler: Windows.Devices.Sms.SmsDeviceStatusChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SmsDeviceStatusChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    MessageStore = property(get_MessageStore, None)
    DeviceStatus = property(get_DeviceStatus, None)
class ISmsDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bd8a5c13-e522-46cb-b8d5-9ead30fb6c47}')
    @winrt_commethod(6)
    def get_SmscAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SmscAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ParentDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AccountPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(12)
    def get_DeviceStatus(self) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_commethod(13)
    def CalculateLength(self, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_commethod(14)
    def SendMessageAndGetResultAsync(self, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_commethod(15)
    def add_DeviceStatusChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsDevice2, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DeviceStatusChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceId = property(get_DeviceId, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
class ISmsDevice2Statics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{65c78325-1031-491e-8fb6-ef9991afe363}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(8)
    def GetDefault(self) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(9)
    def FromParentId(self, parentDeviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
class ISmsDeviceMessageStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9889f253-f188-4427-8d54-ce0c2423c5c1}')
    @winrt_commethod(6)
    def DeleteMessageAsync(self, messageId: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def DeleteMessagesAsync(self, messageFilter: Windows.Devices.Sms.SmsMessageFilter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetMessageAsync(self, messageId: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_commethod(9)
    def GetMessagesAsync(self, messageFilter: Windows.Devices.Sms.SmsMessageFilter) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_commethod(10)
    def get_MaxMessages(self) -> UInt32: ...
    MaxMessages = property(get_MaxMessages, None)
class ISmsDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f88d07ea-d815-4dd1-a234-4520ce4604a4}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
class ISmsDeviceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2ca11c87-0873-4caf-8a7d-bd471e8586d1}')
    @winrt_commethod(6)
    def FromNetworkAccountIdAsync(self, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
class ISmsFilterRule(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{40e32fae-b049-4fbc-afe9-e2a610eff55c}')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_ImsiPrefixes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_DeviceIds(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_SenderNumbers(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_TextMessagePrefixes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PortNumbers(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(12)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(13)
    def put_CellularClass(self, value: Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_commethod(14)
    def get_ProtocolIds(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(15)
    def get_TeleserviceIds(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(16)
    def get_WapApplicationIds(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(17)
    def get_WapContentTypes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(18)
    def get_BroadcastTypes(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_commethod(19)
    def get_BroadcastChannels(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    MessageType = property(get_MessageType, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    DeviceIds = property(get_DeviceIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    PortNumbers = property(get_PortNumbers, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    ProtocolIds = property(get_ProtocolIds, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    BroadcastChannels = property(get_BroadcastChannels, None)
class ISmsFilterRuleFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{00c36508-6296-4f29-9aad-8920ceba3ce8}')
    @winrt_commethod(6)
    def CreateFilterRule(self, messageType: Windows.Devices.Sms.SmsMessageType) -> Windows.Devices.Sms.SmsFilterRule: ...
class ISmsFilterRules(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4e47eafb-79cd-4881-9894-55a4135b23fa}')
    @winrt_commethod(6)
    def get_ActionType(self) -> Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_commethod(7)
    def get_Rules(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
class ISmsFilterRulesFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a09924ed-6e2e-4530-9fde-465d02eed00e}')
    @winrt_commethod(6)
    def CreateFilterRules(self, actionType: Windows.Devices.Sms.SmsFilterActionType) -> Windows.Devices.Sms.SmsFilterRules: ...
class ISmsMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ed3c5e28-6984-4b07-811d-8d5906ed3cea}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MessageClass(self) -> Windows.Devices.Sms.SmsMessageClass: ...
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
class ISmsMessageBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2cf0fe30-fe50-4fc6-aa88-4ccfe27a29ea}')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_MessageClass(self) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_commethod(10)
    def get_SimIccId(self) -> WinRT_String: ...
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class ISmsMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{08e80a98-b8e5-41c1-a3d8-d3abfae22675}')
    @winrt_commethod(6)
    def get_TextMessage(self) -> Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_commethod(7)
    def get_BinaryMessage(self) -> Windows.Devices.Sms.SmsBinaryMessage: ...
    TextMessage = property(get_TextMessage, None)
    BinaryMessage = property(get_BinaryMessage, None)
class ISmsMessageReceivedTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2bcfcbd4-2657-4128-ad5f-e3877132bdb1}')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_TextMessage(self) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_commethod(8)
    def get_WapMessage(self) -> Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_commethod(9)
    def get_AppMessage(self) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_commethod(10)
    def get_BroadcastMessage(self) -> Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_commethod(11)
    def get_VoicemailMessage(self) -> Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_commethod(12)
    def get_StatusMessage(self) -> Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_commethod(13)
    def Drop(self) -> Void: ...
    @winrt_commethod(14)
    def Accept(self) -> Void: ...
    MessageType = property(get_MessageType, None)
    TextMessage = property(get_TextMessage, None)
    WapMessage = property(get_WapMessage, None)
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    StatusMessage = property(get_StatusMessage, None)
class ISmsMessageRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1720503e-f34f-446b-83b3-0ff19923b409}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsMessageRegistration, Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
class ISmsMessageRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{63a05464-2898-4778-a03c-6f994907d63a}')
    @winrt_commethod(6)
    def get_AllRegistrations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_commethod(7)
    def Register(self, id: WinRT_String, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.Devices.Sms.SmsMessageRegistration: ...
    AllRegistrations = property(get_AllRegistrations, None)
class ISmsReceivedEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5bb50f15-e46d-4c82-847d-5a0304c1d53d}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MessageIndex(self) -> UInt32: ...
    DeviceId = property(get_DeviceId, None)
    MessageIndex = property(get_MessageIndex, None)
class ISmsReceivedEventDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{40e05c86-a7b4-4771-9ae7-0b5ffb12c03a}')
    @winrt_commethod(6)
    def get_MessageClass(self) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_commethod(7)
    def get_BinaryMessage(self) -> Windows.Devices.Sms.SmsBinaryMessage: ...
    MessageClass = property(get_MessageClass, None)
    BinaryMessage = property(get_BinaryMessage, None)
class ISmsSendMessageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{db139af2-78c9-4feb-9622-452328088d62}')
    @winrt_commethod(6)
    def get_IsSuccessful(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MessageReferenceNumbers(self) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_ModemErrorCode(self) -> Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_commethod(10)
    def get_IsErrorTransient(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_NetworkCauseCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_TransportFailureCause(self) -> Int32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    CellularClass = property(get_CellularClass, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class ISmsStatusMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6d28342-b70b-4677-9379-c9783fdff8f4}')
    @winrt_commethod(6)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Status(self) -> Int32: ...
    @winrt_commethod(10)
    def get_MessageReferenceNumber(self) -> Int32: ...
    @winrt_commethod(11)
    def get_ServiceCenterTimestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_DischargeTime(self) -> Windows.Foundation.DateTime: ...
    To = property(get_To, None)
    From = property(get_From, None)
    Body = property(get_Body, None)
    Status = property(get_Status, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    DischargeTime = property(get_DischargeTime, None)
class ISmsTextMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d61c904c-a495-487f-9a6f-971548c5bc9f}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PartReferenceId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_PartNumber(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PartCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_From(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Encoding(self) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(17)
    def put_Encoding(self, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(18)
    def ToBinaryMessages(self, format: Windows.Devices.Sms.SmsDataFormat) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsBinaryMessage]: ...
    Timestamp = property(get_Timestamp, None)
    PartReferenceId = property(get_PartReferenceId, None)
    PartNumber = property(get_PartNumber, None)
    PartCount = property(get_PartCount, None)
    To = property(get_To, put_To)
    From = property(get_From, put_From)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
class ISmsTextMessage2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{22a0d893-4555-4755-b5a1-e7fd84955f8d}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Encoding(self) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(13)
    def put_Encoding(self, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(14)
    def get_CallbackNumber(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_CallbackNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_IsDeliveryNotificationEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsDeliveryNotificationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_RetryAttemptCount(self) -> Int32: ...
    @winrt_commethod(19)
    def put_RetryAttemptCount(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_TeleserviceId(self) -> Int32: ...
    @winrt_commethod(21)
    def get_ProtocolId(self) -> Int32: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, None)
    ProtocolId = property(get_ProtocolId, None)
class ISmsTextMessageStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7f68c5ed-3ccc-47a3-8c55-380d3b010892}')
    @winrt_commethod(6)
    def FromBinaryMessage(self, binaryMessage: Windows.Devices.Sms.SmsBinaryMessage) -> Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_commethod(7)
    def FromBinaryData(self, format: Windows.Devices.Sms.SmsDataFormat, value: c_char_p_no) -> Windows.Devices.Sms.SmsTextMessage: ...
class ISmsVoicemailMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{271aa0a6-95b1-44ff-bcb8-b8fdd7e08bc3}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MessageCount(self) -> Windows.Foundation.IReference[Int32]: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    MessageCount = property(get_MessageCount, None)
class ISmsWapMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cd937743-7a55-4d3b-9021-f22e022d09c5}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ApplicationId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_BinaryBody(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Headers(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    From = property(get_From, None)
    ApplicationId = property(get_ApplicationId, None)
    ContentType = property(get_ContentType, None)
    BinaryBody = property(get_BinaryBody, None)
    Headers = property(get_Headers, None)
LegacySmsApiContract: UInt32 = 65536
class SendSmsMessageOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.SendSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncAction, handler: Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncAction) -> Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class SmsAppMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsAppMessage
    _classid_ = 'Windows.Devices.Sms.SmsAppMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsAppMessage) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsAppMessage, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: Windows.Devices.Sms.ISmsAppMessage, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_PortNumber(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_PortNumber(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_TeleserviceId(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_ProtocolId(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_BinaryBody(self: Windows.Devices.Sms.ISmsAppMessage, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    Encoding = property(get_Encoding, put_Encoding)
    PortNumber = property(get_PortNumber, put_PortNumber)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsBinaryMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsBinaryMessage
    _classid_ = 'Windows.Devices.Sms.SmsBinaryMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsBinaryMessage: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Sms.ISmsBinaryMessage) -> Windows.Devices.Sms.SmsDataFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Devices.Sms.ISmsBinaryMessage, value: Windows.Devices.Sms.SmsDataFormat) -> Void: ...
    @winrt_mixinmethod
    def GetData(self: Windows.Devices.Sms.ISmsBinaryMessage) -> c_char_p_no: ...
    @winrt_mixinmethod
    def SetData(self: Windows.Devices.Sms.ISmsBinaryMessage, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Sms.ISmsMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessage) -> Windows.Devices.Sms.SmsMessageClass: ...
    Format = property(get_Format, put_Format)
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
class SmsBroadcastMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsBroadcastMessage
    _classid_ = 'Windows.Devices.Sms.SmsBroadcastMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_GeographicalScope(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_mixinmethod
    def get_MessageCode(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_UpdateNumber(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_BroadcastType(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_mixinmethod
    def get_IsEmergencyAlert(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserPopupRequested(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    Channel = property(get_Channel, None)
    GeographicalScope = property(get_GeographicalScope, None)
    MessageCode = property(get_MessageCode, None)
    UpdateNumber = property(get_UpdateNumber, None)
    BroadcastType = property(get_BroadcastType, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
SmsBroadcastType = Int32
SmsBroadcastType_Other: SmsBroadcastType = 0
SmsBroadcastType_CmasPresidential: SmsBroadcastType = 1
SmsBroadcastType_CmasExtreme: SmsBroadcastType = 2
SmsBroadcastType_CmasSevere: SmsBroadcastType = 3
SmsBroadcastType_CmasAmber: SmsBroadcastType = 4
SmsBroadcastType_CmasTest: SmsBroadcastType = 5
SmsBroadcastType_EUAlert1: SmsBroadcastType = 6
SmsBroadcastType_EUAlert2: SmsBroadcastType = 7
SmsBroadcastType_EUAlert3: SmsBroadcastType = 8
SmsBroadcastType_EUAlertAmber: SmsBroadcastType = 9
SmsBroadcastType_EUAlertInfo: SmsBroadcastType = 10
SmsBroadcastType_EtwsEarthquake: SmsBroadcastType = 11
SmsBroadcastType_EtwsTsunami: SmsBroadcastType = 12
SmsBroadcastType_EtwsTsunamiAndEarthquake: SmsBroadcastType = 13
SmsBroadcastType_LatAlertLocal: SmsBroadcastType = 14
SmsDataFormat = Int32
SmsDataFormat_Unknown: SmsDataFormat = 0
SmsDataFormat_CdmaSubmit: SmsDataFormat = 1
SmsDataFormat_GsmSubmit: SmsDataFormat = 2
SmsDataFormat_CdmaDeliver: SmsDataFormat = 3
SmsDataFormat_GsmDeliver: SmsDataFormat = 4
class SmsDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsDevice
    _classid_ = 'Windows.Devices.Sms.SmsDevice'
    @winrt_mixinmethod
    def SendMessageAsync(self: Windows.Devices.Sms.ISmsDevice, message: Windows.Devices.Sms.ISmsMessage) -> Windows.Devices.Sms.SendSmsMessageOperation: ...
    @winrt_mixinmethod
    def CalculateLength(self: Windows.Devices.Sms.ISmsDevice, message: Windows.Devices.Sms.SmsTextMessage) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_mixinmethod
    def get_AccountPhoneNumber(self: Windows.Devices.Sms.ISmsDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsDevice) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageStore(self: Windows.Devices.Sms.ISmsDevice) -> Windows.Devices.Sms.SmsDeviceMessageStore: ...
    @winrt_mixinmethod
    def get_DeviceStatus(self: Windows.Devices.Sms.ISmsDevice) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_mixinmethod
    def add_SmsMessageReceived(self: Windows.Devices.Sms.ISmsDevice, eventHandler: Windows.Devices.Sms.SmsMessageReceivedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SmsMessageReceived(self: Windows.Devices.Sms.ISmsDevice, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SmsDeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice, eventHandler: Windows.Devices.Sms.SmsDeviceStatusChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SmsDeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FromNetworkAccountIdAsync(cls: Windows.Devices.Sms.ISmsDeviceStatics2, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sms.ISmsDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sms.ISmsDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Sms.ISmsDeviceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsDevice]: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    MessageStore = property(get_MessageStore, None)
    DeviceStatus = property(get_DeviceStatus, None)
class SmsDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsDevice2
    _classid_ = 'Windows.Devices.Sms.SmsDevice2'
    @winrt_mixinmethod
    def get_SmscAddress(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SmscAddress(self: Windows.Devices.Sms.ISmsDevice2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentDeviceId(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccountPhoneNumber(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsDevice2) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_DeviceStatus(self: Windows.Devices.Sms.ISmsDevice2) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_mixinmethod
    def CalculateLength(self: Windows.Devices.Sms.ISmsDevice2, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_mixinmethod
    def SendMessageAndGetResultAsync(self: Windows.Devices.Sms.ISmsDevice2, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_mixinmethod
    def add_DeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsDevice2, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sms.ISmsDevice2Statics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: Windows.Devices.Sms.ISmsDevice2Statics, deviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sms.ISmsDevice2Statics) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def FromParentId(cls: Windows.Devices.Sms.ISmsDevice2Statics, parentDeviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceId = property(get_DeviceId, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
class SmsDeviceMessageStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsDeviceMessageStore
    _classid_ = 'Windows.Devices.Sms.SmsDeviceMessageStore'
    @winrt_mixinmethod
    def DeleteMessageAsync(self: Windows.Devices.Sms.ISmsDeviceMessageStore, messageId: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteMessagesAsync(self: Windows.Devices.Sms.ISmsDeviceMessageStore, messageFilter: Windows.Devices.Sms.SmsMessageFilter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: Windows.Devices.Sms.ISmsDeviceMessageStore, messageId: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def GetMessagesAsync(self: Windows.Devices.Sms.ISmsDeviceMessageStore, messageFilter: Windows.Devices.Sms.SmsMessageFilter) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def get_MaxMessages(self: Windows.Devices.Sms.ISmsDeviceMessageStore) -> UInt32: ...
    MaxMessages = property(get_MaxMessages, None)
SmsDeviceStatus = Int32
SmsDeviceStatus_Off: SmsDeviceStatus = 0
SmsDeviceStatus_Ready: SmsDeviceStatus = 1
SmsDeviceStatus_SimNotInserted: SmsDeviceStatus = 2
SmsDeviceStatus_BadSim: SmsDeviceStatus = 3
SmsDeviceStatus_DeviceFailure: SmsDeviceStatus = 4
SmsDeviceStatus_SubscriptionNotActivated: SmsDeviceStatus = 5
SmsDeviceStatus_DeviceLocked: SmsDeviceStatus = 6
SmsDeviceStatus_DeviceBlocked: SmsDeviceStatus = 7
class SmsDeviceStatusChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{982b1162-3dd7-4618-af89-0c272d5d06d8}')
    _classid_ = 'Windows.Devices.Sms.SmsDeviceStatusChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Devices.Sms.SmsDevice) -> Void: ...
class SmsEncodedLength(EasyCastStructure):
    SegmentCount: UInt32
    CharacterCountLastSegment: UInt32
    CharactersPerSegment: UInt32
    ByteCountLastSegment: UInt32
    BytesPerSegment: UInt32
SmsEncoding = Int32
SmsEncoding_Unknown: SmsEncoding = 0
SmsEncoding_Optimal: SmsEncoding = 1
SmsEncoding_SevenBitAscii: SmsEncoding = 2
SmsEncoding_Unicode: SmsEncoding = 3
SmsEncoding_GsmSevenBit: SmsEncoding = 4
SmsEncoding_EightBit: SmsEncoding = 5
SmsEncoding_Latin: SmsEncoding = 6
SmsEncoding_Korean: SmsEncoding = 7
SmsEncoding_IA5: SmsEncoding = 8
SmsEncoding_ShiftJis: SmsEncoding = 9
SmsEncoding_LatinHebrew: SmsEncoding = 10
SmsFilterActionType = Int32
SmsFilterActionType_AcceptImmediately: SmsFilterActionType = 0
SmsFilterActionType_Drop: SmsFilterActionType = 1
SmsFilterActionType_Peek: SmsFilterActionType = 2
SmsFilterActionType_Accept: SmsFilterActionType = 3
class SmsFilterRule(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsFilterRule
    _classid_ = 'Windows.Devices.Sms.SmsFilterRule'
    @winrt_factorymethod
    def CreateFilterRule(cls: Windows.Devices.Sms.ISmsFilterRuleFactory, messageType: Windows.Devices.Sms.SmsMessageType) -> Windows.Devices.Sms.SmsFilterRule: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_ImsiPrefixes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeviceIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SenderNumbers(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TextMessagePrefixes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PortNumbers(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def put_CellularClass(self: Windows.Devices.Sms.ISmsFilterRule, value: Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_TeleserviceIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_WapApplicationIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_WapContentTypes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_BroadcastTypes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_mixinmethod
    def get_BroadcastChannels(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    MessageType = property(get_MessageType, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    DeviceIds = property(get_DeviceIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    PortNumbers = property(get_PortNumbers, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    ProtocolIds = property(get_ProtocolIds, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    BroadcastChannels = property(get_BroadcastChannels, None)
class SmsFilterRules(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsFilterRules
    _classid_ = 'Windows.Devices.Sms.SmsFilterRules'
    @winrt_factorymethod
    def CreateFilterRules(cls: Windows.Devices.Sms.ISmsFilterRulesFactory, actionType: Windows.Devices.Sms.SmsFilterActionType) -> Windows.Devices.Sms.SmsFilterRules: ...
    @winrt_mixinmethod
    def get_ActionType(self: Windows.Devices.Sms.ISmsFilterRules) -> Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_mixinmethod
    def get_Rules(self: Windows.Devices.Sms.ISmsFilterRules) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
SmsGeographicalScope = Int32
SmsGeographicalScope_None: SmsGeographicalScope = 0
SmsGeographicalScope_CellWithImmediateDisplay: SmsGeographicalScope = 1
SmsGeographicalScope_LocationArea: SmsGeographicalScope = 2
SmsGeographicalScope_Plmn: SmsGeographicalScope = 3
SmsGeographicalScope_Cell: SmsGeographicalScope = 4
SmsMessageClass = Int32
SmsMessageClass_None: SmsMessageClass = 0
SmsMessageClass_Class0: SmsMessageClass = 1
SmsMessageClass_Class1: SmsMessageClass = 2
SmsMessageClass_Class2: SmsMessageClass = 3
SmsMessageClass_Class3: SmsMessageClass = 4
SmsMessageFilter = Int32
SmsMessageFilter_All: SmsMessageFilter = 0
SmsMessageFilter_Unread: SmsMessageFilter = 1
SmsMessageFilter_Read: SmsMessageFilter = 2
SmsMessageFilter_Sent: SmsMessageFilter = 3
SmsMessageFilter_Draft: SmsMessageFilter = 4
class SmsMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsMessageReceivedEventArgs
    _classid_ = 'Windows.Devices.Sms.SmsMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_TextMessage(self: Windows.Devices.Sms.ISmsMessageReceivedEventArgs) -> Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_mixinmethod
    def get_BinaryMessage(self: Windows.Devices.Sms.ISmsMessageReceivedEventArgs) -> Windows.Devices.Sms.SmsBinaryMessage: ...
    TextMessage = property(get_TextMessage, None)
    BinaryMessage = property(get_BinaryMessage, None)
class SmsMessageReceivedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b7ad409-ec2d-47ce-a253-732beeebcacd}')
    _classid_ = 'Windows.Devices.Sms.SmsMessageReceivedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Devices.Sms.SmsDevice, e: Windows.Devices.Sms.SmsMessageReceivedEventArgs) -> Void: ...
class SmsMessageReceivedTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails
    _classid_ = 'Windows.Devices.Sms.SmsMessageReceivedTriggerDetails'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_TextMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_WapMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_mixinmethod
    def get_AppMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_BroadcastMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_mixinmethod
    def get_VoicemailMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_mixinmethod
    def get_StatusMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_mixinmethod
    def Drop(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    @winrt_mixinmethod
    def Accept(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    MessageType = property(get_MessageType, None)
    TextMessage = property(get_TextMessage, None)
    WapMessage = property(get_WapMessage, None)
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    StatusMessage = property(get_StatusMessage, None)
class SmsMessageRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsMessageRegistration
    _classid_ = 'Windows.Devices.Sms.SmsMessageRegistration'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Sms.ISmsMessageRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def Unregister(self: Windows.Devices.Sms.ISmsMessageRegistration) -> Void: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Devices.Sms.ISmsMessageRegistration, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsMessageRegistration, Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Devices.Sms.ISmsMessageRegistration, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllRegistrations(cls: Windows.Devices.Sms.ISmsMessageRegistrationStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_classmethod
    def Register(cls: Windows.Devices.Sms.ISmsMessageRegistrationStatics, id: WinRT_String, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.Devices.Sms.SmsMessageRegistration: ...
    Id = property(get_Id, None)
    AllRegistrations = property(get_AllRegistrations, None)
SmsMessageType = Int32
SmsMessageType_Binary: SmsMessageType = 0
SmsMessageType_Text: SmsMessageType = 1
SmsMessageType_Wap: SmsMessageType = 2
SmsMessageType_App: SmsMessageType = 3
SmsMessageType_Broadcast: SmsMessageType = 4
SmsMessageType_Voicemail: SmsMessageType = 5
SmsMessageType_Status: SmsMessageType = 6
SmsModemErrorCode = Int32
SmsModemErrorCode_Other: SmsModemErrorCode = 0
SmsModemErrorCode_MessagingNetworkError: SmsModemErrorCode = 1
SmsModemErrorCode_SmsOperationNotSupportedByDevice: SmsModemErrorCode = 2
SmsModemErrorCode_SmsServiceNotSupportedByNetwork: SmsModemErrorCode = 3
SmsModemErrorCode_DeviceFailure: SmsModemErrorCode = 4
SmsModemErrorCode_MessageNotEncodedProperly: SmsModemErrorCode = 5
SmsModemErrorCode_MessageTooLarge: SmsModemErrorCode = 6
SmsModemErrorCode_DeviceNotReady: SmsModemErrorCode = 7
SmsModemErrorCode_NetworkNotReady: SmsModemErrorCode = 8
SmsModemErrorCode_InvalidSmscAddress: SmsModemErrorCode = 9
SmsModemErrorCode_NetworkFailure: SmsModemErrorCode = 10
SmsModemErrorCode_FixedDialingNumberRestricted: SmsModemErrorCode = 11
class SmsReceivedEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsReceivedEventDetails
    _classid_ = 'Windows.Devices.Sms.SmsReceivedEventDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsReceivedEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageIndex(self: Windows.Devices.Sms.ISmsReceivedEventDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsReceivedEventDetails2) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_BinaryMessage(self: Windows.Devices.Sms.ISmsReceivedEventDetails2) -> Windows.Devices.Sms.SmsBinaryMessage: ...
    DeviceId = property(get_DeviceId, None)
    MessageIndex = property(get_MessageIndex, None)
    MessageClass = property(get_MessageClass, None)
    BinaryMessage = property(get_BinaryMessage, None)
class SmsSendMessageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsSendMessageResult
    _classid_ = 'Windows.Devices.Sms.SmsSendMessageResult'
    @winrt_mixinmethod
    def get_IsSuccessful(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumbers(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_ModemErrorCode(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_mixinmethod
    def get_IsErrorTransient(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_NetworkCauseCode(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    @winrt_mixinmethod
    def get_TransportFailureCause(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    CellularClass = property(get_CellularClass, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class SmsStatusMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsStatusMessage
    _classid_ = 'Windows.Devices.Sms.SmsStatusMessage'
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumber(self: Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_ServiceCenterTimestamp(self: Windows.Devices.Sms.ISmsStatusMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_DischargeTime(self: Windows.Devices.Sms.ISmsStatusMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    To = property(get_To, None)
    From = property(get_From, None)
    Body = property(get_Body, None)
    Status = property(get_Status, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    DischargeTime = property(get_DischargeTime, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsTextMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsTextMessage
    _classid_ = 'Windows.Devices.Sms.SmsTextMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsTextMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PartReferenceId(self: Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_PartNumber(self: Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_PartCount(self: Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_From(self: Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: Windows.Devices.Sms.ISmsTextMessage) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: Windows.Devices.Sms.ISmsTextMessage, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def ToBinaryMessages(self: Windows.Devices.Sms.ISmsTextMessage, format: Windows.Devices.Sms.SmsDataFormat) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.ISmsBinaryMessage]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Sms.ISmsMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessage) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_classmethod
    def FromBinaryMessage(cls: Windows.Devices.Sms.ISmsTextMessageStatics, binaryMessage: Windows.Devices.Sms.SmsBinaryMessage) -> Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_classmethod
    def FromBinaryData(cls: Windows.Devices.Sms.ISmsTextMessageStatics, format: Windows.Devices.Sms.SmsDataFormat, value: c_char_p_no) -> Windows.Devices.Sms.SmsTextMessage: ...
    Timestamp = property(get_Timestamp, None)
    PartReferenceId = property(get_PartReferenceId, None)
    PartNumber = property(get_PartNumber, None)
    PartCount = property(get_PartCount, None)
    To = property(get_To, put_To)
    From = property(get_From, put_From)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
class SmsTextMessage2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsTextMessage2
    _classid_ = 'Windows.Devices.Sms.SmsTextMessage2'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsTextMessage2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: Windows.Devices.Sms.ISmsTextMessage2) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: Windows.Devices.Sms.ISmsTextMessage2, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsTextMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsTextMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: Windows.Devices.Sms.ISmsTextMessage2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, None)
    ProtocolId = property(get_ProtocolId, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsVoicemailMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsVoicemailMessage
    _classid_ = 'Windows.Devices.Sms.SmsVoicemailMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageCount(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    MessageCount = property(get_MessageCount, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsWapMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sms.ISmsWapMessage
    _classid_ = 'Windows.Devices.Sms.SmsWapMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    From = property(get_From, None)
    ApplicationId = property(get_ApplicationId, None)
    ContentType = property(get_ContentType, None)
    BinaryBody = property(get_BinaryBody, None)
    Headers = property(get_Headers, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
make_head(_module, 'DeleteSmsMessageOperation')
make_head(_module, 'DeleteSmsMessagesOperation')
make_head(_module, 'GetSmsDeviceOperation')
make_head(_module, 'GetSmsMessageOperation')
make_head(_module, 'GetSmsMessagesOperation')
make_head(_module, 'ISmsAppMessage')
make_head(_module, 'ISmsBinaryMessage')
make_head(_module, 'ISmsBroadcastMessage')
make_head(_module, 'ISmsDevice')
make_head(_module, 'ISmsDevice2')
make_head(_module, 'ISmsDevice2Statics')
make_head(_module, 'ISmsDeviceMessageStore')
make_head(_module, 'ISmsDeviceStatics')
make_head(_module, 'ISmsDeviceStatics2')
make_head(_module, 'ISmsFilterRule')
make_head(_module, 'ISmsFilterRuleFactory')
make_head(_module, 'ISmsFilterRules')
make_head(_module, 'ISmsFilterRulesFactory')
make_head(_module, 'ISmsMessage')
make_head(_module, 'ISmsMessageBase')
make_head(_module, 'ISmsMessageReceivedEventArgs')
make_head(_module, 'ISmsMessageReceivedTriggerDetails')
make_head(_module, 'ISmsMessageRegistration')
make_head(_module, 'ISmsMessageRegistrationStatics')
make_head(_module, 'ISmsReceivedEventDetails')
make_head(_module, 'ISmsReceivedEventDetails2')
make_head(_module, 'ISmsSendMessageResult')
make_head(_module, 'ISmsStatusMessage')
make_head(_module, 'ISmsTextMessage')
make_head(_module, 'ISmsTextMessage2')
make_head(_module, 'ISmsTextMessageStatics')
make_head(_module, 'ISmsVoicemailMessage')
make_head(_module, 'ISmsWapMessage')
make_head(_module, 'SendSmsMessageOperation')
make_head(_module, 'SmsAppMessage')
make_head(_module, 'SmsBinaryMessage')
make_head(_module, 'SmsBroadcastMessage')
make_head(_module, 'SmsDevice')
make_head(_module, 'SmsDevice2')
make_head(_module, 'SmsDeviceMessageStore')
make_head(_module, 'SmsDeviceStatusChangedEventHandler')
make_head(_module, 'SmsEncodedLength')
make_head(_module, 'SmsFilterRule')
make_head(_module, 'SmsFilterRules')
make_head(_module, 'SmsMessageReceivedEventArgs')
make_head(_module, 'SmsMessageReceivedEventHandler')
make_head(_module, 'SmsMessageReceivedTriggerDetails')
make_head(_module, 'SmsMessageRegistration')
make_head(_module, 'SmsReceivedEventDetails')
make_head(_module, 'SmsSendMessageResult')
make_head(_module, 'SmsStatusMessage')
make_head(_module, 'SmsTextMessage')
make_head(_module, 'SmsTextMessage2')
make_head(_module, 'SmsVoicemailMessage')
make_head(_module, 'SmsWapMessage')
