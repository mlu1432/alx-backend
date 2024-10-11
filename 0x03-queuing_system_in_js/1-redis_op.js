import redis from 'redis';

/**
 * Create a Redis client to connect to the Redis server
 */
const client = redis.createClient();


/**
 * Handle successful connection
 */
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Handle connection errors
 */
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Set a new value for a specific key in Redis
 * @param {string} schoolName - The key to set in Redis
 * @param {string} value - The value to set for the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Get and display the value for a specific key in Redis
 * @param {string} schoolName - The key to get from Redis
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
    } else {
      console.log(result);
    }
  });
}

/**
 * Test the functions
 */
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
