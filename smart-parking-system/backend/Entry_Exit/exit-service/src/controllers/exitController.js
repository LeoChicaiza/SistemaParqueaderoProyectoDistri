const Exit = require('../models/Exit');

exports.registerExit = async (req, res) => {
    const { vehiclePlate, exitTime, exitGate, entryId } = req.body;
    try {
        const exit = new Exit({ vehiclePlate, exitTime, exitGate, entryId });
        await exit.save();
        res.status(201).json(exit);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getExitsByPlate = async (req, res) => {
    const { vehiclePlate } = req.params;
    try {
        const exits = await Exit.find({ vehiclePlate }).sort({ exitTime: -1 });
        res.json(exits);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
