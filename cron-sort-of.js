const schedule = require('node-schedule');

console.log("This could work..")

const job = schedule.scheduleJob('* * * * *', function(){
  const d = new Date();
  console.log('Cron triggered @', d);
});


