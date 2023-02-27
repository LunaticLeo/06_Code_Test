// 汉字 [\u4e00-\u9fa5]

const axios = require("axios");

async function main() {
    let str = "";
    for (let i = 0; i < 100; i++) {
        let { data } = await axios.get("https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/stream");

        // console.log(data)

        str += data;
    }
    console.log(str.length);
    console.log(str);
}

main();