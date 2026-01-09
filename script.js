
// Mobile Menu Toggle
const menuBtn = document.querySelector('.menu-btn');
const navbar = document.querySelector('.navbar');

menuBtn.addEventListener('click', () => {
    navbar.classList.toggle('active');
    // Change icon based on state
    const icon = menuBtn.querySelector('i');
    if(navbar.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }
});

// Close menu when clicking a link
document.querySelectorAll('.navbar a').forEach(link => {
    link.addEventListener('click', () => {
        navbar.classList.remove('active');
        const icon = menuBtn.querySelector('i');
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    });
});

// Smooth scroll implementation is handled by CSS (scroll-behavior: smooth), 
// but we can add an offset for fixed header if needed.

// Form Submission (Demo)
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const btn = this.querySelector('button');
    const originalText = btn.innerText;
    
    btn.innerText = 'Sending...';
    
    setTimeout(() => {
        btn.innerText = 'Message Sent!';
        btn.style.backgroundColor = '#10b981'; // Success green
        
        setTimeout(() => {
            btn.innerText = originalText;
            btn.style.backgroundColor = '';
            this.reset();
        }, 3000);
    }, 1500);
});

// Add scroll animation for header
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
        header.style.padding = '15px 0';
        header.style.backgroundColor = 'rgba(2, 44, 34, 0.98)';
        header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
    } else {
        header.style.padding = '20px 0';
        header.style.backgroundColor = 'rgba(2, 44, 34, 0.95)';
        header.style.boxShadow = 'none';
    }
});
