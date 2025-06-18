const mongoose = require('mongoose');

const exitSchema = new mongoose.Schema({
    vehiclePlate: { type: String, required: true },
    exitTime: { type: Date, default: Date.now },
    exitGate: { type: String },
    entryId: { type: String }
});

module.exports = mongoose.model('Exit', exitSchema);
