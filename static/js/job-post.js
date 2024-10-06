const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');

// Trigger the file input when the button is clicked
imagePreview.addEventListener('click', function() {
    fileInput.click();  // Simulate a click on the file input
});

// Event listener for file selection
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            imagePreview.src = e.target.result;  // Set the preview image
            // imagePreview.style.display = 'block';  // Show the image preview
        };

        reader.readAsDataURL(file);  // Read the file as a Data URL for image preview
    } else {
        imagePreview.style.display = 'none';  // Hide the image preview if no valid image is selected
        alert('Please upload a valid image file.');
    }
});