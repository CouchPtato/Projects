let timerInterval;
let totalTime;

function startTimer() 
{
    clearInterval(timerInterval);

    let hours = +document.getElementById('hours').value || 0;
    let minutes = +document.getElementById('minutes').value || 0;
    let seconds = +document.getElementById('seconds').value || 0;

    totalTime = (hours * 3600) + (minutes * 60) + seconds;

    if (totalTime <= 0) 
    {
        alert('Please enter a valid time!');
        return;
    }

    document.body.classList.remove('game-over');

    runTimer();
}

function runTimer() 
{
    timerInterval = setInterval(() => {
        if (totalTime <= 0) 
        {
            clearInterval(timerInterval);
            document.getElementById('timerDisplay').textContent = 'GAME OVER';
            document.body.classList.add('game-over');
            return;
        }

        let h = Math.floor(totalTime / 3600);
        let m = Math.floor((totalTime % 3600) / 60);
        let s = totalTime % 60;

        document.getElementById('timerDisplay').textContent =
            `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;

        totalTime--;
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}