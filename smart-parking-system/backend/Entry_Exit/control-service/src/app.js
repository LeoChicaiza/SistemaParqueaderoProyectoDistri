const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const controlRoutes = require('./routes/controlRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/control', controlRoutes);

const PORT = process.env.PORT || 5018;
app.listen(PORT, () => console.log(`Control Service running on port ${PORT}`));
