import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [card, setCard] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const drawCard = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.get(`${API_URL}/api/tarot/random`)
      setCard(response.data)
    } catch (err) {
      setError('Cannot connect to server: ' + err.message)
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    drawCard()
  }, [])

  return (
    <div className="container">
      <div className="card-container">
        <h1>🔮 Tarot Card</h1>
        
        {error && (
          <div className="error">
            ⚠️ {error}
          </div>
        )}

        {card && (
          <div className="tarot-card">
            {card.image_url && (
              <img 
                src={card.image_url} 
                alt={card.name}
                className="card-image"
              />
            )}
            <h2>{card.name}</h2>
            <p className="description">{card.description}</p>
            {card.meaning && (
              <div className="meaning">
                <strong>Meaning:</strong> {card.meaning}
              </div>
            )}
          </div>
        )}

        <button 
          onClick={drawCard} 
          disabled={loading}
          className="draw-button"
        >
          {loading ? 'Drawing...' : '✨ Draw Another'}
        </button>
      </div>
    </div>
  )
}

export default App
