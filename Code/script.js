// Display the total PHQ-9 score in a colored circle
function displayScore(score) {
    var scoreElement = document.querySelector('#scoreCircle');
    
    // Determine the color based on the score range
    var color;
    if (score >= 0 && score <= 4) {
        color = '#81BE83';
    } else if (score >= 5 && score <= 9) {
        color = '#ECEBBD';
    } else if (score >= 10 && score <= 18) {
        color = '#FEA948';
    } else if (score >= 19 && score <= 27) {
        color = '#B31B1B';
    } else {
        // Handle any other cases or default color
        color = 'black';
    }

    // Apply styles to create a circular element
    scoreElement.style.backgroundColor = color;
    scoreElement.style.width = '50px';  // Adjust the size of the circle as needed
    scoreElement.style.height = '50px';
    scoreElement.style.borderRadius = '50%';
    scoreElement.style.margin = '10px';  // Add some margin for spacing
    scoreElement.style.display = 'flex';
    scoreElement.style.alignItems = 'center';
    scoreElement.style.justifyContent = 'center';
    
    // Create a container for the text content
    var textContainer = document.createElement('div');
    textContainer.style.display = 'flex';
    textContainer.style.alignItems = 'center';
    textContainer.style.justifyContent = 'center';
    textContainer.style.width = '100%';
    textContainer.style.height = '100%';
    
    // Create a span for the numerical score
    var spanElement = document.createElement('span');
    spanElement.style.fontSize = '16px';
    spanElement.style.color = 'white';
    spanElement.textContent = score;

    // Append the span to the text container
    textContainer.appendChild(spanElement);
    
    // Append the text container to the score element
    scoreElement.innerHTML = '';
    scoreElement.appendChild(textContainer);
}

// Attach an event listener to the submit button
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Calculate the total PHQ-9// Calculate the total PHQ-9 score
function calculateScore() {
    var totalScore = 0;
    var questions = document.querySelectorAll('input[type="radio"]:checked');

    questions.forEach(function(question) {
      totalScore += parseInt(question.value);
    });

    return totalScore;
}

// Display the total PHQ-9 score in a colored circle
function displayScore(score) {
    var scoreElement = document.querySelector('#scoreCircle');
    
    // Determine the color based on the score range
    var color;
    if (score >= 0 && score <= 4) {
        color = '#81BE83';
    } else if (score >= 5 && score <= 9) {
        color = '#ECEBBD';
    } else if (score >= 10 && score <= 18) {
        color = '#FEA948';
    } else if (score >= 19 && score <= 27) {
        color = '#B31B1B';
    } else {
        // Handle any other cases or default color
        color = 'black';
    }

    // Apply styles to create a circular element
    scoreElement.style.backgroundColor = color;
    scoreElement.style.width = '50px';  // Adjust the size of the circle as needed
    scoreElement.style.height = '50px';
    scoreElement.style.borderRadius = '50%';
    scoreElement.style.margin = '10px';  // Add some margin for spacing
    scoreElement.style.display = 'flex';
    scoreElement.style.alignItems = 'center';
    scoreElement.style.justifyContent = 'center';
    
    // Create a container for the text content
    var textContainer = document.createElement('div');
    textContainer.style.display = 'flex';
    textContainer.style.alignItems = 'center';
    textContainer.style.justifyContent = 'center';
    textContainer.style.width = '100%';
    textContainer.style.height = '100%';
    
    // Create a span for the numerical score
    var spanElement = document.createElement('span');
    spanElement.style.fontSize = '16px';
    spanElement.style.color = 'white';
    spanElement.textContent = score;

    // Append the span to the text container
    textContainer.appendChild(spanElement);
    
    // Append the text container to the score element
    scoreElement.innerHTML = '';
    scoreElement.appendChild(textContainer);
}

// Attach an event listener to the submit button
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Calculate the total PHQ-9 score
    var score = calculateScore();

    // Display the total PHQ-9 score in a colored circle
    displayScore(score);
});
 score
    var score = calculateScore();

    // Display the total PHQ-9 score in a colored circle
    displayScore(score);
});
