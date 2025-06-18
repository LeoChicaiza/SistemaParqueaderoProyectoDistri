const express = require('express');
const router = express.Router();
const { registerEntry, getEntriesByPlate } = require('../controllers/entryController');

router.post('/', registerEntry);
router.get('/:vehiclePlate', getEntriesByPlate);

module.exports = router;
