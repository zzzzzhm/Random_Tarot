import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

// Create axios instance with custom config
const api = axios.create({
  timeout: 10000,
  withCredentials: false
})

function App() {
  const [card, setCard] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [isFlipping, setIsFlipping] = useState(false)

  const drawCard = async () => {
    if (isFlipping) return // Prevent multiple clicks during animation
    
    setLoading(true)
    setError(null)
    setIsFlipping(true)
    
    try {
      console.log('Fetching: /api/tarot/random')
      const response = await api.get('/api/tarot/random')
      console.log('Card received:', response.data)
      
      // Simulate flip animation timing
      await new Promise(resolve => setTimeout(resolve, 600))
      
      setCard(response.data)
    } catch (err) {
      console.error('Error:', err)
      let errMsg = 'Cannot connect to server'
      
      if (err.response) {
        errMsg = `Server error: ${err.response.status}`
      } else if (err.request) {
        errMsg = 'No response from server'
      } else if (err.message) {
        errMsg = `Network error: ${err.message}`
      }
      
      setError(errMsg)
    } finally {
      setLoading(false)
      setIsFlipping(false)
    }
  }

  useEffect(() => {
    drawCard()
  }, [])

  return (
    <div className="container">
      <div className="card-container">
        <h1>🔮 Tarot Reading</h1>
        
        {error && (
          <div className="error">
            ⚠️ {error}
          </div>
        )}

        <div className="flip-container">
          <div 
            className={`flipper ${isFlipping ? 'flipping' : ''} ${card?.is_reversed ? 'reversed' : ''}`}
          >
            {/* Card back (initial state) */}
            <div className="flip-front">
              <div className="card-back">
                <span>🔮</span>
              </div>
            </div>
            
            {/* Card front (after flip) */}
            <div className="flip-back">
              {card ? (
                <div className="card-front">
                  {card.image_url && (
                    <img 
                      src={card.image_url} 
                      alt={card.name}
                      className="card-image"
                    />
                  )}
                </div>
              ) : (
                <div className="card-back">
                  <span>🔮</span>
                </div>
              )}
            </div>
          </div>
        </div>

        {card && (
          <div className="card-info">
            <h2>{card.name}</h2>
            
            <div className="orientation-badge">
              <span className={card.is_reversed ? 'reversed-text' : 'upright-text'}>
                {card.orientation}
              </span>
            </div>

            <p className="description">{card.description}</p>
            
            <div className="meanings">
              <div className="meaning-section">
                <h4>Current Meaning:</h4>
                <p className="current-meaning">{card.current_meaning}</p>
              </div>
              
              <div className="row">
                <div className="meaning-box upright">
                  <h5>Upright:</h5>
                  <p>{card.upright_meaning}</p>
                </div>
                <div className="meaning-box reversed">
                  <h5>Reversed:</h5>
                  <p>{card.reversed_meaning}</p>
                </div>
              </div>
            </div>
          </div>
        )}

        <button 
          onClick={drawCard} 
          disabled={loading || isFlipping}
          className="draw-button"
        >
          {loading || isFlipping ? 'Flipping...' : '🎰 Draw Card'}
        </button>
      </div>
    </div>
  )
}

export default App
