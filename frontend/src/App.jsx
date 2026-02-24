import { useState } from 'react'
import { Sidebar } from './components/Sidebar'
import { Portfolio } from './pages/Portfolio'
import { Tarot } from './pages/Tarot'
import './App.css'

function App() {
  const [activePage, setActivePage] = useState('tarot')

  const renderPage = () => {
    switch (activePage) {
      case 'portfolio':
        return <Portfolio />
      case 'tarot':
        return <Tarot />
      default:
        return <Tarot />
    }
  }

  return (
    <div className="App">
      <Sidebar activePage={activePage} onNavigate={setActivePage} />
      <div className="main-content">
        {renderPage()}
      </div>
    </div>
  )
}

export default App
