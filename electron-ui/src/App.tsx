import {
  CalendarClockIcon,
  CarFrontIcon,
  HouseIcon,
  IdCardIcon,
  LogOutIcon,
  MoonIcon,
  Settings2Icon,
  ShieldCheckIcon,
  SunIcon,
} from 'lucide-react'
import { useEffect, useState } from 'react'

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarInset,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
} from '@/components/ui/sidebar'
import { Button } from '@/components/ui/button'
import { useNavigate } from 'react-router-dom'

const navigationItems = [
  { title: 'Home', href: '#', icon: HouseIcon },
  { title: 'Membership', href: '/membership', icon: IdCardIcon },
  { title: 'Parking', href: '/parking', icon: CarFrontIcon },
  { title: 'Sessions', href: '/sessions', icon: CalendarClockIcon },
  { title: 'Account Options', href: '/account-options', icon: Settings2Icon },
  { title: 'Log Out', href: '/login', icon: LogOutIcon },
] as const

function App() {
  const navigate = useNavigate()
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme')
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    const shouldUseDark = savedTheme ? savedTheme === 'dark' : prefersDark

    document.documentElement.classList.toggle('dark', shouldUseDark)
    setIsDark(shouldUseDark)
  }, [])

  const toggleTheme = () => {
    setIsDark((currentValue) => {
      const nextValue = !currentValue
      document.documentElement.classList.toggle('dark', nextValue)
      localStorage.setItem('theme', nextValue ? 'dark' : 'light')
      return nextValue
    })
  }

  return (
    <SidebarProvider className="w-full">
      <Sidebar collapsible="none" className="border-r border-sidebar-border h-screen">
        <SidebarHeader className="px-4 py-5">
          <div className="flex items-center gap-3">
            <div className="flex size-9 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
              <ShieldCheckIcon className="size-5" />
            </div>
            <div>
              <p className="text-sm font-semibold tracking-tight">Agile Club</p>
              <p className="text-xs text-sidebar-foreground/70">Member Portal</p>
            </div>
          </div>
        </SidebarHeader>

        <SidebarContent>
          <SidebarGroup className="px-3 py-2">
            <SidebarMenu>
              {navigationItems.map((item, index) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton render={<a href={item.href} />} isActive={index === 0} onClick={() => navigate(item.href)}>
                    <item.icon />
                    <span>{item.title}</span>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroup>
        </SidebarContent>

        <SidebarFooter className="border-t border-sidebar-border p-4">
          <div className="rounded-md bg-sidebar-accent/60 px-3 py-2">
            <p className="text-xs text-sidebar-foreground/70">Signed in as</p>
            <p className="text-sm font-medium">Alex Johnson</p>
          </div>
        </SidebarFooter>
      </Sidebar>

      <SidebarInset className="min-h-svh w-full bg-background">
        <div className="flex h-full flex-col">
          <header className="border-b border-border px-6 py-5">
            <h1 className="text-2xl font-semibold tracking-tight">Home</h1>
          </header>
          <main className="flex-1 px-6 py-6">
            <div className="rounded-xl border border-dashed border-border bg-muted/40 p-8 text-sm text-muted-foreground">
              Main dashboard content goes here.
            </div>
          </main>
        </div>
      </SidebarInset>

      <Button
        size="icon-lg"
        variant="outline"
        aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
        onClick={toggleTheme}
        className="hover:cursor-pointer hover:scale-105 fixed right-5 bottom-5 z-50 rounded-full border-border bg-background/90 shadow-lg backdrop-blur"
      >
        {isDark ? <SunIcon /> : <MoonIcon />}
      </Button>
    </SidebarProvider>
  )
}

export default App
