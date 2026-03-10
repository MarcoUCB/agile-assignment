import wx

# UNDERSCORE DEFINITIONS
#     - _ = Protected
#     - __ = Private

class BaseGUI(wx.Frame):
    def __init__(self, title, size : tuple[int, int]):
        super().__init__(parent=None,
                         title=title,
                         size=size,
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

    def _StartGridBuild(self, rows : int, cols : int):
        self.panel = wx.Panel(self)
        self.grid = wx.GridBagSizer(vgap=10, hgap=10)

    def _EndGridBuild(self):
        self.panel.SetSizerAndFit(self.grid)
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        frame_sizer.Add(self.panel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 15)
        
        self.SetSizerAndFit(frame_sizer)
        self.Centre()

    def _AddText(self, text : str, pos : tuple[int, int], span : tuple[int, int] = (1, 1)):
        self.grid.Add(
            wx.StaticText(self.panel, label=text),
            pos=(pos[0], pos[1]),
            span=(span[0], span[1]),
            flag=wx.ALIGN_CENTER
        )
        
    def _AddTextbox(self, pos : tuple[int, int], span : tuple[int, int] = (1, 1)):
        self.grid.Add(
            wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER), 
            pos=(pos[0], pos[1]),
            span=(span[0], span[1]),
            flag=wx.ALIGN_CENTER
        ) 
    
    def _AddButton(self, text : str, pos : tuple[int, int], span : tuple[int, int] = (1, 1)) -> wx.Button:
        button = wx.Button(self.panel, label=text)
        self.grid.Add(
                button,
                pos=(pos[0], pos[1]),
                span=(span[0], span[1]),
                flag=wx.ALIGN_CENTER
        )
        return button


# PARENT ROOT GUI
class WelcomeGUI(BaseGUI):
    def __init__(self, title):
        # ^ is the Bitwise XOR operation. By XORing default frame style with resizing we remove resizing.
        super().__init__("GymPro: Welcome", (100, 100))
        
        self._StartGridBuild(4, 2)
        
        self._AddText("Welcome to GymPro", (0, 0), (1, 2))
        
        self._AddText("Login: ", (1, 0))
        self._AddTextbox((1, 1))
        
        self._AddText("Password: ", (2, 0))
        self._AddTextbox((2, 1))
        
        widget_login_button = self._AddButton("Login / Register", (3, 0), (1, 2))
        widget_login_button.Bind(wx.EVT_BUTTON, self._onLoginButtonPress)

        self._EndGridBuild()
    
    def _onLoginButtonPress(self, event):
        # Jamie: Implement user login / register
        wx.MessageBox("Clicked!")
        