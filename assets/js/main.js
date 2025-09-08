/* Rotate promotional messages in the ticker */
const PROMO_MESSAGES = [
  "Fall Special: 10% off driveways!",
  "Free sealcoating with large paving projects.",
  "We haul gravel, topsoil & more!"
];

let promoIndex = 0;
function rotatePromo() {
  const promoEl = document.getElementById('promo-message');
  if (!promoEl) return;
  promoEl.textContent = PROMO_MESSAGES[promoIndex];
  promoIndex = (promoIndex + 1) % PROMO_MESSAGES.length;
}
setInterval(rotatePromo, 10000);
rotatePromo();

/* Testimonials slider */
document.addEventListener('DOMContentLoaded', () => {
  const testimonials = document.querySelectorAll('.testimonial-item');
  if (testimonials.length > 0) {
    let testimonialIndex = 0;
    function showTestimonial() {
      testimonials.forEach((el, i) => {
        el.classList.toggle('active', i === testimonialIndex);
      });
      testimonialIndex = (testimonialIndex + 1) % testimonials.length;
    }
    showTestimonial();
    setInterval(showTestimonial, 8000);
  }

  /* Before & after slider */
  const rangeInput = document.getElementById('beforeAfterRange');
  const afterContainer = document.getElementById('after-img');
  if (rangeInput && afterContainer) {
    rangeInput.addEventListener('input', function () {
      const val = this.value;
      afterContainer.style.width = val + '%';
    });
  }

  /* FAQ accordion */
  document.querySelectorAll('.faq-item h3').forEach((header) => {
    header.addEventListener('click', () => {
      const answer = header.nextElementSibling;
      if (answer.style.display === 'block') {
        answer.style.display = 'none';
      } else {
        answer.style.display = 'block';
      }
    });
  });

  /* Gallery lightbox */
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const lightImg = lightbox.querySelector('img');
    document.querySelectorAll('.gallery-grid img').forEach((img) => {
      img.addEventListener('click', () => {
        lightImg.src = img.src;
        lightbox.style.display = 'flex';
      });
    });
    lightbox.addEventListener('click', () => {
      lightbox.style.display = 'none';
    });
  }
});