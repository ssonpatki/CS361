// client server to initialize new account data (Post to Port 5009/accountDetails)

const readline = require('readline');
const axios = require('axios');
const fs = require('fs');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function promptForUsername() {
  rl.question('Enter username: ', (username) => {
    const folderName = username;

    if (!fs.existsSync(folderName)) {
      fs.mkdirSync(folderName);
      rl.question('Enter password: ', async (password) => {
        try {
          const response = await axios.post('http://localhost:5009/accountDetails', {
            myUsername: username,
            myPassword: password
          });

          console.log('Response:', response.data);
        } catch (err) {
          if (err.response) {
            console.log('Error:', err.response.data.message);
          } else {
            console.log('Error: Could not reach the server');
          }
        } finally {
          rl.close();
        }
      });
    } else {
      console.log('Username already exists. Please try again.');
      promptForUsername(); 
    }
  });
}

promptForUsername();
