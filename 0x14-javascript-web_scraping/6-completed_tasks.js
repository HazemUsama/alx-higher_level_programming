#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err || res.statusCode !== 200) return;
  const tasks = JSON.parse(body);
  const completedTask = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTask[task.userId]) {
        completedTask[task.userId]++;
      } else {
        completedTask[task.userId] = 1;
      }
    }
  });
  console.log(completedTask);
});
