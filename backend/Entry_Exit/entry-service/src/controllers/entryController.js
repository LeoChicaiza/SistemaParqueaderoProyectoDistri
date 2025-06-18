const Entry = require('../models/Entry');

exports.registerEntry = async (req, res) => {
    const { vehiclePlate, entryTime, entryGate, zoneId } = req.body;
    try {
        const entry = new Entry({ vehiclePlate, entryTime, entryGate, zoneId });
        await entry.save();
        res.status(201).json(entry);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getEntriesByPlate = async (req, res) => {
    const { vehiclePlate } = req.params;
    try {
        const entries = await Entry.find({ vehiclePlate }).sort({ entryTime: -1 });
        res.json(entries);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
