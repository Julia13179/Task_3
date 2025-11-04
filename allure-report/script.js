document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.feature-card, .summary-card, .coverage-item, .browser-card');
    elements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        setTimeout(() => {
            element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 100);
    });
    setTimeout(() => {
        const progressBars = document.querySelectorAll('.coverage-fill');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    }, 1000);
    setTimeout(() => {
        const timingValues = document.querySelectorAll('.timing-value');
        timingValues.forEach(elem => {
            const targetTime = parseFloat(elem.getAttribute('data-time'));
            let currentTime = 0;
            const increment = targetTime / 30;
            const timer = setInterval(() => {
                currentTime += increment;
                if (currentTime >= targetTime) {
                    currentTime = targetTime;
                    clearInterval(timer);
                }
                elem.textContent = currentTime.toFixed(1) + ' сек';
            }, 50);
        });
    }, 1500);
});
