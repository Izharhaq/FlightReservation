document.addEventListener("DOMContentLoaded", function() {
    const passengerReservationButton = document.getElementById("passengerReservationButton");
    const passengerDataDiv = document.getElementById("passengerData");

    passengerReservationButton.addEventListener("click", function() {
        fetchPassengerData();
    });

    function fetchPassengerData() {
        fetch('http://localhost:8000/flightServices/passengers')
            .then(response => {
                if (!response.ok) {
                    throw new Error('HTTP status ' + response.status + ': ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Render the JSON data
                renderPassengerData(data);
            })
            .catch(error => {
                console.error('Error fetching passenger data:', error);
                passengerDataDiv.textContent = 'Error fetching passenger data: ' + error.message;
            });
    }

    function renderPassengerData(data) {
        // Clear existing content
        passengerDataDiv.innerHTML = '';

        // Display JSON data in the div
        const preElement = document.createElement('pre');
        preElement.textContent = JSON.stringify(data, null, 2);
        passengerDataDiv.appendChild(preElement);
    }
});
