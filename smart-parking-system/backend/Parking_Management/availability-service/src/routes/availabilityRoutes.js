const express = require('express');
const router = express.Router();
const { checkAvailabilityByZone, markSlotAvailability } = require('../controllers/availabilityController');

router.get('/:zoneId', checkAvailabilityByZone);
router.post('/update', markSlotAvailability);

module.exports = router;
