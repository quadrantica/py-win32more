from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.BiometricFramework
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WINBIO_MAX_STRING_LEN: UInt32 = 256
WINBIO_SCP_VERSION_1: UInt32 = 1
WINBIO_SCP_RANDOM_SIZE_V1: UInt32 = 32
WINBIO_SCP_DIGEST_SIZE_V1: UInt32 = 32
WINBIO_SCP_CURVE_FIELD_SIZE_V1: UInt32 = 32
WINBIO_SCP_PUBLIC_KEY_SIZE_V1: UInt32 = 65
WINBIO_SCP_PRIVATE_KEY_SIZE_V1: UInt32 = 32
WINBIO_SCP_SIGNATURE_SIZE_V1: UInt32 = 64
WINBIO_SCP_ENCRYPTION_BLOCK_SIZE_V1: UInt32 = 16
WINBIO_SCP_ENCRYPTION_KEY_SIZE_V1: UInt32 = 32
WINBIO_BIR_ALIGN_SIZE: UInt32 = 8
WINBIO_BIR_ALGIN_SIZE: UInt32 = 8
FACILITY_WINBIO: UInt32 = 9
FACILITY_NONE: UInt32 = 0
WINBIO_E_UNSUPPORTED_FACTOR: win32more.Windows.Win32.Foundation.HRESULT = -2146861055
WINBIO_E_INVALID_UNIT: win32more.Windows.Win32.Foundation.HRESULT = -2146861054
WINBIO_E_UNKNOWN_ID: win32more.Windows.Win32.Foundation.HRESULT = -2146861053
WINBIO_E_CANCELED: win32more.Windows.Win32.Foundation.HRESULT = -2146861052
WINBIO_E_NO_MATCH: win32more.Windows.Win32.Foundation.HRESULT = -2146861051
WINBIO_E_CAPTURE_ABORTED: win32more.Windows.Win32.Foundation.HRESULT = -2146861050
WINBIO_E_ENROLLMENT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2146861049
WINBIO_E_BAD_CAPTURE: win32more.Windows.Win32.Foundation.HRESULT = -2146861048
WINBIO_E_INVALID_CONTROL_CODE: win32more.Windows.Win32.Foundation.HRESULT = -2146861047
WINBIO_E_DATA_COLLECTION_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2146861045
WINBIO_E_UNSUPPORTED_DATA_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2146861044
WINBIO_E_UNSUPPORTED_DATA_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2146861043
WINBIO_E_UNSUPPORTED_PURPOSE: win32more.Windows.Win32.Foundation.HRESULT = -2146861042
WINBIO_E_INVALID_DEVICE_STATE: win32more.Windows.Win32.Foundation.HRESULT = -2146861041
WINBIO_E_DEVICE_BUSY: win32more.Windows.Win32.Foundation.HRESULT = -2146861040
WINBIO_E_DATABASE_CANT_CREATE: win32more.Windows.Win32.Foundation.HRESULT = -2146861039
WINBIO_E_DATABASE_CANT_OPEN: win32more.Windows.Win32.Foundation.HRESULT = -2146861038
WINBIO_E_DATABASE_CANT_CLOSE: win32more.Windows.Win32.Foundation.HRESULT = -2146861037
WINBIO_E_DATABASE_CANT_ERASE: win32more.Windows.Win32.Foundation.HRESULT = -2146861036
WINBIO_E_DATABASE_CANT_FIND: win32more.Windows.Win32.Foundation.HRESULT = -2146861035
WINBIO_E_DATABASE_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2146861034
WINBIO_E_DATABASE_FULL: win32more.Windows.Win32.Foundation.HRESULT = -2146861032
WINBIO_E_DATABASE_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2146861031
WINBIO_E_DATABASE_CORRUPTED: win32more.Windows.Win32.Foundation.HRESULT = -2146861030
WINBIO_E_DATABASE_NO_SUCH_RECORD: win32more.Windows.Win32.Foundation.HRESULT = -2146861029
WINBIO_E_DUPLICATE_ENROLLMENT: win32more.Windows.Win32.Foundation.HRESULT = -2146861028
WINBIO_E_DATABASE_READ_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2146861027
WINBIO_E_DATABASE_WRITE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2146861026
WINBIO_E_DATABASE_NO_RESULTS: win32more.Windows.Win32.Foundation.HRESULT = -2146861025
WINBIO_E_DATABASE_NO_MORE_RECORDS: win32more.Windows.Win32.Foundation.HRESULT = -2146861024
WINBIO_E_DATABASE_EOF: win32more.Windows.Win32.Foundation.HRESULT = -2146861023
WINBIO_E_DATABASE_BAD_INDEX_VECTOR: win32more.Windows.Win32.Foundation.HRESULT = -2146861022
WINBIO_E_INCORRECT_BSP: win32more.Windows.Win32.Foundation.HRESULT = -2146861020
WINBIO_E_INCORRECT_SENSOR_POOL: win32more.Windows.Win32.Foundation.HRESULT = -2146861019
WINBIO_E_NO_CAPTURE_DATA: win32more.Windows.Win32.Foundation.HRESULT = -2146861018
WINBIO_E_INVALID_SENSOR_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2146861017
WINBIO_E_LOCK_VIOLATION: win32more.Windows.Win32.Foundation.HRESULT = -2146861014
WINBIO_E_DUPLICATE_TEMPLATE: win32more.Windows.Win32.Foundation.HRESULT = -2146861013
WINBIO_E_INVALID_OPERATION: win32more.Windows.Win32.Foundation.HRESULT = -2146861012
WINBIO_E_SESSION_BUSY: win32more.Windows.Win32.Foundation.HRESULT = -2146861011
WINBIO_E_CRED_PROV_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146861008
WINBIO_E_CRED_PROV_NO_CREDENTIAL: win32more.Windows.Win32.Foundation.HRESULT = -2146861007
WINBIO_E_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146861006
WINBIO_E_CONFIGURATION_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2146861005
WINBIO_E_SENSOR_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2146861004
WINBIO_E_SAS_ENABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146861003
WINBIO_E_DEVICE_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2146861002
WINBIO_E_FAST_USER_SWITCH_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146861001
WINBIO_E_NOT_ACTIVE_CONSOLE: win32more.Windows.Win32.Foundation.HRESULT = -2146861000
WINBIO_E_EVENT_MONITOR_ACTIVE: win32more.Windows.Win32.Foundation.HRESULT = -2146860999
WINBIO_E_INVALID_PROPERTY_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2146860998
WINBIO_E_INVALID_PROPERTY_ID: win32more.Windows.Win32.Foundation.HRESULT = -2146860997
WINBIO_E_UNSUPPORTED_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2146860996
WINBIO_E_ADAPTER_INTEGRITY_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2146860995
WINBIO_E_INCORRECT_SESSION_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2146860994
WINBIO_E_SESSION_HANDLE_CLOSED: win32more.Windows.Win32.Foundation.HRESULT = -2146860993
WINBIO_E_DEADLOCK_DETECTED: win32more.Windows.Win32.Foundation.HRESULT = -2146860992
WINBIO_E_NO_PREBOOT_IDENTITY: win32more.Windows.Win32.Foundation.HRESULT = -2146860991
WINBIO_E_MAX_ERROR_COUNT_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2146860990
WINBIO_E_AUTO_LOGON_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146860989
WINBIO_E_INVALID_TICKET: win32more.Windows.Win32.Foundation.HRESULT = -2146860988
WINBIO_E_TICKET_QUOTA_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2146860987
WINBIO_E_DATA_PROTECTION_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2146860986
WINBIO_E_CRED_PROV_SECURITY_LOCKOUT: win32more.Windows.Win32.Foundation.HRESULT = -2146860985
WINBIO_E_UNSUPPORTED_POOL_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2146860984
WINBIO_E_SELECTION_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2146860983
WINBIO_E_PRESENCE_MONITOR_ACTIVE: win32more.Windows.Win32.Foundation.HRESULT = -2146860982
WINBIO_E_INVALID_SUBFACTOR: win32more.Windows.Win32.Foundation.HRESULT = -2146860981
WINBIO_E_INVALID_CALIBRATION_FORMAT_ARRAY: win32more.Windows.Win32.Foundation.HRESULT = -2146860980
WINBIO_E_NO_SUPPORTED_CALIBRATION_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2146860979
WINBIO_E_UNSUPPORTED_SENSOR_CALIBRATION_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2146860978
WINBIO_E_CALIBRATION_BUFFER_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2146860977
WINBIO_E_CALIBRATION_BUFFER_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2146860976
WINBIO_E_CALIBRATION_BUFFER_INVALID: win32more.Windows.Win32.Foundation.HRESULT = -2146860975
WINBIO_E_INVALID_KEY_IDENTIFIER: win32more.Windows.Win32.Foundation.HRESULT = -2146860974
WINBIO_E_KEY_CREATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2146860973
WINBIO_E_KEY_IDENTIFIER_BUFFER_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2146860972
WINBIO_E_PROPERTY_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2146860971
WINBIO_E_POLICY_PROTECTION_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2146860970
WINBIO_E_INSECURE_SENSOR: win32more.Windows.Win32.Foundation.HRESULT = -2146860969
WINBIO_E_INVALID_BUFFER_ID: win32more.Windows.Win32.Foundation.HRESULT = -2146860968
WINBIO_E_INVALID_BUFFER: win32more.Windows.Win32.Foundation.HRESULT = -2146860967
WINBIO_E_TRUSTLET_INTEGRITY_FAIL: win32more.Windows.Win32.Foundation.HRESULT = -2146860966
WINBIO_E_ENROLLMENT_CANCELED_BY_SUSPEND: win32more.Windows.Win32.Foundation.HRESULT = -2146860965
WINBIO_I_MORE_DATA: win32more.Windows.Win32.Foundation.HRESULT = 589825
WINBIO_I_EXTENDED_STATUS_INFORMATION: win32more.Windows.Win32.Foundation.HRESULT = 589826
GUID_DEVINTERFACE_BIOMETRIC_READER: Guid = Guid('{e2b5183a-99ea-4cc3-ad6b-80ca8d715b80}')
IOCTL_BIOMETRIC_VENDOR: UInt32 = 4464640
WINBIO_WBDI_MAJOR_VERSION: UInt32 = 1
WINBIO_WBDI_MINOR_VERSION: UInt32 = 0
@winfunctype('winbio.dll')
def WinBioEnumServiceProviders(Factor: UInt32, BspSchemaArray: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)), BspCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumBiometricUnits(Factor: UInt32, UnitSchemaArray: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)), UnitCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumDatabases(Factor: UInt32, StorageSchemaArray: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)), StorageCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncOpenFramework(NotificationMethod: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD, TargetWindow: win32more.Windows.Win32.Foundation.HWND, MessageCode: UInt32, CallbackRoutine: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK, UserData: VoidPtr, AsynchronousOpen: win32more.Windows.Win32.Foundation.BOOL, FrameworkHandle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCloseFramework(FrameworkHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumServiceProviders(FrameworkHandle: UInt32, Factor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumBiometricUnits(FrameworkHandle: UInt32, Factor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumDatabases(FrameworkHandle: UInt32, Factor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncMonitorFrameworkChanges(FrameworkHandle: UInt32, ChangeTypes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioOpenSession(Factor: UInt32, PoolType: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_POOL, Flags: UInt32, UnitArray: POINTER(UInt32), UnitCount: UIntPtr, DatabaseId: POINTER(Guid), SessionHandle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncOpenSession(Factor: UInt32, PoolType: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_POOL, Flags: UInt32, UnitArray: POINTER(UInt32), UnitCount: UIntPtr, DatabaseId: POINTER(Guid), NotificationMethod: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD, TargetWindow: win32more.Windows.Win32.Foundation.HWND, MessageCode: UInt32, CallbackRoutine: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK, UserData: VoidPtr, AsynchronousOpen: win32more.Windows.Win32.Foundation.BOOL, SessionHandle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCloseSession(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioVerify(SessionHandle: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, UnitId: POINTER(UInt32), Match: POINTER(Byte), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioVerifyWithCallback(SessionHandle: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, VerifyCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_VERIFY_CALLBACK, VerifyCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioIdentify(SessionHandle: UInt32, UnitId: POINTER(UInt32), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioIdentifyWithCallback(SessionHandle: UInt32, IdentifyCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_IDENTIFY_CALLBACK, IdentifyCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioWait(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCancel(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLocateSensor(SessionHandle: UInt32, UnitId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLocateSensorWithCallback(SessionHandle: UInt32, LocateCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_LOCATE_SENSOR_CALLBACK, LocateCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollBegin(SessionHandle: UInt32, SubFactor: Byte, UnitId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollSelect(SessionHandle: UInt32, SelectorValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCapture(SessionHandle: UInt32, RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCaptureWithCallback(SessionHandle: UInt32, EnrollCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_ENROLL_CAPTURE_CALLBACK, EnrollCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCommit(SessionHandle: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), IsNewTemplate: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollDiscard(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumEnrollments(SessionHandle: UInt32, UnitId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactorArray: POINTER(POINTER(Byte)), SubFactorCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioImproveBegin(SessionHandle: UInt32, UnitId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioImproveEnd(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRegisterEventMonitor(SessionHandle: UInt32, EventMask: UInt32, EventCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_EVENT_CALLBACK, EventCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioUnregisterEventMonitor(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioMonitorPresence(SessionHandle: UInt32, UnitId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCaptureSample(SessionHandle: UInt32, Purpose: Byte, Flags: Byte, UnitId: POINTER(UInt32), Sample: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCaptureSampleWithCallback(SessionHandle: UInt32, Purpose: Byte, Flags: Byte, CaptureCallback: win32more.Windows.Win32.Devices.BiometricFramework.PWINBIO_CAPTURE_CALLBACK, CaptureCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioDeleteTemplate(SessionHandle: UInt32, UnitId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLockUnit(SessionHandle: UInt32, UnitId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioUnlockUnit(SessionHandle: UInt32, UnitId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioControlUnit(SessionHandle: UInt32, UnitId: UInt32, Component: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT, ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioControlUnitPrivileged(SessionHandle: UInt32, UnitId: UInt32, Component: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT, ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetProperty(SessionHandle: UInt32, PropertyType: UInt32, PropertyId: UInt32, UnitId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: POINTER(VoidPtr), PropertyBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioSetProperty(SessionHandle: UInt32, PropertyType: UInt32, PropertyId: UInt32, UnitId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: VoidPtr, PropertyBufferSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioFree(Address: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioSetCredential(Type: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE, Credential: POINTER(Byte), CredentialSize: UIntPtr, Format: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_FORMAT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveCredential(Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY, Type: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveAllCredentials() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveAllDomainCredentials() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetCredentialState(Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY, Type: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE, CredentialState: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLogonIdentifiedUser(SessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetEnrolledFactors(AccountOwner: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), EnrolledFactors: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetEnabledSetting(Value: POINTER(Byte), Source: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioGetLogonSetting(Value: POINTER(Byte), Source: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioGetDomainLogonSetting(Value: POINTER(Byte), Source: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioAcquireFocus() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioReleaseFocus() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), TypeInfoBufferAddress: POINTER(Byte), TypeInfoBufferSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleBuffer: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head), SampleSize: UIntPtr, Purpose: Byte, RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ATTACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), Duplicate: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CLEAR_CONTEXT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_COMMIT_ENROLLMENT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PayloadBlob: POINTER(Byte), PayloadBlobSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CONTROL_UNIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(POINTER(Byte)), NonceSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_ENROLLMENT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_KEY_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Key: POINTER(Byte), KeySize: UIntPtr, KeyIdentifier: POINTER(Byte), KeyIdentifierSize: UIntPtr, ResultSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DEACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DETACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DISCARD_ENROLLMENT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Flags: Byte, SampleBuffer: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_ALL_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PresenceCount: POINTER(UIntPtr), PresenceArray: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(Byte), NonceSize: UIntPtr, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32), Authentication: POINTER(POINTER(Byte)), AuthenticationSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), PayloadBlob: POINTER(POINTER(Byte)), PayloadBlobSize: POINTER(UIntPtr), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(Byte), NonceSize: UIntPtr, KeyIdentifier: POINTER(Byte), KeyIdentifierSize: UIntPtr, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32), Authorization: POINTER(POINTER(Byte)), AuthorizationSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_PIPELINE_CLEANUP_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_PIPELINE_INIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DiscardAndRepeatCapture: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), CalibrationBuffer: POINTER(Byte), CalibrationBufferSize: POINTER(UIntPtr), MaxBufferSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), EnrollmentStatus: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_STATUS_head), EnrollmentStatusSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), EngineInfo: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENGINE_INFO_head), EngineInfoSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AlgorithmCount: POINTER(UIntPtr), AlgorithmBufferSize: POINTER(UIntPtr), AlgorithmBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndexElementCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), StandardFormat: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT_head), VendorFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleHint: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_REFRESH_CACHE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_RESERVED_1_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), FormatArray: POINTER(Guid), FormatCount: UIntPtr, SelectedFormat: POINTER(Guid), MaxBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PolicyItemArray: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ACCOUNT_POLICY_head), PolicyItemCount: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Parameters: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SelectorValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_HASH_ALGORITHM_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AlgorithmBufferSize: UIntPtr, AlgorithmBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_UPDATE_ENROLLMENT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_VERIFY_FEATURE_SET_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, Match: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), PayloadBlob: POINTER(POINTER(Byte)), PayloadBlobSize: POINTER(UIntPtr), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AllocationSize: UIntPtr, Address: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_FREE_MEMORY_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Address: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_GET_PROPERTY_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PropertyType: UInt32, PropertyId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: POINTER(VoidPtr), PropertyBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid, SecureBufferAddress: POINTER(VoidPtr), SecureBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ExtendedStatus: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS_head), ExtendedStatusSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RequiredCapacity: POINTER(UIntPtr), MaxBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), BufferAddress: POINTER(Byte), BufferSize: UIntPtr, ReturnedDataSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RequiredCapacity: UIntPtr, MaxBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), BufferAddress: POINTER(Byte), BufferSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Authentication: POINTER(Byte), AuthenticationSize: UIntPtr, Iv: POINTER(Byte), IvSize: UIntPtr, EncryptedData: POINTER(Byte), EncryptedDataSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SecureIdentityCount: POINTER(UIntPtr), SecureIdentities: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reserved1: UIntPtr, Reserved2: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reserved1: POINTER(Byte), Reserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), CalibrationBuffer: POINTER(Byte), CalibrationBufferSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RawBufferAddress: POINTER(Byte), RawBufferSize: UIntPtr, ResultBufferAddress: POINTER(POINTER(Byte)), ResultBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid, MetadataBufferAddress: POINTER(Byte), MetadataBufferSize: UIntPtr, ResultBufferAddress: POINTER(POINTER(Byte)), ResultBufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ATTACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CANCEL_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CLEAR_CONTEXT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONNECT_SECURE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ConnectionParams: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_PARAMS_head), ConnectionData: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_DATA_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONTROL_UNIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_DEACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_DETACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleBuffer: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_FINISH_CAPTURE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reason: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_GET_INDICATOR_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndicatorStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PIPELINE_CLEANUP_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PIPELINE_INIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Flags: Byte, RejectDetail: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), FormatArray: POINTER(Guid), FormatArraySize: UIntPtr, FormatCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SensorInfo: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_SENSOR_INFO_head), SensorInfoSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), TypeInfoBufferAddress: POINTER(Byte), TypeInfoBufferSize: UIntPtr, TypeInfoDataSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Status: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_RESET_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Format: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_INDICATOR_STATUS_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndicatorStatus: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_MODE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Mode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_CAPTURE_EX_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Nonce: POINTER(Byte), NonceSize: UIntPtr, Flags: Byte, Overlapped: POINTER(POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_CAPTURE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Overlapped: POINTER(POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_NOTIFY_WAKE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Overlapped: POINTER(POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ADD_RECORD_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ATTACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CLEAR_CONTEXT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CLOSE_DATABASE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CONTROL_UNIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CREATE_DATABASE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), Factor: UInt32, Format: POINTER(Guid), FilePath: win32more.Windows.Win32.Foundation.PWSTR, ConnectString: win32more.Windows.Win32.Foundation.PWSTR, IndexElementCount: UIntPtr, InitialSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DEACTIVATE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DELETE_RECORD_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DETACH_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ERASE_DATABASE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), FilePath: win32more.Windows.Win32.Foundation.PWSTR, ConnectString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_FIRST_RECORD_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_CURRENT_RECORD_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_DATABASE_SIZE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AvailableRecordCount: POINTER(UIntPtr), TotalRecordCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_DATA_FORMAT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Format: POINTER(Guid), Version: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_RECORD_COUNT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NEXT_RECORD_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordsAdded: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_OPEN_DATABASE_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), FilePath: win32more.Windows.Win32.Foundation.PWSTR, ConnectString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_PIPELINE_CLEANUP_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_PIPELINE_INIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_BY_CONTENT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SubFactor: Byte, IndexVector: POINTER(UInt32), IndexElementCount: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_BY_SUBJECT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), StorageInfo: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_STORAGE_INFO_head), StorageInfoSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_RESERVED_1_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), Reserved1: POINTER(UInt64), Reserved2: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_RESERVED_2_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, RecordContents: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN(Pipeline: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_ASYNC_COMPLETION_CALLBACK(AsyncResult: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_RESULT_head)) -> Void: ...
@winfunctype_pointer
def PWINBIO_CAPTURE_CALLBACK(CaptureCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Sample: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head), SampleSize: UIntPtr, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_ENROLL_CAPTURE_CALLBACK(EnrollCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_EVENT_CALLBACK(EventCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, Event: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EVENT_head)) -> Void: ...
@winfunctype_pointer
def PWINBIO_IDENTIFY_CALLBACK(IdentifyCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_LOCATE_SENSOR_CALLBACK(LocateCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, UnitId: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_QUERY_ENGINE_INTERFACE_FN(EngineInterface: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_QUERY_SENSOR_INTERFACE_FN(SensorInterface: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_QUERY_STORAGE_INTERFACE_FN(StorageInterface: POINTER(POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_VERIFY_CALLBACK(VerifyCallbackContext: VoidPtr, OperationStatus: win32more.Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Match: win32more.Windows.Win32.Foundation.BOOLEAN, RejectDetail: UInt32) -> Void: ...
class WINBIO_ACCOUNT_POLICY(EasyCastStructure):
    Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    AntiSpoofBehavior: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION
class WINBIO_ADAPTER_INTERFACE_VERSION(EasyCastStructure):
    MajorVersion: UInt16
    MinorVersion: UInt16
class WINBIO_ANTI_SPOOF_POLICY(EasyCastStructure):
    Action: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION
    Source: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_POLICY_SOURCE
WINBIO_ANTI_SPOOF_POLICY_ACTION = Int32
WINBIO_ANTI_SPOOF_DISABLE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 0
WINBIO_ANTI_SPOOF_ENABLE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 1
WINBIO_ANTI_SPOOF_REMOVE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 2
WINBIO_ASYNC_NOTIFICATION_METHOD = Int32
WINBIO_ASYNC_NOTIFY_NONE: WINBIO_ASYNC_NOTIFICATION_METHOD = 0
WINBIO_ASYNC_NOTIFY_CALLBACK: WINBIO_ASYNC_NOTIFICATION_METHOD = 1
WINBIO_ASYNC_NOTIFY_MESSAGE: WINBIO_ASYNC_NOTIFICATION_METHOD = 2
WINBIO_ASYNC_NOTIFY_MAXIMUM_VALUE: WINBIO_ASYNC_NOTIFICATION_METHOD = 3
class WINBIO_ASYNC_RESULT(EasyCastStructure):
    SessionHandle: UInt32
    Operation: UInt32
    SequenceNumber: UInt64
    TimeStamp: Int64
    ApiStatus: win32more.Windows.Win32.Foundation.HRESULT
    UnitId: UInt32
    UserData: VoidPtr
    Parameters: _Parameters_e__Union
    class _Parameters_e__Union(EasyCastUnion):
        Verify: _Verify_e__Struct
        Identify: _Identify_e__Struct
        EnrollBegin: _EnrollBegin_e__Struct
        EnrollCapture: _EnrollCapture_e__Struct
        EnrollCommit: _EnrollCommit_e__Struct
        EnumEnrollments: _EnumEnrollments_e__Struct
        CaptureSample: _CaptureSample_e__Struct
        DeleteTemplate: _DeleteTemplate_e__Struct
        GetProperty: _GetProperty_e__Struct
        SetProperty: _SetProperty_e__Struct
        GetEvent: _GetEvent_e__Struct
        ControlUnit: _ControlUnit_e__Struct
        EnumServiceProviders: _EnumServiceProviders_e__Struct
        EnumBiometricUnits: _EnumBiometricUnits_e__Struct
        EnumDatabases: _EnumDatabases_e__Struct
        VerifyAndReleaseTicket: _VerifyAndReleaseTicket_e__Struct
        IdentifyAndReleaseTicket: _IdentifyAndReleaseTicket_e__Struct
        EnrollSelect: _EnrollSelect_e__Struct
        MonitorPresence: _MonitorPresence_e__Struct
        GetProtectionPolicy: _GetProtectionPolicy_e__Struct
        NotifyUnitStatusChange: _NotifyUnitStatusChange_e__Struct
        class _Verify_e__Struct(EasyCastStructure):
            Match: win32more.Windows.Win32.Foundation.BOOLEAN
            RejectDetail: UInt32
        class _Identify_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
        class _EnrollBegin_e__Struct(EasyCastStructure):
            SubFactor: Byte
        class _EnrollCapture_e__Struct(EasyCastStructure):
            RejectDetail: UInt32
        class _EnrollCommit_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            IsNewTemplate: win32more.Windows.Win32.Foundation.BOOLEAN
        class _EnumEnrollments_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactorCount: UIntPtr
            SubFactorArray: POINTER(Byte)
        class _CaptureSample_e__Struct(EasyCastStructure):
            Sample: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)
            SampleSize: UIntPtr
            RejectDetail: UInt32
        class _DeleteTemplate_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
        class _GetProperty_e__Struct(EasyCastStructure):
            PropertyType: UInt32
            PropertyId: UInt32
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            PropertyBufferSize: UIntPtr
            PropertyBuffer: VoidPtr
        class _SetProperty_e__Struct(EasyCastStructure):
            PropertyType: UInt32
            PropertyId: UInt32
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            PropertyBufferSize: UIntPtr
            PropertyBuffer: VoidPtr
        class _GetEvent_e__Struct(EasyCastStructure):
            Event: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EVENT
        class _ControlUnit_e__Struct(EasyCastStructure):
            Component: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT
            ControlCode: UInt32
            OperationStatus: UInt32
            SendBuffer: POINTER(Byte)
            SendBufferSize: UIntPtr
            ReceiveBuffer: POINTER(Byte)
            ReceiveBufferSize: UIntPtr
            ReceiveDataSize: UIntPtr
        class _EnumServiceProviders_e__Struct(EasyCastStructure):
            BspCount: UIntPtr
            BspSchemaArray: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)
        class _EnumBiometricUnits_e__Struct(EasyCastStructure):
            UnitCount: UIntPtr
            UnitSchemaArray: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)
        class _EnumDatabases_e__Struct(EasyCastStructure):
            StorageCount: UIntPtr
            StorageSchemaArray: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)
        class _VerifyAndReleaseTicket_e__Struct(EasyCastStructure):
            Match: win32more.Windows.Win32.Foundation.BOOLEAN
            RejectDetail: UInt32
            Ticket: UInt64
        class _IdentifyAndReleaseTicket_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
            Ticket: UInt64
        class _EnrollSelect_e__Struct(EasyCastStructure):
            SelectorValue: UInt64
        class _MonitorPresence_e__Struct(EasyCastStructure):
            ChangeType: UInt32
            PresenceCount: UIntPtr
            PresenceArray: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_head)
        class _GetProtectionPolicy_e__Struct(EasyCastStructure):
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            Policy: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PROTECTION_POLICY
        class _NotifyUnitStatusChange_e__Struct(EasyCastStructure):
            ExtendedStatus: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS
class WINBIO_BDB_ANSI_381_HEADER(EasyCastStructure):
    RecordLength: UInt64
    FormatIdentifier: UInt32
    VersionNumber: UInt32
    ProductId: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    CaptureDeviceId: UInt16
    ImageAcquisitionLevel: UInt16
    HorizontalScanResolution: UInt16
    VerticalScanResolution: UInt16
    HorizontalImageResolution: UInt16
    VerticalImageResolution: UInt16
    ElementCount: Byte
    ScaleUnits: Byte
    PixelDepth: Byte
    ImageCompressionAlg: Byte
    Reserved: UInt16
class WINBIO_BDB_ANSI_381_RECORD(EasyCastStructure):
    BlockLength: UInt32
    HorizontalLineLength: UInt16
    VerticalLineLength: UInt16
    Position: Byte
    CountOfViews: Byte
    ViewNumber: Byte
    ImageQuality: Byte
    ImpressionType: Byte
    Reserved: Byte
class WINBIO_BIR(EasyCastStructure):
    HeaderBlock: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    StandardDataBlock: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    VendorDataBlock: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    SignatureBlock: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
class WINBIO_BIR_DATA(EasyCastStructure):
    Size: UInt32
    Offset: UInt32
class WINBIO_BIR_HEADER(EasyCastStructure):
    ValidFields: UInt16
    HeaderVersion: Byte
    PatronHeaderVersion: Byte
    DataFlags: Byte
    Type: UInt32
    Subtype: Byte
    Purpose: Byte
    DataQuality: SByte
    CreationDate: Int64
    ValidityPeriod: _ValidityPeriod_e__Struct
    BiometricDataFormat: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    ProductId: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    class _ValidityPeriod_e__Struct(EasyCastStructure):
        BeginDate: Int64
        EndDate: Int64
class WINBIO_BLANK_PAYLOAD(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
class WINBIO_BSP_SCHEMA(EasyCastStructure):
    BiometricFactor: UInt32
    BspId: Guid
    Description: UInt16 * 256
    Vendor: UInt16 * 256
    Version: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
class WINBIO_CALIBRATION_INFO(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    CalibrationData: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_CAPTURE_DATA(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    SensorStatus: UInt32
    RejectDetail: UInt32
    CaptureData: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_CAPTURE_PARAMETERS(EasyCastStructure):
    PayloadSize: UInt32
    Purpose: Byte
    Format: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    VendorFormat: Guid
    Flags: Byte
WINBIO_COMPONENT = UInt32
WINBIO_COMPONENT_SENSOR: WINBIO_COMPONENT = 1
WINBIO_COMPONENT_ENGINE: WINBIO_COMPONENT = 2
WINBIO_COMPONENT_STORAGE: WINBIO_COMPONENT = 3
WINBIO_CREDENTIAL_FORMAT = Int32
WINBIO_PASSWORD_GENERIC: WINBIO_CREDENTIAL_FORMAT = 1
WINBIO_PASSWORD_PACKED: WINBIO_CREDENTIAL_FORMAT = 2
WINBIO_PASSWORD_PROTECTED: WINBIO_CREDENTIAL_FORMAT = 3
WINBIO_CREDENTIAL_STATE = Int32
WINBIO_CREDENTIAL_NOT_SET: WINBIO_CREDENTIAL_STATE = 1
WINBIO_CREDENTIAL_SET: WINBIO_CREDENTIAL_STATE = 2
WINBIO_CREDENTIAL_TYPE = Int32
WINBIO_CREDENTIAL_PASSWORD: WINBIO_CREDENTIAL_TYPE = 1
WINBIO_CREDENTIAL_ALL: WINBIO_CREDENTIAL_TYPE = -1
class WINBIO_DATA(EasyCastStructure):
    Size: UInt32
    Data: Byte * 1
class WINBIO_DIAGNOSTICS(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    SensorStatus: UInt32
    VendorDiagnostics: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_ENCRYPTED_CAPTURE_PARAMS(EasyCastStructure):
    PayloadSize: UInt32
    Purpose: Byte
    Format: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    VendorFormat: Guid
    Flags: Byte
    NonceSize: UInt32
class WINBIO_ENGINE_INTERFACE(EasyCastStructure):
    Version: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ATTACH_FN
    Detach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DETACH_FN
    ClearContext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CLEAR_CONTEXT_FN
    QueryPreferredFormat: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN
    QueryIndexVectorSize: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN
    QueryHashAlgorithms: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN
    SetHashAlgorithm: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_HASH_ALGORITHM_FN
    QuerySampleHint: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN
    AcceptSampleData: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN
    ExportEngineData: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN
    VerifyFeatureSet: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_VERIFY_FEATURE_SET_FN
    IdentifyFeatureSet: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN
    CreateEnrollment: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_FN
    UpdateEnrollment: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_UPDATE_ENROLLMENT_FN
    GetEnrollmentStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN
    GetEnrollmentHash: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN
    CheckForDuplicate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN
    CommitEnrollment: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_COMMIT_ENROLLMENT_FN
    DiscardEnrollment: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DISCARD_ENROLLMENT_FN
    ControlUnit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_FN
    ControlUnitPrivileged: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN
    Reserved_1: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_RESERVED_1_FN
    PipelineInit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_INIT_FN
    PipelineCleanup: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_CLEANUP_FN
    Activate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACTIVATE_FN
    Deactivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DEACTIVATE_FN
    QueryExtendedInfo: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN
    IdentifyAll: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_ALL_FN
    SetEnrollmentSelector: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN
    SetEnrollmentParameters: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN
    QueryExtendedEnrollmentStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN
    RefreshCache: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_REFRESH_CACHE_FN
    SelectCalibrationFormat: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN
    QueryCalibrationData: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN
    SetAccountPolicy: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN
    CreateKey: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_KEY_FN
    IdentifyFeatureSetSecure: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN
    AcceptPrivateSensorTypeInfo: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN
    CreateEnrollmentAuthenticated: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN
    IdentifyFeatureSetAuthenticated: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN
class WINBIO_EVENT(EasyCastStructure):
    Type: UInt32
    Parameters: _Parameters_e__Union
    class _Parameters_e__Union(EasyCastUnion):
        Unclaimed: _Unclaimed_e__Struct
        UnclaimedIdentify: _UnclaimedIdentify_e__Struct
        Error: _Error_e__Struct
        class _Unclaimed_e__Struct(EasyCastStructure):
            UnitId: UInt32
            RejectDetail: UInt32
        class _UnclaimedIdentify_e__Struct(EasyCastStructure):
            UnitId: UInt32
            Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
        class _Error_e__Struct(EasyCastStructure):
            ErrorCode: win32more.Windows.Win32.Foundation.HRESULT
class WINBIO_EXTENDED_ENGINE_INFO(EasyCastStructure):
    GenericEngineCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                GeneralSamples: UInt32
                Center: UInt32
                TopEdge: UInt32
                BottomEdge: UInt32
                LeftEdge: UInt32
                RightEdge: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
class WINBIO_EXTENDED_ENROLLMENT_PARAMETERS(EasyCastStructure):
    Size: UIntPtr
    SubFactor: Byte
class WINBIO_EXTENDED_ENROLLMENT_STATUS(EasyCastStructure):
    TemplateStatus: win32more.Windows.Win32.Foundation.HRESULT
    RejectDetail: UInt32
    PercentComplete: UInt32
    Factor: UInt32
    SubFactor: Byte
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            BoundingBox: win32more.Windows.Win32.Foundation.RECT
            Distance: Int32
            OpaqueEngineData: _OpaqueEngineData_e__Struct
            class _OpaqueEngineData_e__Struct(EasyCastStructure):
                AdapterId: Guid
                Data: UInt32 * 78
        class _Fingerprint_e__Struct(EasyCastStructure):
            GeneralSamples: UInt32
            Center: UInt32
            TopEdge: UInt32
            BottomEdge: UInt32
            LeftEdge: UInt32
            RightEdge: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            EyeBoundingBox_1: win32more.Windows.Win32.Foundation.RECT
            EyeBoundingBox_2: win32more.Windows.Win32.Foundation.RECT
            PupilCenter_1: win32more.Windows.Win32.Foundation.POINT
            PupilCenter_2: win32more.Windows.Win32.Foundation.POINT
            Distance: Int32
            GridPointCompletionPercent: UInt32
            GridPointIndex: UInt16
            Point3D: _Point3D_e__Struct
            StopCaptureAndShowCriticalFeedback: win32more.Windows.Win32.Foundation.BOOL
            class _Point3D_e__Struct(EasyCastStructure):
                X: Double
                Y: Double
                Z: Double
        class _Voice_e__Struct(EasyCastStructure):
            Reserved: UInt32
class WINBIO_EXTENDED_SENSOR_INFO(EasyCastStructure):
    GenericSensorCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            FrameSize: win32more.Windows.Win32.Foundation.RECT
            FrameOffset: win32more.Windows.Win32.Foundation.POINT
            MandatoryOrientation: UInt32
            HardwareInfo: _HardwareInfo_e__Struct
            class _HardwareInfo_e__Struct(EasyCastStructure):
                ColorSensorId: Char * 260
                InfraredSensorId: Char * 260
                InfraredSensorRotationAngle: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Reserved: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            FrameSize: win32more.Windows.Win32.Foundation.RECT
            FrameOffset: win32more.Windows.Win32.Foundation.POINT
            MandatoryOrientation: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Reserved: UInt32
class WINBIO_EXTENDED_STORAGE_INFO(EasyCastStructure):
    GenericStorageCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Capabilities: UInt32
class WINBIO_EXTENDED_UNIT_STATUS(EasyCastStructure):
    Availability: UInt32
    ReasonCode: UInt32
class WINBIO_FP_BU_STATE(EasyCastStructure):
    SensorAttached: win32more.Windows.Win32.Foundation.BOOL
    CreationResult: win32more.Windows.Win32.Foundation.HRESULT
class WINBIO_FRAMEWORK_INTERFACE(EasyCastStructure):
    Version: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    SetUnitStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN
    VsmStorageAttach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN
    VsmStorageDetach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN
    VsmStorageClearContext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN
    VsmStorageCreateDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN
    VsmStorageOpenDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN
    VsmStorageCloseDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN
    VsmStorageDeleteRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN
    VsmStorageNotifyPowerChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN
    VsmStoragePipelineInit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN
    VsmStoragePipelineCleanup: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN
    VsmStorageActivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN
    VsmStorageDeactivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN
    VsmStorageQueryExtendedInfo: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN
    VsmStorageCacheClear: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN
    VsmStorageCacheImportBegin: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN
    VsmStorageCacheImportNext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN
    VsmStorageCacheImportEnd: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN
    VsmStorageCacheExportBegin: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN
    VsmStorageCacheExportNext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN
    VsmStorageCacheExportEnd: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN
    VsmSensorAttach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN
    VsmSensorDetach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN
    VsmSensorClearContext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN
    VsmSensorPushDataToEngine: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN
    VsmSensorNotifyPowerChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN
    VsmSensorPipelineInit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN
    VsmSensorPipelineCleanup: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN
    VsmSensorActivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN
    VsmSensorDeactivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN
    VsmSensorAsyncImportRawBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN
    VsmSensorAsyncImportSecureBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN
    Reserved1: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN
    Reserved2: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN
    Reserved3: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN
    Reserved4: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN
    Reserved5: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN
    AllocateMemory: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN
    FreeMemory: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_FREE_MEMORY_FN
    GetProperty: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_GET_PROPERTY_FN
    LockAndValidateSecureBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN
    ReleaseSecureBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN
    QueryAuthorizedEnrollments: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN
    DecryptSample: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN
class WINBIO_GESTURE_METADATA(EasyCastStructure):
    Size: UIntPtr
    BiometricType: UInt32
    MatchType: UInt32
    ProtectionType: UInt32
class WINBIO_GET_INDICATOR(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    IndicatorStatus: UInt32
class WINBIO_IDENTITY(EasyCastStructure):
    Type: UInt32
    Value: _Value_e__Union
    class _Value_e__Union(EasyCastUnion):
        Null: UInt32
        Wildcard: UInt32
        TemplateGuid: Guid
        AccountSid: _AccountSid_e__Struct
        SecureId: Byte * 32
        class _AccountSid_e__Struct(EasyCastStructure):
            Size: UInt32
            Data: Byte * 68
class WINBIO_NOTIFY_WAKE(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    Reason: UInt32
class WINBIO_PIPELINE(EasyCastStructure):
    SensorHandle: win32more.Windows.Win32.Foundation.HANDLE
    EngineHandle: win32more.Windows.Win32.Foundation.HANDLE
    StorageHandle: win32more.Windows.Win32.Foundation.HANDLE
    SensorInterface: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head)
    EngineInterface: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head)
    StorageInterface: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head)
    SensorContext: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINIBIO_SENSOR_CONTEXT)
    EngineContext: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINIBIO_ENGINE_CONTEXT)
    StorageContext: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINIBIO_STORAGE_CONTEXT)
    FrameworkInterface: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_FRAMEWORK_INTERFACE_head)
WINBIO_POLICY_SOURCE = Int32
WINBIO_POLICY_UNKNOWN: WINBIO_POLICY_SOURCE = 0
WINBIO_POLICY_DEFAULT: WINBIO_POLICY_SOURCE = 1
WINBIO_POLICY_LOCAL: WINBIO_POLICY_SOURCE = 2
WINBIO_POLICY_ADMIN: WINBIO_POLICY_SOURCE = 3
WINBIO_POOL = UInt32
WINBIO_POOL_SYSTEM: WINBIO_POOL = 1
WINBIO_POOL_PRIVATE: WINBIO_POOL = 2
class WINBIO_PRESENCE(EasyCastStructure):
    Factor: UInt32
    SubFactor: Byte
    Status: win32more.Windows.Win32.Foundation.HRESULT
    RejectDetail: UInt32
    Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    TrackingId: UInt64
    Ticket: UInt64
    Properties: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_PROPERTIES
    Authorization: _Authorization_e__Struct
    class _Authorization_e__Struct(EasyCastStructure):
        Size: UInt32
        Data: Byte * 32
class WINBIO_PRESENCE_PROPERTIES(EasyCastUnion):
    FacialFeatures: _FacialFeatures_e__Struct
    Iris: _Iris_e__Struct
    class _FacialFeatures_e__Struct(EasyCastStructure):
        BoundingBox: win32more.Windows.Win32.Foundation.RECT
        Distance: Int32
        OpaqueEngineData: _OpaqueEngineData_e__Struct
        class _OpaqueEngineData_e__Struct(EasyCastStructure):
            AdapterId: Guid
            Data: UInt32 * 78
    class _Iris_e__Struct(EasyCastStructure):
        EyeBoundingBox_1: win32more.Windows.Win32.Foundation.RECT
        EyeBoundingBox_2: win32more.Windows.Win32.Foundation.RECT
        PupilCenter_1: win32more.Windows.Win32.Foundation.POINT
        PupilCenter_2: win32more.Windows.Win32.Foundation.POINT
        Distance: Int32
class WINBIO_PRIVATE_SENSOR_TYPE_INFO(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    PrivateSensorTypeInfo: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_PROTECTION_POLICY(EasyCastStructure):
    Version: UInt32
    Identity: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    DatabaseId: Guid
    UserState: UInt64
    PolicySize: UIntPtr
    Policy: Byte * 128
class WINBIO_REGISTERED_FORMAT(EasyCastStructure):
    Owner: UInt16
    Type: UInt16
class WINBIO_SECURE_BUFFER_HEADER_V1(EasyCastStructure):
    Type: UInt32
    Size: UInt32
    Flags: UInt32
    ValidationTag: UInt64
class WINBIO_SECURE_CONNECTION_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt16
    Flags: UInt16
    ModelCertificateSize: UInt32
    IntermediateCA1Size: UInt32
    IntermediateCA2Size: UInt32
class WINBIO_SECURE_CONNECTION_PARAMS(EasyCastStructure):
    PayloadSize: UInt32
    Version: UInt16
    Flags: UInt16
class WINBIO_SENSOR_ATTRIBUTES(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    WinBioVersion: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
    SensorType: UInt32
    SensorSubType: UInt32
    Capabilities: UInt32
    ManufacturerName: UInt16 * 256
    ModelName: UInt16 * 256
    SerialNumber: UInt16 * 256
    FirmwareVersion: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
    SupportedFormatEntries: UInt32
    SupportedFormat: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT * 1
class WINBIO_SENSOR_INTERFACE(EasyCastStructure):
    Version: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN
    Detach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN
    ClearContext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN
    QueryStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_STATUS_FN
    Reset: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_RESET_FN
    SetMode: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_MODE_FN
    SetIndicatorStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_INDICATOR_STATUS_FN
    GetIndicatorStatus: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_GET_INDICATOR_STATUS_FN
    StartCapture: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_FN
    FinishCapture: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_CAPTURE_FN
    ExportSensorData: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN
    Cancel: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CANCEL_FN
    PushDataToEngine: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN
    ControlUnit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_FN
    ControlUnitPrivileged: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN
    PipelineInit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN
    PipelineCleanup: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN
    Activate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN
    Deactivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN
    QueryExtendedInfo: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN
    QueryCalibrationFormats: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN
    SetCalibrationFormat: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN
    AcceptCalibrationData: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN
    AsyncImportRawBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN
    AsyncImportSecureBuffer: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN
    QueryPrivateSensorType: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN
    ConnectSecure: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONNECT_SECURE_FN
    StartCaptureEx: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_EX_FN
    StartNotifyWake: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_NOTIFY_WAKE_FN
    FinishNotifyWake: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN
WINBIO_SETTING_SOURCE = UInt32
WINBIO_SETTING_SOURCE_INVALID: WINBIO_SETTING_SOURCE = 0
WINBIO_SETTING_SOURCE_DEFAULT: WINBIO_SETTING_SOURCE = 1
WINBIO_SETTING_SOURCE_LOCAL: WINBIO_SETTING_SOURCE = 3
WINBIO_SETTING_SOURCE_POLICY: WINBIO_SETTING_SOURCE = 2
class WINBIO_SET_INDICATOR(EasyCastStructure):
    PayloadSize: UInt32
    IndicatorStatus: UInt32
class WINBIO_STORAGE_INTERFACE(EasyCastStructure):
    Version: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN
    Detach: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN
    ClearContext: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN
    CreateDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN
    EraseDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ERASE_DATABASE_FN
    OpenDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN
    CloseDatabase: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN
    GetDataFormat: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATA_FORMAT_FN
    GetDatabaseSize: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATABASE_SIZE_FN
    AddRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ADD_RECORD_FN
    DeleteRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN
    QueryBySubject: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_SUBJECT_FN
    QueryByContent: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_CONTENT_FN
    GetRecordCount: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_RECORD_COUNT_FN
    FirstRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_FIRST_RECORD_FN
    NextRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NEXT_RECORD_FN
    GetCurrentRecord: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_CURRENT_RECORD_FN
    ControlUnit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_FN
    ControlUnitPrivileged: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN
    PipelineInit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN
    PipelineCleanup: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN
    Activate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN
    Deactivate: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN
    QueryExtendedInfo: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN
    NotifyDatabaseChange: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN
    Reserved1: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN
    Reserved2: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN
    UpdateRecordBegin: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN
    UpdateRecordCommit: win32more.Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN
class WINBIO_STORAGE_RECORD(EasyCastStructure):
    Identity: POINTER(win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)
    SubFactor: Byte
    IndexVector: POINTER(UInt32)
    IndexElementCount: UIntPtr
    TemplateBlob: POINTER(Byte)
    TemplateBlobSize: UIntPtr
    PayloadBlob: POINTER(Byte)
    PayloadBlobSize: UIntPtr
class WINBIO_STORAGE_SCHEMA(EasyCastStructure):
    BiometricFactor: UInt32
    DatabaseId: Guid
    DataFormat: Guid
    Attributes: UInt32
    FilePath: UInt16 * 256
    ConnectionString: UInt16 * 256
class WINBIO_SUPPORTED_ALGORITHMS(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: win32more.Windows.Win32.Foundation.HRESULT
    NumberOfAlgorithms: UInt32
    AlgorithmData: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_UNIT_SCHEMA(EasyCastStructure):
    UnitId: UInt32
    PoolType: UInt32
    BiometricFactor: UInt32
    SensorSubType: UInt32
    Capabilities: UInt32
    DeviceInstanceId: UInt16 * 256
    Description: UInt16 * 256
    Manufacturer: UInt16 * 256
    Model: UInt16 * 256
    SerialNumber: UInt16 * 256
    FirmwareVersion: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
class WINBIO_UPDATE_FIRMWARE(EasyCastStructure):
    PayloadSize: UInt32
    FirmwareData: win32more.Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_VERSION(EasyCastStructure):
    MajorVersion: UInt32
    MinorVersion: UInt32
WINIBIO_ENGINE_CONTEXT = IntPtr
WINIBIO_SENSOR_CONTEXT = IntPtr
WINIBIO_STORAGE_CONTEXT = IntPtr
make_head(_module, 'PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN')
make_head(_module, 'PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_ACTIVATE_FN')
make_head(_module, 'PIBIO_ENGINE_ATTACH_FN')
make_head(_module, 'PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN')
make_head(_module, 'PIBIO_ENGINE_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_ENGINE_COMMIT_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_KEY_FN')
make_head(_module, 'PIBIO_ENGINE_DEACTIVATE_FN')
make_head(_module, 'PIBIO_ENGINE_DETACH_FN')
make_head(_module, 'PIBIO_ENGINE_DISCARD_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN')
make_head(_module, 'PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_ALL_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN')
make_head(_module, 'PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_ENGINE_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_ENGINE_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN')
make_head(_module, 'PIBIO_ENGINE_REFRESH_CACHE_FN')
make_head(_module, 'PIBIO_ENGINE_RESERVED_1_FN')
make_head(_module, 'PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN')
make_head(_module, 'PIBIO_ENGINE_SET_HASH_ALGORITHM_FN')
make_head(_module, 'PIBIO_ENGINE_UPDATE_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_VERIFY_FEATURE_SET_FN')
make_head(_module, 'PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_FREE_MEMORY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_GET_PROPERTY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN')
make_head(_module, 'PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN')
make_head(_module, 'PIBIO_SENSOR_ACTIVATE_FN')
make_head(_module, 'PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN')
make_head(_module, 'PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_SENSOR_ATTACH_FN')
make_head(_module, 'PIBIO_SENSOR_CANCEL_FN')
make_head(_module, 'PIBIO_SENSOR_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_SENSOR_CONNECT_SECURE_FN')
make_head(_module, 'PIBIO_SENSOR_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_SENSOR_DEACTIVATE_FN')
make_head(_module, 'PIBIO_SENSOR_DETACH_FN')
make_head(_module, 'PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN')
make_head(_module, 'PIBIO_SENSOR_FINISH_CAPTURE_FN')
make_head(_module, 'PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN')
make_head(_module, 'PIBIO_SENSOR_GET_INDICATOR_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_SENSOR_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_SENSOR_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_RESET_FN')
make_head(_module, 'PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN')
make_head(_module, 'PIBIO_SENSOR_SET_INDICATOR_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_SET_MODE_FN')
make_head(_module, 'PIBIO_SENSOR_START_CAPTURE_EX_FN')
make_head(_module, 'PIBIO_SENSOR_START_CAPTURE_FN')
make_head(_module, 'PIBIO_SENSOR_START_NOTIFY_WAKE_FN')
make_head(_module, 'PIBIO_STORAGE_ACTIVATE_FN')
make_head(_module, 'PIBIO_STORAGE_ADD_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_ATTACH_FN')
make_head(_module, 'PIBIO_STORAGE_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_STORAGE_CLOSE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_STORAGE_CREATE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_DEACTIVATE_FN')
make_head(_module, 'PIBIO_STORAGE_DELETE_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_DETACH_FN')
make_head(_module, 'PIBIO_STORAGE_ERASE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_FIRST_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_GET_CURRENT_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_GET_DATABASE_SIZE_FN')
make_head(_module, 'PIBIO_STORAGE_GET_DATA_FORMAT_FN')
make_head(_module, 'PIBIO_STORAGE_GET_RECORD_COUNT_FN')
make_head(_module, 'PIBIO_STORAGE_NEXT_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN')
make_head(_module, 'PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_STORAGE_OPEN_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_STORAGE_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_BY_CONTENT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_BY_SUBJECT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_STORAGE_RESERVED_1_FN')
make_head(_module, 'PIBIO_STORAGE_RESERVED_2_FN')
make_head(_module, 'PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN')
make_head(_module, 'PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN')
make_head(_module, 'PWINBIO_ASYNC_COMPLETION_CALLBACK')
make_head(_module, 'PWINBIO_CAPTURE_CALLBACK')
make_head(_module, 'PWINBIO_ENROLL_CAPTURE_CALLBACK')
make_head(_module, 'PWINBIO_EVENT_CALLBACK')
make_head(_module, 'PWINBIO_IDENTIFY_CALLBACK')
make_head(_module, 'PWINBIO_LOCATE_SENSOR_CALLBACK')
make_head(_module, 'PWINBIO_QUERY_ENGINE_INTERFACE_FN')
make_head(_module, 'PWINBIO_QUERY_SENSOR_INTERFACE_FN')
make_head(_module, 'PWINBIO_QUERY_STORAGE_INTERFACE_FN')
make_head(_module, 'PWINBIO_VERIFY_CALLBACK')
make_head(_module, 'WINBIO_ACCOUNT_POLICY')
make_head(_module, 'WINBIO_ADAPTER_INTERFACE_VERSION')
make_head(_module, 'WINBIO_ANTI_SPOOF_POLICY')
make_head(_module, 'WINBIO_ASYNC_RESULT')
make_head(_module, 'WINBIO_BDB_ANSI_381_HEADER')
make_head(_module, 'WINBIO_BDB_ANSI_381_RECORD')
make_head(_module, 'WINBIO_BIR')
make_head(_module, 'WINBIO_BIR_DATA')
make_head(_module, 'WINBIO_BIR_HEADER')
make_head(_module, 'WINBIO_BLANK_PAYLOAD')
make_head(_module, 'WINBIO_BSP_SCHEMA')
make_head(_module, 'WINBIO_CALIBRATION_INFO')
make_head(_module, 'WINBIO_CAPTURE_DATA')
make_head(_module, 'WINBIO_CAPTURE_PARAMETERS')
make_head(_module, 'WINBIO_DATA')
make_head(_module, 'WINBIO_DIAGNOSTICS')
make_head(_module, 'WINBIO_ENCRYPTED_CAPTURE_PARAMS')
make_head(_module, 'WINBIO_ENGINE_INTERFACE')
make_head(_module, 'WINBIO_EVENT')
make_head(_module, 'WINBIO_EXTENDED_ENGINE_INFO')
make_head(_module, 'WINBIO_EXTENDED_ENROLLMENT_PARAMETERS')
make_head(_module, 'WINBIO_EXTENDED_ENROLLMENT_STATUS')
make_head(_module, 'WINBIO_EXTENDED_SENSOR_INFO')
make_head(_module, 'WINBIO_EXTENDED_STORAGE_INFO')
make_head(_module, 'WINBIO_EXTENDED_UNIT_STATUS')
make_head(_module, 'WINBIO_FP_BU_STATE')
make_head(_module, 'WINBIO_FRAMEWORK_INTERFACE')
make_head(_module, 'WINBIO_GESTURE_METADATA')
make_head(_module, 'WINBIO_GET_INDICATOR')
make_head(_module, 'WINBIO_IDENTITY')
make_head(_module, 'WINBIO_NOTIFY_WAKE')
make_head(_module, 'WINBIO_PIPELINE')
make_head(_module, 'WINBIO_PRESENCE')
make_head(_module, 'WINBIO_PRESENCE_PROPERTIES')
make_head(_module, 'WINBIO_PRIVATE_SENSOR_TYPE_INFO')
make_head(_module, 'WINBIO_PROTECTION_POLICY')
make_head(_module, 'WINBIO_REGISTERED_FORMAT')
make_head(_module, 'WINBIO_SECURE_BUFFER_HEADER_V1')
make_head(_module, 'WINBIO_SECURE_CONNECTION_DATA')
make_head(_module, 'WINBIO_SECURE_CONNECTION_PARAMS')
make_head(_module, 'WINBIO_SENSOR_ATTRIBUTES')
make_head(_module, 'WINBIO_SENSOR_INTERFACE')
make_head(_module, 'WINBIO_SET_INDICATOR')
make_head(_module, 'WINBIO_STORAGE_INTERFACE')
make_head(_module, 'WINBIO_STORAGE_RECORD')
make_head(_module, 'WINBIO_STORAGE_SCHEMA')
make_head(_module, 'WINBIO_SUPPORTED_ALGORITHMS')
make_head(_module, 'WINBIO_UNIT_SCHEMA')
make_head(_module, 'WINBIO_UPDATE_FIRMWARE')
make_head(_module, 'WINBIO_VERSION')
