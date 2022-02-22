const data = require("./try2").data;

const data2 = require("./try2").data2;

console.log(data);
console.log(data2);





// var nodemailer = require('nodemailer');

// var transporter = nodemailer.createTransport({
//   service: 'gmail',
//   auth: {
//     user: 'liaoyufu1998@gmail.com',
//     pass: 'krbwovvsjmjlitni'
//   }
// });

// var mailOptions = {
//   from: 'liaoyufu1998@gmail.com',
//   to: 'yliao10@stevens.edu',
//   subject: 'Sending Email using Node.js',
//   text: 'That was easy!'
// };

// transporter.sendMail(mailOptions, function(error, info){
//   if (error) {
//     console.log(error);
//   } else {
//     console.log('Email sent: ' + info.response);
//   }
// });