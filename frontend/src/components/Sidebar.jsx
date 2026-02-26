import './Sidebar.css'

export function Sidebar({ activePage, onNavigate }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">HZ&apos;s Space</div>

      <nav className="sidebar-nav">
        <div className="nav-section">
          <p className="nav-heading">Pages</p>
          <button
            className={`nav-item ${activePage === 'portfolio' ? 'active' : ''}`}
            onClick={() => onNavigate('portfolio')}
          >
            <span>Portfolio</span>
          </button>
        </div>

        <div className="nav-section">
          <p className="nav-heading">Projects</p>
          <button
            className={`nav-item ${activePage === 'tarot' ? 'active' : ''}`}
            onClick={() => onNavigate('tarot')}
          >
            <span>Tarot</span>
          </button>
        </div>
      </nav>
    </aside>
  )
}

