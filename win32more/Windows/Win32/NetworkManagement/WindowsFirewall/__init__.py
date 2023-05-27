from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WindowsFirewall
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
NETCON_MAX_NAME_LEN: UInt32 = 256
S_OBJECT_NO_LONGER_VALID: win32more.Windows.Win32.Foundation.HRESULT = 2
NETISO_GEID_FOR_WDAG: UInt32 = 1
NETISO_GEID_FOR_NEUTRAL_AWARE: UInt32 = 2
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationSetupAppContainerBinaries(applicationContainerSid: win32more.Windows.Win32.Foundation.PSID, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, packageFolder: win32more.Windows.Win32.Foundation.PWSTR, displayName: win32more.Windows.Win32.Foundation.PWSTR, bBinariesFullyComputed: win32more.Windows.Win32.Foundation.BOOL, binaries: POINTER(win32more.Windows.Win32.Foundation.PWSTR), binariesCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationRegisterForAppContainerChanges(flags: UInt32, callback: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.PAC_CHANGES_CALLBACK_FN, context: VoidPtr, registrationObject: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationUnregisterForAppContainerChanges(registrationObject: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationFreeAppContainers(pPublicAppCs: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationEnumAppContainers(Flags: UInt32, pdwNumPublicAppCs: POINTER(UInt32), ppPublicAppCs: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head))) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationGetAppContainerConfig(pdwNumPublicAppCs: POINTER(UInt32), appContainerSids: POINTER(POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_head))) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationSetAppContainerConfig(dwNumPublicAppCs: UInt32, appContainerSids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationDiagnoseConnectFailureAndGetInfo(wszServerName: win32more.Windows.Win32.Foundation.PWSTR, netIsoError: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETISO_ERROR_TYPE)) -> UInt32: ...
class FW_DYNAMIC_KEYWORD_ADDRESS0(EasyCastStructure):
    id: Guid
    keyword: win32more.Windows.Win32.Foundation.PWSTR
    flags: UInt32
    addresses: win32more.Windows.Win32.Foundation.PWSTR
class FW_DYNAMIC_KEYWORD_ADDRESS_DATA0(EasyCastStructure):
    dynamicKeywordAddress: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0
    next: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)
    schemaVersion: UInt16
    originType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ORIGIN_TYPE
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = Int32
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 1
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 2
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 3
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = Int32
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = 1
FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = Int32
FW_DYNAMIC_KEYWORD_ORIGIN_INVALID: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 0
FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 1
FW_DYNAMIC_KEYWORD_ORIGIN_MDM: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 2
ICS_TARGETTYPE = Int32
ICSTT_NAME: ICS_TARGETTYPE = 0
ICSTT_IPADDRESS: ICS_TARGETTYPE = 1
class IDynamicPortMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4fc80282-23b6-4378-9a27-cd8f17c9400c}')
    @commethod(7)
    def get_ExternalIPAddress(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RemoteHost(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExternalPort(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Protocol(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternalPort(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InternalClient(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Enabled(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Description(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LeaseDuration(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RenewLease(self, lLeaseDurationDesired: Int32, pLeaseDurationReturned: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EditInternalClient(self, bstrInternalClient: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Enable(self, vb: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EditDescription(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EditInternalPort(self, lInternalPort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDynamicPortMappingCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b60de00f-156e-4e8d-9ec1-3a2342c10899}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, bstrRemoteHost: win32more.Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, ppDPM: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, bstrRemoteHost: win32more.Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, bstrRemoteHost: win32more.Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, lInternalPort: Int32, bstrInternalClient: win32more.Windows.Win32.Foundation.BSTR, bEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrDescription: win32more.Windows.Win32.Foundation.BSTR, lLeaseDuration: Int32, ppDPM: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956a0-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingEveryConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956b8-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPortMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956b0-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPrivateConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956b5-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pCeltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPublicConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956b4-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INATEventManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{624bd588-9060-4109-b0b0-1adbbcac32df}')
    @commethod(7)
    def put_ExternalIPAddressCallback(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_NumberOfEntriesCallback(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INATExternalIPAddressCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c416740-a34e-446f-ba06-abd04c3149ae}')
    @commethod(3)
    def NewExternalIPAddress(self, bstrNewExternalIPAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INATNumberOfEntriesCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c83a0a74-91ee-41b6-b67a-67e0f00bbd78}')
    @commethod(3)
    def NewNumberOfEntries(self, lNewNumberOfEntries: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INET_FIREWALL_AC_BINARIES(EasyCastStructure):
    count: UInt32
    binaries: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class INET_FIREWALL_AC_CAPABILITIES(EasyCastStructure):
    count: UInt32
    capabilities: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_head)
class INET_FIREWALL_AC_CHANGE(EasyCastStructure):
    changeType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_TYPE
    createType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CREATION_TYPE
    appContainerSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    userSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    displayName: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        capabilities: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES
        binaries: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES
INET_FIREWALL_AC_CHANGE_TYPE = Int32
INET_FIREWALL_AC_CHANGE_INVALID: INET_FIREWALL_AC_CHANGE_TYPE = 0
INET_FIREWALL_AC_CHANGE_CREATE: INET_FIREWALL_AC_CHANGE_TYPE = 1
INET_FIREWALL_AC_CHANGE_DELETE: INET_FIREWALL_AC_CHANGE_TYPE = 2
INET_FIREWALL_AC_CHANGE_MAX: INET_FIREWALL_AC_CHANGE_TYPE = 3
INET_FIREWALL_AC_CREATION_TYPE = Int32
INET_FIREWALL_AC_NONE: INET_FIREWALL_AC_CREATION_TYPE = 0
INET_FIREWALL_AC_PACKAGE_ID_ONLY: INET_FIREWALL_AC_CREATION_TYPE = 1
INET_FIREWALL_AC_BINARY: INET_FIREWALL_AC_CREATION_TYPE = 2
INET_FIREWALL_AC_MAX: INET_FIREWALL_AC_CREATION_TYPE = 4
class INET_FIREWALL_APP_CONTAINER(EasyCastStructure):
    appContainerSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    userSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    appContainerName: win32more.Windows.Win32.Foundation.PWSTR
    displayName: win32more.Windows.Win32.Foundation.PWSTR
    description: win32more.Windows.Win32.Foundation.PWSTR
    capabilities: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES
    binaries: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES
    workingDirectory: win32more.Windows.Win32.Foundation.PWSTR
    packageFullName: win32more.Windows.Win32.Foundation.PWSTR
class INetConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956a1-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def Connect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Duplicate(self, pszwDuplicateName: win32more.Windows.Win32.Foundation.PWSTR, ppCon: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperties(self, ppProps: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_PROPERTIES_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetUiObjectClassId(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Rename(self, pszwNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetConnectionConnectUi(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956a3-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def SetConnection(self, pCon: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetConnectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c08956a2-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(3)
    def EnumConnections(self, Flags: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCONMGR_ENUM_FLAGS, ppEnum: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetConnectionProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f4277c95-ce5b-463d-8167-5662d9bcaa72}')
    @commethod(7)
    def get_Guid(self, pbstrGuid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DeviceName(self, pbstrDeviceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MediaType(self, pMediaType: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Characteristics(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwAuthorizedApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b5e64ffa-c2c5-444e-a301-fb5e00018050}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ProcessImageFileName(self, imageFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ProcessImageFileName(self, imageFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpVersion(self, ipVersion: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpVersion(self, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Scope(self, scope: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Scope(self, scope: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RemoteAddresses(self, remoteAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_RemoteAddresses(self, remoteAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwAuthorizedApplications(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{644efd52-ccf9-486c-97a2-39f352570b30}')
    @commethod(7)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, app: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, imageFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, imageFileName: win32more.Windows.Win32.Foundation.BSTR, app: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(self, newEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwIcmpSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a6207b2e-7cdd-426a-951e-5e1cbc5afead}')
    @commethod(7)
    def get_AllowOutboundDestinationUnreachable(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AllowOutboundDestinationUnreachable(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AllowRedirect(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AllowRedirect(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AllowInboundEchoRequest(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowInboundEchoRequest(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowOutboundTimeExceeded(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowOutboundTimeExceeded(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AllowOutboundParameterProblem(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_AllowOutboundParameterProblem(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AllowOutboundSourceQuench(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowOutboundSourceQuench(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowInboundRouterRequest(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_AllowInboundRouterRequest(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_AllowInboundTimestampRequest(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_AllowInboundTimestampRequest(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AllowInboundMaskRequest(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AllowInboundMaskRequest(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowOutboundPacketTooBig(self, allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowOutboundPacketTooBig(self, allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f7898af5-cac4-4632-a2ec-da06e5111af2}')
    @commethod(7)
    def get_LocalPolicy(self, localPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwPolicy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentProfileType(self, profileType: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RestoreDefaults(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsPortAllowed(self, imageFileName: win32more.Windows.Win32.Foundation.BSTR, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, portNumber: Int32, localAddress: win32more.Windows.Win32.Foundation.BSTR, ipProtocol: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, allowed: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), restricted: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsIcmpTypeAllowed(self, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, localAddress: win32more.Windows.Win32.Foundation.BSTR, type: Byte, allowed: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), restricted: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwOpenPort(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e0483ba0-47ff-4d9c-a6d6-7741d0b195f7}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IpVersion(self, ipVersion: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_IpVersion(self, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Protocol(self, ipProtocol: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Protocol(self, ipProtocol: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Port(self, portNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Port(self, portNumber: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Scope(self, scope: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Scope(self, scope: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoteAddresses(self, remoteAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RemoteAddresses(self, remoteAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_BuiltIn(self, builtIn: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwOpenPorts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c0e9d7fa-e07e-430a-b19a-090ce82d92e2}')
    @commethod(7)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, port: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPort_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, portNumber: Int32, ipProtocol: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, portNumber: Int32, ipProtocol: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, openPort: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPort_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(self, newEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d46d2478-9ac9-4008-9dc7-5563ce5536cc}')
    @commethod(7)
    def get_CurrentProfile(self, profile: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProfile_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProfileByType(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE, profile: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProfile_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwPolicy2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{98325047-c671-4174-8d81-defcd3f03186}')
    @commethod(7)
    def get_CurrentProfileTypes(self, profileTypesBitmask: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirewallEnabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FirewallEnabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExcludedInterfaces(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, interfaces: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ExcludedInterfaces(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, interfaces: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_BlockAllInboundTraffic(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, Block: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_BlockAllInboundTraffic(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, Block: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NotificationsDisabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_NotificationsDisabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UnicastResponsesToMulticastBroadcastDisabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_UnicastResponsesToMulticastBroadcastDisabled(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Rules(self, rules: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRules_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ServiceRestriction(self, ServiceRestriction: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnableRuleGroup(self, profileTypesBitmask: Int32, group: win32more.Windows.Win32.Foundation.BSTR, enable: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsRuleGroupEnabled(self, profileTypesBitmask: Int32, group: win32more.Windows.Win32.Foundation.BSTR, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RestoreLocalFirewallDefaults(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_DefaultInboundAction(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_DefaultInboundAction(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_DefaultOutboundAction(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_DefaultOutboundAction(self, profileType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_IsRuleGroupCurrentlyEnabled(self, group: win32more.Windows.Win32.Foundation.BSTR, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_LocalPolicyModifyState(self, modifyState: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_MODIFY_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwProduct(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{71881699-18f4-458b-b892-3ffce5e07f75}')
    @commethod(7)
    def get_RuleCategories(self, ruleCategories: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_RuleCategories(self, ruleCategories: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DisplayName(self, displayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DisplayName(self, displayName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PathToSignedProductExe(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwProducts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{39eb36e0-2097-40bd-8af2-63a13b525362}')
    @commethod(7)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Register(self, product: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProduct_head, registration: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, index: Int32, product: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProduct_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(self, newEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwProfile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{174a0dda-e9f9-449d-993b-21ab667ca456}')
    @commethod(7)
    def get_Type(self, type: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirewallEnabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FirewallEnabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExceptionsNotAllowed(self, notAllowed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ExceptionsNotAllowed(self, notAllowed: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_NotificationsDisabled(self, disabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_NotificationsDisabled(self, disabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_UnicastResponsesToMulticastBroadcastDisabled(self, disabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_UnicastResponsesToMulticastBroadcastDisabled(self, disabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RemoteAdminSettings(self, remoteAdminSettings: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_IcmpSettings(self, icmpSettings: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_GloballyOpenPorts(self, openPorts: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Services(self, services: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwServices_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_AuthorizedApplications(self, apps: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwRemoteAdminSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d4becddf-6f73-4a83-b832-9c66874cd20e}')
    @commethod(7)
    def get_IpVersion(self, ipVersion: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_IpVersion(self, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Scope(self, scope: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Scope(self, scope: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RemoteAddresses(self, remoteAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_RemoteAddresses(self, remoteAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwRule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{af230d27-baba-4e42-aced-f524f22cfce2}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, desc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, desc: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationName(self, imageFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationName(self, imageFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ServiceName(self, serviceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ServiceName(self, serviceName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Protocol(self, protocol: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Protocol(self, protocol: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_LocalPorts(self, portNumbers: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_LocalPorts(self, portNumbers: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RemotePorts(self, portNumbers: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_RemotePorts(self, portNumbers: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_LocalAddresses(self, localAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_LocalAddresses(self, localAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RemoteAddresses(self, remoteAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_RemoteAddresses(self, remoteAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_IcmpTypesAndCodes(self, icmpTypesAndCodes: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_IcmpTypesAndCodes(self, icmpTypesAndCodes: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Direction(self, dir: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Direction(self, dir: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Interfaces(self, interfaces: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Interfaces(self, interfaces: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_InterfaceTypes(self, interfaceTypes: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_InterfaceTypes(self, interfaceTypes: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Grouping(self, context: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_Grouping(self, context: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_Profiles(self, profileTypesBitmask: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_Profiles(self, profileTypesBitmask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_EdgeTraversal(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_EdgeTraversal(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Action(self, action: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_Action(self, action: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwRule2(ComPtr):
    extends: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule
    _iid_ = Guid('{9c27c8da-189b-4dde-89f7-8b39a316782c}')
    @commethod(43)
    def get_EdgeTraversalOptions(self, lOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_EdgeTraversalOptions(self, lOptions: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwRule3(ComPtr):
    extends: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule2
    _iid_ = Guid('{b21563ff-d696-4222-ab46-4e89b73ab34a}')
    @commethod(45)
    def get_LocalAppPackageId(self, wszPackageId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_LocalAppPackageId(self, wszPackageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_LocalUserOwner(self, wszUserOwner: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_LocalUserOwner(self, wszUserOwner: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_LocalUserAuthorizedList(self, wszUserAuthList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_LocalUserAuthorizedList(self, wszUserAuthList: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_RemoteUserAuthorizedList(self, wszUserAuthList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_RemoteUserAuthorizedList(self, wszUserAuthList: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_RemoteMachineAuthorizedList(self, wszUserAuthList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_RemoteMachineAuthorizedList(self, wszUserAuthList: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_SecureFlags(self, lOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_SecureFlags(self, lOptions: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwRules(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9c4c6277-5027-441e-afae-ca1f542da009}')
    @commethod(7)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, rule: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, name: win32more.Windows.Win32.Foundation.BSTR, rule: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(self, newEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79fd57c8-908e-4a36-9888-d5b3f0a444cf}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Type(self, type: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Customized(self, customized: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_IpVersion(self, ipVersion: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_IpVersion(self, ipVersion: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Scope(self, scope: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Scope(self, scope: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_RemoteAddresses(self, remoteAddrs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_RemoteAddresses(self, remoteAddrs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_GloballyOpenPorts(self, openPorts: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwServiceRestriction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8267bbe3-f890-491c-b7b6-2db1ef0e5d2b}')
    @commethod(7)
    def RestrictService(self, serviceName: win32more.Windows.Win32.Foundation.BSTR, appName: win32more.Windows.Win32.Foundation.BSTR, restrictService: win32more.Windows.Win32.Foundation.VARIANT_BOOL, serviceSidRestricted: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ServiceRestricted(self, serviceName: win32more.Windows.Win32.Foundation.BSTR, appName: win32more.Windows.Win32.Foundation.BSTR, serviceRestricted: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rules(self, rules: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRules_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetFwServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79649bb4-903e-421b-94c9-79848e79f6ee}')
    @commethod(7)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, svcType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE, service: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetFwService_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, newEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c08956b6-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(7)
    def get_SharingEnabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SharingConnectionType(self, pType: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DisableSharing(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableSharing(self, Type: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternetFirewallEnabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisableInternetFirewall(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableInternetFirewall(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_EnumPortMappings(self, Flags: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddPortMapping(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, ucIPProtocol: Byte, usExternalPort: UInt16, usInternalPort: UInt16, dwOptions: UInt32, bstrTargetNameOrIPAddress: win32more.Windows.Win32.Foundation.BSTR, eTargetType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.ICS_TARGETTYPE, ppMapping: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemovePortMapping(self, pMapping: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingEveryConnectionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{33c4643c-7811-46fa-a89a-768597bd7223}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c08956b7-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(7)
    def get_SharingInstalled(self, pbInstalled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_EnumPublicConnections(self, Flags: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EnumPrivateConnections(self, Flags: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_INetSharingConfigurationForINetConnection(self, pNetConnection: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head, ppNetSharingConfiguration: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_EnumEveryConnection(self, ppColl: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_NetConnectionProps(self, pNetConnection: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head, ppProps: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetConnectionProps_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c08956b1-1cd3-11d1-b1c5-00805fc1270e}')
    @commethod(7)
    def Disable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Enable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Properties(self, ppNSPMP: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMappingCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{02e4a2de-da20-4e34-89c8-ac22275a010b}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMappingProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{24b7e9b5-e38f-4685-851b-00892cf5f940}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IPProtocol(self, pucIPProt: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExternalPort(self, pusPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InternalPort(self, pusPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Options(self, pdwOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TargetName(self, pbstrTargetName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TargetIPAddress(self, pbstrTargetIPAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Enabled(self, pbool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingPrivateConnectionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{38ae69e0-4409-402a-a2cb-e965c727f840}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetSharingPublicConnectionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7d7a6355-f372-4971-a149-bfc927be762a}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStaticPortMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6f10711f-729b-41e5-93b8-f21d0f818df1}')
    @commethod(7)
    def get_ExternalIPAddress(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ExternalPort(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InternalPort(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Protocol(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternalClient(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Enabled(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EditInternalClient(self, bstrInternalClient: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Enable(self, vb: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EditDescription(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EditInternalPort(self, lInternalPort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStaticPortMappingCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cd1f3e77-66d6-4664-82c7-36dbb641d0f1}')
    @commethod(7)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, ppSPM: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, lExternalPort: Int32, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, lInternalPort: Int32, bstrInternalClient: win32more.Windows.Win32.Foundation.BSTR, bEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrDescription: win32more.Windows.Win32.Foundation.BSTR, ppSPM: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMapping_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPNAT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b171c812-cc76-485a-94d8-b6b3a2794e99}')
    @commethod(7)
    def get_StaticPortMappingCollection(self, ppSPMs: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DynamicPortMappingCollection(self, ppDPMs: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NATEventManager(self, ppNEM: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INATEventManager_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
NETCONMGR_ENUM_FLAGS = Int32
NCME_DEFAULT: NETCONMGR_ENUM_FLAGS = 0
NCME_HIDDEN: NETCONMGR_ENUM_FLAGS = 1
NETCONUI_CONNECT_FLAGS = Int32
NCUC_DEFAULT: NETCONUI_CONNECT_FLAGS = 0
NCUC_NO_UI: NETCONUI_CONNECT_FLAGS = 1
NCUC_ENABLE_DISABLE: NETCONUI_CONNECT_FLAGS = 2
NETCON_CHARACTERISTIC_FLAGS = Int32
NCCF_NONE: NETCON_CHARACTERISTIC_FLAGS = 0
NCCF_ALL_USERS: NETCON_CHARACTERISTIC_FLAGS = 1
NCCF_ALLOW_DUPLICATION: NETCON_CHARACTERISTIC_FLAGS = 2
NCCF_ALLOW_REMOVAL: NETCON_CHARACTERISTIC_FLAGS = 4
NCCF_ALLOW_RENAME: NETCON_CHARACTERISTIC_FLAGS = 8
NCCF_INCOMING_ONLY: NETCON_CHARACTERISTIC_FLAGS = 32
NCCF_OUTGOING_ONLY: NETCON_CHARACTERISTIC_FLAGS = 64
NCCF_BRANDED: NETCON_CHARACTERISTIC_FLAGS = 128
NCCF_SHARED: NETCON_CHARACTERISTIC_FLAGS = 256
NCCF_BRIDGED: NETCON_CHARACTERISTIC_FLAGS = 512
NCCF_FIREWALLED: NETCON_CHARACTERISTIC_FLAGS = 1024
NCCF_DEFAULT: NETCON_CHARACTERISTIC_FLAGS = 2048
NCCF_HOMENET_CAPABLE: NETCON_CHARACTERISTIC_FLAGS = 4096
NCCF_SHARED_PRIVATE: NETCON_CHARACTERISTIC_FLAGS = 8192
NCCF_QUARANTINED: NETCON_CHARACTERISTIC_FLAGS = 16384
NCCF_RESERVED: NETCON_CHARACTERISTIC_FLAGS = 32768
NCCF_HOSTED_NETWORK: NETCON_CHARACTERISTIC_FLAGS = 65536
NCCF_VIRTUAL_STATION: NETCON_CHARACTERISTIC_FLAGS = 131072
NCCF_WIFI_DIRECT: NETCON_CHARACTERISTIC_FLAGS = 262144
NCCF_BLUETOOTH_MASK: NETCON_CHARACTERISTIC_FLAGS = 983040
NCCF_LAN_MASK: NETCON_CHARACTERISTIC_FLAGS = 15728640
NETCON_MEDIATYPE = Int32
NCM_NONE: NETCON_MEDIATYPE = 0
NCM_DIRECT: NETCON_MEDIATYPE = 1
NCM_ISDN: NETCON_MEDIATYPE = 2
NCM_LAN: NETCON_MEDIATYPE = 3
NCM_PHONE: NETCON_MEDIATYPE = 4
NCM_TUNNEL: NETCON_MEDIATYPE = 5
NCM_PPPOE: NETCON_MEDIATYPE = 6
NCM_BRIDGE: NETCON_MEDIATYPE = 7
NCM_SHAREDACCESSHOST_LAN: NETCON_MEDIATYPE = 8
NCM_SHAREDACCESSHOST_RAS: NETCON_MEDIATYPE = 9
class NETCON_PROPERTIES(EasyCastStructure):
    guidId: Guid
    pszwName: win32more.Windows.Win32.Foundation.PWSTR
    pszwDeviceName: win32more.Windows.Win32.Foundation.PWSTR
    Status: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_STATUS
    MediaType: win32more.Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE
    dwCharacter: UInt32
    clsidThisObject: Guid
    clsidUiObject: Guid
NETCON_STATUS = Int32
NCS_DISCONNECTED: NETCON_STATUS = 0
NCS_CONNECTING: NETCON_STATUS = 1
NCS_CONNECTED: NETCON_STATUS = 2
NCS_DISCONNECTING: NETCON_STATUS = 3
NCS_HARDWARE_NOT_PRESENT: NETCON_STATUS = 4
NCS_HARDWARE_DISABLED: NETCON_STATUS = 5
NCS_HARDWARE_MALFUNCTION: NETCON_STATUS = 6
NCS_MEDIA_DISCONNECTED: NETCON_STATUS = 7
NCS_AUTHENTICATING: NETCON_STATUS = 8
NCS_AUTHENTICATION_SUCCEEDED: NETCON_STATUS = 9
NCS_AUTHENTICATION_FAILED: NETCON_STATUS = 10
NCS_INVALID_ADDRESS: NETCON_STATUS = 11
NCS_CREDENTIALS_REQUIRED: NETCON_STATUS = 12
NCS_ACTION_REQUIRED: NETCON_STATUS = 13
NCS_ACTION_REQUIRED_RETRY: NETCON_STATUS = 14
NCS_CONNECT_FAILED: NETCON_STATUS = 15
NETCON_TYPE = Int32
NCT_DIRECT_CONNECT: NETCON_TYPE = 0
NCT_INBOUND: NETCON_TYPE = 1
NCT_INTERNET: NETCON_TYPE = 2
NCT_LAN: NETCON_TYPE = 3
NCT_PHONE: NETCON_TYPE = 4
NCT_TUNNEL: NETCON_TYPE = 5
NCT_BRIDGE: NETCON_TYPE = 6
NETISO_ERROR_TYPE = Int32
NETISO_ERROR_TYPE_NONE: NETISO_ERROR_TYPE = 0
NETISO_ERROR_TYPE_PRIVATE_NETWORK: NETISO_ERROR_TYPE = 1
NETISO_ERROR_TYPE_INTERNET_CLIENT: NETISO_ERROR_TYPE = 2
NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER: NETISO_ERROR_TYPE = 3
NETISO_ERROR_TYPE_MAX: NETISO_ERROR_TYPE = 4
NETISO_FLAG = Int32
NETISO_FLAG_FORCE_COMPUTE_BINARIES: NETISO_FLAG = 1
NETISO_FLAG_MAX: NETISO_FLAG = 2
NET_FW_ACTION = Int32
NET_FW_ACTION_BLOCK: NET_FW_ACTION = 0
NET_FW_ACTION_ALLOW: NET_FW_ACTION = 1
NET_FW_ACTION_MAX: NET_FW_ACTION = 2
NET_FW_AUTHENTICATE_TYPE = Int32
NET_FW_AUTHENTICATE_NONE: NET_FW_AUTHENTICATE_TYPE = 0
NET_FW_AUTHENTICATE_NO_ENCAPSULATION: NET_FW_AUTHENTICATE_TYPE = 1
NET_FW_AUTHENTICATE_WITH_INTEGRITY: NET_FW_AUTHENTICATE_TYPE = 2
NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION: NET_FW_AUTHENTICATE_TYPE = 3
NET_FW_AUTHENTICATE_AND_ENCRYPT: NET_FW_AUTHENTICATE_TYPE = 4
NET_FW_EDGE_TRAVERSAL_TYPE = Int32
NET_FW_EDGE_TRAVERSAL_TYPE_DENY: NET_FW_EDGE_TRAVERSAL_TYPE = 0
NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW: NET_FW_EDGE_TRAVERSAL_TYPE = 1
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP: NET_FW_EDGE_TRAVERSAL_TYPE = 2
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER: NET_FW_EDGE_TRAVERSAL_TYPE = 3
NET_FW_IP_PROTOCOL = Int32
NET_FW_IP_PROTOCOL_TCP: NET_FW_IP_PROTOCOL = 6
NET_FW_IP_PROTOCOL_UDP: NET_FW_IP_PROTOCOL = 17
NET_FW_IP_PROTOCOL_ANY: NET_FW_IP_PROTOCOL = 256
NET_FW_IP_VERSION = Int32
NET_FW_IP_VERSION_V4: NET_FW_IP_VERSION = 0
NET_FW_IP_VERSION_V6: NET_FW_IP_VERSION = 1
NET_FW_IP_VERSION_ANY: NET_FW_IP_VERSION = 2
NET_FW_IP_VERSION_MAX: NET_FW_IP_VERSION = 3
NET_FW_MODIFY_STATE = Int32
NET_FW_MODIFY_STATE_OK: NET_FW_MODIFY_STATE = 0
NET_FW_MODIFY_STATE_GP_OVERRIDE: NET_FW_MODIFY_STATE = 1
NET_FW_MODIFY_STATE_INBOUND_BLOCKED: NET_FW_MODIFY_STATE = 2
NET_FW_POLICY_TYPE = Int32
NET_FW_POLICY_GROUP: NET_FW_POLICY_TYPE = 0
NET_FW_POLICY_LOCAL: NET_FW_POLICY_TYPE = 1
NET_FW_POLICY_EFFECTIVE: NET_FW_POLICY_TYPE = 2
NET_FW_POLICY_TYPE_MAX: NET_FW_POLICY_TYPE = 3
NET_FW_PROFILE_TYPE = Int32
NET_FW_PROFILE_DOMAIN: NET_FW_PROFILE_TYPE = 0
NET_FW_PROFILE_STANDARD: NET_FW_PROFILE_TYPE = 1
NET_FW_PROFILE_CURRENT: NET_FW_PROFILE_TYPE = 2
NET_FW_PROFILE_TYPE_MAX: NET_FW_PROFILE_TYPE = 3
NET_FW_PROFILE_TYPE2 = Int32
NET_FW_PROFILE2_DOMAIN: NET_FW_PROFILE_TYPE2 = 1
NET_FW_PROFILE2_PRIVATE: NET_FW_PROFILE_TYPE2 = 2
NET_FW_PROFILE2_PUBLIC: NET_FW_PROFILE_TYPE2 = 4
NET_FW_PROFILE2_ALL: NET_FW_PROFILE_TYPE2 = 2147483647
NET_FW_RULE_CATEGORY = Int32
NET_FW_RULE_CATEGORY_BOOT: NET_FW_RULE_CATEGORY = 0
NET_FW_RULE_CATEGORY_STEALTH: NET_FW_RULE_CATEGORY = 1
NET_FW_RULE_CATEGORY_FIREWALL: NET_FW_RULE_CATEGORY = 2
NET_FW_RULE_CATEGORY_CONSEC: NET_FW_RULE_CATEGORY = 3
NET_FW_RULE_CATEGORY_MAX: NET_FW_RULE_CATEGORY = 4
NET_FW_RULE_DIRECTION = Int32
NET_FW_RULE_DIR_IN: NET_FW_RULE_DIRECTION = 1
NET_FW_RULE_DIR_OUT: NET_FW_RULE_DIRECTION = 2
NET_FW_RULE_DIR_MAX: NET_FW_RULE_DIRECTION = 3
NET_FW_SCOPE = Int32
NET_FW_SCOPE_ALL: NET_FW_SCOPE = 0
NET_FW_SCOPE_LOCAL_SUBNET: NET_FW_SCOPE = 1
NET_FW_SCOPE_CUSTOM: NET_FW_SCOPE = 2
NET_FW_SCOPE_MAX: NET_FW_SCOPE = 3
NET_FW_SERVICE_TYPE = Int32
NET_FW_SERVICE_FILE_AND_PRINT: NET_FW_SERVICE_TYPE = 0
NET_FW_SERVICE_UPNP: NET_FW_SERVICE_TYPE = 1
NET_FW_SERVICE_REMOTE_DESKTOP: NET_FW_SERVICE_TYPE = 2
NET_FW_SERVICE_NONE: NET_FW_SERVICE_TYPE = 3
NET_FW_SERVICE_TYPE_MAX: NET_FW_SERVICE_TYPE = 4
NetFwAuthorizedApplication = Guid('{ec9846b3-2762-4a6b-a214-6acb603462d2}')
NetFwMgr = Guid('{304ce942-6e39-40d8-943a-b913c40c9cd4}')
NetFwOpenPort = Guid('{0ca545c6-37ad-4a6c-bf92-9f7610067ef5}')
NetFwPolicy2 = Guid('{e2b3c97f-6ae1-41ac-817a-f6f92166d7dd}')
NetFwProduct = Guid('{9d745ed8-c514-4d1d-bf42-751fed2d5ac7}')
NetFwProducts = Guid('{cc19079b-8272-4d73-bb70-cdb533527b61}')
NetFwRule = Guid('{2c5bc43e-3369-4c33-ab0c-be9469677af4}')
NetSharingManager = Guid('{5c63c1ad-3956-4ff8-8486-40034758315b}')
@winfunctype_pointer
def PAC_CHANGES_CALLBACK_FN(context: VoidPtr, pChange: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head)) -> Void: ...
@winfunctype_pointer
def PFN_FWADDDYNAMICKEYWORDADDRESS0(dynamicKeywordAddress: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0_head)) -> UInt32: ...
@winfunctype_pointer
def PFN_FWDELETEDYNAMICKEYWORDADDRESS0(dynamicKeywordAddressId: Guid) -> UInt32: ...
@winfunctype_pointer
def PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0(dynamicKeywordAddressId: Guid, dynamicKeywordAddressData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head))) -> UInt32: ...
@winfunctype_pointer
def PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0(flags: UInt32, dynamicKeywordAddressData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head))) -> UInt32: ...
@winfunctype_pointer
def PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0(dynamicKeywordAddressData: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)) -> UInt32: ...
@winfunctype_pointer
def PFN_FWUPDATEDYNAMICKEYWORDADDRESS0(dynamicKeywordAddressId: Guid, updatedAddresses: win32more.Windows.Win32.Foundation.PWSTR, append: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PNETISO_EDP_ID_CALLBACK_FN(context: VoidPtr, wszEnterpriseId: win32more.Windows.Win32.Foundation.PWSTR, dwErr: UInt32) -> Void: ...
SHARINGCONNECTIONTYPE = Int32
ICSSHARINGTYPE_PUBLIC: SHARINGCONNECTIONTYPE = 0
ICSSHARINGTYPE_PRIVATE: SHARINGCONNECTIONTYPE = 1
SHARINGCONNECTION_ENUM_FLAGS = Int32
ICSSC_DEFAULT: SHARINGCONNECTION_ENUM_FLAGS = 0
ICSSC_ENABLED: SHARINGCONNECTION_ENUM_FLAGS = 1
UPnPNAT = Guid('{ae1e00aa-3fd5-403c-8a27-2bbdc30cd0e1}')
make_head(_module, 'FW_DYNAMIC_KEYWORD_ADDRESS0')
make_head(_module, 'FW_DYNAMIC_KEYWORD_ADDRESS_DATA0')
make_head(_module, 'IDynamicPortMapping')
make_head(_module, 'IDynamicPortMappingCollection')
make_head(_module, 'IEnumNetConnection')
make_head(_module, 'IEnumNetSharingEveryConnection')
make_head(_module, 'IEnumNetSharingPortMapping')
make_head(_module, 'IEnumNetSharingPrivateConnection')
make_head(_module, 'IEnumNetSharingPublicConnection')
make_head(_module, 'INATEventManager')
make_head(_module, 'INATExternalIPAddressCallback')
make_head(_module, 'INATNumberOfEntriesCallback')
make_head(_module, 'INET_FIREWALL_AC_BINARIES')
make_head(_module, 'INET_FIREWALL_AC_CAPABILITIES')
make_head(_module, 'INET_FIREWALL_AC_CHANGE')
make_head(_module, 'INET_FIREWALL_APP_CONTAINER')
make_head(_module, 'INetConnection')
make_head(_module, 'INetConnectionConnectUi')
make_head(_module, 'INetConnectionManager')
make_head(_module, 'INetConnectionProps')
make_head(_module, 'INetFwAuthorizedApplication')
make_head(_module, 'INetFwAuthorizedApplications')
make_head(_module, 'INetFwIcmpSettings')
make_head(_module, 'INetFwMgr')
make_head(_module, 'INetFwOpenPort')
make_head(_module, 'INetFwOpenPorts')
make_head(_module, 'INetFwPolicy')
make_head(_module, 'INetFwPolicy2')
make_head(_module, 'INetFwProduct')
make_head(_module, 'INetFwProducts')
make_head(_module, 'INetFwProfile')
make_head(_module, 'INetFwRemoteAdminSettings')
make_head(_module, 'INetFwRule')
make_head(_module, 'INetFwRule2')
make_head(_module, 'INetFwRule3')
make_head(_module, 'INetFwRules')
make_head(_module, 'INetFwService')
make_head(_module, 'INetFwServiceRestriction')
make_head(_module, 'INetFwServices')
make_head(_module, 'INetSharingConfiguration')
make_head(_module, 'INetSharingEveryConnectionCollection')
make_head(_module, 'INetSharingManager')
make_head(_module, 'INetSharingPortMapping')
make_head(_module, 'INetSharingPortMappingCollection')
make_head(_module, 'INetSharingPortMappingProps')
make_head(_module, 'INetSharingPrivateConnectionCollection')
make_head(_module, 'INetSharingPublicConnectionCollection')
make_head(_module, 'IStaticPortMapping')
make_head(_module, 'IStaticPortMappingCollection')
make_head(_module, 'IUPnPNAT')
make_head(_module, 'NETCON_PROPERTIES')
make_head(_module, 'PAC_CHANGES_CALLBACK_FN')
make_head(_module, 'PFN_FWADDDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PFN_FWDELETEDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0')
make_head(_module, 'PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0')
make_head(_module, 'PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0')
make_head(_module, 'PFN_FWUPDATEDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PNETISO_EDP_ID_CALLBACK_FN')
