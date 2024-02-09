const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 80;

let counter = 0;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// GET route to retrieve the counter value
app.get('/', (req, res) => {
  res.send(`Counter: ${counter}`);
});

// POST route to increment the counter
app.post('/', (req, res) => {
  counter++;
  res.send(`Counter incremented: ${counter}`);
});

// Start the server
app.listen(port, () => {
  console.log(`Counter service is listening on port ${port}`);
});
