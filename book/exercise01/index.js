const express = require('express'); // Require express module
const app = express() // calls express function to start new Express app
const path = require('path');
app.use(express.static('public'));

app.listen(3000,()=>{
    console.log('App listening on port 3000');
});

app.get('/', (req, res)=>{
    res.sendFile(path.resolve(__dirname, 'index.html'));
});

app.get('/about', (req, res)=>{
    res.sendFile(path.resolve(__dirname, 'about.html'));
});

app.get('/contact', (req, res)=>{
    res.sendFile(path.resolve(__dirname, 'contact.html'));
});


/*

// Separating BARE Node.js server code from express code

const http = require('http');
const fs = require('fs');
const homePage = fs.readFileSync('index.html');
const aboutPage = fs.readFileSync('about.html');
const contactPage = fs.readFileSync('contact.html');
const notFoundPage = fs.readFileSync('not-found.html');

const server = http.createServer((req, res) => {
    
    if (req.url === '/about')
        res.end(aboutPage);
    else if (req.url === '/contact')
        res.end(contactPage);
    else if (req.url === '/')
        res.end(homePage);
    else {
        res.writeHead(404)
        res.end(notFoundPage);
    }
})

server.listen(3000); */