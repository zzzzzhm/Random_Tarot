import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

// Create axios instance with custom config
const api = axios.create({
  timeout: 10000,
  withCredentials: false
})

const API_URL = import.meta.env.VITE_API_URL || '/api'

function App() {
  const [card, setCard] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [debug, setDebug] = useState('')

  const drawCard = async () => {
    setLoading(true)
    setError(null)
    setDebug('Connecting...')
    
    try {
      // build URL and log
      const url = `${API_URL}/tarot/random`
      console.log('Fetching:', url)
      setDebug(`GET ${url}`)
      
      const response = await api.get(url)
      console.log('Success:', response.data)
      setCard(response.data)
      setDebug('Connected ✓')
    } catch (err) {
      console.error('Error:', err)
      let errMsg = 'Cannot connect to server'
      
      if (err.response) {
        errMsg = `Server error: ${err.response.status} ${err.response.statusText}`
      } else if (err.request) {
        errMsg = 'No response from server - backend not running?'
      } else if (err.message) {
        errMsg = `Network error: ${err.message}`
      }
      
      setError(errMsg)
      setDebug(`Error: ${err.message}`)
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

        {debug && (
          <div style={{
            background: '#f0f0f0',
            padding: '8px',
            marginBottom: '10px',
            borderRadius: '5px',
            fontSize: '12px',
            color: '#666',
            fontFamily: 'monospace'
          }}>
            {debug}
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
