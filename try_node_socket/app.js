const express = require('express');
const app = express();
const session = require('express-session');
const configRoutes = require('./routes');
const { engine } = require('express-handlebars');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set("views", "./views");

app.use(
    session({
        name: 'StevensMarketPlace',
        secret: "This is a secret.. shhh don't tell anyone",
        saveUninitialized: true,
        resave: false
    })
);

app.use(express.static(__dirname + '/public'));


app.get('*', (req, res, next) => {
    let users = [
        "ygandhi2@stevens.edu",
        "ajayadev@stevens.edu",
        "bkongara@stevens.edu",
        "vkusumur@stevens.edu"
    ];
    res.render("message", { "users": users, "laytou": "main" });
});

configRoutes(app);

app.listen(3000, () => {
    console.log("We've now got a server!");
    console.log('Your routes will be running on http://localhost:3000');
});
