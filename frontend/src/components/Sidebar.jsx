import { useState } from 'react'
import './Sidebar.css'

export function Sidebar({ activePage, onNavigate }) {
  const [isOpen, setIsOpen] = useState(true)

  const toggleSidebar = () => {
    setIsOpen(!isOpen)
  }

  return (
    <div className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      <button className="sidebar-toggle" onClick={toggleSidebar}>
        {isOpen ? '◀' : '▶'}
      </button>

      <nav className="sidebar-nav">
        <div className="nav-section">
          <button
            className={`nav-item ${activePage === 'portfolio' ? 'active' : ''}`}
            onClick={() => {
              onNavigate('portfolio')
              setIsOpen(false)
            }}
          >
            <span className="nav-icon">👤</span>
            {isOpen && <span>Portfolio</span>}
          </button>

          <button
            className={`nav-item ${activePage === 'tarot' ? 'active' : ''}`}
            onClick={() => {
              onNavigate('tarot')
              setIsOpen(false)
            }}
          >
            <span className="nav-icon">🃏</span>
            {isOpen && <span>Tarot Reading</span>}
          </button>
        </div>
      </nav>
    </div>
  )
}
