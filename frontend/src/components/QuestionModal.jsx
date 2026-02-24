import { useState } from 'react'
import './QuestionModal.css'

export function QuestionModal({ isOpen, onClose, onSubmit, spread }) {
  const [question, setQuestion] = useState('')

  const handleSubmit = () => {
    if (question.trim()) {
      onSubmit(question)
      setQuestion('')
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && question.trim()) {
      handleSubmit()
    }
  }

  if (!isOpen) return null

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <h2 className="modal-title">
          {spread === 1 ? '🃏 Single Card Reading' : '🃏 Three Card Spread'}
        </h2>
        
        <p className="modal-subtitle">
          Think deeply about your question while drawing
        </p>

        <div className="modal-input-group">
          <label htmlFor="question">What is your question?</label>
          <textarea
            id="question"
            className="modal-textarea"
            placeholder="Ask what's on your mind..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={handleKeyPress}
            autoFocus
          />
        </div>

        <div className="modal-actions">
          <button className="btn-cancel" onClick={onClose}>
            Cancel
          </button>
          <button
            className="btn-draw"
            onClick={handleSubmit}
            disabled={!question.trim()}
          >
            Draw Cards ✨
          </button>
        </div>
      </div>
    </div>
  )
}
