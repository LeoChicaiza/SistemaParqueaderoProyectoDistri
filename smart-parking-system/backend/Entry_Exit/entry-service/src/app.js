const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const entryRoutes = require('./routes/entryRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/entry', entryRoutes);

const PORT = process.env.PORT || 5015;
app.listen(PORT, () => console.log(`Entry Service running on port ${PORT}`));
