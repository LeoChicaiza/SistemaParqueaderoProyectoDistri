const mongoose = require('mongoose');

const controlSchema = new mongoose.Schema({
    vehiclePlate: { type: String, required: true },
    status: { type: String, enum: ['inside', 'outside'], required: true },
    timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Control', controlSchema);
