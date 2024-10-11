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
 * Store the hash values using hset
 */
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

/**
 * Retrieve and display the hash values using hgetall
 */
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
  } else {
    console.log(result);
  }
});
