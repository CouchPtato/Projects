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


// Student work drop-down menu
document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("studentWorkBtn");
    const menu = document.getElementById("studentWorkMenu");
    const details = document.getElementById("viewStudentDetails");
    const studentModal = document.getElementById("studentModal");
    const closeModal = document.querySelector(".close");

    button.addEventListener("click", function(event) {
        event.preventDefault();
        menu.classList.toggle("show");
    });

    document.addEventListener("click", function (event) {
        if (!button.contains(event.target) && !menu.contains(event.target)) {
            menu.classList.remove("show");  
        }
    });

    details.addEventListener("click", function (event) {
        event.preventDefault();
        studentModal.style.display = "flex";
    });

    closeModal.addEventListener("click", function () {
        studentModal.style.display = "none";
    });
});

