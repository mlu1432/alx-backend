import kue from 'kue';

/**
 * Creates push notifications jobs and adds them to the queue.
 * @param {Array} jobs - Array of job data objects.
 * @param {Queue} queue - Kue queue.
 */
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (!err) {
        if (job.id) {
          console.log(`Notification job created: ${job.id}`);
        } else {
          console.log('Notification job created');
        }
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
