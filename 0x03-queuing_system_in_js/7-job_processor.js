import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs in the queue named 'push_notification_code_2' with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
