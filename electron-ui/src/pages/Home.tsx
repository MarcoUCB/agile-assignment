import { SidebarWrapper } from '../components/sidebar-wrapper'

function Home() {
  return (
    <SidebarWrapper title="Home">
      <div className="p-8 login-card-enter">
        <h1 className="text-3xl font-bold mb-4">Welcome to the Home Page</h1>
        <p>This is the home page content.</p>
      </div>
    </SidebarWrapper>
  )
}

export default Home
