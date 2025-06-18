const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const availabilityRoutes = require('./routes/availabilityRoutes');

dotenv.config();
connectDB();

const app = express();
app.use(express.json());
app.use('/api/availability', availabilityRoutes);

const PORT = process.env.PORT || 5010;
app.listen(PORT, () => console.log(`Availability Service running on port ${PORT}`));
