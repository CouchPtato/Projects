const horoscopes = [
  {
    sign: "aries",
    description: "Today is filled with high energy and excitement. You may find yourself taking the lead in situations that require quick decisions. Trust your instincts, but remember to listen to others as well. Channel your energy toward meaningful goals.",
    luckyNumber: 7,
    compatibility: "Libra",
    mood: "Energetic",
    color: "Red",
    advice: "Take some time for self-reflection amidst all the hustle and bustle."
  },
  {
    sign: "taurus",
    description: "A calm and steady day awaits you. Focus on completing tasks that require patience and persistence. Financial stability may be highlighted, and you could receive unexpected good news related to work.",
    luckyNumber: 5,
    compatibility: "Cancer",
    mood: "Calm",
    color: "Green",
    advice: "Indulge in something you love, like a delicious meal or gardening."
  },
  {
    sign: "gemini",
    description: "Your communication skills are at their peak today. It’s a perfect time to network, share ideas, or write down thoughts that can later turn into great projects. Be mindful of spreading yourself too thin.",
    luckyNumber: 3,
    compatibility: "Aquarius",
    mood: "Happy",
    color: "Yellow",
    advice: "Focus on one important task rather than multitasking excessively."
  },
  {
    sign: "cancer",
    description: "Emotional connections are emphasized today. You may feel nostalgic or want to reconnect with family and friends. Home improvements might also capture your interest. Trust your heart in making decisions.",
    luckyNumber: 2,
    compatibility: "Taurus",
    mood: "Nostalgic",
    color: "White",
    advice: "Spend quality time with loved ones or engage in a creative activity."
  },
  {
    sign: "leo",
    description: "Confidence is your superpower today. You will attract attention effortlessly, making this an excellent day for public speaking, leadership, or creative projects. Use your charisma wisely and inspire others.",
    luckyNumber: 9,
    compatibility: "Aries",
    mood: "Confident",
    color: "Gold",
    advice: "Avoid letting your pride get in the way of meaningful connections."
  },
  {
    sign: "virgo",
    description: "Organization and detail-oriented tasks will come naturally to you today. This is a great day to plan long-term projects or declutter your space. Take care not to be overly critical of yourself or others.",
    luckyNumber: 1,
    compatibility: "Capricorn",
    mood: "Focused",
    color: "Brown",
    advice: "Take breaks to avoid overworking yourself; a short walk can refresh your mind."
  },
  {
    sign: "libra",
    description: "Seek balance in all aspects of your life today. Harmony in relationships will be important, and your natural charm will help smooth over any conflicts. Consider engaging in artistic activities.",
    luckyNumber: 8,
    compatibility: "Gemini",
    mood: "Peaceful",
    color: "Pink",
    advice: "Spend time outdoors or meditate to regain inner balance."
  },
  {
    sign: "scorpio",
    description: "Intense emotions and strong passions guide your day. You may uncover hidden truths or feel a desire to dive deep into complex topics. Trust your intuition, but avoid becoming too secretive.",
    luckyNumber: 4,
    compatibility: "Pisces",
    mood: "Mysterious",
    color: "Black",
    advice: "Engage in deep conversations but remain open to differing opinions."
  },
  {
    sign: "sagittarius",
    description: "A day filled with adventure and new possibilities awaits. Your optimistic outlook will inspire those around you. Travel or learning opportunities may present themselves, so keep an open mind.",
    luckyNumber: 6,
    compatibility: "Leo",
    mood: "Optimistic",
    color: "Purple",
    advice: "Take a bold step toward a goal you've been hesitating to pursue."
  },
  {
    sign: "capricorn",
    description: "Hard work and responsibility are highlighted today. Your disciplined approach will help you achieve long-term goals. Financial decisions made now will likely yield positive results in the future.",
    luckyNumber: 10,
    compatibility: "Virgo",
    mood: "Ambitious",
    color: "Gray",
    advice: "Don't forget to celebrate small victories along the way."
  },
  {
    sign: "aquarius",
    description: "Innovation and creativity are your strengths today. You may come up with unique ideas that challenge conventional thinking. Social connections will play an important role in your success.",
    luckyNumber: 11,
    compatibility: "Libra",
    mood: "Inventive",
    color: "Blue",
    advice: "Share your ideas with like-minded individuals for valuable feedback."
  },
  {
    sign: "pisces",
    description: "Your imagination and intuition are heightened today. It's a perfect time for creative pursuits or deep introspection. Listen to your dreams—they might hold important messages.",
    luckyNumber: 12,
    compatibility: "Scorpio",
    mood: "Dreamy",
    color: "Sea Green",
    advice: "Keep a journal to capture creative ideas as they come to you."
  }
];

function showHoroscope() {
  const selectedSign = document.getElementById('zodiac-select').value;
  const horoscope = horoscopes.find(h => h.sign === selectedSign);

  if (horoscope) {
    document.getElementById('horoscope-output').innerHTML = `
      <div class="horoscope-details">
        <h2>${horoscope.sign.charAt(0).toUpperCase() + horoscope.sign.slice(1)} Horoscope</h2>
        <p><strong>Description:</strong> ${horoscope.description}</p>
        <p><strong>Lucky Number:</strong> ${horoscope.luckyNumber}</p>
        <p><strong>Compatibility:</strong> ${horoscope.compatibility}</p>
        <p><strong>Mood:</strong> ${horoscope.mood}</p>
        <p><strong>Color:</strong> ${horoscope.color}</p>
        <p><strong>Advice:</strong> ${horoscope.advice}</p>
      </div>
    `;
  } else {
    document.getElementById('horoscope-output').textContent =
      'No horoscope available for this zodiac sign.';
  }
}
