const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting){
            entry.target.classList.add('show');
        }
    });
    });

const hidddenElements = document.querySelectorAll('.hidden');
hidddenElements.forEach((el) => observer.observe(el));