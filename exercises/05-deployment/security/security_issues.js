// Test file with additional security issues
const express = require('express');
const app = express();

// Hardcoded database credentials
const dbConfig = {
    host: 'localhost',
    user: 'admin',
    password: 'super_secret_password_123',
    database: 'users_db'
};

// Insecure password storage
const users = [
    { id: 1, username: 'user1', password: 'password123' },
    { id: 2, username: 'user2', password: 'qwerty123' }
];

// SQL Injection vulnerability with parameterized query
function getUserById(id) {
    // This is still vulnerable because we're using string concatenation
    const query = `SELECT * FROM users WHERE id = '${id}'`;
    return db.query(query);
}

// XSS vulnerability with innerHTML
app.get('/user/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    res.send(`
        <div>
            <h1>User Profile</h1>
            <p>Username: ${user.username}</p>
            <div id="userData">${user.data}</div>
        </div>
    `);
});

// Insecure cookie settings
app.use(session({
    secret: 'very_secret_key',
    cookie: {
        secure: false,
        httpOnly: false,
        maxAge: 31536000000 // 1 year
    }
}));

// Insecure file upload
app.post('/upload', upload.single('file'), (req, res) => {
    const file = req.file;
    // No file type validation
    // No file size validation
    // No sanitization of filename
    const filePath = `/uploads/${file.originalname}`;
    fs.writeFileSync(filePath, file.buffer);
    res.send('File uploaded successfully');
});

// Insecure direct object reference
app.get('/api/admin/users/:id', (req, res) => {
    // No authorization check
    const user = getUserById(req.params.id);
    res.json(user);
});

// Command injection vulnerability
app.get('/ping', (req, res) => {
    const host = req.query.host;
    // Vulnerable to command injection
    const result = require('child_process').execSync(`ping -c 4 ${host}`);
    res.send(result);
});

module.exports = app; 