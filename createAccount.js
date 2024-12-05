// server to create new account doc in mongodb (Listening to Port 5009/accountDetails)

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const connectDB = require('./config/db');
const User = require('./models/user');

// Initialize the app
const app = express();

app.use(bodyParser.json());

// Connect to MongoDB
connectDB();

// Login endpoint
app.post('/accountDetails', async (req, res) => {
  const { myUsername, myPassword } = req.body;

  if (!myUsername || !myPassword) {
    return res.status(400).json({ message: 'Username and password are required' });
  }

  try {
    const newUser = new User({ username: myUsername, password: myPassword });
    await newUser.save();
    console.log("1 user document inserted");

    res.status(201).json({ message: 'Account created successfully' }); // Send success response
  } catch (err) {
    console.error('Error:', err);
    res.status(500).json({ message: 'Internal server error' }); // Send error response
  }
});

// Start the server
const PORT = process.env.PORT || 5009;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

