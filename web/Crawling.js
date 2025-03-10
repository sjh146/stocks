$(function() {
     // Function to send checkbox state to Python
     async function sendCheckboxState() {
        const checkbox = document.getElementById("MarketPrice");
        const isChecked = checkbox.checked;

        // Call Python function with checkbox state
        const response = await eel.handle_checkbox_state(isChecked)();
        document.getElementById("output").innerText = response;
    }
   
});