from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.ClrHosting
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Threading
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
APPDOMAIN_SECURITY_FLAGS = Int32
APPDOMAIN_SECURITY_DEFAULT: APPDOMAIN_SECURITY_FLAGS = 0
APPDOMAIN_SECURITY_SANDBOXED: APPDOMAIN_SECURITY_FLAGS = 1
APPDOMAIN_SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE: APPDOMAIN_SECURITY_FLAGS = 2
APPDOMAIN_FORCE_TRIVIAL_WAIT_OPERATIONS: APPDOMAIN_SECURITY_FLAGS = 8
DEPRECATED_CLR_API_MESG: String = 'This API has been deprecated. Refer to https://go.microsoft.com/fwlink/?LinkId=143720 for more details.'
CLR_MAJOR_VERSION: UInt32 = 4
CLR_MINOR_VERSION: UInt32 = 0
CLR_BUILD_VERSION: UInt32 = 30319
CLR_ASSEMBLY_MAJOR_VERSION: UInt32 = 4
CLR_ASSEMBLY_MINOR_VERSION: UInt32 = 0
CLR_ASSEMBLY_BUILD_VERSION: UInt32 = 0
BucketParamsCount: UInt32 = 10
BucketParamLength: UInt32 = 255
LIBID_mscoree: Guid = Guid('{5477469e-83b1-11d2-8b49-00a0c9b7c9c4}')
CLSID_CLRStrongName: Guid = Guid('{b79b0acd-f5cd-409b-b5a5-a16244610b92}')
CLSID_CLRMetaHost: Guid = Guid('{9280188d-0e8e-4867-b30c-7fa83884e8de}')
CLSID_CLRMetaHostPolicy: Guid = Guid('{2ebcd49a-1b47-4a61-b13a-4a03701e594b}')
CLSID_CLRDebugging: Guid = Guid('{bacc578d-fbdd-48a4-969f-02d932b74634}')
CLSID_CLRDebuggingLegacy: Guid = Guid('{df8395b5-a4ba-450b-a77c-a9a47762c520}')
CLSID_CLRProfiling: Guid = Guid('{bd097ed8-733e-43fe-8ed7-a95ff9a8448c}')
@winfunctype('MSCorEE.dll')
def GetCORSystemDirectory(pbuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetCORVersion(pbBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetFileVersion(szFilename: win32more.Windows.Win32.Foundation.PWSTR, szBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetCORRequiredVersion(pbuffer: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetRequestedRuntimeInfo(pExe: win32more.Windows.Win32.Foundation.PWSTR, pwszVersion: win32more.Windows.Win32.Foundation.PWSTR, pConfigurationFile: win32more.Windows.Win32.Foundation.PWSTR, startupFlags: UInt32, runtimeInfoFlags: UInt32, pDirectory: win32more.Windows.Win32.Foundation.PWSTR, dwDirectory: UInt32, dwDirectoryLength: POINTER(UInt32), pVersion: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwlength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetRequestedRuntimeVersion(pExe: win32more.Windows.Win32.Foundation.PWSTR, pVersion: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorBindToRuntimeHost(pwszVersion: win32more.Windows.Win32.Foundation.PWSTR, pwszBuildFlavor: win32more.Windows.Win32.Foundation.PWSTR, pwszHostConfigFile: win32more.Windows.Win32.Foundation.PWSTR, pReserved: VoidPtr, startupFlags: UInt32, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorBindToRuntimeEx(pwszVersion: win32more.Windows.Win32.Foundation.PWSTR, pwszBuildFlavor: win32more.Windows.Win32.Foundation.PWSTR, startupFlags: UInt32, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorBindToRuntimeByCfg(pCfgStream: win32more.Windows.Win32.System.Com.IStream_head, reserved: UInt32, startupFlags: UInt32, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorBindToRuntime(pwszVersion: win32more.Windows.Win32.Foundation.PWSTR, pwszBuildFlavor: win32more.Windows.Win32.Foundation.PWSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorBindToCurrentRuntime(pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def ClrCreateManagedInstance(pTypeName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorMarkThreadInThreadPool() -> Void: ...
@winfunctype('MSCorEE.dll')
def RunDll32ShimW(hwnd: win32more.Windows.Win32.Foundation.HWND, hinst: win32more.Windows.Win32.Foundation.HINSTANCE, lpszCmdLine: win32more.Windows.Win32.Foundation.PWSTR, nCmdShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def LoadLibraryShim(szDllName: win32more.Windows.Win32.Foundation.PWSTR, szVersion: win32more.Windows.Win32.Foundation.PWSTR, pvReserved: VoidPtr, phModDll: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CallFunctionShim(szDllName: win32more.Windows.Win32.Foundation.PWSTR, szFunctionName: win32more.Windows.Win32.Foundation.PSTR, lpvArgument1: VoidPtr, lpvArgument2: VoidPtr, szVersion: win32more.Windows.Win32.Foundation.PWSTR, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetRealProcAddress(pwszProcName: win32more.Windows.Win32.Foundation.PSTR, ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorExitProcess(exitCode: Int32) -> Void: ...
@winfunctype('MSCorEE.dll')
def LoadStringRC(iResouceID: UInt32, szBuffer: win32more.Windows.Win32.Foundation.PWSTR, iMax: Int32, bQuiet: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def LoadStringRCEx(lcid: UInt32, iResouceID: UInt32, szBuffer: win32more.Windows.Win32.Foundation.PWSTR, iMax: Int32, bQuiet: Int32, pcwchUsed: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def LockClrVersion(hostCallback: win32more.Windows.Win32.System.ClrHosting.FLockClrVersionCallback, pBeginHostSetup: POINTER(win32more.Windows.Win32.System.ClrHosting.FLockClrVersionCallback), pEndHostSetup: POINTER(win32more.Windows.Win32.System.ClrHosting.FLockClrVersionCallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CreateDebuggingInterfaceFromVersion(iDebuggerVersion: Int32, szDebuggeeVersion: win32more.Windows.Win32.Foundation.PWSTR, ppCordb: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetVersionFromProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pVersion: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CorLaunchApplication(dwClickOnceHost: win32more.Windows.Win32.System.ClrHosting.HOST_TYPE, pwzAppFullName: win32more.Windows.Win32.Foundation.PWSTR, dwManifestPaths: UInt32, ppwzManifestPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwActivationData: UInt32, ppwzActivationData: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetRequestedRuntimeVersionForCLSID(rclsid: POINTER(Guid), pVersion: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, dwLength: POINTER(UInt32), dwResolutionFlags: win32more.Windows.Win32.System.ClrHosting.CLSID_RESOLUTION_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def GetCLRIdentityManager(riid: POINTER(Guid), ppManager: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSCorEE.dll')
def CLRCreateInstance(clsid: POINTER(Guid), riid: POINTER(Guid), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class AssemblyBindInfo(EasyCastStructure):
    dwAppDomainId: UInt32
    lpReferencedIdentity: win32more.Windows.Win32.Foundation.PWSTR
    lpPostPolicyIdentity: win32more.Windows.Win32.Foundation.PWSTR
    ePolicyLevel: UInt32
BucketParameterIndex = Int32
BucketParameterIndex_Parameter1: BucketParameterIndex = 0
BucketParameterIndex_Parameter2: BucketParameterIndex = 1
BucketParameterIndex_Parameter3: BucketParameterIndex = 2
BucketParameterIndex_Parameter4: BucketParameterIndex = 3
BucketParameterIndex_Parameter5: BucketParameterIndex = 4
BucketParameterIndex_Parameter6: BucketParameterIndex = 5
BucketParameterIndex_Parameter7: BucketParameterIndex = 6
BucketParameterIndex_Parameter8: BucketParameterIndex = 7
BucketParameterIndex_Parameter9: BucketParameterIndex = 8
BucketParameterIndex_InvalidBucketParamIndex: BucketParameterIndex = 9
class BucketParameters(EasyCastStructure):
    fInited: win32more.Windows.Win32.Foundation.BOOL
    pszEventTypeName: Char * 255
    pszParams: Char * 2550
@winfunctype_pointer
def CLRCreateInstanceFnPtr(clsid: POINTER(Guid), riid: POINTER(Guid), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
CLRRuntimeHost = Guid('{90f1a06e-7712-4762-86b5-7a5eba6bdb02}')
CLR_DEBUGGING_PROCESS_FLAGS = Int32
CLR_DEBUGGING_MANAGED_EVENT_PENDING: CLR_DEBUGGING_PROCESS_FLAGS = 1
CLR_DEBUGGING_MANAGED_EVENT_DEBUGGER_LAUNCH: CLR_DEBUGGING_PROCESS_FLAGS = 2
class CLR_DEBUGGING_VERSION(EasyCastStructure):
    wStructVersion: UInt16
    wMajor: UInt16
    wMinor: UInt16
    wBuild: UInt16
    wRevision: UInt16
CLSID_RESOLUTION_FLAGS = Int32
CLSID_RESOLUTION_DEFAULT: CLSID_RESOLUTION_FLAGS = 0
CLSID_RESOLUTION_REGISTERED: CLSID_RESOLUTION_FLAGS = 1
class COR_GC_STATS(EasyCastStructure):
    Flags: UInt32
    ExplicitGCCount: UIntPtr
    GenCollectionsTaken: UIntPtr * 3
    CommittedKBytes: UIntPtr
    ReservedKBytes: UIntPtr
    Gen0HeapSizeKBytes: UIntPtr
    Gen1HeapSizeKBytes: UIntPtr
    Gen2HeapSizeKBytes: UIntPtr
    LargeObjectHeapSizeKBytes: UIntPtr
    KBytesPromotedFromGen0: UIntPtr
    KBytesPromotedFromGen1: UIntPtr
COR_GC_STAT_TYPES = Int32
COR_GC_COUNTS: COR_GC_STAT_TYPES = 1
COR_GC_MEMORYUSAGE: COR_GC_STAT_TYPES = 2
class COR_GC_THREAD_STATS(EasyCastStructure):
    PerThreadAllocation: UInt64
    Flags: UInt32
COR_GC_THREAD_STATS_TYPES = Int32
COR_GC_THREAD_HAS_PROMOTED_BYTES: COR_GC_THREAD_STATS_TYPES = 1
@winfunctype_pointer
def CallbackThreadSetFnPtr() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def CallbackThreadUnsetFnPtr() -> win32more.Windows.Win32.Foundation.HRESULT: ...
ComCallUnmarshal = Guid('{3f281000-e95a-11d2-886b-00c04f869f04}')
ComCallUnmarshalV4 = Guid('{45fb4600-e6e8-4928-b25e-50476ff79425}')
CorRuntimeHost = Guid('{cb2f6723-ab3a-11d2-9c40-00c04fa30a3e}')
@winfunctype_pointer
def CreateInterfaceFnPtr(clsid: POINTER(Guid), riid: POINTER(Guid), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class CustomDumpItem(EasyCastStructure):
    itemKind: win32more.Windows.Win32.System.ClrHosting.ECustomDumpItemKind
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pReserved: UIntPtr
EApiCategories = Int32
EApiCategories_eNoChecks: EApiCategories = 0
EApiCategories_eSynchronization: EApiCategories = 1
EApiCategories_eSharedState: EApiCategories = 2
EApiCategories_eExternalProcessMgmt: EApiCategories = 4
EApiCategories_eSelfAffectingProcessMgmt: EApiCategories = 8
EApiCategories_eExternalThreading: EApiCategories = 16
EApiCategories_eSelfAffectingThreading: EApiCategories = 32
EApiCategories_eSecurityInfrastructure: EApiCategories = 64
EApiCategories_eUI: EApiCategories = 128
EApiCategories_eMayLeakOnAbort: EApiCategories = 256
EApiCategories_eAll: EApiCategories = 511
EBindPolicyLevels = Int32
EBindPolicyLevels_ePolicyLevelNone: EBindPolicyLevels = 0
EBindPolicyLevels_ePolicyLevelRetargetable: EBindPolicyLevels = 1
EBindPolicyLevels_ePolicyUnifiedToCLR: EBindPolicyLevels = 2
EBindPolicyLevels_ePolicyLevelApp: EBindPolicyLevels = 4
EBindPolicyLevels_ePolicyLevelPublisher: EBindPolicyLevels = 8
EBindPolicyLevels_ePolicyLevelHost: EBindPolicyLevels = 16
EBindPolicyLevels_ePolicyLevelAdmin: EBindPolicyLevels = 32
EBindPolicyLevels_ePolicyPortability: EBindPolicyLevels = 64
ECLRAssemblyIdentityFlags = Int32
CLR_ASSEMBLY_IDENTITY_FLAGS_DEFAULT: ECLRAssemblyIdentityFlags = 0
EClrEvent = Int32
EClrEvent_Event_DomainUnload: EClrEvent = 0
EClrEvent_Event_ClrDisabled: EClrEvent = 1
EClrEvent_Event_MDAFired: EClrEvent = 2
EClrEvent_Event_StackOverflow: EClrEvent = 3
EClrEvent_MaxClrEvent: EClrEvent = 4
EClrFailure = Int32
EClrFailure_FAIL_NonCriticalResource: EClrFailure = 0
EClrFailure_FAIL_CriticalResource: EClrFailure = 1
EClrFailure_FAIL_FatalRuntime: EClrFailure = 2
EClrFailure_FAIL_OrphanedLock: EClrFailure = 3
EClrFailure_FAIL_StackOverflow: EClrFailure = 4
EClrFailure_FAIL_AccessViolation: EClrFailure = 5
EClrFailure_FAIL_CodeContract: EClrFailure = 6
EClrFailure_MaxClrFailure: EClrFailure = 7
EClrOperation = Int32
EClrOperation_OPR_ThreadAbort: EClrOperation = 0
EClrOperation_OPR_ThreadRudeAbortInNonCriticalRegion: EClrOperation = 1
EClrOperation_OPR_ThreadRudeAbortInCriticalRegion: EClrOperation = 2
EClrOperation_OPR_AppDomainUnload: EClrOperation = 3
EClrOperation_OPR_AppDomainRudeUnload: EClrOperation = 4
EClrOperation_OPR_ProcessExit: EClrOperation = 5
EClrOperation_OPR_FinalizerRun: EClrOperation = 6
EClrOperation_MaxClrOperation: EClrOperation = 7
EClrUnhandledException = Int32
EClrUnhandledException_eRuntimeDeterminedPolicy: EClrUnhandledException = 0
EClrUnhandledException_eHostDeterminedPolicy: EClrUnhandledException = 1
EContextType = Int32
EContextType_eCurrentContext: EContextType = 0
EContextType_eRestrictedContext: EContextType = 1
ECustomDumpFlavor = Int32
DUMP_FLAVOR_Mini: ECustomDumpFlavor = 0
DUMP_FLAVOR_CriticalCLRState: ECustomDumpFlavor = 1
DUMP_FLAVOR_NonHeapCLRState: ECustomDumpFlavor = 2
DUMP_FLAVOR_Default: ECustomDumpFlavor = 0
ECustomDumpItemKind = Int32
DUMP_ITEM_None: ECustomDumpItemKind = 0
EHostApplicationPolicy = Int32
HOST_APPLICATION_BINDING_POLICY: EHostApplicationPolicy = 1
EHostBindingPolicyModifyFlags = Int32
HOST_BINDING_POLICY_MODIFY_DEFAULT: EHostBindingPolicyModifyFlags = 0
HOST_BINDING_POLICY_MODIFY_CHAIN: EHostBindingPolicyModifyFlags = 1
HOST_BINDING_POLICY_MODIFY_REMOVE: EHostBindingPolicyModifyFlags = 2
HOST_BINDING_POLICY_MODIFY_MAX: EHostBindingPolicyModifyFlags = 3
EInitializeNewDomainFlags = Int32
eInitializeNewDomainFlags_None: EInitializeNewDomainFlags = 0
eInitializeNewDomainFlags_NoSecurityChanges: EInitializeNewDomainFlags = 2
EMemoryAvailable = Int32
EMemoryAvailable_eMemoryAvailableLow: EMemoryAvailable = 1
EMemoryAvailable_eMemoryAvailableNeutral: EMemoryAvailable = 2
EMemoryAvailable_eMemoryAvailableHigh: EMemoryAvailable = 3
EMemoryCriticalLevel = Int32
EMemoryCriticalLevel_eTaskCritical: EMemoryCriticalLevel = 0
EMemoryCriticalLevel_eAppDomainCritical: EMemoryCriticalLevel = 1
EMemoryCriticalLevel_eProcessCritical: EMemoryCriticalLevel = 2
EPolicyAction = Int32
EPolicyAction_eNoAction: EPolicyAction = 0
EPolicyAction_eThrowException: EPolicyAction = 1
EPolicyAction_eAbortThread: EPolicyAction = 2
EPolicyAction_eRudeAbortThread: EPolicyAction = 3
EPolicyAction_eUnloadAppDomain: EPolicyAction = 4
EPolicyAction_eRudeUnloadAppDomain: EPolicyAction = 5
EPolicyAction_eExitProcess: EPolicyAction = 6
EPolicyAction_eFastExitProcess: EPolicyAction = 7
EPolicyAction_eRudeExitProcess: EPolicyAction = 8
EPolicyAction_eDisableRuntime: EPolicyAction = 9
EPolicyAction_MaxPolicyAction: EPolicyAction = 10
ESymbolReadingPolicy = Int32
ESymbolReadingPolicy_eSymbolReadingNever: ESymbolReadingPolicy = 0
ESymbolReadingPolicy_eSymbolReadingAlways: ESymbolReadingPolicy = 1
ESymbolReadingPolicy_eSymbolReadingFullTrustOnly: ESymbolReadingPolicy = 2
ETaskType = Int32
TT_DEBUGGERHELPER: ETaskType = 1
TT_GC: ETaskType = 2
TT_FINALIZER: ETaskType = 4
TT_THREADPOOL_TIMER: ETaskType = 8
TT_THREADPOOL_GATE: ETaskType = 16
TT_THREADPOOL_WORKER: ETaskType = 32
TT_THREADPOOL_IOCOMPLETION: ETaskType = 64
TT_ADUNLOAD: ETaskType = 128
TT_USER: ETaskType = 256
TT_THREADPOOL_WAIT: ETaskType = 512
TT_UNKNOWN: ETaskType = -2147483648
@winfunctype_pointer
def FExecuteInAppDomainCallback(cookie: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def FLockClrVersionCallback() -> win32more.Windows.Win32.Foundation.HRESULT: ...
HOST_TYPE = Int32
HOST_TYPE_DEFAULT: HOST_TYPE = 0
HOST_TYPE_APPLAUNCH: HOST_TYPE = 1
HOST_TYPE_CORFLAG: HOST_TYPE = 2
class IActionOnCLREvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{607be24b-d91b-4e28-a242-61871ce56e35}')
    @commethod(3)
    def OnEvent(self, event: win32more.Windows.Win32.System.ClrHosting.EClrEvent, data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApartmentCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{178e5337-1528-4591-b1c9-1c6e484686d8}')
    @commethod(3)
    def DoCallback(self, pFunc: UIntPtr, pData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppDomainBinding(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c2b07a7-1e98-11d3-872f-00c04f79ed0d}')
    @commethod(3)
    def OnAppDomain(self, pAppdomain: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRAppDomainResourceMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c62de18c-2e23-4aea-8423-b40c1fc59eae}')
    @commethod(3)
    def GetCurrentAllocated(self, dwAppDomainId: UInt32, pBytesAllocated: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentSurvived(self, dwAppDomainId: UInt32, pAppDomainBytesSurvived: POINTER(UInt64), pTotalBytesSurvived: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentCpuTime(self, dwAppDomainId: UInt32, pMilliseconds: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRAssemblyIdentityManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{15f0a9da-3ff6-4393-9da9-fdfd284e6972}')
    @commethod(3)
    def GetCLRAssemblyReferenceList(self, ppwzAssemblyReferences: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwNumOfReferences: UInt32, ppReferenceList: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRAssemblyReferenceList_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBindingIdentityFromFile(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBindingIdentityFromStream(self, pStream: win32more.Windows.Win32.System.Com.IStream_head, dwFlags: UInt32, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReferencedAssembliesFromFile(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pExcludeAssembliesList: win32more.Windows.Win32.System.ClrHosting.ICLRAssemblyReferenceList_head, ppReferenceEnum: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRReferenceAssemblyEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetReferencedAssembliesFromStream(self, pStream: win32more.Windows.Win32.System.Com.IStream_head, dwFlags: UInt32, pExcludeAssembliesList: win32more.Windows.Win32.System.ClrHosting.ICLRAssemblyReferenceList_head, ppReferenceEnum: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRReferenceAssemblyEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProbingAssembliesFromReference(self, dwMachineType: UInt32, dwFlags: UInt32, pwzReferenceIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppProbingAssemblyEnum: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRProbingAssemblyEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsStronglyNamed(self, pwzAssemblyIdentity: win32more.Windows.Win32.Foundation.PWSTR, pbIsStronglyNamed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRAssemblyReferenceList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b2c9750-2e66-4bda-8b44-0a642c5cd733}')
    @commethod(3)
    def IsStringAssemblyReferenceInList(self, pwzAssemblyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAssemblyReferenceInList(self, pName: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9065597e-d1a1-4fb2-b6ba-7e1fce230f61}')
    @commethod(3)
    def GetCLRManager(self, riid: POINTER(Guid), ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAppDomainManagerType(self, pwzAppDomainManagerAssembly: win32more.Windows.Win32.Foundation.PWSTR, pwzAppDomainManagerType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRDebugManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00dcaec6-2ac0-43a9-acf9-1e36c139b10d}')
    @commethod(3)
    def BeginConnection(self, dwConnectionId: UInt32, szConnectionName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetConnectionTasks(self, id: UInt32, dwCount: UInt32, ppCLRTask: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndConnection(self, dwConnectionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDacl(self, pacl: POINTER(win32more.Windows.Win32.Security.ACL_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDacl(self, pacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsDebuggerAttached(self, pbAttached: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSymbolReadingPolicy(self, policy: win32more.Windows.Win32.System.ClrHosting.ESymbolReadingPolicy) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRDebugging(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d28f3c5a-9634-4206-a509-477552eefb10}')
    @commethod(3)
    def OpenVirtualProcess(self, moduleBaseAddress: UInt64, pDataTarget: win32more.Windows.Win32.System.Com.IUnknown_head, pLibraryProvider: win32more.Windows.Win32.System.ClrHosting.ICLRDebuggingLibraryProvider_head, pMaxDebuggerSupportedVersion: POINTER(win32more.Windows.Win32.System.ClrHosting.CLR_DEBUGGING_VERSION_head), riidProcess: POINTER(Guid), ppProcess: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head), pVersion: POINTER(win32more.Windows.Win32.System.ClrHosting.CLR_DEBUGGING_VERSION_head), pdwFlags: POINTER(win32more.Windows.Win32.System.ClrHosting.CLR_DEBUGGING_PROCESS_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanUnloadNow(self, hModule: win32more.Windows.Win32.Foundation.HMODULE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRDebuggingLibraryProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3151c08d-4d09-4f9b-8838-2880bf18fe51}')
    @commethod(3)
    def ProvideLibrary(self, pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, dwTimestamp: UInt32, dwSizeOfImage: UInt32, phModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRDomainManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{270d00a2-8e15-4d0b-adeb-37bc3e47df77}')
    @commethod(3)
    def SetAppDomainManagerType(self, wszAppDomainManagerAssembly: win32more.Windows.Win32.Foundation.PWSTR, wszAppDomainManagerType: win32more.Windows.Win32.Foundation.PWSTR, dwInitializeDomainFlags: win32more.Windows.Win32.System.ClrHosting.EInitializeNewDomainFlags) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertiesForDefaultAppDomain(self, nProperties: UInt32, pwszPropertyNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pwszPropertyValues: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRErrorReportingManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{980d2f1a-bf79-4c08-812a-bb9778928f78}')
    @commethod(3)
    def GetBucketParametersForCurrentException(self, pParams: POINTER(win32more.Windows.Win32.System.ClrHosting.BucketParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginCustomDump(self, dwFlavor: win32more.Windows.Win32.System.ClrHosting.ECustomDumpFlavor, dwNumItems: UInt32, items: POINTER(win32more.Windows.Win32.System.ClrHosting.CustomDumpItem_head), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndCustomDump(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRGCManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54d9007e-a8e2-4885-b7bf-f998deee4f2a}')
    @commethod(3)
    def Collect(self, Generation: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStats(self, pStats: POINTER(win32more.Windows.Win32.System.ClrHosting.COR_GC_STATS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetGCStartupLimits(self, SegmentSize: UInt32, MaxGen0Size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRGCManager2(ComPtr):
    extends: win32more.Windows.Win32.System.ClrHosting.ICLRGCManager
    _iid_ = Guid('{0603b793-a97a-4712-9cb4-0cd1c74c0f7c}')
    @commethod(6)
    def SetGCStartupLimitsEx(self, SegmentSize: UIntPtr, MaxGen0Size: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRHostBindingPolicyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b3545e7-1856-48c9-a8ba-24b21a753c09}')
    @commethod(3)
    def ModifyApplicationPolicy(self, pwzSourceAssemblyIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzTargetAssemblyIdentity: win32more.Windows.Win32.Foundation.PWSTR, pbApplicationPolicy: POINTER(Byte), cbAppPolicySize: UInt32, dwPolicyModifyFlags: UInt32, pbNewApplicationPolicy: POINTER(Byte), pcbNewAppPolicySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EvaluatePolicy(self, pwzReferenceIdentity: win32more.Windows.Win32.Foundation.PWSTR, pbApplicationPolicy: POINTER(Byte), cbAppPolicySize: UInt32, pwzPostPolicyReferenceIdentity: win32more.Windows.Win32.Foundation.PWSTR, pcchPostPolicyReferenceIdentity: POINTER(UInt32), pdwPoliciesApplied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRHostProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89f25f5c-ceef-43e1-9cfa-a68ce863aaac}')
    @commethod(3)
    def SetProtectedCategories(self, categories: win32more.Windows.Win32.System.ClrHosting.EApiCategories) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEagerSerializeGrantSets(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRIoCompletionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2d74ce86-b8d6-4c84-b3a7-9768933b3c12}')
    @commethod(3)
    def OnComplete(self, dwErrorCode: UInt32, NumberOfBytesTransferred: UInt32, pvOverlapped: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRMemoryNotificationCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{47eb8e57-0846-4546-af76-6f42fcfc2649}')
    @commethod(3)
    def OnMemoryNotification(self, eMemoryAvailable: win32more.Windows.Win32.System.ClrHosting.EMemoryAvailable) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRMetaHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d332db9e-b9b3-4125-8207-a14884f53216}')
    @commethod(3)
    def GetRuntime(self, pwzVersion: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppRuntime: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionFromFile(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateInstalledRuntimes(self, ppEnumerator: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateLoadedRuntimes(self, hndProcess: win32more.Windows.Win32.Foundation.HANDLE, ppEnumerator: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestRuntimeLoadedNotification(self, pCallbackFunction: win32more.Windows.Win32.System.ClrHosting.RuntimeLoadedCallbackFnPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryLegacyV2RuntimeBinding(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ExitProcess(self, iExitCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRMetaHostPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2190695-77b2-492e-8e14-c4b3a7fdd593}')
    @commethod(3)
    def GetRequestedRuntime(self, dwPolicyFlags: win32more.Windows.Win32.System.ClrHosting.METAHOST_POLICY_FLAGS, pwzBinary: win32more.Windows.Win32.Foundation.PWSTR, pCfgStream: win32more.Windows.Win32.System.Com.IStream_head, pwzVersion: win32more.Windows.Win32.Foundation.PWSTR, pcchVersion: POINTER(UInt32), pwzImageVersion: win32more.Windows.Win32.Foundation.PWSTR, pcchImageVersion: POINTER(UInt32), pdwConfigFlags: POINTER(UInt32), riid: POINTER(Guid), ppRuntime: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLROnEventManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d0e0132-e64f-493d-9260-025c0e32c175}')
    @commethod(3)
    def RegisterActionOnEvent(self, event: win32more.Windows.Win32.System.ClrHosting.EClrEvent, pAction: win32more.Windows.Win32.System.ClrHosting.IActionOnCLREvent_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterActionOnEvent(self, event: win32more.Windows.Win32.System.ClrHosting.EClrEvent, pAction: win32more.Windows.Win32.System.ClrHosting.IActionOnCLREvent_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRPolicyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d290010-d781-45da-a6f8-aa5d711a730e}')
    @commethod(3)
    def SetDefaultAction(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimeout(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetActionOnTimeout(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTimeoutAndAction(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, dwMilliseconds: UInt32, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetActionOnFailure(self, failure: win32more.Windows.Win32.System.ClrHosting.EClrFailure, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetUnhandledExceptionPolicy(self, policy: win32more.Windows.Win32.System.ClrHosting.EClrUnhandledException) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRProbingAssemblyEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0c5fb1f-416b-4f97-81f4-7ac7dc24dd5d}')
    @commethod(3)
    def Get(self, dwIndex: UInt32, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRProfiling(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b349abe3-b56f-4689-bfcd-76bf39d888ea}')
    @commethod(3)
    def AttachProfiler(self, dwProfileeProcessID: UInt32, dwMillisecondsMax: UInt32, pClsidProfiler: POINTER(Guid), wszProfilerPath: win32more.Windows.Win32.Foundation.PWSTR, pvClientData: VoidPtr, cbClientData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRReferenceAssemblyEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d509cb5d-cf32-4876-ae61-67770cf91973}')
    @commethod(3)
    def Get(self, dwIndex: UInt32, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRRuntimeHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90f1a06c-7712-4762-86b5-7a5eba6bdb02}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHostControl(self, pHostControl: win32more.Windows.Win32.System.ClrHosting.IHostControl_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCLRControl(self, pCLRControl: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRControl_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnloadAppDomain(self, dwAppDomainId: UInt32, fWaitUntilDone: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ExecuteInAppDomain(self, dwAppDomainId: UInt32, pCallback: win32more.Windows.Win32.System.ClrHosting.FExecuteInAppDomainCallback, cookie: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentAppDomainId(self, pdwAppDomainId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ExecuteApplication(self, pwzAppFullName: win32more.Windows.Win32.Foundation.PWSTR, dwManifestPaths: UInt32, ppwzManifestPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwActivationData: UInt32, ppwzActivationData: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pReturnValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ExecuteInDefaultAppDomain(self, pwzAssemblyPath: win32more.Windows.Win32.Foundation.PWSTR, pwzTypeName: win32more.Windows.Win32.Foundation.PWSTR, pwzMethodName: win32more.Windows.Win32.Foundation.PWSTR, pwzArgument: win32more.Windows.Win32.Foundation.PWSTR, pReturnValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRRuntimeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bd39d1d2-ba2f-486a-89b0-b4b0cb466891}')
    @commethod(3)
    def GetVersionString(self, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeDirectory(self, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsLoaded(self, hndProcess: win32more.Windows.Win32.Foundation.HANDLE, pbLoaded: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LoadErrorString(self, iResourceID: UInt32, pwzBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBuffer: POINTER(UInt32), iLocaleID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadLibraryA(self, pwzDllName: win32more.Windows.Win32.Foundation.PWSTR, phndModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProcAddress(self, pszProcName: win32more.Windows.Win32.Foundation.PSTR, ppProc: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInterface(self, rclsid: POINTER(Guid), riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsLoadable(self, pbLoadable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultStartupFlags(self, dwStartupFlags: UInt32, pwzHostConfigFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDefaultStartupFlags(self, pdwStartupFlags: POINTER(UInt32), pwzHostConfigFile: win32more.Windows.Win32.Foundation.PWSTR, pcchHostConfigFile: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def BindAsLegacyV2Runtime(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsStarted(self, pbStarted: POINTER(win32more.Windows.Win32.Foundation.BOOL), pdwStartupFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRStrongName(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9fd93ccf-3280-4391-b3a9-96e1cde77c8d}')
    @commethod(3)
    def GetHashFromAssemblyFile(self, pszFilePath: win32more.Windows.Win32.Foundation.PSTR, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHashFromAssemblyFileW(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHashFromBlob(self, pbBlob: POINTER(Byte), cchBlob: UInt32, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHashFromFile(self, pszFilePath: win32more.Windows.Win32.Foundation.PSTR, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHashFromFileW(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHashFromHandle(self, hFile: win32more.Windows.Win32.Foundation.HANDLE, piHashAlg: POINTER(UInt32), pbHash: POINTER(Byte), cchHash: UInt32, pchHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StrongNameCompareAssemblies(self, pwzAssembly1: win32more.Windows.Win32.Foundation.PWSTR, pwzAssembly2: win32more.Windows.Win32.Foundation.PWSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def StrongNameFreeBuffer(self, pbMemory: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def StrongNameGetBlob(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, pbBlob: POINTER(Byte), pcbBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StrongNameGetBlobFromImage(self, pbBase: POINTER(Byte), dwLength: UInt32, pbBlob: POINTER(Byte), pcbBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StrongNameGetPublicKey(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32, ppbPublicKeyBlob: POINTER(POINTER(Byte)), pcbPublicKeyBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StrongNameHashSize(self, ulHashAlg: UInt32, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def StrongNameKeyDelete(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def StrongNameKeyGen(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppbKeyBlob: POINTER(POINTER(Byte)), pcbKeyBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def StrongNameKeyGenEx(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwKeySize: UInt32, ppbKeyBlob: POINTER(POINTER(Byte)), pcbKeyBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def StrongNameKeyInstall(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def StrongNameSignatureGeneration(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32, ppbSignatureBlob: POINTER(POINTER(Byte)), pcbSignatureBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def StrongNameSignatureGenerationEx(self, wszFilePath: win32more.Windows.Win32.Foundation.PWSTR, wszKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32, ppbSignatureBlob: POINTER(POINTER(Byte)), pcbSignatureBlob: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StrongNameSignatureSize(self, pbPublicKeyBlob: POINTER(Byte), cbPublicKeyBlob: UInt32, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def StrongNameSignatureVerification(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, dwInFlags: UInt32, pdwOutFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def StrongNameSignatureVerificationEx(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, fForceVerification: win32more.Windows.Win32.Foundation.BOOLEAN, pfWasVerified: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def StrongNameSignatureVerificationFromImage(self, pbBase: POINTER(Byte), dwLength: UInt32, dwInFlags: UInt32, pdwOutFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def StrongNameTokenFromAssembly(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, ppbStrongNameToken: POINTER(POINTER(Byte)), pcbStrongNameToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def StrongNameTokenFromAssemblyEx(self, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR, ppbStrongNameToken: POINTER(POINTER(Byte)), pcbStrongNameToken: POINTER(UInt32), ppbPublicKeyBlob: POINTER(POINTER(Byte)), pcbPublicKeyBlob: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def StrongNameTokenFromPublicKey(self, pbPublicKeyBlob: POINTER(Byte), cbPublicKeyBlob: UInt32, ppbStrongNameToken: POINTER(POINTER(Byte)), pcbStrongNameToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRStrongName2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c22ed5c5-4b59-4975-90eb-85ea55c0069b}')
    @commethod(3)
    def StrongNameGetPublicKeyEx(self, pwzKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32, ppbPublicKeyBlob: POINTER(POINTER(Byte)), pcbPublicKeyBlob: POINTER(UInt32), uHashAlgId: UInt32, uReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StrongNameSignatureVerificationEx2(self, wszFilePath: win32more.Windows.Win32.Foundation.PWSTR, fForceVerification: win32more.Windows.Win32.Foundation.BOOLEAN, pbEcmaPublicKey: POINTER(Byte), cbEcmaPublicKey: UInt32, pfWasVerified: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRStrongName3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22c7089b-bbd3-414a-b698-210f263f1fed}')
    @commethod(3)
    def StrongNameDigestGenerate(self, wszFilePath: win32more.Windows.Win32.Foundation.PWSTR, ppbDigestBlob: POINTER(POINTER(Byte)), pcbDigestBlob: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StrongNameDigestSign(self, wszKeyContainer: win32more.Windows.Win32.Foundation.PWSTR, pbKeyBlob: POINTER(Byte), cbKeyBlob: UInt32, pbDigestBlob: POINTER(Byte), cbDigestBlob: UInt32, hashAlgId: UInt32, ppbSignatureBlob: POINTER(POINTER(Byte)), pcbSignatureBlob: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StrongNameDigestEmbed(self, wszFilePath: win32more.Windows.Win32.Foundation.PWSTR, pbSignatureBlob: POINTER(Byte), cbSignatureBlob: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55ff199d-ad21-48f9-a16c-f24ebbb8727d}')
    @commethod(3)
    def GetMonitorOwner(self, Cookie: UIntPtr, ppOwnerHostTask: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRWLockOwnerIterator(self, Cookie: UIntPtr, pIterator: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRWLockOwnerNext(self, Iterator: UIntPtr, ppOwnerHostTask: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteRWLockOwnerIterator(self, Iterator: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRTask(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28e66a4a-9906-4225-b231-9187c3eb8611}')
    @commethod(3)
    def SwitchIn(self, threadHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SwitchOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMemStats(self, memUsage: POINTER(win32more.Windows.Win32.System.ClrHosting.COR_GC_THREAD_STATS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self, fFull: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ExitTask(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RudeAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NeedsPriorityScheduling(self, pbNeedsPriorityScheduling: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def YieldTask(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def LocksHeld(self, pLockCount: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetTaskIdentifier(self, asked: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRTask2(ComPtr):
    extends: win32more.Windows.Win32.System.ClrHosting.ICLRTask
    _iid_ = Guid('{28e66a4a-9906-4225-b231-9187c3eb8612}')
    @commethod(14)
    def BeginPreventAsyncAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EndPreventAsyncAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICLRTaskManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4862efbe-3ae5-44f8-8feb-346190ee8a34}')
    @commethod(3)
    def CreateTask(self, pTask: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentTask(self, pTask: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUILocale(self, lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLocale(self, lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentTaskType(self, pTaskType: POINTER(win32more.Windows.Win32.System.ClrHosting.ETaskType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatalogServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04c6be1e-1db1-4058-ab7a-700cccfbf254}')
    @commethod(3)
    def Autodone(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotAutodone(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c2b07a5-1e98-11d3-872f-00c04f79ed0d}')
    @commethod(3)
    def SetGCThreadControl(self, pGCThreadControl: win32more.Windows.Win32.System.ClrHosting.IGCThreadControl_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetGCHostControl(self, pGCHostControl: win32more.Windows.Win32.System.ClrHosting.IGCHostControl_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDebuggerThreadControl(self, pDebuggerThreadControl: win32more.Windows.Win32.System.ClrHosting.IDebuggerThreadControl_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddDebuggerSpecialThread(self, dwSpecialThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorRuntimeHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb2f6722-ab3a-11d2-9c40-00c04fa30a3e}')
    @commethod(3)
    def CreateLogicalThreadState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteLogicalThreadState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SwitchInLogicalThreadState(self, pFiberCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SwitchOutLogicalThreadState(self, pFiberCookie: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LocksHeldByLogicalThread(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MapFile(self, hFile: win32more.Windows.Win32.Foundation.HANDLE, hMapAddress: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetConfiguration(self, pConfiguration: POINTER(win32more.Windows.Win32.System.ClrHosting.ICorConfiguration_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateDomain(self, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pIdentityArray: win32more.Windows.Win32.System.Com.IUnknown_head, pAppDomain: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultDomain(self, pAppDomain: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumDomains(self, hEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def NextDomain(self, hEnum: VoidPtr, pAppDomain: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CloseEnum(self, hEnum: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateDomainEx(self, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pSetup: win32more.Windows.Win32.System.Com.IUnknown_head, pEvidence: win32more.Windows.Win32.System.Com.IUnknown_head, pAppDomain: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateDomainSetup(self, pAppDomainSetup: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateEvidence(self, pEvidence: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def UnloadDomain(self, pAppDomain: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CurrentDomain(self, pAppDomain: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorThreadpool(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{84680d3a-b2c1-46e8-acc2-dbc0a359159a}')
    @commethod(3)
    def CorRegisterWaitForSingleObject(self, phNewWaitObject: POINTER(win32more.Windows.Win32.Foundation.HANDLE), hWaitObject: win32more.Windows.Win32.Foundation.HANDLE, Callback: win32more.Windows.Win32.System.Threading.WAITORTIMERCALLBACK, Context: VoidPtr, timeout: UInt32, executeOnlyOnce: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CorUnregisterWait(self, hWaitObject: win32more.Windows.Win32.Foundation.HANDLE, CompletionEvent: win32more.Windows.Win32.Foundation.HANDLE, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CorQueueUserWorkItem(self, Function: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, Context: VoidPtr, executeOnlyOnce: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CorCreateTimer(self, phNewTimer: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Callback: win32more.Windows.Win32.System.Threading.WAITORTIMERCALLBACK, Parameter: VoidPtr, DueTime: UInt32, Period: UInt32, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CorChangeTimer(self, Timer: win32more.Windows.Win32.Foundation.HANDLE, DueTime: UInt32, Period: UInt32, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CorDeleteTimer(self, Timer: win32more.Windows.Win32.Foundation.HANDLE, CompletionEvent: win32more.Windows.Win32.Foundation.HANDLE, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CorBindIoCompletionCallback(self, fileHandle: win32more.Windows.Win32.Foundation.HANDLE, callback: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CorCallOrQueueUserWorkItem(self, Function: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, Context: VoidPtr, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CorSetMaxThreads(self, MaxWorkerThreads: UInt32, MaxIOCompletionThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CorGetMaxThreads(self, MaxWorkerThreads: POINTER(UInt32), MaxIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CorGetAvailableThreads(self, AvailableWorkerThreads: POINTER(UInt32), AvailableIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebuggerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf24142d-a47d-4d24-a66d-8c2141944e44}')
    @commethod(3)
    def IsDebuggerAttached(self, pbAttached: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebuggerThreadControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23d86786-0bb5-4774-8fb5-e3522add6246}')
    @commethod(3)
    def ThreadIsBlockingForDebugger(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseAllRuntimeThreads(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StartBlockingForDebugger(self, dwUnused: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGCHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fac34f6e-0dcd-47b5-8021-531bc5ecca63}')
    @commethod(3)
    def SetGCStartupLimits(self, SegmentSize: UInt32, MaxGen0Size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Collect(self, Generation: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStats(self, pStats: POINTER(win32more.Windows.Win32.System.ClrHosting.COR_GC_STATS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetThreadStats(self, pFiberCookie: POINTER(UInt32), pStats: POINTER(win32more.Windows.Win32.System.ClrHosting.COR_GC_THREAD_STATS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVirtualMemLimit(self, sztMaxVirtualMemMB: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGCHost2(ComPtr):
    extends: win32more.Windows.Win32.System.ClrHosting.IGCHost
    _iid_ = Guid('{a1d70cec-2dbe-4e2f-9291-fdf81438a1df}')
    @commethod(8)
    def SetGCStartupLimitsEx(self, SegmentSize: UIntPtr, MaxGen0Size: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGCHostControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5513d564-8374-4cb9-aed9-0083f4160a1d}')
    @commethod(3)
    def RequestVirtualMemLimit(self, sztMaxVirtualMemMB: UIntPtr, psztNewMaxVirtualMemMB: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGCThreadControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f31d1788-c397-4725-87a5-6af3472c2791}')
    @commethod(3)
    def ThreadIsBlockingForSuspension(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SuspensionStarting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SuspensionEnding(self, Generation: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostAssemblyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{613dabd7-62b2-493e-9e65-c1e32a1e0c5e}')
    @commethod(3)
    def GetNonHostStoreAssemblies(self, ppReferenceList: POINTER(win32more.Windows.Win32.System.ClrHosting.ICLRAssemblyReferenceList_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAssemblyStore(self, ppAssemblyStore: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostAssemblyStore_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostAssemblyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7b102a88-3f7f-496d-8fa2-c35374e01af3}')
    @commethod(3)
    def ProvideAssembly(self, pBindInfo: POINTER(win32more.Windows.Win32.System.ClrHosting.AssemblyBindInfo_head), pAssemblyId: POINTER(UInt64), pContext: POINTER(UInt64), ppStmAssemblyImage: POINTER(win32more.Windows.Win32.System.Com.IStream_head), ppStmPDB: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProvideModule(self, pBindInfo: POINTER(win32more.Windows.Win32.System.ClrHosting.ModuleBindInfo_head), pdwModuleId: POINTER(UInt32), ppStmModuleImage: POINTER(win32more.Windows.Win32.System.Com.IStream_head), ppStmPDB: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostAutoEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50b0cfce-4063-4278-9673-e5cb4ed0bdb8}')
    @commethod(3)
    def Wait(self, dwMilliseconds: UInt32, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Set(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02ca073c-7079-4860-880a-c2f7a449c991}')
    @commethod(3)
    def GetHostManager(self, riid: POINTER(Guid), ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAppDomainManager(self, dwAppDomainID: UInt32, pUnkAppDomainManager: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostCrst(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6df710a6-26a4-4a65-8cd5-7237b8bda8dc}')
    @commethod(3)
    def Enter(self, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Leave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TryEnter(self, option: UInt32, pbSucceeded: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSpinCount(self, dwSpinCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostGCManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d4ec34e-f248-457b-b603-255faaba0d21}')
    @commethod(3)
    def ThreadIsBlockingForSuspension(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SuspensionStarting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SuspensionEnding(self, Generation: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostIoCompletionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8bde9d80-ec06-41d6-83e6-22580effcc20}')
    @commethod(3)
    def CreateIoCompletionPort(self, phPort: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CloseIoCompletionPort(self, hPort: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreads(self, dwMaxIOCompletionThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxThreads(self, pdwMaxIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAvailableThreads(self, pdwAvailableIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHostOverlappedSize(self, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetCLRIoCompletionManager(self, pManager: win32more.Windows.Win32.System.ClrHosting.ICLRIoCompletionManager_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InitializeHostOverlapped(self, pvOverlapped: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Bind(self, hPort: win32more.Windows.Win32.Foundation.HANDLE, hHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetMinThreads(self, dwMinIOCompletionThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMinThreads(self, pdwMinIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostMalloc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1831991c-cc53-4a31-b218-04e910446479}')
    @commethod(3)
    def Alloc(self, cbSize: UIntPtr, eCriticalLevel: win32more.Windows.Win32.System.ClrHosting.EMemoryCriticalLevel, ppMem: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DebugAlloc(self, cbSize: UIntPtr, eCriticalLevel: win32more.Windows.Win32.System.ClrHosting.EMemoryCriticalLevel, pszFileName: win32more.Windows.Win32.Foundation.PSTR, iLineNo: Int32, ppMem: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Free(self, pMem: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostManualEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bf4ec38-affe-4fb9-85a6-525268f15b54}')
    @commethod(3)
    def Wait(self, dwMilliseconds: UInt32, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Set(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostMemoryManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bc698d1-f9e3-4460-9cde-d04248e9fa25}')
    @commethod(3)
    def CreateMalloc(self, dwMallocType: UInt32, ppMalloc: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostMalloc_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def VirtualAlloc(self, pAddress: VoidPtr, dwSize: UIntPtr, flAllocationType: UInt32, flProtect: UInt32, eCriticalLevel: win32more.Windows.Win32.System.ClrHosting.EMemoryCriticalLevel, ppMem: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def VirtualFree(self, lpAddress: VoidPtr, dwSize: UIntPtr, dwFreeType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def VirtualQuery(self, lpAddress: VoidPtr, lpBuffer: VoidPtr, dwLength: UIntPtr, pResult: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def VirtualProtect(self, lpAddress: VoidPtr, dwSize: UIntPtr, flNewProtect: UInt32, pflOldProtect: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMemoryLoad(self, pMemoryLoad: POINTER(UInt32), pAvailableBytes: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterMemoryNotificationCallback(self, pCallback: win32more.Windows.Win32.System.ClrHosting.ICLRMemoryNotificationCallback_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NeedsVirtualAddressSpace(self, startAddress: VoidPtr, size: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AcquiredVirtualAddressSpace(self, startAddress: VoidPtr, size: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReleasedVirtualAddressSpace(self, startAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostPolicyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ae49844-b1e3-4683-ba7c-1e8212ea3b79}')
    @commethod(3)
    def OnDefaultAction(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTimeout(self, operation: win32more.Windows.Win32.System.ClrHosting.EClrOperation, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnFailure(self, failure: win32more.Windows.Win32.System.ClrHosting.EClrFailure, action: win32more.Windows.Win32.System.ClrHosting.EPolicyAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostSecurityContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7e573ce4-0343-4423-98d7-6318348a1d3c}')
    @commethod(3)
    def Capture(self, ppClonedContext: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostSecurityContext_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostSecurityManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75ad2468-a349-4d02-a764-76a68aee0c4f}')
    @commethod(3)
    def ImpersonateLoggedOnUser(self, hToken: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevertToSelf(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenThreadToken(self, dwDesiredAccess: UInt32, bOpenAsSelf: win32more.Windows.Win32.Foundation.BOOL, phThreadToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetThreadToken(self, hToken: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSecurityContext(self, eContextType: win32more.Windows.Win32.System.ClrHosting.EContextType, ppSecurityContext: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostSecurityContext_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSecurityContext(self, eContextType: win32more.Windows.Win32.System.ClrHosting.EContextType, pSecurityContext: win32more.Windows.Win32.System.ClrHosting.IHostSecurityContext_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostSemaphore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{855efd47-cc09-463a-a97d-16acab882661}')
    @commethod(3)
    def Wait(self, dwMilliseconds: UInt32, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseSemaphore(self, lReleaseCount: Int32, lpPreviousCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{234330c7-5f10-4f20-9615-5122dab7a0ac}')
    @commethod(3)
    def SetCLRSyncManager(self, pManager: win32more.Windows.Win32.System.ClrHosting.ICLRSyncManager_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateCrst(self, ppCrst: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostCrst_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateCrstWithSpinCount(self, dwSpinCount: UInt32, ppCrst: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostCrst_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateAutoEvent(self, ppEvent: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostAutoEvent_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateManualEvent(self, bInitialState: win32more.Windows.Win32.Foundation.BOOL, ppEvent: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostManualEvent_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateMonitorEvent(self, Cookie: UIntPtr, ppEvent: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostAutoEvent_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateRWLockWriterEvent(self, Cookie: UIntPtr, ppEvent: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostAutoEvent_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateRWLockReaderEvent(self, bInitialState: win32more.Windows.Win32.Foundation.BOOL, Cookie: UIntPtr, ppEvent: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostManualEvent_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSemaphoreA(self, dwInitial: UInt32, dwMax: UInt32, ppSemaphore: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostSemaphore_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostTask(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2275828-c4b1-4b55-82c9-92135f74df1a}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Alert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Join(self, dwMilliseconds: UInt32, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPriority(self, newPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPriority(self, pPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCLRTask(self, pCLRTask: win32more.Windows.Win32.System.ClrHosting.ICLRTask_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostTaskManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{997ff24c-43b7-4352-8667-0dc04fafd354}')
    @commethod(3)
    def GetCurrentTask(self, pTask: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTask(self, dwStackSize: UInt32, pStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pParameter: VoidPtr, ppTask: POINTER(win32more.Windows.Win32.System.ClrHosting.IHostTask_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Sleep(self, dwMilliseconds: UInt32, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SwitchToTask(self, option: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetUILocale(self, lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetLocale(self, lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CallNeedsHostHook(self, target: UIntPtr, pbCallNeedsHostHook: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LeaveRuntime(self, target: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnterRuntime(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReverseLeaveRuntime(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ReverseEnterRuntime(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BeginDelayAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EndDelayAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def BeginThreadAffinity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EndThreadAffinity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetStackGuarantee(self, guarantee: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetStackGuarantee(self, pGuarantee: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetCLRTaskManager(self, ppManager: win32more.Windows.Win32.System.ClrHosting.ICLRTaskManager_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHostThreadpoolManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{983d50e2-cb15-466b-80fc-845dc6e8c5fd}')
    @commethod(3)
    def QueueUserWorkItem(self, Function: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, Context: VoidPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaxThreads(self, dwMaxWorkerThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxThreads(self, pdwMaxWorkerThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAvailableThreads(self, pdwAvailableWorkerThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMinThreads(self, dwMinIOCompletionThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMinThreads(self, pdwMinIOCompletionThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManagedObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3fcc19e-a970-11d2-8b5a-00a0c9b7c9c4}')
    @commethod(3)
    def GetSerializedBuffer(self, pBSTR: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectIdentity(self, pBSTRGUID: POINTER(win32more.Windows.Win32.Foundation.BSTR), AppDomainID: POINTER(Int32), pCCW: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectHandle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c460e2b4-e199-412a-8456-84dc3e4838c3}')
    @commethod(3)
    def Unwrap(self, ppv: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeName(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b81ff171-20f3-11d2-8dcc-00a0c9b00522}')
    @commethod(3)
    def GetNameCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNames(self, count: UInt32, rgbszNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTypeArgumentCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTypeArguments(self, count: UInt32, rgpArguments: POINTER(win32more.Windows.Win32.System.ClrHosting.ITypeName_head), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetModifierLength(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetModifiers(self, count: UInt32, rgModifiers: POINTER(UInt32), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAssemblyName(self, rgbszAssemblyNames: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeNameBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b81ff171-20f3-11d2-8dcc-00a0c9b00523}')
    @commethod(3)
    def OpenGenericArguments(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CloseGenericArguments(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenGenericArgument(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CloseGenericArgument(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddName(self, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddPointer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddByRef(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddSzArray(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddArray(self, rank: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddAssemblySpec(self, szAssemblySpec: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ToString(self, pszStringRepresentation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeNameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b81ff171-20f3-11d2-8dcc-00a0c9b00521}')
    @commethod(3)
    def ParseTypeName(self, szName: win32more.Windows.Win32.Foundation.PWSTR, pError: POINTER(UInt32), ppTypeName: POINTER(win32more.Windows.Win32.System.ClrHosting.ITypeName_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeNameBuilder(self, ppTypeBuilder: POINTER(win32more.Windows.Win32.System.ClrHosting.ITypeNameBuilder_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MALLOC_TYPE = Int32
MALLOC_THREADSAFE: MALLOC_TYPE = 1
MALLOC_EXECUTABLE: MALLOC_TYPE = 2
class MDAInfo(EasyCastStructure):
    lpMDACaption: win32more.Windows.Win32.Foundation.PWSTR
    lpMDAMessage: win32more.Windows.Win32.Foundation.PWSTR
    lpStackTrace: win32more.Windows.Win32.Foundation.PWSTR
METAHOST_CONFIG_FLAGS = Int32
METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_UNSET: METAHOST_CONFIG_FLAGS = 0
METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_TRUE: METAHOST_CONFIG_FLAGS = 1
METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_FALSE: METAHOST_CONFIG_FLAGS = 2
METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_MASK: METAHOST_CONFIG_FLAGS = 3
METAHOST_POLICY_FLAGS = Int32
METAHOST_POLICY_HIGHCOMPAT: METAHOST_POLICY_FLAGS = 0
METAHOST_POLICY_APPLY_UPGRADE_POLICY: METAHOST_POLICY_FLAGS = 8
METAHOST_POLICY_EMULATE_EXE_LAUNCH: METAHOST_POLICY_FLAGS = 16
METAHOST_POLICY_SHOW_ERROR_DIALOG: METAHOST_POLICY_FLAGS = 32
METAHOST_POLICY_USE_PROCESS_IMAGE_PATH: METAHOST_POLICY_FLAGS = 64
METAHOST_POLICY_ENSURE_SKU_SUPPORTED: METAHOST_POLICY_FLAGS = 128
METAHOST_POLICY_IGNORE_ERROR_MODE: METAHOST_POLICY_FLAGS = 4096
class ModuleBindInfo(EasyCastStructure):
    dwAppDomainId: UInt32
    lpAssemblyIdentity: win32more.Windows.Win32.Foundation.PWSTR
    lpModuleName: win32more.Windows.Win32.Foundation.PWSTR
@winfunctype_pointer
def PTLS_CALLBACK_FUNCTION(__MIDL____MIDL_itf_mscoree_0000_00040005: VoidPtr) -> Void: ...
RUNTIME_INFO_FLAGS = Int32
RUNTIME_INFO_UPGRADE_VERSION: RUNTIME_INFO_FLAGS = 1
RUNTIME_INFO_REQUEST_IA64: RUNTIME_INFO_FLAGS = 2
RUNTIME_INFO_REQUEST_AMD64: RUNTIME_INFO_FLAGS = 4
RUNTIME_INFO_REQUEST_X86: RUNTIME_INFO_FLAGS = 8
RUNTIME_INFO_DONT_RETURN_DIRECTORY: RUNTIME_INFO_FLAGS = 16
RUNTIME_INFO_DONT_RETURN_VERSION: RUNTIME_INFO_FLAGS = 32
RUNTIME_INFO_DONT_SHOW_ERROR_DIALOG: RUNTIME_INFO_FLAGS = 64
RUNTIME_INFO_IGNORE_ERROR_MODE: RUNTIME_INFO_FLAGS = 4096
@winfunctype_pointer
def RuntimeLoadedCallbackFnPtr(pRuntimeInfo: win32more.Windows.Win32.System.ClrHosting.ICLRRuntimeInfo_head, pfnCallbackThreadSet: win32more.Windows.Win32.System.ClrHosting.CallbackThreadSetFnPtr, pfnCallbackThreadUnset: win32more.Windows.Win32.System.ClrHosting.CallbackThreadUnsetFnPtr) -> Void: ...
STARTUP_FLAGS = Int32
STARTUP_CONCURRENT_GC: STARTUP_FLAGS = 1
STARTUP_LOADER_OPTIMIZATION_MASK: STARTUP_FLAGS = 6
STARTUP_LOADER_OPTIMIZATION_SINGLE_DOMAIN: STARTUP_FLAGS = 2
STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN: STARTUP_FLAGS = 4
STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST: STARTUP_FLAGS = 6
STARTUP_LOADER_SAFEMODE: STARTUP_FLAGS = 16
STARTUP_LOADER_SETPREFERENCE: STARTUP_FLAGS = 256
STARTUP_SERVER_GC: STARTUP_FLAGS = 4096
STARTUP_HOARD_GC_VM: STARTUP_FLAGS = 8192
STARTUP_SINGLE_VERSION_HOSTING_INTERFACE: STARTUP_FLAGS = 16384
STARTUP_LEGACY_IMPERSONATION: STARTUP_FLAGS = 65536
STARTUP_DISABLE_COMMITTHREADSTACK: STARTUP_FLAGS = 131072
STARTUP_ALWAYSFLOW_IMPERSONATION: STARTUP_FLAGS = 262144
STARTUP_TRIM_GC_COMMIT: STARTUP_FLAGS = 524288
STARTUP_ETW: STARTUP_FLAGS = 1048576
STARTUP_ARM: STARTUP_FLAGS = 4194304
class StackOverflowInfo(EasyCastStructure):
    soType: win32more.Windows.Win32.System.ClrHosting.StackOverflowType
    pExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)
StackOverflowType = Int32
SO_Managed: StackOverflowType = 0
SO_ClrEngine: StackOverflowType = 1
SO_Other: StackOverflowType = 2
TypeNameFactory = Guid('{b81ff171-20f3-11d2-8dcc-00a0c9b00525}')
WAIT_OPTION = Int32
WAIT_MSGPUMP: WAIT_OPTION = 1
WAIT_ALERTABLE: WAIT_OPTION = 2
WAIT_NOTINDEADLOCK: WAIT_OPTION = 4
make_head(_module, 'AssemblyBindInfo')
make_head(_module, 'BucketParameters')
make_head(_module, 'CLRCreateInstanceFnPtr')
make_head(_module, 'CLR_DEBUGGING_VERSION')
make_head(_module, 'COR_GC_STATS')
make_head(_module, 'COR_GC_THREAD_STATS')
make_head(_module, 'CallbackThreadSetFnPtr')
make_head(_module, 'CallbackThreadUnsetFnPtr')
make_head(_module, 'CreateInterfaceFnPtr')
make_head(_module, 'CustomDumpItem')
make_head(_module, 'FExecuteInAppDomainCallback')
make_head(_module, 'FLockClrVersionCallback')
make_head(_module, 'IActionOnCLREvent')
make_head(_module, 'IApartmentCallback')
make_head(_module, 'IAppDomainBinding')
make_head(_module, 'ICLRAppDomainResourceMonitor')
make_head(_module, 'ICLRAssemblyIdentityManager')
make_head(_module, 'ICLRAssemblyReferenceList')
make_head(_module, 'ICLRControl')
make_head(_module, 'ICLRDebugManager')
make_head(_module, 'ICLRDebugging')
make_head(_module, 'ICLRDebuggingLibraryProvider')
make_head(_module, 'ICLRDomainManager')
make_head(_module, 'ICLRErrorReportingManager')
make_head(_module, 'ICLRGCManager')
make_head(_module, 'ICLRGCManager2')
make_head(_module, 'ICLRHostBindingPolicyManager')
make_head(_module, 'ICLRHostProtectionManager')
make_head(_module, 'ICLRIoCompletionManager')
make_head(_module, 'ICLRMemoryNotificationCallback')
make_head(_module, 'ICLRMetaHost')
make_head(_module, 'ICLRMetaHostPolicy')
make_head(_module, 'ICLROnEventManager')
make_head(_module, 'ICLRPolicyManager')
make_head(_module, 'ICLRProbingAssemblyEnum')
make_head(_module, 'ICLRProfiling')
make_head(_module, 'ICLRReferenceAssemblyEnum')
make_head(_module, 'ICLRRuntimeHost')
make_head(_module, 'ICLRRuntimeInfo')
make_head(_module, 'ICLRStrongName')
make_head(_module, 'ICLRStrongName2')
make_head(_module, 'ICLRStrongName3')
make_head(_module, 'ICLRSyncManager')
make_head(_module, 'ICLRTask')
make_head(_module, 'ICLRTask2')
make_head(_module, 'ICLRTaskManager')
make_head(_module, 'ICatalogServices')
make_head(_module, 'ICorConfiguration')
make_head(_module, 'ICorRuntimeHost')
make_head(_module, 'ICorThreadpool')
make_head(_module, 'IDebuggerInfo')
make_head(_module, 'IDebuggerThreadControl')
make_head(_module, 'IGCHost')
make_head(_module, 'IGCHost2')
make_head(_module, 'IGCHostControl')
make_head(_module, 'IGCThreadControl')
make_head(_module, 'IHostAssemblyManager')
make_head(_module, 'IHostAssemblyStore')
make_head(_module, 'IHostAutoEvent')
make_head(_module, 'IHostControl')
make_head(_module, 'IHostCrst')
make_head(_module, 'IHostGCManager')
make_head(_module, 'IHostIoCompletionManager')
make_head(_module, 'IHostMalloc')
make_head(_module, 'IHostManualEvent')
make_head(_module, 'IHostMemoryManager')
make_head(_module, 'IHostPolicyManager')
make_head(_module, 'IHostSecurityContext')
make_head(_module, 'IHostSecurityManager')
make_head(_module, 'IHostSemaphore')
make_head(_module, 'IHostSyncManager')
make_head(_module, 'IHostTask')
make_head(_module, 'IHostTaskManager')
make_head(_module, 'IHostThreadpoolManager')
make_head(_module, 'IManagedObject')
make_head(_module, 'IObjectHandle')
make_head(_module, 'ITypeName')
make_head(_module, 'ITypeNameBuilder')
make_head(_module, 'ITypeNameFactory')
make_head(_module, 'MDAInfo')
make_head(_module, 'ModuleBindInfo')
make_head(_module, 'PTLS_CALLBACK_FUNCTION')
make_head(_module, 'RuntimeLoadedCallbackFnPtr')
make_head(_module, 'StackOverflowInfo')
