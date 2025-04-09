const jwtDecode = require('jwt-decode');

// Your provided JWT token
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZjM5ZTU5OWNhMmJlN2M1NDQ1ZGJkZiIsInJvbGUiOiJ2ZW5kb3IiLCJpYXQiOjE3NDQwMjMyNTQsImV4cCI6MTc0NDEwOTY1NH0.QFBRt784cXAZ0lQt3o4SSHckFdbJ66vm_qL1WUD02UU';

try {
    const decoded = jwtDecode(token);
    console.log('Decoded Token:', decoded);

    // Check if the token is expired
    const expirationTime = decoded.exp * 1000; // Convert expiration time to milliseconds
    const currentTime = Date.now(); // Get current time in milliseconds

    if (currentTime > expirationTime) {
        console.log('Token has expired');
    } else {
        console.log('Token is valid');
    }
} catch (error) {
    console.error('Invalid Token:', error.message);
}
