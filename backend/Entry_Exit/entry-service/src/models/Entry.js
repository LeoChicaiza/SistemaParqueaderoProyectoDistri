const mongoose = require('mongoose');

const entrySchema = new mongoose.Schema({
    vehiclePlate: { type: String, required: true },
    entryTime: { type: Date, default: Date.now },
    entryGate: { type: String },
    zoneId: { type: String }
});

module.exports = mongoose.model('Entry', entrySchema);
