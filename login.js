
const readline = require('readline');
const axios = require('axios');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


rl.question('Enter your username: ', (username) => {
  const dataToAppend = username;

  fs.writeFile('config/username.txt', dataToAppend, (err) => {
    if (err) {
      console.error("Error appending to file:", err);
      return;
    }
  });

  rl.question('Enter your password: ', async (password) => {
    try {

      const response = await axios.post('http://localhost:5008/login', {
        username,
        password
      });

      data = '\nyes'
      fs.appendFile('config/username.txt', data, (err) => {
        if (err) throw err;
      });

      console.log('Response:', response.data);
    } catch (err) {
      data = '\nno'
      fs.appendFile('config/username.txt', data, (err) => {
        if (err) throw err;
      });
      
      if (err.response) {
        console.log('Error:', err.response.data.message);
      } else {
        console.log('Error: Could not reach the server');
      }
    } finally {
      rl.close();
    }
  });
});
