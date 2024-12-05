let username = '';

const setUsername = (newUsername) => {
    if (!username) {
        username = newUsername;
    } else {
        console.error('Username is already set and cannot be changed.');
    }
};

const getUsername = () => username;

module.exports = { setUsername, getUsername };
