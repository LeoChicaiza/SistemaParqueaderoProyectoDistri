const express = require('express');
const router = express.Router();
const { register, login } = require('../controllers/authController');
const authMiddleware = require('../middlewares/authMiddleware');

router.post('/register', register);
router.post('/login', login);
router.get('/protected', authMiddleware, (req, res) => {
    res.json({ message: 'You have accessed a protected route', user: req.user });
});

module.exports = router;
