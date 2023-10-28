function appendToDisplay(value) {
    const display = document.getElementById('display');
    display.value += value;
}

function clearDisplay() {
    const display = document.getElementById('display');
    display.value = '';
}


function callLambdaFunction() {
    const expression = document.getElementById('display').value;

    // Define the URL of your API Gateway endpoint
    const apiUrl = 'https://0ql4wfvxsd.execute-api.ap-south-1.amazonaws.com/dev';

    // Create an object with the data to send to the Lambda function
    const data = {
        expression: expression
    };

    // Make an HTTP POST request to your Lambda function
    fetch(apiUrl, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            // Display the result in the HTML element
            document.getElementById('display').value = JSON.parse(data.body).result;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Modify the calculateResult function to call the Lambda function
function calculateResult() {
    callLambdaFunction();
}
