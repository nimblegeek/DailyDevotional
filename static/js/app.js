document.addEventListener('DOMContentLoaded', () => {
    const moodButtons = document.querySelectorAll('.mood-btn');
    const devotionalDiv = document.getElementById('devotional');
    const quoteElement = document.getElementById('quote');
    const prayerElement = document.getElementById('prayer');

    moodButtons.forEach(button => {
        button.addEventListener('click', () => {
            const mood = button.dataset.mood;
            fetchDevotional(mood);
        });
    });

    async function fetchDevotional(mood) {
        try {
            const response = await fetch(`/api/devotional/${mood}`);
            const data = await response.json();

            quoteElement.textContent = data.quote;
            prayerElement.textContent = data.prayer;
            devotionalDiv.classList.remove('hidden');
        } catch (error) {
            console.error('Error fetching devotional:', error);
            quoteElement.textContent = "An error occurred while fetching the devotional. Please try again.";
            prayerElement.textContent = "";
            devotionalDiv.classList.remove('hidden');
        }
    }
});
