import wx

class BaseUI(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None,
                         title=title,
                         size=(100, 100),
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

    def _StartGridBuild(self):
        self.panel = wx.Panel(self)
        self.grid = wx.GridBagSizer(vgap=10, hgap=10)
        
        # Handling dynamic row assignment
        self.__next_row = 0

    def _NextRow(self) -> int:
        row = self.__next_row
        self.__next_row += 1
        return row
    
    def __ResolvePosition(self, pos : tuple[int, int], span: tuple[int, int]):
        if pos is None:
            return (self._NextRow(), 0)
        # Keep cursor in sync when a manual pos is used
        self.__next_row = max(self.__next_row, pos[0] + span[0])
        return pos

    def _EndGridBuild(self):
        self.panel.SetSizerAndFit(self.grid)
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        frame_sizer.Add(self.panel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 15)
        
        self.SetSizerAndFit(frame_sizer)
        self.Centre()

    def _AddText(self, text : str, pos : tuple[int, int] | None = None, span : tuple[int, int] = (1, 1), underline : bool = False, bold : bool = False) -> wx.StaticText:
        pos = self.__ResolvePosition(pos, span)
        
        static_text = wx.StaticText(self.panel, label=text)
        
        if underline:
            font = static_text.GetFont()
            font.MakeUnderlined()
            static_text.SetFont(font)
        
        if bold:
            font = static_text.GetFont()
            font.MakeBold()
            static_text.SetFont(font)
        
        self.grid.Add(
            static_text,
            pos=(pos[0], pos[1]),
            span=(span[0], span[1]),
            flag=wx.ALIGN_CENTER
        )
        return static_text
        
    def _AddTextbox(self, pos : tuple[int, int] | None = None, span : tuple[int, int] = (1, 1)) -> wx.TextCtrl:
        textbox = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        pos = self.__ResolvePosition(pos, span)
        self.grid.Add(
            textbox, 
            pos=(pos[0], pos[1]),
            span=(span[0], span[1]),
            flag=wx.ALIGN_CENTER
        ) 
        return textbox
    
    def _AddButton(self, text : str, pos : tuple[int, int] | None = None, span : tuple[int, int] = (1, 1), event : callable = None) -> wx.Button:
        pos = self.__ResolvePosition(pos, span)
        button = wx.Button(self.panel, label=text)
        button.SetMinSize((200, 35))
        self.grid.Add(
                button,
                pos=(pos[0], pos[1]),
                span=(span[0], span[1]),
                flag=wx.ALIGN_CENTER | wx.EXPAND
        )
        if event:
            button.Bind(wx.EVT_BUTTON, event)
        return button
    
    def _AddDivider(self, pos : tuple[int, int] | None = None, span : tuple[int, int] = (1, 1), vertical : bool = False):
        pos = self.__ResolvePosition(pos, span)
        style = wx.LI_VERTICAL if vertical else wx.LI_HORIZONTAL
        line = wx.StaticLine(self.panel, style=style)
        self.grid.Add(
            line,
            pos=(pos[0], pos[1]),
            span=(span[0], span[1]),
            flag=wx.EXPAND | wx.ALIGN_CENTER_VERTICAL
        )
        return line