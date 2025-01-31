async function fetchHoroscope() {
    const zodiacSign = document.getElementById('zodiac-select').value;
    const url = `https://corsproxy.io/?https://aztro.sameerkumar.website/?sign=${zodiacSign}&day=today`;
  
    try {
      const response = await fetch(url, {
        method: 'POST'
      });
  
      if (!response.ok) {
        throw new Error("Error fetching horoscope");
      }
  
      const data = await response.json();
  
      document.getElementById('horoscope-output').innerHTML = `
        <div class="horoscope-details">
          <h2>${zodiacSign.charAt(0).toUpperCase() + zodiacSign.slice(1)} Horoscope</h2>
          <p><strong>Date Range:</strong> ${data.date_range}</p>
          <p><strong>Current Date:</strong> ${data.current_date}</p>
          <p><strong>Description:</strong> ${data.description}</p>
          <p><strong>Mood:</strong> ${data.mood}</p>
          <p><strong>Compatibility:</strong> ${data.compatibility}</p>
          <p><strong>Lucky Color:</strong> ${data.color}</p>
          <p><strong>Lucky Number:</strong> ${data.lucky_number}</p>
          <p><strong>Lucky Time:</strong> ${data.lucky_time}</p>
        </div>
      `;
    } catch (error) {
      console.error('Error fetching horoscope:', error);
      document.getElementById('horoscope-output').textContent =
        'Error fetching horoscope. Please try again later.';
    }
  }
  