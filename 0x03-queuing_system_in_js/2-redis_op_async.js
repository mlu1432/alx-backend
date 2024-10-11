import redis from 'redis';
import {promisify} from 'util';


/**
 * Create a Redis client to connect to the Redis server
 */
const client = redis.createClient();


/**
 * Handle successful connection
 */
client.on('connect', () =>{
	console.log('Redis connected to the server');
});


/**
 * Handle connection errors
 */
console.log('Redis client not connected to the server: ${err.message}');


/**
 * Set a new value for a specific key in Redis
 * @param {string} schoolName - The key to set in Redis
 * @param {string} value - The value to set for the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Get and display the value for a specific key in Redis using async/await
 * @param {string} schoolName - The key to get from Redis
 */
async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

/**
 * Test the functions
 */
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100'); 
displaySchoolValue('HolbertonSanFrancisco');
