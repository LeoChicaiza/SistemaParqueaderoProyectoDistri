const express = require('express');
const router = express.Router();
const { recognizePlate } = require('../controllers/ocrController');

router.post('/recognize', recognizePlate);

module.exports = router;
