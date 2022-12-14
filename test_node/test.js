// 汉字 [\u4e00-\u9fa5]

const fs = require('fs');

const url = "C:\\Users\\liaoy\\OneDrive\\Desktop\\Application_Android\\read\\novels\\";
const name = "锁情咒.txt"



fs.readFile(url + name, 'utf8', (err, data) => {

    let fix = "";

    if (err) {
        console.error(err);
        return;
    }

    const lines = data.split("\r\n");

    for(let i = 0; i < lines.length; i++){
        if(lines[i].match(/^（[\u4e00-\u9fa5]+）$/)){
            let content = lines[i].slice(1,-1);
            fix += "第"+content+"章\r\n";
        }else{
            fix += lines[i] + "\r\n";
        }
    }

    fs.writeFile(url + "fixed" + name, fix, err => {
        if (err) {
            console.error(err);
        }
    });
});


