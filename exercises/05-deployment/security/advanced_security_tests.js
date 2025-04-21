// Advanced security test cases
const express = require('express');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const rateLimit = require('express-rate-limit');
const path = require('path');
const bcrypt = require('bcrypt');
const session = require('express-session');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();

// Add body-parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Use environment variable for JWT secret
const JWT_SECRET = process.env.JWT_SECRET || crypto.randomBytes(64).toString('hex');

// Secure JWT verification
app.get('/verify-token', (req, res) => {
    const token = req.headers.authorization;
    try {
        const decoded = jwt.verify(token, JWT_SECRET, { algorithms: ['HS256'] });
        res.json(decoded);
    } catch (err) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

// Secure password hashing using bcrypt
async function hashPassword(password) {
    const saltRounds = 12;
    return await bcrypt.hash(password, saltRounds);
}

// Secure random token generation
function generateToken() {
    return crypto.randomBytes(32).toString('hex');
}

// Rate limiting middleware
const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5 // limit each IP to 5 requests per windowMs
});

// Apply rate limiting to login route
app.post('/login', loginLimiter, (req, res) => {
    const { username, password } = req.body;
    // Implement authentication logic here
    res.json({ success: true });
});

// Secure file download with path validation
app.get('/download/:file', (req, res) => {
    try {
        const requestedPath = req.params.file;
        const downloadsDir = path.join(__dirname, 'downloads');
        const filePath = path.join(downloadsDir, requestedPath);

        // Normalize paths for comparison
        const normalizedFilePath = path.normalize(filePath);
        const normalizedDownloadsDir = path.normalize(downloadsDir);

        // Check for path traversal attempt
        if (!normalizedFilePath.startsWith(normalizedDownloadsDir)) {
            return res.status(400).json({ error: 'Invalid file path' });
        }

        // Check if file exists
        if (!fs.existsSync(filePath)) {
            return res.status(400).json({ error: 'File not found' });
        }

        res.sendFile(filePath);
    } catch (err) {
        res.status(400).json({ error: 'Invalid request' });
    }
});

// Secure data processing with input validation
app.post('/data', (req, res) => {
    try {
        const data = JSON.parse(req.body.data);
        // Add input validation here
        if (!isValidData(data)) {
            return res.status(400).json({ error: 'Invalid data format' });
        }
        processData(data);
        res.json({ success: true });
    } catch (err) {
        res.status(400).json({ error: 'Invalid JSON data' });
    }
});

// Secure user creation with input validation
app.post('/user', (req, res) => {
    try {
        const user = {
            name: sanitizeInput(req.body.name),
            role: validateRole(req.body.role),
            permissions: validatePermissions(req.body.permissions)
        };
        if (!isValidUser(user)) {
            return res.status(400).json({ error: 'Invalid user data' });
        }
        saveUser(user);
        res.json({ success: true });
    } catch (err) {
        res.status(400).json({ error: 'Invalid input' });
    }
});

// Secure API endpoints configuration
const API_ENDPOINTS = {
    prod: 'https://api.production.com',
    staging: 'https://api.staging.com',
    test: 'https://internal-testing.local'
};

// Secure session configuration
app.use(session({
    name: 'session-id',
    secret: process.env.SESSION_SECRET || crypto.randomBytes(64).toString('hex'),
    resave: false,
    saveUninitialized: true,
    cookie: {
        secure: true,
        httpOnly: true,
        sameSite: 'strict',
        maxAge: 24 * 60 * 60 * 1000 // 24 hours
    }
}));

// Helper functions for validation
function isValidData(data) {
    // Basic data validation
    return data && typeof data === 'object';
}

function isValidUser(user) {
    return user &&
        typeof user.name === 'string' &&
        typeof user.role === 'string' &&
        Array.isArray(user.permissions);
}

function sanitizeInput(input) {
    if (typeof input !== 'string') {
        throw new Error('Invalid input type');
    }
    // Remove potentially dangerous characters
    return input.replace(/<[^>]*>/g, '');
}

function validateRole(role) {
    if (typeof role !== 'string') {
        throw new Error('Invalid role type');
    }
    const validRoles = ['user', 'admin', 'moderator'];
    if (!validRoles.includes(role)) {
        throw new Error('Invalid role');
    }
    return role;
}

function validatePermissions(permissions) {
    if (!Array.isArray(permissions)) {
        throw new Error('Invalid permissions type');
    }
    const validPermissions = ['read', 'write', 'delete'];
    const filteredPermissions = permissions.filter(p => 
        typeof p === 'string' && validPermissions.includes(p)
    );
    if (filteredPermissions.length === 0) {
        throw new Error('No valid permissions provided');
    }
    return filteredPermissions;
}

// Mock function for testing
function processData(data) {
    // Implementation
}

// Mock function for testing
function saveUser(user) {
    // Implementation
}

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal server error' });
});

// 404 handler
app.use((req, res) => {
    res.status(400).json({ error: 'Not found' });
});

// Start server if not in test mode
if (process.env.NODE_ENV !== 'test') {
    const port = process.env.PORT || 3000;
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}

module.exports = {
    app,
    hashPassword,
    generateToken,
    API_ENDPOINTS
}; 