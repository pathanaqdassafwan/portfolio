// Advanced Portfolio Website JavaScript with High-Level Animations

// Smooth scrolling for navigation links with custom easing
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - 80;
            const startPosition = window.pageYOffset;
            const distance = targetPosition - startPosition;
            const duration = 1200;
            let start = null;

            function animation(currentTime) {
                if (start === null) start = currentTime;
                const timeElapsed = currentTime - start;
                const progress = Math.min(timeElapsed / duration, 1);
                
                // Custom easing function (ease-in-out-cubic)
                const ease = progress < 0.5 
                    ? 4 * progress * progress * progress 
                    : (progress - 1) * (2 * progress - 2) * (2 * progress - 2) + 1;
                
                window.scrollTo(0, startPosition + distance * ease);
                
                if (timeElapsed < duration) {
                    requestAnimationFrame(animation);
                }
            }
            
            requestAnimationFrame(animation);
        }
    });
});

// Advanced navbar scroll effects
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    const scrollY = window.scrollY;
    
    if (scrollY > 50) {
        navbar.classList.add('scrolled');
        navbar.style.transform = `translateY(${Math.min(scrollY * 0.1, 10)}px)`;
    } else {
        navbar.classList.remove('scrolled');
        navbar.style.transform = 'translateY(0)';
    }
    
    // Parallax effect for navbar background
    navbar.style.backgroundPosition = `center ${scrollY * 0.1}px`;
});

// Active navigation highlighting with smooth transitions
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let currentSection = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 150;
        const sectionHeight = section.clientHeight;
        
        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === currentSection) {
            link.classList.add('active');
        }
    });
});

// Advanced Intersection Observer for animations
const observerOptions = {
    threshold: [0, 0.1, 0.2, 0.3, 0.4, 0.5],
    rootMargin: '0px 0px -100px 0px'
};

const animationObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const element = entry.target;
        const intersectionRatio = entry.intersectionRatio;
        
        if (entry.isIntersecting) {
            // Fade in animation with stagger
            element.style.opacity = Math.min(intersectionRatio * 2, 1);
            element.style.transform = `translateY(${30 * (1 - intersectionRatio * 2)}px) scale(${0.8 + intersectionRatio * 0.2})`;
            
            // Add animated class
            element.classList.add('animated');
            
            // Trigger stagger animations for child elements
            const children = element.querySelectorAll('.stagger-child');
            children.forEach((child, index) => {
                setTimeout(() => {
                    child.style.opacity = '1';
                    child.style.transform = 'translateY(0) scale(1)';
                }, index * 100);
            });
        } else {
            // Reset for re-animation
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px) scale(0.9)';
        }
    });
}, observerOptions);

// Observe all animated elements
document.querySelectorAll('.fade-in, .slide-in, .scale-in').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px) scale(0.9)';
    el.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
    animationObserver.observe(el);
});

// Advanced typing animation for hero section
function advancedTypeWriter(element, text, options = {}) {
    const {
        speed = 80,
        deleteSpeed = 50,
        pauseTime = 2000,
        loop = false,
        cursor = true
    } = options;
    
    let i = 0;
    let isDeleting = false;
    element.innerHTML = '';
    
    // Add cursor
    if (cursor) {
        const cursorSpan = document.createElement('span');
        cursorSpan.className = 'typing-cursor';
        cursorSpan.innerHTML = '|';
        element.appendChild(cursorSpan);
    }
    
    function type() {
        const currentText = isDeleting ? text.substring(0, i - 1) : text.substring(0, i + 1);
        element.firstChild ? element.firstChild.nodeValue = currentText : element.insertAdjacentText('afterbegin', currentText);
        
        if (!isDeleting && i < text.length) {
            i++;
            setTimeout(type, speed + Math.random() * 50);
        } else if (isDeleting && i > 0) {
            i--;
            setTimeout(type, deleteSpeed);
        } else if (!isDeleting && i === text.length) {
            if (loop) {
                setTimeout(() => {
                    isDeleting = true;
                    type();
                }, pauseTime);
            }
        } else if (isDeleting && i === 0) {
            isDeleting = false;
            type();
        }
    }
    
    type();
}

// Removed typing animation for hero name
document.addEventListener('DOMContentLoaded', () => {
    const heroName = document.querySelector('.hero-name');
    // No typing animation applied to hero name to ensure it stays visible
});

// Advanced project card animations
document.querySelectorAll('.project-card').forEach((card, index) => {
    // 3D tilt effect
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(20px) scale(1.02)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px) scale(1)';
    });
    
    // Hover glow effect
    card.addEventListener('mouseenter', () => {
        card.style.boxShadow = '0 30px 80px rgba(102, 126, 234, 0.4), 0 0 50px rgba(102, 126, 234, 0.2)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.boxShadow = '0 15px 40px rgba(102, 126, 234, 0.1)';
    });
});

