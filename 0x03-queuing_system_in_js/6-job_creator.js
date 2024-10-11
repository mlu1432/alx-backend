import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create a job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test notification!',
};

// Create a job in the queue named 'push_notification_code'
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Error creating notification job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
