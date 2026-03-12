
from ui.Base import BaseUI
from ui.MembershipManagement import MembershipManagementUI


class UserDashboardUI(BaseUI):
    def __init__(self, user_id : int):
        super().__init__("GymPro: Dashboard")
        self.user_id = user_id
        
        self._StartGridBuild()
        
        self._AddText("Statistics", underline=True)
        
        self._AddDivider()
        
        self._AddText("Management", underline=True)
        
        self._AddButton("Membership Management", event=self.__e_MembershipManagementPressed)
        self._AddButton("Parking Management")
        self._AddButton("Book a Session")
        self._AddButton("Delete Account ")
        
        self._EndGridBuild()
    
    def __e_MembershipManagementPressed(self, event):
        self.next_gui = MembershipManagementUI(self.user_id)
        self.next_gui.Show()