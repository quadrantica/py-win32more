from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.Ribbon
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
UI_ALL_COMMANDS: UInt32 = 0
UI_COLLECTION_INVALIDINDEX: UInt32 = 4294967295
LIBID_UIRibbon: Guid = Guid('{942f35c2-e83b-45ef-b085-ac295dd63d5b}')
class IUIApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d428903c-729a-491d-910d-682a08ff2522}')
    @commethod(3)
    def OnViewChanged(self, viewId: UInt32, typeID: win32more.Windows.Win32.UI.Ribbon.UI_VIEWTYPE, view: win32more.Windows.Win32.System.Com.IUnknown_head, verb: win32more.Windows.Win32.UI.Ribbon.UI_VIEWVERB, uReasonCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCreateUICommand(self, commandId: UInt32, typeID: win32more.Windows.Win32.UI.Ribbon.UI_COMMANDTYPE, commandHandler: POINTER(win32more.Windows.Win32.UI.Ribbon.IUICommandHandler_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDestroyUICommand(self, commandId: UInt32, typeID: win32more.Windows.Win32.UI.Ribbon.UI_COMMANDTYPE, commandHandler: win32more.Windows.Win32.UI.Ribbon.IUICommandHandler_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUICollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df4f45bf-6f9d-4dd7-9d68-d8f9cd18c4db}')
    @commethod(3)
    def GetCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, index: UInt32, item: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, item: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Insert(self, index: UInt32, item: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Replace(self, indexReplaced: UInt32, itemReplaceWith: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUICollectionChangedEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6502ae91-a14d-44b5-bbd0-62aacc581d52}')
    @commethod(3)
    def OnChanged(self, action: win32more.Windows.Win32.UI.Ribbon.UI_COLLECTIONCHANGE, oldIndex: UInt32, oldItem: win32more.Windows.Win32.System.Com.IUnknown_head, newIndex: UInt32, newItem: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUICommandHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75ae0a2d-dc03-4c9f-8883-069660d0beb6}')
    @commethod(3)
    def Execute(self, commandId: UInt32, verb: win32more.Windows.Win32.UI.Ribbon.UI_EXECUTIONVERB, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), currentValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), commandExecutionProperties: win32more.Windows.Win32.UI.Ribbon.IUISimplePropertySet_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProperty(self, commandId: UInt32, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), currentValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), newValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIContextualUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eea11f37-7c46-437c-8e55-b52122b29293}')
    @commethod(3)
    def ShowAtLocation(self, x: Int32, y: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIEventLogger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec3e1034-dbf4-41a1-95d5-03e0f1026e05}')
    @commethod(3)
    def OnUIEvent(self, pEventParams: POINTER(win32more.Windows.Win32.UI.Ribbon.UI_EVENTPARAMS_head)) -> Void: ...
class IUIEventingManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3be6ea7f-9a9b-4198-9368-9b0f923bd534}')
    @commethod(3)
    def SetEventLogger(self, eventLogger: win32more.Windows.Win32.UI.Ribbon.IUIEventLogger_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIFramework(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4f0385d-6872-43a8-ad09-4c339cb3f5c5}')
    @commethod(3)
    def Initialize(self, frameWnd: win32more.Windows.Win32.Foundation.HWND, application: win32more.Windows.Win32.UI.Ribbon.IUIApplication_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Destroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadUI(self, instance: win32more.Windows.Win32.Foundation.HINSTANCE, resourceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetView(self, viewId: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUICommandProperty(self, commandId: UInt32, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetUICommandProperty(self, commandId: UInt32, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InvalidateUICommand(self, commandId: UInt32, flags: win32more.Windows.Win32.UI.Ribbon.UI_INVALIDATIONS, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FlushPendingInvalidations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetModes(self, iModes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23c8c838-4de6-436b-ab01-5554bb7c30dd}')
    @commethod(3)
    def GetBitmap(self, bitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIImageFromBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18aba7f3-4c1c-4ba2-bf6c-f5c3326fa816}')
    @commethod(3)
    def CreateImage(self, bitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, options: win32more.Windows.Win32.UI.Ribbon.UI_OWNERSHIP, image: POINTER(win32more.Windows.Win32.UI.Ribbon.IUIImage_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIRibbon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{803982ab-370a-4f7e-a9e7-8784036a6e26}')
    @commethod(3)
    def GetHeight(self, cy: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadSettingsFromStream(self, pStream: win32more.Windows.Win32.System.Com.IStream_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveSettingsToStream(self, pStream: win32more.Windows.Win32.System.Com.IStream_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUISimplePropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c205bb48-5b1c-4219-a106-15bd0a5f24e2}')
    @commethod(3)
    def GetValue(self, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UIRibbonFramework = Guid('{926749fa-2615-4987-8845-c33e65f2b957}')
UIRibbonImageFromBitmapFactory = Guid('{0f7434b6-59b6-4250-999e-d168d6ae4293}')
UI_COLLECTIONCHANGE = Int32
UI_COLLECTIONCHANGE_INSERT: UI_COLLECTIONCHANGE = 0
UI_COLLECTIONCHANGE_REMOVE: UI_COLLECTIONCHANGE = 1
UI_COLLECTIONCHANGE_REPLACE: UI_COLLECTIONCHANGE = 2
UI_COLLECTIONCHANGE_RESET: UI_COLLECTIONCHANGE = 3
UI_COMMANDTYPE = Int32
UI_COMMANDTYPE_UNKNOWN: UI_COMMANDTYPE = 0
UI_COMMANDTYPE_GROUP: UI_COMMANDTYPE = 1
UI_COMMANDTYPE_ACTION: UI_COMMANDTYPE = 2
UI_COMMANDTYPE_ANCHOR: UI_COMMANDTYPE = 3
UI_COMMANDTYPE_CONTEXT: UI_COMMANDTYPE = 4
UI_COMMANDTYPE_COLLECTION: UI_COMMANDTYPE = 5
UI_COMMANDTYPE_COMMANDCOLLECTION: UI_COMMANDTYPE = 6
UI_COMMANDTYPE_DECIMAL: UI_COMMANDTYPE = 7
UI_COMMANDTYPE_BOOLEAN: UI_COMMANDTYPE = 8
UI_COMMANDTYPE_FONT: UI_COMMANDTYPE = 9
UI_COMMANDTYPE_RECENTITEMS: UI_COMMANDTYPE = 10
UI_COMMANDTYPE_COLORANCHOR: UI_COMMANDTYPE = 11
UI_COMMANDTYPE_COLORCOLLECTION: UI_COMMANDTYPE = 12
UI_CONTEXTAVAILABILITY = Int32
UI_CONTEXTAVAILABILITY_NOTAVAILABLE: UI_CONTEXTAVAILABILITY = 0
UI_CONTEXTAVAILABILITY_AVAILABLE: UI_CONTEXTAVAILABILITY = 1
UI_CONTEXTAVAILABILITY_ACTIVE: UI_CONTEXTAVAILABILITY = 2
UI_CONTROLDOCK = Int32
UI_CONTROLDOCK_TOP: UI_CONTROLDOCK = 1
UI_CONTROLDOCK_BOTTOM: UI_CONTROLDOCK = 3
UI_EVENTLOCATION = Int32
UI_EVENTLOCATION_Ribbon: UI_EVENTLOCATION = 0
UI_EVENTLOCATION_QAT: UI_EVENTLOCATION = 1
UI_EVENTLOCATION_ApplicationMenu: UI_EVENTLOCATION = 2
UI_EVENTLOCATION_ContextPopup: UI_EVENTLOCATION = 3
class UI_EVENTPARAMS(EasyCastStructure):
    EventType: win32more.Windows.Win32.UI.Ribbon.UI_EVENTTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Modes: Int32
        Params: win32more.Windows.Win32.UI.Ribbon.UI_EVENTPARAMS_COMMAND
class UI_EVENTPARAMS_COMMAND(EasyCastStructure):
    CommandID: UInt32
    CommandName: win32more.Windows.Win32.Foundation.PWSTR
    ParentCommandID: UInt32
    ParentCommandName: win32more.Windows.Win32.Foundation.PWSTR
    SelectionIndex: UInt32
    Location: win32more.Windows.Win32.UI.Ribbon.UI_EVENTLOCATION
UI_EVENTTYPE = Int32
UI_EVENTTYPE_ApplicationMenuOpened: UI_EVENTTYPE = 0
UI_EVENTTYPE_RibbonMinimized: UI_EVENTTYPE = 1
UI_EVENTTYPE_RibbonExpanded: UI_EVENTTYPE = 2
UI_EVENTTYPE_ApplicationModeSwitched: UI_EVENTTYPE = 3
UI_EVENTTYPE_TabActivated: UI_EVENTTYPE = 4
UI_EVENTTYPE_MenuOpened: UI_EVENTTYPE = 5
UI_EVENTTYPE_CommandExecuted: UI_EVENTTYPE = 6
UI_EVENTTYPE_TooltipShown: UI_EVENTTYPE = 7
UI_EXECUTIONVERB = Int32
UI_EXECUTIONVERB_EXECUTE: UI_EXECUTIONVERB = 0
UI_EXECUTIONVERB_PREVIEW: UI_EXECUTIONVERB = 1
UI_EXECUTIONVERB_CANCELPREVIEW: UI_EXECUTIONVERB = 2
UI_FONTDELTASIZE = Int32
UI_FONTDELTASIZE_GROW: UI_FONTDELTASIZE = 0
UI_FONTDELTASIZE_SHRINK: UI_FONTDELTASIZE = 1
UI_FONTPROPERTIES = Int32
UI_FONTPROPERTIES_NOTAVAILABLE: UI_FONTPROPERTIES = 0
UI_FONTPROPERTIES_NOTSET: UI_FONTPROPERTIES = 1
UI_FONTPROPERTIES_SET: UI_FONTPROPERTIES = 2
UI_FONTUNDERLINE = Int32
UI_FONTUNDERLINE_NOTAVAILABLE: UI_FONTUNDERLINE = 0
UI_FONTUNDERLINE_NOTSET: UI_FONTUNDERLINE = 1
UI_FONTUNDERLINE_SET: UI_FONTUNDERLINE = 2
UI_FONTVERTICALPOSITION = Int32
UI_FONTVERTICALPOSITION_NOTAVAILABLE: UI_FONTVERTICALPOSITION = 0
UI_FONTVERTICALPOSITION_NOTSET: UI_FONTVERTICALPOSITION = 1
UI_FONTVERTICALPOSITION_SUPERSCRIPT: UI_FONTVERTICALPOSITION = 2
UI_FONTVERTICALPOSITION_SUBSCRIPT: UI_FONTVERTICALPOSITION = 3
UI_INVALIDATIONS = Int32
UI_INVALIDATIONS_STATE: UI_INVALIDATIONS = 1
UI_INVALIDATIONS_VALUE: UI_INVALIDATIONS = 2
UI_INVALIDATIONS_PROPERTY: UI_INVALIDATIONS = 4
UI_INVALIDATIONS_ALLPROPERTIES: UI_INVALIDATIONS = 8
UI_OWNERSHIP = Int32
UI_OWNERSHIP_TRANSFER: UI_OWNERSHIP = 0
UI_OWNERSHIP_COPY: UI_OWNERSHIP = 1
UI_SWATCHCOLORMODE = Int32
UI_SWATCHCOLORMODE_NORMAL: UI_SWATCHCOLORMODE = 0
UI_SWATCHCOLORMODE_MONOCHROME: UI_SWATCHCOLORMODE = 1
UI_SWATCHCOLORTYPE = Int32
UI_SWATCHCOLORTYPE_NOCOLOR: UI_SWATCHCOLORTYPE = 0
UI_SWATCHCOLORTYPE_AUTOMATIC: UI_SWATCHCOLORTYPE = 1
UI_SWATCHCOLORTYPE_RGB: UI_SWATCHCOLORTYPE = 2
UI_VIEWTYPE = Int32
UI_VIEWTYPE_RIBBON: UI_VIEWTYPE = 1
UI_VIEWVERB = Int32
UI_VIEWVERB_CREATE: UI_VIEWVERB = 0
UI_VIEWVERB_DESTROY: UI_VIEWVERB = 1
UI_VIEWVERB_SIZE: UI_VIEWVERB = 2
UI_VIEWVERB_ERROR: UI_VIEWVERB = 3
make_head(_module, 'IUIApplication')
make_head(_module, 'IUICollection')
make_head(_module, 'IUICollectionChangedEvent')
make_head(_module, 'IUICommandHandler')
make_head(_module, 'IUIContextualUI')
make_head(_module, 'IUIEventLogger')
make_head(_module, 'IUIEventingManager')
make_head(_module, 'IUIFramework')
make_head(_module, 'IUIImage')
make_head(_module, 'IUIImageFromBitmap')
make_head(_module, 'IUIRibbon')
make_head(_module, 'IUISimplePropertySet')
make_head(_module, 'UI_EVENTPARAMS')
make_head(_module, 'UI_EVENTPARAMS_COMMAND')
