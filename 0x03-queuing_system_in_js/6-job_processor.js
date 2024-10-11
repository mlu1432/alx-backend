import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send notification
/**
 * Send a notification with phoneNumber and message
 * @param {string} phoneNumber - The phone number to send the notification to
 * @param {string} message - The message to be sent
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
