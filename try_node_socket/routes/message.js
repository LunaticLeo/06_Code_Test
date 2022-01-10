const express = require('express');
const router = express.Router();

router.post('/send', async (req, res) => {
    res.status(200).json({ "title": "send" });
});

module.exports = router;