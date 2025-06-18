const Control = require('../models/Control');

exports.checkVehicleStatus = async (req, res) => {
    const { vehiclePlate } = req.params;
    try {
        const lastRecord = await Control.findOne({ vehiclePlate }).sort({ timestamp: -1 });
        if (!lastRecord) {
            return res.json({ status: 'not_found' });
        }
        res.json({ status: lastRecord.status, timestamp: lastRecord.timestamp });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.updateVehicleStatus = async (req, res) => {
    const { vehiclePlate, status } = req.body;
    try {
        const newRecord = new Control({ vehiclePlate, status });
        await newRecord.save();
        res.status(201).json(newRecord);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
