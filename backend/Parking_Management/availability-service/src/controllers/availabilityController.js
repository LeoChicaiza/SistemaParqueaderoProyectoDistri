const Slot = require('../models/Slot');

exports.checkAvailabilityByZone = async (req, res) => {
    const { zoneId } = req.params;
    try {
        const availableSlots = await Slot.find({ zoneId, available: true });
        res.json({ availableSlots: availableSlots.length });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.markSlotAvailability = async (req, res) => {
    const { slotId, available } = req.body;
    try {
        const updated = await Slot.findByIdAndUpdate(slotId, { available }, { new: true });
        res.json(updated);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
