const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const connectDB = require('./config/db');
const User = require('./models/user');

// Initialize the app
const app = express();

app.use(bodyParser.json());

// Connect to MongoDB
connectDB();

// JWT secret (in your app, store this securely in an environment variable)
const JWT_SECRET = 'your_jwt_secret_key';

// Login endpoint
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ message: 'Username and password are required' });
  }

  try {
    // Check if the user exists in the database
    const user = await User.findOne({ username });

    if (!user || user.password !== password) {
      return res.status(401).json({ message: 'No user account information found' });
    }

    // If credentials are valid, create a JWT token
    const token = jwt.sign({ username: user.username }, JWT_SECRET, { expiresIn: '1h' });

    // Send back the token in the Authorization header
    res.status(200).json({ message: 'Authenticated successfully', Authorization: token });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 5008;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
