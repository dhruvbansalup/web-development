import mongoose from 'mongoose';

const connectDB = async () => {
    try {
        const conn = await mongoose.connect('mongodb://localhost:27017/testDB');
        console.log(`MongoDB Connected: ${conn.connection.host}`);
    } catch (error) {
        console.error(`MongoDB Error: ${error.message}`);
        process.exit(1);
    }
};

export default connectDB;