const ocrService = require('../utils/ocrService');

exports.recognizePlate = async (req, res) => {
    try {
        const { imageBase64 } = req.body;
        if (!imageBase64) {
            return res.status(400).json({ message: 'Image data is required.' });
        }

        const plate = await ocrService.recognizePlateFromImage(imageBase64);
        res.json({ plate });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
