function handleSubmit(event) {
    event.preventDefault();
    const rollType = document.getElementById('rollType').value;
    const rollno = document.getElementById('rollno').value;
    const name = document.getElementById('name').value;
    const dobDay = document.getElementById('dob-day').value;
    const dobMonth = document.getElementById('dob-month').value;
    const dobYear = document.getElementById('dob-year').value;

    if (rollType && rollno && name && dobDay && dobMonth && dobYear) {
        // Redirect after successful login
        window.location.href = 'dashboard.html';
    } else {
        alert('Please fill out all required fields.');
    }
}


// Student work
const studentWorkBtn = document.getElementById('studentWorkBtn');
const studentWorkMenu = document.getElementById('studentWorkMenu');

studentWorkBtn.addEventListener('click', (event) => {
    event.preventDefault();
    studentWorkMenu.classList.toggle('show');
});

// Close dropdown if clicked outside
document.addEventListener('click', (event) => {
    if (!studentWorkBtn.contains(event.target) && !studentWorkMenu.contains(event.target)) {
        studentWorkMenu.classList.remove('show');
    }
});
