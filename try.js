function check(input, datatype) {
    try {
        switch (datatype) {
            case "account":
                if (input == undefined) throw datatype + " should not be none";
                if (typeof (input) != "string") throw datatype + " should be string";
                if (input.length == 0) throw datatype + " should not be empty";
                input = input.trim();
                if (input.length == 0) throw datatype + " should not be all space";
                if (! /^[a-zA-Z0-9]{5,}@stevens.edu*/.test(input)) throw datatype + "not valid";
                return true;
            default:
                throw "should provide a check datatype for input";
        }
    } catch (error) {
        return false;
    }
}

function main() {
    let errors = [], account = "";
    account = check(account, "account") ? account.trim() : errors.push();
    console.log(errors, account)
}

main();