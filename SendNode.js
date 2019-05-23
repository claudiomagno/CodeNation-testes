var fs = require("fs");
var request = require("request");

var options = { method: 'POST',
  url: 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution',
  qs: { token: 'e5b63083899cbd9feb21e0716ce712ae00890a57' },
  headers: 
   { 
     'cache-control': 'no-cache',
     'content-type': 'multipart/form-data'  
  },
  formData: 
   { answer: 
      { value: fs.createReadStream("answer.json"),
        options: { filename: 'answer.json', contentType: null }
      } 
   } 
 };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  //console.log(response);
  console.log(body);
});



/*

------------------------------------------------------------------------------------------

var formData = {
  answer: fs.createReadStream('answer.json'),
};

headers= 
   { 
     'cache-control': 'no-cache',
     'content-type': 'multipart/form-data'  
  }
 
request.post({url:'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=e5b63083899cbd9feb21e0716ce712ae00890a57', formData: formData,headers:headers}, function(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});

*/
