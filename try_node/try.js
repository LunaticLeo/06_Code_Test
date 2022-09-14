var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'taskoo.cs554final@gmail.com',
    pass: 'kuwulmtcraxhplue'
  }
});

// {
//   service: 'gmail',
//   auth: {
//     user: 'liaoyufu1998@gmail.com',
//     pass: 'krbwovvsjmjlitni'
//   }
// }
var mailOptions = {
  from: 'taskoo.cs554final@gmail.com',
  to: 'yliao10@stevens.edu',
  subject: 'Sending Email using Node.js',
  text: 'asdasdfasd'
};

transporter.sendMail(mailOptions, function (error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});