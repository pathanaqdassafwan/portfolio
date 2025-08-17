// Particles Animation for Hero Section
document.addEventListener('DOMContentLoaded', function() {
    const heroSection = document.querySelector('.hero-section');
    
    // Create particles container if it doesn't exist
    let particlesContainer = document.querySelector('.hero-particles');
    if (!particlesContainer) {
        particlesContainer = document.createElement('div');
        particlesContainer.className = 'hero-particles';
        heroSection.appendChild(particlesContainer);
    }
    
    // Create particles
    const particleCount = 50; // Number of particles
    
    for (let i = 0; i < particleCount; i++) {
        createParticle(particlesContainer);
    }
    
    // Parallax effect on mouse move
    heroSection.addEventListener('mousemove', function(e) {
        const shapes = document.querySelectorAll('.animated-shape');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        
        shapes.forEach((shape, index) => {
            const speed = 0.03 * (index + 1);
            const x = (mouseX - 0.5) * speed * 100;
            const y = (mouseY - 0.5) * speed * 100;
            
            shape.style.transform = `translate(${x}px, ${y}px)`;
        });
    });
    
    // Add animation class to elements with 'fade-in-up' class after page load
    const animatedElements = document.querySelectorAll('.fade-in-up');
    animatedElements.forEach((element, index) => {
        element.style.animationDelay = `${0.2 * index}s`;
    });
    
    // Initialize skill categories animations
    initSkillsAnimation();
    
    // Scroll animation for section visibility
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
});

// Function to initialize skills animations
function initSkillsAnimation() {
    const skillCategories = document.querySelectorAll('.skill-category');
    
    skillCategories.forEach((category, index) => {
        // Add hover effect animation
        category.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.03)';
            this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.2)';
            
            // Animate skill tags
            const tags = this.querySelectorAll('.skill-tag');
            tags.forEach((tag, tagIndex) => {
                tag.style.transition = 'all 0.3s ease';
                tag.style.transitionDelay = `${tagIndex * 0.05}s`;
                tag.style.transform = 'scale(1.05)';
                tag.style.boxShadow = '0 5px 15px rgba(79, 70, 229, 0.3)';
            });
        });
        
        category.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.1)';
            
            // Reset skill tags
            const tags = this.querySelectorAll('.skill-tag');
            tags.forEach(tag => {
                tag.style.transform = 'scale(1)';
                tag.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
            });
        });
        
        // Add staggered entrance animation
        category.style.opacity = '0';
        category.style.transform = 'translateY(30px)';
        category.style.transition = 'all 0.5s ease';
        category.style.transitionDelay = `${index * 0.1}s`;
    });
    
    // Add intersection observer for skills section
    const skillsObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            skillCategories.forEach(category => {
                category.style.opacity = '1';
                category.style.transform = 'translateY(0)';
            });
            skillsObserver.unobserve(entries[0].target);
        }
    }, { threshold: 0.2 });
    
    const skillsSection = document.querySelector('.skills');
    if (skillsSection) {
        skillsObserver.observe(skillsSection);
    }
}

// Function to create a single particle
function createParticle(container) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    // Random size between 2-6px
    const size = Math.random() * 4 + 2;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    
    // Random position
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.top = `${Math.random() * 100}%`;
    
    // Random opacity
    particle.style.opacity = Math.random() * 0.5 + 0.1;
    
    // Add animation
    const duration = Math.random() * 20 + 10; // 10-30s
    const delay = Math.random() * 5; // 0-5s delay
    
    particle.style.animation = `float ${duration}s ease-in-out ${delay}s infinite alternate`;
    
    container.appendChild(particle);
    
    return particle;
}

// Scroll to section smoothly when clicking on nav links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 70, // Adjust for nav height
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }
});
