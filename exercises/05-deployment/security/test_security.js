// Test file with security issues
const axios = require('axios');
const { app, hashPassword, generateToken } = require('./advanced_security_tests');
const request = require('supertest');
const assert = require('assert');

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

describe('Security Tests', () => {
    // Test JWT verification
    it('should reject invalid JWT tokens', async () => {
        const response = await request(app)
            .get('/verify-token')
            .set('Authorization', 'invalid-token');
        assert.strictEqual(response.status, 401);
    });

    // Test password hashing
    it('should hash passwords securely', async () => {
        const password = 'testPassword123';
        const hashedPassword = await hashPassword(password);
        assert.notStrictEqual(password, hashedPassword);
        assert.strictEqual(typeof hashedPassword, 'string');
        assert(hashedPassword.startsWith('$2')); // bcrypt hash format
    });

    // Test token generation
    it('should generate secure random tokens', () => {
        const token1 = generateToken();
        const token2 = generateToken();
        assert.strictEqual(typeof token1, 'string');
        assert.strictEqual(token1.length, 64); // 32 bytes in hex = 64 characters
        assert.notStrictEqual(token1, token2);
    });

    // Test rate limiting
    it('should enforce rate limiting on login endpoint', async () => {
        for (let i = 0; i < 6; i++) {
            const response = await request(app)
                .post('/login')
                .send({ username: 'test', password: 'test' });
            if (i < 5) {
                assert.notStrictEqual(response.status, 429);
            } else {
                assert.strictEqual(response.status, 429);
            }
        }
    });

    // Test path traversal protection
    it('should prevent path traversal attacks', async () => {
        const response = await request(app)
            .get('/download/../../../etc/passwd');
        assert.strictEqual(response.status, 400);
    });

    // Test input validation
    it('should validate user input', async () => {
        const response = await request(app)
            .post('/user')
            .send({
                name: '<script>alert("xss")</script>',
                role: 'admin',
                permissions: ['*']
            });
        assert.strictEqual(response.status, 400);
    });
});

module.exports = {
    getUserData,
    displayUserInput,
    hashPassword
}; 