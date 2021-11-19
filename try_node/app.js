const express = require('express');
const app = express();
const session = require('express-session');
const { engine } = require('express-handlebars');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public/'));
app.engine('handlebars', engine({ "defaultLayout": "main" }));
app.set('view engine', 'handlebars');
app.set("views", "./views");

app.use(
    session({
        name: 'try_node',
        secret: "This is a secret.. shhh don't tell anyone",
        saveUninitialized: true,
        resave: false,
        cookie: { maxAge: 60000 }
    })
);

app.get("*", (req, res, next) => {
    res.render('try', { "title": "try" });
});

app.listen(3000, () => {
    console.log("We've now got a server!");
    console.log('Your routes will be running on http://localhost:3000');
});
