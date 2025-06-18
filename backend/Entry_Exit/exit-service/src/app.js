const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const exitRoutes = require('./routes/exitRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/exit', exitRoutes);

const PORT = process.env.PORT || 5016;
app.listen(PORT, () => console.log(`Exit Service running on port ${PORT}`));