// Advanced skill card animations
document.querySelectorAll('.skill').forEach((skill, index) => {
    skill.addEventListener('mouseenter', () => {
        // Ripple effect
        const ripple = document.createElement('div');
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(102, 126, 234, 0.3)';
        ripple.style.pointerEvents = 'none';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s linear';
        ripple.style.left = '50%';
        ripple.style.top = '50%';
        ripple.style.width = '20px';
        ripple.style.height = '20px';
        ripple.style.marginLeft = '-10px';
        ripple.style.marginTop = '-10px';
        
        skill.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Parallax scrolling effects
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax');
    
    parallaxElements.forEach(element => {
        const speed = element.dataset.speed || 0.5;
        const yPos = -(scrolled * speed);
        element.style.transform = `translateY(${yPos}px)`;
    });
    
    // Hero image parallax
    const heroImage = document.querySelector('.hero-image');
    if (heroImage && scrolled < window.innerHeight) {
        const speed = 0.3;
        heroImage.style.transform = `translateY(${scrolled * speed}px) scale(${1 + scrolled * 0.0002})`;
    }
});

// Advanced loading animations
window.addEventListener('load', () => {
    // Remove loading class and trigger entrance animations
    document.body.classList.add('loaded');
    
    // Stagger animation for navigation items
    const navItems = document.querySelectorAll('.nav-link');
    navItems.forEach((item, index) => {
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
        }, index * 100);
    });
});

// Mouse cursor trail effect
let mouseTrail = [];
document.addEventListener('mousemove', (e) => {
    mouseTrail.push({ x: e.clientX, y: e.clientY, time: Date.now() });
    
    // Keep only recent trail points
    mouseTrail = mouseTrail.filter(point => Date.now() - point.time < 500);
    
    // Create trail particles occasionally
    if (Math.random() < 0.1) {
        createTrailParticle(e.clientX, e.clientY);
    }
});

function createTrailParticle(x, y) {
    const particle = document.createElement('div');
    particle.style.position = 'fixed';
    particle.style.left = x + 'px';
    particle.style.top = y + 'px';
    particle.style.width = '4px';
    particle.style.height = '4px';
    particle.style.background = 'rgba(102, 126, 234, 0.6)';
    particle.style.borderRadius = '50%';
    particle.style.pointerEvents = 'none';
    particle.style.zIndex = '9999';
    particle.style.animation = 'particle-fade 0.8s ease-out forwards';
    
    document.body.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 800);
}

// Add particle fade animation
const style = document.createElement('style');
style.textContent = `
    @keyframes particle-fade {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(0); opacity: 0; }
    }
    
    @keyframes ripple {
        to { transform: scale(4); opacity: 0; }
    }
    
    .typing-cursor {
        animation: blink 1s infinite;
    }
`;
document.head.appendChild(style);

// Advanced scroll-triggered counters
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const startTime = performance.now();
    
    function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const current = Math.floor(start + (target - start) * easeOutQuart);
        
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        }
    }
    
    requestAnimationFrame(updateCounter);
}

// Initialize counters when visible
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counter = entry.target;
            const target = parseInt(counter.dataset.target) || 100;
            animateCounter(counter, target);
            counterObserver.unobserve(counter);
        }
    });
});

document.querySelectorAll('[data-counter]').forEach(counter => {
    counterObserver.observe(counter);
});

// Advanced form animations (if contact form exists)
document.querySelectorAll('input, textarea').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', function() {
        if (!this.value) {
            this.parentElement.classList.remove('focused');
        }
    });
});

// Performance optimization: Throttle scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Apply throttling to scroll events
window.addEventListener('scroll', throttle(() => {
    // Scroll-dependent animations go here
}, 16)); // ~60fps

// Mobile hamburger menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navItems = document.querySelectorAll('.nav-link');
    const body = document.body;

    // Toggle mobile menu
    function toggleMobileMenu() {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        body.classList.toggle('menu-open');
        
        // Animate hamburger lines
        const lines = hamburger.querySelectorAll('span');
        if (hamburger.classList.contains('active')) {
            lines[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            lines[1].style.opacity = '0';
            lines[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            lines[0].style.transform = 'rotate(0) translate(0, 0)';
            lines[1].style.opacity = '1';
            lines[2].style.transform = 'rotate(0) translate(0, 0)';
        }
    }

    // Close mobile menu
    function closeMobileMenu() {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
        body.classList.remove('menu-open');
        
        const lines = hamburger.querySelectorAll('span');
        lines[0].style.transform = 'rotate(0) translate(0, 0)';
        lines[1].style.opacity = '1';
        lines[2].style.transform = 'rotate(0) translate(0, 0)';
    }

    // Event listeners
    if (hamburger) {
        hamburger.addEventListener('click', toggleMobileMenu);
    }

    // Close menu when clicking on nav links
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            setTimeout(closeMobileMenu, 300); // Delay to allow smooth scroll
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (navLinks && navLinks.classList.contains('active') && 
            !navLinks.contains(event.target) && 
            !hamburger.contains(event.target)) {
            closeMobileMenu();
        }
    });

    // Close menu when pressing escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && navLinks && navLinks.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768 && navLinks && navLinks.classList.contains('active')) {
            closeMobileMenu();
        }
    });
});

console.log('🚀 Advanced Portfolio Animations Loaded Successfully!');
