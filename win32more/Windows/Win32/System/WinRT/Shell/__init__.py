from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Shell
import win32more.Windows.Win32.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CreateProcessMethod = Int32
CreateProcessMethod_CpCreateProcess: CreateProcessMethod = 0
CreateProcessMethod_CpCreateProcessAsUser: CreateProcessMethod = 1
CreateProcessMethod_CpAicLaunchAdminProcess: CreateProcessMethod = 2
class IDDEInitializer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30dc931f-33fc-4ffd-a168-942258cf3ca4}')
    @commethod(3)
    def Initialize(self, fileExtensionOrProtocol: win32more.Windows.Win32.Foundation.PWSTR, method: win32more.Windows.Win32.System.WinRT.Shell.CreateProcessMethod, currentDirectory: win32more.Windows.Win32.Foundation.PWSTR, execTarget: win32more.Windows.Win32.UI.Shell.IShellItem_head, site: win32more.Windows.Win32.System.Com.IUnknown_head, application: win32more.Windows.Win32.Foundation.PWSTR, targetFile: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, verb: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDDEInitializer')
