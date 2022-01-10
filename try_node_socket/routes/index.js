const messageRoutes = require('./message');

const constructorMethod = (app) => {

    app.use('/message', messageRoutes);

    app.use('*', (req, res) => {
        res.status(404).json({ error: 'Page Not found' });
    });
};

module.exports = constructorMethod;