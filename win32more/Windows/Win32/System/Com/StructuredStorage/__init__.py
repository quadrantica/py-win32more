from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
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
PROPSETFLAG_DEFAULT: UInt32 = 0
PROPSETFLAG_NONSIMPLE: UInt32 = 1
PROPSETFLAG_ANSI: UInt32 = 2
PROPSETFLAG_UNBUFFERED: UInt32 = 4
PROPSETFLAG_CASE_SENSITIVE: UInt32 = 8
PROPSET_BEHAVIOR_CASE_SENSITIVE: UInt32 = 1
PID_DICTIONARY: UInt32 = 0
PID_CODEPAGE: UInt32 = 1
PID_FIRST_USABLE: UInt32 = 2
PID_FIRST_NAME_DEFAULT: UInt32 = 4095
PID_LOCALE: UInt32 = 2147483648
PID_MODIFY_TIME: UInt32 = 2147483649
PID_SECURITY: UInt32 = 2147483650
PID_BEHAVIOR: UInt32 = 2147483651
PID_ILLEGAL: UInt32 = 4294967295
PID_MIN_READONLY: UInt32 = 2147483648
PID_MAX_READONLY: UInt32 = 3221225471
PRSPEC_INVALID: UInt32 = 4294967295
PROPSETHDR_OSVERSION_UNKNOWN: UInt32 = 4294967295
PIDDI_THUMBNAIL: Int32 = 2
PIDSI_TITLE: Int32 = 2
PIDSI_SUBJECT: Int32 = 3
PIDSI_AUTHOR: Int32 = 4
PIDSI_KEYWORDS: Int32 = 5
PIDSI_COMMENTS: Int32 = 6
PIDSI_TEMPLATE: Int32 = 7
PIDSI_LASTAUTHOR: Int32 = 8
PIDSI_REVNUMBER: Int32 = 9
PIDSI_EDITTIME: Int32 = 10
PIDSI_LASTPRINTED: Int32 = 11
PIDSI_CREATE_DTM: Int32 = 12
PIDSI_LASTSAVE_DTM: Int32 = 13
PIDSI_PAGECOUNT: Int32 = 14
PIDSI_WORDCOUNT: Int32 = 15
PIDSI_CHARCOUNT: Int32 = 16
PIDSI_THUMBNAIL: Int32 = 17
PIDSI_APPNAME: Int32 = 18
PIDSI_DOC_SECURITY: Int32 = 19
PIDDSI_CATEGORY: UInt32 = 2
PIDDSI_PRESFORMAT: UInt32 = 3
PIDDSI_BYTECOUNT: UInt32 = 4
PIDDSI_LINECOUNT: UInt32 = 5
PIDDSI_PARCOUNT: UInt32 = 6
PIDDSI_SLIDECOUNT: UInt32 = 7
PIDDSI_NOTECOUNT: UInt32 = 8
PIDDSI_HIDDENCOUNT: UInt32 = 9
PIDDSI_MMCLIPCOUNT: UInt32 = 10
PIDDSI_SCALE: UInt32 = 11
PIDDSI_HEADINGPAIR: UInt32 = 12
PIDDSI_DOCPARTS: UInt32 = 13
PIDDSI_MANAGER: UInt32 = 14
PIDDSI_COMPANY: UInt32 = 15
PIDDSI_LINKSDIRTY: UInt32 = 16
PIDMSI_EDITOR: Int32 = 2
PIDMSI_SUPPLIER: Int32 = 3
PIDMSI_SOURCE: Int32 = 4
PIDMSI_SEQUENCE_NO: Int32 = 5
PIDMSI_PROJECT: Int32 = 6
PIDMSI_STATUS: Int32 = 7
PIDMSI_OWNER: Int32 = 8
PIDMSI_RATING: Int32 = 9
PIDMSI_PRODUCTION: Int32 = 10
PIDMSI_COPYRIGHT: Int32 = 11
CWCSTORAGENAME: UInt32 = 32
STGOPTIONS_VERSION: UInt32 = 1
CCH_MAX_PROPSTG_NAME: UInt32 = 31
@winfunctype('OLE32.dll')
def CoGetInstanceFromFile(pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, grfMode: UInt32, pwszName: win32more.Windows.Win32.Foundation.PWSTR, dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInstanceFromIStorage(pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgOpenAsyncDocfileOnIFillLockBytes(pflb: win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head, grfMode: UInt32, asyncFlags: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnILockBytes(pilb: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, ppflb: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnFile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, ppflb: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dflayout.dll')
def StgOpenLayoutDocfile(pwcsDfName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateStreamOnHGlobal(hGlobal: win32more.Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: win32more.Windows.Win32.Foundation.BOOL, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromStream(pstm: win32more.Windows.Win32.System.Com.IStream_head, phglobal: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInterfaceAndReleaseStream(pStm: win32more.Windows.Win32.System.Com.IStream_head, iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantCopy(pvarDest: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarSrc: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantClear(pvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FreePropVariantArray(cVariants: UInt32, rgvars: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfileOnILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorage(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageOnILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageFile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgSetTimes(lpszName: win32more.Windows.Win32.Foundation.PWSTR, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateStorageEx(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, stgfmt: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageEx(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, stgfmt: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropStg(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenPropStg(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, fmtid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropSetStg(pStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, dwReserved: UInt32, ppPropSetStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FmtIdToPropStgName(pfmtid: POINTER(Guid), oszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropStgNameToFmtId(oszName: win32more.Windows.Win32.Foundation.PWSTR, pfmtid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStm(pStm: win32more.Windows.Win32.System.Com.IStream_head, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStm(pStm: win32more.Windows.Win32.System.Com.IStream_head, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, phglobal: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateILockBytesOnHGlobal(hGlobal: win32more.Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: win32more.Windows.Win32.Foundation.BOOL, pplkbyt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetConvertStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgConvertVariantToProperty(pvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), CodePage: UInt16, pprop: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), pcb: POINTER(UInt32), pid: UInt32, fReserved: win32more.Windows.Win32.Foundation.BOOLEAN, pcIndirect: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head): ...
@winfunctype('ole32.dll')
def StgPropertyLengthAsVariant(pProp: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbProp: UInt32, CodePage: UInt16, bReserved: Byte) -> UInt32: ...
@winfunctype('OLE32.dll')
def WriteFmtUserTypeStg(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, cf: UInt16, lpszUserType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadFmtUserTypeStg(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, pcf: POINTER(UInt16), lplpszUserType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorage(lpolestream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAM(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, lpolestream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def SetConvertStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, fConvert: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAMEx(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, cfFormat: UInt16, lWidth: Int32, lHeight: Int32, dwSize: UInt32, pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head), polestm: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorageEx(polestm: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, pcfFormat: POINTER(UInt16), plwWidth: POINTER(Int32), plHeight: POINTER(Int32), pdwSize: POINTER(UInt32), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToWinRTPropertyValue(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def WinRTPropertyValueToPropVariant(punkPropertyValue: win32more.Windows.Win32.System.Com.IUnknown_head, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromResource(hinst: win32more.Windows.Win32.Foundation.HINSTANCE, id: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBuffer(pv: VoidPtr, cb: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromCLSID(clsid: POINTER(Guid), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromGUIDAsString(guid: POINTER(Guid), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTime(pftIn: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromPropVariantVectorElem(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantVectorFromPropVariant(propvarSingle: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppropvarVector: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBooleanVector(prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt16Vector(prgn: POINTER(Int16), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt16Vector(prgn: POINTER(UInt16), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt32Vector(prgn: POINTER(Int32), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt32Vector(prgn: POINTER(UInt32), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt64Vector(prgn: POINTER(Int64), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt64Vector(prgn: POINTER(UInt64), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromDoubleVector(prgn: POINTER(Double), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTimeVector(prgft: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringVector(prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringAsVector(psz: win32more.Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pszDefault: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBoolean(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pfRet: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), piRet: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), puiRet: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), plRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pulRet: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pllRet: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pullRet: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDouble(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdblRet: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBuffer(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToString(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), psz: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToGUID(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppszOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBSTR(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTime(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pstfOut: win32more.Windows.Win32.System.Variant.PSTIME_FLAGS, pftOut: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetElementCount(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), crgf: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgft: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), crgft: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgf: POINTER(POINTER(win32more.Windows.Win32.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgft: POINTER(POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgsz: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetBooleanElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pfVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt16Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt16Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt32Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt32Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt64Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt64Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetDoubleElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetFileTimeElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pftVal: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetStringElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppszVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearPropVariantArray(rgPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), cVars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def PropVariantCompareEx(propvar1: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propvar2: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), unit: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT, flags: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantChangeType(ppropvarDest: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propvarSrc: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), flags: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS, vt: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToVariant(pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToPropVariant(pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgSerializePropVariant(ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppProp: POINTER(POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head)), pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgDeserializePropVariant(pprop: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbMax: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class BSTRBLOB(EasyCastStructure):
    cbSize: UInt32
    pData: POINTER(Byte)
class CABOOL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
class CABSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.BSTR)
class CABSTRBLOB(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.BSTRBLOB_head)
class CAC(EasyCastStructure):
    cElems: UInt32
    pElems: win32more.Windows.Win32.Foundation.PSTR
class CACLIPDATA(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.CLIPDATA_head)
class CACLSID(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Guid)
class CACY(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.CY_head)
class CADATE(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Double)
class CADBL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Double)
class CAFILETIME(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)
class CAFLT(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Single)
class CAH(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int64)
class CAI(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int16)
class CAL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CALPSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.PSTR)
class CALPWSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class CAPROPVARIANT(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
class CASCODE(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CAUB(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Byte)
class CAUH(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt64)
class CAUI(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt16)
class CAUL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CLIPDATA(EasyCastStructure):
    cbSize: UInt32
    ulClipFmt: Int32
    pClipData: POINTER(Byte)
class IDirectWriterLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d92-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def WaitForWriteAccess(self, dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteAccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HaveWriteAccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSETSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013b-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000139-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.STATSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFillLockBytes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99caf010-415e-11cf-8814-00aa00b569f5}')
    @commethod(3)
    def FillAppend(self, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FillAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFillSize(self, ulSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self, bCanceled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILayoutStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d90-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def LayoutScript(self, pStorageLayout: POINTER(win32more.Windows.Win32.System.Com.StorageLayout_head), nEntries: UInt32, glfInterleavedFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginMonitor(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndMonitor(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReLayoutDocfile(self, pwcsNewDfName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReLayoutDocfileOnILockBytes(self, pILockBytes: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILockBytes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000a-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, cb: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stat(self, pstatstg: POINTER(win32more.Windows.Win32.System.Com.STATSTG_head), grfStatFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{0000010a-0000-0000-c000-000000000046}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitNew(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Load(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Save(self, pStgSave: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, fSameAsLoad: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveCompleted(self, pStgNew: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HandsOffStorage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55272a00-42cb-11ce-8135-00aa004bb851}')
    @commethod(3)
    def Read(self, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pErrorLog: win32more.Windows.Win32.System.Com.IErrorLog_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f55882-280b-11d0-a8a9-00a0c90c2004}')
    @commethod(3)
    def Read(self, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pErrLog: win32more.Windows.Win32.System.Com.IErrorLog_head, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), phrError: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountProperties(self, pcProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyInfo(self, iProperty: UInt32, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pcProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadObject(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR, dwHint: UInt32, pUnkObject: win32more.Windows.Win32.System.Com.IUnknown_head, pErrLog: win32more.Windows.Win32.System.Com.IErrorLog_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertySetStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013a-0000-0000-c000-000000000046}')
    @commethod(3)
    def Create(self, rfmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, ppprstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Open(self, rfmtid: POINTER(Guid), grfMode: UInt32, ppprstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, rfmtid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enum(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000138-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadPropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WritePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Enum(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimes(self, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetClass(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stat(self, pstatpsstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRootStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000012-0000-0000-c000-000000000046}')
    @commethod(3)
    def SwitchToFile(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000b-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateStream(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStream(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, reserved1: VoidPtr, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved2: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStorage(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenStorage(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(self, ciidExclude: UInt32, rgiidExclude: POINTER(Guid), snbExclude: POINTER(POINTER(UInt16)), pstgDest: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveElementTo(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgDest: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, pwcsNewName: win32more.Windows.Win32.Foundation.PWSTR, grfFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumElements(self, reserved1: UInt32, reserved2: VoidPtr, reserved3: UInt32, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DestroyElement(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameElement(self, pwcsOldName: win32more.Windows.Win32.Foundation.PWSTR, pwcsNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetElementTimes(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetClass(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateBits(self, grfStateBits: UInt32, grfMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Stat(self, pstatstg: POINTER(win32more.Windows.Win32.System.Com.STATSTG_head), grfStatFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OLESTREAM(EasyCastStructure):
    lpstbl: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAMVTBL_head)
class OLESTREAMVTBL(EasyCastStructure):
    Get: IntPtr
    Put: IntPtr
PIDMSI_STATUS_VALUE = Int32
PIDMSI_STATUS_NORMAL: PIDMSI_STATUS_VALUE = 0
PIDMSI_STATUS_NEW: PIDMSI_STATUS_VALUE = 1
PIDMSI_STATUS_PRELIM: PIDMSI_STATUS_VALUE = 2
PIDMSI_STATUS_DRAFT: PIDMSI_STATUS_VALUE = 3
PIDMSI_STATUS_INPROGRESS: PIDMSI_STATUS_VALUE = 4
PIDMSI_STATUS_EDIT: PIDMSI_STATUS_VALUE = 5
PIDMSI_STATUS_REVIEW: PIDMSI_STATUS_VALUE = 6
PIDMSI_STATUS_PROOF: PIDMSI_STATUS_VALUE = 7
PIDMSI_STATUS_FINAL: PIDMSI_STATUS_VALUE = 8
PIDMSI_STATUS_OTHER: PIDMSI_STATUS_VALUE = 32767
class PROPBAG2(EasyCastStructure):
    dwType: UInt32
    vt: win32more.Windows.Win32.System.Variant.VARENUM
    cfType: UInt16
    dwHint: UInt32
    pstrName: win32more.Windows.Win32.Foundation.PWSTR
    clsid: Guid
class PROPSPEC(EasyCastStructure):
    ulKind: win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        propid: UInt32
        lpwstr: win32more.Windows.Win32.Foundation.PWSTR
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR: PROPSPEC_KIND = 0
PRSPEC_PROPID: PROPSPEC_KIND = 1
class PROPVARIANT(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        decVal: win32more.Windows.Win32.Foundation.DECIMAL
        class _Anonymous_e__Struct(EasyCastStructure):
            vt: win32more.Windows.Win32.System.Variant.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(EasyCastUnion):
                cVal: win32more.Windows.Win32.Foundation.CHAR
                bVal: Byte
                iVal: Int16
                uiVal: UInt16
                lVal: Int32
                ulVal: UInt32
                intVal: Int32
                uintVal: UInt32
                hVal: Int64
                uhVal: UInt64
                fltVal: Single
                dblVal: Double
                boolVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: win32more.Windows.Win32.System.Com.CY
                date: Double
                filetime: win32more.Windows.Win32.Foundation.FILETIME
                puuid: POINTER(Guid)
                pclipdata: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.CLIPDATA_head)
                bstrVal: win32more.Windows.Win32.Foundation.BSTR
                bstrblobVal: win32more.Windows.Win32.System.Com.StructuredStorage.BSTRBLOB
                blob: win32more.Windows.Win32.System.Com.BLOB
                pszVal: win32more.Windows.Win32.Foundation.PSTR
                pwszVal: win32more.Windows.Win32.Foundation.PWSTR
                punkVal: win32more.Windows.Win32.System.Com.IUnknown_head
                pdispVal: win32more.Windows.Win32.System.Com.IDispatch_head
                pStream: win32more.Windows.Win32.System.Com.IStream_head
                pStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head
                pVersionedStream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.VERSIONEDSTREAM_head)
                parray: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY_head)
                cac: win32more.Windows.Win32.System.Com.StructuredStorage.CAC
                caub: win32more.Windows.Win32.System.Com.StructuredStorage.CAUB
                cai: win32more.Windows.Win32.System.Com.StructuredStorage.CAI
                caui: win32more.Windows.Win32.System.Com.StructuredStorage.CAUI
                cal: win32more.Windows.Win32.System.Com.StructuredStorage.CAL
                caul: win32more.Windows.Win32.System.Com.StructuredStorage.CAUL
                cah: win32more.Windows.Win32.System.Com.StructuredStorage.CAH
                cauh: win32more.Windows.Win32.System.Com.StructuredStorage.CAUH
                caflt: win32more.Windows.Win32.System.Com.StructuredStorage.CAFLT
                cadbl: win32more.Windows.Win32.System.Com.StructuredStorage.CADBL
                cabool: win32more.Windows.Win32.System.Com.StructuredStorage.CABOOL
                cascode: win32more.Windows.Win32.System.Com.StructuredStorage.CASCODE
                cacy: win32more.Windows.Win32.System.Com.StructuredStorage.CACY
                cadate: win32more.Windows.Win32.System.Com.StructuredStorage.CADATE
                cafiletime: win32more.Windows.Win32.System.Com.StructuredStorage.CAFILETIME
                cauuid: win32more.Windows.Win32.System.Com.StructuredStorage.CACLSID
                caclipdata: win32more.Windows.Win32.System.Com.StructuredStorage.CACLIPDATA
                cabstr: win32more.Windows.Win32.System.Com.StructuredStorage.CABSTR
                cabstrblob: win32more.Windows.Win32.System.Com.StructuredStorage.CABSTRBLOB
                calpstr: win32more.Windows.Win32.System.Com.StructuredStorage.CALPSTR
                calpwstr: win32more.Windows.Win32.System.Com.StructuredStorage.CALPWSTR
                capropvar: win32more.Windows.Win32.System.Com.StructuredStorage.CAPROPVARIANT
                pcVal: win32more.Windows.Win32.Foundation.PSTR
                pbVal: POINTER(Byte)
                piVal: POINTER(Int16)
                puiVal: POINTER(UInt16)
                plVal: POINTER(Int32)
                pulVal: POINTER(UInt32)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
                pdecVal: POINTER(win32more.Windows.Win32.Foundation.DECIMAL_head)
                pscode: POINTER(Int32)
                pcyVal: POINTER(win32more.Windows.Win32.System.Com.CY_head)
                pdate: POINTER(Double)
                pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)
                ppunkVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)
                ppdispVal: POINTER(win32more.Windows.Win32.System.Com.IDispatch_head)
                pparray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY_head))
                pvarVal: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
PROPVAR_CHANGE_FLAGS = Int32
PVCHF_DEFAULT: PROPVAR_CHANGE_FLAGS = 0
PVCHF_NOVALUEPROP: PROPVAR_CHANGE_FLAGS = 1
PVCHF_ALPHABOOL: PROPVAR_CHANGE_FLAGS = 2
PVCHF_NOUSEROVERRIDE: PROPVAR_CHANGE_FLAGS = 4
PVCHF_LOCALBOOL: PROPVAR_CHANGE_FLAGS = 8
PVCHF_NOHEXSTRING: PROPVAR_CHANGE_FLAGS = 16
PROPVAR_COMPARE_FLAGS = Int32
PVCF_DEFAULT: PROPVAR_COMPARE_FLAGS = 0
PVCF_TREATEMPTYASGREATERTHAN: PROPVAR_COMPARE_FLAGS = 1
PVCF_USESTRCMP: PROPVAR_COMPARE_FLAGS = 2
PVCF_USESTRCMPC: PROPVAR_COMPARE_FLAGS = 4
PVCF_USESTRCMPI: PROPVAR_COMPARE_FLAGS = 8
PVCF_USESTRCMPIC: PROPVAR_COMPARE_FLAGS = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE: PROPVAR_COMPARE_FLAGS = 32
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT: PROPVAR_COMPARE_UNIT = 0
PVCU_SECOND: PROPVAR_COMPARE_UNIT = 1
PVCU_MINUTE: PROPVAR_COMPARE_UNIT = 2
PVCU_HOUR: PROPVAR_COMPARE_UNIT = 3
PVCU_DAY: PROPVAR_COMPARE_UNIT = 4
PVCU_MONTH: PROPVAR_COMPARE_UNIT = 5
PVCU_YEAR: PROPVAR_COMPARE_UNIT = 6
class RemSNB(EasyCastStructure):
    ulCntStr: UInt32
    ulCntChar: UInt32
    rgString: Char * 1
class SERIALIZEDPROPERTYVALUE(EasyCastStructure):
    dwType: UInt32
    rgb: Byte * 1
class STATPROPSETSTG(EasyCastStructure):
    fmtid: Guid
    clsid: Guid
    grfFlags: UInt32
    mtime: win32more.Windows.Win32.Foundation.FILETIME
    ctime: win32more.Windows.Win32.Foundation.FILETIME
    atime: win32more.Windows.Win32.Foundation.FILETIME
    dwOSVersion: UInt32
class STATPROPSTG(EasyCastStructure):
    lpwstrName: win32more.Windows.Win32.Foundation.PWSTR
    propid: UInt32
    vt: win32more.Windows.Win32.System.Variant.VARENUM
STGFMT = UInt32
STGFMT_STORAGE: STGFMT = 0
STGFMT_NATIVE: STGFMT = 1
STGFMT_FILE: STGFMT = 3
STGFMT_ANY: STGFMT = 4
STGFMT_DOCFILE: STGFMT = 5
STGFMT_DOCUMENT: STGFMT = 0
STGMOVE = Int32
STGMOVE_MOVE: STGMOVE = 0
STGMOVE_COPY: STGMOVE = 1
STGMOVE_SHALLOWCOPY: STGMOVE = 2
class STGOPTIONS(EasyCastStructure):
    usVersion: UInt16
    reserved: UInt16
    ulSectorSize: UInt32
    pwcsTemplateFile: win32more.Windows.Win32.Foundation.PWSTR
class VERSIONEDSTREAM(EasyCastStructure):
    guidVersion: Guid
    pStream: win32more.Windows.Win32.System.Com.IStream_head
make_head(_module, 'BSTRBLOB')
make_head(_module, 'CABOOL')
make_head(_module, 'CABSTR')
make_head(_module, 'CABSTRBLOB')
make_head(_module, 'CAC')
make_head(_module, 'CACLIPDATA')
make_head(_module, 'CACLSID')
make_head(_module, 'CACY')
make_head(_module, 'CADATE')
make_head(_module, 'CADBL')
make_head(_module, 'CAFILETIME')
make_head(_module, 'CAFLT')
make_head(_module, 'CAH')
make_head(_module, 'CAI')
make_head(_module, 'CAL')
make_head(_module, 'CALPSTR')
make_head(_module, 'CALPWSTR')
make_head(_module, 'CAPROPVARIANT')
make_head(_module, 'CASCODE')
make_head(_module, 'CAUB')
make_head(_module, 'CAUH')
make_head(_module, 'CAUI')
make_head(_module, 'CAUL')
make_head(_module, 'CLIPDATA')
make_head(_module, 'IDirectWriterLock')
make_head(_module, 'IEnumSTATPROPSETSTG')
make_head(_module, 'IEnumSTATPROPSTG')
make_head(_module, 'IEnumSTATSTG')
make_head(_module, 'IFillLockBytes')
make_head(_module, 'ILayoutStorage')
make_head(_module, 'ILockBytes')
make_head(_module, 'IPersistStorage')
make_head(_module, 'IPropertyBag')
make_head(_module, 'IPropertyBag2')
make_head(_module, 'IPropertySetStorage')
make_head(_module, 'IPropertyStorage')
make_head(_module, 'IRootStorage')
make_head(_module, 'IStorage')
make_head(_module, 'OLESTREAM')
make_head(_module, 'OLESTREAMVTBL')
make_head(_module, 'PROPBAG2')
make_head(_module, 'PROPSPEC')
make_head(_module, 'PROPVARIANT')
make_head(_module, 'RemSNB')
make_head(_module, 'SERIALIZEDPROPERTYVALUE')
make_head(_module, 'STATPROPSETSTG')
make_head(_module, 'STATPROPSTG')
make_head(_module, 'STGOPTIONS')
make_head(_module, 'VERSIONEDSTREAM')
