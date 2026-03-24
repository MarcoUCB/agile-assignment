import { SidebarWrapper } from "@/components/sidebar-wrapper";
import { Button } from "@/components/ui/button";

function AccountOptions() {
    return (
        <SidebarWrapper title="Account Options">
            <div className="flex flex-col gap-4 p-8 login-card-enter">
                <Button variant="default">Request your Data</Button>
                <Button variant="default">Delete Account</Button>
            </div>
        </SidebarWrapper>
    )
}
export default AccountOptions