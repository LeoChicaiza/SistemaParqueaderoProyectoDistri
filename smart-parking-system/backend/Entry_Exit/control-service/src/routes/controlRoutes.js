const express = require('express');
const router = express.Router();
const { checkVehicleStatus, updateVehicleStatus } = require('../controllers/controlController');

router.get('/:vehiclePlate', checkVehicleStatus);
router.post('/', updateVehicleStatus);

module.exports = router;
