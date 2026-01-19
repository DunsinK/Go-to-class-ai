// MongoDB initialization script
db = db.getSiblingDB('go_to_class_ai');

// Create collections
db.createCollection('users');
db.createCollection('classes');
db.createCollection('schedules');

// Create indexes
db.users.createIndex({ "email": 1 }, { unique: true });
db.classes.createIndex({ "name": 1 });
db.schedules.createIndex({ "userId": 1, "date": 1 });

print("MongoDB initialization completed successfully");
