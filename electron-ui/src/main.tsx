import React from 'react'
import ReactDOM from 'react-dom/client'
import { HashRouter, Route, Routes } from 'react-router-dom'
import Home from '../src/pages/Home.tsx';
import './index.css'
import { SidebarProvider } from './components/ui/sidebar.tsx'
import Authenticate from './App.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <HashRouter>
      <SidebarProvider>
        <Routes>
          <Route path="/" element={<Authenticate />} />
          <Route path="/membership" element={<div>Membership Page</div>} />
          <Route path="/home" element={<Home />} />
        </Routes>
      </SidebarProvider>
    </HashRouter>
  </React.StrictMode>,
)

// Only available when running inside Electron with preload bridge.
window.ipcRenderer?.on('main-process-message', (_event, message) => {
  console.log(message)
})
