var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'liaoyufu1998@gmail.com',
    pass: 'krbwovvsjmjlitni'
  }
});

var mailOptions = {
  from: 'liaoyufu1998@gmail.com',
  to: 'yliao10@stevens.edu',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});