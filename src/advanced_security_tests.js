// Advanced security test cases
const express = require('express');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const app = express();

// JWT with weak secret
const JWT_SECRET = 'my-weak-secret-123';  // Security issue: Weak secret

// Insecure JWT verification
app.get('/verify-token', (req, res) => {
    const token = req.headers.authorization;
    try {
        // Security issue: No algorithm specified
        const decoded = jwt.verify(token, JWT_SECRET);
        res.json(decoded);
    } catch (err) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

// Weak password hashing
function hashPassword(password) {
    // Security issue: Using MD5
    return crypto.createHash('md5').update(password).digest('hex');
}

// Insecure random number generation
function generateToken() {
    // Security issue: Using Math.random()
    return Math.random().toString(36).substring(2);
}

// Missing rate limiting
app.post('/login', (req, res) => {
    // Security issue: No rate limiting
    const { username, password } = req.body;
    authenticateUser(username, password);
});

// Insecure file operations
app.get('/download/:file', (req, res) => {
    const filePath = req.params.file;
    // Security issue: Path traversal vulnerability
    res.sendFile(filePath);
});

// Insecure deserialization
app.post('/data', (req, res) => {
    // Security issue: Unsafe deserialization
    const data = JSON.parse(req.body.data);
    processData(data);
});

// Missing input validation
app.post('/user', (req, res) => {
    const user = {
        // Security issue: No input validation
        name: req.body.name,
        role: req.body.role,
        permissions: req.body.permissions
    };
    saveUser(user);
});

// Hardcoded API endpoints
const API_ENDPOINTS = {
    prod: 'https://api.production.com',
    staging: 'https://api.staging.com',
    test: 'http://internal-testing.local'  // Security issue: HTTP instead of HTTPS
};

// Insecure WebSocket configuration
const ws = new WebSocket('ws://insecure.example.com');  // Security issue: WS instead of WSS

// Insecure cookie configuration
app.use(session({
    name: 'session-id',
    secret: 'keyboard-cat-123',
    cookie: {
        secure: false,  // Security issue: Missing secure flag
        httpOnly: false,  // Security issue: Missing httpOnly flag
        sameSite: null  // Security issue: Missing sameSite attribute
    }
}));

module.exports = {
    app,
    hashPassword,
    generateToken,
    API_ENDPOINTS
}; 