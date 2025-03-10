import eel

# Initialize the Eel app
eel.init('web')

# Expose a Python function to handle checkbox state
@eel.expose
def handle_checkbox_state(is_checked):
    if is_checked:
        return "Checkbox is checked!"
    else:
        return "Checkbox is unchecked."

# Start the Eel app
eel.start('test.html', size=(400, 300))