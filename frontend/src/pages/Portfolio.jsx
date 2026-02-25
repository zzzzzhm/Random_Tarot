import { useMemo, useState } from 'react'
import './Portfolio.css'

function ProjectCard({ project }) {
  return (
    <article className="project-card">
      <div className="project-card-header">
        <h3>{project.title}</h3>
        <div className="project-links">
          {project.demo && (
            <a href={project.demo} target="_blank" rel="noreferrer">
              Demo
            </a>
          )}
          {project.github && (
            <a href={project.github} target="_blank" rel="noreferrer">
              GitHub
            </a>
          )}
        </div>
      </div>
      <p>{project.description}</p>
      <div className="project-tags">
        {project.tags.map((tag) => (
          <span key={tag}>{tag}</span>
        ))}
      </div>
    </article>
  )
}

function HobbyCard({ hobby }) {
  return (
    <article className="hobby-card">
      <h3>{hobby.title}</h3>
      <p>{hobby.description}</p>
    </article>
  )
}

export function Portfolio() {
  const [aboutOpen, setAboutOpen] = useState(false)

  const projects = useMemo(
    () => [
      {
        title: 'Random Tarot (AWS + FastAPI + CloudFront)',
        description:
          'Tarot draw API + web UI. Images via CloudFront with reliable seeding and cleanup for 78 cards.',
        tags: ['FastAPI', 'AWS', 'CloudFront', 'SQLAlchemy', 'React'],
        demo: '#',
        github: 'https://github.com/zzzzzhm/Random_Tarot',
      },
      {
        title: 'AI Chat Assistant (Agent + RAG)',
        description:
          'Lightweight assistant with memory and tool calling for practical daily workflows.',
        tags: ['Python', 'Agents', 'RAG', 'LLM'],
        demo: '#',
        github: '#',
      },
      {
        title: 'Symbolic Music Generation',
        description:
          'Markov and Transformer experiments evaluated with perplexity and pitch-distribution metrics.',
        tags: ['PyTorch', 'MIDI', 'Transformer'],
        demo: '#',
        github: '#',
      },
    ],
    [],
  )

  const hobbies = useMemo(
    () => [
      {
        title: 'Tarot and Symbolism',
        description: 'Meaning systems and visual storytelling keep my product thinking grounded.',
      },
      {
        title: 'Music Generation',
        description: 'I like turning patterns into sound with model-driven experimentation.',
      },
      {
        title: 'Strategy Games',
        description: 'Constraint-based decision making sharpens engineering tradeoff judgement.',
      },
      {
        title: 'Journaling in Cafes',
        description: 'Writing helps me clarify product direction and execution details.',
      },
    ],
    [],
  )

  const scrollToSection = (sectionId) => {
    const target = document.getElementById(sectionId)
    if (!target) return
    target.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <div className="portfolio-container">
      <div className="portfolio-scroll">
        <section id="hero" className="portfolio-section hero-section">
          <div className="section-inner">
            <header className="hero-top">
              <p>
                <span>Zhiming</span> AI Engineer
              </p>
              <nav>
                <button type="button" onClick={() => scrollToSection('projects')}>
                  Projects
                </button>
                <button type="button" onClick={() => scrollToSection('personal')}>
                  Personal
                </button>
              </nav>
            </header>

            <div className="hero-center">
              <div className="hero-badge">AI systems | calm UI | shipped projects</div>
              <h1>
                I build practical AI products
                <br />
                with clean, intentional design.
              </h1>
              <p>
                Full-stack + AI/ML. APIs, data pipelines, deployment, and interfaces that feel focused.
              </p>

              <div className="hero-actions">
                <button type="button" className="primary" onClick={() => scrollToSection('projects')}>
                  Projects
                </button>
                <a href="https://github.com/zzzzzhm" target="_blank" rel="noreferrer">
                  GitHub
                </a>
                <a href="/resume.pdf">Resume</a>
              </div>
            </div>

            <div className="hero-bottom">
              <div
                className="about-trigger"
                onMouseEnter={() => setAboutOpen(true)}
                onMouseLeave={() => setAboutOpen(false)}
              >
                <button type="button" onClick={() => scrollToSection('personal')}>
                  <span className="about-icon">v</span>
                  <span>
                    <strong>About me</strong>
                    <small>go to Personal</small>
                    <em className={aboutOpen ? 'open' : ''}>
                      I enjoy end-to-end systems and creative AI projects with strong engineering quality.
                    </em>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </section>

        <section id="projects" className="portfolio-section">
          <div className="section-inner">
            <div className="section-heading">
              <div>
                <h2>Featured Projects</h2>
                <p>3 projects, each with a clear technical story.</p>
              </div>
              <button type="button" onClick={() => scrollToSection('personal')}>
                Next
              </button>
            </div>

            <div className="project-grid">
              {projects.map((project) => (
                <ProjectCard key={project.title} project={project} />
              ))}
            </div>

            <div className="section-nav">
              <button type="button" onClick={() => scrollToSection('hero')}>
                Back to Hero
              </button>
              <button type="button" onClick={() => scrollToSection('personal')}>
                Personal
              </button>
            </div>
          </div>
        </section>

        <section id="personal" className="portfolio-section">
          <div className="section-inner">
            <div className="section-heading">
              <div>
                <h2>Personal</h2>
                <p>The human side that shapes how I build and collaborate.</p>
              </div>
              <button type="button" onClick={() => scrollToSection('hero')}>
                Back
              </button>
            </div>

            <div className="hobby-grid">
              {hobbies.map((hobby) => (
                <HobbyCard key={hobby.title} hobby={hobby} />
              ))}
            </div>

            <div className="contact-card">
              <h3>Say hi</h3>
              <p>
                Email: <a href="mailto:hezhuang@ucsd.edu">hezhuang@ucsd.edu</a>
              </p>
              <div className="contact-links">
                <a href="https://github.com/zzzzzhm" target="_blank" rel="noreferrer">
                  GitHub
                </a>
                <a href="https://www.linkedin.com/" target="_blank" rel="noreferrer">
                  LinkedIn
                </a>
              </div>
            </div>

            <footer>{`Copyright ${new Date().getFullYear()} | React | scroll-snap`}</footer>
          </div>
        </section>
      </div>
    </div>
  )
}
