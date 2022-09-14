const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(__dirname+'/front/'));

app.get('/user', (req, res) => {
    console.log(req.query);
    res.sendFile('chat.html');
});



app.use('*', (req, res) => {
    res.status(404).json({ error: 'Page Not found' });
});

app.listen(3000, () => {
    console.log("We've now got a server!");
    console.log('Your routes will be running on http://localhost:3000');
});

// const server = require('http').createServer(app);
// const io = require('socket.io')(server);
// io.on('connection', () => { /* … */ });
// server.listen(4000, () => {
//     console.log(`Chat Server listening to port 4000...`);
// });