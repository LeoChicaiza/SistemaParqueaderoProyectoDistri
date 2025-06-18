const express = require('express');
const dotenv = require('dotenv');
const ocrRoutes = require('./routes/ocrRoutes');
const connectDB = require('./config/db');

dotenv.config();
connectDB();

const app = express();
app.use(express.json({ limit: '10mb' }));
app.use('/api/ocr', ocrRoutes);

const PORT = process.env.PORT || 5019;
app.listen(PORT, () => console.log(`License Plate Recognition Service running on port ${PORT}`));
