import { SidebarWrapper } from "@/components/sidebar-wrapper";

function Sessions() {
    return (
        <SidebarWrapper title="Sessions">
            <div className="p-4 login-card-enter">
                <p className="text-gray-600">Your recent sessions will appear here.</p>
            </div>
        </SidebarWrapper>
    )
}

export default Sessions