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
import Windows.Security.Authentication.Identity.Provider
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
class ISecondaryAuthenticationFactorAuthentication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{020a16e5-6a25-40a3-8c00-50a023f619d1}')
    @winrt_commethod(6)
    def get_ServiceAuthenticationHmac(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_SessionNonce(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_DeviceNonce(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_DeviceConfigurationData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def FinishAuthenticationAsync(self, deviceHmac: Windows.Storage.Streams.IBuffer, sessionHmac: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorFinishAuthenticationStatus]: ...
    @winrt_commethod(11)
    def AbortAuthenticationAsync(self, errorLogMessage: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
    DeviceNonce = property(get_DeviceNonce, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
class ISecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9cbb5987-ef6d-4bc2-bf49-4617515a0f9a}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_commethod(7)
    def get_Authentication(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Status = property(get_Status, None)
    Authentication = property(get_Authentication, None)
class ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d4a5ee56-7291-4073-bc1f-ccb8f5afdf96}')
    @winrt_commethod(6)
    def get_StageInfo(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo: ...
    StageInfo = property(get_StageInfo, None)
class ISecondaryAuthenticationFactorAuthenticationStageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{56fec28b-e8aa-4c0f-8e4c-a559e73add88}')
    @winrt_commethod(6)
    def get_Stage(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStage: ...
    @winrt_commethod(7)
    def get_Scenario(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationScenario: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    Stage = property(get_Stage, None)
    Scenario = property(get_Scenario, None)
    DeviceId = property(get_DeviceId, None)
class ISecondaryAuthenticationFactorAuthenticationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3f582656-28f8-4e0f-ae8c-5898b9ae2469}')
    @winrt_commethod(6)
    def ShowNotificationMessageAsync(self, deviceName: WinRT_String, message: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StartAuthenticationAsync(self, deviceId: WinRT_String, serviceAuthenticationNonce: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult]: ...
    @winrt_commethod(8)
    def add_AuthenticationStageChanged(self, handler: Windows.Foundation.EventHandler[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AuthenticationStageChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetAuthenticationStageInfoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo]: ...
class ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{90499a19-7ef2-4523-951c-a417a24acf93}')
    @winrt_commethod(6)
    def RegisterDevicePresenceMonitoringAsync(self, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_commethod(7)
    def RegisterDevicePresenceMonitoringWithNewDeviceAsync(self, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_commethod(8)
    def UnregisterDevicePresenceMonitoringAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def IsDevicePresenceMonitoringSupported(self) -> Boolean: ...
class ISecondaryAuthenticationFactorInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1e2ba861-8533-4fce-839b-ecb72410ac14}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DeviceModelNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DeviceConfigurationData(self) -> Windows.Storage.Streams.IBuffer: ...
    DeviceId = property(get_DeviceId, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
class ISecondaryAuthenticationFactorInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{14d981a3-fc26-4ff7-abc3-48e82a512a0a}')
    @winrt_commethod(6)
    def get_PresenceMonitoringMode(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode: ...
    @winrt_commethod(7)
    def UpdateDevicePresenceAsync(self, presenceState: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresence) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_IsAuthenticationSupported(self) -> Boolean: ...
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
class ISecondaryAuthenticationFactorRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9f4cbbb4-8cba-48b0-840d-dbb22a54c678}')
    @winrt_commethod(6)
    def FinishRegisteringDeviceAsync(self, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def AbortRegisteringDeviceAsync(self, errorLogMessage: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class ISecondaryAuthenticationFactorRegistrationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a4fe35f0-ade3-4981-af6b-ec195921682a}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationStatus: ...
    @winrt_commethod(7)
    def get_Registration(self) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration: ...
    Status = property(get_Status, None)
    Registration = property(get_Registration, None)
class ISecondaryAuthenticationFactorRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1adf0f65-e3b7-4155-997f-b756ef65beba}')
    @winrt_commethod(6)
    def RequestStartRegisteringDeviceAsync(self, deviceId: WinRT_String, capabilities: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceCapabilities, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceKey: Windows.Storage.Streams.IBuffer, mutualAuthenticationKey: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult]: ...
    @winrt_commethod(7)
    def FindAllRegisteredDeviceInfoAsync(self, queryType: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceFindScope) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo]]: ...
    @winrt_commethod(8)
    def UnregisterDeviceAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UpdateDeviceConfigurationDataAsync(self, deviceId: WinRT_String, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
class SecondaryAuthenticationFactorAuthentication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication'
    @winrt_mixinmethod
    def get_ServiceAuthenticationHmac(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_SessionNonce(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DeviceNonce(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DeviceConfigurationData(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def FinishAuthenticationAsync(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication, deviceHmac: Windows.Storage.Streams.IBuffer, sessionHmac: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorFinishAuthenticationStatus]: ...
    @winrt_mixinmethod
    def AbortAuthenticationAsync(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication, errorLogMessage: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowNotificationMessageAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, deviceName: WinRT_String, message: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def StartAuthenticationAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, deviceId: WinRT_String, serviceAuthenticationNonce: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult]: ...
    @winrt_classmethod
    def add_AuthenticationStageChanged(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, handler: Windows.Foundation.EventHandler[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AuthenticationStageChanged(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetAuthenticationStageInfoAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo]: ...
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
    DeviceNonce = property(get_DeviceNonce, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
SecondaryAuthenticationFactorAuthenticationMessage = Int32
SecondaryAuthenticationFactorAuthenticationMessage_Invalid: SecondaryAuthenticationFactorAuthenticationMessage = 0
SecondaryAuthenticationFactorAuthenticationMessage_SwipeUpWelcome: SecondaryAuthenticationFactorAuthenticationMessage = 1
SecondaryAuthenticationFactorAuthenticationMessage_TapWelcome: SecondaryAuthenticationFactorAuthenticationMessage = 2
SecondaryAuthenticationFactorAuthenticationMessage_DeviceNeedsAttention: SecondaryAuthenticationFactorAuthenticationMessage = 3
SecondaryAuthenticationFactorAuthenticationMessage_LookingForDevice: SecondaryAuthenticationFactorAuthenticationMessage = 4
SecondaryAuthenticationFactorAuthenticationMessage_LookingForDevicePluggedin: SecondaryAuthenticationFactorAuthenticationMessage = 5
SecondaryAuthenticationFactorAuthenticationMessage_BluetoothIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 6
SecondaryAuthenticationFactorAuthenticationMessage_NfcIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 7
SecondaryAuthenticationFactorAuthenticationMessage_WiFiIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 8
SecondaryAuthenticationFactorAuthenticationMessage_ExtraTapIsRequired: SecondaryAuthenticationFactorAuthenticationMessage = 9
SecondaryAuthenticationFactorAuthenticationMessage_DisabledByPolicy: SecondaryAuthenticationFactorAuthenticationMessage = 10
SecondaryAuthenticationFactorAuthenticationMessage_TapOnDeviceRequired: SecondaryAuthenticationFactorAuthenticationMessage = 11
SecondaryAuthenticationFactorAuthenticationMessage_HoldFinger: SecondaryAuthenticationFactorAuthenticationMessage = 12
SecondaryAuthenticationFactorAuthenticationMessage_ScanFinger: SecondaryAuthenticationFactorAuthenticationMessage = 13
SecondaryAuthenticationFactorAuthenticationMessage_UnauthorizedUser: SecondaryAuthenticationFactorAuthenticationMessage = 14
SecondaryAuthenticationFactorAuthenticationMessage_ReregisterRequired: SecondaryAuthenticationFactorAuthenticationMessage = 15
SecondaryAuthenticationFactorAuthenticationMessage_TryAgain: SecondaryAuthenticationFactorAuthenticationMessage = 16
SecondaryAuthenticationFactorAuthenticationMessage_SayPassphrase: SecondaryAuthenticationFactorAuthenticationMessage = 17
SecondaryAuthenticationFactorAuthenticationMessage_ReadyToSignIn: SecondaryAuthenticationFactorAuthenticationMessage = 18
SecondaryAuthenticationFactorAuthenticationMessage_UseAnotherSignInOption: SecondaryAuthenticationFactorAuthenticationMessage = 19
SecondaryAuthenticationFactorAuthenticationMessage_ConnectionRequired: SecondaryAuthenticationFactorAuthenticationMessage = 20
SecondaryAuthenticationFactorAuthenticationMessage_TimeLimitExceeded: SecondaryAuthenticationFactorAuthenticationMessage = 21
SecondaryAuthenticationFactorAuthenticationMessage_CanceledByUser: SecondaryAuthenticationFactorAuthenticationMessage = 22
SecondaryAuthenticationFactorAuthenticationMessage_CenterHand: SecondaryAuthenticationFactorAuthenticationMessage = 23
SecondaryAuthenticationFactorAuthenticationMessage_MoveHandCloser: SecondaryAuthenticationFactorAuthenticationMessage = 24
SecondaryAuthenticationFactorAuthenticationMessage_MoveHandFarther: SecondaryAuthenticationFactorAuthenticationMessage = 25
SecondaryAuthenticationFactorAuthenticationMessage_PlaceHandAbove: SecondaryAuthenticationFactorAuthenticationMessage = 26
SecondaryAuthenticationFactorAuthenticationMessage_RecognitionFailed: SecondaryAuthenticationFactorAuthenticationMessage = 27
SecondaryAuthenticationFactorAuthenticationMessage_DeviceUnavailable: SecondaryAuthenticationFactorAuthenticationMessage = 28
class SecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_Authentication(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Status = property(get_Status, None)
    Authentication = property(get_Authentication, None)
SecondaryAuthenticationFactorAuthenticationScenario = Int32
SecondaryAuthenticationFactorAuthenticationScenario_SignIn: SecondaryAuthenticationFactorAuthenticationScenario = 0
SecondaryAuthenticationFactorAuthenticationScenario_CredentialPrompt: SecondaryAuthenticationFactorAuthenticationScenario = 1
SecondaryAuthenticationFactorAuthenticationStage = Int32
SecondaryAuthenticationFactorAuthenticationStage_NotStarted: SecondaryAuthenticationFactorAuthenticationStage = 0
SecondaryAuthenticationFactorAuthenticationStage_WaitingForUserConfirmation: SecondaryAuthenticationFactorAuthenticationStage = 1
SecondaryAuthenticationFactorAuthenticationStage_CollectingCredential: SecondaryAuthenticationFactorAuthenticationStage = 2
SecondaryAuthenticationFactorAuthenticationStage_SuspendingAuthentication: SecondaryAuthenticationFactorAuthenticationStage = 3
SecondaryAuthenticationFactorAuthenticationStage_CredentialCollected: SecondaryAuthenticationFactorAuthenticationStage = 4
SecondaryAuthenticationFactorAuthenticationStage_CredentialAuthenticated: SecondaryAuthenticationFactorAuthenticationStage = 5
SecondaryAuthenticationFactorAuthenticationStage_StoppingAuthentication: SecondaryAuthenticationFactorAuthenticationStage = 6
SecondaryAuthenticationFactorAuthenticationStage_ReadyForLock: SecondaryAuthenticationFactorAuthenticationStage = 7
SecondaryAuthenticationFactorAuthenticationStage_CheckingDevicePresence: SecondaryAuthenticationFactorAuthenticationStage = 8
class SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs'
    @winrt_mixinmethod
    def get_StageInfo(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo: ...
    StageInfo = property(get_StageInfo, None)
class SecondaryAuthenticationFactorAuthenticationStageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo'
    @winrt_mixinmethod
    def get_Stage(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStage: ...
    @winrt_mixinmethod
    def get_Scenario(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationScenario: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> WinRT_String: ...
    Stage = property(get_Stage, None)
    Scenario = property(get_Scenario, None)
    DeviceId = property(get_DeviceId, None)
SecondaryAuthenticationFactorAuthenticationStatus = Int32
SecondaryAuthenticationFactorAuthenticationStatus_Failed: SecondaryAuthenticationFactorAuthenticationStatus = 0
SecondaryAuthenticationFactorAuthenticationStatus_Started: SecondaryAuthenticationFactorAuthenticationStatus = 1
SecondaryAuthenticationFactorAuthenticationStatus_UnknownDevice: SecondaryAuthenticationFactorAuthenticationStatus = 2
SecondaryAuthenticationFactorAuthenticationStatus_DisabledByPolicy: SecondaryAuthenticationFactorAuthenticationStatus = 3
SecondaryAuthenticationFactorAuthenticationStatus_InvalidAuthenticationStage: SecondaryAuthenticationFactorAuthenticationStatus = 4
SecondaryAuthenticationFactorDeviceCapabilities = UInt32
SecondaryAuthenticationFactorDeviceCapabilities_None: SecondaryAuthenticationFactorDeviceCapabilities = 0
SecondaryAuthenticationFactorDeviceCapabilities_SecureStorage: SecondaryAuthenticationFactorDeviceCapabilities = 1
SecondaryAuthenticationFactorDeviceCapabilities_StoreKeys: SecondaryAuthenticationFactorDeviceCapabilities = 2
SecondaryAuthenticationFactorDeviceCapabilities_ConfirmUserIntentToAuthenticate: SecondaryAuthenticationFactorDeviceCapabilities = 4
SecondaryAuthenticationFactorDeviceCapabilities_SupportSecureUserPresenceCheck: SecondaryAuthenticationFactorDeviceCapabilities = 8
SecondaryAuthenticationFactorDeviceCapabilities_TransmittedDataIsEncrypted: SecondaryAuthenticationFactorDeviceCapabilities = 16
SecondaryAuthenticationFactorDeviceCapabilities_HMacSha256: SecondaryAuthenticationFactorDeviceCapabilities = 32
SecondaryAuthenticationFactorDeviceCapabilities_CloseRangeDataTransmission: SecondaryAuthenticationFactorDeviceCapabilities = 64
SecondaryAuthenticationFactorDeviceFindScope = Int32
SecondaryAuthenticationFactorDeviceFindScope_User: SecondaryAuthenticationFactorDeviceFindScope = 0
SecondaryAuthenticationFactorDeviceFindScope_AllUsers: SecondaryAuthenticationFactorDeviceFindScope = 1
SecondaryAuthenticationFactorDevicePresence = Int32
SecondaryAuthenticationFactorDevicePresence_Absent: SecondaryAuthenticationFactorDevicePresence = 0
SecondaryAuthenticationFactorDevicePresence_Present: SecondaryAuthenticationFactorDevicePresence = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringMode = Int32
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_Unsupported: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 0
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_AppManaged: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_SystemManaged: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 2
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = Int32
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_Unsupported: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 0
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_Succeeded: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_DisabledByPolicy: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 2
SecondaryAuthenticationFactorFinishAuthenticationStatus = Int32
SecondaryAuthenticationFactorFinishAuthenticationStatus_Failed: SecondaryAuthenticationFactorFinishAuthenticationStatus = 0
SecondaryAuthenticationFactorFinishAuthenticationStatus_Completed: SecondaryAuthenticationFactorFinishAuthenticationStatus = 1
SecondaryAuthenticationFactorFinishAuthenticationStatus_NonceExpired: SecondaryAuthenticationFactorFinishAuthenticationStatus = 2
class SecondaryAuthenticationFactorInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceFriendlyName(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceModelNumber(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceConfigurationData(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_PresenceMonitoringMode(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode: ...
    @winrt_mixinmethod
    def UpdateDevicePresenceAsync(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2, presenceState: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresence) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_IsAuthenticationSupported(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2) -> Boolean: ...
    DeviceId = property(get_DeviceId, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
class SecondaryAuthenticationFactorRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration'
    @winrt_mixinmethod
    def FinishRegisteringDeviceAsync(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AbortRegisteringDeviceAsync(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration, errorLogMessage: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RegisterDevicePresenceMonitoringAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_classmethod
    def RegisterDevicePresenceMonitoringWithNewDeviceAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_classmethod
    def UnregisterDevicePresenceMonitoringAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def IsDevicePresenceMonitoringSupported(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics) -> Boolean: ...
    @winrt_classmethod
    def RequestStartRegisteringDeviceAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String, capabilities: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceCapabilities, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceKey: Windows.Storage.Streams.IBuffer, mutualAuthenticationKey: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult]: ...
    @winrt_classmethod
    def FindAllRegisteredDeviceInfoAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, queryType: Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceFindScope) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo]]: ...
    @winrt_classmethod
    def UnregisterDeviceAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def UpdateDeviceConfigurationDataAsync(cls: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String, deviceConfigurationData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
class SecondaryAuthenticationFactorRegistrationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationStatus: ...
    @winrt_mixinmethod
    def get_Registration(self: Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult) -> Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration: ...
    Status = property(get_Status, None)
    Registration = property(get_Registration, None)
SecondaryAuthenticationFactorRegistrationStatus = Int32
SecondaryAuthenticationFactorRegistrationStatus_Failed: SecondaryAuthenticationFactorRegistrationStatus = 0
SecondaryAuthenticationFactorRegistrationStatus_Started: SecondaryAuthenticationFactorRegistrationStatus = 1
SecondaryAuthenticationFactorRegistrationStatus_CanceledByUser: SecondaryAuthenticationFactorRegistrationStatus = 2
SecondaryAuthenticationFactorRegistrationStatus_PinSetupRequired: SecondaryAuthenticationFactorRegistrationStatus = 3
SecondaryAuthenticationFactorRegistrationStatus_DisabledByPolicy: SecondaryAuthenticationFactorRegistrationStatus = 4
make_head(_module, 'ISecondaryAuthenticationFactorAuthentication')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationResult')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStageInfo')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStatics')
make_head(_module, 'ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics')
make_head(_module, 'ISecondaryAuthenticationFactorInfo')
make_head(_module, 'ISecondaryAuthenticationFactorInfo2')
make_head(_module, 'ISecondaryAuthenticationFactorRegistration')
make_head(_module, 'ISecondaryAuthenticationFactorRegistrationResult')
make_head(_module, 'ISecondaryAuthenticationFactorRegistrationStatics')
make_head(_module, 'SecondaryAuthenticationFactorAuthentication')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationResult')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationStageInfo')
make_head(_module, 'SecondaryAuthenticationFactorInfo')
make_head(_module, 'SecondaryAuthenticationFactorRegistration')
make_head(_module, 'SecondaryAuthenticationFactorRegistrationResult')
