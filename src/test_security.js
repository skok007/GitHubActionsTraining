// Test file with security issues
const axios = require('axios');

// Hardcoded credentials (this is intentional for testing)
const API_KEY = 'sk_test_123456789';
const AWS_SECRET = 'AKIAIOSFODNN7EXAMPLE';

// SQL Injection vulnerability
function getUserData(userId) {
    const query = `SELECT * FROM users WHERE id = ${userId}`;
    return db.query(query);  // Vulnerable to SQL injection
}

// Insecure direct object reference
app.get('/api/user/:id', (req, res) => {
    const userData = getUserData(req.params.id);
    res.json(userData);
});

// Potential XSS vulnerability
function displayUserInput(input) {
    document.getElementById('output').innerHTML = input;  // Vulnerable to XSS
}

// Weak cryptography
const crypto = require('crypto');
function hashPassword(password) {
    return crypto.createHash('md5').update(password).digest('hex');  // MD5 is weak
}

// Insecure cookie settings
app.use(session({
    secret: 'keyboard cat',
    cookie: { secure: false }  // Missing secure flag
}));

module.exports = {
    getUserData,
    displayUserInput,
    hashPassword
}; 