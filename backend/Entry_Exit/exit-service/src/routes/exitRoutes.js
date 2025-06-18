const express = require('express');
const router = express.Router();
const { registerExit, getExitsByPlate } = require('../controllers/exitController');

router.post('/', registerExit);
router.get('/:vehiclePlate', getExitsByPlate);

module.exports = router;
