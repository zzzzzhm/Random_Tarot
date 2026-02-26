import { useMemo } from 'react'
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
  const projects = useMemo(
    () => [
      {
        title: 'Job Filtering Agent',
        description:
          'An automated Python-based agentic workflow to scrape, filter, and score job postings based on technical requirements.',
        tags: ['Python', 'Automation', 'LLM', 'Data Pipeline'],
        demo: '', 
        github: 'https://github.com/zzzzzhm/Job_agent',
      },
      {
        title: 'Random Tarot (AWS)',
        description:
          'Full-stack tarot reading application supporting multi-card spreads and interactive interpretations, deployed on AWS.',
        tags: ['React', 'FastAPI', 'AWS', 'Docker'],
        demo: '', 
        github: 'https://github.com/zzzzzhm/Random_Tarot',
      },
      {
        title: 'Tarot Card Generator',
        description:
          'A two-stage layout-to-image pipeline using a fine-tuned Stable Diffusion LoRA to generate a complete 78-card deck.',
        tags: ['Stable Diffusion', 'Python', 'LoRA', 'GenAI'],
        demo: '', 
        github: 'https://github.com/zzzzzhm/tarot-deck-lora', 
      },
    ],
    [],
  )

  const keywords = useMemo(
    () => [
      'Software Engineer',
      'Backend / DevOps',
      'Python',
      'AWS',
      'FastAPI',
      'Docker',
      'UCSD',
      '🧗 Rock Climbing',
      '🏸 Badminton',
      '🥾 Hiking',
      'RAG',
      'Agents',
      'React',
    ],
    [],
  )

  const hobbies = useMemo(
    () => [
      {
        title: '🧗 Rock Climbing',
        description: 'Solving physical puzzles on the wall and pushing my mental limits.',
      },
      {
        title: '🏸 Badminton',
        description: 'Enjoying fast-paced rallies, quick reflexes, and friendly competition.',
      },
      {
        title: '🥾 Hiking',
        description: 'Disconnecting from screens and finding clarity on the trails.',
      },
      {
        title: '🃏 Tarot & Symbolism',
        description: 'Meaning systems and visual storytelling keep my product thinking grounded.',
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
        
        {/* Intro 区域 */}
        <section id="intro" className="portfolio-section intro-section">
          <div className="section-inner">
            <div className="intro-center">
              <h1>Hengmeng Zhuang</h1>
              <p className="intro-subtitle">Building practical AI products with clean engineering and intentional UI.</p>

              <div className="intro-keywords">
                {keywords.map((keyword) => (
                  <span key={keyword}>{keyword}</span>
                ))}
              </div>

              <div className="intro-actions">
                <button type="button" className="primary" onClick={() => scrollToSection('projects')}>
                  Projects
                </button>
                <a href="/resume.pdf" target="_blank" rel="noreferrer">Resume</a>
                <button type="button" onClick={() => scrollToSection('personal')}>
                  Contact
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* Projects 区域 */}
        <section id="projects" className="portfolio-section">
          <div className="section-inner">
            <div className="section-heading">
              <div>
                <h2>Featured Projects</h2>
                <p>3 projects, each with a clear technical story and production intent.</p>
                <div className="project-categories">
                  <span className="active">All</span>
                  <span>Backend / DevOps</span>
                  <span>GenAI</span>
                </div>
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
              <button type="button" onClick={() => scrollToSection('intro')}>
                Back to Top
              </button>
              <button type="button" onClick={() => scrollToSection('personal')}>
                Personal
              </button>
            </div>
          </div>
        </section>

        {/* Personal 区域 */}
        <section id="personal" className="portfolio-section">
          <div className="section-inner">
            <div className="section-heading">
              <div>
                <h2>Personal</h2>
                <p>The human side that shapes how I build and collaborate.</p>
              </div>
              <button type="button" onClick={() => scrollToSection('intro')}>
                Back to Top
              </button>
            </div>

            <div className="hobby-grid">
              {hobbies.map((hobby) => (
                <HobbyCard key={hobby.title} hobby={hobby} />
              ))}
            </div>

            <div id="contact" className="contact-card">
              <h3>Say hi</h3>
              <p>
                Email: <a href="mailto:hezhuang@ucsd.edu">hezhuang@ucsd.edu</a>
              </p>
              <div className="contact-links">
                <a href="https://github.com/zzzzzhm" target="_blank" rel="noreferrer">
                  GitHub
                </a>
                <a href="https://www.linkedin.com/in/hengmeng-zhuang-a91595355/" target="_blank" rel="noreferrer">
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