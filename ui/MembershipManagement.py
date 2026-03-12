from ui.Base import BaseUI
from ui.CardInput import CardInputUI

class MembershipManagementUI(BaseUI):
    def __init__(self, user_id):
        super().__init__("GymPro: Membership Management")
        self.user_id = user_id
        
        self._StartGridBuild()

        self._AddText(f"Current Membership Status: {self.FetchMembershipStatus()}")
        self._AddButton("Upgrade to Plus", event=self.__e_PlusPressed)
        self._AddButton("Upgrade to Pro", event=self.__e_ProPressed)
        self._AddButton("Upgrade to Pro+", event=self.__e_PlusProPressed)
        
        self._EndGridBuild()
    
    def FetchMembershipStatus(self):
        # Jamie: fetch membership status from database here.
        return "No Membership" 
    
    def OpenCardGUI(self) -> bool:
        self.next_gui = CardInputUI(self.user_id)
        self.next_gui.Show()
    
    def __e_PlusPressed(self, event):
        self.OpenCardGUI()
    def __e_ProPressed(self, event):
        self.OpenCardGUI()
    def __e_PlusProPressed(self, event):
        self.OpenCardGUI()