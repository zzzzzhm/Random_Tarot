import { useState, useEffect } from 'react'
import axios from 'axios'
import { QuestionModal } from '../components/QuestionModal'
import './Tarot.css'

const api = axios.create({
  timeout: 10000,
  withCredentials: false
})

export function Tarot() {
  const [spread, setSpread] = useState(1) // 1 or 3 cards
  const [cards, setCards] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [showQuestionModal, setShowQuestionModal] = useState(false)
  const [isFlipping, setIsFlipping] = useState(false)
  const [currentQuestion, setCurrentQuestion] = useState(null)

  const handleSpreadChange = (newSpread) => {
    if (!isFlipping) {
      setSpread(newSpread)
      setCards([])
      setCurrentQuestion(null)
    }
  }

  const handleDrawClick = () => {
    setShowQuestionModal(true)
  }

  const handleQuestionSubmit = async (question) => {
    setCurrentQuestion(question)
    setShowQuestionModal(false)
    await drawCards(question)
  }

  const drawCards = async (question) => {
    if (isFlipping) return

    setLoading(true)
    setError(null)
    setIsFlipping(true)

    try {
      const numCards = spread
      const newCards = []

      // Draw cards one by one
      for (let i = 0; i < numCards; i++) {
        await new Promise(resolve => setTimeout(resolve, 300))

        console.log(`Fetching card ${i + 1}/${numCards}`)
        const response = await api.get('/api/tarot/random')
        console.log(`Card ${i + 1}:`, response.data)
        newCards.push(response.data)
        setCards([...newCards])
      }
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

  return (
    <div className="tarot-container">
      <div className="tarot-header">
        <h1>🃏 Tarot Reading</h1>
        <p className="tarot-subtitle">
          {currentQuestion && `Question: "${currentQuestion}"`}
        </p>
      </div>

      <div className="spread-selector">
        <button
          className={`spread-btn ${spread === 1 ? 'active' : ''}`}
          onClick={() => handleSpreadChange(1)}
          disabled={isFlipping}
        >
          <span className="spread-icon">1️⃣</span>
          <span className="spread-text">Single Card</span>
        </button>
        <button
          className={`spread-btn ${spread === 3 ? 'active' : ''}`}
          onClick={() => handleSpreadChange(3)}
          disabled={isFlipping}
        >
          <span className="spread-icon">3️⃣</span>
          <span className="spread-text">Three Card</span>
        </button>
      </div>

      {error && <div className="error-message">❌ {error}</div>}

      <div className="cards-display">
        {cards.length === 0 && !isFlipping && (
          <div className="empty-state">
            <div className="empty-icon">🎴</div>
            <p>Select a spread and ask your question</p>
          </div>
        )}

        {cards.map((card, index) => (
          <div key={index} className="card-item">
            <div className={`card-wrapper ${card.is_reversed ? 'reversed' : 'upright'}`}>
              {card.image_url ? (
                <img
                  src={card.image_url}
                  alt={card.name}
                  className="card-image"
                />
              ) : (
                <div className="card-placeholder">{card.name}</div>
              )}
            </div>
            <div className="card-info">
              <h3>{card.name}</h3>
              <p className={`orientation ${card.is_reversed ? 'reversed' : 'upright'}`}>
                {card.is_reversed ? '⬇️ Reversed' : '⬆️ Upright'}
              </p>
              <p className="card-meaning">{card.current_meaning}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="tarot-actions">
        <button
          className="btn-draw-main"
          onClick={handleDrawClick}
          disabled={isFlipping}
        >
          {isFlipping ? '✨ Drawing...' : '🎴 Draw Cards'}
        </button>

        {cards.length > 0 && !isFlipping && (
          <button
            className="btn-reset"
            onClick={() => {
              setCards([])
              setCurrentQuestion(null)
            }}
          >
            Clear Reading
          </button>
        )}
      </div>

      <QuestionModal
        isOpen={showQuestionModal}
        onClose={() => setShowQuestionModal(false)}
        onSubmit={handleQuestionSubmit}
        spread={spread}
      />

      {loading && <div className="loading-indicator">🌟 Connecting...</div>}
    </div>
  )
}
